import yaml
import os
import sys
import difflib

def validate_and_fix():
    rules_path = 'rules/sigma'
    REQUIRED_KEYS = ['title', 'logsource', 'detection', 'status', 'level', 'author']
    any_error = False

    for root, dirs, files in os.walk(rules_path):
        for file in files:
            if file.endswith('.yaml'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    rule = yaml.safe_load(f)
                
                fixed = False
                new_rule = {}
                
                # Elírások javítása automatikusan
                for key, value in rule.items():
                    matches = difflib.get_close_matches(key, REQUIRED_KEYS, n=1, cutoff=0.8)
                    if matches and matches[0] != key:
                        print(f"🔧 JAVÍTÁS [{file}]: '{key}' -> '{matches[0]}'")
                        new_rule[matches[0]] = value
                        fixed = True
                    else:
                        new_rule[key] = value
                
                if fixed:
                    with open(path, 'w', encoding='utf-8') as f:
                        yaml.dump(new_rule, f, sort_keys=False, allow_unicode=True)
                
                # Súlyos hibák (amiket nem tudunk kitalálni, pl. hiányzó author)
                if 'author' not in new_rule:
                    print(f"❌ HIBA [{file}]: Hiányzik az author!")
                    any_error = True
    
    if any_error: sys.exit(1)

if __name__ == "__main__":
    validate_and_fix()
