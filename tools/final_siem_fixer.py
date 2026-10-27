import os
import re

def expand_complex_list(field, values_str, siem_type):
    # Értékek kinyerése és tisztítása
    raw_values = [v.strip().strip("'").strip('"').strip('%').strip('*') for v in values_str.split(',')]
    
    # MEZŐNÉV LEKÉPEZÉSEK
    nw_map = {
        "Image": "process", "process": "process",
        "CommandLine": "param", "param": "param",
        "User": "user.dst", "username": "user.dst"
    }
    
    qr_map = {
        "Image": '"Filename"', 
        "username": '"UserName"', 
        "Process CommandLine": '"Process CommandLine"',
        "CommandLine": '"Process CommandLine"',
        "ParentImage": '"Parent Filename"',
        "ParentCommandLine": '"Parent Process CommandLine"',
        "cs-method": "RequestMethod", 
        "cs-uri-query": "URL"
    }

    sentinel_map = {
        "Image": "FolderPath",
        "CommandLine": "ProcessCommandLine",
        "ParentImage": "ParentProcessName",
        "User": "Account",
        "Computer": "DeviceName"
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
        # Speciális karakterek kezelése
        v_esc = v.replace("\\", "\\\\").replace("'", "\\'")
        
        if siem_type == "qradar":
            clauses.append(f"{mapped_field} LIKE '%{v_esc}%'")
        elif siem_type == "sentinel":
            clauses.append(f"{mapped_field} contains '{v_esc}'")
        else: # NetWitness
            clauses.append(f"{mapped_field} = '*{v_esc}*'")
    
    if not clauses: return ""

    if siem_type == "netwitness":
        return "((" + " OR ".join(clauses) + "))"
    
    return "(" + " OR ".join(clauses) + ")"

def fix_sentinel(content):
    """Speciális Sentinel (KQL) javítások"""
    # 1. Alapvető mezőcsere, ha a convert nem tette meg
    sentinel_replacements = {
        "CommandLine": "ProcessCommandLine",
        "Image": "FolderPath",
        "ParentImage": "ParentProcessName",
        "ParentCommandLine": "ParentProcessCommandLine",
        "DestinationPort": "RemotePort",
        "DestinationIp": "RemoteIP"
    }
    for old, new in sentinel_replacements.items():
        content = re.sub(rf'\b{old}\b', new, content)

    content = content.replace("|  |", "|")
    content = re.sub(r'\|\s*$', '', content, flags=re.MULTILINE)
    content = content.replace("== 'None'", "!= ''")

    if "TimeGenerated" not in content:
        content = "DeviceProcessEvents\n| where TimeGenerated > ago(24h)\n" + content

    return content

def fix_qradar(content):
    content = content.replace('""', '"')
    # Bővített mapping QRadarhoz
    mapping = {
        'cs-method': 'RequestMethod', 
        'cs-uri-query': 'URL',
        'Image': '"Filename"',
        'CommandLine': '"Process CommandLine"',
        'ParentImage': '"Parent Filename"'
    }
    for old, new in mapping.items():
        content = re.sub(rf'\b{old}\b', new, content)
        
    pattern = r'("[^"]+"|\w+)\s+(?:ILIKE ENUMERATION|LIKE)\s*\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "qradar"), content)
    
    # Biztosítsuk, hogy az AQL tartalmaz SELECT-et, ha a sigma elhagyta volna
    if not content.startswith("SELECT"):
        content = "SELECT * FROM events WHERE " + content
        
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
    root = os.environ.get('SIEM_ROOT', 'rules')  # CI points this at build/legacy
    tasks = [
        (f'{root}/qradar', '.aql', fix_qradar),
        (f'{root}/netwitness', '.txt', fix_netwitness),
        (f'{root}/sentinel', '.kql', fix_sentinel)
    ]

    for folder, extension, fixer in tasks:
        if os.path.exists(folder):
            count = 0
            for f in os.listdir(folder):
                if f.endswith(extension):
                    p = os.path.join(folder, f)
                    try:
                        with open(p, 'r', encoding='utf-8') as file: 
                            data = file.read()
                        
                        if not data.strip():
                            continue
                            
                        processed_data = fixer(data)
                        
                        with open(p, 'w', encoding='utf-8') as file: 
                            file.write(processed_data)
                        count += 1
                    except Exception as e:
                        print(f"Error processing {p}: {e}")
            print(f"✓ {folder}: {count} queries fixed.")

if __name__ == "__main__":
    process_files()
