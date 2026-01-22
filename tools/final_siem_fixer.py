import os
import re

def expand_complex_list(field, values_str, siem_type):
    # Értékek kinyerése és tisztítása
    raw_values = [v.strip().strip("'").strip('"').strip('%').strip('*') for v in values_str.split(',')]
    
    # NetWitness: Meghagyjuk a te eredeti neveidet
    nw_map = {
        "Image": "process", 
        "process": "process",
        "CommandLine": "param", 
        "param": "param",
        "User": "user.dst", 
        "username": "user.dst"
    }
    
    qr_map = {
        "Image": '"Filename"', 
        "username": '"UserName"', 
        "Process CommandLine": '"Process CommandLine"',
        "cs-method": "RequestMethod", 
        "cs-uri-query": "URL"
    }
    
    clean_field = field.strip().strip('"')
    
    if siem_type == "netwitness":
        mapped_field = nw_map.get(clean_field, clean_field)
    else:
        mapped_field = qr_map.get(clean_field, f'"{clean_field}"')

    clauses = []
    for v in raw_values:
        if not v: continue
        # Visszaállítjuk a dupla perjelet és a csillagokat
        v_esc = v.replace("\\", "\\\\")
        
        if siem_type == "qradar":
            clauses.append(f"{mapped_field} LIKE '%{v_esc}%'")
        else: # netwitness - VISSZAÁLLÍTVA A TE STÍLUSODRA
            clauses.append(f"{mapped_field} = '*{v_esc}*'")
    
    # NetWitness-nél a sima OR-t használjuk, hogy konzisztens maradjon veled
    sep = " OR "
    return "(" + sep.join(clauses) + ")"

def fix_qradar(content):
    content = content.replace('""', '"')
    mapping = {'cs-method': 'RequestMethod', 'cs-uri-query': 'URL'}
    for old, new in mapping.items():
        content = content.replace(old, new)
        
    pattern = r'("[^"]+"|\w+)\s+(?:ILIKE ENUMERATION|LIKE)\s*\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "qradar"), content)
    return content

def fix_netwitness(content):
    # 1. Lista alapú minták javítása (megtartva a process/param neveket)
    nw_list_pattern = r'(\w+)\s+(?:contains|ends|=)\s+((?:\'[^\']+\'(?:,)?\s*)+)'
    
    def nw_replacer(match):
        field = match.group(1)
        values_str = match.group(2).strip()
        return expand_complex_list(field, values_str, "netwitness")

    content = re.sub(nw_list_pattern, nw_replacer, content)

    # 2. LOGIKAI TISZTÍTÁS (Ez javítja meg az Invalid Expressiont)
    # Eltávolítjuk a felesleges dupla zárójeleket
    while "((" in content:
        content = content.replace("((", "(").replace("))", ")")
    
    # A NOT utáni részt "laposítjuk", mert a NetWitness nem szereti a NOT (( ))-t
    content = content.replace("NOT ( (", "NOT (").replace("NOT ((", "NOT (")

    # 3. Operátorok és perjelek kényszerítése
    content = content.replace(" && ", " AND ").replace(" || ", " OR ")
    # Minden egyes perjelet megduplázunk, ha még nem lenne az
    content = content.replace("\\", "\\\\").replace("\\\\\\\\", "\\\\")
    
    # Biztosítjuk, hogy a mezőnevek az általad kért formában maradjanak
    mapping = {"filename": "process", "arguments": "param", "Image": "process", "CommandLine": "param"}
    for old, new in mapping.items():
        content = re.sub(rf'\b{old}\b', new, content)

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
