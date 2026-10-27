import pytest
from sigma.exceptions import SigmaError

from dectools.wazuh.emit import render_rule
from dectools.wazuh.logic import Unsupported
from dectools.wazuh.matcher import rule_matches


def ev(**kw):
    base = {
        "win.eventdata.image": r"C:\Windows\System32\wmic.exe",
        "win.eventdata.commandLine": "wmic /node:host process call create calc",
        "win.eventdata.parentImage": r"C:\Windows\explorer.exe",
        "win.eventdata.user": r"CORP\alice",
    }
    base.update(kw)
    return base


def test_single_clause_structure(compile_rule, sigma):
    (r,) = compile_rule(sigma("""
        sel:
            Image|endswith: '\\wmic.exe'
            CommandLine|contains: ['/node:', 'process call']
        condition: sel
    """))
    assert r.if_sid == (61603,)
    assert r.level == 11 and r.mitre == ["T1059.001"]
    assert "attack_execution" in r.groups
    assert rule_matches(r, ev())
    assert not rule_matches(r, ev(**{"win.eventdata.image": r"C:\x\notepad.exe"}))
    assert not rule_matches(r, ev(**{"win.eventdata.commandLine": "wmic /?"}))


def test_case_insensitive_by_default_cased_on_request(compile_rule, sigma):
    (r,) = compile_rule(sigma("""
        sel:
            Image|endswith: '\\WMIC.EXE'
        condition: sel
    """))
    assert rule_matches(r, ev())
    (c,) = compile_rule(sigma("""
        sel:
            Image|endswith|cased: '\\WMIC.EXE'
        condition: sel
    """))
    assert not rule_matches(c, ev())


def test_or_across_fields_becomes_multiple_rules(compile_rule, sigma):
    rules = compile_rule(sigma("""
        a:
            Image|endswith: '\\wmic.exe'
        b:
            ParentImage|endswith: '\\winword.exe'
        condition: a or b
    """))
    assert len(rules) == 2
    assert len({r.id for r in rules}) == 2


def test_or_values_of_same_field_stay_one_rule(compile_rule, sigma):
    rules = compile_rule(sigma("""
        a:
            Image|endswith: ['\\a.exe', '\\b.exe', '\\c.exe']
        b:
            Image|endswith: '\\d.exe'
        condition: a or b
    """))
    assert len(rules) == 1


def test_not_of_and_expands_by_de_morgan(compile_rule, sigma):
    rules = compile_rule(sigma("""
        sel:
            Image|endswith: '\\wmic.exe'
        flt:
            User: 'SYSTEM'
            ParentImage|endswith: '\\services.exe'
        condition: sel and not flt
    """))
    assert len(rules) == 2
    both = ev(**{"win.eventdata.user": "SYSTEM", "win.eventdata.parentImage": r"C:\services.exe"})
    assert not any(rule_matches(r, both) for r in rules)
    only_user = ev(**{"win.eventdata.user": "SYSTEM"})
    assert any(rule_matches(r, only_user) for r in rules)


def test_same_field_twice_uses_one_field_element(compile_rule, sigma):
    (r,) = compile_rule(sigma("""
        sel:
            CommandLine|contains|all: ['process', 'call']
            CommandLine|contains: 'create'
        condition: sel
    """))
    names = [q.name for q in r.requirements]
    assert len(names) == len(set(names))
    assert rule_matches(r, ev())
    assert not rule_matches(r, ev(**{"win.eventdata.commandLine": "process call"}))


def test_wildcards_and_special_chars(compile_rule, sigma):
    (r,) = compile_rule(sigma(r"""
        sel:
            CommandLine|contains: 'a?c*d (x) [y] $z ^'
        condition: sel
    """))
    assert rule_matches(r, ev(**{"win.eventdata.commandLine": "xx aBc--d (x) [y] $z ^ yy"}))
    assert not rule_matches(r, ev(**{"win.eventdata.commandLine": "a?c*d x"}))


def test_regex_modifier(compile_rule, sigma):
    (r,) = compile_rule(sigma("""
        sel:
            CommandLine|re: 'node:\\S+\\s+process'
        condition: sel
    """))
    assert rule_matches(r, ev())


def test_keyword_search_uses_regex_element(compile_rule, sigma):
    (r,) = compile_rule(sigma("""
        kw:
            - 'mimikatz'
        condition: kw
    """))
    xml = render_rule(r)
    assert "<regex" in xml and 'type="pcre2"' in xml


def test_cidr_octet_aligned(compile_rule, mapping):
    from sigma.collection import SigmaCollection

    from dectools.wazuh.convert import convert_sigma_rule
    from dectools.wazuh.registry import IdRegistry

    y = """
title: net
id: 8a7e4a3c-1b0b-4d11-9a53-0d3d8f6c2222
logsource: {product: windows, category: network_connection}
detection:
  sel:
    DestinationIp|cidr: 10.0.0.0/8
  condition: sel
level: low
"""
    (r,) = convert_sigma_rule(SigmaCollection.from_yaml(y).rules[0], mapping, IdRegistry())
    assert r.if_sid == (61605,)
    assert rule_matches(r, {"win.eventdata.destinationIp": "10.1.2.3"})
    assert not rule_matches(r, {"win.eventdata.destinationIp": "110.1.2.3"})


@pytest.mark.parametrize(
    "body",
    [
        "sel:\n    Image: null\ncondition: sel",
        "sel:\n    CommandLine|fieldref: Image\ncondition: sel",
        "sel:\n    DestinationPort|gt: 1024\ncondition: sel",
    ],
)
def test_unsupported_constructs_are_reported_not_dropped(compile_rule, sigma, body):
    with pytest.raises((Unsupported, SigmaError)):
        compile_rule(sigma(body))


def test_unsupported_logsource_is_reported(mapping):
    from sigma.collection import SigmaCollection

    from dectools.wazuh.convert import convert_sigma_rule
    from dectools.wazuh.registry import IdRegistry

    y = """
title: cloud
id: 8a7e4a3c-1b0b-4d11-9a53-0d3d8f6c3333
logsource: {product: azure, service: signinlogs}
detection: {sel: {Foo: bar}, condition: sel}
level: low
"""
    with pytest.raises(Unsupported, match="unsupported logsource"):
        convert_sigma_rule(SigmaCollection.from_yaml(y).rules[0], mapping, IdRegistry())


def test_too_many_clauses_is_unsupported(compile_rule, sigma):
    # 8 independent two-way ORs on different fields -> 256 clauses
    body = "\n".join(
        f"s{i}:\n  - Image|endswith: 'a{i}'\n  - ParentImage|endswith: 'b{i}'\n  - CommandLine|contains: 'c{i}'"
        for i in range(5)
    )
    cond = " and ".join(f"s{i}" for i in range(5))
    with pytest.raises(Unsupported, match="Wazuh rules"):
        compile_rule(sigma(body + f"\ncondition: {cond}"))
