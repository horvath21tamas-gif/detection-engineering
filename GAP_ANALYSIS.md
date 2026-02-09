# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-02-09 06:32:05*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 539 |
| Aktív (van logforrás) | 537 |
| Inaktív (hiányzó log) | 2 |
| MITRE Lefedettség | 537 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Ultra-Pro High-Fidelity Cloud Control Plane Hijacking (T1021.007) (`T1021_007.yaml`) | service: `activitylogs` |
| Ultra-Pro High-Fidelity Cloud Groups Discovery (T1069.003) (`T1069_003.yaml`) | service: `azure_ad` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

✅ Minden kritikus technika le van fedve legalább egy szabállyal.
