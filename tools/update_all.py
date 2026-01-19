import os
import yaml
import re
import json

def get_rule_data():
    sigma_dir = 'rules/sigma'
    rules = []
    techniques_found = {}

    if not os.path.exists(sigma_dir):
        return rules, techniques_found

    for root, dirs, files in os.walk(sigma_dir):
        for file in files:
            if file.endswith('.yaml'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = yaml.safe_load(f)
                        if not content: continue
                        level = str(content.get('level', 'low')).lower()
                        tags = content.get('tags', [])
                        for tag in tags:
                            match = re.search(r't\d{4}(?:\.\d{3})?', tag.lower())
                            if match:
                                tid = match.group(0).upper()
                                if tid not in techniques_found or level in ['high', 'critical']:
                                    techniques_found[tid] = level
                        rules.append({"name": file, "level": level})
                except: continue
    return rules, techniques_found

def generate_svg_map(techniques_found):
    """Létrehoz egy vizuális mátrix ábrát SVG formátumban."""
    colors = {"critical": "#ff6666", "high": "#ff6666", "medium": "#ffbd66", "low": "#ffe766"}
    
    # SVG beállítások
    rect_width = 60
    rect_height = 30
    padding = 5
    cols = 8
    
    sorted_tids = sorted(techniques_found.keys())
    num_tech = len(sorted_tids)
    rows = (num_tech // cols) + (1 if num_tech % cols != 0 else 0)
    rows = max(rows, 1)

    svg_width = cols * (rect_width + padding) + padding
    svg_height = rows * (rect_height + padding) + padding

    svg_header = f'<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">'
    svg_content = '<rect width="100%" height="100%" fill="#f6f8fa" rx="10"/>' # Háttér
    
    for i, tid in enumerate(sorted_tids):
        lvl = techniques_found[tid]
        color = colors.get(lvl, "#ffe766")
        r = i // cols
        c = i % cols
        x = c * (rect_width + padding) + padding
        y = r * (rect_height + padding) + padding
        
        svg_content += f'''
        <g>
            <rect x="{x}" y="{y}" width="{rect_width}" height="{rect_height}" fill="{color}" rx="4" stroke="#333" stroke-width="0.5"/>
            <text x="{x + rect_width/2}" y="{y + rect_height/2 + 5}" font-family="Arial" font-size="10" text-anchor="middle" fill="#000">{tid}</text>
        </g>'''
    
    svg_footer = '</svg>'
    
    with open('coverage_map.svg', 'w', encoding='utf-8') as f:
        f.write(svg_header + svg_content + svg_footer)

def update_files():
    rules, techniques_found = get_rule_data()
    
    # 1. SVG Ábra generálása
    generate_svg_map(techniques_found)

    # 2. Navigator JSON (háttérnek)
    colors = {"critical": "#ff6666", "high": "#ff6666", "medium": "#ffbd66", "low": "#ffe766"}
    layer = {
        "name": "Coverage",
        "versions": {"attack": "14", "navigator": "4.9", "layer": "4.4"},
        "domain": "enterprise-attack",
        "techniques": [{"techniqueID": tid, "color": colors.get(lvl, "#ffe766")} for tid, lvl in techniques_found.items()]
    }
    with open('attack_navigator_layer.json', 'w') as f:
        json.dump(layer, f, indent=4)

    # 3. README frissítése (Kép beágyazással)
    USER = "horvath21tamas"
    REPO = "detection-engineering"
    BRANCH = "test"
    
    coverage_pct = round((len(techniques_found) / 201) * 100, 1)
    raw_json_url = f"https://raw.githubusercontent.com/{USER}/{REPO}/{BRANCH}/attack_navigator_layer.json"
    navigator_link = f"https://mitre-attack.github.io/attack-navigator/#layerURL={raw_json_url}"

    readme_content = f"""# 🛡️ Detection Engineering Dashboard

## 📊 Lefedettségi Vizualizáció
Ez az ábra automatikusan frissül a szabályok alapján:

![MITRE Coverage Map](coverage_map.svg)

**Jelmagyarázat:** 🔴 High/Critical | 🟠 Medium | 🟡 Low

---
### 📈 Statisztikák
- **Lefedettség:** {coverage_pct}%
- **Szabályok száma:** {len(rules)} db
- **Részletes lista:** [COVERAGE.md](./COVERAGE.md)
- **Interaktív Navigator:** [Kattints ide]({navigator_link})
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_files()
