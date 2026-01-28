import yaml
import json
import os
import uuid
import random
from datetime import datetime, timedelta

# Útvonalak a te struktúrád alapján
SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def get_random_ip():
    return f"192.168.1.{random.randint(10, 250)}"

def generate_mock_event(rule_content):
    """Létrehoz egy dúsított eseményt a Sigma szabály alapján"""
    # Alap metaadatok
    mock_event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": (datetime.now() - timedelta(minutes=random.randint(1, 60))).isoformat(),
        "hostname": f"WIN-SRV-{random.randint(10, 99)}",
        "source_ip": get_random_ip(),
        "user": random.choice(["admin", "svc_sql", "j.doe", "db_backup"]),
        "domain": "CORP.LOCAL"
    }
    
    # Detekciós logika kinyerése
    detection = rule_content.get('detection', {})
    # Megnézzük a 'selection' vagy 'selection_...' kezdetű kulcsokat
    selections = [v for k, v in detection.items() if k.startswith('selection')]
    
    if not selections:
        return None

    # Vegyük az első detekciós blokkot
    target_selection = selections[0]
    if isinstance(target_selection, list):
        target_selection = target_selection[0]

    # Mezők átmásolása a logba
    for field, value in target_selection.items():
        if isinstance(value, list):
            mock_event[field] = random.choice(value)
        else:
            mock_event[field] = value
            
    return mock_event

def main():
    print("--- Szintetikus Log Generálás Indítása ---")
    
    # Végigmegyünk a rules/sigma összes alkönyvtárán (pl. credential_access, execution)
    for root, _, files in os.walk(SIGMA_BASE_PATH):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                # Meghatározzuk a kategóriát a mappanév alapján (pl. credential_access)
                category = os.path.basename(root)
                
                # Célmappa létrehozása a test/logs alatt (test/logs/credential_access)
                output_dir = os.path.join(OUTPUT_BASE_PATH, category)
                os.makedirs(output_dir, exist_ok=True)

                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        rule = yaml.safe_load(f)
                        log = generate_mock_event(rule)
                        
                        if log:
                            output_file = file.rsplit('.', 1)[0] + '.json'
                            with open(os.path.join(output_dir, output_file), 'w') as out:
                                json.dump(log, out, indent=4)
                            print(f"[+] OK: {category}/{output_file}")
                    except Exception as e:
                        print(f"[!] HIBA ({file}): {e}")

if __name__ == "__main__":
    main()
