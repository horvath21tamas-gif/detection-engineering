import json
import os
import yaml

def run_gap_analysis():
    layer_path = 'attack_navigator_layer.json'
    inventory_path = 'inventory/log_sources.yaml'
    sigma_path = 'rules/sigma'
    
    # 1. MITRE Lefedettség ellenőrzése
    covered_techniques = []
    if os.path.exists(layer_path):
        with open(layer_path, 'r') as f:
            data = json.load(f)
            covered_techniques = [t['techniqueID'] for t in data.get('techniques', [])]

    # 2. Log Source alapú "Vakfolt" ellenőrzés
    inventory = {}
    if os.path.exists(inventory_path):
        with open(inventory_path, 'r') as f:
            inventory = yaml.safe_load(f).get('available_sources', {})

    log_source_gaps = []
    for root, _, files in os.walk(sigma_path):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                with open(os.path.join(root, file), 'r') as f:
                    rule = yaml.safe_load(f)
                    ls = rule.get('logsource', {})
                    # Ellenőrizzük, hogy minden megadott forrás szerepel-e az inventory-ban
                    for key in ['category', 'product', 'service']:
                        val = ls.get(key)
                        if val and val not in inventory.get(key, []):
                            log_source_gaps.append(f"{file} (Hiányzó {key}: `{val}`)")
                            break

    # 3. Jelentés generálása
    critical_targets = ["T1003", "T1059", "T1053", "T1021", "T1098", "T1547", "T1562"]
    mitre_gaps = [t for t in critical_targets if t not in covered_techniques]

    with open('GAP_ANALYSIS.md', 'w', encoding='utf-8') as f:
        f.write("# 🎯 Detection Strategy & Gap Analysis\n\n")
        
        f.write("## 🛑 Kritikus Adatforrás Hiányok\n")
        f.write("Az alábbi szabályok **soha nem fognak riasztani**, mert a hozzájuk rendelt logforrás nincs regisztrálva az inventory-ban:\n\n")
        if log_source_gaps:
            for gap in log_source_gaps:
                f.write(f"- [ ] ⚠️ {gap}\n")
        else:
            f.write("✅ Minden szabályhoz rendelkezésre áll a megfelelő adatforrás.\n")

        f.write("\n## 🛡️ Hiányzó MITRE ATT&CK Lefedettség\n")
        f.write("A stratégiai fontosságú technikák közül ezekre nincs még szabályod:\n\n")
        for gap in mitre_gaps:
            f.write(f"- [ ] **{gap}** (https://attack.mitre.org/techniques/{gap})\n")
            
    print("✅ Gap Analysis és Adatforrás audit elkészült.")

if __name__ == "__main__":
    run_gap_analysis()
