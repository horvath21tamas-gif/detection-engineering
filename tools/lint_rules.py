# tools/lint_rules.py
import os
import yaml
import subprocess

SIGMA_DIR = os.path.join(os.path.dirname(__file__), '..', 'rules', 'sigma')

def lint_sigma_rules():
    for root, dirs, files in os.walk(SIGMA_DIR):
        for file in files:
            if file.endswith(".yaml"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        rule = yaml.safe_load(f)
                        # Ellenőrizzük, hogy a szükséges kulcsok léteznek-e
                        if 'title' not in rule or 'detection' not in rule:
                            raise ValueError(f"Missing required fields in {file_path}")
                except Exception as e:
                    print(f"Linting failed for {file_path}: {e}")
                    raise
    print("[OK] All Sigma rules validated")

if __name__ == '__main__':
    lint_sigma_rules()
