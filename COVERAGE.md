# 📘 Részletes MITRE ATT&CK Lefedettség

**Utolsó frissítés:** `2026-02-23 13:55:41`

## 📈 SIEM Platform Lefedettség

| Platform | Konvertált szabályok | Lefedettség |
| :--- | :---: | :---: |
| Sigma (Forrás) | 628 | 100% |
| Splunk (SPL) | 623 | 99.2% |
| Microsoft Sentinel (KQL) | 629 | 100.2% |
| QRadar (AQL) | 627 | 99.8% |
| Elastic (KQL/EQL) | 629 | 100.2% |
| RSA NetWitness | 622 | 99.0% |

## 🎯 Technika alapú bontás
| Technika ID | Szint | Kapcsolódó szabályok |
| :--- | :--- | :--- |
| T1001 | CRITICAL | Ultra-Pro High-Fidelity Steganography & Data Reconstruction (T1001) |
| T1001.001 | HIGH | Ultra-Pro High-Fidelity Junk Data & Command Padding (T1001.001) |
| T1001.002 | CRITICAL | Ultra-Pro High-Fidelity Steganography & Data Reconstruction (T1001.002) |
| T1001.003 | HIGH | Ultra-Pro High-Fidelity Protocol Impersonation (T1001.003) |
| T1003 | HIGH | Suspicious Access to LSASS Process Memory (Credential Dumping Attempt) |
| T1003.001 | HIGH | LSASS Memory Dump & LOLBin Abuse (T1003.007), Ultra-Pro High-Fidelity LSASS Credential Dumping (T1003), Suspicious Access to LSASS Process Memory, Suspicious Access to LSASS Process Memory (Credential Dumping Attempt) |
| T1003.002 | CRITICAL | Ultra-Pro High-Fidelity SAM & SYSTEM Registry Theft (T1003.002) |
| T1003.003 | CRITICAL | Ultra-Pro High-Fidelity NTDS.dit Extraction (T1003.003) |
| T1003.004 | CRITICAL | Ultra-Pro High-Fidelity LSA Secrets & Security Hive Theft (T1003.004) |
| T1003.005 | CRITICAL | Ultra-Pro High-Fidelity MSCASH/DCC Extraction (T1003.005) |
| T1003.006 | CRITICAL | Ultra-Pro High-Fidelity DCSync Attack Detection (T1003.006) |
| T1003.007 | CRITICAL | Ultra-Pro High-Fidelity LSASS Memory Dump & LOLBin Abuse (T1003.007) |
| T1003.008 | CRITICAL | Ultra-Pro High-Fidelity Linux Shadow File Extraction (T1003.008) |
| T1005 | CRITICAL | Ultra-Pro High-Fidelity Local Data Harvesting (T1005) |
| T1006 | CRITICAL | Ultra-Pro Stealthy Direct Volume Access (T1006) |
| T1007 | HIGH | Suspicious Event Log Enumeration from Anomalous Execution Context, Ultra-Pro High-Fidelity System Service Discovery (T1007) |
| T1008 | CRITICAL | Ultra-Pro High-Fidelity Fallback Channel Detection (T1008) |
| T1010 | HIGH | Ultra-Pro High-Fidelity Application Window Discovery (T1010) |
| T1011 | HIGH | Ultra-Pro High-Fidelity Bluetooth Exfiltration (T1011) |
| T1011.001 | CRITICAL | Ultra-Pro High-Fidelity BLE Advertising Exfiltration (T1011.001) |
| T1012 | HIGH | Ultra-Pro High-Fidelity Query Registry Discovery (T1012) |
| T1014 | CRITICAL | Ultra-Pro High-Fidelity BYOVD Rootkit Loading (T1014) |
| T1016 | HIGH | Ultra-Pro High-Fidelity System Network Configuration Discovery (T1016) |
| T1016.001 | HIGH | Ultra-Pro High-Fidelity Internet IP Discovery (T1016.001) |
| T1016.002 | HIGH | Ultra-Pro High-Fidelity Terminal Services Configuration Discovery (T1016.002) |
| T1018 | HIGH | Ultra-Pro High-Fidelity Remote System Discovery (T1018) |
| T1020 | CRITICAL | Ultra-Pro High-Fidelity Automated Exfiltration (T1020) |
| T1020.001 | CRITICAL | Client-Linked Cloud Exfil (T1020.001) |
| T1021 | HIGH | Rapid Logons to Multiple Distant Hosts by Same User, Suspicious Service Creation via Remote Administration Tools Outside Approved Management Scope |
| T1021.001 | MEDIUM | Suspicious RDP Logon from Unusual Source |
| T1021.002 | CRITICAL | SMB Admin Share Mapping (T1021.002), Admin Share Data Exfiltration (T1602.001) |
| T1021.003 | CRITICAL | DCOM Remote Execution (T1021.003) |
| T1021.004 | CRITICAL | SSH Lateral Movement & Tunneling (T1021.004) |
| T1021.005 | CRITICAL | VNC Lateral Movement & Hijacking (T1021.005) |
| T1021.006 | CRITICAL | WinRM Remote Execution (T1021.006) |
| T1021.007 | CRITICAL | Cloud Control Plane Hijacking (T1021.007) |
| T1021.008 | CRITICAL | macOS ARD Remote Hijacking (T1021.008) |
| T1025 | CRITICAL | Removable Media Data Theft (T1025) |
| T1027 | HIGH | Suspicious Base64-Encoded PowerShell Command with Network Activity, Suspicious Encoded PowerShell Command Execution |
| T1027.001 | HIGH | Binary Padding Activity (T1027.001) |
| T1027.002 | HIGH | Software Packing Event (T1027.002) |
| T1027.003 | CRITICAL | Steganography Payload Extraction (T1027.003) |
| T1027.004 | CRITICAL | Steganography Payload Extraction (T1027.004) |
| T1027.005 | CRITICAL | Indicator Removal and Signature Theft (T1027.005) |
| T1027.006 | CRITICAL | HTML Smuggling Execution (T1027.006) |
| T1027.007 | HIGH | Binary Symbol Stripping (T1027.007) |
| T1027.008 | HIGH | Binary Symbol Stripping (T1027.008) |
| T1027.009 | CRITICAL | Embedded Payload Extraction (T1027.009) |
| T1027.010 | HIGH | Command Line Obfuscation (T1027.010) |
| T1027.011 | HIGH | Suspicious Archive Creation (T1027.011) |
| T1027.012 | CRITICAL | Windows LDR Hijacking (T1027.012) |
| T1029 | CRITICAL | Scheduled Transfer (T1029) |
| T1030 | CRITICAL | Data Chunking and Fragmentation (T1030) |
| T1033 | HIGH | System Owner/User Discovery (T1033) |
| T1036 | CRITICAL | Masquerading and Process Path Abuse (T1036), Legitimate Windows Binary Copied to User-Writable Location, Double File Extension Execution (T1036.007) |
| T1036.001 | CRITICAL | Invalid or Forged Code Signature (T1036.001) |
| T1036.002 | CRITICAL | RTLO Character Execution (T1036.002) |
| T1036.003 | CRITICAL | Renamed System Utility Detection (T1036.003) |
| T1036.004 | CRITICAL | Masquerading via Path Anomaly (T1036.004) |
| T1036.005 | HIGH | Legitimate Windows Binary Copied to User-Writable Location |
| T1036.006 | CRITICAL | Space After Filename Masquerading (T1036.006) |
| T1036.007 | CRITICAL | Double File Extension Execution (T1036.007) |
| T1036.008 | CRITICAL | Masquerade via Interpreter Misuse (T1036.008) |
| T1036.009 | CRITICAL | Allure Document & RTLO Masquerading Detection |
| T1037 | CRITICAL | High-Fidelity Logon Script Persistence (T1037) |
| T1037.001 | CRITICAL | High-Fidelity UserInitMprLogonScript Persistence |
| T1037.002 | CRITICAL | High-Fidelity Netsh Helper DLL Persistence |
| T1037.003 | CRITICAL | Ultra-Pro Network Logon Script/Shortcut Modification (T1037.003) |
| T1037.004 | CRITICAL | Ultra-Pro RC Script and Init.d Persistence (T1037.004) |
| T1037.005 | CRITICAL | Ultra-Pro macOS Startup Items Persistence (T1037.005) |
| T1039 | CRITICAL | Network Share Discovery and Collection (ATT&CK T1039) |
| T1040 | HIGH | Network Sniffing Detection (ATT&CK T1040) |
| T1041 | CRITICAL | Exfiltration Over C2 Channel (ATT&CK T1041) |
| T1046 | HIGH | Network Service Discovery (ATT&CK T1046) |
| T1047 | HIGH | Suspicious Remote Process Creation via WMIC |
| T1048 | CRITICAL | Alternative Protocol Exfiltration (ATT&CK T1048) |
| T1048.001 | CRITICAL | Symmetric Encrypted Exfiltration (ATT&CK T1048.001) |
| T1048.002 | CRITICAL | Asymmetric Encrypted Exfiltration (ATT&CK T1048.002) |
| T1048.003 | CRITICAL | Unencrypted Protocol Exfiltration (ATT&CK T1048.003) |
| T1049 | HIGH | Port Knocking or Raw Socket Listener Deployment (T1205.001), Traffic Signaling and Port Knocking Activity (T1205), System Network Connections Discovery (ATT&CK T1049) |
| T1052 | CRITICAL | Physical Medium Exfiltration (ATT&CK T1052) |
| T1052.001 | CRITICAL | USB Exfiltration Detection (ATT&CK T1052.001) |
| T1053 | HIGH | Gyanús ütemezett feladat vagy munkakör létrehozása a Persistence (T1053) miatt |
| T1053.002 | HIGH | High-Fidelity At.exe Activity Detection |
| T1053.003 | HIGH | High-Fidelity Cron Persistence and In-Place Modification |
| T1053.005 | HIGH | Suspicious Scheduled Task Creation Executing PowerShell |
| T1053.006 | HIGH | High-Fidelity Systemd Service Creation or Modification |
| T1053.007 | HIGH | High-Fidelity Systemd Timer Persistence Detection |
| T1055 | CRITICAL | Process Injection Detection (ATT&CK T1055) |
| T1055.001 | CRITICAL | DLL Injection Detection (ATT&CK T1055.001) |
| T1055.002 | CRITICAL | PE Injection Detection (ATT&CK T1055.002) |
| T1055.003 | CRITICAL | Thread Hijacking Detection (ATT&CK T1055.003) |
| T1055.004 | CRITICAL | APC Injection Detection (ATT&CK T1055.004) |
| T1055.005 | CRITICAL | TLS Injection Detection (ATT&CK T1055.005) |
| T1055.008 | CRITICAL | Ptrace Injection Detection (ATT&CK T1055.008) |
| T1055.009 | CRITICAL | Stealthy Module Overwriting (ATT&CK T1055.009) |
| T1055.011 | CRITICAL | Stealthy Extra Window Memory (EWM) Injection (ATT&CK T1055.011) |
| T1055.012 | CRITICAL | Stealthy Process Hollowing (ATT&CK T1055.012) |
| T1055.013 | CRITICAL | Stealthy Process Hollowing (ATT&CK T1055.013) |
| T1055.014 | CRITICAL | Stealthy Process Ghosting (ATT&CK T1055.014) |
| T1055.015 | CRITICAL | Stealthy ListPlanting Injection (ATT&CK T1055.015) |
| T1056 | HIGH | Input Capture Detection (ATT&CK T1056) |
| T1056.001 | HIGH | Input Capture Detection (ATT&CK T1056), Keylogging & Input Hooking (ATT&CK T1056.001) |
| T1056.002 | HIGH | GUI Input Capture (ATT&CK T1056.002) |
| T1056.003 | CRITICAL | Digital Certificate Theft (ATT&CK T1056.003) |
| T1056.004 | HIGH | Suspicious Credential API Hooking via Win32 Libraries |
| T1057 | HIGH | Process Discovery (ATT&CK T1057) |
| T1059 | HIGH | High-Fidelity Scripting Interpreter Contextual Anomaly, Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity), Webshell Upload or Interaction Detection (T1505.003) |
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
| T1069 | HIGH | Permission Groups Discovery (ATT&CK T1069) |
| T1069.001 | HIGH | Local Group Discovery (ATT&CK T1069.001) |
| T1069.002 | HIGH | Domain Group Discovery (ATT&CK T1069.002) |
| T1069.003 | HIGH | Cloud Groups Discovery (ATT&CK T1069.003) |
| T1070 | CRITICAL | Indicator Removal on Host (ATT&CK T1070), Command History Logging Impairment, Indicator Blocking and Telemetry Suppression |
| T1070.001 | HIGH | Indicator Removal on Host (ATT&CK T1070), Security Event Log Cleared Using wevtutil.exe |
| T1070.002 | HIGH | Linux Log Clearing and Journal Sabotage (ATT&CK T1070.002) |
| T1070.003 | HIGH | Mailbox Data Clearing and Rule Manipulation (ATT&CK T1070.003) |
| T1070.004 | HIGH | Indicator Removal on Host (ATT&CK T1070), Forensic Artifact and File Deletion (ATT&CK T1070.004) |
| T1070.005 | HIGH | Network Share and Credential Cleanup (ATT&CK T1070.005) |
| T1070.006 | HIGH | Timestomp and MACE Attribute Manipulation (T1070.006) |
| T1070.007 | HIGH | Network History and RDP Trace Removal (T1070.007) |
| T1070.008 | CRITICAL | Email Storage and Database Destruction (T1070.008) |
| T1070.009 | HIGH | Persistence Artifact Removal (T1070.009) |
| T1071 | CRITICAL | Application Layer C2 Anomaly (T1071) |
| T1071.001 | CRITICAL | Application Layer C2 Anomaly (T1071), HTTP/S C2 Anomaly (T1071.001) |
| T1071.002 | CRITICAL | FTP/SFTP Protocol Anomaly (T1071.002) |
| T1071.003 | CRITICAL | Mail Protocol Anomaly (T1071.003) |
| T1071.004 | CRITICAL | DNS Tunneling & Beaconing (T1071.004) |
| T1072 | CRITICAL | High-Fidelity Software Deployment Tool Abuse Detection |
| T1074 | CRITICAL | Data Staging Anomaly (T1074), Local Data Staging Anomaly (T1074.001) |
| T1074.001 | CRITICAL | Local Data Staging Anomaly (T1074.001) |
| T1074.002 | CRITICAL | Remote Data Staging (T1074.002) |
| T1078 | HIGH | High-Fidelity Anomalous Logon via Valid Account, Suspicious Impersonation via RunAs Abuse or Deceptive Local Account Creation |
| T1078.001 | CRITICAL | High-Fidelity Default Account Abuse Detection |
| T1078.002 | HIGH | High-Fidelity Domain Account Lateral Movement Anomaly |
| T1078.003 | CRITICAL | High-Fidelity Local Account Remote Access Detection |
| T1078.004 | CRITICAL | High-Fidelity Cloud Account Compromise (Entra ID) |
| T1080 | HIGH | Taint Shared Content (T1080) |
| T1082 | HIGH | Suspicious Event Log Enumeration from Anomalous Execution Context, System Information Discovery (T1082) |
| T1083 | HIGH | File and Directory Discovery (T1083) |
| T1087 | HIGH | Suspicious Use of net user or net localgroup via cmd.exe |
| T1087.001 | HIGH | Local Account Discovery (T1087.001) |
| T1087.002 | HIGH | Domain Account Discovery (T1087.002) |
| T1087.003 | HIGH | Email Account Discovery (T1087.003) |
| T1087.004 | HIGH | Cloud Account Discovery (T1087.004) |
| T1090 | CRITICAL | Proxy & Pivot Point Detection (T1090), External Proxy & Tunneling (T1090.002) |
| T1090.001 | CRITICAL | Internal Proxy & Pivot Detection (T1090.001) |
| T1090.002 | CRITICAL | External Proxy & Tunneling (T1090.002) |
| T1090.003 | CRITICAL | Multi-hop Proxy & Tor Detection (T1090.003) |
| T1090.004 | CRITICAL | Domain Fronting Detection (T1090.004) |
| T1091 | HIGH | High-Fidelity Process Execution from Removable Media |
| T1092 | CRITICAL | Removable Media C2 Anomaly (T1071.002 / T1092) |
| T1095 | CRITICAL | Non-Application Layer C2 (T1095) |
| T1098 | CRITICAL | Suspicious Use of net user or net localgroup via cmd.exe, High-Fidelity Account Manipulation - Persistence Focused |
| T1098.001 | CRITICAL | High-Fidelity Entra ID Application Credential Addition |
| T1098.002 | CRITICAL | High-Fidelity Exchange Mailbox Permission Grant (T1098.002) |
| T1098.003 | CRITICAL | High-Fidelity Entra ID App Certificate Addition |
| T1098.004 | CRITICAL | High-Fidelity Azure Role Assignment Escalation |
| T1098.005 | HIGH | High-Fidelity Device Registration Persistence (T1098.005) |
| T1098.006 | CRITICAL | High-Fidelity MFA Method Addition |
| T1102 | CRITICAL | Web Service C2 (T1102) |
| T1102.001 | CRITICAL | Dead Drop Resolver (T1102.001) |
| T1102.002 | CRITICAL | Bidirectional Cloud C2 (T1102.002) |
| T1102.003 | CRITICAL | One-Way Web Service C2 (T1102.003) |
| T1104 | CRITICAL | Multi-Stage C2 (T1104) |
| T1105 | HIGH | Suspicious Base64-Encoded PowerShell Command with Network Activity, Suspicious Use of Built-in Windows Tools for File Download and Code Execution |
| T1106 | CRITICAL | High-Fidelity Native API Abuse via LOLBins |
| T1110 | HIGH | Brute Force & Tooling (T1110) |
| T1110.001 | MEDIUM | Multiple Failed Login Attempts for Single User (Possible Password Guessing) |
| T1110.002 | CRITICAL | Credential Export & Cracking (T1110.002) |
| T1110.003 | HIGH | Password Spraying (T1110.003) |
| T1110.004 | HIGH | Credential Stuffing & Combo-list Abuse (T1110.004) |
| T1111 | CRITICAL | MFA Evasion & Session Hijacking (T1111) |
| T1112 | CRITICAL | Registry Tampering for Evasion (T1112), Windows Event Log Service Impairment, Indicator Blocking and Telemetry Suppression |
| T1113 | CRITICAL | Screen Capture Anomaly (T1113) |
| T1114 | CRITICAL | Email Harvesting Anomaly (T1114) |
| T1114.001 | CRITICAL | Local Email Harvesting Anomaly (T1114.001), Email Harvesting Anomaly (T1114) |
| T1114.002 | CRITICAL | Email Harvesting Anomaly (T1114), Remote Email Export Anomaly (T1114.002) |
| T1114.003 | CRITICAL | Email Forwarding Rule Anomaly (T1114.003) |
| T1115 | CRITICAL | Clipboard Data Spying (T1115) |
| T1119 | CRITICAL | Automated Collection (T1119) |
| T1120 | HIGH | Peripheral Device Discovery (T1120) |
| T1123 | CRITICAL | Audio Capture & Spying (T1123) |
| T1124 | HIGH | System Time Discovery (T1124) |
| T1125 | CRITICAL | Video Capture Anomaly (T1125) |
| T1127 | CRITICAL | Trusted Developer Utility Proxy (T1127), MSBuild Proxy Execution (T1127.001) |
| T1127.001 | CRITICAL | MSBuild Proxy Execution (T1127.001) |
| T1129 | HIGH | High-Fidelity Shared Module Load from Untrusted Path |
| T1132 | CRITICAL | Data Encoding & Obfuscation (T1132) |
| T1132.001 | CRITICAL | Data Encoding & Obfuscation (T1132), Standard Encoding & Payload Injection (T1132.001) |
| T1132.002 | CRITICAL | Non-Standard Encoding & XOR Obfuscation (T1132.002) |
| T1133 | HIGH | Anomalous External Remote Service Access Context |
| T1134 | CRITICAL | Access Token Manipulation & Impersonation (T1134) |
| T1134.001 | CRITICAL | Token Impersonation via LSASS Handle Duplication (T1134.001) |
| T1134.002 | CRITICAL | Create Process with Token (T1134.002) |
| T1134.003 | CRITICAL | Make and Impersonate Token (T1134.003) |
| T1134.004 | CRITICAL | Parent PID Spoofing & Process Tree Violation (T1134.004) |
| T1134.005 | CRITICAL | SID-History Injection & DS Manipulation (T1134.005) |
| T1135 | HIGH | Network Share Discovery (T1135) |
| T1136 | CRITICAL | Ultra-Pro Unauthorized Account Creation (T1136) |
| T1136.001 | CRITICAL | Ultra-Pro Unauthorized Local Account Creation (T1136.001) |
| T1136.002 | CRITICAL | Ultra-Pro Unauthorized Domain Account Creation (T1136.002) |
| T1136.003 | CRITICAL | Ultra-Pro Unauthorized Cloud Account Creation (T1136.003) |
| T1137 | HIGH | Office Application Startup Persistence (T1137) |
| T1137.001 | CRITICAL | Suspicious Modification of Office Global Template (Normal.dotm) |
| T1137.002 | CRITICAL | Office Test DLL Persistence (T1137.002) |
| T1137.003 | HIGH | Outlook Custom Forms Persistence (T1137.003) |
| T1137.004 | CRITICAL | Outlook Home Page Hijacking & Bypass (T1137.004) |
| T1137.005 | CRITICAL | Office Security Policy Tampering (T1137.005) |
| T1137.006 | CRITICAL | Office Add-in Binary Persistence (T1137.006) |
| T1140 | HIGH | Stealthy Deobfuscation/Decoding (T1140) |
| T1176 | CRITICAL | Ultra-Pro Browser Extension Force-Install Persistence (T1176) |
| T1185 | CRITICAL | Browser Session Hijacking (T1185) |
| T1187 | CRITICAL | Forced Authentication (T1187) |
| T1189 | CRITICAL | Browser-Originating Shell or System Tool Execution |
| T1190 | MEDIUM | Suspicious Cross-Site Scripting (XSS) Attempt Detected on Web Server |
| T1195 | CRITICAL | High-Fidelity Supply Chain Compromise Detection (Post-Update Anomaly) |
| T1195.001 | CRITICAL | High-Fidelity Dependency Poisoning Detection |
| T1195.002 | CRITICAL | High-Fidelity Compromised Binary Activity (Post-Update) |
| T1195.003 | CRITICAL | High-Fidelity Hardware/Firmware Manipulation Detection |
| T1197 | HIGH | Suspicious File Download via Bitsadmin (High Fidelity) |
| T1199 | HIGH | High-Fidelity Trusted Relationship Abuse Detection |
| T1200 | CRITICAL | Malicious Hardware-Induced Command Execution (HID Injection) |
| T1201 | HIGH | Password Policy Discovery Detection (T1201) |
| T1202 | HIGH | Indirect Command Execution via Proxy Binaries (T1202) |
| T1203 | CRITICAL | High-Fidelity Client-Side Exploitation and Shell Spawning |
| T1204 | HIGH | Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity) |
| T1204.001 | CRITICAL | High-Fidelity User Execution of Malicious Link (T1204.001) |
| T1204.002 | CRITICAL | High-Fidelity User Execution of Malicious File |
| T1204.003 | CRITICAL | High-Fidelity Execution from Mounted Virtual Disk (T1204.003) |
| T1204.004 | HIGH | Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel |
| T1205 | HIGH | Traffic Signaling and Port Knocking Activity (T1205) |
| T1205.001 | HIGH | Port Knocking or Raw Socket Listener Deployment (T1205.001) |
| T1205.002 | CRITICAL | WFP Callout Registration or Kernel Driver Staging (T1205.002) |
| T1207 | CRITICAL | Rogue DC / DCShadow Detection (T1207) |
| T1210 | CRITICAL | Remote Service RCE / Post-Exploitation Spawn Detection (T1210) |
| T1211 | CRITICAL | Sandbox Breakout / Privilege Escalation Exploitation (T1211) |
| T1212 | CRITICAL | Credential Service Exploitation Detection (T1212) |
| T1213 | CRITICAL | Internal Repository Mass Dump Detection (T1213) |
| T1213.001 | CRITICAL | Confluence Mass Scraping Detection (T1213.001) |
| T1213.002 | CRITICAL | Enterprise SharePoint Mass Data Exfiltration Detection (T1213.002) |
| T1213.003 | CRITICAL | Enterprise Knowledge Base Mass Scraping / Mirroring Detection (T1213.003) |
| T1216 | CRITICAL | Windows System Script Proxy Execution (T1216) |
| T1216.001 | CRITICAL | Pubprn.vbs Script Proxy Execution (T1216.001) |
| T1217 | HIGH | Browser Information Discovery (T1217) |
| T1218 | HIGH | Windows System Binary Proxy Execution, Suspicious Use of Built-in Windows Tools for File Download and Code Execution |
| T1218.001 | CRITICAL | HH.exe CHM/ITS Proxy Execution |
| T1218.002 | CRITICAL | Control.exe CPL/DLL Proxy Execution |
| T1218.003 | CRITICAL | MsiExec Proxy Execution |
| T1218.004 | CRITICAL | InstallUtil .NET Proxy Execution |
| T1218.005 | HIGH | Suspicious Mshta Execution of Remote Script (High Fidelity) |
| T1218.007 | HIGH | Suspicious Msiexec Installation from Remote URL (High Fidelity) |
| T1218.008 | CRITICAL | Odbcconf REGSVR Proxy Execution |
| T1218.009 | CRITICAL | Regsvcs/Regasm .NET Proxy Execution |
| T1218.010 | HIGH | Suspicious Regsvr32 Execution Indicative of LOLBAS Abuse (High Fidelity) |
| T1218.011 | HIGH | Suspicious Rundll32 Execution with Script or Remote Payload (High Fidelity) |
| T1218.012 | CRITICAL | Verclsid Proxy Execution via COM Object Abuse |
| T1218.013 | CRITICAL | Rundll32 Proxy Execution (LOLBAS Abuse) |
| T1218.014 | CRITICAL | Suspicious MMC Proxy Execution via Untrusted MSC or COM Hijack |
| T1219 | HIGH | Suspicious Service Creation via Remote Administration Tools Outside Approved Management Scope |
| T1220 | HIGH | XSL Script Processing (T1220) |
| T1221 | HIGH | Office Template Injection (T1221) |
| T1222 | HIGH | Windows Permissions Modification (T1222) |
| T1222.001 | HIGH | Windows File Permissions Modification (T1222.001), Windows Permissions Modification (T1222) |
| T1222.002 | HIGH | Linux File Permissions Modification (T1222.002) |
| T1480 | HIGH | Execution Guardrails Discovery (T1480) |
| T1480.001 | HIGH | Environmental Keying Discovery (T1480.001) |
| T1482 | HIGH | Domain Trust Discovery (T1482) |
| T1484 | CRITICAL | Domain Policy Manipulation & GPO Abuse (T1484) |
| T1484.001 | CRITICAL | Group Policy Modification & Abuse (T1484.001) |
| T1484.002 | CRITICAL | Domain Trust Tampering & SID Filtering Bypass (T1484.002) |
| T1485 | CRITICAL | Data Destruction (T1485/T1490) |
| T1486 | CRITICAL | Ransomware Preparation Activity Detected on Windows Host (High Fidelity) |
| T1489 | CRITICAL | Service Stop (T1489) |
| T1490 | CRITICAL | Suspicious Deletion of Volume Shadow Copies via VSSAdmin (High Fidelity), Data Destruction (T1485/T1490), Ransomware Preparation Activity Detected on Windows Host (High Fidelity) |
| T1491 | CRITICAL | Defacement (T1491) |
| T1491.001 | CRITICAL | Defacement (T1491), Internal Defacement (T1491.001) |
| T1491.002 | CRITICAL | Defacement (T1491), External Defacement (T1491.002) |
| T1495 | CRITICAL | Firmware Corruption (T1495) |
| T1496 | HIGH | Resource Hijacking (T1496) |
| T1497 | HIGH | Virtualization/Sandbox Evasion (T1497) |
| T1497.001 | HIGH | VM Artifact Discovery (T1497.001), Virtualization/Sandbox Evasion (T1497) |
| T1497.002 | HIGH | User Interaction Evasion (T1497.002) |
| T1497.003 | HIGH | Virtualization/Sandbox Evasion (T1497), Time-based Evasion (T1497.003) |
| T1498 | HIGH | Network DoS (T1498) |
| T1498.001 | HIGH | Network DoS (T1498), Direct Flow Flood (T1498.001) |
| T1498.002 | HIGH | Network DoS (T1498) |
| T1499 | CRITICAL | Endpoint Denial of Service (T1499) |
| T1499.001 | CRITICAL | OS Self-Destruction Detection (T1499.001) |
| T1499.002 | CRITICAL | Service Exhaustion Detection (T1499.002) |
| T1499.003 | CRITICAL | OS Self-Destruction Detection (T1499.003), Endpoint Denial of Service (T1499) |
| T1499.004 | CRITICAL | Endpoint Denial of Service (T1499), Resource Exhaustion Detection (T1499.004) |
| T1505 | CRITICAL | Web Shell Execution Patterns (T1505) |
| T1505.001 | CRITICAL | SQL Server Command Shell Execution (T1505.001) |
| T1505.002 | CRITICAL | IIS Native Module Injection (T1505.002) |
| T1505.003 | HIGH | Webshell Upload or Interaction Detection (T1505.003) |
| T1505.004 | CRITICAL | Mainboard Boot Image & SPI Flash Tampering (T1505.004) |
| T1505.005 | CRITICAL | Terminal Services DLL Hijacking Detection (T1505.005) |
| T1518 | HIGH | Software Discovery Detection (T1518) |
| T1518.001 | HIGH | Security Software Discovery Detection (T1518.001) |
| T1525 | CRITICAL | Exploit-Grade Unauthorized Container Image Execution (Implant Container Image) |
| T1526 | HIGH | Cloud Service Discovery Detection (T1526) |
| T1528 | CRITICAL | Application Token & Session Hijacking Detection (T1528) |
| T1529 | CRITICAL | Unauthorized System Shutdown/Reboot Detection (T1529) |
| T1530 | CRITICAL | Cloud Storage Data Theft Detection (T1530) |
| T1531 | CRITICAL | Account Access Removal Detection (T1531) |
| T1534 | CRITICAL | Internal Spearphishing Detection (T1534) |
| T1535 | CRITICAL | Unused Service Manipulation Detection (T1535) |
| T1537 | CRITICAL | Cloud Account Exfiltration Detection (T1537) |
| T1538 | HIGH | Cloud Service Dashboard Discovery (T1538) |
| T1539 | CRITICAL | Web Browser Session Cookie & Credential Theft Detection (T1539) |
| T1542 | CRITICAL | Pre-OS Boot Manipulation (T1542) |
| T1542.001 | CRITICAL | ROM Kit & UEFI Firmware Tampering (T1542.001) |
| T1542.002 | CRITICAL | Component Firmware Tampering (T1542.002) |
| T1542.003 | CRITICAL | Bootkit Persistence & EFI Tampering (T1542.003) |
| T1542.004 | CRITICAL | Mainboard Boot Image & SPI Flash Tampering (T1542.004) |
| T1542.005 | CRITICAL | DHCP/PXE Boot Hijacking (T1542.005) |
| T1543 | CRITICAL | Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services, Windows Event Log Service Impairment |
| T1543.001 | HIGH | Ultra-Pro macOS Launch Agent Persistence Detection (T1543.001), Suspicious macOS LaunchAgent or LaunchDaemon Plist Modification |
| T1543.002 | CRITICAL | High-Fidelity Systemd Timer Persistence Detection, Ultra-Pro Systemd Service Persistence (T1543.002) |
| T1543.003 | CRITICAL | Ultra-Pro Unauthorized Windows Service Installation (T1543.003) |
| T1543.004 | CRITICAL | Ultra-Pro Unauthorized macOS Launch Daemon (T1543.004) |
| T1546 | CRITICAL | WMI Event Subscription Persistence via WMIC or PowerShell (High Fidelity), Suspicious COM Hijacking for User-Level Persistence (High Fidelity), Ultra-Pro WMI Event Subscription Persistence (T1546.003) |
| T1546.001 | CRITICAL | Ultra-Pro File Association Hijacking (T1546.001) |
| T1546.002 | CRITICAL | Ultra-Pro Screensaver Persistence Detection (T1546.002) |
| T1546.003 | CRITICAL | WMI Event Subscription Persistence via WMIC or PowerShell (High Fidelity), Ultra-Pro WMI Event Subscription Persistence (T1546.003) |
| T1546.004 | CRITICAL | Ultra-Pro AppCert DLL Persistence Detection (T1546.004) |
| T1546.005 | CRITICAL | Ultra-Pro Shell Trap Persistence Detection (T1546.005) |
| T1546.006 | CRITICAL | Ultra-Pro Mach-O LC_LOAD_DYLIB Injection (T1546.006) |
| T1546.007 | CRITICAL | Ultra-Pro Netsh Helper DLL Persistence (T1546.007) |
| T1546.008 | CRITICAL | Ultra-Pro WER SilentProcessExit Persistence (T1546.008) |
| T1546.009 | CRITICAL | Ultra-Pro AppInit_DLLs Persistence Detection (T1546.009) |
| T1546.010 | CRITICAL | Ultra-Pro AppCert DLL Persistence Detection (T1546.010) |
| T1546.011 | CRITICAL | Ultra-Pro Application Shimming Persistence Detection (T1546.011) |
| T1546.012 | CRITICAL | Ultra-Pro IFEO Debugger Hijacking Detection (T1546.012) |
| T1546.013 | HIGH | Ultra-Pro PowerShell Profile Injection Detection (T1546.013) |
| T1546.014 | CRITICAL | Ultra-Pro WMI Event Subscription Persistence (T1546.014) |
| T1546.015 | CRITICAL | Suspicious COM Hijacking for User-Level Persistence (High Fidelity), Suspicious MMC Proxy Execution via Untrusted MSC or COM Hijack |
| T1546.016 | HIGH | Ultra-Pro MSI Installer Custom Action Persistence (T1546.016) |
| T1547 | HIGH | Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása |
| T1547.001 | HIGH | Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása, Suspicious Registry Run Key Modification for User Persistence (High Fidelity) |
| T1547.002 | CRITICAL | High-Fidelity LSA Authentication Package Persistence |
| T1547.003 | CRITICAL | High-Fidelity Time Provider Persistence (T1547.003) |
| T1547.004 | CRITICAL | High-Fidelity Winlogon Helper DLL Persistence (T1547.004) |
| T1547.005 | CRITICAL | High-Fidelity SSP DLL Persistence (T1547.005) |
| T1547.006 | CRITICAL | WFP Callout Registration or Kernel Driver Staging (T1205.002), High-Fidelity Kernel Driver Registration (T1547.006) |
| T1547.007 | HIGH | High-Fidelity Browser Session Persistence (T1547.007) |
| T1547.008 | CRITICAL | High-Fidelity LSASS Driver/Package Persistence (T1547.008) |
| T1547.009 | HIGH | High-Fidelity Shortcut Modification Detection |
| T1547.010 | CRITICAL | High-Fidelity AppCert DLL Persistence (T1547.010) |
| T1547.011 | CRITICAL | High-Fidelity Application Shimming Persistence (T1547.011) |
| T1547.012 | HIGH | High-Fidelity COM Hijacking Persistence (T1547.012) |
| T1547.013 | HIGH | High-Fidelity Email Client Helper Persistence (T1547.013) |
| T1547.014 | CRITICAL | High-Fidelity Active Setup Persistence (T1547.014) |
| T1547.015 | HIGH | High-Fidelity COM Hijacking Persistence (T1547.015) |
| T1548 | CRITICAL | Privilege Escalation via Registry Hijacking (T1548) |
| T1548.001 | HIGH | Setuid/Setgid Bit Manipulation (T1548.001) |
| T1548.002 | HIGH | UAC Bypass via Fodhelper Registry Hijack (High Fidelity) |
| T1548.003 | CRITICAL | Sudoers Manipulation and Sudo Abuse (T1548.003) |
| T1548.004 | CRITICAL | AppleScript Privilege Escalation (T1548.004) |
| T1548.005 | HIGH | SUID Desktop Entry & Shortcut Abuse (T1548.005) |
| T1550 | CRITICAL | Alternate Authentication Material (T1550) |
| T1550.001 | CRITICAL | Application Access Token Abuse (T1550.001) |
| T1550.002 | CRITICAL | Alternate Authentication Material (T1550), Pass-the-Hash Detection (T1550.002) |
| T1550.003 | CRITICAL | Alternate Authentication Material (T1550), Pass-the-Ticket Detection (T1550.003) |
| T1550.004 | CRITICAL | Pass-the-Session Detection (T1550.004) |
| T1552 | HIGH | Credentials In Registry Discovery (T1552.002) |
| T1552.001 | HIGH | Unsecured Credentials Discovery (T1552), Credentials In Files Discovery (T1552.001) |
| T1552.002 | HIGH | Unsecured Credentials Discovery (T1552), Credentials In Registry Discovery (T1552.002) |
| T1552.003 | HIGH | Unsecured Credentials Discovery (T1552), Shell History & Console Discovery (T1552.003) |
| T1552.004 | HIGH | Private Key Discovery (T1552.004) |
| T1552.005 | CRITICAL | Cloud Credential Discovery (T1552.005) |
| T1552.006 | CRITICAL | Credentials in Files Discovery (T1552.006) |
| T1552.007 | HIGH | Container Secret Discovery (T1552.007) |
| T1552.008 | CRITICAL | GPP Password Discovery (T1552.008) |
| T1553 | CRITICAL | Subvert Trust Controls (T1553) |
| T1553.001 | CRITICAL | macOS Gatekeeper and Quarantine Bypass (T1553.001) |
| T1553.002 | CRITICAL | SIP Hijacking and Trust Subversion (T1553.002) |
| T1553.003 | CRITICAL | Windows Catalog Database Subversion (T1553.003) |
| T1553.004 | CRITICAL | Root Certificate Injection (T1553.004), Subvert Trust Controls (T1553) |
| T1553.005 | CRITICAL | Mark-of-the-Web (MotW) Bypass & Zone Subversion Detection (T1553.005), Subvert Trust Controls (T1553) |
| T1553.006 | CRITICAL | Windows Code Integrity & DSE Subversion Detection (T1553.006) |
| T1554 | CRITICAL | Ultra-Pro Client Binary Integrity Compromise (T1554) |
| T1555 | HIGH | Nem böngészős folyamat hozzáférése a böngésző hitelesítőadat-tárolóihoz (High Fidelity) |
| T1555.001 | HIGH | Windows Vault Credential Harvesting Detection (T1555.001) |
| T1555.002 | CRITICAL | Securityd Memory Dumping Detection (T1555.002) |
| T1555.003 | CRITICAL | Browser Credential Harvesting Detection (T1555.003) |
| T1555.004 | HIGH | Windows Credential Manager Harvesting Detection (T1555.004) |
| T1555.005 | CRITICAL | Password Manager Extraction Detection (T1555.005) |
| T1555.006 | CRITICAL | Cloud Secret Harvesting Detection (T1555.006) |
| T1556 | CRITICAL | Exploit-Grade Authentication Process Hijack via Suspicious DLL Registration |
| T1556.001 | CRITICAL | Exploit-Grade Security Support Provider Hijacking (LSA SSP) |
| T1556.002 | CRITICAL | Exploit-Grade Password Filter DLL Hijacking via LSA Notification Packages |
| T1556.003 | CRITICAL | Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003) |
| T1556.004 | CRITICAL | Ultra-Pro Network Device Authentication Hijacking (T1556.004) |
| T1556.005 | CRITICAL | Ultra-Pro SID History Injection Correlation (T1556.005) |
| T1556.006 | CRITICAL | Ultra-Pro Entra ID MFA Method Hijacking (T1556.006) |
| T1556.007 | CRITICAL | Hybrid Identity Sync Manipulation Detection (T1556.007) |
| T1556.008 | CRITICAL | Network-to-Cloud Auth Hijacking Detection (T1556.008) |
| T1557 | HIGH | Adversary-in-the-Middle Detection (T1557) |
| T1557.001 | CRITICAL | LLMNR/NBT-NS Poisoning & SMB Relay Detection (T1557.001) |
| T1557.002 | HIGH | Rogue ARP Poisoning / MITM Detection (T1557.002) |
| T1557.003 | CRITICAL | Rogue DHCP / DHCP Spoofing Detection (T1557.003) |
| T1558 | CRITICAL | Kerberos Attack Detection |
| T1558.001 | CRITICAL | Kerberos Attack Detection, Golden Ticket Forgery & Injection |
| T1558.002 | CRITICAL | Kerberos Attack Detection, Silver Ticket Forgery & Injection |
| T1558.003 | HIGH | Kerberos Attack Detection, Gyanús Kerberos TGS jegykérés (Kerberoasting) |
| T1558.004 | CRITICAL | Kerberos Attack Detection, Ultra-Pro High-Fidelity AS-REP Roasting & LDAP Enumeration |
| T1559 | CRITICAL | High-Fidelity Indirect IPC and COM Execution |
| T1559.001 | HIGH | High-Fidelity Indirect IPC and COM Execution, Gyanús elnevezett csővezeték-létrehozás, amely utólagos kihasználási eszközökhöz kapcsolódik (High Fidelity) |
| T1559.002 | CRITICAL | High-Fidelity Office DDE Contextual Anomaly, High-Fidelity Indirect IPC and COM Execution |
| T1559.003 | HIGH | High-Fidelity Hypervisor API and VM Escape Research |
| T1560 | HIGH | Adatok gyanús archiválása exfiltráció céljából |
| T1560.001 | CRITICAL | Adatok gyanús archiválása exfiltráció céljából, Data Archiving for Exfiltration |
| T1560.002 | CRITICAL | Data Archiving via Library |
| T1560.003 | CRITICAL | Archive via Custom Method |
| T1561 | CRITICAL | Disk Structure Wipe, Disk Content Wipe, Disk Wipe |
| T1561.001 | CRITICAL | Disk Content Wipe, Disk Wipe |
| T1561.002 | CRITICAL | Disk Structure Wipe, Disk Wipe |
| T1562 | HIGH | Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services |
| T1562.001 | CRITICAL | WFP Callout Registration or Kernel Driver Staging (T1205.002), Port Knocking or Raw Socket Listener Deployment (T1205.001), Traffic Signaling and Port Knocking Activity (T1205), Ransomware Preparation Activity Detected on Windows Host (High Fidelity), Windows Defender védelem kikapcsolása vagy módosítása PowerShell segítségével, Biztonsági szolgáltatások gyanús leállítása |
| T1562.002 | CRITICAL | Windows Event Log Service Impairment |
| T1562.003 | HIGH | Command History Logging Impairment |
| T1562.004 | HIGH | Suspicious Firewall Modification via Netsh.exe |
| T1562.006 | CRITICAL | Indicator Blocking and Telemetry Suppression |
| T1562.007 | CRITICAL | Cloud Firewall Impairment (T1562.007) |
| T1562.008 | CRITICAL | Cloud Logging Impairment (T1562.008) |
| T1562.009 | CRITICAL | Safe Mode Defense Evasion (T1562.009) |
| T1562.010 | CRITICAL | Defense Downgrade Attack (T1562.010) |
| T1562.012 | CRITICAL | Cloud Security Infrastructure Impairment (T1562.012) |
| T1563 | CRITICAL | Remote Service Session Hijacking (T1563) |
| T1563.001 | CRITICAL | Remote Service Session Hijacking (T1563), Local Session Hijacking (T1563.001) |
| T1563.002 | CRITICAL | Remote Service Session Hijacking (T1563), RDP Session Hijacking (T1563.002) |
| T1564 | HIGH | Hide Artifacts Detection (T1564) |
| T1564.001 | HIGH | Hidden File Attribute Manipulation (T1564.001), Hide Artifacts Detection (T1564) |
| T1564.002 | CRITICAL | Hide Artifacts Detection (T1564), Hidden User Account Creation (T1564.002) |
| T1564.003 | HIGH | Hidden Window Execution (T1564.003) |
| T1564.004 | HIGH | Hide Artifacts Detection (T1564), NTFS Alternative Data Stream (ADS) Abuse (T1564.004) |
| T1564.005 | HIGH | Hidden File System Manipulation (T1564.005) |
| T1564.006 | HIGH | Virtual Instance Execution Abuse (T1564.006) |
| T1564.007 | HIGH | VBA Macro Security Evasion (T1564.007) |
| T1564.008 | CRITICAL | Email Hiding Rules Detection (T1564.008) |
| T1564.009 | HIGH | Resource Extraction and Abuse (T1564.009) |
| T1564.010 | HIGH | Process Argument Spoofing Detection (T1564.010) |
| T1564.011 | HIGH | Virtual Instance Abuse (T1564.011), Virtualization and Sandbox Evasion (T1564.011) |
| T1565 | CRITICAL | Data Manipulation (T1565) |
| T1565.001 | CRITICAL | Stored Data Manipulation (T1565.001), Data Manipulation (T1565) |
| T1565.002 | CRITICAL | Transmitted Data Manipulation (T1565.002), Data Manipulation (T1565) |
| T1565.003 | CRITICAL | Runtime Process Manipulation (T1565.003) |
| T1566 | CRITICAL | High-Fidelity Phishing Payload Execution from Communication Apps |
| T1566.001 | CRITICAL | High-Fidelity Spearphishing Attachment Execution |
| T1566.002 | CRITICAL | High-Fidelity Browser-Originating Payload Execution |
| T1566.003 | CRITICAL | High-Fidelity Process Spawn from Business Communication Service |
| T1566.004 | HIGH | High-Fidelity Detection of Post-Vishing Remote Tool Execution |
| T1567 | CRITICAL | Enterprise Knowledge Base Mass Scraping / Mirroring Detection (T1213.003), Web Service Exfiltration (T1567) |
| T1567.001 | CRITICAL | Code Repository Exfil (T1567.001) |
| T1567.002 | CRITICAL | Cloud Storage Exfil (T1567.002) |
| T1567.003 | CRITICAL | Video Hosting Exfil (T1567.003) |
| T1567.004 | CRITICAL | Text Storage Exfil (T1567.004) |
| T1568 | HIGH | Dynamic Resolution & DGA (T1568) |
| T1568.001 | CRITICAL | Fast Flux & DNS Cache Evasion (T1568.001) |
| T1568.002 | CRITICAL | Dynamic Resolution & DGA (T1568), Domain Generation Algorithm (DGA) Detection (T1568.002) |
| T1568.003 | CRITICAL | DNS Calculation & Extraction (T1568.003) |
| T1569 | HIGH | High-Fidelity System Service Execution Detection |
| T1569.001 | CRITICAL | High-Fidelity Launch Daemon Persistence Detection |
| T1569.002 | HIGH | High-Fidelity System Service Execution Detection, High-Fidelity System Service Execution Detection (T1569.002) |
| T1570 | HIGH | Lateral Tool Transfer (T1570) |
| T1571 | CRITICAL | Non-Standard Port C2 (T1571) |
| T1572 | CRITICAL | Protocol Tunneling Detection (T1572) |
| T1573 | CRITICAL | Encrypted C2 Channel (T1573) |
| T1573.001 | CRITICAL | Encrypted C2 Channel (T1573), Symmetric Encryption C2 Channel (T1573.001) |
| T1573.002 | CRITICAL | Asymmetric Encryption C2 (T1573.002), Encrypted C2 Channel (T1573) |
| T1574 | CRITICAL | Ultra-Pro DLL Hijacking & Side-Loading Detection (T1574) |
| T1574.001 | CRITICAL | Ultra-Pro DLL Hijacking & Side-Loading Detection (T1574), Ultra-Pro DLL Search Order Hijacking Detection (T1574.001) |
| T1574.002 | CRITICAL | Ultra-Pro DLL Side-Loading Integrity Gap Detection (T1574.002), Ultra-Pro DLL Hijacking & Side-Loading Detection (T1574) |
| T1574.003 | HIGH | Ultra-Pro Shell Configuration & Path Interception (T1574.003) |
| T1574.004 | CRITICAL | Ultra-Pro Library Search Order Hijacking & Integrity Gap (T1574.004) |
| T1574.005 | CRITICAL | Ultra-Pro Installer File Permissions Weakness (T1574.005) |
| T1574.006 | CRITICAL | Dynamic Linker Hijacking Against Privileged Binary |
| T1574.007 | CRITICAL | PATH Hijacking Leading to Privileged Binary Execution |
| T1574.008 | CRITICAL | .NET Assembly Search Order Hijacking via User-Writable Directory |
| T1574.009 | CRITICAL | .NET AppDomainManager Hijacking via Non-GAC Assembly |
| T1574.010 | CRITICAL | Privileged Service Executable Overwritten from User-Writable Location |
| T1574.011 | CRITICAL | Privileged Service ImagePath or ServiceDll Hijacked via Registry |
| T1574.012 | CRITICAL | Exploit-Grade COR_PROFILER Hijacking via User-Writable Profiler DLL |
| T1574.013 | CRITICAL | Exploit-Grade KernelCallbackTable Manipulation |
| T1578 | CRITICAL | Cloud Snapshot Exfiltration (T1578.002), Cloud Infrastructure Tampering (T1578) |
| T1578.001 | CRITICAL | Suspicious Cloud Instance Creation (T1578.001) |
| T1578.002 | CRITICAL | Cloud Snapshot Exfiltration (T1578.002) |
| T1578.003 | CRITICAL | Cloud Instance Destruction (T1578.003) |
| T1578.004 | CRITICAL | Cloud Image Tampering (T1578.004) |
| T1578.005 | CRITICAL | Cloud Network Security Regression (T1578.005) |
| T1580 | HIGH | Cloud Infrastructure Discovery (T1580) |
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
| T1599 | CRITICAL | Logical Isolation Bypass (T1599.001), Network Boundary Bridging (T1599) |
| T1599.001 | CRITICAL | Logical Isolation Bypass (T1599.001) |
| T1600 | HIGH | Weaken Encryption Attempt (T1600) |
| T1600.001 | CRITICAL | System Image Patching (T1600.001) |
| T1600.002 | HIGH | Disable Entity Verification (T1600.002) |
| T1601 | CRITICAL | Network OS Image Modification (T1601) |
| T1601.001 | CRITICAL | Network Binary Patching (T1601.001) |
| T1601.002 | CRITICAL | Ultra-Pro High-Fidelity Malicious Network OS Upgrade (T1601.002) |
| T1602 | CRITICAL | Network Share Automated Collection (T1602) |
| T1602.001 | CRITICAL | Admin Share Data Exfiltration (T1602.001) |
| T1602.002 | CRITICAL | Ultra-Pro High-Fidelity Cloud Share Exfiltration (T1602.002) |
| T1606 | CRITICAL | Ultra-Pro High-Fidelity Web Token & Credential Forgery (T1606) |
| T1606.001 | CRITICAL | Ultra-Pro High-Fidelity Web Cookie & Browser Credential Harvesting (T1606.001), Ultra-Pro High-Fidelity Web Token & Credential Forgery (T1606) |
| T1606.002 | CRITICAL | Ultra-Pro High-Fidelity Web Token Forgery & Golden SAML (T1606.002), Ultra-Pro High-Fidelity Web Token & Credential Forgery (T1606) |
| T1608 | HIGH | Anomalous Infrastructure Staging and Resource Deployment |
| T1608.001 | HIGH | Anomalous Malware Staging to External Infrastructure |
| T1608.002 | HIGH | Anomalous Offensive Tool Staging and External Upload |
| T1608.003 | HIGH | Strategic Digital Certificate Staging in Trusted Root Store |
| T1608.004 | HIGH | Anomalous Web Content Modification for Drive-by Staging |
| T1608.005 | HIGH | Strategic Staging of Malicious Link Targets |
| T1608.006 | HIGH | Anomalous SEO Poisoning and Metadata Staging |
| T1609 | CRITICAL | High-Fidelity Container Interactive Shell Execution |
| T1610 | CRITICAL | High-Fidelity Malicious Container Deployment Detection |
| T1611 | CRITICAL | Ultra-Pro Container Escape & Host Access (T1611) |
| T1612 | CRITICAL | Ultra-Pro Stealthy Local Image Build (T1612) |
| T1613 | HIGH | Ultra-Pro High-Fidelity Container and Kubernetes Discovery |
| T1614 | HIGH | High-Fidelity System Location and Regional Kill-Switch Discovery |
| T1614.001 | HIGH | High-Fidelity System Language and Keyboard Layout Discovery |
| T1615 | HIGH | High-Fidelity Group Policy Discovery Detection |
| T1619 | HIGH | High-Fidelity Cloud Storage Object Discovery Detection |
| T1620 | CRITICAL | High-Fidelity Reflective Code Loading and In-Memory Assembly Execution |
| T1621 | HIGH | Suspicious MFA Prompt Bombing or Authentication Flood Automation |
| T1622 | HIGH | Suspicious Anti-Debug API Access From Unbacked or User-Space Memory |
| T1647 | HIGH | Suspicious macOS LaunchAgent or LaunchDaemon Plist Modification |
| T1648 | HIGH | High-Fidelity Serverless Function Persistence or Abuse |
| T1649 | CRITICAL | Suspicious Certificate and Private Key Export or Theft Activity |
| T1650 | HIGH | High-Fidelity Cloud Account Acquisition and Initialization - T1650 |
| T1651 | CRITICAL | High-Fidelity Cloud Administration Agent Abuse |
| T1652 | HIGH | Suspicious Device Driver Enumeration From Anomalous Context (BYOVD Recon) |
| T1653 | MEDIUM | Ultra-Pro Power Settings Manipulation (T1137.001) |
| T1654 | HIGH | Suspicious Event Log Enumeration from Anomalous Execution Context |
| T1656 | HIGH | Suspicious Impersonation via RunAs Abuse or Deceptive Local Account Creation |
| T1657 | HIGH | Suspicious Clipboard Manipulation and Financial Document Access From Untrusted Parent Process |
| T1659 | HIGH | Professional Content Impersonation and Infrastructure Mirroring |
