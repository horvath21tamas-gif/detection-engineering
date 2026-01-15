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

# Segédfüggvény log generálására Sigma szabály alapján
def generate_log_from_rule(rule):
    log_event = {}
    detection = rule.get("detection", {})

    # Vegyük az első "selection" blokkot (ha több van, az első elég a teszthez)
    selection = detection.get("selection") or detection.get("selection_logon") or {}

    for key, value in selection.items():
        # Operátorok kezelése
        if "|endswith" in key:
            base_key = key.split("|")[0]
            if "User" in base_key or "Name" in base_key:
                log_event[base_key] = "hota05"
            elif "Image" in base_key or "TargetImage" in base_key:
                log_event[base_key] = "\\lsass.exe" if "lsass" in rule.get("title", "").lower() else "\\procdump.exe"
            else:
                log_event[base_key] = "example"
        elif isinstance(value, list):
            log_event[key] = value[0] if value else None
        else:
            log_event[key] = value

    # Alapértelmezett mezők
    log_event.setdefault("TargetUserName", "hota05")
    log_event.setdefault("User", "hota05")
    log_event.setdefault("Computer", "HOST01")
    log_event.setdefault("Host", "HOST01")
    log_event.setdefault("IpAddress", "192.168.1.1")
    log_event.setdefault("EventID", 4624)
    log_event.setdefault("LogonType", 10)

    return log_event

# Bejárjuk a Sigma szabályokat
for root, dirs, files in os.walk(rules_dir):
    for file in files:
        if file.endswith(".yaml") or file.endswith(".yml"):
            rule_path = os.path.join(root, file)
            with open(rule_path) as f:
                rule = yaml.safe_load(f)

            # Rule név ID alapján vagy fájlnév
            rule_name = str(rule.get("id") or os.path.splitext(file)[0])

            # Fájlok elérési útja
            log_file_path = os.path.join(logs_dir, f"{rule_name}.json")
            expected_file_path = os.path.join(expected_dir, f"{rule_name}_expected.json")

            # Generáljunk 2 példa logot
            logs = [generate_log_from_rule(rule) for _ in range(2)]
            expected = []

            # Generáljuk az expected listát a test_rules.py logikájához
            for log in logs:
                detections = []

                # Credential Dumping LSASS
                if "lsass" in rule.get("title", "").lower():
                    if log.get("TargetImage", "").endswith("\\lsass.exe") and log.get("Image", "").endswith("\\procdump.exe"):
                        detections.append({
                            "rule": "Credential Dumping LSASS",
                            "severity": "high",
                            "technique": "T1003.001",
                            "user": log.get("User"),
                            "computer": log.get("Computer") or log.get("Host")
                        })

                # Multiple Remote Logons / T1021 / suspicious_login
                elif "t1021" in rule_name.lower() or "suspicious_login" in rule_name.lower():
                    if (
                        log.get("EventID") == 4624
                        and log.get("TargetUserName") not in ["SYSTEM", "LOCAL SERVICE", "NETWORK SERVICE"]
                        and log.get("IpAddress") not in ["127.0.0.1", "::1"]
                    ):
                        detections.append({
                            "rule": "Multiple Remote Logons",
                            "severity": "medium",
                            "technique": "T1021",
                            "user": log.get("TargetUserName"),
                            "computer": log.get("Host")
                        })

                expected.extend(detections)

            # Írjuk a log és expected fájlokat
            with open(log_file_path, "w") as f:
                json.dump(logs, f, indent=2)
            with open(expected_file_path, "w") as f:
                json.dump(expected, f, indent=2)

            print(f"Generated {log_file_path} and {expected_file_path}")
