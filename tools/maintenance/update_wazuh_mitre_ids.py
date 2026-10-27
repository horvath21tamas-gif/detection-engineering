"""Refresh src/dectools/wazuh/mitre_ids.json from the ATT&CK data shipped with a Wazuh release.

Wazuh only knows the techniques in its bundled MITRE database; a <mitre><id> it does not know
can make rule loading fail or warn. The converter therefore only emits ids from this list.

    python tools/maintenance/update_wazuh_mitre_ids.py [wazuh_version]   # default 4.9.0
"""

import json
import sys
import urllib.request
from pathlib import Path

version = sys.argv[1] if len(sys.argv) > 1 else "4.9.0"
url = f"https://raw.githubusercontent.com/wazuh/wazuh/v{version}/ruleset/mitre/enterprise-attack.json"
data = json.load(urllib.request.urlopen(url, timeout=120))
ids = sorted({
    ref["external_id"]
    for obj in data["objects"]
    if obj.get("type") == "attack-pattern" and not obj.get("revoked") and not obj.get("x_mitre_deprecated")
    for ref in obj.get("external_references", [])
    if ref.get("source_name") == "mitre-attack"
})
out = Path(__file__).resolve().parents[2] / "src" / "dectools" / "wazuh" / "mitre_ids.json"
out.write_text(json.dumps({"wazuh_version": version, "ids": ids}, indent=0) + "\n", encoding="utf-8")
print(f"{len(ids)} technique ids from Wazuh {version} -> {out}")
