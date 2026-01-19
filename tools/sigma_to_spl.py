import os
import yaml

SIGMA_DIR = os.path.join(os.path.dirname(__file__), '..', 'rules', 'sigma')
SPLUNK_DIR = os.path.join(os.path.dirname(__file__), '..', 'rules', 'splunk')

def generate_spl_from_sigma():
    if not os.path.isdir(SIGMA_DIR):
        raise RuntimeError(f"Sigma directory not found: {SIGMA_DIR}")
    if not os.path.isdir(SPLUNK_DIR):
        os.makedirs(SPLUNK_DIR)

    for sigma_file in os.listdir(SIGMA_DIR):
        if not sigma_file.endswith(".yaml"):
            continue

        sigma_file_path = os.path.join(SIGMA_DIR, sigma_file)

        try:
            with open(sigma_file_path, 'r', encoding='utf-8') as f:
                sigma_rule = yaml.safe_load(f)
            
            if sigma_rule is None:
                print(f"[WARNING] {sigma_file} is empty or invalid YAML.")
                continue

            # Használjuk os.path.splitext() hogy eltávolítsuk a fájl kiterjesztését
            rule_name = sigma_rule.get('title', os.path.splitext(sigma_file)[0])

            if 'detection' not in sigma_rule:
                print(f"[ERROR] {sigma_file} is missing 'detection' field.")
                continue

            spl = f"# SPL generated from {rule_name}\nsearch index=security\n"
            spl_output = os.path.join(SPLUNK_DIR, f"{rule_name}.spl")

            with open(spl_output, 'w', encoding='utf-8') as spl_f:
                spl_f.write(spl)

            print(f"[OK] Generated SPL for {rule_name}")

        except yaml.YAMLError as e:
            print(f"[ERROR] YAML parsing error in {sigma_file_path}: {e}")
            continue

if __name__ == "__main__":
    generate_spl_from_sigma()
