# test/test_rules.py
import json
import pytest

def test_credential_dumping_lsass():
    with open("test/logs/credential_dumping_lsass.json") as f:
        logs = json.load(f)

    with open("test/expected/credential_dumping_lsass_expected.json") as f:
        expected = json.load(f)

    detections = []

    for log in logs:
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

    assert detections == expected, "Detection test failed"
