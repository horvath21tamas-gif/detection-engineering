"""Read-only Sigma rule validator (never rewrites rule files).

Errors fail the build. Warnings are tracked against a committed baseline so that
new problems fail CI while the existing backlog can be worked off step by step.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import uuid
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import yaml
from sigma.collection import SigmaCollection
from sigma.exceptions import SigmaError

REQUIRED = ("title", "id", "status", "description", "author", "date", "logsource", "detection", "level", "tags")
STATUS = {"stable", "test", "experimental", "deprecated", "unsupported"}
LEVEL = {"informational", "low", "medium", "high", "critical"}
TECHNIQUE_TAG = re.compile(r"^attack\.t\d{4}(\.\d{3})?$")
# plain (non-|re) values that look like regular expressions
REGEXY = re.compile(
    r"(\.\*|\.\+|\\\.|\(\?[:i=!]|\[[^\]]+\][+*{]|\\[dws][+*{]|\([^()]*\|[^()]*\)|^\^|\)\$$)"
)


@dataclass(frozen=True)
class Finding:
    path: str
    level: str  # error | warning
    code: str
    message: str

    @property
    def key(self) -> str:
        return f"{self.path}::{self.code}"


class _DupKeyLoader(yaml.SafeLoader):
    """SafeLoader that records duplicate mapping keys (PyYAML silently keeps the last one)."""

    duplicates: list[str]


def _construct_mapping(loader, node, deep=False):
    seen = set()
    for key_node, _ in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in seen:
            loader.duplicates.append(str(key))
        seen.add(key)
    return yaml.SafeLoader.construct_mapping(loader, node, deep=deep)


_DupKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _construct_mapping)


def load_with_duplicates(text: str) -> tuple[object, list[str]]:
    loader = _DupKeyLoader(text)
    loader.duplicates = []
    try:
        return loader.get_single_data(), loader.duplicates
    finally:
        loader.dispose()


def _walk_values(node, field=None):
    if isinstance(node, dict):
        for k, v in node.items():
            yield from _walk_values(v, k)
    elif isinstance(node, list):
        for v in node:
            yield from _walk_values(v, field)
    elif field is not None:
        yield field, node


def validate_file(path: Path, root: Path) -> tuple[list[Finding], str | None]:
    rel = str(path.relative_to(root))
    out: list[Finding] = []

    def err(code, msg):
        out.append(Finding(rel, "error", code, msg))

    def warn(code, msg):
        out.append(Finding(rel, "warning", code, msg))

    try:
        data, duplicates = load_with_duplicates(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        err("yaml", f"invalid YAML: {exc}")
        return out, None
    if not isinstance(data, dict):
        err("yaml", "top level is not a mapping")
        return out, None

    if duplicates:
        warn(
            "duplicate-key",
            f"duplicate YAML key(s) {sorted(set(duplicates))}: YAML keeps only the LAST one, so the "
            "detection is silently weaker than written (use '|contains|all' or separate selections)",
        )
    for key in REQUIRED:
        if not data.get(key):
            err("missing-key", f"missing or empty '{key}'")
    rule_id = str(data.get("id", ""))
    try:
        uuid.UUID(rule_id)
    except ValueError:
        err("bad-id", f"id '{rule_id}' is not a UUID")
        rule_id = None
    if data.get("status") and data["status"] not in STATUS:
        err("bad-status", f"status '{data['status']}' not in {sorted(STATUS)}")
    if data.get("level") and str(data["level"]).lower() not in LEVEL:
        err("bad-level", f"level '{data['level']}' not in {sorted(LEVEL)}")

    tags = [str(t).lower() for t in data.get("tags") or []]
    techniques = [t for t in tags if TECHNIQUE_TAG.match(t)]
    if not techniques:
        warn("no-technique-tag", "no attack.tNNNN[.NNN] tag")
    else:
        m = re.match(r"^(T\d{4})(?:_(\d{3}))?", path.stem, re.I)
        if m:
            want = "attack." + m.group(1).lower() + (f".{m.group(2)}" if m.group(2) else "")
            if want not in techniques:
                warn("filename-tag-mismatch", f"file name suggests {want}, tags have {techniques}")

    try:
        coll = SigmaCollection.from_yaml(path.read_text(encoding="utf-8"))
        for rule in coll.rules:
            for e in rule.errors:
                err("sigma", str(e))
        _ = [c.parsed for r in coll.rules for c in r.detection.parsed_condition]
    except (SigmaError, Exception) as exc:  # noqa: BLE001 - report anything pySigma chokes on
        err("sigma", f"{type(exc).__name__}: {exc}")

    seen_regexy = 0
    for fld, val in _walk_values(data.get("detection", {})):
        if fld == "condition" or not isinstance(val, str):
            continue
        mods = fld.split("|")[1:]
        if "re" in mods:
            continue
        if REGEXY.search(val):
            seen_regexy += 1
    if seen_regexy:
        warn(
            "regex-without-re",
            f"{seen_regexy} value(s) look like regular expressions but the field has no |re modifier "
            "(Sigma would match them literally)",
        )
    return out, rule_id


def validate_tree(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    ids: dict[str, str] = {}
    for path in sorted(root.rglob("*")):
        if path.suffix not in (".yml", ".yaml"):
            continue
        f, rid = validate_file(path, root)
        findings += f
        if rid:
            if rid in ids:
                findings.append(Finding(str(path.relative_to(root)), "error", "duplicate-id", f"id also used by {ids[rid]}"))
            ids[rid] = str(path.relative_to(root))
    return findings


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="dectools-validate")
    ap.add_argument("rules", nargs="?", default="rules/sigma")
    ap.add_argument("--baseline", default=".validation-baseline.json", help="accepted warnings")
    ap.add_argument("--write-baseline", action="store_true")
    ap.add_argument("--json", help="write all findings to this file")
    ap.add_argument("--github", action="store_true", help="emit GitHub annotations")
    args = ap.parse_args(argv)

    root = Path(args.rules)
    findings = validate_tree(root)
    errors = [f for f in findings if f.level == "error"]
    warnings = [f for f in findings if f.level == "warning"]
    base_path = Path(args.baseline)

    if args.write_baseline:
        base_path.write_text(json.dumps(sorted({f.key for f in warnings}), indent=1) + "\n", encoding="utf-8")
        print(f"baseline written: {len(warnings)} warnings accepted")
    baseline = set(json.loads(base_path.read_text())) if base_path.exists() else set()
    new_warnings = [f for f in warnings if f.key not in baseline]

    for f in errors + new_warnings:
        if args.github:
            print(f"::{f.level} file={root / f.path},title={f.code}::{f.message}")
        else:
            print(f"{f.level.upper():7} {f.path}: [{f.code}] {f.message}")
    by_code = Counter(f"{f.level}:{f.code}" for f in findings)
    print(f"\n{len(list(root.rglob('*.y*ml')))} rules | errors {len(errors)} | warnings {len(warnings)} "
          f"({len(warnings) - len(new_warnings)} baselined, {len(new_warnings)} new)")
    for code, n in by_code.most_common():
        print(f"  {n:5}  {code}")
    if args.json:
        Path(args.json).write_text(json.dumps([f.__dict__ for f in findings], indent=1), encoding="utf-8")
    return 1 if errors or new_warnings else 0


if __name__ == "__main__":
    sys.exit(main())
