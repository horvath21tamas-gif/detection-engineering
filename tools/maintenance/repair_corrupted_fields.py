"""One-off repair: restore Sigma field names that tools/preprocess_sigma.py corrupted.

The old pipeline rewrote the *source* rules in place (``Image:`` -> ``processname:``,
``User:`` -> ``username:`` ...), also inside longer names (``ParentImage:`` became
``Parentprocessname:``). Sigma only knows the original names, so every converter
other than QRadar silently matched on non-existent fields.

Usage:  python tools/maintenance/repair_corrupted_fields.py [--write] [rules/sigma]
Without --write it only reports what would change.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

REPAIR = {
    "username": "User",
    "processname": "Image",
    "Parentprocessname": "ParentImage",
    "Targetprocessname": "TargetImage",
    "Sourceprocessname": "SourceImage",
    "processcommandline": "CommandLine",
    "parentprocessname": "ParentImage",
    "parentprocesscommandline": "ParentCommandLine",
    "Parentprocesscommandline": "ParentCommandLine",
    "logonid": "LogonId",
    "Subjectlogonid": "SubjectLogonId",
    "filename": "TargetFilename",
    "hash": "Hashes",
}
KEY = re.compile(r"^(?P<indent>\s*(?:-\s+)?)(?P<key>" + "|".join(map(re.escape, REPAIR)) + r")(?P<mods>(?:\|[A-Za-z0-9_|]+)?):", re.M)


def main(argv: list[str]) -> int:
    write = "--write" in argv
    args = [a for a in argv if not a.startswith("--")]
    root = Path(args[0] if args else "rules/sigma")
    changed, stats = 0, Counter()
    for path in sorted(root.rglob("*.y*ml")):
        text = path.read_text(encoding="utf-8")
        new = KEY.sub(lambda m: stats.update([m["key"]]) or f"{m['indent']}{REPAIR[m['key']]}{m['mods']}:", text)
        if new != text:
            changed += 1
            if write:
                path.write_text(new, encoding="utf-8")
    print(f"{'repaired' if write else 'would repair'} {changed} files")
    for key, n in stats.most_common():
        print(f"  {key:>26} -> {REPAIR[key]:<18} x{n}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
