import yaml
import os
import json

def analyze_kill_chain():
    sigma_path = 'rules/sigma'
    # A standard Lockheed Martin / MITRE alapú fázisok
    kill_chain_mapping = {
        'initial-access': 'Belépési pont',
        'execution': 'Végrehajtás',
        'persistence': 'Perzisztencia',
        'privilege-escalation': 'Jogosultság kiterjesztés',
        'defense-evasion': 'Védelem elkerülése',
        'credential-access': 'Hitelesítő adatok megszerzése',
        'discovery': 'Felderítés',
        'lateral-movement': 'Oldalirányú mozgás',
        'collection': 'Adatgyűjtés',
        'exfiltration': 'Adatszivárogtatás',
        'command-and-control': 'Vezérlés (C2)'
    }
    
    stats = {key: 0 for key in kill_chain_mapping.keys()}
    total_rules = 0

    # Szabályok elemzése
    for root, _, files in os.walk(sigma_path):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        d = yaml.safe_load(f)
                        if not d: continue
                        total_rules += 1
                        tags = [t.lower() for t in d.get('tags', [])]
                        
                        for phase in kill_chain_mapping.keys():
                            if any(phase in t for t in tags):
                                stats[phase] += 1
                    except: continue

    # Jelentés összeállítása (Markdown formátumban)
    report = "# ⛓️ Cyber Kill Chain Lefedettségi Jelentés\n\n"
    report += f"Ez a jelentés automatikusan készült {total_rules} szabály alapján.\n\n"
    report += "| Támadási Fázis | Szabályok Száma | Lefedettség |\n"
    report += "| :--- | :---: | :--- |\n"

    for phase, label in kill_chain_mapping.items():
        count = stats[phase]
        # Vizuális sáv (progress bar) készítése
        bar = "█" * (count // 10) + "░" * (10 - (count // 10))
        report += f "| {label} (`{phase}`) | {count} | `{bar}` |\n"

    with open('KILL_CHAIN_REPORT.md', 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("✅ Kill Chain elemzés kész: KILL_CHAIN_REPORT.md")

if __name__ == "__main__":
    analyze_kill_chain()
