# generate_test_files_from_sigma.py
import os
import yaml
import json
from datetime import datetime

# Mappák
sigma_dir = "rules/sigma"
logs_dir = "test/logs"
expected_dir = "test/expected"

# Ha nem léteznek, hozzuk létre a teszt mappákat
os.makedirs(logs_dir, exist_ok=True)
os.makedirs(expected_dir, exist_ok=True)

# Segédfüggvény random host/user generáláshoz
def make_sample_events(detection, num=2):
    events = []
    for i in range(1, num+1):
        event = {}

        # Ha EventID van, tegyük bele
        if "EventID" in detection:
            event["EventID"] = detection["EventID"]
        if "LogonType" in detection:
            event["LogonType"] = detection["LogonType"][0]  # csak az első érték
        if "TargetUserName" in detection:
            event["TargetUserName"] = f"hota05"
        if "IpAddress" in detection:
            event["IpAddress"] = f"10.0.0.{i}"
        if "TargetImage" in detection:
            event["TargetImage"] = detection["TargetImage"]
        if "Image" in detection:
            event["Image"] = detection["Image"]
        if "GrantedAccess" in detection:
            event["GrantedAccess"] = detection["GrantedAccess"]

        # Adjunk hozzá alap mezőket
        event["Host"] = f"HOST{i}"
        event["User"] = event.get("TargetUserName", f"user{i}")
        event["Computer"] = event["Host"]

        events.append(event)
    return events

# Iterate Sigma YAML files
for filename in os.listdir(sigma_dir):
    if filename.endswith(".yaml") or filename.endswith(".yml"):
        filepath = os.path.join(sigma_dir, filename)
        with open(filepath) as f:
            sigma_rule = yaml.safe_load(f)

        # Szabály neve a fájlnév alapján
        rule_name = os.path.splitext(filename)[0]

        # Ellenőrzés: van-e detection mező
        detection = sigma_rule.get("detection")
        if not detection:
            print(f"{filename} nincs detection mező, kihagyva")
            continue

        # Generáljunk logokat
        logs = []
        # A Sigma condition mezőt nem dolgozzuk fel teljesen, csak egyszerű sample eventeket generálunk
        for key, val in detection.items():
            if isinstance(val, dict):
                events = make_sample_events(val)
                logs.extend(events)

        # Mentsük el a logs JSON-t
        logs_path = os.path.join(logs_dir, f"{rule_name}.json")
        with open(logs_path, "w") as f:
            json.dump(logs, f, indent=2)
        
        # Generáljuk az expected JSON-t
        expected = []
        for event in logs:
            expected.append({
                "rule": sigma_rule.get("title", rule_name),
                "severity": sigma_rule.get("level", "medium"),
                "technique": sigma_rule.get("tags", [""])[0] if sigma_rule.get("tags") else "",
                "user": event["User"],
                "computer": event["Computer"]
            })

        expected_path = os.path.join(expected_dir, f"{rule_name}_expected.json")
        with open(expected_path, "w") as f:
            json.dump(expected, f, indent=2)

        print(f"Generált: {logs_path} és {expected_path}")
