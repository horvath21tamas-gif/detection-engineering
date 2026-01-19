import os
import yaml

def update_readme_with_sigma():
    sigma_rules_dir = 'rules/sigma'
    readme_file = 'README.md'
    
    mitre_groups = {}  # Különböző MITRE ATT&CK technikák szerint csoportosítjuk a szabályokat
    for root, dirs, files in os.walk(sigma_rules_dir):
        for file in files:
            if file.endswith('.yaml'):
                rule_path = os.path.join(root, file)
                with open(rule_path, 'r') as rule_file:
                    sigma_rule = yaml.safe_load(rule_file)
                    technique = sigma_rule.get('technique', 'UNMAPPED')
                    rule_name = sigma_rule.get('title', 'Unnamed Rule')

                    if technique not in mitre_groups:
                        mitre_groups[technique] = []
                    mitre_groups[technique].append(rule_name)
    
    # README.md frissítése
    with open(readme_file, 'a') as readme:
        readme.write("\n# Sigma Rules\n")
        for technique, rules in mitre_groups.items():
            readme.write(f"\n## {technique}\n")
            for rule in rules:
                readme.write(f"- {rule}\n")
    
    print(f"[OK] README.md updated with Sigma rules")

if __name__ == "__main__":
    update_readme_with_sigma()
