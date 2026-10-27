"""Behavioural rule tests: tests/rule_cases/*.yml hold events that must / must not trigger.

Every case is checked against the Sigma source (reference evaluator) and, when the rule
compiles to Wazuh, against the generated Wazuh rules too.
"""

from pathlib import Path

import pytest
import yaml
from sigma.collection import SigmaCollection

from dectools.oracle import rule_triggers
from dectools.wazuh.convert import convert_sigma_rule
from dectools.wazuh.logic import Unsupported
from dectools.wazuh.mapping import Mapping
from dectools.wazuh.matcher import rule_matches
from dectools.wazuh.registry import IdRegistry

ROOT = Path(__file__).resolve().parents[1]
CASES = sorted((ROOT / "tests" / "rule_cases").glob("*.yml"))
MAPPING = Mapping.load()


def load_rule(stem: str):
    path = next((ROOT / "rules" / "sigma").rglob(f"{stem}.y*ml"))
    return SigmaCollection.from_yaml(path.read_text(encoding="utf-8")).rules[0]


def _cases():
    for f in CASES:
        spec = yaml.safe_load(f.read_text(encoding="utf-8"))
        for expected, key in ((True, "match"), (False, "no_match")):
            for c in spec.get(key) or []:
                yield pytest.param(spec["rule"], c["event"], expected, id=f"{spec['rule']}-{c['name']}")


@pytest.mark.parametrize("stem,event,expected", list(_cases()))
def test_sigma_semantics(stem, event, expected):
    assert rule_triggers(load_rule(stem), event) is expected


@pytest.mark.parametrize("stem,event,expected", list(_cases()))
def test_wazuh_semantics(stem, event, expected):
    rule = load_rule(stem)
    try:
        compiled = convert_sigma_rule(rule, MAPPING, IdRegistry())
    except Unsupported:
        pytest.skip("rule is not compilable to Wazuh")
    profile = MAPPING.profile_for(rule.logsource)
    wazuh_event = {MAPPING.wazuh_field(profile, k): v for k, v in event.items()}
    got = any(rule_matches(r, wazuh_event) for r in compiled)
    assert got is expected
