import os
import re

def expand_complex_list(field, values_str, siem_type):
    # Értékek kinyerése és tisztítása
    raw_values = [v.strip().strip("'").strip('"').strip('%').strip('*') for v in values_str.split(',')]
    
    # BŐVÍTETT MEZŐNÉV LEKÉPEZÉS
    nw_map = {
        "Image": "filename", 
        "process": "filename",
        "CommandLine": "arguments", 
        "param": "arguments",
        "User": "user.dst", 
        "username": "user.dst",
        "cs-method": "action" # NetWitness-ben gyakran action vagy method
    }
    
    qr_map = {
        "Image": '"Filename"', 
        "username": '"UserName"', 
        "Process CommandLine": '"Process CommandLine"',
        "cs-method": "RequestMethod", # EZ JAVÍTJA A CS-METHOD HIBÁT
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
        # Perjelek duplázása minden SIEM-nél biztonsági okból
        v_esc = v.replace("\\", "\\\\")
        
        if siem_type == "qradar":
            clauses.append(f"{mapped_field} LIKE '%{v_esc}%'")
        else: # netwitness - ÁTÁLLÍTVA CONTAINS-RA WILDCARD NÉLKÜL
            if mapped_field == "filename":
                clauses.append(f"{mapped_field} ends '{v_esc}'")
            else:
                clauses.append(f"{mapped_field} contains '{v_esc}'")
    
    # NetWitness-nél a || stabilabb mint az OR
    sep = " OR " if siem_type == "qradar" else " || "
    return "(" + sep.join(clauses) + ")"

def fix_qradar(content):
    content = content.replace('""', '"')
    # Általános mezőnév csere a listákon kívül is (pl. magányos cs-method)
    mapping = {'cs-method': 'RequestMethod', 'cs-uri-query': 'URL'}
    for old, new in mapping.items():
        content = content.replace(old, new)
        
    pattern = r'("[^"]+"|\w+)\s+(?:ILIKE ENUMERATION|LIKE)\s*\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "qradar"), content)
    return content

def fix_netwitness(content):
    # 1. Lista alapú minták javítása
    nw_list_pattern = r'(\w+)\s+(?:contains|ends|=)\s+((?:\'[^\']+\'(?:,)?\s*)+)'
    
    def nw_replacer(match):
        field = match.group(1)
        values_str = match.group(2).strip()
        return expand_complex_list(field, values_str, "netwitness")

    content = re.sub(nw_list_pattern, nw_replacer, content)

    # 2. Logikai operátorok és perjelek
    content = content.replace(" && ", " AND ").replace(" || ", " OR ")
    content = content.replace("\\", "\\\\") # Dupla perjelek kényszerítése
    
    # 3. Mezőnevek végső simítása
    mapping = {"process": "filename", "param": "arguments", "Image": "filename", "CommandLine": "arguments"}
    for old, new in mapping.items():
        content = re.sub(rf'\b{old}\b', new, content)

    return content

def process_files():
    # ... (a fájlkezelő rész változatlan marad)
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
