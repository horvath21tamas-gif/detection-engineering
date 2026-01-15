import os
import yaml
import json
from itertools import product

# Mappák
sigma_dir = "rules/sigma"
logs_dir = "test/logs"
expected_dir = "test/expected"

os.makedirs(logs_dir, exist_ok=True)
os.makedirs(expected_dir, exist_ok=True)

# Segédfüggvény: generáljunk egy log példányt a feltételek alapján
def generate_log(selection):
    log = {}
    for key, value in selection.items():
        if isinstance(value, list):
            log[key] = value[0]  # Vegyük az első értéket a teszthez
        elif isinstance(value, dict) and "|endswith" in value:
            log[key] = "TEST" + value["|endswith"]  # endswith mintával
        else:
            log[key] = value
    return log

# Bejárjuk a Sigma szabályokat
for file_name in os.listdir(sigma_dir):
    if not file_name.endswith(".yaml"):
        continue
    rule_path = os.path.join(sigma_dir, file_name)
    with open(rule_path, "r") as f:
        sigma = yaml.safe_load(f)

    rule_id = sigma.get("id") or file_name.replace(".yaml", "")
    rule_name = sigma.get("title", file_name.replace(".yaml", ""))
    condition = sigma.get("detection", {}).get("condition", "selection")

    # Létrehozzuk a log eseményeket
    detections = []
    logs = []

    detection_dict = sigma.get("detection", {})
    selections = {k:v for k,v in detection_dict.items() if k != "condition"}

    # Generáljunk minden selection kombinációt (egyszerűsítve)
    for sel_key, sel_value in selections.items():
        if isinstance(sel_value, dict):
            log = generate_log(sel_value)
        else:
            log = generate_log({sel_key: sel_value})
        logs.append(log)
        detections.append({
            "rule": rule_name,
            "severity": sigma.get("level", "medium"),
            "technique": sigma.get("tags", [""])[0],
            **{k: log.get(k) for k in ["User", "TargetUserName", "Host", "Computer", "IpAddress"] if k in log}
        })

    # Fájlok elérési útja
    log_file_path = os.path.join(logs_dir, f"{rule_id}.json")
    expected_file_path = os.path.join(expected_dir, f"{rule_id}_expected.json")

    # Mentés
    with open(log_file_path, "w") as f:
        json.dump(logs, f, indent=2)
    with open(expected_file_path, "w") as f:
        json.dump(detections, f, indent=2)

    print(f"Generált tesztfájlok a(z) {rule_name} szabályhoz: {log_file_path}, {expected_file_path}")
