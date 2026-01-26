# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-01-26 12:09:31*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 41 |
| Aktív (van logforrás) | 40 |
| Inaktív (hiányzó log) | 1 |
| MITRE Lefedettség | 45 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel (`T1204_004.yaml`) | category: `email` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
