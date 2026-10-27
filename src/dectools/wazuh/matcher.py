"""Tiny emulation of how Wazuh evaluates <field>/<regex> requirements.

Used by the test-suite to prove that compiled rules behave like the Sigma source.
Assumption (matches Wazuh behaviour for decoded event-channel logs): a rule whose
required field is absent from the event does not match, even with negate="yes".
"""

from __future__ import annotations

import json

import regex

from .emit import WazuhRule
from .logic import KEYWORD_FIELD


def rule_matches(rule: WazuhRule, event: dict[str, str], full_log: str | None = None) -> bool:
    for req in rule.requirements:
        if req.name == KEYWORD_FIELD:
            value = full_log if full_log is not None else json.dumps(event)
        else:
            if req.name not in event:
                return False
            value = str(event[req.name])
        hit = regex.search(req.pattern, value) is not None
        if hit == req.negate:
            return False
    return True


def first_match(rules: list[WazuhRule], event: dict[str, str]) -> WazuhRule | None:
    """Wazuh semantics: among sibling rules the first match wins."""
    for r in rules:
        if rule_matches(r, event):
            return r
    return None
