# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-02-03 14:54:34*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 421 |
| Aktív (van logforrás) | 420 |
| Inaktív (hiányzó log) | 1 |
| MITRE Lefedettség | 421 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Ultra-Pro High-Fidelity Logical Isolation Bypass (T1599.001) (`T1599_001.yaml`) | service: `Cisco IOS` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

✅ Minden kritikus technika le van fedve legalább egy szabállyal.
