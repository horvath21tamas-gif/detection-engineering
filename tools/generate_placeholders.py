import os
import yaml

# Útvonalak
SIGMA_DIR = os.path.join(os.path.dirname(__file__), '..', 'rules', 'sigma')
README_FILE = os.path.join(os.path.dirname(__file__), '..', 'README.md')

def update_readme_with_sigma():
    if not os.path.isfile(README_FILE):
        raise FileNotFoundError(f"README file not found: {README_FILE}")
    
    # Beolvassuk a README-t
    with open(README_FILE, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # Az új tartalom a SIGMA szabályokkal
    new_content = ""

    # Iterálunk az összes sigma szabályon
    for sigma_file in os.listdir(SIGMA_DIR):
        if not sigma_file.endswith(".yaml"):
            continue
        
        sigma_file_path = os.path.join(SIGMA_DIR, sigma_file)

        try:
            with open(sigma_file_path, 'r', encoding='utf-8') as f:
                rule = yaml.safe_load(f)
            
            # Ha a szabály nem érvényes, ugrunk a következőre
            if rule is None:
                print(f"[WARNING] {sigma_file} is empty or invalid YAML.")
                continue

            title = rule.get("title", "Unnamed Rule")
            
            # Ha nincs 'detection' kulcs, akkor szintén nem dolgozzuk fel
            if "detection" not in rule:
                print(f"[ERROR] {sigma_file} is missing 'detection' field.")
                continue

            # Addig hozzuk a README tartalmához
            new_content += f"- {title}\n"
        
        except yaml.YAMLError as e:
            print(f"[ERROR] YAML parsing error in {sigma_file_path}: {e}")
            continue

    # Frissítjük a README-t az új tartalommal
    start_marker = "<!-- SIGMA_RULES_START -->"
    end_marker = "<!-- SIGMA_RULES_END -->"
    
    if start_marker not in readme_content or end_marker not in readme_content:
        raise RuntimeError("SIGMA_RULES markers missing in README.md")

    before = readme_content.split(start_marker)[0]
    after = readme_content.split(end_marker)[1]

    new_readme = f"{before}\n{start_marker}\n{new_content.strip()}\n{end_marker}\n{after}"

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(new_readme)

    print(f"[OK] README updated with SIGMA rules")

if __name__ == "__main__":
    update_readme_with_sigma()
