# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-01-27 13:20:03*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 97 |
| Aktív (van logforrás) | 97 |
| Inaktív (hiányzó log) | 0 |
| MITRE Lefedettség | 100 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

✅ Minden szabályhoz rendelkezésre áll a megfelelő adatforrás a SIEM-ben.

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
