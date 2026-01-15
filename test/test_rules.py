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

# Iteráljunk az összes log fájlon
for log_file in os.listdir(logs_dir):
    if log_file.endswith(".json"):
        rule_name = log_file.replace(".json", "")
        log_path = os.path.join(logs_dir, log_file)
        expected_path = os.path.join(expected_dir, f"{rule_name}_expected.json")

        # Dinamikus teszt generálása
        def make_test(log_path, expected_path, rule_name):
            def test_rule():
                logs = load_json(log_path)
                expected = load_json(expected_path)

                detections = []

                # Itt jön a Sigma logika – ezt kell módosítani a saját szabályaidhoz
                for log in logs:
                    # Példa szabály: Credential Dumping LSASS
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

                assert detections == expected, f"Detection test failed for {rule_name}"
            return test_rule

        globals()[f"test_{rule_name}"] = make_test(log_path, expected_path, rule_name)
