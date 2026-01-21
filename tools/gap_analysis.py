import json
import os

def run_gap_analysis():
    layer_path = 'attack_navigator_layer.json'
    if not os.path.exists(layer_path):
        return

    with open(layer_path, 'r') as f:
        data = json.load(f)
    
    covered_techniques = [t['techniqueID'] for t in data.get('techniques', [])]
    
    # Példa kritikus technikákra, amiket mindenképp figyelni kell
    critical_targets = ["T1003", "T1059", "T1053", "T1021", "T1098", "T1547", "T1562"]
    
    gaps = [t for t in critical_targets if t not in covered_techniques]
    
    with open('GAP_ANALYSIS.md', 'w', encoding='utf-8') as f:
        f.write("# 🎯 MITRE ATT&CK Gap Analysis\n\n")
        f.write("Az alábbi kritikus technikákra **jelenleg nincs** aktív detekciós szabályod:\n\n")
        for gap in gaps:
            f.write(f"- [ ] **{gap}** (https://attack.mitre.org/techniques/{gap})\n")
            
    print("✅ Gap Analysis elkészült.")

if __name__ == "__main__":
    run_gap_analysis()
