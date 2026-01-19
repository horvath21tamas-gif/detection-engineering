import json
import pytest
import os

# Segédfüggvény JSON fájlok betöltésére
def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

# A teszt elvárt eredményeinek generálása
def process_rule(rule_name, logs):
    detections = []
    for log in logs:
        if rule_name.lower() == "credential_dumping_lsass":
            if log.get("TargetImage", "").endswith("\\lsass.exe") and log.get("Image", "").endswith("\\procdump.exe"):
                detections.append({
                    "rule": "Credential Dumping LSASS",
                    "severity": "high",
                    "technique": "T1003.001",
                    "user": log.get("User"),
                    "computer": log.get("Computer")
                })
        elif rule_name.lower() == "suspicious_login":
            if log.get("EventID") == 4624 and log.get("TargetUserName") not in ["SYSTEM", "LOCAL SERVICE", "NETWORK SERVICE"]:
                detections.append({
                    "rule": "Suspicious Login",
                    "severity": "medium",
                    "technique": "T1021",
                    "user": log.get("TargetUserName"),
                    "computer": log.get("Host")
                })
    return detections

# Paraméterezett tesztek
@pytest.mark.parametrize("log_path,expected_path,rule_name", [
    ("test/logs/suspicious_login.json", "test/expected/suspicious_login_expected.json", "suspicious_login"),
    ("test/logs/credential_dumping_lsass.json", "test/expected/credential_dumping_lsass_expected.json", "credential_dumping_lsass"),
])
def test_rule(log_path, expected_path, rule_name):
    logs = load_json(log_path)
    expected = load_json(expected_path)
    
    detections = process_rule(rule_name, logs)
    assert detections == expected, f"Detection test failed for {rule_name}"
