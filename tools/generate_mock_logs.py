import yaml
import json
import os
import uuid
from datetime import datetime

SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def generate_mock_log(rule_content):
    detection = rule_content.get('detection', {})
    logsource = rule_content.get('logsource', {})
    
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "product": logsource.get('product', 'windows'),
        "service": logsource.get('service', 'sysmon'),
        "category": logsource.get('category', 'process_creation'),
    }

    # Megkeressük az első olyan blokkot, ami nem filter és nem condition
    for key, data in detection.items():
        if isinstance(data, dict) and 'filter' not in key.lower() and key != 'condition':
            for field, value in data.items():
                # Mezőnév tisztítása (pl. CommandLine|contains -> CommandLine)
                clean_field = field.split('|')[0]
                
                # Érték kinyerése és tisztítása a wildcardoktól (*, ?)
                if isinstance(value, list):
                    val = str(value[0]).replace('*', '').replace('?', '')
                else:
                    val = str(value).replace('*', '').replace('?', '')
                
                # Trükk: Ha a szabály "contains" módosítót használ, 
                # biztosítjuk, hogy az érték benne legyen egy életszerűbb környezetben
                if '|contains' in field or '|endswith' in field or '|startswith' in field:
                    event[clean_field] = f"test_prefix_{val}_test_suffix"
                else:
                    event[clean_field] = val
                
                # Mappingek a backend kompatibilitás miatt
                if clean_field == "CommandLine": event["command"] = event[clean_field]
                if clean_field == "Image": event["process_path"] = event[clean_field]

    return event

def main():
    processed = 0
    for root, _, files in os.walk(SIGMA_BASE_PATH):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        docs = yaml.safe_load_all(f)
                        for content in docs:
                            if not content or 'detection' not in content: continue
                            
                            log = generate_mock_log(content)
                            rel_path = os.path.relpath(root, SIGMA_BASE_PATH)
                            out_dir = os.path.join(OUTPUT_BASE_PATH, rel_path)
                            os.makedirs(out_dir, exist_ok=True)
                            
                            with open(os.path.join(out_dir, file.replace('.yml', '.json').replace('.yaml', '.json')), 'w') as out:
                                json.dump(log, out, indent=4)
                            processed += 1
                    except: continue
    print(f"Generálva: {processed} log.")

if __name__ == "__main__":
    main()
