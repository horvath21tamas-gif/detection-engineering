import os
import re

def expand_complex_list(field, values_str, siem_type):
    # Értékek kinyerése és tisztítása
    raw_values = [v.strip().strip("'").strip('"').strip('%').strip('*') for v in values_str.split(',')]
    
    # 1. MEZŐNÉV LEKÉPEZÉSEK
    # NetWitness: Megtartjuk a 'process' és 'param' neveket
    nw_map = {
        "Image": "process", 
        "process": "process",
        "CommandLine": "param", 
        "param": "param",
        "User": "user.dst", 
        "username": "user.dst"
    }
    
    # QRadar: Itt alkalmazzuk a bővített listát a cs-method javításhoz
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
        # Perjelek duplázása (NetWitness-nél és QRadar-nál is fontos)
        v_esc = v.replace("\\", "\\\\")
        
        if siem_type == "qradar":
            clauses.append(f"{mapped_field} LIKE '%{v_esc}%'")
        else: # NetWitness - Visszatérés az eredeti '=' és '*' stílushoz
            clauses.append(f"{mapped_field} = '*{v_esc}*'")
    
    # NetWitness-nél dupla zárójelet használunk a lista köré, ahogy kérted
    if siem_type == "netwitness":
        return "((" + " OR ".join(clauses) + "))"
    
    return "(" + " OR ".join(clauses) + ")"

def fix_qradar(content):
    content = content.replace('""', '"')
    
    # Magányos mezőnevek cseréje (pl. cs-method a listákon kívül)
    mapping = {'cs-method': 'RequestMethod', 'cs-uri-query': 'URL'}
    for old, new in mapping.items():
        content = content.replace(old, new)
        
    pattern = r'("[^"]+"|\w+)\s+(?:ILIKE ENUMERATION|LIKE)\s*\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "qradar"), content)
    return content

def fix_netwitness(content):
    # 1. Lista alapú minták javítása (process/param megtartásával)
    nw_list_pattern = r'(\w+)\s+(?:contains|ends|=)\s+((?:\'[^\']+\'(?:,)?\s*)+)'
    
    def nw_replacer(match):
        field = match.group(1)
        values_str = match.group(2).strip()
        return expand_complex_list(field, values_str, "netwitness")

    content = re.sub(nw_list_pattern, nw_replacer, content)

    # 2. Logikai tisztítás és operátorok
    content = content.replace(" && ", " AND ").replace(" || ", " OR ")
    
    # 3. NOT blokk javítása (tripla zárójel biztosítása, ha szükséges)
    content = content.replace("NOT (", "NOT ((")
    
    # 4. Perjelek kényszerítése (ha a backend elvétette volna)
    content = re.sub(r'(?<!\\)\\(?!\\)', r'\\\\', content)
    
    # 5. Mezőnevek visszaellenőrzése (ne engedjük át a filename/arguments-et)
    mapping = {"filename": "process", "arguments": "param", "Image": "process", "CommandLine": "param"}
    for old, new in mapping.items():
        content = re.sub(rf'\b{old}\b', new, content)

    # 6. Zárójel egyensúly (hogy ne maradjon nyitott zárójel a végén)
    diff = content.count('(') - content.count(')')
    if diff > 0:
        content += (")" * diff)
    elif diff < 0:
        content = content.rstrip(')') # Levágja a felesleges bezárókat

    return content

def process_files():
    # QRadar feldolgozás
    if os.path.exists('rules/qradar'):
        for f in os.listdir('rules/qradar'):
            if f.endswith('.aql'):
                p = os.path.join('rules/qradar', f)
                with open(p, 'r', encoding='utf-8') as file: data = file.read()
                processed_data = fix_qradar(data)
                with open(p, 'w', encoding='utf-8') as file: file.write(processed_data)

    # NetWitness feldolgozás
    if os.path.exists('rules/netwitness'):
        for f in os.listdir('rules/netwitness'):
            if f.endswith('.txt'):
                p = os.path.join('rules/netwitness', f)
                with open(p, 'r', encoding='utf-8') as file: data = file.read()
                processed_data = fix_netwitness(data)
                with open(p, 'w', encoding='utf-8') as file: file.write(processed_data)

if __name__ == "__main__":
    process_files()
