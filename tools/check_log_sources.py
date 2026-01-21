import yaml
import os
import sys

def check_sources():
    inventory_path = 'inventory/log_sources.yaml'
    sigma_path = 'rules/sigma'
    
    with open(inventory_path, 'r') as f:
        inventory = yaml.safe_load(f)['available_sources']

    errors = 0
    for root, _, files in os.walk(sigma_path):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                with open(os.path.join(root, file), 'r') as f:
                    rule = yaml.safe_load(f)
                    logsource = rule.get('logsource', {})
                    
                    # Ellenőrizzük a kategóriát, terméket és szervizt
                    for key in ['category', 'product', 'service']:
                        val = logsource.get(key)
                        if val and val not in inventory.get(key, []):
                            print(f"❌ HIBA: {file} - Ismeretlen {key}: '{val}'")
                            errors += 1
    
    if errors > 0:
        print(f"\n⚠️ Összesen {errors} logsource hiba található!")
        # Itt dönthetsz: sys.exit(1) leállítja a pipeline-t, ha hiba van
    else:
        print("✅ Minden szabály valid logforrást használ.")

if __name__ == "__main__":
    check_sources()
