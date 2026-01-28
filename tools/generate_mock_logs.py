import yaml
import json
import os
import uuid
from datetime import datetime

SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def clean_field_name(field):
    """Eltávolítja a módosítókat, pl. CommandLine|contains -> CommandLine"""
    return field.split('|')[0]

def generate_mock_event(rule_content):
    # Alap metaadatok, amiket a legtöbb szabály elvár
    logsource = rule_content.get('logsource', {})
    mock_event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "Product": logsource.get('product', 'windows'),
        "Service": logsource.get('service', 'sysmon')
    }
    
    detection = rule_content.get('detection', {})
    
    # Minden olyan blokkot feldolgozunk, ami NEM a 'condition' vagy 'timeframe'
    for key, value in detection.items():
        if key not in ['condition', 'timeframe'] and isinstance(value, dict):
            for field, val in value.items():
                clean_name = clean_field_name(field)
                
                # Érték tisztítása (listából az első, vagy wildcardok törlése)
                if isinstance(val, list) and len(val) > 0:
                    mock_event[clean_name] = val[0]
                elif isinstance(val, str):
                    mock_event[clean_name] = val.replace('*', '')
                else:
                    mock_event[clean_name] = val
                    
    return mock_event

def main():
    for root, _, files in os.walk(SIGMA_BASE_PATH):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                category = os.path.basename(root)
                output_dir = os.path.join(OUTPUT_BASE_PATH, category)
                os.makedirs(output_dir, exist_ok=True)

                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        content = yaml.safe_load(f)
                        if not content: continue
                        
                        log = generate_mock_event(content)
                        
                        output_file = file.rsplit('.', 1)[0] + '.json'
                        with open(os.path.join(output_dir, output_file), 'w') as out:
                            json.dump(log, out, indent=4)
                    except Exception as e:
                        print(f"Hiba a {file} feldolgozásakor: {e}")

    print("✅ Frissített, okosabb mock logok legyártva.")

if __name__ == "__main__":
    main()
