#!/usr/bin/env python3
"""Best-effort conversion to QRadar (AQL), NetWitness and Microsoft Sentinel (KQL).

These backends need old pySigma (<0.11) and cannot share an environment with the core
tooling, so they run in their own CI job (.github/workflows/legacy-siem.yml, Python 3.11).
Differences to the old pipeline: Sigma sources are never rewritten, failed rules are not
replaced by "conversion_failed" placeholder files, failures are listed in _failures.json.

    python tools/convert_legacy.py --out build/legacy
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


def sigma_cli(target: str, args: list[str], rule: Path) -> str:
    proc = subprocess.run(
        ["sigma", "convert", "-t", target, *args, str(rule)],
        capture_output=True, text=True, timeout=120, check=False,
    )
    out = proc.stdout.strip()
    if proc.returncode != 0 or not out or out.startswith(("Error", "Usage:")):
        raise RuntimeError((proc.stderr or proc.stdout or "no output").strip().splitlines()[-1][:300])
    return out


def sentinel(rule: Path) -> str:
    from sigma.backends.azure import AzureBackend
    from sigma.collection import SigmaCollection

    result = AzureBackend().convert(SigmaCollection.from_yaml(rule.read_text(encoding="utf-8")))
    if not result:
        raise RuntimeError("backend produced no query")
    return str(result[0])


TARGETS = {
    "qradar": (".aql", lambda r: sigma_cli("qradar", ["--without-pipeline"], r)),
    "netwitness": (".txt", lambda r: sigma_cli("net_witness", [], r)),
    "sentinel": (".kql", sentinel),
}


def convert_one(job):
    target, rule, out_dir = job
    ext, fn = TARGETS[target]
    try:
        (out_dir / target / f"{rule.stem}{ext}").write_text(fn(rule) + "\n", encoding="utf-8")
        return target, rule.name, None
    except Exception as exc:  # noqa: BLE001 - reported, never hidden
        return target, rule.name, f"{type(exc).__name__}: {exc}"[:300]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--rules", default="rules/sigma")
    ap.add_argument("--out", default="build/legacy")
    ap.add_argument("--target", action="append", choices=sorted(TARGETS))
    ap.add_argument("--jobs", type=int, default=4)
    args = ap.parse_args(argv)

    out = Path(args.out)
    targets = args.target or sorted(TARGETS)
    for t in targets:
        (out / t).mkdir(parents=True, exist_ok=True)
    rules = [p for p in sorted(Path(args.rules).rglob("*")) if p.suffix in (".yml", ".yaml")]
    jobs = [(t, r, out) for t in targets for r in rules]
    failures: dict[str, list] = {t: [] for t in targets}
    with ThreadPoolExecutor(args.jobs) as pool:
        for target, name, err in pool.map(convert_one, jobs):
            if err:
                failures[target].append({"rule": name, "error": err})
    for t in targets:
        (out / t / "_failures.json").write_text(json.dumps(failures[t], indent=1), encoding="utf-8")
        print(f"{t:10} converted {len(rules) - len(failures[t]):4}  failed {len(failures[t]):4}")
    return 0  # best effort: the job reports, it does not gate


if __name__ == "__main__":
    sys.exit(main())
