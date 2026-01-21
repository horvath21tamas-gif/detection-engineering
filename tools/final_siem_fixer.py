import os
import re

def expand_complex_list(field, values_str, siem_type):
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
    # KIFEJEZETT MEZŐNÉV CSERE QRADARHOZ
    mapping = {
        '"Image"': '"Filename"',
        '"username"': '"UserName"',
        '"Process CommandLine"': '"Process CommandLine"'
    }
    for old, new in mapping.items():
        content = content.replace(old, new)
    
    # Ha a sigma-cli véletlenül idézőjel nélkül hagyta volna:
    content = content.replace(' Image ', ' "Filename" ').replace(' username ', ' "UserName" ')
    
    # Tisztítás
    content = content.replace('""', '"')
    pattern = r'("[^"]+"|\w+)\s+(?:ILIKE ENUMERATION|LIKE)\s*\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "qradar"), content)
    return content

def fix_netwitness(content):
    # KIFEJEZETT MEZŐNÉV CSERE NETWITNESZHEZ
    # Ezeket a meta-kulcsokat használja az RSA/NetWitness alapból
    mapping = {
        "CommandLine =": "param =",
        "Image =": "process =",
        "User =": "user.dst =",
        "username =": "user.dst ="
    }
    for old, new in mapping.items():
        content = content.replace(old, new)

    # Lista bontás és operátor javítás
    nw_pattern = r'(\w+(?:\.\w+)?)\s+(?:contains|ends|=)\s+((?:\'[^\']+\'(?:,)?\s*)+)'
    content = re.sub(nw_pattern, lambda m: expand_complex_list(m.group(1).strip(), m.group(2).strip().strip('()'), "netwitness"), content)
    
    content = content.replace(" && ", " AND ").replace(" || ", " OR ")
    content = content.replace("%", "*")
    return content

def process_files():
    if os.path.exists('rules/qradar'):
        for f in os.listdir('rules/qradar'):
            if f.endswith('.aql'):
                p = os.path.join('rules/qradar', f)
                with open(p, 'r', encoding='utf-8') as file: data = file.read()
                with open(p, 'w', encoding='utf-8') as file: file.write(fix_qradar(data))

    if os.path.exists('rules/netwitness'):
        for f in os.listdir('rules/netwitness'):
            if f.endswith('.txt'):
                p = os.path.join('rules/netwitness', f)
                with open(p, 'r', encoding='utf-8') as file: data = file.read()
                with open(p, 'w', encoding='utf-8') as file: file.write(fix_netwitness(data))

if __name__ == "__main__":
    process_files()
