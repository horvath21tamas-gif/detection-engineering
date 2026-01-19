import os
import yaml
import re
import json

def get_rule_data():
    """Összegyűjti a MITRE technikákat a Sigma szabályokból."""
    sigma_dir = 'rules/sigma'
    techniques_found = {}
    
    if not os.path.exists(sigma_dir):
        return {}

    for root, dirs, files in os.walk(sigma_dir):
        for file in files:
            if file.endswith('.yaml'):
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        content = yaml.safe_load(f)
                        level = str(content.get('level', 'low')).lower()
                        # MITRE tagek keresése
                        for tag in content.get('tags', []):
                            match = re.search(r't\d{4}(?:\.\d{3})?', tag.lower())
                            if match:
                                tid = match.group(0).upper()
                                # Színezési prioritás (High felülírja a Low-t)
                                if tid not in techniques_found or level in ['high', 'critical']:
                                    techniques_found[tid] = level
                except:
                    continue
    return techniques_found

def generate_visual_matrix(techniques_found):
    """Létrehoz egy SVG képet a lefedettségről."""
    colors = {"critical": "#ff6666", "high": "#ff6666", "medium": "#ffbd66", "low": "#ffe766"}
    
    cell_w, cell_h = 80, 40
    gap = 4
    cols = 10
    
    tids = sorted(techniques_found.keys())
    if not tids:
        # Ha nincs technika, csinálunk egy üres jelzést
        svg = '<svg width="200" height="50" xmlns="http://www.w3.org/2000/svg"><text x="10" y="30">Nincs detektált technika</text></svg>'
    else:
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
            svg += f'<text x="{x+cell_w/2}" y="{y+cell_h/2+5}" font-family="sans-serif" font-size="11" text-anchor="middle" font-weight="bold" fill="#000">{tid}</text>'
        svg += '</svg>'
    
    with open('mitre_matrix.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def update_all():
    """Fő folyamat: adatok gyűjtése, kép és JSON generálás, README frissítés."""
    # 1. Adatok begyűjtése
    techniques = get_rule_data()
    
    # 2. SVG kép generálása
    generate_visual_matrix(techniques)
    
    # 3. Navigator JSON generálása (manuális feltöltéshez)
    layer = {
        "name": "Detection Coverage",
        "versions": {"attack": "14", "navigator": "4.9", "layer": "4.4"},
        "domain": "enterprise-attack",
        "techniques": [{"techniqueID": tid, "color": "#ff6666" if lvl in ['high','critical'] else "#ffbd66"} for tid, lvl in techniques.items()]
    }
    with open('attack_navigator_layer.json', 'w', encoding='utf-8') as f:
        json.dump(layer, f, indent=4)

    # 4. README frissítése (Private repo kompatibilis)
    USER = "horvath21tamas-gif"
    REPO = "detection-engineering"
    BRANCH = "test"

    readme_content = f"""# 🛡️ Detection Engineering Dashboard

## 📊 MITRE ATT&CK Lefedettségi Kép
Ez az ábra a privát szabályaid alapján generálódik:

![MITRE Matrix](https://raw.githubusercontent.com/{USER}/{REPO}/{BRANCH}/mitre_matrix.svg)

> [!IMPORTANT]
> **Interaktív Navigator használata:**
> Mivel a repository **Private**, a közvetlen link nem működik. 
> 1. Nyisd meg a [MITRE Navigatort](https://mitre-attack.github.io/attack-navigator/).
> 2. Kattints: **Open Existing Layer** -> **Upload from local**.
> 3. Válaszd ki az [attack_navigator_layer.json](./attack_navigator_layer.json) fájlt.
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_all()
