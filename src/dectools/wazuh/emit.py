"""Wazuh rule data model and XML writer."""

from __future__ import annotations

from dataclasses import dataclass, field
from xml.sax.saxutils import escape

from .logic import KEYWORD_FIELD, Atom, Pat

FLAGS = "(?is)"


@dataclass
class FieldReq:
    name: str  # Wazuh field name or KEYWORD_FIELD
    pattern: str  # complete PCRE2 expression incl. flags
    negate: bool = False


@dataclass
class WazuhRule:
    id: int
    level: int
    description: str
    if_sid: tuple[int, ...] = ()
    if_group: str | None = None
    requirements: list[FieldReq] = field(default_factory=list)
    mitre: list[str] = field(default_factory=list)
    groups: list[str] = field(default_factory=list)
    sigma_id: str = ""
    sigma_title: str = ""
    clause_key: str = ""
    atoms: dict = field(default_factory=dict, repr=False)  # wazuh field -> [Atom]; used for test vectors


def _canon(pats) -> tuple[Pat, ...]:
    """Deterministic, de-duplicated order (set iteration order varies between processes)."""
    return tuple(sorted(dict.fromkeys(pats), key=lambda p: (p.standalone(), p.cased)))


def _alt(pats: tuple[Pat, ...]) -> str:
    parts = [p.standalone() for p in pats]
    return parts[0] if len(parts) == 1 else "(?:" + "|".join(parts) + ")"


def _alt_lookahead(pats: tuple[Pat, ...]) -> str:
    parts = []
    for p in pats:
        frag = ("" if p.prefix else ".*?") + p.body + ("$" if p.suffix else "")
        parts.append(f"(?-i:{frag})" if p.cased else frag)
    return "(?:" + "|".join(parts) + ")"


def requirements_for(atoms_by_field: dict[str, list[Atom]]) -> list[FieldReq]:
    """One <field>/<regex> element per Wazuh field (never repeated names)."""
    reqs: list[FieldReq] = []
    for name in sorted(atoms_by_field):
        atoms = atoms_by_field[name]
        pos = sorted(
            (Atom(a.field, _canon(a.alts), False) for a in atoms if not a.neg),
            key=lambda a: [p.standalone() for p in a.alts],
        )
        neg = [a for a in atoms if a.neg]
        neg_alts: tuple[Pat, ...] = _canon(p for a in neg for p in a.alts)
        if len(pos) == 1 and not neg:
            reqs.append(FieldReq(name, FLAGS + _alt(pos[0].alts)))
        elif not pos and neg:
            reqs.append(FieldReq(name, FLAGS + _alt(neg_alts), negate=True))
        else:
            rx = "^" + "".join(f"(?={_alt_lookahead(a.alts)})" for a in pos)
            if neg_alts:
                rx += f"(?!{_alt_lookahead(neg_alts)})"
            reqs.append(FieldReq(name, FLAGS + rx))
    return reqs


def _xml(text: str) -> str:
    return escape(text)


def _desc(text: str) -> str:
    # $(field) is Wazuh variable substitution; titles must stay literal
    return _xml(text.replace("$(", "$ ("))


def render_rule(r: WazuhRule) -> str:
    lines = [f'  <rule id="{r.id}" level="{r.level}">']
    if r.if_sid:
        lines.append(f"    <if_sid>{','.join(str(s) for s in r.if_sid)}</if_sid>")
    if r.if_group:
        lines.append(f"    <if_group>{_xml(r.if_group)}</if_group>")
    for q in r.requirements:
        neg = ' negate="yes"' if q.negate else ""
        if q.name == KEYWORD_FIELD:
            lines.append(f'    <regex type="pcre2"{neg}>{_xml(q.pattern)}</regex>')
        else:
            lines.append(f'    <field name="{_xml(q.name)}" type="pcre2"{neg}>{_xml(q.pattern)}</field>')
    lines.append(f"    <description>{_desc(r.description)}</description>")
    lines.append(f'    <info type="text">sigma:{_xml(r.sigma_id)}</info>')
    if r.mitre:
        lines.append("    <mitre>")
        lines.extend(f"      <id>{_xml(m)}</id>" for m in r.mitre)
        lines.append("    </mitre>")
    if r.groups:
        lines.append(f"    <group>{_xml(','.join(r.groups))},</group>")
    lines.append("    <options>no_full_log</options>")
    lines.append("  </rule>")
    return "\n".join(lines)


def render_file(group_name: str, rules: list[WazuhRule], header: str) -> str:
    out = ['<!--', *(f"  {h}" for h in header.splitlines()), "-->", "", f'<group name="{_xml(group_name)},">']
    for rule in rules:
        out.append(render_rule(rule))
        out.append("")
    out.append("</group>")
    return "\n".join(out) + "\n"
