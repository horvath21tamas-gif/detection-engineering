import os
import yaml

# Mező megfeleltetések a "makacs" SIEM-ekhez
MAPPING = {
    "Image": "process",
    "CommandLine": "command",
    "ParentImage": "parent_process",
    "ParentCommandLine": "parent_command",
    "OriginalFileName": "filename",
    "User": "username",
    "PipeName": "pipename"
}

def preprocess():
    sigma_path = 'rules/sigma'
    for root, _, files in os.walk(sigma_path):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    try:
                        data = f.read()
                        # Egyszerű string csere a mezőkre (gyors és hatékony)
                        for old, new in MAPPING.items():
                            data = data.replace(f"{old}:", f"{new}:")
                        
                        # Visszaírjuk az ideiglenesen módosított szabályt
                        with open(path, 'w', encoding='utf-8') as wf:
                            wf.write(data)
                    except Exception as e:
                        print(f"Hiba a fájl feldolgozásakor: {file} - {e}")

if __name__ == "__main__":
    preprocess()
