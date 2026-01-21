# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-01-21 13:53:48*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 39 |
| Aktív (van logforrás) | 36 |
| Inaktív (hiányzó log) | 3 |
| MITRE Lefedettség | 30 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| egy nem admin felhasznalo rovid idon belul tobb kulonbozo, erzekeny windows szolgaltatsat proball leallitani vagy modositani (`T1543.yaml`) | category: `system` |
| Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastol tavol levo hostra jelentkezik be (`T1021.yaml`) | category: `security` |
| Gyanus RDP belepes (`T1021_001.yaml`) | category: `security` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1003** - Credential Dumping ([Link](https://attack.mitre.org/techniques/T1003))
- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
