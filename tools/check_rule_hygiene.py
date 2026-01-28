import os
import datetime

# Útvonalak beállítása a struktúrád alapján
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# A tools-ból egyet vissza, majd be a rules/sigma szabályok mappába
SIGMA_RULES_PATH = os.path.join(BASE_DIR, '..', 'rules', 'sigma szabályok')
THRESHOLD_DAYS = 90

def check_age():
    today = datetime.datetime.now()
    stale_rules = []

    if not os.path.exists(SIGMA_RULES_PATH):
        print(f"[!] Hiba: Nem találom a Sigma szabályokat itt: {SIGMA_RULES_PATH}")
        return

    print(f"--- Sigma Higiénia Ellenőrzés (> {THRESHOLD_DAYS} nap) ---")

    for root, _, files in os.walk(SIGMA_RULES_PATH):
        for file in files:
            if file.endswith(('.yml', '.yaml')):
                file_path = os.path.join(root, file)
                
                # Utolsó módosítás lekérése
                mtime = os.path.getmtime(file_path)
                last_mod = datetime.datetime.fromtimestamp(mtime)
                age = (today - last_mod).days

                if age >= THRESHOLD_DAYS:
                    stale_rules.append((file, age, last_mod.date()))

    if stale_rules:
        print(f"\n[!] {len(stale_rules)} szabály elavult:")
        for name, days, l_date in stale_rules:
            print(f" - {name:30} | {days} napja módosítva ({l_date})")
    else:
        print("\n[+] Minden szabály naprakész!")

if __name__ == "__main__":
    check_age()
