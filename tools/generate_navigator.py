import json
import yaml
import os
import re

def generate_layer():
    sigma_path = 'rules/sigma'
    layer_path = 'attack_navigator_layer.json'
    
    # Színkódok a súlyosság alapján
    colors = {
        "critical": "#ff6666",
        "high": "#ff6666",
        "medium": "#ffbd66",
        "low": "#ffe766",
        "informational": "#ffe766"
    }

    techniques_data = {}

    # Végigmegyünk az összes Sigma szabályon
    for root, dirs, files in os.walk(sigma_path):
        for file in files:
            if file.endswith('.yaml'):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        rule = yaml.safe_load(f)
                        
                        level = rule.get('level', 'low').lower()
                        tags = rule.get('tags', [])
                        
                        for tag in tags:
                            # Megkeressük a TXXXX formátumú ID-kat a tagek között
                            match = re.search(r't\d{4}(?:\.\d{3})?', tag.lower())
                            if match:
                                tid = match.group(0).upper()
                                # Ha egy technika több szabályban is van, a legerősebbet vesszük alapul
                                if tid not in techniques_data or level == 'high' or level == 'critical':
                                    techniques_data[tid] = level
                except Exception as e:
                    print(f"Hiba a {file} feldolgozásakor: {e}")

    # Navigator Layer felépítése
    layer = {
        "name": "Detection Coverage by Severity",
        "versions": {"attack": "14", "navigator": "4.9", "layer": "4.4"},
        "domain": "enterprise-attack",
        "description": "Sigma szabályok lefedettsége súlyosság szerint színezve",
        "filters": {"platforms": ["Windows", "Linux"]},
        "techniques": [
            {
                "techniqueID": tid,
                "color": colors.get(lvl, "#3182bd"),
                "comment": f"Súlyosság: {lvl}",
                "enabled": True
            } for tid, lvl in techniques_data.items()
        ],
        "legendItems": [
            {"label": "High / Critical", "color": "#ff6666"},
            {"label": "Medium", "color": "#ffbd66"},
            {"label": "Low", "color": "#ffe766"}
        ]
    }

    with open(layer_path, 'w', encoding='utf-8') as f:
        json.dump(layer, f, indent=4)
    print(f"Navigator layer elkészült {len(techniques_data)} technikával.")

if __name__ == "__main__":
    generate_layer()
