import yaml
import json
import os
import uuid
from datetime import datetime

SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def clean_field_name(field):
    """Eltávolítja a Sigma módosítókat: pl. Image|endswith -> Image"""
    return field.split('|')[0]

def generate_mock_event(rule_content):
    # Alap metaadatok, amik nélkül sok Sigma motor el sem indul
    logsource = rule_content.get('logsource', {})
    mock_event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "Product": logsource.get('product', 'windows'),
        "Service": logsource.get('service', 'sysmon'),
        "Source": logsource.get('source', 'Security')
    }
    
    detection = rule_content.get('detection', {})
    
    # Végigmegyünk az összes detekciós blokkon (kivéve a kondíciót)
    for key, value in detection.items():
        if key not in ['condition', 'timeframe'] and isinstance(value, dict):
            for field, val in value.items():
                clean_name = clean_field_name(field)
                
                # Érték finomítása
                if isinstance(val, list) and val:
                    mock_event[clean_name] = val[0] # Listából az elsőt vesszük
                elif isinstance(val, str):
                    mock_event[clean_name] = val.replace('*', '') # Wildcard törlése
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
                        content = yaml.safe_load(f)
                        if not content or 'detection' not in content:
                            continue
                        
                        log = generate_mock_event(content)
                        
                        output_file = file.rsplit('.', 1)[0] + '.json'
                        with open(os.path.join(output_dir, output_file), 'w') as out:
                            json.dump(log, out, indent=4)
                    except Exception as e:
                        print(f"Hiba a {file} feldolgozásakor: {e}")

    print("✅ Az okosabb mock logok generálása befejeződött.")

if __name__ == "__main__":
    main()
