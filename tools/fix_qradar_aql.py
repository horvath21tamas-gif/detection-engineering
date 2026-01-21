import sys
import re

def fix_aql(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. ENUMERATION eltávolítása és IN/OR logikára váltás
    # A Sigma rosszul használja az ENUMERATION-t, sima zárójelek és LIKE kell helyette
    content = content.replace("ENUMERATION", "")
    
    # 2. ILIKE cseréje LIKE-ra (QRadarban a LIKE alapból case-insensitive lehet konfigurációtól függően, 
    # de a modern AQL a LIKE-ot szereti)
    content = content.replace("ILIKE", "LIKE")

    # 3. Mezőnevek fixálása (idézőjelek és nevek)
    # A QRadar AQL-ben a mezőnevek idézőjel nélkül vagy dupla idézőjellel kellenek, 
    # de a preprocesszált neveket használjuk.
    mapping = {
        '"Image"': "processname",
        '"Process CommandLine"': "processcommandline",
        '"username"': "username"
    }
    for old, new in mapping.items():
        content = content.replace(old, new)

    # 4. Tisztítás: Dupla zárójelek és felesleges karakterek
    content = re.sub(r'\s+', ' ', content) # Szóközök tisztítása

    # 5. AQL váz felépítése (ha a konverter nagyon elrontotta volna a SELECT részt)
    if "SELECT" not in content:
        content = f"SELECT processname, processcommandline, username, DATEFORMAT(devicetime, 'yyyy-MM-dd HH:mm:ss') as Time FROM events WHERE {content}"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        fix_aql(sys.argv[1])
