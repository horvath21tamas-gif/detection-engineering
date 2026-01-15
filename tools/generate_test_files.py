import os
import yaml
import json

# Mappák
rules_dir = "rules/sigma"
logs_dir = "test/logs"
expected_dir = "test/expected"

# Ellenőrizzük, hogy a log/expected mappák léteznek-e
os.makedirs(logs_dir, exist_ok=True)
os.makedirs(expected_dir, exist_ok=True)

# Segédfüggvény a példa log generálására Sigma szabály alapján
def generate_log_from_rule(rule):
    log_event = {}

    detection = rule.get("detection", {})
    if not detection:
        return log_event

    # Vegyük a selection részt
    selection = detection.get("selection_logon") or detection.get("selection") or {}
    for key, value in selection.items():
        # |endswith operátor kezelése
        if "|endswith" in key:
            base_key = key.split("|")[0]
            if "User" in base_key or "Name" in base_key:
                log_event[base_key] = "hota05"
            elif "Image" in base_key or "TargetImage" in base_key:
                log_event[base_key] = "\\procdump.exe"
            else:
                log_event[base_key] = "example"
        # Lista esetén vegyük az első elemet
        elif isinstance(value, list):
            log_event[key] = value[0]
        # Egyszerű érték
        else:
            log_event[key] = value

    # Hozzáadunk alapértelmezett mezőket, ha nincsenek
    if "User" not in log_event and "TargetUserName" not in log_event:
        log_event["TargetUserName"] = "hota05"
    if "Computer" not in log_event and "Host" not in log_event:
        log_event["Host"] = "HOST01"

    return log_event

# Bejárjuk a szabályokat
for root, dirs, files in os.walk(rules_dir):
    for file in files:
        if file.endswith(".yaml") or file.endswith(".yml"):
            rule_path = os.path.join(root, file)
            with open(rule_path) as f:
                rule = yaml.safe_load(f)

            # Log fájl neve
            rule_name = rule.get("id") or os.path.splitext(file)[0]
            log_file_path = os.path.join(logs_dir, f"{rule_name}.json")
            expected_file_path = os.path.join(expected_dir, f"{rule_name}_expected.json")

            # Példa log
            log_event = generate_log_from_rule(rule)

            # Több log esemény generálása (például 2 log a teszthez)
            logs = [log_event.copy(), log_event.copy()]
            expected = []

            # A detections lista a teszt logikának megfelelően
            # Itt figyeljük a rule_name-et és a hardcoded logikát a test_rules.py-ból
            for log in logs:
                detections = []

                # Credential Dumping LSASS
                if "lsass" in rule_name.lower():
                    if (
                        log.get("TargetImage", "").endswith("\\lsass.exe")
                        and log.get("Image", "").endswith("\\procdump.exe")
                        and log.get("GrantedAccess") in ["0x10", "0x30", "0x50", "0x1fffff", None]
                    ):
                        detections.append({
                            "rule": "Credential Dumping LSASS",
                            "severity": "high",
                            "technique": "T1003.001",
                            "user": log.get("User"),
                            "computer": log.get("Computer") or log.get("Host")
                        })

                # Multiple Remote Logons / T1021 / suspicious_login
                elif rule_name.lower() == "t1021" or "suspicious_login" in rule_name.lower():
                    if (
                        log.get("EventID") == 4624
                        and log.get("TargetUserName") not in ["SYSTEM", "LOCAL SERVICE", "NETWORK SERVICE"]
                        and log.get("IpAddress") not in ["127.0.0.1", "::1", None]
                    ):
                        detections.append({
                            "rule": "Multiple Remote Logons",
                            "severity": "medium",
                            "technique": "T1021",
                            "user": log.get("TargetUserName"),
                            "computer": log.get("Host")
                        })

                # Ide lehet új szabályokat hozzáadni

                expected.extend(detections)

            # Írjuk a fájlokat
            with open(log_file_path, "w") as f:
                json.dump(logs, f, indent=2)
            with open(expected_file_path, "w") as f:
                json.dump(expected, f, indent=2)

            print(f"Generated {log_file_path} and {expected_file_path}")
