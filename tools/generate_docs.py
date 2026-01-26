import yaml
import os
import json

def get_stars(score):
    if score >= 90: return "⭐⭐⭐⭐⭐ (Kiváló)"
    if score >= 70: return "⭐⭐⭐⭐ (Jó)"
    if score >= 50: return "⭐⭐⭐ (Közepes)"
    return "⭐⭐ (Fejlesztendő)"

def get_playbook(category, level):
    """Automatikus intézkedési terv generálása a szabály típusa alapján."""
    playbook = "#### 🚨 Response Playbook\n"
    if category == 'process_creation':
        playbook += "1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.\n"
        playbook += "2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.\n"
    elif category == 'network_connection':
        playbook += "1. **IP hírnév:** Ellenőrizd a távoli IP címet hírnév-adatbázisokban.\n"
        playbook += "2. **Forgalom elemzés:** Vizsgáld meg a küldött adatmennyiséget és a protokoll típusát.\n"
    elif category == 'email': # ÚJ: E-mail specifikus playbook
        playbook += "1. **Header elemzés:** Ellenőrizd a feladó valódi IP címét és az SPF/DKIM/DMARC státuszt.\n"
        playbook += "2. **Link/Melléklet:** Vizsgáld meg az URL-t sandbox környezetben (pl. URLScan.io).\n"
    else:
        playbook += "1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.\n"
        playbook += "2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.\n"
    
    if level in ['high', 'critical']:
        playbook += "3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!\n"
    
    return playbook

def generate_wiki():
    sigma_path = 'rules/sigma'
    scores_path = 'rule_scores.json'
    
    scores = {}
    if os.path.exists(scores_path):
        with open(scores_path, 'r', encoding='utf-8') as f:
            scores = json.load(f)

    if not os.path.exists(sigma_path):
        print(f"⚠️ Hiba: A {sigma_path} mappa nem található!")
        return

    rules_data = []
    for root, _, files in os.walk(sigma_path):
        for file in sorted(files):
            if file.endswith(('.yaml', '.yml')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        # Beolvassuk a YAML-t
                        d = yaml.safe_load(f)
                        if d:
                            rules_data.append({'filename': file, 'data': d})
                    except Exception as e:
                        # NE maradjon némán a hiba!
                        print(f"❌ Hiba a {file} feldolgozásakor: {e}")
                        continue

    if not rules_data:
        print("⚠️ Nem találtam feldolgozható Sigma szabályt!")
        return

    wiki_content = "# 🛡️ Detection Rule Knowledge Base\n\n"
    
    # 1. Tartalomjegyzék
    wiki_content += "## 📖 Tartalomjegyzék\n"
    for item in rules_data:
        title = item['data'].get('title', 'Névtelen szabály')
        anchor = title.lower().replace(' ', '-').replace('.', '').replace('/', '').replace(',', '')
        wiki_content += f"- [{title}](#{anchor})\n"
    wiki_content += "\n---\n\n"

    # 2. Szabályok részletezése
    for item in rules_data:
        file = item['filename']
        d = item['data']
        
        title = d.get('title', 'Névtelen szabály')
        level = d.get('level', 'n/a')
        desc = d.get('description', 'Nincs leírás megadva.')
        fps = d.get('falsepositives', ['Nincs megadva'])
        category = d.get('logsource', {}).get('category', 'unknown')
        
        current_score = scores.get(file, 0)
        star_rating = get_stars(current_score)

        wiki_content += f"## {title}\n"
        wiki_content += f"- **Azonosító:** `{file}`\n"
        wiki_content += f"- **Minőségi mutató:** `{current_score}/100` {star_rating}\n"
        wiki_content += f"- **Kritikusság:** {'🔴' if level == 'critical' else '🟠' if level == 'high' else '🟡' if level == 'medium' else '🟢'} ({level})\n"
        wiki_content += f"- **Leírás:** {desc.strip()}\n"
        
        # Hamis pozitívok listázása
        if isinstance(fps, list):
            wiki_content += f"- **Hamis pozitívok:** {', '.join(fps)}\n"
        else:
            wiki_content += f"- **Hamis pozitívok:** {fps}\n"
        
        # MITRE ATT&CK
        tags = d.get('tags', []) if d.get('tags') else []
        techniques = [t.split('.')[-1].upper() for t in tags if t.startswith('attack.t')]
        if techniques:
            wiki_content += f"- **MITRE ATT&CK:** `{', '.join(techniques)}`\n"

        # Playbook
        wiki_content += "\n" + get_playbook(category, level) + "\n"
        wiki_content += "---\n\n"

    with open('DETECTION_WIKI.md', 'w', encoding='utf-8') as f:
        f.write(wiki_content)
    print(f"✅ Wiki generálva ({len(rules_data)} szabály).")

if __name__ == "__main__":
    generate_wiki()
