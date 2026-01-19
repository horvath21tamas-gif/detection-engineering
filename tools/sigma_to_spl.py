from pathlib import Path
import yaml

SIGMA_DIR = Path("rules/sigma")
OUTPUT_DIR = Path("rules/splunk")


def convert_selection_to_spl(selection, negation=None):
    """
    Egyszerű konverter a selection blokkhoz.
    - selection: dict
    - negation: dict mezők, amiket NOT-tal kell kezelni
    """
    parts = []

    for field, value in selection.items():
        if isinstance(value, list):
            # Lista: OR operátor
            or_parts = [f'{field}="{v}"' for v in value]
            parts.append("(" + " OR ".join(or_parts) + ")")
        else:
            parts.append(f'{field}="{value}"')

    if negation:
        for field, value in negation.items():
            if isinstance(value, list):
                for v in value:
                    parts.append(f'NOT {field}="{v}"')
            else:
                parts.append(f'NOT {field}="{value}"')

    return " ".join(parts)


def process_rule(rule_file):
    with open(rule_file, "r", encoding="utf-8") as f:
        try:
            sigma = yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"[ERROR] Cannot parse {rule_file}: {e}")
            return

    title = sigma.get("title", rule_file.stem)
    detection = sigma.get("detection", {})
    condition = detection.pop("condition", None)

    # Különítsük el a NOT szűrőket
    negation = {}
    for key in list(detection.keys()):
        if key.startswith("filter_") or key.startswith("not_"):
            negation[key.replace("filter_", "").replace("not_", "")] = detection.pop(key)

    # Konvertálás SPL-re
    spl_body = convert_selection_to_spl(detection, negation)

    # Alap SPL
    spl = f"""# SPL generated from {rule_file.name} - {title}
search index=security {spl_body}
"""

    output_file = OUTPUT_DIR / f"{rule_file.stem}.spl"
    output_file.write_text(spl, encoding="utf-8")
    print(f"[OK] Generated SPL: {output_file}")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    for rule in SIGMA_DIR.rglob("*.yaml"):
        process_rule(rule)


if __name__ == "__main__":
    main()
