import yaml
import json
import os
import uuid
from datetime import datetime

SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def clean_field(f):
    return f.split('|')[0]

def generate_mock_event(rule):
    detection = rule.get('detection', {})
    logsource = rule.get('logsource', {})
    
    # Alapváz
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "Product": logsource.get('product', 'windows'),
        "Service": logsource.get('service', 'sysmon'),
        "User": "AttackerAdmin" # Elkerüljük a SYSTEM szűrőt alapból
    }

    # 1. Összes gyűjtjük a szűrőket, hogy tudjuk, mit kell KERÜLNI
    blacklist = []
    for k, v in detection.items():
        if 'filter' in k.lower() and isinstance(v, dict):
            for val in v.values():
                if isinstance(val, list): blacklist.extend([str(i).lower() for i in val])
                else: blacklist.append(str(val).lower())

    # 2. Végigmegyünk az ÖSSZES detekciós blokkon
    for key, data in detection.items():
        if key in ['condition', 'timeframe'] or 'filter' in key.lower():
            continue
            
        if isinstance(data, dict):
            for field, value in data.items():
                fname = clean_field(field)
                
                # Ha lista, keresünk olyat, ami nincs a tiltólistán
                if isinstance(value, list):
                    chosen = value[0]
                    for candidate in value:
                        if str(candidate).lower() not in blacklist:
                            chosen = candidate
                            break
                    event[fname] = str(chosen).replace('*', '')
                else:
                    event[fname] = str(value).replace('*', '')

    # 3. Kényszerített CommandLine tisztítás (gyakori hibaforrás)
    if "CommandLine" in event:
        # Ha a CommandLine-ba véletlenül bekerült egy legitim útvonal a szabályból
        safe_paths = ["\\microsoft\\windows\\", "windows defender", "googleupdate"]
        if any(p in event["CommandLine"].lower() for p in safe_paths):
            event["CommandLine"] = "powershell.exe -enc ZXZpbGNvZGU=" # Generic gyanús kód

    return event

def main():
    for root, _, files in os.walk(SIGMA_BASE_PATH):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        content = yaml.safe_load(f)
                        if not content or 'detection' not in content: continue
                        
                        log = generate_mock_event(content)
                        
                        category = os.path.basename(root)
                        out_dir = os.path.join(OUTPUT_BASE_PATH, category)
                        os.makedirs(out_dir, exist_ok=True)
                        
                        with open(os.path.join(out_dir, file.replace('.yml', '.json').replace('.yaml', '.json')), 'w') as out:
                            json.dump(log, out, indent=4)
                    except: continue

if __name__ == "__main__":
    main()
