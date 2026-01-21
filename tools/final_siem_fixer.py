import os
import re

def expand_complex_list(field, values_str, siem_type):
    """
    Szétbontja a listákat érvényes SIEM logikára.
    QRadar: (field LIKE '%v1%' OR field LIKE '%v2%')
    NetWitness: (field = '*v1*' OR field = '*v2*')
    """
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
    # Mezőnevek kényszerítése (már jól működik nálad, de biztosítjuk a konzisztenciát)
    mapping = {
        '"Image"': '"Filename"',
        '"username"': '"UserName"',
        '"username"': '"UserName"' # esetleges kisbetűs hiba javítása
    }
    for old, new in mapping.items():
        content = content.replace(old, new)
    
    # Dupla idézőjel és egyéb tisztítások
    content = content.replace('""', '"')
    pattern = r'("[^"]+"|\w+)\s+(?:ILIKE ENUMERATION|LIKE)\s*\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "qradar"), content)
    return content

def fix_netwitness(content):
    # 1. MEZŐNEVEK CSERÉJE NetWitness meta-kulcsokra
    # Ez a legfontosabb rész a Meta Database miatt
    mapping = {
        "CommandLine": "param",
        "Image": "process",
        "User": "user.dst",
        "username": "user.dst"
    }
    for old, new in mapping.items():
        content = content.replace(old, new)

    # 2. Lista bontás és operátor javítás (biztonsági mentés, ha maradt volna valami)
    nw_pattern = r'(\w+(?:\.\w+)?)\s+(?:contains|ends|=)\s+((?:\'[^\']+\'(?:,)?\s*)+)'
    content = re.sub(nw_pattern, lambda m: expand_complex_list(m.group(1).strip(), m.group(2).strip().strip('()'), "netwitness"), content)
    
    # 3. Operátorok és wildcardok
    content = content.replace(" && ", " AND ").replace(" || ", " OR ")
    content = content.replace("%", "*")
    
    # 4. Tisztítás: ha esetleg duplázódott volna a mezőnév a csere miatt
    content = content.replace("process = '*", "process = '*").replace("param = '*", "param = '*")
    
    return content

def process_files():
    # QRadar javítás
    if os.path.exists('rules/qradar'):
        for f in os.listdir('rules/qradar'):
            if f.endswith('.aql'):
                p = os.path.join('rules/qradar', f)
                with open(p, 'r', encoding='utf-8') as file: data = file.read()
                with open(p, 'w', encoding='utf-8') as file: file.write(fix_qradar(data))

    # NetWitness javítás
    if os.path.exists('rules/netwitness'):
        for f in os.listdir('rules/netwitness'):
            if f.endswith('.txt'):
                p = os.path.join('rules/netwitness', f)
                with open(p, 'r', encoding='utf-8') as file: data = file.read()
                with open(p, 'w', encoding='utf-8') as file: file.write(fix_netwitness(data))

if __name__ == "__main__":
    process_files()
