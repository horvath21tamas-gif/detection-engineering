import json
import re
import os

def generate_layer():
    readme_path = 'README.md'
    layer_path = 'attack_navigator_layer.json'
    
    if not os.path.exists(readme_path):
        print("README.md nem található!")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Megkeressük az összes TXXXX vagy TXXXX.XXX formátumú ID-t
    techniques = list(set(re.findall(r'T\d{4}(?:\.\d{3})?', content)))
    
    # MITRE Navigator Layer struktúra
    layer = {
        "name": "Detection Coverage",
        "versions": {
            "attack": "14",
            "navigator": "4.9",
            "layer": "4.4"
        },
        "domain": "enterprise-attack",
        "description": f"Automatikusan generált lefedettség: {len(techniques)} technika",
        "filters": {"platforms": ["Windows", "Linux", "macOS"]},
        "techniques": [
            {
                "techniqueID": tid,
                "color": "#3182bd", # Kék szín
                "comment": "Kész Sigma szabály elérhető",
                "enabled": True
            } for tid in techniques
        ],
        "gradient": {
            "colors": ["#ff6666", "#ffe766", "#8ecb88"],
            "minValue": 0,
            "maxValue": 100
        },
        "legendItems": [
            {"label": "Lefedett technikák", "color": "#3182bd"}
        ]
    }

    with open(layer_path, 'w', encoding='utf-8') as f:
        json.dump(layer, f, indent=4)
    print(f"Navigator layer elkészült {len(techniques)} technikával.")

if __name__ == "__main__":
    generate_layer()
