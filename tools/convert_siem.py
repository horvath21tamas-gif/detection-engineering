#!/usr/bin/env python3
"""Convert Sigma rules to Splunk (SPL) and Elastic (Lucene) queries.

Replaces the old shell loop: no placeholder "conversion_failed" files, no rewriting of
the Sigma sources. Failures are listed in <out>/<target>/_failures.json and make the
run fail when they exceed --max-failures, so a regression is visible in CI.

    python tools/convert_siem.py --out build/siem [--target splunk --target elastic]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from sigma.backends.elasticsearch import LuceneBackend
from sigma.backends.splunk import SplunkBackend
from sigma.collection import SigmaCollection
from sigma.pipelines.elasticsearch.windows import ecs_windows
from sigma.pipelines.splunk import splunk_windows_pipeline

TARGETS = {
    "splunk": (lambda win: SplunkBackend(splunk_windows_pipeline() if win else None), ".spl"),
    "elastic": (lambda win: LuceneBackend(ecs_windows() if win else None), ".kql"),
}


def convert_all(rules_dir: Path, out_dir: Path, targets: list[str]) -> dict[str, dict]:
    summary: dict[str, dict] = {}
    for target in targets:
        factory, ext = TARGETS[target]
        target_dir = out_dir / target
        target_dir.mkdir(parents=True, exist_ok=True)
        ok, failures = 0, []
        for path in sorted(rules_dir.rglob("*")):
            if path.suffix not in (".yml", ".yaml"):
                continue
            try:
                rule = SigmaCollection.from_yaml(path.read_text(encoding="utf-8")).rules[0]
                windows = (rule.logsource.product or "").lower() == "windows"
                queries = factory(windows).convert_rule(rule)
                if not queries:
                    raise ValueError("backend produced no query")
                (target_dir / f"{path.stem}{ext}").write_text("\n".join(map(str, queries)) + "\n", encoding="utf-8")
                ok += 1
            except Exception as exc:  # noqa: BLE001 - every failure is reported, none is hidden
                failures.append({"rule": path.name, "error": f"{type(exc).__name__}: {exc}"[:300]})
        (target_dir / "_failures.json").write_text(json.dumps(failures, indent=1), encoding="utf-8")
        summary[target] = {"converted": ok, "failed": len(failures)}
    return summary


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rules", default="rules/sigma")
    ap.add_argument("--out", default="build/siem")
    ap.add_argument("--target", action="append", choices=sorted(TARGETS))
    ap.add_argument("--max-failures", type=int, default=0)
    args = ap.parse_args(argv)
    summary = convert_all(Path(args.rules), Path(args.out), args.target or sorted(TARGETS))
    bad = False
    for target, s in summary.items():
        print(f"{target:8} converted {s['converted']:4}  failed {s['failed']:4}")
        bad |= s["failed"] > args.max_failures
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
