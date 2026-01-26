import os
import re

def expand_complex_list(field, values_str, siem_type):
    # Értékek kinyerése és tisztítása
    raw_values = [v.strip().strip("'").strip('"').strip('%').strip('*') for v in values_str.split(',')]
    
    # 1. MEZŐNÉV LEKÉPEZÉSEK
    nw_map = {
        "Image": "process", "process": "process",
        "CommandLine": "param", "param": "param",
        "User": "user.dst", "username": "user.dst"
    }
    
    qr_map = {
        "Image": '"Filename"', "username": '"UserName"', 
        "Process CommandLine": '"Process CommandLine"',
        "cs-method": "RequestMethod", "cs-uri-query": "URL"
    }

    # SENTINEL MAP: KQL specifikus mezők
    sentinel_map = {
        "Image": "FolderPath",
        "CommandLine": "ProcessCommandLine",
        "ParentImage": "ParentProcessName",
        "User": "Account"
    }
    
    clean_field = field.strip().strip('"')
    
    if siem_type == "netwitness":
        mapped_field = nw_map.get(clean_field, clean_field)
    elif siem_type == "sentinel":
        mapped_field = sentinel_map.get(clean_field, clean_field)
    else:
        mapped_field = qr_map.get(clean_field, f'"{clean_field}"')

    clauses = []
    for v in raw_values:
        if not v: continue
        v_esc = v.replace("\\", "\\\\")
        
        if siem_type == "qradar":
            clauses.append(f"{mapped_field} LIKE '%{v_esc}%'")
        elif siem_type == "sentinel":
            # KQL-ben a contains hatékonyabb nagy szövegekre
            clauses.append(f"{mapped_field} contains '{v_esc}'")
        else: # NetWitness
            clauses.append(f"{mapped_field} = '*{v_esc}*'")
    
    if siem_type == "netwitness":
        return "((" + " OR ".join(clauses) + "))"
    
    return "(" + " OR ".join(clauses) + ")"

def fix_sentinel(content):
    """Speciális Sentinel (KQL) javítások"""
    # 1. Mezőnevek utólagos finomhangolása
    sentinel_replacements = {
        "CommandLine": "ProcessCommandLine",
        "Image": "FolderPath",
        "ParentImage": "ParentProcessName",
        "\\\\": "\\" # KQL néha nem szereti a túlzott escape-elést a végén
    }
    for old, new in sentinel_replacements.items():
        content = content.replace(old, new)

    # 2. Üres sorok és felesleges Pipe (|) karakterek takarítása
    content = content.replace("|  |", "|")
    
    return content

def fix_qradar(content):
    content = content.replace('""', '"')
    mapping = {'cs-method': 'RequestMethod', 'cs-uri-query': 'URL'}
    for old, new in mapping.items():
        content = content.replace(old, new)
        
    pattern = r'("[^"]+"|\w+)\s+(?:ILIKE ENUMERATION|LIKE)\s*\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "qradar"), content)
    return content

def fix_netwitness(content):
    nw_list_pattern = r'(\w+)\s+(?:contains|ends|=)\s+((?:\'[^\']+\'(?:,)?\s*)+)'
    content = re.sub(nw_list_pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "netwitness"), content)
    content = content.replace(" && ", " AND ").replace(" || ", " OR ")
    content = content.replace("NOT (", "NOT ((")
    content = re.sub(r'(?<!\\)\\(?!\\)', r'\\\\', content)
    mapping = {"filename": "process", "arguments": "param", "Image": "process", "CommandLine": "param"}
    for old, new in mapping.items():
        content = re.sub(rf'\b{old}\b', new, content)

    diff = content.count('(') - content.count(')')
    if diff > 0: content += (")" * diff)
    elif diff < 0: content = content.rstrip(')')
    return content

def process_files():
    # SIEM típusok és hozzájuk tartozó fixerek meghatározása
    tasks = [
        ('rules/qradar', '.aql', fix_qradar),
        ('rules/netwitness', '.txt', fix_netwitness),
        ('rules/sentinel', '.kql', fix_sentinel) # ÚJ: Sentinel feladat
    ]

    for folder, extension, fixer in tasks:
        if os.path.exists(folder):
            for f in os.listdir(folder):
                if f.endswith(extension):
                    p = os.path.join(folder, f)
                    with open(p, 'r', encoding='utf-8') as file: data = file.read()
                    processed_data = fixer(data)
                    with open(p, 'w', encoding='utf-8') as file: file.write(processed_data)
            print(f"✓ {folder} queries fixed.")

if __name__ == "__main__":
    process_files()
