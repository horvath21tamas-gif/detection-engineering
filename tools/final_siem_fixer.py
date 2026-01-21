import os
import re

def expand_complex_list(field, values_str, siem_type):
    """
    Szétbontja a listákat érvényes SIEM logikára és közben leképezi a mezőneveket.
    """
    raw_values = [v.strip().strip("'").strip('"').strip('%').strip('*') for v in values_str.split(',')]
    
    # Mezőnév leképezés (Mapping)
    nw_map = {"Image": "process", "CommandLine": "param", "User": "user.dst", "username": "user.dst"}
    qr_map = {"Image": '"Filename"', "username": '"UserName"', "Process CommandLine": '"Process CommandLine"'}
    
    clean_field = field.strip().strip('"')
    if siem_type == "netwitness":
        mapped_field = nw_map.get(clean_field, clean_field)
    else:
        mapped_field = qr_map.get(clean_field, f'"{clean_field}"')

    clauses = []
    for v in raw_values:
        if not v: continue
        if siem_type == "qradar":
            clauses.append(f"{mapped_field} LIKE '%{v}%'")
        else: # netwitness
            clauses.append(f"{mapped_field} = '*{v}*'")
    
    return "(" + " OR ".join(clauses) + ")"

def fix_qradar(content):
    content = content.replace('""', '"')
    # Megkeresi a mező LIKE (...) mintákat
    pattern = r'("[^"]+"|\w+)\s+(?:ILIKE ENUMERATION|LIKE)\s*\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "qradar"), content)
    return content

def fix_netwitness(content):
    # 1. Először a magányos mezőneveket cseréljük le (pl. Image = '*...')
    # Úgy keressük, hogy előtte zárójel vagy szóköz van, utána pedig egyenlőségjel
    content = re.sub(r'(\bImage\b)(?=\s*=)', 'process', content)
    content = re.sub(r'(\bCommandLine\b)(?=\s*=)', 'param', content)
    content = re.sub(r'(\bUser\b|\busername\b)(?=\s*=)', 'user.dst', content)

    # 2. Logikai operátorok és wildcardok
    content = content.replace(" && ", " AND ").replace(" || ", " OR ").replace("%", "*")

    # 3. Biztonsági javítás: Ha a \Users\ útvonalat véletlenül elrontotta volna egy korábbi futás
    content = content.replace("user.dst\\Public", "Users\\Public")
    content = content.replace("user.dsts\\Public", "Users\\Public")
    
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
