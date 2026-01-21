import os
import re

def expand_list(field, values_str, operator):
    """Szétbontja a ('a','b') listát (field OP 'a' OR field OP 'b') formára."""
    # Tisztítjuk az értékeket
    values = [v.strip().strip("'").strip('"') for v in values_str.split(',')]
    
    # QRadar (LIKE) vagy NetWitness (=) formázás
    if operator == "LIKE":
        clauses = [f"{field} LIKE '%{v}%'" for v in values]
    else:
        # NetWitness: a 'contains' és 'ends' helyett is '=' + wildcard
        clauses = [f"{field} = '*{v}*'" for v in values]
        
    return "(" + " OR ".join(clauses) + ")"

def fix_qradar(content):
    # 1. Dupla idézőjelek javítása (pl. ""UserName"" -> "UserName")
    content = content.replace('""', '"')
    
    # 2. Maradék LIKE ('a','b') listák javítása
    # Ez kezeli a NOT ("UserName" LIKE ('%SYSTEM%')) részt is
    pattern = r'("[a-zA-Z\s]+")\s+LIKE\s+\(([^)]+)\)'
    content = re.sub(pattern, lambda m: expand_list(m.group(1), m.group(2), "LIKE"), content)
    
    # 3. SELECT tisztítása (ha kétszer szerepelne)
    if content.count("SELECT") > 1:
        content = "SELECT " + content.split("SELECT")[-1]
    
    return content

def fix_netwitness(content):
    # 1. Alapvető operátor cserék: contains -> =, ends -> =, && -> AND, || -> OR
    content = content.replace(" && ", " AND ").replace(" || ", " OR ")
    
    # 2. Mezőnevek fixálása (ha a Sigma benne hagyta az eredetit)
    mapping = {
        "Image": "process",
        "CommandLine": "param",
        "User": "user.dst"
    }
    for old, new in mapping.items():
        content = content.replace(old, new)

    # 3. Lista bontás: (field operator 'val1','val2'...) -> (field = '*val1*' OR field = '*val2*')
    # Ez felismeri a: (process ends 'a','b') és a (param contains 'a','b') mintákat is
    pattern = r'([a-z.0-9]+)\s+(?:ends|contains|=)\s+\(([^)]+)\)'
    
    def nw_replacer(match):
        field = match.group(1)
        values_str = match.group(2)
        return expand_list(field, values_str, "=")

    content = re.sub(pattern, nw_replacer, content)
    
    # 4. Magányos 'contains' és 'ends' javítása (ha nincs lista, csak egy érték)
    # pl: process ends '\schtasks.exe' -> process = '*\schtasks.exe*'
    content = re.sub(r"(\w+)\s+(?:ends|contains)\s+'([^']+)'", r"\1 = '*\2*'", content)

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
