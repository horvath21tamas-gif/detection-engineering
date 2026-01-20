import yaml
import os

def generate_wiki():
    sigma_path = 'rules/sigma'
    wiki_content = "# 🛡️ Detection Rule Knowledge Base\n\n"
    
    for root, _, files in os.walk(sigma_path):
        for file in sorted(files):
            if file.endswith('.yaml'):
                with open(os.path.join(root, file), 'r') as f:
                    d = yaml.safe_load(f)
                    wiki_content += f"### {d.get('title')}\n"
                    wiki_content += f"- **Azonosító:** `{file.replace('.yaml', '')}`\n"
                    wiki_content += f"- **Leírás:** {d.get('description')}\n"
                    wiki_content += f"- **Szint:** `{d.get('level')}`\n"
                    wiki_content += f"- **Kritikusság:** {'🔴' if d.get('level') == 'critical' else '🟠' if d.get('level') == 'high' else '🟡'}\n"
                    wiki_content += f"- **Hamis pozitívok:** {', '.join(d.get('falsepositives', ['Nincs megadva']))}\n\n"
                    wiki_content += "---\n"

    with open('DETECTION_WIKI.md', 'w') as f:
        f.write(wiki_content)
    print("✅ Wiki dokumentáció generálva.")

if __name__ == "__main__":
    generate_wiki()
