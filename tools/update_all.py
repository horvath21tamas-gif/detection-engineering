import os
import yaml
import re
import json

def get_rule_data():
    sigma_dir = 'rules/sigma'
    techniques_found = {} # ID: Level
    
    if not os.path.exists(sigma_dir):
        return {}, {}

    for root, dirs, files in os.walk(sigma_dir):
        for file in files:
            if file.endswith('.yaml'):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        content = yaml.safe_load(f)
                        level = str(content.get('level', 'low')).lower()
                        for tag in content.get('tags', []):
                            match = re.search(r't\d{4}(?:\.\d{3})?', tag.lower())
                            if match:
                                tid = match.group(0).upper()
                                if tid not in techniques_found or level in ['high', 'critical']:
                                    techniques_found[tid] = level
                except: continue
    return techniques_found

def generate_visual_matrix(techniques_found):
    """Egy SVG képet generál, ami úgy néz ki, mint a MITRE Navigator mátrix."""
    colors = {"critical": "#ff6666", "high": "#ff6666", "medium": "#ffbd66", "low": "#ffe766"}
    
    # SVG Paraméterek
    cell_w, cell_h = 80, 40
    gap = 4
    cols = 10
    
    tids = sorted(techniques_found.keys())
    rows = (len(tids) // cols) + (1 if len(tids) % cols != 0 else 0)
    
    width = cols * (cell_w + gap) + gap
    height = rows * (cell_h + gap) + gap

    svg = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">'
    svg += '<rect width="100%" height="100%" fill="#ffffff"/>'

    for i, tid in enumerate(tids):
        r, c = i // cols, i % cols
        x, y = c * (cell_w + gap) + gap, r * (cell_h + gap) + gap
        color = colors.get(techniques_found[tid], "#ffe766")
        
        svg += f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{color}" stroke="#333" stroke-width="1" rx="2"/>'
        svg += f'<text x="{x+cell_w/2}" y="{y+cell_h/2+5}" font-family="sans-serif" font-size="11" text-anchor="middle" font-weight="bold">{tid}</text>'

    svg += '</svg>'
    
    with open('mitre_matrix.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def update_all():
    techniques = get_rule_data()
    
    # 1. Kép generálása (ez jelenik meg a README-ben)
    generate_visual_matrix(techniques)
    
    # 2. JSON generálása (hogy a link is működjön ha rákkattintanak)
    layer = {
        "name": "Detection Coverage",
        "versions": {"attack": "14", "navigator": "4.9", "layer": "4.4"},
        "domain": "enterprise-attack",
        "techniques": [{"techniqueID": tid, "color": "#ff6666" if lvl in ['high','critical'] else "#ffbd66"} for tid, lvl in techniques.items()]
    }
    with open('attack_navigator_layer.json', 'w') as f:
        json.dump(layer, f, indent=4)

    # 3. README.md frissítése
    readme_content = f"""# 🛡️ Detection Engineering Dashboard

## 📊 MITRE ATT&CK Lefedettségi Kép
Ez az ábra automatikusan frissül a szabályok alapján:

![MITRE Matrix](./mitre_matrix.svg)

[👉 Kattints ide az interaktív Navigator megnyitásához](https://mitre-attack.github.io/attack-navigator/#layerURL=https://raw.githubusercontent.com/horvath21tamas-gif/detection-engineering/test/attack_navigator_layer.json)
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_all()
