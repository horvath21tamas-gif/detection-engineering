# 📘 Részletes MITRE ATT&CK Lefedettség

**Utolsó frissítés:** `2026-01-26 13:49:19`

## 📈 SIEM Platform Lefedettség

| Platform | Konvertált szabályok | Lefedettség |
| :--- | :---: | :---: |
| Sigma (Forrás) | 46 | 100% |
| Splunk (SPL) | 46 | 100.0% |
| Microsoft Sentinel (KQL) | 46 | 100.0% |
| QRadar (AQL) | 46 | 100.0% |
| Elastic (KQL/EQL) | 46 | 100.0% |
| RSA NetWitness | 46 | 100.0% |

## 🎯 Technika alapú bontás
| Technika ID | Szint | Kapcsolódó szabályok |
| :--- | :--- | :--- |
| T1003 | HIGH | Credential Dumping LSASS |
| T1003.001 | HIGH | Suspicious Access to LSASS Process Memory, Credential Dumping LSASS |
| T1021 | MEDIUM | Rapid Logons to Multiple Distant Hosts by Same User |
| T1021.001 | MEDIUM | Suspicious RDP Logon from Unusual Source |
| T1027 | HIGH | Suspicious Base64-Encoded PowerShell Command with Network Activity, Suspicious Encoded PowerShell Command Execution |
| T1036 | HIGH | Legitimate Windows Binary Copied to User-Writable Location |
| T1036.005 | HIGH | Legitimate Windows Binary Copied to User-Writable Location |
| T1047 | HIGH | Suspicious Remote Process Creation via WMIC |
| T1053 | HIGH | Gyanús ütemezett feladat vagy munkakör létrehozása a Persistence (T1053) miatt |
| T1053.005 | HIGH | Suspicious Scheduled Task Creation Executing PowerShell |
| T1056.004 | HIGH | Suspicious Credential API Hooking via Win32 Libraries |
| T1059 | HIGH | Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity), Webshell Upload or Interaction Detected on Web Server (High Fidelity) |
| T1059.001 | HIGH | Suspicious Encoded PowerShell Command Execution |
| T1068 | HIGH | Suspicious SYSTEM Process Spawned from User Context |
| T1070.001 | HIGH | Security Event Log Cleared Using wevtutil.exe |
| T1087 | HIGH | Suspicious Use of net user or net localgroup via cmd.exe |
| T1098 | HIGH | Suspicious Use of net user or net localgroup via cmd.exe |
| T1105 | HIGH | Suspicious Base64-Encoded PowerShell Command with Network Activity, Suspicious Use of Built-in Windows Tools for File Download and Code Execution |
| T1110.001 | MEDIUM | Multiple Failed Login Attempts for Single User (Possible Password Guessing) |
| T1190 | MEDIUM | Suspicious Cross-Site Scripting (XSS) Attempt Detected on Web Server |
| T1197 | HIGH | Suspicious File Download via Bitsadmin (High Fidelity) |
| T1204 | HIGH | Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity) |
| T1204.004 | HIGH | Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel |
| T1218 | HIGH | Suspicious Use of Built-in Windows Tools for File Download and Code Execution |
| T1218.005 | HIGH | Suspicious Mshta Execution of Remote Script (High Fidelity) |
| T1218.007 | HIGH | Suspicious Msiexec Installation from Remote URL (High Fidelity) |
| T1218.010 | HIGH | Suspicious Regsvr32 Execution Indicative of LOLBAS Abuse (High Fidelity) |
| T1218.011 | HIGH | Suspicious Rundll32 Execution with Script or Remote Payload (High Fidelity) |
| T1219 | HIGH | Suspicious Use of Legitimate Remote Administration Tools Outside Enterprise Pattern |
| T1486 | CRITICAL | Ransomware Preparation Activity Detected on Windows Host (High Fidelity) |
| T1490 | CRITICAL | Suspicious Deletion of Volume Shadow Copies via VSSAdmin (High Fidelity), Ransomware Preparation Activity Detected on Windows Host (High Fidelity) |
| T1505.003 | HIGH | Webshell Upload or Interaction Detected on Web Server (High Fidelity) |
| T1543 | HIGH | Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services |
| T1546 | HIGH | WMI Event Subscription Persistence via WMIC or PowerShell (High Fidelity), Suspicious COM Hijacking for User-Level Persistence (High Fidelity) |
| T1546.003 | HIGH | WMI Event Subscription Persistence via WMIC or PowerShell (High Fidelity) |
| T1546.015 | HIGH | Suspicious COM Hijacking for User-Level Persistence (High Fidelity) |
| T1547.001 | HIGH | Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása, Suspicious Registry Run Key Modification for User Persistence (High Fidelity) |
| T1548.002 | HIGH | UAC Bypass via Fodhelper Registry Hijack (High Fidelity) |
| T1555 | HIGH | Nem böngészős folyamat hozzáférése a böngésző hitelesítőadat-tárolóihoz (High Fidelity) |
| T1558.003 | HIGH | Gyanús Kerberos TGS jegykérés (Kerberoasting) |
| T1559.001 | HIGH | Gyanús elnevezett csővezeték-létrehozás, amely utólagos kihasználási eszközökhöz kapcsolódik (High Fidelity) |
| T1560.001 | HIGH | Adatok gyanús archiválása exfiltráció céljából |
| T1562 | HIGH | Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services |
| T1562.001 | CRITICAL | Ransomware Preparation Activity Detected on Windows Host (High Fidelity), Windows Defender védelem kikapcsolása vagy módosítása PowerShell segítségével, Biztonsági szolgáltatások gyanús leállítása |
| T1562.004 | HIGH | Suspicious Firewall Modification via Netsh.exe |
| T1592 | HIGH | High-Confidence Firmware Enumeration Against Network Devices, High-Confidence Client Configuration Fingerprinting (Reconnaissance) |
| T1592.003 | HIGH | High-Confidence Firmware Enumeration Against Network Devices |
| T1592.004 | MEDIUM | High-Confidence Client Configuration Fingerprinting (Reconnaissance) |
| T1595 | HIGH | High-Fidelity External IP Block Scanning Detection, High-Confidence External Vulnerability Scanning Activity, Active Wordlist Scanning Against Authentication Endpoints |
| T1595.001 | HIGH | High-Fidelity External IP Block Scanning Detection |
| T1595.002 | HIGH | High-Confidence External Vulnerability Scanning Activity |
| T1595.003 | HIGH | Active Wordlist Scanning Against Authentication Endpoints |
