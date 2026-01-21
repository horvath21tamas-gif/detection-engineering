import os
import re

def expand_complex_list(field, values_str, siem_type):
    """
    Szétbontja a listákat érvényes SIEM logikára.
    QRadar: (field LIKE '%val1%' OR field LIKE '%val2%')
    NetWitness: (field = '*val1*' OR field = '*val2*')
    """
    # Értékek kinyerése, tisztítása az idézőjelektől és százalékjelektől
    raw_values = [v.strip().strip("'").strip('"').strip('%').strip('*') for v in values_str.split(',')]
    
    clauses = []
    for v in raw_values:
        if not v: continue
        if siem_type == "qradar":
            clauses.append(f"{field} LIKE '%{v}%'")
        else: # netwitness
            clauses.append(f"{field} = '*{v}*'")
    
    return "(" + " OR ".join(clauses) + ")"

def fix_qradar(content):
    # 1. Mezőnevek kényszerítése (DSM kompatibilis nevek)
    mapping = {
        '"Image"': '"Filename"',
        '"Process CommandLine"': '"Process CommandLine"',
        '"username"': '"UserName"',
        'Image': '"Filename"',
        'username': '"UserName"'
    }
    for old, new in mapping.items():
        content = content.replace(old, new)

    # 2. ILIKE ENUMERATION(...) és LIKE (...) minták keresése
    # Megkeresi a mezőnév + operátor + (lista) szerkezetet
    pattern = r'("[^"]+"|\w+)\s+(?:ILIKE ENUMERATION|LIKE)\s*\(([^)]+)\)'
    
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "qradar"), content)

    # 3. SELECT váz és végső tisztítás
    if "SELECT" not in content:
        content = f"SELECT UTF8(payload), \"Filename\", \"Process CommandLine\" FROM events WHERE {content}"
    
    return content

def fix_netwitness(content):
    # 1. Alapvető operátorok
    content = content.replace(" && ", " AND ").replace(" || ", " OR ")
    
    # 2. Mezőnevek NetWitness meta kulcsokra
    mapping = {
        "Image": "process",
        "CommandLine": "param",
        "User": "user.dst",
        "user.dsts": "user.dst" # Javítás a korábbi elírásodra
    }
    for old, new in mapping.items():
        content = content.replace(old, new)

    # 3. Lista bontás: mező = ('a','b') -> (mező = '*a*' OR mező = '*b*')
    # Regex: mező + egyenlőség + (lista)
    pattern = r'([a-z.0-9]+)\s*=\s*\(([^)]+)\)'
    
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "netwitness"), content)

    # 4. Magányos értékek wildcardozása (ami nem listában van)
    # pl: process = 'schtasks.exe' -> process = '*schtasks.exe*'
    # Csak akkor, ha nincs már ott csillag
    content = re.sub(r"(\w+)\s+=\s+'(?!\*)([^']+)(?<!\*)'", r"\1 = '*\2*'", content)

    return content

def process_files():
    # QRadar
    if os.path.exists('rules/qradar'):
        for f in os.listdir('rules/qradar'):
            if f.endswith('.aql'):
                p = os.path.join('rules/qradar', f)
                with open(p, 'r', encoding='utf-8') as file: data = file.read()
                with open(p, 'w', encoding='utf-8') as file: file.write(fix_qradar(data))

    # NetWitness
    if os.path.exists('rules/netwitness'):
        for f in os.listdir('rules/netwitness'):
            if f.endswith('.txt'):
                p = os.path.join('rules/netwitness', f)
                with open(p, 'r', encoding='utf-8') as file: data = file.read()
                with open(p, 'w', encoding='utf-8') as file: file.write(fix_netwitness(data))

if __name__ == "__main__":
    process_files()
