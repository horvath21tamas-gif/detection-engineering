"""One-off repair: split Sigma selections that repeat the same YAML key.

    selection:                          selection:
      CommandLine|contains: [a, b]  ->    CommandLine|contains: [a, b]
      CommandLine|contains: [c, d]      selection_and2:
                                          CommandLine|contains: [c, d]
    condition: selection                condition: (selection and selection_and2)

YAML silently keeps only the LAST duplicate, so the rule lost its first conditions. The authors
clearly meant AND (every duplicate narrows the match), which is what this script restores.
Only plain mappings inside `detection:` are handled; anything else is reported for manual work.

Usage: python tools/maintenance/fix_duplicate_keys.py [--write] [rules/sigma]
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

import yaml
from yaml.nodes import MappingNode


def region_end(lines: list[str], start: int, boundaries: list[int]) -> int:
    nxt = [b for b in boundaries if b > start]
    end = min(nxt) if nxt else len(lines)
    while end > start and (not lines[end - 1].strip() or lines[end - 1].lstrip().startswith("#")):
        end -= 1
    return end


def fix_text(text: str) -> tuple[str, list[str]]:
    notes: list[str] = []
    root = yaml.compose(text)
    if not isinstance(root, MappingNode):
        return text, notes
    top = {k.value: (k, v) for k, v in root.value}
    if "detection" not in top or not isinstance(top["detection"][1], MappingNode):
        return text, notes
    det_map = top["detection"][1]
    lines = text.split("\n")
    boundaries = sorted({k.start_mark.line for k, _ in root.value} | {k.start_mark.line for k, _ in det_map.value})

    edits = []  # (start_line, end_line, replacement_lines, name, extra_names)
    for key, val in det_map.value:
        if key.value == "condition":
            continue
        if not isinstance(val, MappingNode):
            continue
        names = [k.value for k, _ in val.value]
        dups = {n for n, c in Counter(names).items() if c > 1}
        if not dups:
            continue
        pairs = val.value
        starts = [k.start_mark.line for k, _ in pairs]
        end = region_end(lines, starts[0], boundaries)
        spans = [(starts[i], starts[i + 1] if i + 1 < len(starts) else end) for i in range(len(pairs))]
        seen: Counter = Counter()
        keep, extra = [], {}
        for (k, _), (a, b) in zip(pairs, spans):
            seen[k.value] += 1
            n = seen[k.value]
            chunk = lines[a:b]
            while chunk and not chunk[-1].strip():
                chunk.pop()
            if n == 1:
                keep.append(chunk)
            else:
                extra.setdefault(n, []).extend(chunk)
        indent = " " * key.start_mark.column
        header_line = key.start_mark.line
        body = [ln for c in keep for ln in c]
        block = lines[header_line:starts[0]] + body
        extra_names = []
        for n in sorted(extra):
            nm = f"{key.value}_and{n}"
            extra_names.append(nm)
            block += [f"{indent}{nm}:"] + extra[n]
        edits.append((header_line, end, block, key.value, extra_names))
    if not edits:
        return text, notes

    for start, end, block, _name, _extra in sorted(edits, key=lambda e: -e[0]):
        lines[start:end] = block

    # condition rewrite on the (re-composed) document
    text2 = "\n".join(lines)
    root2 = yaml.compose(text2)
    det2 = dict((k.value, v) for k, v in root2.value)["detection"]
    ckey, cval = next((k, v) for k, v in det2.value if k.value == "condition")
    a, b = ckey.start_mark.line, max(cval.end_mark.line, ckey.start_mark.line) + 1
    lines = text2.split("\n")
    cond = "\n".join(lines[a:b])
    for _s, _e, _blk, name, extra_names in edits:
        repl = "(" + " and ".join([name, *extra_names]) + ")"
        new = re.sub(rf"(?<![\w]){re.escape(name)}(?![\w])", repl, cond)
        if new == cond:
            notes.append(f"condition does not mention '{name}' literally - check by hand")
        cond = new
    lines[a:b] = cond.split("\n")
    return "\n".join(lines), notes


def main(argv: list[str]) -> int:
    write = "--write" in argv
    args = [a for a in argv if not a.startswith("--")]
    root = Path(args[0] if args else "rules/sigma")
    changed = manual = 0
    for path in sorted(root.rglob("*.y*ml")):
        text = path.read_text(encoding="utf-8")
        new, notes = fix_text(text)
        if new != text:
            changed += 1
            if write:
                path.write_text(new, encoding="utf-8")
        for n in notes:
            manual += 1
            print(f"{path.name}: {n}")
    print(f"{'fixed' if write else 'would fix'} {changed} files, {manual} note(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
