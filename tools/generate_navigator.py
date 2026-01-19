import json
import yaml
import os
import re

def generate_navigator_and_stats():
    sigma_path = 'rules/sigma/credential_access' # Itt vannak a szabályaid
    layer_path = 'attack_navigator_layer.json'
    
    colors = {"critical": "#ff6666", "high": "#ff6666", "medium": "#ffbd66", "low": "#ffe766"}
    techniques_data = {}

    # Beolvasás és elemzés
    for root, dirs, files in os.walk(sigma_path):
        for file in files:
            if file.endswith('.yaml'):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        rule = yaml.safe_load(f)
                        level = rule.get('level', 'low').lower()
                        for tag in rule.get('tags', []):
                            match = re.search(r't\d{4}(?:\.\d{3})?', tag.lower())
                            if match:
                                tid = match.group(0).upper()
                                if tid not in techniques_data or level in ['high', 'critical']:
                                    techniques_data[tid] = level
                except: continue

    # JSON Layer mentése (ez kell a színezéshez)
    layer = {
        "name": "Detection Coverage",
        "versions": {"attack": "14", "navigator": "4.9", "layer": "4.4"},
        "domain": "enterprise-attack",
        "techniques": [
            {"techniqueID": tid, "color": colors.get(lvl, "#ffe766"), "comment": f"Level: {lvl}", "enabled": True} 
            for tid, lvl in techniques_data.items()
        ]
    }
    
    with open(layer_path, 'w') as f:
        json.dump(layer, f, indent=4)

    # Százalékos lefedettség számítása (Enterprise ATT&CK ~200 technika)
    coverage_pct = round((len(techniques_data) / 201) * 100, 2)
    return coverage_pct, len(techniques_data)

if __name__ == "__main__":
    generate_navigator_and_stats()
