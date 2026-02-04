# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-02-04 10:00:37*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 490 |
| Aktív (van logforrás) | 490 |
| Inaktív (hiányzó log) | 0 |
| MITRE Lefedettség | 486 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Ultra-Pro High-Fidelity Cloud Groups Discovery (T1069.003) (`T1069_003.yaml`) | service: `azure_ad` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

✅ Minden kritikus technika le van fedve legalább egy szabállyal.
