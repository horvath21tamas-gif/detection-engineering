import yaml
import json
import os
import uuid
from datetime import datetime

SIGMA_BASE_PATH = 'rules/sigma'
OUTPUT_BASE_PATH = 'test/logs'

def flatten_value(v):
    """Kinyeri a tiszta szöveget a Sigma értékekből (listákból vagy stringekből)."""
    if isinstance(v, list):
        return [str(i).replace('*', '').replace('?', '') for i in v]
    return [str(v).replace('*', '').replace('?', '')]

def generate_mock_log(rule_content):
    detection = rule_content.get('detection', {})
    logsource = rule_content.get('logsource', {})
    
    # A legfontosabb: a log mezőinek tükrözniük kell a logsource-t!
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        # Sok Sigma backend ezek alapján szűr először
        "product": logsource.get('product'),
        "service": logsource.get('service'),
        "category": logsource.get('category')
    }

    # Minden olyan mezőt kitöltünk, ami a detekcióban szerepel
    for key, data in detection.items():
        # Csak a pozitív illesztéseket nézzük (selection, keywords, stb.)
        if isinstance(data, dict) and 'filter' not in key.lower() and key != 'condition':
            for field, value in data.items():
                clean_field = field.split('|')[0]
                values = flatten_value(value)
                
                # Trükk: összefűzzük az összes értéket egy mezőbe, 
                # így bármelyikre is szűr a szabály, "megtalálja"
                combined_val = " ".join(values)
                event[clean_field] = combined_val
                
                # Aliasok biztosítása
                if clean_field == "CommandLine": event["command"] = combined_val
                if clean_field == "Image": event["process_path"] = combined_val

        # Ha a szabály kulcsszavakat (keywords) használ mezőnév nélkül
        elif isinstance(data, list) and key != 'condition':
            event["raw_data"] = " ".join(flatten_value(data))

    return event

def main():
    processed = 0
    for root, _, files in os.walk(SIGMA_BASE_PATH):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    try:
                        # Safe load kezelése, ha több dokumentum van
                        content_list = list(yaml.safe_load_all(f))
                        for content in content_list:
                            if not content or 'detection' not in content: continue
                            
                            log = generate_mock_log(content)
                            rel_path = os.path.relpath(root, SIGMA_BASE_PATH)
                            out_dir = os.path.join(OUTPUT_BASE_PATH, rel_path)
                            os.makedirs(out_dir, exist_ok=True)
                            
                            out_file_name = file.replace('.yml', '.json').replace('.yaml', '.json')
                            with open(os.path.join(out_dir, out_file_name), 'w') as out:
                                json.dump(log, out, indent=4)
                            processed += 1
                    except Exception as e:
                        print(f"Hiba {file}: {e}")
    print(f"Kész! {processed} log generálva.")

if __name__ == "__main__":
    main()
