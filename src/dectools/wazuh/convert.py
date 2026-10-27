"""Sigma rule -> Wazuh rules."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from sigma.collection import SigmaCollection
from sigma.exceptions import SigmaError
from sigma.rule import SigmaRule

from .emit import FieldReq, WazuhRule, render_file, requirements_for
from .logic import Atom, Unsupported, condition_to_dnf
from .mapping import Mapping
from .registry import IdRegistry

TECHNIQUE = re.compile(r"^t\d{4}(\.\d{3})?$")
HEADER = (
    "GENERATED FILE - DO NOT EDIT BY HAND.\n"
    "Compiled from Sigma rules by dectools (see wazuh/README.md).\n"
    "Change the Sigma source and let the pipeline regenerate this file.\n"
    "Wazuh fires only the FIRST matching sibling rule per event, so rules are split\n"
    "into files that load most-severe first (file names sort alphabetically)."
)
# Wazuh loads rule files alphabetically and only the first matching child of a
# parent rule alerts. Severity-ordered files make sure the worst detection wins.
LEVEL_FILES = ["critical", "high", "medium", "low", "informational"]


@dataclass
class RuleOutcome:
    path: str
    sigma_id: str
    title: str
    status: str  # ok | unsupported | error
    reason: str = ""
    rules: list[WazuhRule] = field(default_factory=list)
    source_dir: str = ""


@dataclass
class BuildResult:
    outcomes: list[RuleOutcome]
    files: dict[str, str]

    @property
    def counts(self) -> Counter:
        return Counter(o.status for o in self.outcomes)

    @property
    def rule_count(self) -> int:
        return sum(len(o.rules) for o in self.outcomes)


def known_mitre_ids() -> frozenset[str]:
    path = Path(__file__).with_name("mitre_ids.json")
    return frozenset(json.loads(path.read_text(encoding="utf-8"))["ids"]) if path.exists() else frozenset()


_KNOWN = known_mitre_ids()


def _mitre_and_groups(rule: SigmaRule) -> tuple[list[str], list[str]]:
    mitre, groups = [], ["sigma"]
    for tag in rule.tags:
        if tag.namespace != "attack":
            continue
        if TECHNIQUE.match(tag.name):
            tid = tag.name.upper()
            if not _KNOWN or tid in _KNOWN:
                mitre.append(tid)
            else:  # unknown to Wazuh's MITRE database: keep it searchable as a group instead
                groups.append("mitre_" + tid.replace(".", "_"))
        else:
            groups.append("attack_" + tag.name.replace("-", "_"))
    return sorted(set(mitre)), list(dict.fromkeys(groups))


def convert_sigma_rule(
    rule: SigmaRule, mapping: Mapping, registry: IdRegistry, *, use_mitre: bool = True
) -> list[WazuhRule]:
    """Raises Unsupported when the rule cannot be expressed in Wazuh."""
    if rule.id is None:
        raise Unsupported("rule has no 'id' (UUID) - required for stable Wazuh ids")
    profile = mapping.profile_for(rule.logsource)

    clauses: list[frozenset[Atom]] = []
    for cond in rule.detection.parsed_condition:
        for clause in condition_to_dnf(cond.parsed):
            if clause not in clauses:
                clauses.append(clause)

    built: list[tuple[str, list[FieldReq], dict]] = []
    for clause in clauses:
        by_field: dict[str, list[Atom]] = defaultdict(list)
        for atom in clause:
            wfield = mapping.wazuh_field(profile, atom.field)
            by_field[wfield].append(Atom(wfield, atom.alts, atom.neg))
        reqs = [FieldReq(n, p) for n, p in profile.require]
        reqs += requirements_for(by_field)
        key = hashlib.sha1(repr([(r.name, r.pattern, r.negate) for r in reqs]).encode()).hexdigest()[:10]
        built.append((key, reqs, dict(by_field)))
    built.sort(key=lambda kv: kv[0])

    mitre, groups = _mitre_and_groups(rule)
    level = mapping.level(rule.level)
    out = []
    for i, (key, reqs, atoms) in enumerate(built, 1):
        title = rule.title if len(built) == 1 else f"{rule.title} [{i}/{len(built)}]"
        out.append(
            WazuhRule(
                id=registry.get(f"{rule.id}:{key}"),
                level=level,
                description=title,
                if_sid=profile.if_sid,
                if_group=profile.if_group,
                requirements=reqs,
                mitre=mitre if use_mitre else [],
                groups=groups,
                sigma_id=str(rule.id),
                sigma_title=rule.title,
                clause_key=key,
                atoms=atoms,
            )
        )
    return out


def iter_rule_files(rules_dir: Path):
    for p in sorted(rules_dir.rglob("*")):
        if p.suffix in (".yml", ".yaml") and p.is_file():
            yield p


def build_ruleset(
    rules_dir: str | Path,
    mapping: Mapping,
    registry: IdRegistry,
    *,
    use_mitre: bool = True,
    only: set[str] | None = None,
    quarantine: dict[str, str] | None = None,
) -> BuildResult:
    rules_dir = Path(rules_dir)
    outcomes: list[RuleOutcome] = []
    for path in iter_rule_files(rules_dir):
        rel = path.relative_to(rules_dir)
        source_dir = rel.parts[0] if len(rel.parts) > 1 else "root"
        outcome = RuleOutcome(str(rel), "", path.stem, "ok", source_dir=source_dir)
        try:
            collection = SigmaCollection.from_yaml(path.read_text(encoding="utf-8"))
            if len(collection.rules) != 1:
                raise Unsupported(f"expected 1 rule per file, found {len(collection.rules)}")
            rule = collection.rules[0]
            outcome.sigma_id, outcome.title = str(rule.id or ""), rule.title
            if only and outcome.sigma_id not in only and str(rel) not in only:
                continue
            if quarantine and outcome.sigma_id in quarantine:
                outcome.status = "quarantined"
                outcome.reason = f"quarantined: {quarantine[outcome.sigma_id]}"
            else:
                outcome.rules = convert_sigma_rule(rule, mapping, registry, use_mitre=use_mitre)
        except Unsupported as exc:
            outcome.status, outcome.reason = "unsupported", str(exc)
        except (SigmaError, ValueError, KeyError) as exc:
            outcome.status, outcome.reason = "error", f"{type(exc).__name__}: {exc}"
        outcomes.append(outcome)

    return BuildResult(outcomes, render_files(outcomes, mapping))


def render_files(outcomes: list[RuleOutcome], mapping: Mapping) -> dict[str, str]:
    by_level: dict[str, list[WazuhRule]] = defaultdict(list)
    for o in outcomes:
        for r in o.rules:
            by_level[mapping.level_name(r.level)].append(r)
    files = {}
    for rank, name in enumerate(LEVEL_FILES, 1):
        rules = by_level.get(name)
        if rules:
            # most specific (most requirements) first, then stable by id
            rules.sort(key=lambda r: (-len(r.requirements), r.id))
            files[f"sigma_{rank}_{name}.xml"] = render_file("sigma", rules, HEADER)
    return files
