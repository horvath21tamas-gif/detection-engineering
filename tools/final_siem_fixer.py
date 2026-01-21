import os
import re

def expand_list_to_or_logic(field, values_str):
    """
    Átalakítja a ('val1','val2') listát (field LIKE 'val1' OR field LIKE 'val2') formátumra.
    """
    # Kiszedjük az értékeket a zárójelek közül
    values = [v.strip().strip("'") for v in values_str.split(',')]
    # Felépítjük az OR láncot
    or_chain = " OR ".join([f"{field} LIKE '{v}'" for v in values])
    return f"({or_chain})"

def fix_qradar(content):
    # 1. ENUMERATION és felesleges szavak törlése
    content = content.replace("ENUMERATION", "")
    content = content.replace("ILIKE", "LIKE")
    
    # 2. Mezőnevek fixálása (idézőjelek nélkül)
    mapping = {
        '"Image"': "processname",
        '"Process CommandLine"': "processcommandline",
        '"username"': "username"
    }
    for old, new in mapping.items():
        content = content.replace(old, new)

    # 3. A legnehezebb rész: (field LIKE ('a','b')) -> (field LIKE 'a' OR field LIKE 'b')
    # Regex keresi a: field LIKE ('érték1','érték2'...) mintát
    pattern = r"(\w+)\s+LIKE\s+\(([^)]+)\)"
    
    def replacer(match):
        field = match.group(1)
        values_str = match.group(2)
        if ',' in values_str:
            return expand_list_to_or_logic(field, values_str)
        return match.group(0) # Ha nincs benne vessző, nem nyúlunk hozzá

    content = re.sub(pattern, replacer, content)

    # 4. SELECT váz hozzáadása
    if "SELECT" not in content:
        content = f"SELECT UTF8(payload) as EventPayload, deviceatttime, processname, processcommandline FROM events WHERE {content}"
    
    return content

def fix_netwitness(content):
    # Mezőnevek átalakítása NetWitness meta kulcsokra
    mapping = {
        "Image": "process",
        "CommandLine": "param",
        "username": "user.dst"
    }
    for old, new in mapping.items():
        content = content.replace(old, new)
    
    # NetWitness-nél a % helyett * kell wildcardnak
    content = content.replace("%", "*")
    return content

def process_files():
    # QRadar
    q_path = 'rules/qradar'
    if os.path.exists(q_path):
        for f in os.listdir(q_path):
            if f.endswith('.aql'):
                p = os.path.join(q_path, f)
                with open(p, 'r') as file: data = file.read()
                with open(p, 'w') as file: file.write(fix_qradar(data))

    # NetWitness
    n_path = 'rules/netwitness'
    if os.path.exists(n_path):
        for f in os.listdir(n_path):
            if f.endswith('.txt'):
                p = os.path.join(n_path, f)
                with open(p, 'r') as file: data = file.read()
                with open(p, 'w') as file: file.write(fix_netwitness(data))

if __name__ == "__main__":
    process_files()
