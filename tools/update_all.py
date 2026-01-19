import os
import yaml
import re
import json

def get_rule_data():
    # A szabályok gyökérmappája
    sigma_dir = 'rules/sigma'
    rules = []
    techniques_found = {} # ID: Level tárolása a színezéshez

    if not os.path.exists(sigma_dir):
        print(f"HIBA: A {sigma_dir} mappa nem található!")
        return rules, techniques_found

    # Szabályok beolvasása rekurzívan
    for root, dirs, files in os.walk(sigma_dir):
        for file in files:
            if file.endswith('.yaml'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = yaml.safe_load(f)
                        if not content: continue
                        
                        # Alapvető metaadatok kinyerése
                        level = str(content.get('level', 'low')).lower()
                        tags = content.get('tags', [])
                        
                        t_ids = []
                        if tags:
                            for tag in tags:
                                # MITRE ATT&CK ID keresése (T1234 vagy T1234.001)
                                match = re.search(r't\d{4}(?:\.\d{3})?', tag.lower())
                                if match:
                                    tid = match.group(0).upper()
                                    t_ids.append(tid)
                                    # Színezési prioritás: a High/Critical felülírja a Low-t
                                    if tid not in techniques_found or level in ['high', 'critical']:
                                        techniques_found[tid] = level
                        
                        rules.append({
                            "name": file,
                            "title": content.get('title', 'N/A'),
                            "ids": ", ".join(t_ids) if t_ids else "N/A",
                            "level": level
                        })
                except Exception as e:
                    print(f"Hiba a fájl feldolgozásakor ({file}): {e}")
                    continue
                    
    return rules, techniques_found

def update_files():
    rules, techniques_found = get_rule_data()
    
    # 1. Részletes táblázat mentése a COVERAGE.md fájlba
    with open('COVERAGE.md', 'w', encoding='utf-8') as f:
        f.write("# 📝 Részletes Szabály Lista\n\n")
        f.write("Ez a fájl automatikusan frissül minden commit után.\n\n")
        f.write("| Fájlnév | Megnevezés | MITRE ID | Szint |\n")
        f.write("| :--- | :--- | :--- | :--- |\n")
        for r in rules:
            f.write(f"| {r['name']} | {r['title']} | {r['ids']} | {r['level']} |\n")

    # 2. MITRE Navigator JSON (Layer) generálása
    # Színkódok a Navigatorhoz
    colors = {
        "critical": "#ff6666", 
        "high": "#ff6666", 
        "medium": "#ffbd66", 
        "low": "#ffe766",
        "informational": "#ffe766"
    }
    
    layer = {
        "name": "Detection Coverage",
        "versions": {"attack": "14", "navigator": "4.9", "layer": "4.4"},
        "domain": "enterprise-attack",
        "description": "Sigma Detection Rules Coverage map",
        "filters": {"platforms": ["windows", "linux", "macos"]},
        "techniques": [
            {
                "techniqueID": tid, 
                "color": colors.get(lvl, "#ffe766"), 
                "comment": f"Súlyosság: {lvl}", 
                "enabled": True
            } for tid, lvl in techniques_found.items()
        ]
    }
    
    with open('attack_navigator_layer.json', 'w', encoding='utf-8') as f:
        json.dump(layer, f, indent=4)

    # 3. README.md frissítése statisztikákkal és interaktív linkkel
    total_techniques = 201 # Becsült technika szám az Enterprise mátrixban
    coverage_pct = round((len(techniques_found) / total_techniques) * 100, 1) if total_techniques > 0 else 0
    
    # --- KONFIGURÁCIÓ: A te elérésed ---
    USER = "horvath21tamas"
    REPO = "detection-engineering"
    BRANCH = "test" 
    # ----------------------------------

    raw_json_url = f"https://raw.githubusercontent.com/{USER}/{REPO}/{BRANCH}/attack_navigator_layer.json"
    navigator_link = f"https://mitre-attack.github.io/attack-navigator/#layerURL={raw_json_url}"

    readme_content = f"""# 🛡️ Detection Engineering Repository

![Coverage](https://img.shields.io/badge/MITRE_ATT%26CK_Lefedettség-{coverage_pct}%25-blue?style=for-the-badge)
![Rules](https://img.shields.io/badge/Sigma_Szabályok-{len(rules)}_db-green?style=for-the-badge)

## 📊 Detektálási Statisztika
- **Összes Sigma szabály:** {len(rules)}
- **Lefedett egyedi MITRE technikák:** {len(techniques_found)}
- **Részletes lista:** [COVERAGE.md](./COVERAGE.md)

## 🗺️ MITRE ATT&CK Navigator (Élő Térkép)
Kattints az alábbi logóra az interaktív, színezett lefedettségi térkép megnyitásához:

[![MITRE Navigator Map](https://raw.githubusercontent.com/mitre-attack/attack-navigator/master/nav-app/src/assets/favicon.ico)]({navigator_link})

> [!IMPORTANT]
> A színek a szabályok súlyosságát tükrözik: 🔴 **High**, 🟠 **Medium**, 🟡 **Low**. 
> Ha a térkép üres vagy hibát dob, ellenőrizd, hogy a repository **Public** (nyilvános) állapotban van-e!

---
*Automatikusan generálva a GitHub Actions által.*
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_files()
