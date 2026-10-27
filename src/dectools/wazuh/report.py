"""Coverage report: which Sigma rules were compiled, which not and why."""

from __future__ import annotations

import json
from collections import Counter

from .convert import BuildResult


def to_dict(result: BuildResult) -> dict:
    return {
        "summary": {
            "sigma_rules": len(result.outcomes),
            "converted": result.counts.get("ok", 0),
            "unsupported": result.counts.get("unsupported", 0),
            "quarantined": result.counts.get("quarantined", 0),
            "errors": result.counts.get("error", 0),
            "wazuh_rules": result.rule_count,
        },
        "rules": [
            {
                "path": o.path,
                "sigma_id": o.sigma_id,
                "title": o.title,
                "status": o.status,
                "reason": o.reason,
                "wazuh_ids": [r.id for r in o.rules],
            }
            for o in result.outcomes
        ],
    }


def to_json(result: BuildResult) -> str:
    return json.dumps(to_dict(result), indent=1, ensure_ascii=False) + "\n"


def to_markdown(result: BuildResult) -> str:
    s = to_dict(result)["summary"]
    reasons = Counter(
        "quarantined (see wazuh/quarantine.yml)" if o.status == "quarantined"
        else o.reason.split(":")[0] if o.status == "error" else o.reason
        for o in result.outcomes if o.status != "ok"
    )
    lines = [
        "# Sigma -> Wazuh coverage",
        "",
        f"- Sigma rules: **{s['sigma_rules']}**",
        f"- Converted: **{s['converted']}** -> {s['wazuh_rules']} Wazuh rules",
        f"- Not convertible: **{s['unsupported']}**, quarantined: **{s['quarantined']}**, errors: **{s['errors']}**",
        "",
        "## Why rules were not converted",
        "",
        "| Reason | Rules |",
        "|---|---|",
    ]
    lines += [f"| {r.replace('|', '/')} | {n} |" for r, n in reasons.most_common()]
    return "\n".join(lines) + "\n"
