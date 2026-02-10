import yaml
import os
import json

def get_stars(score):
    if score >= 90: return "⭐⭐⭐⭐⭐ (Kiváló)"
    if score >= 70: return "⭐⭐⭐⭐ (Jó)"
    if score >= 50: return "⭐⭐⭐ (Közepes)"
    return "⭐⭐ (Fejlesztendő)"

def get_lolbas_info(rule_data):
    """LOLBAS linkek keresése a szabályban található folyamatnevek alapján."""
    lolbas_links = []
    try:
        if os.path.exists('inventory/lolbas_map.json'):
            with open('inventory/lolbas_map.json', 'r') as f:
                lolbas_map = json.load(f)
            
            # Kikeressük a folyamatneveket a YAML-ből (egyszerűsített keresés)
            yaml_str = str(rule_data).lower()
            for proc, link in lolbas_map.items():
                if proc in yaml_str:
                    lolbas_links.append(f"[{proc.upper()}]({link})")
    except:
        pass
    
    if lolbas_links:
        return f"\n> ⚠️ **LOLBAS Érintettség:** Ez a szabály visszaélésre alkalmas gyári binárist érint: {', '.join(lolbas_links)}\n"
    return ""

def get_estimated_volume(category):
    """Becsült eseményszám (EPS) alapú besorolás."""
    volumes = {
        'process_creation': ('Magas', '⚠️ Erős szűrés javasolt (sok log)'),
        'network_connection': ('Kritikusan Magas', '🛑 SIEM gyilkos kategória!'),
        'registry_event': ('Közepes', 'ℹ️ Mérsékelt zajszint'),
        'file_event': ('Magas', '⚠️ Tárolás-igényes'),
        'email': ('Alacsony', '✅ Jól monitorozható')
    }
    vol, advice = volumes.get(category, ('Ismeretlen', 'Nincs adat'))
    return f"- **Becsült zajszint:** {vol} ({advice})\n"

def get_correlation_hint(tags):
    """Támadási láncolat (Correlation) tippek a MITRE fázisok alapján."""
    phases = {
        'initial_access': 'Belépési pont',
        'execution': 'Kódfuttatás',
        'persistence': 'Megtelepedés',
        'privilege_escalation': 'Jogosultság emelés',
        'exfiltration': 'Adatszivárogtatás'
    }
    found_phases = []
    for tag in tags:
        for phase, name in phases.items():
            if phase in tag:
                found_phases.append(name)
    
    if found_phases:
        return f"- **Detekciós lánc szerep:** `{ ' -> '.join(set(found_phases)) }`\n"
    return ""

def get_playbook(category, level):
    playbook = "#### 🚨 Response Playbook\n"
    if category == 'process_creation':
        playbook += "1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.\n"
        playbook += "2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.\n"
    elif category == 'network_connection':
        playbook += "1. **IP hírnév:** Ellenőrizd a távoli IP címet hírnév-adatbázisokban.\n"
        playbook += "2. **Forgalom elemzés:** Vizsgáld meg a küldött adatmennyiséget.\n"
    else:
        playbook += "1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.\n"
    
    if level in ['high', 'critical']:
        playbook += "2. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett hostot!\n"
    return playbook

def generate_wiki():
    sigma_path = 'rules/sigma'
    scores_path = 'rule_scores.json'
    scores = {}
    
    if os.path.exists(scores_path):
        with open(scores_path, 'r', encoding='utf-8') as f:
            scores = json.load(f)

    rules_data = []
    for root, _, files in os.walk(sigma_path):
        for file in sorted(files):
            if file.endswith(('.yaml', '.yml')):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        d = yaml.safe_load(f)
                        if d: rules_data.append({'filename': file, 'data': d})
                    except: continue

    wiki_content = "# 🛡️ Detection Rule Knowledge Base\n\n"
    wiki_content += "## 📖 Tartalomjegyzék\n"
    for item in rules_data:
        title = item['data'].get('title', 'Névtelen szabály')
        anchor = title.lower().replace(' ', '-').replace('.', '').replace('/', '').replace(',', '')
        wiki_content += f"- [{title}](#{anchor})\n"

    for item in rules_data:
        file = item['filename']
        d = item['data']
        title = d.get('title', 'Névtelen szabály')
        level = d.get('level', 'n/a')
        category = d.get('logsource', {}).get('category', 'unknown')
        tags = d.get('tags', []) if d.get('tags') else []
        
        current_score = scores.get(file, 0)
        
        wiki_content += f"\n---\n## {title}\n"
        wiki_content += f"- **Azonosító:** `{file}`\n"
        wiki_content += f"- **Minőségi mutató:** `{current_score}/100` {get_stars(current_score)}\n"
        wiki_content += f"- **Kritikusság:** {'🔴' if level == 'critical' else '🟠' if level == 'high' else '🟡'} ({level})\n"
        
        # Gazdagítás (Enrichment)
        wiki_content += get_estimated_volume(category)
        wiki_content += get_correlation_hint(tags)
        wiki_content += get_lolbas_info(d)
        
        wiki_content += f"- **Leírás:** {str(d.get('description', 'Nincs leírás')).strip()}\n"
        
        techniques = [t.split('.')[-1].upper() for t in tags if t.startswith('attack.t')]
        if techniques:
            wiki_content += f"- **MITRE ATT&CK:** `{', '.join(techniques)}`\n"

        wiki_content += "\n" + get_playbook(category, level) + "\n"

    with open('DETECTION_WIKI.md', 'w', encoding='utf-8') as f:
        f.write(wiki_content)
    print(f"✅ Wiki generálva ({len(rules_data)} szabály).")

if __name__ == "__main__":
    generate_wiki()
