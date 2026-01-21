import os
import re

def expand_complex_list(field, values_str, siem_type):
    """
    Szétbontja a listákat (v1, v2) érvényes SIEM logikára.
    QRadar: (field LIKE '%v1%' OR field LIKE '%v2%')
    NetWitness: (field = '*v1*' OR field = '*v2*')
    """
    # Értékek kinyerése és tisztítása
    raw_values = [v.strip().strip("'").strip('"').strip('%').strip('*') for v in values_str.split(',')]
    
    clauses = []
    for v in raw_values:
        if not v: continue
        if siem_type == "qradar":
            clauses.append(f"{field} LIKE '%{v}%'")
        else: # netwitness
            # NetWitnessnél minden tartalmazza/végződik keresés = '*érték*'
            clauses.append(f"{field} = '*{v}*'")
    
    return "(" + " OR ".join(clauses) + ")"

def fix_qradar(content):
    # QRadar most már rendben van a kimeneted alapján, 
    # de a biztonság kedvéért a korábbi javításokat benne hagyjuk.
    content = content.replace('""', '"')
    pattern = r'("[^"]+"|\w+)\s+(?:ILIKE ENUMERATION|LIKE)\s*\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_complex_list(m.group(1), m.group(2), "qradar"), content)
    return content

def fix_netwitness(content):
    # 1. Alapvető logikai operátorok cseréje
    content = content.replace(" && ", " AND ").replace(" || ", " OR ")

    # 2. Speciális NetWitness lista bontás (contains és ends esetére is)
    # Ez a regex elkapja a: field contains 'a','b' és field ends 'a','b' mintákat
    nw_pattern = r'(\w+(?:\.\w+)?)\s+(?:contains|ends|=)\s+((?:\'[^\']+\'(?:,)?\s*)+)'
    
    def nw_replacer(match):
        field = match.group(1)
        # Az értékeket tartalmazó string tisztítása a külső zárójelektől (ha vannak)
        values_str = match.group(2).strip().strip('()')
        return expand_complex_list(field, values_str, "netwitness")

    content = re.sub(nw_pattern, nw_replacer, content)

    # 3. Wildcardok egységesítése
    content = content.replace("%", "*")
    
    # 4. Tisztítás: ha maradtak volna magányos contains/ends szavak
    content = content.replace("contains", "=").replace("ends", "=")
    
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
