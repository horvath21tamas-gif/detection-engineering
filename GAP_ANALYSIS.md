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
| High-Fidelity Entra ID Application Credential Addition (`T1098_001.yaml`) | service: `ad` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

- [ ] **T1547** - Boot or Logon Autostart Execution ([Link](https://attack.mitre.org/techniques/T1547))
