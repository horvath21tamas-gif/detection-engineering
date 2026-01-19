import os
import yaml
from sigma.parser import SigmaParser

def lint_sigma_rules():
    sigma_rules_dir = 'rules/sigma/credential_access'
    for root, dirs, files in os.walk(sigma_rules_dir):
        for file in files:
            if file.endswith('.yaml'):
                rule_path = os.path.join(root, file)
                try:
                    with open(rule_path, 'r') as rule_file:
                        rule = yaml.safe_load(rule_file)
                        SigmaParser().parse(rule)  # Parse and validate the rule
                    print(f"[OK] Valid Sigma rule: {rule_path}")
                except Exception as e:
                    print(f"[ERROR] Invalid Sigma rule: {rule_path} - {str(e)}")

if __name__ == "__main__":
    lint_sigma_rules()
