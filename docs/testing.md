# Tesztelés

| Réteg | Hol | Mit bizonyít |
|---|---|---|
| Validátor | `tests/test_validate.py` | érvénytelen/duplikált szabályok, a validátor soha nem ír fájlt |
| Szabály-esetek | `tests/rule_cases/*.yml` | adott esemény kiváltja / nem váltja ki a szabályt (Sigma + Wazuh) |
| Fordító | `tests/wazuh/test_convert.py`, `test_registry_emit.py` | De Morgan, regex-escape, ID-stabilitás, XML |
| Differenciális | `tests/wazuh/test_equivalence.py` | a fordított szabályok = a Sigma-szemantika, véletlen eseményeken |
| Tanúesemények | `tests/wazuh/test_witness_cli.py` | minden szabály bizonyíthatóan kiváltható, mutáció nem váltja ki |
| Deploy-kapu | `tests/wazuh/test_gate.py` | telepítés, szintaktikai/logtest hiba → rollback, manipulált csomag elutasítása |

Új viselkedési teszt: másold a `tests/rule_cases/T1047.yml`-t, nevezd át, és írd át az eseményeket
(Sigma-mezőnevekkel: `Image`, `CommandLine`, `User`, …).

A régi `archive/legacy-tests/` szimulációs tesztjei megszűntek: saját, módosító-ignoráló illesztőt használtak, és a 111
mintalogból csak 37 váltotta ki a saját szabályát; a CI ráadásul `|| echo`-val lenyelte a hibákat.
