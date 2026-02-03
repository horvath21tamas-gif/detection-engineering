# 🎯 Detection Strategy & Gap Analysis
*Frissítve: 2026-02-03 11:03:09*

## 📊 Állapotösszegző
| Mutató | Érték |
| :--- | :--- |
| Összes szabály | 364 |
| Aktív (van logforrás) | 346 |
| Inaktív (hiányzó log) | 18 |
| MITRE Lefedettség | 364 technika |

## 🛑 Kritikus Adatforrás Hiányok
Az alábbi szabályok **inaktívak**, mert a SIEM nem küldi a szükséges logokat:

| Szabály | Hiányzó forrás |
| :--- | :--- |
| Ultra-Pro Unauthorized Windows Service Installation (T1543.003) (`T1543_003.yaml`) | service: `process_creation` |
| Ultra-Pro High-Fidelity Cloud Network Security Regression (T1578.005) (`T1578_005.yaml`) | product: `cloud`, service: `Azure Activity` |
| Ultra-Pro High-Fidelity Network OS Image Modification (T1601) (`T1601.yaml`) | product: `network`, service: `FortiOS` |
| Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003) (`T1556_003.yaml`) | service: `auditd` |
| Ultra-Pro Unauthorized Cloud Account Creation (T1136.003) (`T1136_003.yaml`) | service: `auditlogs` |
| High-Fidelity Device Registration Persistence (T1098.005) (`T1098_005.yaml`) | service: `process_creation` |
| High-Fidelity Entra ID Application Credential Addition (`T1098_001.yaml`) | service: `ad` |
| High-Fidelity Azure Role Assignment Escalation (`T1098_004.yaml`) | service: `process_access` |
| High-Fidelity MFA Method Addition (`T1098_006.yaml`) | service: `process_creation` |
| Ultra-Pro High-Fidelity Cloud Image Tampering (T1578.004) (`T1578_004.yaml`) | product: `cloud`, service: `Azure Activity` |
| Ultra-Pro High-Fidelity Cloud Snapshot Exfiltration (T1578.002) (`T1578_002.yaml`) | product: `cloud`, service: `Azure Activity` |
| Ultra-Pro RC Script and Init.d Persistence (T1037.004) (`T1037_004.yaml`) | service: `auditd` |
| Ultra-Pro High-Fidelity Cloud Infrastructure Tampering (T1578) (`T1578.yaml`) | product: `cloud`, service: `Azure Activity` |
| Ultra-Pro High-Fidelity Cloud Instance Destruction (T1578.003) (`T1578_003.yaml`) | product: `cloud`, service: `Azure Activity` |
| High-Fidelity Entra ID App Certificate Addition (`T1098_003.yaml`) | service: `ad` |
| Ultra-Pro Stealthy Ptrace Injection (T1055.008) (`T1055_008.yaml`) | service: `auditd` |
| Ultra-Pro High-Fidelity Cloud Security Infrastructure Impairment (T1562.012) (`T1562_012.yaml`) | product: `cloud`, service: `aws.cloudtrail` |
| Privileged Service Executable Overwritten from User-Writable Location (`T1574_010.yaml`) | category: `file_change` |
| Ultra-Pro High-Fidelity Suspicious Cloud Instance Creation (T1578.001) (`T1578_001.yaml`) | product: `cloud`, service: `Azure Activity` |

## 🛡️ Stratégiai Teendők (Hiányzó Technikák)
A SOC hatékonyság növelése érdekében ezekre a technikákra kellene szabályt írni:

✅ Minden kritikus technika le van fedve legalább egy szabállyal.
