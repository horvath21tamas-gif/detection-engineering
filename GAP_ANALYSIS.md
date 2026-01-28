# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-01-28 13:04:06*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 117 |
| Aktív (van logforrás) | 115 |
| Inaktív (hiányzó log) | 2 |
| MITRE Lefedettség | 120 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Anomalous Cloud User Account Creation (`T1585_003.yaml`) | service: `audit` |
| Stealthy Email Account Establishment and Manipulation (`T1585_002.yaml`) | product: `m365`, service: `exchange` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
