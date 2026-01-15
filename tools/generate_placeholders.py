import os, yaml, json

rules_dir = "rules"
logs_dir = "test/logs"
expected_dir = "test/expected"

for root, _, files in os.walk(rules_dir):
    for file in files:
        if file.endswith(".yaml"):
            rule_path = os.path.join(root, file)
            with open(rule_path) as f:
                rule = yaml.safe_load(f)
            rule_id = file.replace(".yaml", "")
            
            log_file = os.path.join(logs_dir, f"{rule_id}.json")
            expected_file = os.path.join(expected_dir, f"{rule_id}_expected.json")
            
            # Ha még nem léteznek, létrehozza alapértelmezett placeholder fájlokat
            if not os.path.exists(log_file):
                with open(log_file, "w") as f:
                    json.dump([], f, indent=2)
            if not os.path.exists(expected_file):
                with open(expected_file, "w") as f:
                    json.dump([], f, indent=2)
