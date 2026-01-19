# tools/generate_placeholders.py
import os
import yaml
from collections import defaultdict

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SIGMA_DIR = os.path.join(BASE_DIR, "rules", "sigma")
README_FILE = os.path.join(BASE_DIR, "README.md")

def update_readme_with_sigma():
    mitre_rules = defaultdict(list)

    for root, dirs, files in os.walk(SIGMA_DIR):
        for file in files:
            if file.endswith(".yaml"):
                rule_path = os.path.join(root, file)
                with open(rule_path, 'r', encoding='utf-8') as f:
                    rule = yaml.safe_load(f)
                    title = rule.get("title", "Unnamed Rule")
                    tags = rule.get("tags", [])
                    techniques = [tag.replace("attack.", "") for tag in tags if tag.startswith("attack.")]
                    if not techniques:
                        techniques = ["UNMAPPED"]
                    for tech in techniques:
                        mitre_rules[tech].append(title)

    start_marker = "<!-- SIGMA_RULES_START -->"
    end_marker = "<!-- SIGMA_RULES_END -->"

    with open(README_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    if start_marker not in content or end_marker not in content:
        raise RuntimeError("SIGMA_RULES marker hiányzik a README.md-ből!")

    lines = []
    for technique, rules in sorted(mitre_rules.items()):
        lines.append(f"### {technique}")
        for rule in sorted(rules):
            lines.append(f"- {rule}")
        lines.append("")

    new_block = f"{start_marker}\n" + "\n".join(lines).strip() + f"\n{end_marker}"

    before = content.split(start_marker)[0]
    after = content.split(end_marker)[1]

    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(before + new_block + after)

    print("[OK] README.md successfully updated")

if __name__ == "__main__":
    update_readme_with_sigma()
