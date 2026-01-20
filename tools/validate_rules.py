import yaml
import os
import sys

def validate_sigma_rules():
    rules_path = 'rules/sigma'
    errors = []
    
    for root, dirs, files in os.walk(rules_path):
        for file in files:
            if file.endswith('.yaml'):
                full_path = os.path.join(root, file)
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        rule = yaml.safe_load(f)
                        
                        # Ellenőrzés 1: Van author?
                        if 'author' not in rule or not rule['author']:
                            errors.append(f"❌ {file}: Hiányzik az 'author' mező!")
                        
                        # Ellenőrzés 2: Helyes a Level?
                        valid_levels = ['low', 'medium', 'high', 'critical']
                        if 'level' in rule and rule['level'].lower() not in valid_levels:
                            errors.append(f"❌ {file}: Érvénytelen level: '{rule['level']}'. Javaslat: {valid_levels}")

                        # Ellenőrzés 3: Van MITRE tag?
                        tags = rule.get('tags', [])
                        if not any(tag.startswith('attack.t') for tag in tags):
                            errors.append(f"⚠️ {file}: Nincs MITRE ATT&CK technika hozzárendelve!")

                except Exception as e:
                    errors.append(f"🔥 {file}: YAML formázási hiba: {str(e)}")

    if errors:
        print("\n".join(errors))
        # Ha hibát találunk, a pipeline elbukik (exit 1)
        sys.exit(1)
    else:
        print("✅ Minden szabály rendben van!")

if __name__ == "__main__":
    validate_sigma_rules()
