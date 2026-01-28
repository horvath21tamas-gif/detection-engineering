# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-01-28 11:02:36*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 114 |
| Aktív (van logforrás) | 113 |
| Inaktív (hiányzó log) | 1 |
| MITRE Lefedettség | 117 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Anomalous Cloud User Account Creation (`T1585_003.yaml`) | service: `audit` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
