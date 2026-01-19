import os
import yaml
import json
from collections import defaultdict

# === ÚTVONALAK (CI-BIZTOS) ===
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SIGMA_DIR = os.path.join(BASE_DIR, "rules", "sigma")
LOGS_DIR = os.path.join(BASE_DIR, "test", "logs")
EXPECTED_DIR = os.path.join(BASE_DIR, "test", "expected")
README_FILE = os.path.join(BASE_DIR, "README.md")

os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(EXPECTED_DIR, exist_ok=True)


# === SIGMA FELDOLGOZÁS ===
def process_rule(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            sigma = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"[ERROR] YAML parsing failed for {file_path}: {e}")
        return None

    rule_id = sigma.get("id") or os.path.splitext(os.path.basename(file_path))[0]
    detection = sigma.get("detection", {}).copy()
    detection.pop("condition", None)

    dummy_log = {}

    for _, value in detection.items():
        if isinstance(value, dict):
            for field, field_val in value.items():
                field_name = field.split("|")[0]
                if isinstance(field_val, list):
                    dummy_log[field_name] = field_val[0]
                else:
                    dummy_log[field_name] = field_val
        elif isinstance(value, list):
            dummy_log["value"] = value[0]

    expected_detection = {
        "rule": sigma.get("title", rule_id),
        "severity": sigma.get("level", "medium"),
        "technique": next(
            (t for t in sigma.get("tags", []) if t.startswith("attack.")),
            "UNMAPPED"
        ),
    }

    log_file = os.path.join(LOGS_DIR, f"{rule_id}.json")
    expected_file = os.path.join(EXPECTED_DIR, f"{rule_id}_expected.json")

    with open(log_file, "w", encoding="utf-8") as f:
        json.dump([dummy_log], f, indent=2, ensure_ascii=False)

    with open(expected_file, "w", encoding="utf-8") as f:
        json.dump([expected_detection], f, indent=2, ensure_ascii=False)

    print(f"[OK] Generated test artifacts for {rule_id}")
    return sigma


# === MITRE TAG KINYERÉS ===
def extract_mitre_techniques(tags):
    techniques = []
    for tag in tags or []:
        if tag.startswith("attack."):
            techniques.append(tag.replace("attack.", "").upper())
    return techniques if techniques else ["UNMAPPED"]


# === README FRISSÍTÉS ===
def update_readme(mitre_rules):
    start_marker = "<!-- SIGMA_RULES_START -->"
    end_marker = "<!-- SIGMA_RULES_END -->"

    if not os.path.exists(README_FILE):
        raise FileNotFoundError("README.md nem található!")

    with open(README_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if start_marker not in content or end_marker not in content:
        raise RuntimeError("SIGMA_RULES marker hiányzik a README.md-ből!")

    lines = []
    for technique in sorted(mitre_rules.keys()):
        lines.append(f"### {technique}")
        for rule in sorted(mitre_rules[technique]):
            lines.append(f"- {rule}")
        lines.append("")

    new_block = f"{start_marker}\n" + "\n".join(lines).strip() + f"\n{end_marker}"

    before = content.split(start_marker)[0]
    after = content.split(end_marker)[1]

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(before + new_block + after)

    print("[OK] README.md successfully updated")


# === MAIN ===
def main():
    if not os.path.isdir(SIGMA_DIR):
        raise RuntimeError(f"Sigma directory not found: {SIGMA_DIR}")

    mitre_rules = defaultdict(list)

    for file in sorted(os.listdir(SIGMA_DIR)):
        if not file.endswith(".yaml"):
            continue

        path = os.path.join(SIGMA_DIR, file)
        sigma = process_rule(path)
        if sigma is None:
            continue  # YAML parsing failed, skip

        title = sigma.get("title", file)
        techniques = extract_mitre_techniques(sigma.get("tags", []))

        for tech in techniques:
            mitre_rules[tech].append(title)

    print("[DEBUG] MITRE grouping:", dict(mitre_rules))
    update_readme(mitre_rules)


if __name__ == "__main__":
    main()

