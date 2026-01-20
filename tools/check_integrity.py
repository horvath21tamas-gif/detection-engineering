import os
import sys

def check_rules():
    directories = {
        'rules/splunk': '.spl',
        'rules/qradar': '.aql',
        'rules/netwitness': '.txt'
    }
    
    errors = []
    
    for directory, extension in directories.items():
        if not os.path.exists(directory):
            continue
            
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        
        for filename in files:
            path = os.path.join(directory, filename)
            size = os.path.getsize(path)
            
            # 1. Hiba: Üres fájl
            if size == 0:
                errors.append(f"❌ Üres fájl: {path}")
                continue
            
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                
                # 2. Hiba: A fájl csak hibaüzenetet tartalmaz
                if "Error" in content or "Usage:" in content:
                    errors.append(f"❌ Konverziós hiba maradt a fájlban: {path}")
                
                # 3. Hiba: Túl rövid tartalom (valószínűleg hibás lekérdezés)
                if len(content) < 10:
                    errors.append(f"❌ Gyanúsan rövid lekérdezés: {path} ('{content}')")

    if errors:
        print("\n--- Integrity Check Hibák ---")
        for err in errors:
            print(err)
        return False
    
    print("\n✅ Minden generált szabály sértetlen és valid.")
    return True

if __name__ == "__main__":
    if not check_rules():
        sys.exit(1)
