import os
import yaml

SIGMA_DIR = os.path.join(os.path.dirname(__file__), '..', 'rules', 'sigma')

def lint_sigma_rules():
    for root, dirs, files in os.walk(SIGMA_DIR):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        rule = yaml.safe_load(f)
                    
                    # Ellenőrizzük, hogy a rule valóban tartalmaz adatokat
                    if rule is None:
                        print(f"[WARNING] {file_path} is empty or invalid YAML.")
                        continue

                    # Ellenőrizzük, hogy a szükséges kulcsok jelen vannak
                    if 'title' not in rule or 'detection' not in rule:
                        print(f"[ERROR] {file_path} is missing 'title' or 'detection' field.")
                        continue

                except yaml.YAMLError as e:
                    print(f"[ERROR] YAML parsing error in {file_path}: {e}")
                    continue

                # További linting szabályok itt...

def main():
    lint_sigma_rules()

if __name__ == "__main__":
    main()
