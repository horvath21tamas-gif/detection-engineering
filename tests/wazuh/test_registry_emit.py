import json

import pytest
from lxml import etree

from dectools.wazuh.emit import render_file
from dectools.wazuh.registry import IdRegistry, RegistryFull


def test_ids_are_stable_sequential_and_never_reused(tmp_path):
    reg = IdRegistry()
    a, b = reg.get("A:1"), reg.get("B:1")
    assert (a, b) == (100000, 100001)
    path = tmp_path / "reg.json"
    reg.save(path)

    reg2 = IdRegistry.load(path)
    assert reg2.get("B:1") == b and reg2.get("A:1") == a
    assert reg2.get("C:1") == 100002
    reg2.retire_unseen()  # nothing unseen
    assert not reg2.assigned.keys() - {"A:1", "B:1", "C:1"}

    reg3 = IdRegistry.load(path)
    reg3.get("A:1")  # B vanished from the rule set
    reg3.retire_unseen()
    assert "B:1" in reg3.retired and reg3.get("D:1") == 100002  # id of B not reused
    # a deleted rule that returns gets its old id back
    assert reg3.get("B:1") == b


def test_registry_full():
    reg = IdRegistry(base=5, max_id=5)
    reg.get("a")
    with pytest.raises(RegistryFull):
        reg.get("b")


def test_registry_json_is_deterministic():
    reg = IdRegistry()
    for k in ("z", "a", "m"):
        reg.get(k)
    assert json.loads(reg.to_json())["assigned"] == {"z": 100000, "a": 100001, "m": 100002}


def test_generated_xml_is_well_formed_and_escaped(compile_rule, sigma):
    rules = compile_rule(sigma("""
        sel:
            CommandLine|contains: ['a<b', 'x&y', '$(whoami)']
        condition: sel
    """))
    rules[0].description = 'Title with <tag> & $(cmd)'
    xml = render_file("sigma", rules, "header")
    root = etree.fromstring(xml.encode())
    rule = root.find("rule")
    assert "$(" not in rule.findtext("description")
    assert rule.find("field").text.startswith("(?is)")
