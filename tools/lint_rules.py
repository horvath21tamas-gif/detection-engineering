import os
import yaml

def lint_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            yaml.safe_load(file)
        print(f"Valid YAML: {file_path}")
    except yaml.YAMLError as exc:
        print(f"Error in file {file_path}: {exc}")

def main():
    rules_dir = "rules/sigma"  # Vagy "rules/splunk", attól függően, hogy melyik szabályokat ellenőrizzük
    for root, dirs, files in os.walk(rules_dir):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".spl"):
                file_path = os.path.join(root, file)
                lint_yaml_file(file_path)

if __name__ == "__main__":
    main()
