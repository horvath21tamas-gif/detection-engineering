# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-02-03 07:32:48*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 310 |
| Aktív (van logforrás) | 299 |
| Inaktív (hiányzó log) | 11 |
| MITRE Lefedettség | 311 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Ultra-Pro Unauthorized Windows Service Installation (T1543.003) (`T1543_003.yaml`) | service: `process_creation` |
| Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003) (`T1556_003.yaml`) | service: `auditd` |
| Ultra-Pro Unauthorized Cloud Account Creation (T1136.003) (`T1136_003.yaml`) | service: `auditlogs` |
| High-Fidelity Device Registration Persistence (T1098.005) (`T1098_005.yaml`) | service: `process_creation` |
| High-Fidelity Entra ID Application Credential Addition (`T1098_001.yaml`) | service: `ad` |
| High-Fidelity Azure Role Assignment Escalation (`T1098_004.yaml`) | service: `process_access` |
| High-Fidelity MFA Method Addition (`T1098_006.yaml`) | service: `process_creation` |
| Ultra-Pro RC Script and Init.d Persistence (T1037.004) (`T1037_004.yaml`) | service: `auditd` |
| High-Fidelity Entra ID App Certificate Addition (`T1098_003.yaml`) | service: `ad` |
| Ultra-Pro Stealthy Ptrace Injection (T1055.008) (`T1055_008.yaml`) | service: `auditd` |
| Privileged Service Executable Overwritten from User-Writable Location (`T1574_010.yaml`) | category: `file_change` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

✅ Minden kritikus technika le van fedve legalább egy szabállyal.
