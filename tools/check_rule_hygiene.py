import os
import datetime

# A CI/CD környezetben a gyökérkönyvtárból indulunk
SIGMA_RULES_PATH = 'rules/sigma' 
THRESHOLD_DAYS = 90

def check_age():
    today = datetime.datetime.now()
    stale_found = False

    if not os.path.exists(SIGMA_RULES_PATH):
        print(f"[!] Hiba: Nem találom a Sigma szabályokat itt: {SIGMA_RULES_PATH}")
        return

    print(f"--- Sigma Higiénia Ellenőrzés (> {THRESHOLD_DAYS} nap) ---")

    for root, _, files in os.walk(SIGMA_RULES_PATH):
        for file in files:
            if file.endswith(('.yaml', '.yml')):
                file_path = os.path.join(root, file)
                
                # Utolsó módosítás lekérése
                mtime = os.path.getmtime(file_path)
                last_mod = datetime.datetime.fromtimestamp(mtime)
                age = (today - last_mod).days

                if age >= THRESHOLD_DAYS:
                    stale_found = True
                    print(f"[⚠️ FIGYELEM] ELAVULT SZABÁLY: {file} | {age} napja érintetlen ({last_mod.date()})")

    if not stale_found:
        print("[✅ OK] Minden szabály frissítve lett 90 napon belül.")

if __name__ == "__main__":
    check_age()
