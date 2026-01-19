import os
import yaml

def generate_spl_from_sigma():
    sigma_rules_dir = 'rules/sigma'
    splunk_rules_dir = 'rules/splunk'
    if not os.path.exists(splunk_rules_dir):
        os.makedirs(splunk_rules_dir)

    for root, dirs, files in os.walk(sigma_rules_dir):
        for file in files:
            if file.endswith('.yaml'):
                rule_path = os.path.join(root, file)
                with open(rule_path, 'r') as rule_file:
                    sigma_rule = yaml.safe_load(rule_file)

                splunk_rule = convert_sigma_to_spl(sigma_rule)

                # Splunk szabály mentése
                splunk_file_path = os.path.join(splunk_rules_dir, file.replace('.yaml', '.spl'))
                with open(splunk_file_path, 'w') as splunk_file:
                    splunk_file.write(splunk_rule)

                print(f"[OK] Generated SPL for {file}")

def convert_sigma_to_spl(sigma_rule):
    # Itt történik az átalakítás a Splunk szabályra
    splunk_rule = f"# Converted Sigma Rule\n"
    splunk_rule += f"# {sigma_rule.get('title', 'Unnamed Rule')}\n"
    splunk_rule += f"search = {sigma_rule.get('detection', {}).get('search', 'No search defined')}\n"
    return splunk_rule

if __name__ == "__main__":
    generate_spl_from_sigma()
