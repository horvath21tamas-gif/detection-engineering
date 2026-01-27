# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-01-27 06:25:49*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 55 |
| Aktív (van logforrás) | 55 |
| Inaktív (hiányzó log) | 0 |
| MITRE Lefedettség | 59 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

✅ Minden szabályhoz rendelkezésre áll a megfelelő adatforrás a SIEM-ben.

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
