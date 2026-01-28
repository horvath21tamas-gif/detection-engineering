import yaml
import json
import os
import uuid
import random
from datetime import datetime

SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def clean_field_name(field):
    """Eltávolítja a Sigma módosítókat (pl. |contains, |endswith)"""
    return field.split('|')[0]

def generate_mock_event(rule_content):
    # Alap metaadatok, amiket a legtöbb Windows/Sysmon szabály elvár
    mock_event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "Product": rule_content.get('logsource', {}).get('product', 'windows'),
        "Service": rule_content.get('logsource', {}).get('service', 'sysmon')
    }
    
    detection = rule_content.get('detection', {})
    
    # Keressük meg az összes 'selection' kezdetű blokkot
    for key, value in detection.items():
        if key.startswith('selection') and isinstance(value, dict):
            for field, val in value.items():
                clean_name = clean_field_name(field)
                
                # Érték feldolgozása (listából egy elem, vagy wildcard törlése)
                if isinstance(val, list):
                    mock_event[clean_name] = val[0]
                elif isinstance(val, str):
                    mock_event[clean_name] = val.replace('*', '')
                else:
                    mock_event[clean_name] = val
                    
    return mock_event

def main():
    if not os.path.exists(SIGMA_BASE_PATH):
        print(f"Hiba: {SIGMA_BASE_PATH} nem található!")
        return

    for root, _, files in os.walk(SIGMA_BASE_PATH):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                category = os.path.basename(root)
                output_dir = os.path.join(OUTPUT_BASE_PATH, category)
                os.makedirs(output_dir, exist_ok=True)

                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        rule = yaml.safe_load(f)
                        if not rule: continue
                        
                        log = generate_mock_event(rule)
                        
                        output_file = file.rsplit('.', 1)[0] + '.json'
                        with open(os.path.join(output_dir, output_file), 'w') as out:
                            json.dump(log, out, indent=4)
                    except Exception as e:
                        print(f"Hiba a generálásnál ({file}): {e}")

    print("✅ A mock logok generálása sikeres (tisztított mezőnevekkel).")

if __name__ == "__main__":
    main()
