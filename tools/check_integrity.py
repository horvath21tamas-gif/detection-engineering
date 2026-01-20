import os

def check_and_clean_rules():
    directories = {
        'rules/splunk': '.spl',
        'rules/qradar': '.aql',
        'rules/netwitness': '.txt'
    }
    
    removed_count = 0
    
    for directory, extension in directories.items():
        if not os.path.exists(directory):
            continue
            
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        
        for filename in files:
            path = os.path.join(directory, filename)
            should_remove = False
            reason = ""
            
            # Ellenőrizzük a méretet
            size = os.path.getsize(path)
            if size == 0:
                should_remove = True
                reason = "üres fájl"
            else:
                # Ellenőrizzük a tartalmat
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read().strip()
                    if "Error" in content or "Usage:" in content:
                        should_remove = True
                        reason = "konverziós hibaüzenet"
                    elif len(content) < 10:
                        should_remove = True
                        reason = "túl rövid tartalom"

            if should_remove:
                print(f"🗑️ Törlés: {path} ({reason})")
                os.remove(path)
                removed_count += 1

    if removed_count > 0:
        print(f"\n✅ Összesen {removed_count} hibás szabály lett eltávolítva.")
    else:
        print("\n✨ Minden szabály rendben, nem volt szükség törlésre.")

if __name__ == "__main__":
    check_and_clean_rules()
    # Mindig 0-val lépünk ki, hogy a pipeline ne álljon meg
