import os
import yaml
import re
import json

# ... (a get_rule_data és a generate_visual_matrix függvények maradjanak a régiek) ...

def update_all():
    techniques = get_rule_data()
    generate_visual_matrix(techniques)
    
    # JSON generálása (ez kell a manuális feltöltéshez)
    layer = {
        "name": "Detection Coverage",
        "versions": {"attack": "14", "navigator": "4.9", "layer": "4.4"},
        "domain": "enterprise-attack",
        "techniques": [{"techniqueID": tid, "color": "#ff6666" if lvl in ['high','critical'] else "#ffbd66"} for tid, lvl in techniques.items()]
    }
    with open('attack_navigator_layer.json', 'w', encoding='utf-8') as f:
        json.dump(layer, f, indent=4)

    # README frissítése - ÚGY, HOGY PRIVÁT MÓDBAN IS JÓ LEGYEN
    # A kép elérését abszolút útvonalra cseréljük a saját repódon belül
    USER = "horvath21tamas-gif"
    REPO = "detection-engineering"
    BRANCH = "test"

    readme_content = f"""# 🛡️ Detection Engineering Dashboard

## 📊 MITRE ATT&CK Lefedettségi Kép (Belső)
Ez az ábra a privát szabályaid alapján generálódik és csak te látod:

![MITRE Matrix](https://raw.githubusercontent.com/{USER}/{REPO}/{BRANCH}/mitre_matrix.svg)

> [!TIP]
> **Hogyan nézd meg interaktívan?**
> 1. Kattints ide az üres [MITRE Navigator megnyitásához](https://mitre-attack.github.io/attack-navigator/).
> 2. Válaszd: **Open Existing Layer** -> **Upload from local**.
> 3. Válaszd ki a repódban lévő [attack_navigator_layer.json](./attack_navigator_layer.json) fájlt.
"""
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    update_all()
