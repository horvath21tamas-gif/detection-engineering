"""Constructive test events ("witnesses") for compiled Wazuh rules.

For every Wazuh rule we build an event that must trigger it. The same events are
used (a) by the unit tests, to prove the rules can fire, and (b) as test vectors
for ``wazuh-logtest`` on the real manager before a deployment goes live.
"""

from __future__ import annotations

import json
import re
from itertools import product

import regex

from .emit import WazuhRule
from .logic import KEYWORD_FIELD, Atom, Pat

SYSMON_EID = {
    61603: 1, 61604: 2, 61605: 3, 61606: 4, 61607: 5, 61608: 6, 61609: 7, 61610: 8, 61611: 9,
    61612: 10, 61613: 11, 61614: 12, 61615: 13, 61616: 14, 61617: 15, 61644: 16, 61645: 17,
    61646: 18, 61647: 19, 61648: 20, 61649: 21, 61650: 22, 61651: 23, 61652: 24, 61653: 25,
    61654: 26, 61655: 255, 61600: 1,
}
BASE_SYSTEM = {
    "win.system.computer": "WIN-TEST.lab.local",
    "win.system.severityValue": "INFORMATION",
}
CHANNELS = {
    61600: ("Microsoft-Windows-Sysmon/Operational", "Microsoft-Windows-Sysmon"),
    60001: ("Security", "Microsoft-Windows-Security-Auditing"),
    60002: ("System", "Service Control Manager"),
    60003: ("Application", "Application"),
    60005: ("Microsoft-Windows-Windows Defender/Operational", "Microsoft-Windows-Windows Defender"),
    60000: ("Microsoft-Windows-PowerShell/Operational", "Microsoft-Windows-PowerShell"),
}


def _literal_from_regex(rx: str) -> str:
    """Turn simple anchored regexes like ^Microsoft-Windows-X/Operational$ into text."""
    rx = rx.removeprefix("^").removesuffix("$")
    return re.sub(r"\\(.)", r"\1", rx)


def _compose(pats: list[Pat]) -> list[str]:
    first = [p for p in pats if p.prefix]
    last = [p for p in pats if p.suffix and not p.prefix]
    mid = [p for p in pats if not p.prefix and not p.suffix]
    text = " ".join(p.sample for p in first + mid + last)
    # an exact (prefix+suffix) pattern must stand alone
    return [text, "".join(p.sample for p in first + mid + last)]


def _field_value(name: str, atoms: list[Atom], pattern: str) -> str | None:
    pos = [a for a in atoms if not a.neg]
    if not pos:
        candidates = ["benign-value", "Z:\\benign\\value.txt"]
    else:
        candidates = []
        choices = [[p for p in a.alts if p.sample is not None] for a in pos]
        if any(not c for c in choices):
            return None
        for combo in list(product(*choices))[:64]:
            candidates += _compose(list(combo))
    for cand in candidates:
        if regex.search(pattern, cand):  # same test Wazuh applies (non-negated form below)
            return cand
    return None


def witness_event(rule: WazuhRule) -> dict[str, str] | None:
    """Flat Wazuh-field event that triggers ``rule`` (or None if none could be built)."""
    from .matcher import rule_matches  # local import: matcher imports emit

    event: dict[str, str] = {}
    for req in rule.requirements:
        if req.name == KEYWORD_FIELD:
            return None
        atoms = rule.atoms.get(req.name)
        if atoms is None:  # a 'require' pattern from mapping.yml
            event[req.name] = _literal_from_regex(req.pattern.removeprefix("(?is)"))
            continue
        if req.negate:
            value = _field_value(req.name, atoms, "(?s)^")  # any value works...
            value = value or "benign-value"
            probe = regex.search(req.pattern, value)
            if probe:  # ...unless it hits the negated pattern
                value = "benign-value" if not regex.search(req.pattern, "benign-value") else "q"
        else:
            value = _field_value(req.name, atoms, req.pattern)
        if value is None:
            return None
        event[req.name] = value
    event = {**BASE_SYSTEM, **event}
    parent = rule.if_sid[0] if rule.if_sid else None
    if parent in CHANNELS:
        event.setdefault("win.system.channel", CHANNELS[parent][0])
        event.setdefault("win.system.providerName", CHANNELS[parent][1])
    if parent in SYSMON_EID:
        event.setdefault("win.system.channel", CHANNELS[61600][0])
        event.setdefault("win.system.providerName", CHANNELS[61600][1])
        event["win.system.eventID"] = str(SYSMON_EID[parent])
    event.setdefault("win.system.eventID", "1")
    return event if rule_matches(rule, event) else None


def to_logtest_json(event: dict[str, str]) -> str:
    """Flat dotted keys -> nested JSON string as the Wazuh agent sends event-channel logs."""
    root: dict = {}
    for dotted, value in event.items():
        node = root
        parts = dotted.split(".")
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = value
    return json.dumps(root, separators=(",", ":"))


def is_windows_event_rule(rule: WazuhRule) -> bool:
    return bool(rule.if_sid) and all(s in SYSMON_EID or s in CHANNELS for s in rule.if_sid)
