import os

def get_sigma_rules():
    """
    Lekéri az összes Sigma szabály nevét a rules/sigma mappából.
    """
    sigma_dir = 'rules/sigma'
    rule_list = []

    for root, dirs, files in os.walk(sigma_dir):
        for file in files:
            if file.endswith('.yaml'):
                rule_list.append(file)
    
    return rule_list

def update_readme():
    """
    Frissíti a README.md fájlt az új Sigma szabályokkal.
    """
    readme_path = 'README.md'
    sigma_rules = get_sigma_rules()

    # Ha a README.md fájl nem létezik, akkor hozzunk létre egy új fájlt
    if not os.path.exists(readme_path):
        with open(readme_path, 'w') as f:
            f.write("# Detection Rules\n\n")

    # Olvassuk be a README.md fájlt
    with open(readme_path, 'r') as f:
        readme_content = f.read()

    # Készítsünk egy listát a szabályokról
    rule_list = '\n'.join([f"- {rule}" for rule in sigma_rules])

    # Ellenőrizzük, hogy van-e már lista a szabályokból, ha igen, frissítjük
    if "## Sigma Detection Rules" in readme_content:
        start_index = readme_content.index("## Sigma Detection Rules") + len("## Sigma Detection Rules\n")
        end_index = readme_content.find("\n", start_index)
        readme_content = readme_content[:start_index] + '\n' + rule_list + readme_content[end_index:]

    else:
        readme_content += f"\n## Sigma Detection Rules\n{rule_list}\n"
    
    # Írjuk vissza a módosított tartalmat
    with open(readme_path, 'w') as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_readme()
