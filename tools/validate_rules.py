import yaml
import os
import sys
import difflib

def validate_rules():
    rules_path = 'rules/sigma'
    has_error = False
    
    # A Sigma szabályok kötelező és ajánlott alapmezői
    REQUIRED_KEYS = ['title', 'logsource', 'detection', 'status', 'level', 'author']
    
    if not os.path.exists(rules_path):
        print(f"❌ Hiba: A {rules_path} mappa nem létezik!")
        sys.exit(1)

    print("🔍 Sigma szabályok mélyellenőrzése elírás-figyelővel...")
    
    for root, dirs, files in os.walk(rules_path):
        for file in files:
            if file.endswith('.yaml'):
                full_path = os.path.join(root, file)
                with open(full_path, 'r', encoding='utf-8') as f:
                    try:
                        rule = yaml.safe_load(f)
                        if not rule: continue
                        
                        # --- ELÍRÁS ELLENŐRZÉS ---
                        rule_keys = list(rule.keys())
                        for key in rule_keys:
                            # Ha a kulcs nincs a listában, de nagyon hasonlít valamelyikre
                            if key not in REQUIRED_KEYS:
                                matches = difflib.get_close_matches(key, REQUIRED_KEYS, n=1, cutoff=0.7)
                                if matches:
                                    print(f"⚠️ HIBA [{file}]: Lehetséges elírás: '{key}'.")
                                    print(f"   💡 JAVÍTÁS: Úgy tűnik, erre gondoltál: '{matches[0]}'")
                                    has_error = True

                        # --- KÖTELEZŐ MEZŐK ELLENŐRZÉSE ---
                        for req in REQUIRED_KEYS:
                            if req not in rule:
                                print(f"⚠️ HIBA [{file}]: Hiányzik a kötelező mező: '{req}'.")
                                has_error = True

                        # --- ÉRTÉK ELLENŐRZÉS ---
                        valid_levels = ['low', 'medium', 'high', 'critical']
                        if 'level' in rule and str(rule['level']).lower() not in valid_levels:
                            print(f"⚠️ HIBA [{file}]: Érvénytelen szint: '{rule['level']}'.")
                            print(f"   💡 JAVÍTÁS: Használd ezeket: {valid_levels}")
                            has_error = True

                        if 'tags' in rule:
                            if not any(tag.startswith('attack.t') for tag in rule['tags']):
                                print(f"⚠️ HIBA [{file}]: Nincs MITRE ATT&CK tag (pl. attack.t1059).")
                                has_error = True

                    except Exception as e:
                        print(f"❌ KRITIKUS HIBA [{file}]: YAML szintaktikai hiba! {str(e)}")
                        has_error = True

    if has_error:
        print("\n❌ A validáció elbukott. Javítsd a hibákat a beküldéshez!")
        sys.exit(1)
    else:
        print("\n✅ Minden szabály formailag és tartalmilag is megfelelő!")

if __name__ == "__main__":
    validate_rules()
