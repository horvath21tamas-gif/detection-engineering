# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-01-27 06:12:10*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 55 |
| Aktív (van logforrás) | 54 |
| Inaktív (hiányzó log) | 1 |
| MITRE Lefedettség | 58 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Network Reconnaissance with High Port Diversity (`T1590.yaml`) | product: `zeek` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
