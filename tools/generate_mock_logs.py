import yaml
import json
import os
import uuid
from datetime import datetime

SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def generate_mock_log(rule_content):
    detection = rule_content.get('detection', {})
    # Alapváz, ami a legtöbb Windows/Sysmon szabályhoz kell
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "User": "TargetUser",
        "SourceUser": "TargetUser",
        "Image": "C:\\Windows\\System32\\cmd.exe",
        "CommandLine": "whoami"
    }
    
    # Minden detekciós blokkot feldolgozunk, ami nem szűrő
    for key, data in detection.items():
        if isinstance(data, dict) and 'filter' not in key.lower() and key != 'condition':
            for field, value in data.items():
                # Sigma specifikus módosítók (pl. |contains) levágása
                clean_name = field.split('|')[0]
                
                # Érték kinyerése (wildcardok nélkül)
                if isinstance(value, list):
                    val = str(value[0]).replace('*', '')
                else:
                    val = str(value).replace('*', '')
                
                event[clean_name] = val
                
                # Kompatibilitási aliasok (ha a szabály máshogy hivatkozna rá)
                if clean_name == "CommandLine": event["command"] = val
                if clean_name == "Image": event["process_path"] = val
                if clean_name == "ParentImage": event["parent_process_path"] = val

    return event

def main():
    if not os.path.exists(SIGMA_BASE_PATH):
        print(f"Hiba: A {SIGMA_BASE_PATH} könyvtár nem található!")
        return

    for root, _, files in os.walk(SIGMA_BASE_PATH):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                rule_full_path = os.path.join(root, file)
                with open(rule_full_path, 'r', encoding='utf-8') as f:
                    try:
                        content = yaml.safe_load(f)
                        if not content or 'detection' not in content:
                            continue
                        
                        # Log generálása
                        log = generate_mock_log(content)
                        
                        # Mentési útvonal meghatározása (tükrözi a szabály struktúráját)
                        rel_path = os.path.relpath(root, SIGMA_BASE_PATH)
                        out_dir = os.path.join(OUTPUT_BASE_PATH, rel_path)
                        os.makedirs(out_dir, exist_ok=True)
                        
                        out_file = os.path.join(out_dir, file.rsplit('.', 1)[0] + '.json')
                        with open(out_file, 'w', encoding='utf-8') as out:
                            json.dump(log, out, indent=4)
                    except Exception as e:
                        print(f"Hiba a {file} feldolgozásakor: {e}")

if __name__ == "__main__":
    main()
