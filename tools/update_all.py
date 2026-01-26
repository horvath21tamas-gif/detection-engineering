import os
import yaml
import re
import json
import time

def get_rule_data():
    sigma_dir = 'rules/sigma'
    splunk_dir = 'rules/splunk'
    qradar_dir = 'rules/qradar'
    netwitness_dir = 'rules/netwitness'
    elastic_dir = 'rules/elastic'
    sentinel_dir = 'rules/sentinel' # ÚJ: Sentinel mappa

    techniques_found = {} 
    rule_mapping = {}    
    logsource_stats = {} 
    rules_count = 0
    
    # SIEM specifikus számlálók
    splunk_count = 0
    qradar_count = 0
    netwitness_count = 0
    elastic_count = 0
    sentinel_count = 0 # ÚJ: Sentinel számláló
    
    if os.path.exists(splunk_dir):
        splunk_count = len([f for f in os.listdir(splunk_dir) if f.endswith('.spl')])
    if os.path.exists(qradar_dir):
        qradar_count = len([f for f in os.listdir(qradar_dir) if f.endswith('.aql')])
    if os.path.exists(netwitness_dir):
        netwitness_count = len([f for f in os.listdir(netwitness_dir) if f.endswith('.txt')])
    if os.path.exists(elastic_dir):
        elastic_count = len([f for f in os.listdir(elastic_dir) if f.endswith('.kql') or f.endswith('.eql')])
    if os.path.exists(sentinel_dir): # ÚJ: Sentinel fájlok számolása
        sentinel_count = len([f for f in os.listdir(sentinel_dir) if f.endswith('.kql')])
        
    if not os.path.exists(sigma_dir):
        return {}, {}, 0, {}, 0, 0, 0, 0, 0 # Bővítve sentinel_count-tal
        
    for root, dirs, files in os.walk(sigma_dir):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                rules_count += 1
                try:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        content = yaml.safe_load(f)
                        level = str(content.get('level', 'low')).lower()
                        title = content.get('title', file)
                        
                        ls = content.get('logsource', {})
                        ls_key = ls.get('service') or ls.get('category') or ls.get('product') or 'unknown'
                        logsource_stats[ls_key] = logsource_stats.get(ls_key, 0) + 1

                        for tag in content.get('tags', []):
                            match = re.search(r't\d{4}(?:\.\d{3})?', tag.lower())
                            if match:
                                tid = match.group(0).upper()
                                if tid not in techniques_found or level in ['high', 'critical']:
                                    techniques_found[tid] = level
                                if tid not in rule_mapping:
                                    rule_mapping[tid] = []
                                if title not in rule_mapping[tid]:
                                    rule_mapping[tid].append(title)
                except: continue

    return techniques_found, rule_mapping, rules_count, logsource_stats, splunk_count, qradar_count, netwitness_count, elastic_count, sentinel_count

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

    svg += f'<g transform="translate(10, {rows * (cell_h + gap) + 20})">'
    svg += '<circle cx="5" cy="5" r="5" fill="#ff6666"/><text x="15" y="9" font-family="Arial" font-size="11">High/Critical</text>'
    svg += '<circle cx="95" cy="5" r="5" fill="#ffbd66"/><text x="105" y="9" font-family="Arial" font-size="11">Medium</text>'
    svg += '<circle cx="170" cy="5" r="5" fill="#ffe766"/><text x="180" y="9" font-family="Arial" font-size="11">Low</text>'
    svg += '</g></svg>'

    with open('mitre_matrix.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

def update_all():
    # ÚJ: sentinel_count fogadása (se_count)
    techniques, rule_mapping, rules_count, ls_stats, splunk_count, qradar_count, nw_count, el_count, se_count = get_rule_data()
    generate_matrix_svg(techniques)
    
    USER = "horvath21tamas-gif"
    REPO = "detection-engineering"
    BRANCH = "test"
    
    ts = int(time.time())
    current_time = time.strftime('%Y-%m-%d %H:%M:%S')
    total_mitre_tech = 201 
    coverage_pct = round((len(techniques) / total_mitre_tech) * 100, 1)
    
    # Százalékos SIEM lefedettség számítása
    splunk_pct = round((splunk_count / rules_count * 100), 1) if rules_count > 0 else 0
    qradar_pct = round((qradar_count / rules_count * 100), 1) if rules_count > 0 else 0
    nw_pct = round((nw_count / rules_count * 100), 1) if rules_count > 0 else 0
    el_pct = round((el_count / rules_count * 100), 1) if rules_count > 0 else 0
    se_pct = round((se_count / rules_count * 100), 1) if rules_count > 0 else 0 # ÚJ: Sentinel %
    
    # 1. Navigator JSON
    layer = {
        "name": "Detection Coverage",
        "versions": {"attack": "14", "navigator": "4.9", "layer": "4.4"},
        "domain": "enterprise-attack",
        "techniques": [{"techniqueID": tid, "color": "#ff6666" if lvl in ['high','critical'] else "#ffbd66"} for tid, lvl in techniques.items()]
    }
    with open('attack_navigator_layer.json', 'w', encoding='utf-8') as f:
        json.dump(layer, f, indent=4)

    # 2. COVERAGE.md (Sentinel-lel bővítve)
    siem_table = f"## 📈 SIEM Platform Lefedettség\n\n"
    siem_table += "| Platform | Konvertált szabályok | Lefedettség |\n"
    siem_table += "| :--- | :---: | :---: |\n"
    siem_table += f"| Sigma (Forrás) | {rules_count} | 100% |\n"
    siem_table += f"| Splunk (SPL) | {splunk_count} | {splunk_pct}% |\n"
    siem_table += f"| Microsoft Sentinel (KQL) | {se_count} | {se_pct}% |\n" # ÚJ sor
    siem_table += f"| QRadar (AQL) | {qradar_count} | {qradar_pct}% |\n"
    siem_table += f"| Elastic (KQL/EQL) | {el_count} | {el_pct}% |\n"
    siem_table += f"| RSA NetWitness | {nw_count} | {nw_pct}% |\n\n"

    coverage_content = f"# 📘 Részletes MITRE ATT&CK Lefedettség\n\n"
    coverage_content += f"**Utolsó frissítés:** `{current_time}`\n\n"
    coverage_content += siem_table
    coverage_content += "## 🎯 Technika alapú bontás\n"
    coverage_content += "| Technika ID | Szint | Kapcsolódó szabályok |\n"
    coverage_content += "| :--- | :--- | :--- |\n"
    for tid in sorted(rule_mapping.keys()):
        level = techniques[tid].upper()
        rules_list = ", ".join(rule_mapping[tid])
        coverage_content += f"| {tid} | {level} | {rules_list} |\n"
    with open('COVERAGE.md', 'w', encoding='utf-8') as f:
        f.write(coverage_content)

    # 3. LogSource táblázat
    ls_table = "| Log Forrás | Szabályok száma |\n| :--- | :--- |\n"
    for source, count in sorted(ls_stats.items(), key=lambda item: item[1], reverse=True):
        ls_table += f"| {source.capitalize()} | {count} |\n"

    # 4. README.md
    raw_json_url = f"https://raw.githubusercontent.com/{USER}/{REPO}/{BRANCH}/attack_navigator_layer.json"
    navigator_link = f"https://mitre-attack.github.io/attack-navigator/#layerURL={raw_json_url}"

    readme_content = f"""# 🛡️ Detection Engineering Dashboard

## 📊 Összesített Statisztika
- **Lefedett technikák:** `{len(techniques)}` db
- **Sigma szabályok:** `{rules_count}` db
- **MITRE ATT&CK Lefedettség:** `[{coverage_pct}%]`
- **Részletes lista:** [COVERAGE.md](./COVERAGE.md)

![Progress Bar](https://geps.dev/progress/{int(coverage_pct)}?dangerColor=ff6666&warningColor=ffbd66&successColor=8ecb88&v={ts})

## 🗺️ MITRE ATT&CK Mátrix Vizualizáció
![MITRE Matrix](./mitre_matrix.svg?v={ts})

## 🔗 Interaktív Navigator
🚀 [**Kattints ide a teljes interaktív mátrix megnyitásához**]({navigator_link})

---
*Ez a dokumentum automatikusan frissül minden módosítás után.*
*Legutóbbi frissítés: {current_time} (UTC)*
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_all()
