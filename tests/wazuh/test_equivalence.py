"""Differential test: every compiled Wazuh rule set must agree with the Sigma
rule it came from on randomly generated events (oracle: dectools.oracle)."""

import json
import random
from pathlib import Path

import pytest
from sigma.collection import SigmaCollection
from sigma.conditions import ConditionFieldEqualsValueExpression
from sigma.types import SigmaCIDRExpression, SigmaNumber, SigmaString, SpecialChars

from dectools.oracle import evaluate as oracle
from dectools.oracle import leaves
from dectools.wazuh.convert import convert_sigma_rule
from dectools.wazuh.logic import KEYWORD_FIELD, Unsupported
from dectools.wazuh.matcher import rule_matches
from dectools.wazuh.registry import IdRegistry

RULES_DIR = Path(__file__).resolve().parents[2] / "rules" / "sigma"
FILES = sorted(RULES_DIR.rglob("*.yml")) + sorted(RULES_DIR.rglob("*.yaml"))
EVENTS_PER_RULE = 60


def sample_for(value, rnd):
    """A string that matches (or nearly matches) the given Sigma value."""
    if isinstance(value, SigmaString):
        out = []
        for p in value.s:
            if p is SpecialChars.WILDCARD_MULTI:
                out.append(rnd.choice(["", "x", r"C:\dir\ ", "a b"]))
            elif p is SpecialChars.WILDCARD_SINGLE:
                out.append(rnd.choice(["z", "Q"]))
            else:
                out.append(str(p))
        s = "".join(out)
        if rnd.random() < 0.25:
            s = s.upper()
        if rnd.random() < 0.15 and s:
            s = s[:-1]  # near miss
        return s
    if isinstance(value, SigmaNumber):
        return str(value.number if rnd.random() < 0.8 else value.number + 1)
    if isinstance(value, SigmaCIDRExpression):
        return str(next(iter(value.network.hosts()))) if rnd.random() < 0.7 else "8.8.8.8"
    return rnd.choice(["", "foo", "bar baz"])


@pytest.mark.skipif(not FILES, reason="no Sigma rules in repo")
def test_compiled_rules_agree_with_sigma_semantics(mapping):
    rnd = random.Random(1337)
    converted = positives = disagreements_checked = 0
    for path in FILES:
        rule = SigmaCollection.from_yaml(path.read_text(encoding="utf-8")).rules[0]
        try:
            compiled = convert_sigma_rule(rule, mapping, IdRegistry())
        except Unsupported:
            continue
        converted += 1
        profile = mapping.profile_for(rule.logsource)
        conds = [c.parsed for c in rule.detection.parsed_condition]
        by_field: dict[str, list] = {}
        for c in conds:
            for leaf in leaves(c):
                f = leaf.field if isinstance(leaf, ConditionFieldEqualsValueExpression) else KEYWORD_FIELD
                by_field.setdefault(f, []).append(leaf.value)
        for _ in range(EVENTS_PER_RULE):
            sigma_event = {}
            for f, values in by_field.items():
                sigma_event[f] = sample_for(rnd.choice(values), rnd) if rnd.random() < 0.7 else rnd.choice(["", "foo.exe", r"C:\Windows\System32\cmd.exe"])
            sigma_event = {k: v for k, v in sigma_event.items()}
            want = any(oracle(c, sigma_event) for c in conds)
            wazuh_event = {}
            for f, v in sigma_event.items():
                if f == KEYWORD_FIELD:
                    continue
                wazuh_event[mapping.wazuh_field(profile, f)] = v
            if KEYWORD_FIELD in sigma_event:
                full = sigma_event[KEYWORD_FIELD]
                got = any(rule_matches(r, wazuh_event, full_log=full) for r in compiled)
            else:
                got = any(rule_matches(r, wazuh_event) for r in compiled)
            assert got == want, f"{path.name}: event {json.dumps(sigma_event)} sigma={want} wazuh={got}"
            positives += want
            disagreements_checked += 1
    assert converted > 400
    assert positives > converted  # generator really exercises the true branch
