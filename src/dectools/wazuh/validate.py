"""Static validation of generated Wazuh rule files (no Wazuh needed)."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import regex
from lxml import etree

LEVEL_RANGE = range(0, 16)


def validate_files(rules_dir: str | Path) -> list[str]:
    problems: list[str] = []
    ids: Counter = Counter()
    for path in sorted(Path(rules_dir).glob("*.xml")):
        try:
            root = etree.parse(str(path)).getroot()
        except etree.XMLSyntaxError as exc:
            problems.append(f"{path.name}: XML error: {exc}")
            continue
        for rule in root.iter("rule"):
            rid = rule.get("id")
            ids[rid] += 1
            if int(rule.get("level", -1)) not in LEVEL_RANGE:
                problems.append(f"{path.name}: rule {rid}: bad level")
            if rule.find("description") is None:
                problems.append(f"{path.name}: rule {rid}: no description")
            for el in list(rule.iter("field")) + list(rule.iter("regex")):
                if el.get("type") != "pcre2":
                    problems.append(f"{path.name}: rule {rid}: non-pcre2 match")
                    continue
                try:
                    regex.compile(el.text or "", regex.V0)
                except regex.error as exc:
                    problems.append(f"{path.name}: rule {rid}: bad regex {el.text!r}: {exc}")
            names = [f.get("name") for f in rule.iter("field")]
            if len(names) != len(set(names)):
                problems.append(f"{path.name}: rule {rid}: repeated <field> name")
    problems += [f"duplicate rule id {i}" for i, n in ids.items() if n > 1]
    return problems
