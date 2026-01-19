import yaml
import os

def sigma_to_splunk(sigma_rule):
    """
    Konvertálja a Sigma szabályokat Splunk SPL szabályokká.
    """
    splunk_rule = []
    
    if sigma_rule.get('detection'):
        detection = sigma_rule['detection']
        selection = detection.get('selection', {})
        
        if 'EventID' in selection:
            # Például egy EventID alapú SPL szabály létrehozása
            splunk_rule.append(f"index=security sourcetype=WinEventLog:Security EventCode={selection['EventID']}")
            
    return '\n'.join(splunk_rule)

def convert_sigma_files():
    sigma_dir = 'rules/sigma'
    
    for root, dirs, files in os.walk(sigma_dir):
        for file in files:
            if file.endswith('.yaml'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    sigma_rule = yaml.safe_load(f)
                
                splunk_rule = sigma_to_splunk(sigma_rule)
                spl_file_path = file_path.replace('sigma', 'splunk').replace('.yaml', '.spl')
                
                os.makedirs(os.path.dirname(spl_file_path), exist_ok=True)
                
                with open(spl_file_path, 'w') as f:
                    f.write(splunk_rule)

if __name__ == "__main__":
    convert_sigma_files()
