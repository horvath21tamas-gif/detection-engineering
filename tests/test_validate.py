import textwrap

from dectools import validate

GOOD = textwrap.dedent(
    """\
    title: Good rule
    id: 8a7e4a3c-1b0b-4d11-9a53-0d3d8f6c5555
    status: stable
    description: something
    author: me
    date: 2026-01-01
    level: high
    tags: [attack.execution, attack.t1047]
    logsource: {product: windows, category: process_creation}
    detection:
      sel:
        Image|endswith: '\\wmic.exe'
      condition: sel
    """
)


def run(tmp_path, **files):
    for name, text in files.items():
        (tmp_path / name).write_text(text)
    return validate.validate_tree(tmp_path)


def codes(findings):
    return sorted({f"{f.level}:{f.code}" for f in findings})


def test_good_rule_is_clean(tmp_path):
    assert run(tmp_path, **{"T1047.yml": GOOD}) == []


def test_missing_keys_and_bad_id(tmp_path):
    bad = GOOD.replace("id: 8a7e4a3c-1b0b-4d11-9a53-0d3d8f6c5555", "id: 1").replace("author: me\n", "")
    assert {"error:bad-id", "error:missing-key"} <= set(codes(run(tmp_path, **{"T1047.yml": bad})))


def test_duplicate_ids(tmp_path):
    f = run(tmp_path, **{"T1047.yml": GOOD, "T1047_001.yml": GOOD.replace("t1047", "t1047.001")})
    assert "error:duplicate-id" in codes(f)


def test_regex_without_re_is_a_warning(tmp_path):
    rule = GOOD.replace("Image|endswith: '\\wmic.exe'", "Image: '(a|b)\\.exe$'")
    assert "warning:regex-without-re" in codes(run(tmp_path, **{"T1047.yml": rule}))
    ok = GOOD.replace("Image|endswith: '\\wmic.exe'", "Image|re: '(a|b)\\.exe$'")
    assert "warning:regex-without-re" not in codes(run(tmp_path, **{"T1047.yml": ok}))


def test_validator_never_modifies_rules(tmp_path):
    p = tmp_path / "T1047.yml"
    p.write_text(GOOD.replace("author:", "autor:"))
    before = p.read_text()
    validate.validate_tree(tmp_path)
    assert p.read_text() == before


def test_baseline_ratchet(tmp_path, capsys):
    rules = tmp_path / "rules"
    rules.mkdir()
    (rules / "T1047.yml").write_text(GOOD.replace("Image|endswith: '\\wmic.exe'", "Image: '(a|b)$'"))
    base = tmp_path / "base.json"
    assert validate.main([str(rules), "--baseline", str(base)]) == 1  # new warning fails
    assert validate.main([str(rules), "--baseline", str(base), "--write-baseline"]) == 0
    assert validate.main([str(rules), "--baseline", str(base)]) == 0  # accepted now


def test_duplicate_yaml_keys_are_flagged(tmp_path):
    dup = GOOD.replace(
        "Image|endswith: '\\wmic.exe'",
        "CommandLine|contains: 'a'\n    CommandLine|contains: 'b'",
    )
    assert "warning:duplicate-key" in codes(run(tmp_path, **{"T1047.yml": dup}))
