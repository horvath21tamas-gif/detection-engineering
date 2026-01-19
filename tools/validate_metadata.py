import os
import yaml

def validate_rule_metadata(rule_file):
    """
    Validálja a szabály metaadatait.
    Ellenőrzi a szükséges mezők meglétét, mint id, title, description.
    """
    required_fields = ['id', 'title', 'description']
    
    try:
        with open(rule_file, 'r', encoding='utf-8') as file:
            rule = yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Error reading YAML file {rule_file}: {e}")
        return False
    except Exception as e:
        print(f"Error opening file {rule_file}: {e}")
        return False
    
    # --- JAVÍTÁS: Ellenőrizzük, hogy a 'rule' nem üres-e ---
    if rule is None:
        print(f"Warning: File is empty or invalid YAML: {rule_file}")
        return False

    # Ellenőrizzük, hogy a beolvasott adat valóban szótár-e (dict)
    if not isinstance(rule, dict):
        print(f"Error: YAML content is not a dictionary in {rule_file}")
        return False
    # -----------------------------------------------------
    
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
    overall_valid = True
    
    for rule_dir in rule_dirs:
        if not os.path.exists(rule_dir):
            print(f"Directory {rule_dir} does not exist.")
            continue
        
        for root, dirs, files in os.walk(rule_dir):
            for file in files:
                # Csak a YAML fájlokat vizsgáljuk metadata szempontból
                if file.endswith('.yaml'):
                    file_path = os.path.join(root, file)
                    if not validate_rule_metadata(file_path):
                        print(f"Validation FAILED for: {file_path}")
                        overall_valid = False
                    else:
                        print(f"Valid metadata in: {file_path}")
    
    # Ha bármelyik fájl hibás volt, jelezzük a rendszernek (exit code 1)
    if not overall_valid:
        exit(1)

if __name__ == "__main__":
    validate_metadata()
