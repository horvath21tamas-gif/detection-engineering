import os
import yaml
import json

# Mappák
rules_dir = "rules/sigma"
logs_dir = "test/logs"
expected_dir = "test/expected"

# Létrehozzuk a mappákat, ha nem léteznek
os.makedirs(logs_dir, exist_ok=True)
os.makedirs(expected_dir, exist_ok=True)

# Segédfüggvény a detekciós mezők egyszerű generálásához
def generate_log_and_expected(sigma_rule):
    log_event = {}
    expected = []

    # Ha Windows szabály
    if sigma_rule.get("logsource", {}).get("product", "").lower() == "windows":
        selection = sigma_rule.get("detection", {}).get("selection_logon", sigma_rule.get("detection", {}))
        if not selection:
            selection = {}

        # Példa: EventID
        if "EventID" in selection:
            log_event["EventID"] = selection["EventID"]

        # Példa: TargetUserName
        if "TargetUserName" in selection:
            if isinstance(selection["TargetUserName"], list):
                log_event["TargetUserName"] = selection["TargetUserName"][0]
            else:
                log_event["TargetUserName"] = selection["TargetUserName"]

        # Példa: Host
        log_event["Host"] = "HOST01"

        # Expected generálás
        expected.append({
            "rule": sigma_rule.get("title", "Unknown Rule"),
            "severity": sigma_rule.get("level", "medium"),
            "technique": sigma_rule.get("tags", [""])[0].upper().replace("ATTACK.", ""),
            "user": log_event.get("TargetUserName", "Unknown"),
            "computer": log_event.get("Host", "Unknown")
        })

    # Linux/egyéb log források
    elif sigma_rule.get("logsource", {}).get("product", "").lower() == "linux":
        log_event = {
            "User": "root",
            "Command": "sudo cat /etc/shadow",
            "Host": "HOST01"
        }
        expected.append({
            "rule": sigma_rule.get("title", "Unknown Rule"),
            "severity": sigma_rule.get("level", "medium"),
            "technique": sigma_rule.get("tags", [""])[0].upper().replace("ATTACK.", ""),
            "user": log_event["User"],
            "computer": log_event["Host"]
        })

    # Ha nem tudjuk
    else:
        log_event = {}
        expected = []

    return log_event, expected


# Iterálunk minden Sigma YAML fájlon
for root, dirs, files in os.walk(rules_dir):
    for file in files:
        if file.endswith(".yaml") or file.endswith(".yml"):
            rule_path = os.path.join(root, file)
            with open(rule_path) as f:
                sigma_rule = yaml.safe_load(f)

            rule_name = file.replace(".yaml", "").replace(".yml", "")

            log_event, expected = generate_log_and_expected(sigma_rule)

            # Fájlok mentése
            log_file_path = os.path.join(logs_dir, f"{rule_name}.json")
            expected_file_path = os.path.join(expected_dir, f"{rule_name}_expected.json")

            with open(log_file_path, "w") as f:
                json.dump([log_event] if log_event else [], f, indent=2)

            with open(expected_file_path, "w") as f:
                json.dump(expected, f, indent=2)

            print(f"[+] Generated test files for {rule_name}")
