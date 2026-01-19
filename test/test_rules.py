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
        # Ha nem találunk semmit, adjunk hozzá egy default "UNMAPPED" technikát
        if not detections:
            detections.append({
                "rule": f"Rule {rule_name} not matched",
                "severity": "medium",
                "technique": "UNMAPPED"
            })

    return detections
