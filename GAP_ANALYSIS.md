# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-02-03 13:11:39*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 396 |
| Aktív (van logforrás) | 395 |
| Inaktív (hiányzó log) | 1 |
| MITRE Lefedettség | 394 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Ultra-Pro High-Fidelity Logical Isolation Bypass (T1599.001) (`T1599_001.yaml`) | service: `Cisco IOS` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

✅ Minden kritikus technika le van fedve legalább egy szabállyal.
