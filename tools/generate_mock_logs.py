import yaml
import json
import os
import uuid
from datetime import datetime

SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def generate_mock_log(rule_content):
    """
    Legyárt egy mesterséges log eseményt a Sigma szabály detekciós logikája alapján.
    """
    detection = rule_content.get('detection', {})
    logsource = rule_content.get('logsource', {})
    
    # Alap metaadatok, amiket sok SIEM/Sigma backend elvár
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "product": logsource.get('product', 'windows'),
        "service": logsource.get('service', 'sysmon'),
        "category": logsource.get('category', 'process_creation'),
        "User": "TargetUser",
        "SourceUser": "TargetUser"
    }
    
    # Alapértelmezett értékek, ha a szabály nem specifikálja
    if event["category"] == "process_creation":
        event["Image"] = "C:\\Windows\\System32\\cmd.exe"
        event["CommandLine"] = "whoami"

    # Végigmegyünk a detekciós blokkokon (kivéve a condition-t és a filtereket)
    for key, data in detection.items():
        if isinstance(data, dict) and 'filter' not in key.lower() and key != 'condition':
            for field, value in data.items():
                # Sigma módosítók (pl. |contains, |endswith) levágása
                clean_name = field.split('|')[0]
                
                # Érték feldolgozása (ha lista, az első elemet vesszük)
                if isinstance(value, list):
                    val = str(value[0])
                else:
                    val = str(value)

                # Wildcardok eltávolítása a teszt adathoz
                clean_val = val.replace('*', '')

                # Érték beillesztése a logba
                # Ha a szabály specifikus értéket vár, azt adjuk meg neki
                event[clean_name] = clean_val
                
                # Néhány gyakori SIEM mező-mapping (aliasok)
                if clean_name == "CommandLine":
                    event["command"] = clean_val
                elif clean_name == "Image":
                    event["process_path"] = clean_val
                elif clean_name == "ParentImage":
                    event["parent_process_path"] = clean_val

    return event

def main():
    if not os.path.exists(SIGMA_BASE_PATH):
        print(f"Hiba: A {SIGMA_BASE_PATH} könyvtár nem található!")
        return

    processed_count = 0
    for root, _, files in os.walk(SIGMA_BASE_PATH):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                rule_full_path = os.path.join(root, file)
                with open(rule_full_path, 'r', encoding='utf-8') as f:
                    try:
                        # Több dokumentum kezelése egy YAML-en belül (Sigma gyűjtemények)
                        docs = yaml.safe_load_all(f)
                        for content in docs:
                            if not content or 'detection' not in content:
                                continue
                            
                            log = generate_mock_log(content)
                            
                            # Mentési struktúra kialakítása
                            rel_path = os.path.relpath(root, SIGMA_BASE_PATH)
                            out_dir = os.path.join(OUTPUT_BASE_PATH, rel_path)
                            os.makedirs(out_dir, exist_ok=True)
                            
                            out_file = os.path.join(out_dir, file.rsplit('.', 1)[0] + '.json')
                            with open(out_file, 'w', encoding='utf-8') as out:
                                json.dump(log, out, indent=4)
                            
                            processed_count += 1
                    except Exception as e:
                        print(f"Hiba a {file} feldolgozásakor: {e}")

    print(f"Siker: {processed_count} teszt log generálva a {OUTPUT_BASE_PATH} mappába.")

if __name__ == "__main__":
    main()
