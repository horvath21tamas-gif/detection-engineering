import os

# QRadar specifikus AQL mapping
# Ezeket a mezőneveket a QRadar alapból felismeri
QRADAR_MAPPING = {
    "Image:": "processname:",
    "CommandLine:": "processcommandline:",
    "ParentImage:": "parentprocessname:",
    "ParentCommandLine:": "parentprocesscommandline:",
    "User:": "username:",
    "LogonId:": "logonid:",
    "Hashes:": "hash:",
    "TargetFilename:": "filename:"
}

def preprocess():
    sigma_path = 'rules/sigma'
    for root, _, files in os.walk(sigma_path):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        data = f.read()
                    
                    # Lecseréljük a mezőket a QRadar által emészthető nevekre
                    for old, new in QRADAR_MAPPING.items():
                        data = data.replace(old, new)
                    
                    with open(path, 'w', encoding='utf-8') as wf:
                        wf.write(data)
                except Exception as e:
                    print(f"Hiba: {file} - {e}")

if __name__ == "__main__":
    preprocess()
