"""One-off repair: add the missing `|re|i` modifier to Sigma fields whose values are all regexes.

Without `|re` Sigma treats `(a\\.exe|b\\.exe)$` as a LITERAL string, so the rule never matches.
Only unmodified keys (exact match) whose every string value looks like a regex are converted;
`|contains` keys are left alone (their backslash/dot values are normally literal paths).
Runs of 4+ backslashes in single-quoted/plain scalars are halved (the authors double-escaped).

Usage: python tools/maintenance/fix_regex_fields.py [--write] [rules/sigma]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml
from yaml.nodes import MappingNode, ScalarNode, SequenceNode

REGEXY = re.compile(
    r"(\.\*|\.\+|\\\.|\(\?[:i=!]|\[[^\]]+\][+*{]|\\[dws][+*{]|\([^()]*\|[^()]*\)|^\^|\)\$$)"
)


def halve(m: re.Match) -> str:
    return "\\" * (len(m.group(0)) // 2)


def fix_text(text: str) -> tuple[str, int]:
    root = yaml.compose(text)
    if not isinstance(root, MappingNode):
        return text, 0
    det = next((v for k, v in root.value if k.value == "detection"), None)
    if not isinstance(det, MappingNode):
        return text, 0
    lines = text.split("\n")
    jobs = []  # (key_line, key_col, key_text, [(line, col_start, col_end)])

    def maps(node):
        if isinstance(node, MappingNode):
            yield node
        elif isinstance(node, SequenceNode):
            for x in node.value:
                yield from maps(x)

    for sel_key, sel in det.value:
        if sel_key.value == "condition":
            continue
        for m in maps(sel):
            for k, v in m.value:
                if "|" in k.value:
                    continue
                vals = v.value if isinstance(v, SequenceNode) else [v]
                if not vals or not all(isinstance(x, ScalarNode) and x.tag.endswith("str") for x in vals):
                    continue
                if not all(REGEXY.search(x.value) for x in vals):
                    continue
                if any(x.style == '"' for x in vals):
                    print(f"  skip (double-quoted): {k.value}")
                    continue
                jobs.append((k, vals))
    for k, vals in sorted(jobs, key=lambda j: -j[0].start_mark.line):
        for x in sorted(vals, key=lambda x: -x.start_mark.line):
            ln = x.start_mark.line
            if x.start_mark.line != x.end_mark.line:
                continue
            seg = lines[ln]
            a, b = x.start_mark.column, x.end_mark.column
            lines[ln] = seg[:a] + re.sub(r"\\{4,}", halve, seg[a:b]) + seg[b:]
        kl, kc = k.start_mark.line, k.start_mark.column
        lines[kl] = lines[kl][:kc] + k.value + "|re|i" + lines[kl][kc + len(k.value):]
    return "\n".join(lines), len(jobs)


def main(argv: list[str]) -> int:
    write = "--write" in argv
    args = [a for a in argv if not a.startswith("--")]
    root = Path(args[0] if args else "rules/sigma")
    files = fields = 0
    for p in sorted(root.rglob("*.y*ml")):
        t = p.read_text(encoding="utf-8")
        new, n = fix_text(t)
        if n:
            files += 1
            fields += n
            if write:
                p.write_text(new, encoding="utf-8")
    print(f"{'fixed' if write else 'would fix'} {fields} field(s) in {files} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
