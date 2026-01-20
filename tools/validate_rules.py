import yaml
import os
import sys
import difflib

def validate_and_fix():
    rules_path = 'rules/sigma'
    REQUIRED_KEYS = ['title', 'logsource', 'detection', 'status', 'level', 'author']
    any_critical_error = False

    for root, dirs, files in os.walk(rules_path):
        for file in files:
            if file.endswith('.yaml'):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        rule = yaml.safe_load(f)
                    
                    if not rule: continue

                    fixed = False
                    new_rule = {}
                    
                    # 1. Elírások keresése és javítása
                    for key, value in rule.items():
                        matches = difflib.get_close_matches(key, REQUIRED_KEYS, n=1, cutoff=0.8)
                        if matches and matches[0] != key:
                            print(f"🔧 JAVÍTÁS [{file}]: '{key}' -> '{matches[0]}'")
                            new_rule[matches[0]] = value
                            fixed = True
                        else:
                            new_rule[key] = value
                    
                    # 2. MENTÉS: Ha bármit javítottunk, azonnal írjuk ki a lemezre
                    if fixed:
                        with open(path, 'w', encoding='utf-8') as f:
                            yaml.dump(new_rule, f, sort_keys=False, allow_unicode=True, default_flow_style=False)
                        print(f"✅ Fájl frissítve (auto-fix): {file}")

                    # 3. ELLENŐRZÉS: Ezeket nem tudja a gép javítani
                    if 'author' not in new_rule or not new_rule['author']:
                        print(f"❌ HIBA [{file}]: Hiányzik az 'author'!")
                        any_critical_error = True
                        
                    valid_levels = ['low', 'medium', 'high', 'critical']
                    if 'level' in new_rule and str(new_rule['level']).lower() not in valid_levels:
                        print(f"❌ HIBA [{file}]: Érvénytelen szint: '{new_rule['level']}'")
                        any_critical_error = True

                except Exception as e:
                    print(f"🔥 Hiba: {file} -> {e}")
                    any_critical_error = True
    
    # Ha volt hiba, a legvégén állunk le, hogy a javítások elmentődhessenek
    if any_critical_error:
        sys.exit(1)

if __name__ == "__main__":
    validate_and_fix()
