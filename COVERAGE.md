# 📘 Részletes MITRE ATT&CK Lefedettség

**Utolsó frissítés:** `2026-02-02 08:17:04`

## 📈 SIEM Platform Lefedettség

| Platform | Konvertált szabályok | Lefedettség |
| :--- | :---: | :---: |
| Sigma (Forrás) | 165 | 100% |
| Splunk (SPL) | 165 | 100.0% |
| Microsoft Sentinel (KQL) | 165 | 100.0% |
| QRadar (AQL) | 95 | 57.6% |
| Elastic (KQL/EQL) | 165 | 100.0% |
| RSA NetWitness | 165 | 100.0% |

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
| T1059 | HIGH | High-Fidelity Scripting Interpreter Contextual Anomaly, Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity), Webshell Upload or Interaction Detected on Web Server (High Fidelity) |
| T1059.001 | HIGH | Suspicious Encoded PowerShell Command Execution |
| T1059.002 | HIGH | High-Fidelity AppleScript (osascript) Abuse Detection |
| T1059.003 | CRITICAL | Advanced Windows Command Shell Contextual Anomaly |
| T1059.004 | CRITICAL | High-Fidelity Unix Shell Abuse and Reverse Shell Detection |
| T1059.005 | CRITICAL | High-Fidelity VBScript Contextual Anomaly Detection |
| T1059.006 | CRITICAL | High-Fidelity Python Interpreter Abuse Detection |
| T1059.007 | CRITICAL | High-Fidelity JScript Interpreter Contextual Anomaly |
| T1059.008 | CRITICAL | High-Fidelity Network Device CLI Manipulation |
| T1059.009 | CRITICAL | High-Fidelity Cloud Shell Exploitation and Data Exfiltration |
| T1068 | HIGH | Suspicious SYSTEM Process Spawned from User Context |
| T1070.001 | HIGH | Security Event Log Cleared Using wevtutil.exe |
| T1078 | HIGH | High-Fidelity Anomalous Logon via Valid Account |
| T1078.001 | CRITICAL | High-Fidelity Default Account Abuse Detection |
| T1078.002 | HIGH | High-Fidelity Domain Account Lateral Movement Anomaly |
| T1078.003 | CRITICAL | High-Fidelity Local Account Remote Access Detection |
| T1078.004 | CRITICAL | High-Fidelity Cloud Account Compromise (Entra ID) |
| T1087 | HIGH | Suspicious Use of net user or net localgroup via cmd.exe |
| T1091 | HIGH | High-Fidelity Process Execution from Removable Media |
| T1098 | HIGH | Suspicious Use of net user or net localgroup via cmd.exe |
| T1105 | HIGH | Suspicious Base64-Encoded PowerShell Command with Network Activity, Suspicious Use of Built-in Windows Tools for File Download and Code Execution |
| T1110.001 | MEDIUM | Multiple Failed Login Attempts for Single User (Possible Password Guessing) |
| T1133 | HIGH | Anomalous External Remote Service Access Context |
| T1189 | CRITICAL | Browser-Originating Shell or System Tool Execution |
| T1190 | MEDIUM | Suspicious Cross-Site Scripting (XSS) Attempt Detected on Web Server |
| T1195 | CRITICAL | High-Fidelity Supply Chain Compromise Detection (Post-Update Anomaly) |
| T1195.001 | CRITICAL | High-Fidelity Dependency Poisoning Detection |
| T1195.002 | CRITICAL | High-Fidelity Compromised Binary Activity (Post-Update) |
| T1195.003 | CRITICAL | High-Fidelity Hardware/Firmware Manipulation Detection |
| T1197 | HIGH | Suspicious File Download via Bitsadmin (High Fidelity) |
| T1199 | HIGH | High-Fidelity Trusted Relationship Abuse Detection |
| T1200 | CRITICAL | Malicious Hardware-Induced Command Execution (HID Injection) |
| T1203 | CRITICAL | High-Fidelity Client-Side Exploitation and Shell Spawning |
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
| T1559.001 | HIGH | High-Fidelity Indirect IPC and COM Execution, Gyanús elnevezett csővezeték-létrehozás, amely utólagos kihasználási eszközökhöz kapcsolódik (High Fidelity) |
| T1559.002 | CRITICAL | High-Fidelity Indirect IPC and COM Execution |
| T1560.001 | HIGH | Adatok gyanús archiválása exfiltráció céljából |
| T1562 | HIGH | Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services |
| T1562.001 | CRITICAL | Ransomware Preparation Activity Detected on Windows Host (High Fidelity), Windows Defender védelem kikapcsolása vagy módosítása PowerShell segítségével, Biztonsági szolgáltatások gyanús leállítása |
| T1562.004 | HIGH | Suspicious Firewall Modification via Netsh.exe |
| T1566 | CRITICAL | High-Fidelity Phishing Payload Execution from Communication Apps |
| T1566.001 | CRITICAL | High-Fidelity Spearphishing Attachment Execution |
| T1566.002 | CRITICAL | High-Fidelity Browser-Originating Payload Execution |
| T1566.003 | CRITICAL | High-Fidelity Process Spawn from Business Communication Service |
| T1566.004 | HIGH | High-Fidelity Detection of Post-Vishing Remote Tool Execution |
| T1583 | HIGH | High-Fidelity Offensive Infrastructure Provisioning - T1583 |
| T1583.001 | HIGH | High-Fidelity VPS Infrastructure Provisioning - T1583.001 |
| T1583.002 | HIGH | High-Fidelity Automated Domain Registration & Acquisition - T1583.002 |
| T1583.003 | HIGH | High-Fidelity Cloud Network (VPC) Provisioning - T1583.003 |
| T1583.004 | HIGH | High-Fidelity Serverless Infrastructure Provisioning - T1583.004 |
| T1583.005 | CRITICAL | High-Fidelity Botnet Infrastructure Acquisition - T1583.005 |
| T1583.006 | HIGH | High-Fidelity Web Service Acquisition and Provisioning - T1583.006 |
| T1583.007 | HIGH | High-Fidelity Serverless Infrastructure Provisioning - T1583.007 |
| T1583.008 | HIGH | High-Fidelity Cloud Account Acquisition and Bootstrap - T1583.008 |
| T1584 | HIGH | High-Fidelity Compromised Infrastructure and Resource Abuse - T1584 |
| T1584.001 | CRITICAL | High-Fidelity Domain Infrastructure Hijacking - T1584.001 |
| T1584.002 | CRITICAL | High-Fidelity DNS Server Configuration Subversion - T1584.002 |
| T1584.003 | CRITICAL | High-Fidelity Cloud Identity Subversion and Persistence - T1584.003 |
| T1584.004 | HIGH | High-Fidelity Serverless Function Subversion - T1584.004 |
| T1584.005 | HIGH | High-Fidelity Botnet Agent Persistence and Control - T1584.005 |
| T1584.006 | HIGH | High-Fidelity Web Service and Cloud Storage Subversion - T1584.006 |
| T1584.007 | HIGH | High-Fidelity VPS Control and Tunneling - T1584.007 |
| T1585 | HIGH | Suspicious User Account Creation via CLI/Scripting |
| T1585.001 | HIGH | Potential Automated Social Media Account Establishment |
| T1585.002 | HIGH | Stealthy Email Account Establishment and Manipulation |
| T1585.003 | HIGH | Anomalous Cloud User Account Creation |
| T1586 | HIGH | High-Fidelity Account Compromise and Identity Manipulation - T1586 |
| T1586.001 | HIGH | High-Fidelity Automated Social Media Manipulation - T1586.001 |
| T1586.002 | HIGH | High-Fidelity Email Forwarding Rule Manipulation - T1586.002 |
| T1586.003 | HIGH | High-Fidelity Cloud Account Takeover and Persistence - T1586.003 |
| T1587 | HIGH | High-Fidelity Offensive Capability Development and Compilation - T1587 |
| T1587.001 | CRITICAL | High-Fidelity Malware Development and Evasion Patterns - T1587.001 |
| T1587.002 | HIGH | High-Fidelity Unauthorized Code Signing Capability Development - T1587.002 |
| T1587.003 | HIGH | High-Fidelity Unauthorized Digital Certificate Development - T1587.003 |
| T1587.004 | CRITICAL | High-Fidelity Exploit Development and Compilation Detection - T1587.004 |
| T1588 | HIGH | Anomalous Procurement of Offensive Capabilities |
| T1588.001 | HIGH | Anomalous Procurement of Malware Capabilities |
| T1588.002 | HIGH | Anomalous Offensive Tool Acquisition via CLI |
| T1588.003 | HIGH | Anomalous Code Signing Certificate Export or Acquisition |
| T1588.004 | HIGH | Strategic Trusted Root Certificate Store Manipulation |
| T1588.005 | HIGH | Anomalous Procurement of Exploit or PoC Code |
| T1588.006 | HIGH | Targeted Harvesting of Vulnerability Research Artifacts |
| T1589 | HIGH | High-Confidence OSINT Identity Enumeration via Public APIs, High-Fidelity Identity Enumeration via Authentication Endpoints, Targeted OSINT Enumeration of Open Websites and Domains, Credential Enumeration via Authentication API (High Confidence) |
| T1589.001 | HIGH | Credential Enumeration via Authentication API (High Confidence) |
| T1589.002 | HIGH | High-Confidence OSINT Identity Enumeration via Public APIs |
| T1589.003 | HIGH | Targeted OSINT Enumeration of Open Websites and Domains |
| T1590 | HIGH | Network Reconnaissance with High Port Diversity |
| T1590.001 | MEDIUM | Professional IP Infrastructure Reconnaissance - T1590.001 |
| T1590.002 | HIGH | Advanced DNS Infrastructure Reconnaissance - T1590.002 |
| T1590.003 | HIGH | Advanced Network Trust Dependencies Reconnaissance - T1590.003 |
| T1590.004 | HIGH | Advanced Certificate Information Reconnaissance - T1590.004 |
| T1590.005 | HIGH | Advanced Cloud Infrastructure Reconnaissance - T1590.005 |
| T1590.006 | HIGH | Advanced Victim Web Page Info Reconnaissance - T1590.006 |
| T1591 | HIGH | Advanced Organizational Infrastructure Enumeration - T1591, Advanced Business Relationship Information Discovery - T1591.002 |
| T1591.001 | HIGH | Advanced Physical Location Infrastructure Enumeration - T1591.001 |
| T1591.002 | HIGH | Advanced Business Relationship Information Discovery - T1591.002 |
| T1591.003 | HIGH | Advanced Knowledge Management Discovery - T1591.003 |
| T1591.004 | HIGH | High-Fidelity Personnel Information Discovery - T1591.004 |
| T1592 | HIGH | High-Confidence Firmware Enumeration Against Network Devices, Advanced Software Enumeration Reconnaissance via Web Endpoints, High-Confidence Hardware Enumeration via Management Interfaces, High-Confidence Client Configuration Fingerprinting (Reconnaissance), High-Fidelity Host Information Reconnaissance Activity |
| T1592.001 | HIGH | High-Confidence Hardware Enumeration via Management Interfaces |
| T1592.002 | HIGH | Advanced Software Enumeration Reconnaissance via Web Endpoints |
| T1592.003 | HIGH | High-Confidence Firmware Enumeration Against Network Devices |
| T1592.004 | MEDIUM | High-Confidence Client Configuration Fingerprinting (Reconnaissance) |
| T1593 | HIGH | High-Fidelity Automated Web Reconnaissance - T1593 |
| T1593.001 | HIGH | High-Fidelity Social Media Entity Harvesting - T1593.001 |
| T1593.002 | HIGH | High-Fidelity Automated Search Engine Reconnaissance - T1593.002 |
| T1593.003 | HIGH | High-Fidelity Social Media Entity Harvesting - T1593.003 |
| T1594 | HIGH | High-Fidelity Information Repository Reconnaissance - T1594 |
| T1595 | HIGH | High-Fidelity Active Scanning Detection (Behavior-Based), High-Fidelity External IP Block Scanning Detection, High-Confidence External Vulnerability Scanning Activity, Active Wordlist Scanning Against Authentication Endpoints |
| T1595.001 | HIGH | High-Fidelity External IP Block Scanning Detection |
| T1595.002 | HIGH | High-Confidence External Vulnerability Scanning Activity |
| T1595.003 | HIGH | Active Wordlist Scanning Against Authentication Endpoints |
| T1596 | HIGH | High-Fidelity Open Technical Database Reconnaissance - T1596 |
| T1596.001 | HIGH | High-Fidelity WHOIS Database Reconnaissance - T1596.001 |
| T1596.002 | HIGH | High-Fidelity Automated Search Engine Dorking - T1596.002 |
| T1596.003 | HIGH | High-Fidelity Passive DNS Reconnaissance - T1597.003 |
| T1596.004 | HIGH | High-Fidelity Digital Certificate Reconnaissance - T1596.004 |
| T1596.005 | HIGH | High-Fidelity IP Infrastructure Reconnaissance - T1596.005 |
| T1597 | HIGH | High-Fidelity Victim-Owned Website Reconnaissance - T1597 |
| T1597.001 | HIGH | High-Fidelity Domain Infrastructure Enumeration - T1597.001 |
| T1597.002 | HIGH | High-Fidelity Secret Hunting in Code Repositories - T1597.002 |
| T1598 | HIGH | Advanced Phishing for Info & Credential Harvesting - T1598 |
| T1598.001 | HIGH | Advanced Spearphishing Link Redirection - T1598.001 |
| T1598.002 | HIGH | Advanced BEC Mail & Financial Data Exfiltration - T1598.002 |
| T1598.003 | HIGH | High-Fidelity MFA/OTP Spoofing & Harvesting - T1598.003 |
| T1598.004 | HIGH | High-Fidelity Spearphishing Attachment Interaction - T1598.004 |
| T1608 | HIGH | Anomalous Infrastructure Staging and Resource Deployment |
| T1608.001 | HIGH | Anomalous Malware Staging to External Infrastructure |
| T1608.002 | HIGH | Anomalous Offensive Tool Staging and External Upload |
| T1608.003 | HIGH | Strategic Digital Certificate Staging in Trusted Root Store |
| T1608.004 | HIGH | Anomalous Web Content Modification for Drive-by Staging |
| T1608.005 | HIGH | Strategic Staging of Malicious Link Targets |
| T1608.006 | HIGH | Anomalous SEO Poisoning and Metadata Staging |
| T1609 | CRITICAL | High-Fidelity Container Interactive Shell Execution |
| T1610 | CRITICAL | High-Fidelity Malicious Container Deployment Detection |
| T1650 | HIGH | High-Fidelity Cloud Account Acquisition and Initialization - T1650 |
| T1651 | CRITICAL | High-Fidelity Cloud Administration Agent Abuse |
| T1659 | HIGH | Professional Content Impersonation and Infrastructure Mirroring |
