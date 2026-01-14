import json
import sys

def main():
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

    if detections != expected:
        print("❌ Detection test failed")
        sys.exit(1)

    print("✅ Detection test passed")

if __name__ == "__main__":
    main()
