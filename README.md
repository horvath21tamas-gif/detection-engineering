# Detection Engineering

Sigma-alapú detection-as-code repó: a szabályok (`rules/sigma/`) az egyetlen igazságforrás, a CI ellenőrzi,
teszteli és lefordítja őket a SIEM-ek nyelvére – **Wazuh**, Splunk, Elastic, valamint (best effort) QRadar,
NetWitness és Sentinel formátumra.

[![CI](../../actions/workflows/ci.yml/badge.svg)](../../actions/workflows/ci.yml)

| | |
|---|---|
| Sigma szabályok | `rules/sigma/` (628 db, ATT&CK technikánként egy fájl) |
| Dashboard, lefedettség, wiki | [DASHBOARD.md](DASHBOARD.md) · [COVERAGE.md](COVERAGE.md) · `DETECTION_WIKI_*.md` |
| Wazuh fordító és deploy | [wazuh/README.md](wazuh/README.md) |
| Eszközkészlet (Python) | `src/dectools/` – validátor, Wazuh fordító, referencia-kiértékelő |

## Gyorsstart

```bash
python -m venv .venv && source .venv/bin/activate
make install        # pip install -e ".[dev,siem]"
make check          # validate + ruff + pytest + Wazuh build  (ugyanaz, mint a CI)
```

| Parancs | Mit csinál |
|---|---|
| `make validate` | Sigma-szabályok ellenőrzése (csak olvas, soha nem ír át fájlt) |
| `make test` | egységtesztek, differenciális tesztek, szabály-esetek, deploy-gate teszt |
| `make wazuh` | Sigma → Wazuh XML a `build/wazuh/` alá + lefedettségi jelentés |
| `make bundle` | a deploy-hoz szánt csomag (`build/wazuh-bundle.tar.gz`) |
| `make siem` | Splunk + Elastic lekérdezések a `build/siem/` alá |

## Hogyan működik a pipeline

```
PR / push ──► ci.yml
               ├─ quality  : dectools-validate · ruff · pytest
               ├─ wazuh    : Sigma → Wazuh XML · ID-regiszter ellenőrzés · jóindulatú-esemény teszt · bundle
               └─ siem     : Splunk + Elastic lekérdezések (artifact)
push main ──► deploy-wazuh.yml : build → (jóváhagyás) → SSH a Wazuh managerre → szintaxis + logtest → élesítés / auto-rollback
push test ──► docs.yml         : wiki, pontszámok, dashboard újragenerálása (csak dokumentáció kerül commitba)
hetente   ──► legacy-siem.yml  : QRadar / NetWitness / Sentinel (best effort, nem blokkoló)
              weekly_report.yaml: heti összefoglaló issue
```

A generált SIEM-lekérdezések (`rules/splunk`, `rules/elastic`, …) **nem** kerülnek a repóba: a CI artifactként
adja őket, így nincs bot-commit-zaj és nincs „conversion_failed” helyőrző fájl.

## Szabály írása / módosítása

1. Új fájl a `rules/sigma/` alatt, a meglévők mintájára (UUID `id`, `tags` ATT&CK technikával, `logsource`).
2. `make validate` – a hibák (`error`) mindig megállítják a buildet; az új figyelmeztetések (`warning`) is,
   a régi tartozás a `.validation-baseline.json`-ban van, és onnan csökkenthető.
3. Viselkedési teszt: `tests/rule_cases/<szabály>.yml` – `match` és `no_match` események Sigma-mezőnevekkel
   (példa: `tests/rule_cases/T1047.yml`). A teszt a Sigma-forráson **és** a lefordított Wazuh-szabályokon is lefut.
4. PR → a CI zöld → merge.

## Ismert minőségi tartozás (a validátor jelzi, nem javítja magától)

* **`duplicate-key` (44 szabály):** ugyanaz a YAML-kulcs kétszer szerepel egy blokkban (pl. két `CommandLine|contains:`).
  A YAML csak az utolsót tartja meg, így a szabály csendben gyengébb, mint amit leírtak. Javítás: külön
  selection-blokkok, és `condition: a and b`.
* **`regex-without-re` (38 szabály):** reguláris kifejezés `|re` módosító nélkül – Sigmában ez szó szerinti egyezés.
* **`filename-tag-mismatch` (4 szabály):** a fájlnév és az `attack.tNNNN` címke nem egyezik.
* **`wazuh/quarantine.yml` (4 szabály):** jóindulatú teszt-eseményre riasztanak, ezért nem kerülnek éles Wazuh-ra,
  amíg ki nem javítják őket.

A régi pipeline `preprocess_sigma.py` lépése a *forrás* szabályokat írta át (`User:` → `username:`,
`ParentImage:` → `Parentprocessname:` …). Ez megszűnt; a már megsérült 303 fájlt a
`tools/maintenance/repair_corrupted_fields.py` állította helyre.

## Könyvtárszerkezet

```
rules/sigma/        Sigma szabályok (forrás)
src/dectools/       validátor, Wazuh fordító, referencia-kiértékelő
tests/              pytest (+ tests/rule_cases/ viselkedési esetek)
wazuh/              ID-regiszter, karantén, jóindulatú események, szerveroldali deploy-script
tools/              dokumentáció- és riportgenerátorok, legacy konverterek
archive/            régi anyagok (legacy-4sigma, legacy-tests) – törölhető, ha már nem kell
```
