import json
import textwrap
from pathlib import Path

from lxml import etree

from dectools.wazuh import cli
from dectools.wazuh.matcher import first_match, rule_matches
from dectools.wazuh.witness import to_logtest_json, witness_event

RULE = textwrap.dedent(
    """\
    title: WMIC remote process
    id: 8a7e4a3c-1b0b-4d11-9a53-0d3d8f6c4444
    status: test
    description: d
    author: t
    date: 2026-01-01
    level: critical
    tags: [attack.execution, attack.t1047]
    logsource: {product: windows, category: process_creation}
    detection:
      sel:
        Image|endswith: '\\wmic.exe'
        CommandLine|contains: '/node:'
      flt:
        User|contains: 'SYSTEM'
      condition: sel and not flt
    """
)


def test_cli_build_end_to_end(tmp_path: Path):
    rules = tmp_path / "rules"
    rules.mkdir()
    (rules / "T1047.yml").write_text(RULE)
    out, reg = tmp_path / "out", tmp_path / "reg.json"
    rc = cli.main(["build", "--rules", str(rules), "--out", str(out), "--registry", str(reg), "--update-registry"])
    assert rc == 0
    xml = out / "rules" / "sigma_1_critical.xml"
    root = etree.parse(str(xml)).getroot()
    assert [r.get("id") for r in root.iter("rule")] == ["100000"]
    assert json.loads(reg.read_text())["assigned"]
    vec = [json.loads(line) for line in (out / "testvectors.jsonl").read_text().splitlines()]
    assert vec[0]["rule_id"] == 100000
    assert json.loads(vec[0]["log"])["win"]["system"]["eventID"] == "1"
    # second run must not change ids
    before = reg.read_text()
    assert cli.main(["build", "--rules", str(rules), "--out", str(out), "--registry", str(reg), "--check-registry"]) == 0
    assert reg.read_text() == before


def test_check_registry_fails_when_out_of_date(tmp_path: Path):
    rules = tmp_path / "rules"
    rules.mkdir()
    (rules / "T1047.yml").write_text(RULE)
    rc = cli.main(["build", "--rules", str(rules), "--out", str(tmp_path / "o"), "--registry", str(tmp_path / "r.json"), "--check-registry"])
    assert rc == 1


def test_witness_matches_and_mutations_do_not(compile_rule):
    rules = compile_rule(RULE)
    for r in rules:
        ev = witness_event(r)
        assert ev and rule_matches(r, ev)
        broken = {**ev, "win.eventdata.image": "C:\\Windows\\notepad.exe"}
        assert not rule_matches(r, broken)


def test_first_match_wins_order(compile_rule):
    a, = compile_rule(RULE)
    ev = witness_event(a)
    assert first_match([a], ev) is a


def test_logtest_json_is_nested():
    j = json.loads(to_logtest_json({"win.system.eventID": "1", "win.eventdata.image": "x"}))
    assert j == {"win": {"system": {"eventID": "1"}, "eventdata": {"image": "x"}}}


def test_all_repo_rules_have_witnesses(mapping):
    """At least 90% of the compiled repo rules must be provably able to fire."""
    from dectools.wazuh.convert import build_ruleset
    from dectools.wazuh.registry import IdRegistry

    root = Path(__file__).resolve().parents[2] / "rules" / "sigma"
    if not root.exists():
        return
    res = build_ruleset(root, mapping, IdRegistry())
    rules = [r for o in res.outcomes for r in o.rules]
    ok = sum(1 for r in rules if witness_event(r))
    assert ok / len(rules) > 0.9, f"only {ok}/{len(rules)} rules have a witness"


def test_output_is_deterministic_across_processes(tmp_path):
    """Hash randomisation must not change rule text or ids (ids are committed)."""
    import subprocess
    import sys

    root = Path(__file__).resolve().parents[2]
    outputs = []
    for seed in ("1", "2", "3"):
        out = tmp_path / f"o{seed}"
        subprocess.run(
            [sys.executable, "-m", "dectools.wazuh", "build", "--rules", str(root / "rules" / "sigma"),
             "--out", str(out), "--registry", str(tmp_path / f"r{seed}.json"), "--update-registry",
             "--quarantine", str(root / "wazuh" / "quarantine.yml"), "--benign", str(root / "wazuh" / "benign_events.jsonl")],
            env={**__import__("os").environ, "PYTHONHASHSEED": seed}, check=True, capture_output=True,
        )
        outputs.append(((out / "rules" / "sigma_1_critical.xml").read_bytes(), (tmp_path / f"r{seed}.json").read_bytes()))
    assert outputs[0] == outputs[1] == outputs[2]
