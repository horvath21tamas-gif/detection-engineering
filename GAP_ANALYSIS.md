# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-02-02 08:58:13*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 184 |
| Aktív (van logforrás) | 182 |
| Inaktív (hiányzó log) | 2 |
| MITRE Lefedettség | 184 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| High-Fidelity Device Registration Persistence (T1098.005) (`T1098_005.yaml`) | service: `process_creation` |
| High-Fidelity Entra ID Application Credential Addition (`T1098_001.yaml`) | service: `ad` |
| High-Fidelity Azure Role Assignment Escalation (`T1098_004.yaml`) | service: `process_access` |
| High-Fidelity Entra ID App Certificate Addition (`T1098_003.yaml`) | service: `ad` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
