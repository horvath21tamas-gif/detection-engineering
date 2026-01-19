import os
import yaml

def validate_rule_metadata(rule_file):
    """
    Validálja a szabály metaadatait.
    Ellenőrzi a szükséges mezők meglétét, mint id, title, description.
    """
    required_fields = ['id', 'title', 'description']
    
    try:
        with open(rule_file, 'r') as file:
            rule = yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Error reading YAML file {rule_file}: {e}")
        return False
    except Exception as e:
        print(f"Error opening file {rule_file}: {e}")
        return False
    
    missing_fields = [field for field in required_fields if field not in rule]
    
    if missing_fields:
        print(f"Missing metadata fields in {rule_file}: {', '.join(missing_fields)}")
        return False
    
    return True

def validate_metadata():
    """
    Végigmegy a Sigma és Splunk szabályokon, és ellenőrzi a metaadatokat.
    """
    rule_dirs = ['rules/sigma', 'rules/splunk']
    
    for rule_dir in rule_dirs:
        if not os.path.exists(rule_dir):
            print(f"Directory {rule_dir} does not exist.")
            continue
        
        for root, dirs, files in os.walk(rule_dir):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith('.yaml') or file.endswith('.spl'):
                    if not validate_rule_metadata(file_path):
                        print(f"Invalid metadata in {file_path}")
                    else:
                        print(f"Valid metadata in {file_path}")

if __name__ == "__main__":
    validate_metadata()
