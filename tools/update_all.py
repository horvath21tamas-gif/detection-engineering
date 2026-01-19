import os
import yaml
import re
import json

def get_rule_data():
    sigma_dir = 'rules/sigma'
    rules = []
    techniques_found = {} # ID: Level

    for root, dirs, files in os.walk(sigma_dir):
        for file in files:
            if file.endswith('.yaml'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = yaml.safe_load(f)
                        level = content.get('level', 'low').lower()
                        tags = content.get('tags', [])
                        
                        t_ids = []
                        for tag in tags:
                            match = re.search(r't\d{4}(?:\.\d{3})?', tag.lower())
                            if match:
                                tid = match.group(0).upper()
                                t_ids.append(tid)
                                # Navigator színezéshez: a legmagasabb szintet tartjuk meg
                                if tid not in techniques_found or level in ['high', 'critical']:
                                    techniques_found[tid] = level
                        
                        rules.append({
                            "name": file,
                            "title": content.get('title', 'N/A'),
                            "ids": ", ".join(t_ids) if t_ids else "N/A",
                            "level": level
                        })
                except: continue
    return rules, techniques_found

def update_files():
    rules, techniques_found = get_rule_data()
    
    # 1. Részletes lista mentése egy külön fájlba (COVERAGE.md)
    with open('COVERAGE.md', 'w', encoding='utf-8') as f:
        f.write("# 📝 Részletes Szabály Lista\n\n")
        f.write("| Fájlnév | Megnevezés | MITRE ID | Szint |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for r in rules:
            f.write(f"| {r['name']} | {r['title']} | {r['ids']} | {r['level']} |\n")

    # 2. Navigator JSON generálása
    colors = {"critical": "#ff6666", "high": "#ff6666", "medium": "#ffbd66", "low": "#ffe766"}
    layer = {
        "name": "Detection Coverage",
        "versions": {"attack": "14", "navigator": "4.9", "layer": "4.4"},
        "domain": "enterprise-attack",
        "techniques": [
            {"techniqueID": tid, "color": colors.get(lvl, "#ffe766"), "comment": f"Level: {lvl}", "enabled": True} 
            for tid, lvl in techniques_found.items()
        ]
    }
    with open('attack_navigator_layer.json', 'w') as f:
        json.dump(layer, f, indent=4)

    # 3. README.md frissítése statisztikákkal
    total_techniques = 201 # Enterprise ATT&CK alap technikák száma
    coverage_pct = round((len(techniques_found) / total_techniques) * 100, 1)
    
    # Raw link a Navigatorhoz (ezt írd át a sajátodra!)
    raw_json_url = "https://raw.githubusercontent.com/hota05/detection-engineering/test/attack_navigator_layer.json"
    navigator_link = f"https://mitre-attack.github.io/attack-navigator/#layerURL={raw_json_url}"

    readme_content = f"""# 🛡️ Detection Engineering Repository

![Coverage](https://img.shields.io/badge/MITRE_ATT%26CK_Lefedettség-{coverage_pct}%25-blue?style=for-the-badge)
![Rules](https://img.shields.io/badge/Sigma_Szabályok-{len(rules)}_db-green?style=for-the-badge)

## 📊 Összegzés
- **Összes Sigma szabály:** {len(rules)}
- **Lefedett egyedi technikák:** {len(techniques_found)}
- **Részletes lista:** [COVERAGE.md](./COVERAGE.md)

## 🗺️ MITRE ATT&CK Navigator
Kattints az alábbi képre a színes térkép megnyitásához:

[![Navigator](https://raw.githubusercontent.com/mitre-attack/attack-navigator/master/nav-app/src/assets/favicon.ico)]({navigator_link})

*A színek a szabályok súlyosságát jelzik (🔴 High, 🟠 Medium, 🟡 Low).*
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_all()
