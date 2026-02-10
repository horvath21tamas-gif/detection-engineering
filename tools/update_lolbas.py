import requests
import json
import os

def update_lolbas():
    url = "https://lolbas-project.github.io/api/lolbas.json"
    response = requests.get(url)
    if response.status_code == 200:
        # Kiszűrjük csak a binárisok neveit a könnyebb kereséshez
        data = response.json()
        lol_dict = {item['Name'].lower(): f"https://lolbas-project.github.io/lolbas/{item['Fullpath'] if 'Fullpath' in item else ''}" for item in data}
        
        os.makedirs('inventory', exist_ok=True)
        with open('inventory/lolbas_map.json', 'w') as f:
            json.dump(lol_dict, f, indent=4)
        print("✅ LOLBAS adatbázis frissítve.")

if __name__ == "__main__":
    update_lolbas()
