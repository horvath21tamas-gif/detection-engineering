from pathlib import Path

SIGMA_DIR = Path("rules/sigma")
OUTPUT_DIR = Path("rules/splunk")

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    for rule in SIGMA_DIR.rglob("*.yaml"):
        spl = f"# SPL generated from {rule.name}\nsearch index=security\n"
        output = OUTPUT_DIR / f"{rule.stem}.spl"
        output.write_text(spl)

if __name__ == "__main__":
    main()
