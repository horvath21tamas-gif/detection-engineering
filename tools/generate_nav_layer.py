import yaml
import json
import os

def generate_layer():
    sigma_path = 'rules/sigma'
    techniques = {}

    for root, _, files in os.walk(sigma_path):
        for file in files:
            if file.endswith('.yaml'):
                with open(os.path.join(root, file), 'r') as f:
                    data = yaml.safe_load(f)
                    tags = data.get('tags', [])
                    for tag in tags:
                        if tag.startswith('attack.t'):
                            t_code = tag.split('.')[-1].upper()
                            techniques[t_code] = techniques.get(t_code, 0) + 1

    layer = {
        "name": "Detection Coverage",
        "versions": {"attack": "14", "navigator": "4.8.0", "layer": "4.3"},
        "domain": "enterprise-attack",
        "techniques": [
            {"techniqueID": t, "score": count, "comment": f"{count} szabály"}
            for t, count in techniques.items()
        ],
        "gradient": {"colors": ["#ff6666", "#66ff66"], "minValue": 1, "maxValue": 10}
    }

    with open('attack_navigator_layer.json', 'w') as f:
        json.dump(layer, f, indent=4)
    print("✅ MITRE Layer generálva.")

if __name__ == "__main__":
    generate_layer()
