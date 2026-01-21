import yaml
import os
import json

def get_stars(score):
    if score >= 90: return "⭐⭐⭐⭐⭐ (Kiváló)"
    if score >= 70: return "⭐⭐⭐⭐ (Jó)"
    if score >= 50: return "⭐⭐⭐ (Közepes)"
    return "⭐⭐ (Fejlesztendő)"

def generate_wiki():
    sigma_path = 'rules/sigma'
    scores_path = 'rule_scores.json'
    wiki_content = "# 🛡️ Detection Rule Knowledge Base\n\n"
    
    # Pontszámok beolvasása, ha létezik a fájl
    scores = {}
    if os.path.exists(scores_path):
        with open(scores_path, 'r', encoding='utf-8') as f:
            scores = json.load(f)

    if not os.path.exists(sigma_path):
        print(f"⚠️ Hiba: A {sigma_path} mappa nem található!")
        return

    for root, _, files in os.walk(sigma_path):
        for file in sorted(files):
            if file.endswith(('.yaml', '.yml')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        d = yaml.safe_load(f)
                        if not d:
                            continue

                        # Adatok kinyerése alapértelmezett értékekkel
                        title = d.get('title', 'Névtelen szabály')
                        level = d.get('level', 'n/a')
                        desc = d.get('description', 'Nincs leírás megadva.')
                        fps = d.get('falsepositives', ['Nincs megadva'])
                        
                        # Pontszám lekérése ehhez a fájlhoz
                        current_score = scores.get(file, 0)
                        star_rating = get_stars(current_score)

                        # Markdown szakasz felépítése
                        wiki_content += f"### {title}\n"
                        wiki_content += f"- **Azonosító:** `{file}`\n"
                        wiki_content += f"- **Minőségi mutató:** `{current_score}/100` {star_rating}\n"
                        wiki_content += f"- **Kritikusság:** {'🔴' if level == 'critical' else '🟠' if level == 'high' else '🟡' if level == 'medium' else '🟢'} ({level})\n"
                        wiki_content += f"- **Leírás:** {desc}\n"
                        wiki_content += f"- **Hamis pozitívok:** {', '.join(fps) if isinstance(fps, list) else fps}\n"
                        
                        # MITRE Technikák hozzáadása, ha vannak
                        tags = d.get('tags', [])
                        techniques = [t.split('.')[-1].upper() for t in tags if t.startswith('attack.t')]
                        if techniques:
                            wiki_content += f"- **MITRE ATT&CK:** `{', '.join(techniques)}`\n"

                        wiki_content += "\n---\n\n"
                except Exception as e:
                    print(f"❌ Hiba a fájl feldolgozásakor ({file}): {e}")

    with open('DETECTION_WIKI.md', 'w', encoding='utf-8') as f:
        f.write(wiki_content)
    print("✅ Wiki dokumentáció generálva a minőségi pontszámokkal.")

if __name__ == "__main__":
    generate_wiki()
