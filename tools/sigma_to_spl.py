# tools/sigma_to_spl.py
import os
import yaml
from pathlib import Path

SIGMA_DIR = Path("rules/sigma")
SPLUNK_DIR = Path("rules/splunk")

def generate_spl_from_sigma():
    SPLUNK_DIR.mkdir(exist_ok=True)

    for sigma_file in SIGMA_DIR.rglob("*.yaml"):
        with open(sigma_file, 'r', encoding='utf-8') as f:
            sigma_rule = yaml.safe_load(f)

        rule_name = sigma_rule.get('title', sigma_file.stem)
        spl = f"# SPL generated from {rule_name}\nsearch index=security\n"

        # Generálás a Splunk kereséshez (példa, a pontos logikát a sigma szabály alapján kell kitölteni)
        spl += f"search {rule_name} | stats count by src_ip, dest_ip\n"

        output_file = SPLUNK_DIR / f"{sigma_file.stem}.spl"
        with open(output_file, 'w', encoding='utf-8') as out_f:
            out_f.write(spl)

        print(f"[OK] Generated SPL for {rule_name}")

if __name__ == "__main__":
    generate_spl_from_sigma()
