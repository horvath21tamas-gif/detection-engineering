# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-02-04 12:36:49*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 507 |
| Aktív (van logforrás) | 506 |
| Inaktív (hiányzó log) | 1 |
| MITRE Lefedettség | 505 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Ultra-Pro High-Fidelity Cloud Groups Discovery (T1069.003) (`T1069_003.yaml`) | service: `azure_ad` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

✅ Minden kritikus technika le van fedve legalább egy szabállyal.
