# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-02-03 13:58:35*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 409 |
| Aktív (van logforrás) | 408 |
| Inaktív (hiányzó log) | 1 |
| MITRE Lefedettség | 407 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Ultra-Pro High-Fidelity Logical Isolation Bypass (T1599.001) (`T1599_001.yaml`) | service: `Cisco IOS` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

✅ Minden kritikus technika le van fedve legalább egy szabállyal.
