import json
import os
import yaml
from datetime import datetime

def run_gap_analysis():
    layer_path = 'attack_navigator_layer.json'
    inventory_path = 'inventory/log_sources.yaml'
    sigma_path = 'rules/sigma'
    
    # 1. MITRE Lefedettség beolvasása
    covered_techniques = []
    if os.path.exists(layer_path):
        with open(layer_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            covered_techniques = [t['techniqueID'] for t in data.get('techniques', [])]

    # 2. Live Inventory beolvasása
    inventory = {'category': [], 'product': [], 'service': []}
    if os.path.exists(inventory_path):
        with open(inventory_path, 'r', encoding='utf-8') as f:
            inv_data = yaml.safe_load(f)
            if inv_data and 'available_sources' in inv_data:
                inventory = inv_data['available_sources']

    log_source_gaps = []
    active_rules_count = 0
    total_rules_count = 0

    # 3. Szabályok átvizsgálása adatforrás szempontjából
    for root, _, files in os.walk(sigma_path):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                total_rules_count += 1
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        rule = yaml.safe_load(f)
                        ls = rule.get('logsource', {})
                        
                        is_broken = False
                        missing_details = []
                        
                        for key in ['category', 'product', 'service']:
                            val = ls.get(key)
                            if val and val not in inventory.get(key, []):
                                missing_details.append(f"{key}: `{val}`")
                                is_broken = True
                        
                        if is_broken:
                            log_source_gaps.append({
                                'file': file,
                                'title': rule.get('title', 'Névtelen'),
                                'missing': ", ".join(missing_details)
                            })
                        else:
                            active_rules_count += 1
                    except Exception:
                        continue

    # 4. Stratégiai MITRE hiányok (Prioritási lista)
    critical_targets = {
        "T1003": "Credential Dumping",
        "T1059": "Command and Scripting Interpreter",
        "T1053": "Scheduled Task/Job",
        "T1021": "Remote Services",
        "T1098": "Account Manipulation",
        "T1547": "Boot or Logon Autostart Execution",
        "T1562": "Impair Defenses"
    }
    mitre_gaps = {tid: name for tid, name in critical_targets.items() if tid not in covered_techniques}

    # 5. GAP_ANALYSIS.md összeállítása
    with open('GAP_ANALYSIS.md', 'w', encoding='utf-8') as f:
        f.write(f"# 🎯 Detection Strategy & Gap Analysis\n")
        f.write(f"*Frissítve: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
        
        # Összegző táblázat
        f.write("## 📊 Állapotösszegző\n")
        f.write("| Mutató | Érték |\n")
        f.write("| :--- | :--- |\n")
        f.write(f"| Összes szabály | {total_rules_count} |\n")
        f.write(f"| Aktív (van logforrás) | {active_rules_count} |\n")
        f.write(f"| Inaktív (hiányzó log) | {len(log_source_gaps)} |\n")
        f.write(f"| MITRE Lefedettség | {len(covered_techniques)} technika |\n\n")

        # Log Source hibák
        f.write("## 🛑 Kritikus Adatforrás Hiányok\n")
        f.write("Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:\n\n")
        if log_source_gaps:
            f.write("| Szabály | Hiányzó forrás |\n")
            f.write("| :--- | :--- |\n")
            for gap in log_source_gaps:
                f.write(f"| {gap['title']} (`{gap['file']}`) | {gap['missing']} |\n")
        else:
            f.write("✅ Minden szabályhoz rendelkezésre áll a megfelelő adatforrás a SIEM-ben.\n")

        # MITRE Hiányok
        f.write("\n## 🛡️ Stratégiai Teendők (Hiányzó Technikák)\n")
        f.write("A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:\n\n")
        if mitre_gaps:
            for tid, name in mitre_gaps.items():
                f.write(f"- [ ] **{tid}** - {name} ([Link](https://attack.mitre.org/techniques/{tid}))\n")
        else:
            f.write("✅ Minden kritikus technika le van fedve legalább egy szabállyal.\n")

    print(f"✅ Gap Analysis elkészült. (Aktív: {active_rules_count}/{total_rules_count})")

if __name__ == "__main__":
    run_gap_analysis()
