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
    condition = detection.get('condition', '').lower()
    
    for key, value in detection.items():
        # 1. KIHAGYJUK a szűrőket (amik a 'not' után vannak vagy 'filter' a nevük)
        if 'filter' in key.lower():
            continue
            
        # 2. CSAK azokat a mezőket vesszük be, amik kellenek a detekcióhoz (szerepelnek a condition-ben)
        if key in condition and isinstance(value, dict):
            for field, val in value.items():
                clean_name = clean_field_name(field)
                
                # Ha a mező már benne van (pl. CommandLine), ne írjuk felül 
                # egy szűrő értékkel, hanem próbáljunk gyanúsat választani
                if isinstance(val, list) and val:
                    # Olyan értéket választunk, ami valószínűleg NEM szűrő (pl. a lista vége vagy gyanúsabb elem)
                    mock_event[clean_name] = val[0]
                elif isinstance(val, str):
                    mock_event[clean_name] = val.replace('*', '')
                else:
                    mock_event[clean_name] = val
                    
    # Manuális korrekció a beküldött példád alapján, hogy ne legyen SYSTEM a tesztben
    if mock_event.get("User") in ["SYSTEM", "LOCAL SERVICE", "NETWORK SERVICE"]:
        mock_event["User"] = "Attacker"
    
    # Ha a CommandLine-ba véletlenül bekerült egy szűrő kifejezés, írjuk felül valami gyanússal
    if "\\Microsoft\\Windows\\" in mock_event.get("CommandLine", ""):
        mock_event["CommandLine"] = "schtasks /create /sc daily /tn 'Persistence' /tr 'C:\\Users\\Public\\malware.exe'"

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
                        output_file = file.rsplit('.', 1)[0] + '.json'
                        with open(os.path.join(output_dir, output_file), 'w') as out:
                            json.dump(log, out, indent=4)
                    except Exception as e:
                        print(f"Hiba: {e}")
    print("✅ Mock logok generálva a szűrők elkerülésével.")

if __name__ == "__main__":
    main()
