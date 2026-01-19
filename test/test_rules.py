import json
import os
import pytest

# Segédfüggvény JSON fájlok betöltésére
def load_json(path):
    with open(path) as f:
        return json.load(f)

# Mappa útvonalak
logs_dir = "test/logs"
expected_dir = "test/expected"

# Az összes teszt generálása
def generate_tests():
    tests = []
    
    for log_file in os.listdir(logs_dir):
        if log_file.endswith(".json"):
            rule_name = log_file.replace(".json", "")
            log_path = os.path.join(logs_dir, log_file)
            expected_path = os.path.join(expected_dir, f"{rule_name}_expected.json")

            tests.append((log_path, expected_path, rule_name))

    return tests

# A szabály-specifikus logika
def process_rule(rule_name, logs):
    detections = []
    
    # Itt jön a szabály-specifikus logika
    for log in logs:
        if rule_name.lower() == "credential_dumping_lsass":
            if (
                log.get("TargetImage", "").endswith("\\lsass.exe")
                and log.get("Image", "").endswith("\\procdump.exe")
                and log.get("GrantedAccess") in ["0x10", "0x30", "0x50", "0x1fffff"]
            ):
                detections.append({
                    "rule": "Credential Dumping LSASS",
                    "severity": "high",
                    "technique": "T1003.001",
                    "user": log.get("User"),
                    "computer": log.get("Computer")
                })
        elif rule_name.lower() == "t1021" or rule_name.lower() == "suspicious_login":
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
    return detections

# Teszt dinamikus létrehozása
@pytest.mark.parametrize("log_path,expected_path,rule_name", generate_tests())
def test_rule(log_path, expected_path, rule_name):
    logs = load_json(log_path)
    expected = load_json(expected_path)

    detections = process_rule(rule_name, logs)

    assert detections == expected, f"Detection test failed for {rule_name}"

