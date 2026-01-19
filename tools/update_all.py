import os
import yaml
import re
import json

def get_rule_data():
    sigma_dir = 'rules/sigma'
    techniques_found = {} 
    rules_count = 0
    if not os.path.exists(sigma_dir):
        return {}, 0
    for root, dirs, files in os.walk(sigma_dir):
        for file in files:
            if file.endswith('.yaml'):
                rules_count += 1
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
    return techniques_found, rules_count

def generate_matrix_svg(techniques_found):
    colors = {"critical": "#ff6666", "high": "#ff6666", "medium": "#ffbd66", "low": "#ffe766"}
    cell_w, cell_h = 55, 25
    gap = 3
    cols, rows = 12, 16 
    
    svg_w = cols * (cell_w + gap)
    svg_h = rows * (cell_h + gap) + 50

    svg = f'<svg width="{svg_w}" height="{svg_h}" xmlns="http://www.w3.org/2000/svg">'
    svg += '<rect width="100%" height="100%" fill="#ffffff" rx="8"/>'
    
    all_tids = sorted(list(techniques_found.keys()))
    count = 0
    for r in range(rows):
        for c in range(cols):
            x, y = c * (cell_w + gap) + 5, r * (cell_h + gap) + 5
            if count < len(all_tids):
                tid = all_tids[count]
                color = colors.get(techniques_found[tid], "#ffe766")
                label = tid
                opacity = "1.0"
                count += 1
            else:
                color = "#eeeeee"
                label = ""
                opacity = "0.4"
            
            svg += f'<rect x="{x}" y="{y}" width="{cell_w}" height="{cell_h}" fill="{color}" opacity="{opacity}" stroke="#d0d0d0" stroke-width="0.5" rx="3"/>'
            if label:
                svg += f'<text x="{x+cell_w/2}" y="{y+cell_h/2+4}" font-family="Segoe UI,Arial" font-size="9" text-anchor="middle" font-weight="600" fill="#222">{label}</text>'

    # Legend
    svg += f'<g transform="translate(10, {rows * (cell_h + gap) + 20})">'
    svg += '<circle cx="5" cy="5" r="5" fill="#ff6666"/><text x="15" y="9" font-family="Arial" font-size="11">High</text>'
    svg += '<circle cx="65" cy="5" r="5" fill="#ffbd66"/><text x="75" y="9" font-family="Arial" font-size="11">Medium</text>'
    svg += '<circle cx="140" cy="5" r="5" fill="#ffe766"/><text x="150" y="9" font-family="Arial" font-size="11">Low</text>'
    svg += '<circle cx="200" cy="5" r="5" fill="#eeeeee"/><text x="210" y="9" font-family="Arial" font-size="11">Nincs lefedve</text>'
    svg += '</g></svg>'

    with open('mitre_matrix.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def update_all():
    techniques, rules_count = get_rule_data()
    generate_matrix_svg(techniques)
    
    USER = "horvath21tamas-gif"
    REPO = "detection-engineering"
    BRANCH = "test"
    
    # Statisztika számítása (kb. 200 technika van az Enterprise mátrixban)
    total_mitre_tech = 201 
    coverage_pct = round((len(techniques) / total_mitre_tech) * 100, 1)
    
    raw_json_url = f"https://raw.githubusercontent.com/{USER}/{REPO}/{BRANCH}/attack_navigator_layer.json"
    navigator_link = f"https://mitre-attack.github.io/attack-navigator/#layerURL={raw_json_url}"

    layer = {
        "name": "Detection Coverage",
        "versions": {"attack": "14", "navigator": "4.9", "layer": "4.4"},
        "domain": "enterprise-attack",
        "techniques": [{"techniqueID": tid, "color": "#ff6666" if lvl in ['high','critical'] else "#ffbd66"} for tid, lvl in techniques.items()]
    }
    with open('attack_navigator_layer.json', 'w', encoding='utf-8') as f:
        json.dump(layer, f, indent=4)

    readme_content = f"""# 🛡️ Detection Engineering Dashboard

## 📊 Összesített Statisztika
- **Lefedett technikák:** `{len(techniques)}` db
- **Sigma szabályok:** `{rules_count}` db
- **MITRE ATT&CK Lefedettség:** `[{coverage_pct}%]`

![Progress Bar](https://geps.dev/progress/{int(coverage_pct)}?dangerColor=ff6666&warningColor=ffbd66&successColor=8ecb88)

## 🗺️ MITRE ATT&CK Mátrix Vizualizáció
![MITRE Matrix](./mitre_matrix.svg)

## 🔗 Interaktív Navigator
🚀 [**Kattints ide a teljes interaktív mátrix megnyitásához**]({navigator_link})

---
*Ez a dokumentum automatikusan frissül minden commit után.*
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_all()
