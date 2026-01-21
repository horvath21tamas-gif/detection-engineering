import sys
import os
import re

def fix_qradar(content):
    # ENUMERATION eltávolítása (modern QRadar nem szereti)
    content = content.replace("ENUMERATION", "")
    # ILIKE cseréje LIKE-ra
    content = content.replace("ILIKE", "LIKE")
    # Idézőjelek és mezőnevek tisztítása
    content = content.replace('"processname"', 'processname').replace('"processcommandline"', 'processcommandline')
    # Ha maradtak benne felesleges zárójelek az ENUMERATION után
    content = content.replace("( '", "('").replace("' )", "')")
    # Ha nincs SELECT, adjunk hozzá egy alap vázat
    if "SELECT" not in content:
        content = f"SELECT UTF8(payload), processname, processcommandline FROM events WHERE {content}"
    return content

def fix_netwitness(content):
    # A NetWitness gyakran "mező=érték" helyett "mező = 'érték'" formát vár
    # De a legfontosabb: a mezőneveket a meta kulcsokhoz kell igazítani
    mapping = {
        "Image": "process",
        "CommandLine": "param",
        "ParentImage": "parent.process",
        "User": "user.dst",
        "TargetFilename": "filename"
    }
    for old, new in mapping.items():
        content = content.replace(f"{old} =", f"{new} =")
        content = content.replace(f"{old}=", f"{new}=")
    
    # NetWitness-nél a wildcards (*) gyakran jobb, mint a %
    content = content.replace("%", "*")
    return content

def process_files():
    # QRadar javítás
    qradar_path = 'rules/qradar'
    if os.path.exists(qradar_path):
        for f in os.listdir(qradar_path):
            if f.endswith('.aql'):
                p = os.path.join(qradar_path, f)
                with open(p, 'r') as file: content = file.read()
                with open(p, 'w') as file: file.write(fix_qradar(content))

    # NetWitness javítás
    nw_path = 'rules/netwitness'
    if os.path.exists(nw_path):
        for f in os.listdir(nw_path):
            if f.endswith('.txt'):
                p = os.path.join(nw_path, f)
                with open(p, 'r') as file: content = file.read()
                with open(p, 'w') as file: file.write(fix_netwitness(content))

if __name__ == "__main__":
    process_files()
