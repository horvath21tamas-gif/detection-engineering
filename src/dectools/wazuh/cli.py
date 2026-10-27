"""Command line: python -m dectools.wazuh build ..."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

from .convert import build_ruleset
from .mapping import Mapping
from .matcher import rule_matches
from .registry import IdRegistry
from .report import to_json, to_markdown
from .validate import validate_files
from .witness import is_windows_event_rule, to_logtest_json, witness_event


def load_quarantine(path: str | None) -> dict[str, str]:
    import yaml

    if path and Path(path).exists():
        return {str(k): str(v) for k, v in (yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}).items()}
    return {}


def flatten(node: dict, prefix: str = "") -> dict[str, str]:
    flat: dict[str, str] = {}
    for key, value in node.items():
        if isinstance(value, dict):
            flat.update(flatten(value, f"{prefix}{key}."))
        else:
            flat[f"{prefix}{key}"] = str(value)
    return flat


def benign_hits(result, benign_path: str | Path) -> dict[str, str]:
    """sigma_id -> name of the first benign event that wrongly triggers it."""
    path = Path(benign_path)
    if not path.exists():
        return {}
    events = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    flat = [(e.get("name", "?"), flatten(json.loads(e["log"]))) for e in events]
    hits: dict[str, str] = {}
    for outcome in result.outcomes:
        for r in outcome.rules:
            for name, ev in flat:
                if rule_matches(r, ev):
                    hits.setdefault(r.sigma_id, name)
    return hits


def make_bundle(build: Path, benign: Path, out: Path, git_sha: str) -> int:
    import hashlib
    import io
    import tarfile
    import time

    rule_files = sorted((build / "rules").glob("*.xml"))
    if not rule_files:
        print("nothing to bundle - run `build` first", file=sys.stderr)
        return 1
    members: dict[str, bytes] = {f"rules/{p.name}": p.read_bytes() for p in rule_files}
    members["testvectors.jsonl"] = (build / "testvectors.jsonl").read_bytes()
    members["benign.jsonl"] = benign.read_bytes() if benign.exists() else b""
    manifest = {
        "git_sha": git_sha,
        "created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "files": {n: hashlib.sha256(b).hexdigest() for n, b in members.items() if n.startswith("rules/")},
    }
    members["manifest.json"] = (json.dumps(manifest, indent=1) + "\n").encode()
    out.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(out, "w:gz") as tf:
        for name, data in sorted(members.items()):
            info = tarfile.TarInfo(name)
            info.size, info.mtime, info.mode = len(data), 0, 0o644  # reproducible
            tf.addfile(info, io.BytesIO(data))
    print(f"bundle: {out} ({out.stat().st_size // 1024} KiB, {len(rule_files)} rule files)")
    return 0


def triage(args) -> int:
    import yaml

    registry = IdRegistry.load(args.registry)
    result = build_ruleset(args.rules, Mapping.load(), registry, quarantine=load_quarantine(args.quarantine))
    hits = benign_hits(result, args.benign)
    titles = {o.sigma_id: o.title for o in result.outcomes}
    for sid, event in hits.items():
        print(f"{sid}  {titles.get(sid, '')}  <- '{event}'")
    print(f"{len(hits)} rule(s) alert on benign events")
    if args.write and hits:
        current = load_quarantine(args.quarantine)
        for sid, event in hits.items():
            current[sid] = f"{titles.get(sid, '')} - alerts on benign event '{event}'"
        Path(args.quarantine).write_text(
            "# Sigma rules kept out of the Wazuh build until they are fixed (id: reason).\n"
            + yaml.safe_dump(dict(sorted(current.items())), allow_unicode=True, width=200), encoding="utf-8")
        print(f"quarantine updated: {args.quarantine}")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="dectools-wazuh", description="Compile Sigma rules to Wazuh rules")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build", help="compile rules")
    b.add_argument("--rules", default="rules/sigma", help="Sigma rule directory")
    b.add_argument("--out", default="build/wazuh", help="output directory")
    b.add_argument("--registry", default="wazuh/id_registry.json")
    b.add_argument("--mapping", default=None, help="custom mapping.yml")
    b.add_argument("--quarantine", default="wazuh/quarantine.yml", help="sigma ids kept out of the build")
    b.add_argument("--benign", default="wazuh/benign_events.jsonl", help="benign events that must not alert")
    b.add_argument("--no-mitre", action="store_true", help="omit <mitre> blocks")
    b.add_argument("--update-registry", action="store_true", help="write new ids to the registry file")
    b.add_argument("--check-registry", action="store_true", help="fail if the registry file is out of date")
    b.add_argument("--max-unsupported", type=int, default=None, help="fail if more rules are unsupported")
    t = sub.add_parser("triage", help="find rules that alert on the benign corpus")
    t.add_argument("--rules", default="rules/sigma")
    t.add_argument("--benign", default="wazuh/benign_events.jsonl")
    t.add_argument("--quarantine", default="wazuh/quarantine.yml")
    t.add_argument("--registry", default="wazuh/id_registry.json")
    t.add_argument("--write", action="store_true", help="add the offenders to the quarantine file")
    k = sub.add_parser("bundle", help="package a build for wazuh-deploy-gate")
    k.add_argument("--build", default="build/wazuh")
    k.add_argument("--benign", default="wazuh/benign_events.jsonl")
    k.add_argument("--out", default="build/wazuh-bundle.tar.gz")
    k.add_argument("--git-sha", default="unknown")
    args = ap.parse_args(argv)
    if args.cmd == "bundle":
        return make_bundle(Path(args.build), Path(args.benign), Path(args.out), args.git_sha)
    if args.cmd == "triage":
        return triage(args)

    mapping = Mapping.load(args.mapping)
    registry = IdRegistry.load(args.registry)
    quarantine = load_quarantine(args.quarantine)
    result = build_ruleset(args.rules, mapping, registry, use_mitre=not args.no_mitre, quarantine=quarantine)
    registry.retire_unseen()
    noisy = benign_hits(result, args.benign)

    out = Path(args.out)
    if out.exists():
        shutil.rmtree(out)
    (out / "rules").mkdir(parents=True)
    for name, xml in result.files.items():
        (out / "rules" / name).write_text(xml, encoding="utf-8")
    vectors = []
    for outcome in result.outcomes:
        for r in outcome.rules:
            if is_windows_event_rule(r) and (ev := witness_event(r)):
                vectors.append({"rule_id": r.id, "sigma_id": r.sigma_id, "title": r.sigma_title,
                                "log": to_logtest_json(ev)})
    (out / "testvectors.jsonl").write_text(
        "".join(json.dumps(v, ensure_ascii=False) + "\n" for v in vectors), encoding="utf-8")
    (out / "report.json").write_text(to_json(result), encoding="utf-8")
    (out / "report.md").write_text(to_markdown(result), encoding="utf-8")

    problems = validate_files(out / "rules")
    for p in problems:
        print(f"INVALID: {p}", file=sys.stderr)

    print(to_markdown(result).split("## Why")[0].strip())
    rc = 0
    for sigma_id, event in noisy.items():
        print(f"BENIGN HIT: sigma rule {sigma_id} alerts on benign event '{event}' - fix it or run "
              "`dectools-wazuh triage --write` to quarantine it", file=sys.stderr)
        rc = 1
    if problems:
        rc = 1
    if result.counts.get("error"):
        print(f"{result.counts['error']} rule(s) failed to parse - see report.json", file=sys.stderr)
        rc = 1
    if args.max_unsupported is not None and result.counts.get("unsupported", 0) > args.max_unsupported:
        print("more unsupported rules than allowed", file=sys.stderr)
        rc = 1
    if registry.dirty:
        if args.update_registry:
            registry.save(args.registry)
            print(f"registry updated: {args.registry}")
        elif args.check_registry:
            print(f"{args.registry} is out of date - run with --update-registry and commit it", file=sys.stderr)
            rc = 1
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
