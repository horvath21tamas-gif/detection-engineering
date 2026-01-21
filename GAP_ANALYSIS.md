# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-01-21 07:22:52*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 38 |
| Aktív (van logforrás) | 34 |
| Inaktív (hiányzó log) | 4 |
| MITRE Lefedettség | 31 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| egy nem admin felhasznalo rovid idon belul tobb kulonbozo, erzekeny windows szolgaltatsat proball leallitani vagy modositani (`T1543.yaml`) | category: `system` |
| Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastol tavol levo hostra jelentkezik be (`T1021.yaml`) | category: `security` |
| Gyanus RDP belepes (`T1021_001.yaml`) | category: `security` |
| Szokatlan mennyisegu szolgaltatas jegy kerese (`T1558_003.yaml`) | category: `security` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1053** - Scheduled Task/Job ([Link](https://attack.mitre.org/techniques/T1053))
- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
