import os
import yaml
import json

# Mappák
SIGMA_DIR = "rules/sigma"
LOGS_DIR = "test/logs"
EXPECTED_DIR = "test/expected"

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(EXPECTED_DIR, exist_ok=True)

def generate_dummy_log(detection):
    """
    Egyszerű dummy log generátor a detection mezők alapján
    """
    log = {}
    for key, value in detection.items():
        if isinstance(value, dict):
            # Ha van |endswith filter pl. TargetUserName|endswith
            for subkey, subval in value.items():
                if subkey.endswith("endswith"):
                    field = key
                    log[field] = subval + "_dummy"
        elif isinstance(value, list):
            # Lista: vegyünk egy első elemet
            log[key] = value[0]
        else:
            log[key] = value
    return log

def process_rule(file_path):
    with open(file_path, "r") as f:
        sigma = yaml.safe_load(f)

    rule_id = sigma.get("id") or os.path.splitext(os.path.basename(file_path))[0]
    detections = sigma.get("detection", {})
    condition = detections.pop("condition", "selection")  # alap default

    # Dummy log generálása minden selection/filter alapján
    dummy_log = {}
    for key, value in detections.items():
        if isinstance(value, dict):
            for subkey, subval in value.items():
                if subkey.endswith("endswith"):
                    dummy_log[key] = str(subval) + "_dummy"
                else:
                    dummy_log[key] = subval if isinstance(subval, str) else str(subval[0])
        elif isinstance(value, list):
            dummy_log[key] = value[0]
        else:
            dummy_log[key] = value

    # Várt detekció
    expected_detection = {
        "rule": sigma.get("title", rule_id),
        "severity": sigma.get("level", "medium"),
        "technique": sigma.get("tags", ["unknown"])[0] if sigma.get("tags") else "unknown",
    }

    # Próbáljuk meg kiegészíteni a log mezőket expected-hez
    if "TargetUserName" in dummy_log:
        expected_detection["user"] = dummy_log["TargetUserName"]
    if "Host" in dummy_log:
        expected_detection["computer"] = dummy_log["Host"]
    elif "Computer" in dummy_log:
        expected_detection["computer"] = dummy_log["Computer"]

    # Mentés JSON-be
    log_file = os.path.join(LOGS_DIR, f"{rule_id}.json")
    expected_file = os.path.join(EXPECTED_DIR, f"{rule_id}_expected.json")

    with open(log_file, "w") as f:
        json.dump([dummy_log], f, indent=2)

    with open(expected_file, "w") as f:
        json.dump([expected_detection], f, indent=2)

    print(f"[INFO] Generated {log_file} and {expected_file}")

# Fő loop: minden sigma fájl
for sigma_file in os.listdir(SIGMA_DIR):
    if sigma_file.endswith(".yaml"):
        process_rule(os.path.join(SIGMA_DIR, sigma_file))
