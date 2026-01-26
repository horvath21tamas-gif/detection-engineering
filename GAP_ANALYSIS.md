# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-01-26 13:49:18*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 46 |
| Aktív (van logforrás) | 44 |
| Inaktív (hiányzó log) | 2 |
| MITRE Lefedettség | 52 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| High-Fidelity External IP Block Scanning Detection (`T1595_001.yaml`) | category: `network_traffic` |
| Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel (`T1204_004.yaml`) | category: `email` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
