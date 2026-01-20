import yaml
import os
import sys

def validate_rules():
    rules_path = 'rules/sigma'
    has_error = False
    
    if not os.path.exists(rules_path):
        print(f"❌ Hiba: A {rules_path} mappa nem létezik!")
        sys.exit(1)

    print("🔍 Sigma szabályok ellenőrzése és javítási javaslatok...")
    
    for root, dirs, files in os.walk(rules_path):
        for file in files:
            if file.endswith('.yaml'):
                full_path = os.path.join(root, file)
                with open(full_path, 'r', encoding='utf-8') as f:
                    try:
                        rule = yaml.safe_load(f)
                        
                        # 1. Ellenőrzés: Author
                        if 'author' not in rule or not rule['author']:
                            print(f"⚠️ HIBA [{file}]: Hiányzik a szerző (author).")
                            print(f"   💡 JAVÍTÁS: Adj hozzá egy 'author: {os.environ.get('USER', 'Név')}' sort.")
                            has_error = True

                        # 2. Ellenőrzés: Level formátum
                        valid_levels = ['low', 'medium', 'high', 'critical']
                        if 'level' in rule:
                            current_level = str(rule['level']).lower()
                            if current_level not in valid_levels:
                                print(f"⚠️ HIBA [{file}]: Érvénytelen szint: '{rule['level']}'.")
                                print(f"   💡 JAVÍTÁS: Cseréld le erre: {valid_levels}")
                                has_error = True

                        # 3. Ellenőrzés: MITRE tagek
                        tags = rule.get('tags', [])
                        if not any(tag.startswith('attack.t') for tag in tags):
                            print(f"⚠️ HIBA [{file}]: Nincs MITRE ATT&CK technika!")
                            print(f"   💡 JAVÍTÁS: Adj hozzá egy technika kódot, pl: 'attack.t1059.001'")
                            has_error = True

                    except Exception as e:
                        print(f"❌ KRITIKUS HIBA [{file}]: Hibás YAML formátum!")
                        print(f"   💡 JAVÍTÁS: Ellenőrizd a kettőspontokat és a behúzásokat. Hiba: {str(e)}")
                        has_error = True

    if has_error:
        print("\n❌ A validáció sikertelen. Kérlek javítsd a fenti hibákat a javaslatok alapján!")
        sys.exit(1)
    else:
        print("\n✅ Minden szabály tökéletes!")

if __name__ == "__main__":
    validate_rules()
