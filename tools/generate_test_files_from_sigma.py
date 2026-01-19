import os
import yaml
import json
from collections import defaultdict

SIGMA_DIR = "rules/sigma"
LOGS_DIR = "test/logs"
EXPECTED_DIR = "test/expected"
README_FILE = "README.md"

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(EXPECTED_DIR, exist_ok=True)


def process_rule(file_path):
    with open(file_path, "r") as f:
        sigma = yaml.safe_load(f)

    rule_id = sigma.get("id") or os.path.splitext(os.path.basename(file_path))[0]
    detections = sigma.get("detection", {}).copy()
    detections.pop("condition", None)

    dummy_log = {}

    for _, value in detections.items():
        if isinstance(value, dict):
            for field, field_val in value.items():
                if isinstance(field_val, list):
                    dummy_log[field.split("|")[0]] = field_val[0]
                else:
                    dummy_log[field.split("|")[0]] = field_val
        elif isinstance(value, list):
            dummy_log["value"] = value[0]

    expected_detection = {
        "rule": sigma.get("title", rule_id),
        "severity": sigma.get("level", "medium"),
        "technique": sigma.get("tags", ["unknown"])[0],
    }

    log_file = os.path.join(LOGS_DIR, f"{rule_id}.json")
    expected_file = os.path.join(EXPECTED_DIR, f"{rule_id}_expected.json")

    with open(log_file, "w") as f:
        json.dump([dummy_log], f, indent=2)

    with open(expected_file, "w") as f:
        json.dump([expected_detection], f, indent=2)

    print(f"[INFO] Generated {log_file} and {expected_file}")

    return sigma


def extract_mitre_tags(tags):
    mitre_tags = []
    for tag in tags or []:
        if tag.startswith("attack."):
            mitre_tags.append(tag.replace("attack.", "").upper())
    return mitre_tags


def update_readme(mitre_rules):
    start_marker = "<!-- SIGMA_RULES_START -->"
    end_marker = "<!-- SIGMA_RULES_END -->"

    if not os.path.exists(README_FILE):
        print("[WARN] README.md not found")
        return

    with open(README_FILE, "r") as f:
        content = f.read()

    if start_marker not in content or end_marker not in content:
        print("[WARN] README markers missing")
        return

    section_lines = []

    for technique in sorted(mitre_rules.keys()):
        section_lines.append(f"### {technique}")
        for rule in sorted(mitre_rules[technique]):
            section_lines.append(f"- {rule}")
        section_lines.append("")

    new_section = (
        f"{start_marker}\n"
        + "\n".join(section_lines).strip()
        + f"\n{end_marker}"
    )

    before = content.split(start_marker)[0]
    after = content.split(end_marker)[1]

    with open(README_FILE, "w") as f:
        f.write(before + new_section + after)

    print("[INFO] README.md updated (MITRE grouped)")


def main():
    mitre_rules = defaultdict(list)

    for sigma_file in os.listdir(SIGMA_DIR):
        if not sigma_file.endswith(".yaml"):
            continue

        path = os.path.join(SIGMA_DIR, sigma_file)
        sigma = process_rule(path)

        title = sigma.get("title", sigma_file)
        mitre_tags = extract_mitre_tags(sigma.get("tags", []))

        if not mitre_tags:
            mitre_rules["UNMAPPED"].append(title)
        else:
            for tag in mitre_tags:
                mitre_rules[tag].append(title)

    update_readme(mitre_rules)


if __name__ == "__main__":
    main()
