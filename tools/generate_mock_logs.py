import yaml
import json
import os
import uuid
import random
from datetime import datetime

SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def clean_field_name(field):
    """Eltávolítja a Sigma módosítókat (pl. |contains, |endswith) a mezőnévből"""
    return field.split('|')[0]

def generate_mock_event(rule_content):
    # Alapváz, ami sok szabályhoz kell
    mock_event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "Product": rule_content.get('logsource', {}).get('product', 'windows'),
        "Service": rule_content.get('logsource', {}).get('service', 'sysmon'),
    }
    
    detection = rule_content.get('detection', {})
    # Megkeressük az összes selection-t
    for key, value in detection.items():
        if key.startswith('selection'):
            if isinstance(value, dict):
                for field, val in value.items():
                    clean_field = clean_field_name(field)
                    # Ha lista, válasszunk egy elemet, ha string, tisztítsuk a wildcards-tól
                    if isinstance(val, list):
                        mock_event[clean_field] = val[0]
                    else:
                        mock_event[clean_field] = str(val).replace('*', '')
    
    return mock_event

def main():
    for root, _, files in os.walk(SIGMA_BASE_PATH):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                category = os.path.basename(root)
                output_dir = os.path.join(OUTPUT_BASE_PATH, category)
                os.makedirs(output_dir, exist_ok=True)

                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    rule = yaml.safe_load(f)
                    log = generate_mock_event(rule)
                    
                    output_file = file.rsplit('.', 1)[0] + '.json'
                    with open(os.path.join(output_dir, output_file), 'w') as out:
                        json.dump(log, out, indent=4)
    print("Mock logok újra-generálva okosabb logikával.")

if __name__ == "__main__":
    main()
