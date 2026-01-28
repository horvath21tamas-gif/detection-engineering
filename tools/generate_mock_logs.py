import yaml
import json
import os
import uuid
from datetime import datetime

SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def clean_field_name(field):
    return field.split('|')[0]

def generate_mock_event(rule_content):
    logsource = rule_content.get('logsource', {})
    mock_event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "Product": logsource.get('product', 'windows'),
        "Service": logsource.get('service', 'sysmon')
    }
    
    detection = rule_content.get('detection', {})
    
    # Először összegyűjtjük a tiltólistás (filter) értékeket
    filters = set()
    for key, value in detection.items():
        if 'filter' in key.lower() and isinstance(value, dict):
            for field, val in value.items():
                if isinstance(val, list): filters.update([str(v).lower() for v in val])
                else: filters.add(str(val).lower())

    # Generálunk értékeket a pozitív (selection) blokkokból
    for key, value in detection.items():
        if 'selection' in key.lower() or 'suspicious' in key.lower():
            if isinstance(value, dict):
                for field, val in value.items():
                    clean_name = clean_field_name(field)
                    
                    if isinstance(val, list):
                        # Megpróbálunk olyan értéket választani a listából, ami NINCS a szűrőben
                        chosen_val = val[0]
                        for candidate in val:
                            if str(candidate).lower() not in filters:
                                chosen_val = candidate
                                break
                        mock_event[clean_name] = str(chosen_val).replace('*', '')
                    else:
                        mock_event[clean_name] = str(val).replace('*', '')

    # Kényszerített korrekciók, hogy a log biztosan "gonosz" legyen
    if mock_event.get("User", "").upper() in ["SYSTEM", "LOCAL SERVICE"]:
        mock_event["User"] = "DetectedUser"
    
    # Ha a szabály specifikus szerszámokat vár (pl. schtasks), biztosítsuk, hogy ott legyenek
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
                        if not content or 'detection' not in content: continue
                        log = generate_mock_event(content)
                        with open(os.path.join(output_dir, file.rsplit('.', 1)[0] + '.json'), 'w') as out:
                            json.dump(log, out, indent=4)
                    except Exception as e:
                        print(f"Hiba: {e}")

if __name__ == "__main__":
    main()
