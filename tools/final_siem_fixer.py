import os
import re

def expand_list_to_or_logic(field, values_str, operator="LIKE"):
    """Szétbontja a listát (field OP 'v1' OR field OP 'v2') formára."""
    values = [v.strip().strip("'").strip("%").strip("*") for v in values_str.split(',')]
    # QRadarhoz LIKE '%érték%', NetWitnesshez = '*érték*'
    if operator == "LIKE":
        or_chain = " OR ".join([f"{field} LIKE '%{v}%'" for v in values])
    else:
        or_chain = " OR ".join([f"{field} = '*{v}*'" for f, v in zip([field]*len(values), values)])
    return f"({or_chain})"

def fix_qradar(content):
    # 1. Alapvető QRadar mezőnevek (DSM függő, de ezek a leggyakoribbak)
    # Ha a processname nem jó, a "Filename" vagy a "Process Name" (idézőjelben) a befutó
    mapping = {
        'processname': '"Filename"',
        'processcommandline': '"Process CommandLine"',
        'username': '"UserName"',
        '"Image"': '"Filename"',
        '"Process CommandLine"': '"Process CommandLine"'
    }
    for old, new in mapping.items():
        content = content.replace(old, new)

    # 2. Tisztítás
    content = content.replace("ENUMERATION", "").replace("ILIKE", "LIKE")
    
    # 3. Lista bontás: mező LIKE ('a','b') -> (mező LIKE '%a%' OR mező LIKE '%b%')
    pattern = r'(\"?[a-zA-Z\s]+\"?)\s+LIKE\s+\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_list_to_or_logic(m.group(1), m.group(2), "LIKE"), content)

    # 4. SELECT javítás
    if "SELECT" not in content:
        content = f"SELECT UTF8(payload), \"Filename\", \"Process CommandLine\" FROM events WHERE {content}"
    
    return content

def fix_netwitness(content):
    # NetWitness-nél nincs CONTAINS, helyette mező = '*érték*'
    # 1. Mezőnevek fixálása
    mapping = {
        "Image": "process",
        "CommandLine": "param",
        "username": "user.dst",
        "CONTAINS": "=" # Ez a legfontosabb javítás
    }
    for old, new in mapping.items():
        content = content.replace(old, new)

    # 2. Lista bontás NetWitnessre: mező = ('a','b') -> (mező = '*a*' OR mező = '*b*')
    pattern = r'(\w+)\s+=\s+\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_list_to_or_logic(m.group(1), m.group(2), "="), content)

    # 3. Wildcard javítás: % -> *
    content = content.replace("%", "*")
    
    # Felesleges LIKE-ok törlése, ha maradtak volna
    content = content.replace("LIKE", "=")
    return content

def process_files():
    # QRadar (.aql)
    if os.path.exists('rules/qradar'):
        for f in os.listdir('rules/qradar'):
            if f.endswith('.aql'):
                p = os.path.join('rules/qradar', f)
                with open(p, 'r') as file: data = file.read()
                with open(p, 'w') as file: file.write(fix_qradar(data))

    # NetWitness (.txt)
    if os.path.exists('rules/netwitness'):
        for f in os.listdir('rules/netwitness'):
            if f.endswith('.txt'):
                p = os.path.join('rules/netwitness', f)
                with open(p, 'r') as file: data = file.read()
                with open(p, 'w') as file: file.write(fix_netwitness(data))

if __name__ == "__main__":
    process_files()
