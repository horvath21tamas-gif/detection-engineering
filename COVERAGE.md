# 📘 Részletes MITRE ATT&CK Lefedettség

**Utolsó frissítés:** `2026-02-04 08:52:36`

## 📈 SIEM Platform Lefedettség

| Platform | Konvertált szabályok | Lefedettség |
| :--- | :---: | :---: |
| Sigma (Forrás) | 472 | 100% |
| Splunk (SPL) | 467 | 98.9% |
| Microsoft Sentinel (KQL) | 469 | 99.4% |
| QRadar (AQL) | 209 | 44.3% |
| Elastic (KQL/EQL) | 469 | 99.4% |
| RSA NetWitness | 466 | 98.7% |

## 🎯 Technika alapú bontás
| Technika ID | Szint | Kapcsolódó szabályok |
| :--- | :--- | :--- |
| T1003 | HIGH | Credential Dumping LSASS |
| T1003.001 | HIGH | Ultra-Pro High-Fidelity LSASS Memory Dump & LOLBin Abuse (T1003.007), Ultra-Pro High-Fidelity LSASS Credential Dumping (T1003), Suspicious Access to LSASS Process Memory, Credential Dumping LSASS |
| T1003.002 | CRITICAL | Ultra-Pro High-Fidelity SAM & SYSTEM Registry Theft (T1003.002) |
| T1003.003 | CRITICAL | Ultra-Pro High-Fidelity NTDS.dit Extraction (T1003.003) |
| T1003.004 | CRITICAL | Ultra-Pro High-Fidelity LSA Secrets & Security Hive Theft (T1003.004) |
| T1003.005 | CRITICAL | Ultra-Pro High-Fidelity MSCASH/DCC Extraction (T1003.005) |
| T1003.006 | CRITICAL | Ultra-Pro High-Fidelity DCSync Attack Detection (T1003.006) |
| T1003.007 | CRITICAL | Ultra-Pro High-Fidelity LSASS Memory Dump & LOLBin Abuse (T1003.007) |
| T1003.008 | CRITICAL | Ultra-Pro High-Fidelity Linux Shadow File Extraction (T1003.008) |
| T1006 | CRITICAL | Ultra-Pro Stealthy Direct Volume Access (T1006) |
| T1010 | HIGH | Ultra-Pro High-Fidelity Application Window Discovery (T1010) |
| T1014 | CRITICAL | Ultra-Pro High-Fidelity BYOVD Rootkit Loading (T1014) |
| T1021 | MEDIUM | Rapid Logons to Multiple Distant Hosts by Same User |
| T1021.001 | MEDIUM | Suspicious RDP Logon from Unusual Source |
| T1027 | HIGH | Suspicious Base64-Encoded PowerShell Command with Network Activity, Suspicious Encoded PowerShell Command Execution |
| T1027.001 | HIGH | Ultra-Pro High-Fidelity Binary Padding Activity (T1027.001) |
| T1027.002 | HIGH | Ultra-Pro High-Fidelity Software Packing Event (T1027.002) |
| T1027.003 | CRITICAL | Ultra-Pro High-Fidelity Steganography Payload Extraction (T1027.003) |
| T1027.004 | CRITICAL | Ultra-Pro High-Fidelity Steganography Payload Extraction (T1027.004) |
| T1027.005 | CRITICAL | Ultra-Pro High-Fidelity Indicator Removal and Signature Theft (T1027.005) |
| T1027.006 | CRITICAL | Ultra-Pro High-Fidelity HTML Smuggling Execution (T1027.006) |
| T1027.007 | HIGH | Ultra-Pro High-Fidelity Binary Symbol Stripping (T1027.007) |
| T1027.008 | HIGH | Ultra-Pro High-Fidelity Binary Symbol Stripping (T1027.008) |
| T1027.009 | CRITICAL | Ultra-Pro High-Fidelity Embedded Payload Extraction (T1027.009) |
| T1027.010 | HIGH | Ultra-Pro High-Fidelity Command Line Obfuscation (T1027.010) |
| T1027.011 | HIGH | Ultra-Pro High-Fidelity Suspicious Archive Creation (T1027.011) |
| T1027.012 | CRITICAL | Ultra-Pro High-Fidelity Windows LDR Hijacking (T1027.012) |
| T1036 | CRITICAL | Ultra-Pro High-Fidelity Masquerading and Process Path Abuse (T1036), Legitimate Windows Binary Copied to User-Writable Location, Ultra-Pro High-Fidelity Double File Extension Execution (T1036.007) |
| T1036.001 | CRITICAL | Ultra-Pro High-Fidelity Invalid or Forged Code Signature (T1036.001) |
| T1036.002 | CRITICAL | Ultra-Pro High-Fidelity RTLO Character Execution (T1036.002) |
| T1036.003 | CRITICAL | Ultra-Pro High-Fidelity Renamed System Utility (T1036.003) |
| T1036.004 | CRITICAL | Ultra-Pro High-Fidelity Masquerading via Path Anomaly (T1036.004) |
| T1036.005 | HIGH | Legitimate Windows Binary Copied to User-Writable Location |
| T1036.006 | CRITICAL | Ultra-Pro High-Fidelity Space After Filename Masquerading (T1036.006) |
| T1036.007 | CRITICAL | Ultra-Pro High-Fidelity Double File Extension Execution (T1036.007) |
| T1036.008 | CRITICAL | Ultra-Pro High-Fidelity Masquerade File Type via Interpreter Misuse (T1036.008) |
| T1036.009 | CRITICAL | Ultra-Pro High-Fidelity Allure Document and RTLO Masquerading (T1036.009) |
| T1037 | CRITICAL | High-Fidelity Logon Script Persistence (T1037) |
| T1037.001 | CRITICAL | High-Fidelity UserInitMprLogonScript Persistence |
| T1037.002 | CRITICAL | High-Fidelity Netsh Helper DLL Persistence |
| T1037.003 | CRITICAL | Ultra-Pro Network Logon Script/Shortcut Modification (T1037.003) |
| T1037.004 | CRITICAL | Ultra-Pro RC Script and Init.d Persistence (T1037.004) |
| T1037.005 | CRITICAL | Ultra-Pro macOS Startup Items Persistence (T1037.005) |
| T1040 | HIGH | Ultra-Pro High-Fidelity Network Sniffing Detection (T1040) |
| T1047 | HIGH | Suspicious Remote Process Creation via WMIC |
| T1053 | HIGH | Gyanús ütemezett feladat vagy munkakör létrehozása a Persistence (T1053) miatt |
| T1053.002 | HIGH | High-Fidelity At.exe Activity Detection |
| T1053.003 | HIGH | High-Fidelity Cron Persistence and In-Place Modification |
| T1053.005 | HIGH | Suspicious Scheduled Task Creation Executing PowerShell |
| T1053.006 | HIGH | High-Fidelity Systemd Service Creation or Modification |
| T1053.007 | HIGH | High-Fidelity Systemd Timer Persistence Detection |
| T1055 | CRITICAL | Ultra-Pro Stealthy Process Injection Detection (T1055) |
| T1055.001 | CRITICAL | Ultra-Pro Stealthy DLL Injection (T1055.001) |
| T1055.002 | CRITICAL | Ultra-Pro Stealthy PE Injection (T1055.002) |
| T1055.003 | CRITICAL | Ultra-Pro Stealthy Thread Hijacking (T1055.003) |
| T1055.004 | CRITICAL | Ultra-Pro Stealthy APC Injection (T1055.004) |
| T1055.005 | CRITICAL | Ultra-Pro Stealthy TLS Injection (T1055.005) |
| T1055.008 | CRITICAL | Ultra-Pro Stealthy Ptrace Injection (T1055.008) |
| T1055.009 | CRITICAL | Ultra-Pro Stealthy Module Overwriting (T1055.009) |
| T1055.011 | CRITICAL | Ultra-Pro Stealthy EWM Injection (T1055.011) |
| T1055.012 | CRITICAL | Ultra-Pro Stealthy Process Hollowing (T1055.012) |
| T1055.013 | CRITICAL | Ultra-Pro Stealthy Process Hollowing (T1055.013) |
| T1055.014 | CRITICAL | Ultra-Pro Stealthy Process Ghosting (T1055.014) |
| T1055.015 | CRITICAL | Ultra-Pro Stealthy ListPlanting Injection (T1055.015) |
| T1056.001 | HIGH | Ultra-Pro High-Fidelity Input Capture Detection (T1056), Ultra-Pro High-Fidelity Keylogging & Input Hooking (T1056.001) |
| T1056.002 | HIGH | Ultra-Pro High-Fidelity GUI Input Capture (T1056.002) |
| T1056.003 | CRITICAL | Ultra-Pro High-Fidelity Digital Certificate Theft (T1056.003) |
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
| T1070 | HIGH | Ultra-Pro High-Fidelity Indicator Removal on Host (T1070) |
| T1070.001 | HIGH | Ultra-Pro High-Fidelity Indicator Removal on Host (T1070), Security Event Log Cleared Using wevtutil.exe |
| T1070.002 | HIGH | Ultra-Pro High-Fidelity Linux Log Clearing and Journal Sabotage (T1070.002) |
| T1070.003 | HIGH | Ultra-Pro High-Fidelity Mailbox Data Clearing and Rule Sabotage (T1070.003) |
| T1070.004 | HIGH | Ultra-Pro High-Fidelity Indicator Removal on Host (T1070), Ultra-Pro High-Fidelity Forensic Artifact and File Deletion (T1070.004) |
| T1070.005 | HIGH | Ultra-Pro High-Fidelity Network Share and Credential Removal (T1070.005) |
| T1070.006 | HIGH | Ultra-Pro High-Fidelity Timestomp and MACE Attribute Manipulation (T1070.006) |
| T1070.007 | HIGH | Ultra-Pro High-Fidelity Network History and RDP Trace Removal (T1070.007) |
| T1070.008 | CRITICAL | Ultra-Pro High-Fidelity Email Storage and Database Destruction (T1070.008) |
| T1070.009 | HIGH | Ultra-Pro High-Fidelity Persistence Artifact Removal (T1070.009) |
| T1072 | CRITICAL | High-Fidelity Software Deployment Tool Abuse Detection |
| T1078 | HIGH | High-Fidelity Anomalous Logon via Valid Account |
| T1078.001 | CRITICAL | High-Fidelity Default Account Abuse Detection |
| T1078.002 | HIGH | High-Fidelity Domain Account Lateral Movement Anomaly |
| T1078.003 | CRITICAL | High-Fidelity Local Account Remote Access Detection |
| T1078.004 | CRITICAL | High-Fidelity Cloud Account Compromise (Entra ID) |
| T1087 | HIGH | Suspicious Use of net user or net localgroup via cmd.exe |
| T1087.001 | HIGH | Ultra-Pro High-Fidelity Local Account Discovery (T1087.001) |
| T1091 | HIGH | High-Fidelity Process Execution from Removable Media |
| T1098 | CRITICAL | Suspicious Use of net user or net localgroup via cmd.exe, High-Fidelity Account Manipulation - Persistence Focused |
| T1098.001 | CRITICAL | High-Fidelity Entra ID Application Credential Addition |
| T1098.002 | CRITICAL | High-Fidelity Exchange Mailbox Permission Grant (T1098.002) |
| T1098.003 | CRITICAL | High-Fidelity Entra ID App Certificate Addition |
| T1098.004 | CRITICAL | High-Fidelity Azure Role Assignment Escalation |
| T1098.005 | HIGH | High-Fidelity Device Registration Persistence (T1098.005) |
| T1098.006 | CRITICAL | High-Fidelity MFA Method Addition |
| T1105 | HIGH | Suspicious Base64-Encoded PowerShell Command with Network Activity, Suspicious Use of Built-in Windows Tools for File Download and Code Execution |
| T1106 | CRITICAL | High-Fidelity Native API Abuse via LOLBins |
| T1110 | HIGH | Ultra-Pro High-Fidelity Brute Force & Tooling (T1110) |
| T1110.001 | MEDIUM | Multiple Failed Login Attempts for Single User (Possible Password Guessing) |
| T1110.002 | CRITICAL | Ultra-Pro High-Fidelity Credential Export & Cracking (T1110.002) |
| T1110.003 | HIGH | Ultra-Pro High-Fidelity Password Spraying (T1110.003) |
| T1110.004 | HIGH | Ultra-Pro High-Fidelity Credential Stuffing & Combo-list Abuse (T1110.004) |
| T1111 | CRITICAL | Ultra-Pro High-Fidelity MFA Evasion & Session Hijacking (T1111) |
| T1112 | CRITICAL | Ultra-Pro High-Fidelity Registry Tampering for Evasion (T1112) |
| T1127 | CRITICAL | Ultra-Pro High-Fidelity Trusted Developer Utility Proxy (T1127), Ultra-Pro High-Fidelity MSBuild Proxy Execution (T1127.001) |
| T1127.001 | CRITICAL | Ultra-Pro High-Fidelity MSBuild Proxy Execution (T1127.001) |
| T1129 | HIGH | High-Fidelity Shared Module Load from Untrusted Path |
| T1133 | HIGH | Anomalous External Remote Service Access Context |
| T1134 | CRITICAL | Ultra-Pro Access Token Manipulation & Impersonation (T1134) |
| T1134.001 | CRITICAL | Ultra-Pro Token Impersonation via LSASS Handle Duplication (T1134.001) |
| T1134.002 | CRITICAL | Ultra-Pro Create Process with Token (T1134.002) |
| T1134.003 | CRITICAL | Ultra-Pro Make and Impersonate Token (T1134.003) |
| T1134.004 | CRITICAL | Ultra-Pro Parent PID Spoofing & Process Tree Violation (T1134.004) |
| T1134.005 | CRITICAL | Ultra-Pro SID-History Injection & DS Manipulation (T1134.005) |
| T1136 | CRITICAL | Ultra-Pro Unauthorized Account Creation (T1136) |
| T1136.001 | CRITICAL | Ultra-Pro Unauthorized Local Account Creation (T1136.001) |
| T1136.002 | CRITICAL | Ultra-Pro Unauthorized Domain Account Creation (T1136.002) |
| T1136.003 | CRITICAL | Ultra-Pro Unauthorized Cloud Account Creation (T1136.003) |
| T1137 | HIGH | Ultra-Pro Office Application Startup Persistence (T1137) |
| T1137.001 | CRITICAL | Ultra-Pro Office Global Template Integrity (T1137.001) |
| T1137.002 | CRITICAL | Ultra-Pro Office Test DLL Persistence (T1137.002) |
| T1137.003 | HIGH | Ultra-Pro Outlook Custom Forms Persistence (T1137.003) |
| T1137.004 | CRITICAL | Ultra-Pro Outlook Home Page Hijacking & Bypass (T1137.004) |
| T1137.005 | CRITICAL | Ultra-Pro Office Security Policy Tampering (T1137.005) |
| T1137.006 | CRITICAL | Ultra-Pro Office Add-in Binary Persistence (T1137.006) |
| T1140 | HIGH | Ultra-Pro Stealthy Deobfuscation/Decoding (T1140) |
| T1176 | CRITICAL | Ultra-Pro Browser Extension Force-Install Persistence (T1176) |
| T1187 | CRITICAL | Ultra-Pro High-Fidelity Forced Authentication (T1187) |
| T1189 | CRITICAL | Browser-Originating Shell or System Tool Execution |
| T1190 | MEDIUM | Suspicious Cross-Site Scripting (XSS) Attempt Detected on Web Server |
| T1195 | CRITICAL | High-Fidelity Supply Chain Compromise Detection (Post-Update Anomaly) |
| T1195.001 | CRITICAL | High-Fidelity Dependency Poisoning Detection |
| T1195.002 | CRITICAL | High-Fidelity Compromised Binary Activity (Post-Update) |
| T1195.003 | CRITICAL | High-Fidelity Hardware/Firmware Manipulation Detection |
| T1197 | HIGH | Suspicious File Download via Bitsadmin (High Fidelity) |
| T1199 | HIGH | High-Fidelity Trusted Relationship Abuse Detection |
| T1200 | CRITICAL | Malicious Hardware-Induced Command Execution (HID Injection) |
| T1202 | HIGH | Ultra-Pro High-Fidelity Indirect Command Execution (T1202) |
| T1203 | CRITICAL | High-Fidelity Client-Side Exploitation and Shell Spawning |
| T1204 | HIGH | Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity) |
| T1204.001 | CRITICAL | High-Fidelity User Execution of Malicious Link (T1204.001) |
| T1204.002 | CRITICAL | High-Fidelity User Execution of Malicious File |
| T1204.003 | CRITICAL | High-Fidelity Execution from Mounted Virtual Disk (T1204.003) |
| T1204.004 | HIGH | Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel |
| T1205 | HIGH | Ultra-Pro Traffic Signaling & Port Knocking (T1205) |
| T1205.001 | HIGH | Ultra-Pro Port Knocking & Raw Socket Listener (T1205.001) |
| T1205.002 | CRITICAL | Ultra-Pro Socket Filter & WFP Traffic Signaling (T1205.002) |
| T1207 | CRITICAL | Ultra-Pro High-Fidelity Rogue DC Topology Manipulation (T1207) |
| T1211 | CRITICAL | Ultra-Pro High-Fidelity Privilege Escalation Exploitation (T1211) |
| T1212 | CRITICAL | Ultra-Pro High-Fidelity Credential Service Exploitation (T1212) |
| T1216 | CRITICAL | Ultra-Pro High-Fidelity System Script Proxy Execution (T1216) |
| T1216.001 | CRITICAL | Ultra-Pro High-Fidelity Pubprn Script Proxy Execution (T1216.001) |
| T1217 | HIGH | Ultra-Pro High-Fidelity Browser Information Discovery (T1217) |
| T1218 | HIGH | Ultra-Pro High-Fidelity Regsvcs/Regasm Proxy Execution (T1218.009), Ultra-Pro High-Fidelity System Binary Proxy Execution (T1218), Suspicious Use of Built-in Windows Tools for File Download and Code Execution |
| T1218.001 | CRITICAL | Ultra-Pro High-Fidelity HH.exe Proxy Execution (T1218.001) |
| T1218.002 | CRITICAL | Ultra-Pro High-Fidelity Control.exe Proxy Execution (T1218.002) |
| T1218.003 | CRITICAL | Ultra-Pro High-Fidelity MsiExec Proxy Execution (T1218.003) |
| T1218.004 | CRITICAL | Ultra-Pro High-Fidelity InstallUtil Proxy Execution (T1218.004) |
| T1218.005 | HIGH | Suspicious Mshta Execution of Remote Script (High Fidelity) |
| T1218.007 | HIGH | Suspicious Msiexec Installation from Remote URL (High Fidelity) |
| T1218.008 | CRITICAL | Ultra-Pro High-Fidelity Odbcconf Proxy Execution (T1218.008) |
| T1218.009 | CRITICAL | Ultra-Pro High-Fidelity Regsvcs/Regasm Proxy Execution (T1218.009) |
| T1218.010 | HIGH | Suspicious Regsvr32 Execution Indicative of LOLBAS Abuse (High Fidelity) |
| T1218.011 | HIGH | Suspicious Rundll32 Execution with Script or Remote Payload (High Fidelity) |
| T1218.012 | CRITICAL | Ultra-Pro High-Fidelity Verclsid Proxy Execution (T1218.012) |
| T1218.013 | CRITICAL | Ultra-Pro High-Fidelity Rundll32 Proxy Execution (T1218.013) |
| T1218.014 | CRITICAL | Ultra-Pro High-Fidelity MMC Proxy Execution (T1218.014) |
| T1219 | HIGH | Suspicious Use of Legitimate Remote Administration Tools Outside Enterprise Pattern |
| T1220 | HIGH | Ultra-Pro High-Fidelity XSL Script Processing (T1220) |
| T1221 | HIGH | Ultra-Pro High-Fidelity Office Template Injection (T1221) |
| T1222 | HIGH | Ultra-Pro High-Fidelity Permissions Modification (T1222) |
| T1222.001 | HIGH | Ultra-Pro High-Fidelity Windows File Permissions Modification (T1222.001), Ultra-Pro High-Fidelity Permissions Modification (T1222) |
| T1222.002 | HIGH | Ultra-Pro High-Fidelity Linux File Permissions Modification (T1222.002) |
| T1480 | HIGH | Ultra-Pro High-Fidelity Execution Guardrails Discovery (T1480) |
| T1480.001 | HIGH | Ultra-Pro Environmental Keying Discovery (T1480.001) |
| T1484 | CRITICAL | Ultra-Pro Domain Policy Manipulation & GPO Abuse (T1484) |
| T1484.001 | CRITICAL | Ultra-Pro Group Policy Modification & Abuse (T1484.001) |
| T1484.002 | CRITICAL | Ultra-Pro Domain Trust Tampering & SID Filtering Bypass (T1484.002) |
| T1486 | CRITICAL | Ransomware Preparation Activity Detected on Windows Host (High Fidelity) |
| T1490 | CRITICAL | Suspicious Deletion of Volume Shadow Copies via VSSAdmin (High Fidelity), Ransomware Preparation Activity Detected on Windows Host (High Fidelity) |
| T1497 | HIGH | Ultra-Pro High-Fidelity Virtualization/Sandbox Evasion (T1497) |
| T1497.001 | HIGH | Ultra-Pro High-Fidelity VM Artifact Discovery (T1497.001), Ultra-Pro High-Fidelity Virtualization/Sandbox Evasion (T1497) |
| T1497.002 | HIGH | Ultra-Pro High-Fidelity User Interaction Evasion (T1497.002) |
| T1497.003 | HIGH | Ultra-Pro High-Fidelity Virtualization/Sandbox Evasion (T1497), Ultra-Pro High-Fidelity Time-based Evasion (T1497.003) |
| T1505 | CRITICAL | Ultra-Pro Web Shell Execution Patterns (T1505.003) |
| T1505.001 | CRITICAL | Ultra-Pro SQL Server Command Shell Execution (T1505.001) |
| T1505.002 | CRITICAL | Ultra-Pro IIS Native Module Injection (T1505.002) |
| T1505.003 | HIGH | Webshell Upload or Interaction Detected on Web Server (High Fidelity) |
| T1505.004 | CRITICAL | Ultra-Pro Mainboard Boot Image & SPI Flash Tampering (T1542.004) |
| T1505.005 | CRITICAL | Ultra-Pro Terminal Services DLL Hijacking (T1505.005) |
| T1525 | CRITICAL | Exploit-Grade Unauthorized Container Image Execution (Implant Container Image) |
| T1528 | CRITICAL | Ultra-Pro High-Fidelity Application Token & Session Hijacking (T1528) |
| T1535 | CRITICAL | Ultra-Pro High-Fidelity Unused Service Manipulation (T1535) |
| T1539 | CRITICAL | Ultra-Pro High-Fidelity Web Session Cookie Theft (T1539) |
| T1542 | CRITICAL | Ultra-Pro Pre-OS Boot Manipulation (T1542) |
| T1542.001 | CRITICAL | Ultra-Pro ROM Kit & UEFI Firmware Tampering (T1542.001) |
| T1542.002 | CRITICAL | Ultra-Pro Component Firmware Tampering (T1542.002) |
| T1542.003 | CRITICAL | Ultra-Pro Bootkit Persistence & EFI Tampering (T1542.003) |
| T1542.004 | CRITICAL | Ultra-Pro Mainboard Boot Image & SPI Flash Tampering (T1542.004) |
| T1542.005 | CRITICAL | Ultra-Pro DHCP/PXE Boot Hijacking (T1542.005) |
| T1543 | HIGH | Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services |
| T1543.001 | CRITICAL | Ultra-Pro macOS Launch Agent Persistence Detection (T1543.001) |
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
| T1546.015 | HIGH | Suspicious COM Hijacking for User-Level Persistence (High Fidelity) |
| T1546.016 | HIGH | Ultra-Pro MSI Installer Custom Action Persistence (T1546.016) |
| T1547 | HIGH | Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása |
| T1547.001 | HIGH | Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása, Suspicious Registry Run Key Modification for User Persistence (High Fidelity) |
| T1547.002 | CRITICAL | High-Fidelity LSA Authentication Package Persistence |
| T1547.003 | CRITICAL | High-Fidelity Time Provider Persistence (T1547.003) |
| T1547.004 | CRITICAL | High-Fidelity Winlogon Helper DLL Persistence (T1547.004) |
| T1547.005 | CRITICAL | High-Fidelity SSP DLL Persistence (T1547.005) |
| T1547.006 | CRITICAL | High-Fidelity Kernel Driver Registration (T1547.006) |
| T1547.007 | HIGH | High-Fidelity Browser Session Persistence (T1547.007) |
| T1547.008 | CRITICAL | High-Fidelity LSASS Driver/Package Persistence (T1547.008) |
| T1547.009 | HIGH | High-Fidelity Shortcut Modification Detection |
| T1547.010 | CRITICAL | High-Fidelity AppCert DLL Persistence (T1547.010) |
| T1547.011 | CRITICAL | High-Fidelity Application Shimming Persistence (T1547.011) |
| T1547.012 | HIGH | High-Fidelity COM Hijacking Persistence (T1547.012) |
| T1547.013 | HIGH | High-Fidelity Email Client Helper Persistence (T1547.013) |
| T1547.014 | CRITICAL | High-Fidelity Active Setup Persistence (T1547.014) |
| T1547.015 | HIGH | High-Fidelity COM Hijacking Persistence (T1547.015) |
| T1548 | CRITICAL | Ultra-Pro Privilege Escalation via Registry Hijacking (T1548.002) |
| T1548.001 | HIGH | Ultra-Pro Setuid/Setgid Bit Manipulation (T1548.001) |
| T1548.002 | HIGH | Ultra-Pro Privilege Escalation via Registry Hijacking (T1548.002), UAC Bypass via Fodhelper Registry Hijack (High Fidelity) |
| T1548.003 | CRITICAL | Ultra-Pro Sudoers Manipulation and Sudo Abuse (T1548.003) |
| T1548.004 | CRITICAL | Ultra-Pro AppleScript Privilege Escalation (T1548.004) |
| T1548.005 | HIGH | Ultra-Pro SUID Desktop Entry & Shortcut Abuse (T1548.005) |
| T1550 | CRITICAL | Ultra-Pro High-Fidelity Alternate Authentication Material (T1550) |
| T1550.001 | CRITICAL | Ultra-Pro High-Fidelity Application Access Token Abuse (T1550.001) |
| T1550.002 | CRITICAL | Ultra-Pro High-Fidelity Alternate Authentication Material (T1550), Ultra-Pro High-Fidelity Pass-the-Hash Detection (T1550.002) |
| T1550.003 | CRITICAL | Ultra-Pro High-Fidelity Alternate Authentication Material (T1550), Ultra-Pro High-Fidelity Pass-the-Ticket Detection (T1550.003) |
| T1550.004 | CRITICAL | Ultra-Pro High-Fidelity Pass-the-Session Detection (T1550.004) |
| T1552 | HIGH | Ultra-Pro High-Fidelity Credentials In Registry Discovery (T1552.002) |
| T1552.001 | HIGH | Ultra-Pro High-Fidelity Unsecured Credentials Discovery (T1552), Ultra-Pro High-Fidelity Credentials In Files Discovery (T1552.001) |
| T1552.002 | HIGH | Ultra-Pro High-Fidelity Unsecured Credentials Discovery (T1552), Ultra-Pro High-Fidelity Credentials In Registry Discovery (T1552.002) |
| T1552.003 | HIGH | Ultra-Pro High-Fidelity Shell History & Console Discovery (T1552.003) |
| T1552.004 | HIGH | Ultra-Pro High-Fidelity Private Key Discovery (T1552.004) |
| T1552.005 | CRITICAL | Ultra-Pro High-Fidelity Cloud Credential Discovery (T1552.005) |
| T1552.006 | CRITICAL | Ultra-Pro High-Fidelity GPP Password Discovery (T1552.006) |
| T1552.007 | HIGH | Ultra-Pro High-Fidelity Container Secret Discovery (T1552.007) |
| T1552.008 | CRITICAL | Ultra-Pro High-Fidelity GPP Password Discovery (T1552.008) |
| T1553 | CRITICAL | Ultra-Pro High-Fidelity macOS Gatekeeper and Quarantine Bypass (T1553.001) |
| T1553.001 | CRITICAL | Ultra-Pro High-Fidelity macOS Gatekeeper and Quarantine Bypass (T1553.001) |
| T1553.002 | CRITICAL | Ultra-Pro High-Fidelity SIP Hijacking and Trust Subversion (T1553.002) |
| T1553.003 | CRITICAL | Ultra-Pro High-Fidelity Windows Catalog Database Subversion (T1553.003) |
| T1553.004 | CRITICAL | Ultra-Pro High-Fidelity Root Certificate Injection (T1553.004), Ultra-Pro High-Fidelity Subvert Trust Controls (T1553) |
| T1553.005 | CRITICAL | Ultra-Pro High-Fidelity MotW Bypass & Zone Subversion (T1553.005), Ultra-Pro High-Fidelity Subvert Trust Controls (T1553) |
| T1553.006 | CRITICAL | Ultra-Pro High-Fidelity Code Integrity & DSE Subversion (T1553.006) |
| T1554 | CRITICAL | Ultra-Pro Client Binary Integrity Compromise (T1554) |
| T1555 | HIGH | Nem böngészős folyamat hozzáférése a böngésző hitelesítőadat-tárolóihoz (High Fidelity) |
| T1555.001 | HIGH | Ultra-Pro High-Fidelity Vault Credential Harvesting (T1555.001) |
| T1555.002 | CRITICAL | Ultra-Pro High-Fidelity Securityd Memory Dumping (T1555.002) |
| T1555.003 | CRITICAL | Ultra-Pro High-Fidelity Browser Credential Harvesting (T1555.003) |
| T1555.004 | HIGH | Ultra-Pro High-Fidelity Windows Credential Manager Harvesting (T1555.004) |
| T1555.005 | CRITICAL | Ultra-Pro High-Fidelity Password Manager Extraction (T1555.005) |
| T1555.006 | CRITICAL | Ultra-Pro High-Fidelity Cloud Secret Harvesting (T1555.006) |
| T1556 | CRITICAL | Exploit-Grade Authentication Process Hijack via Suspicious DLL Registration |
| T1556.001 | CRITICAL | Exploit-Grade Security Support Provider Hijacking (LSA SSP) |
| T1556.002 | CRITICAL | Exploit-Grade Password Filter DLL Hijacking via LSA Notification Packages |
| T1556.003 | CRITICAL | Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003) |
| T1556.004 | CRITICAL | Ultra-Pro Network Device Authentication Hijacking (T1556.004) |
| T1556.005 | CRITICAL | Ultra-Pro SID History Injection Correlation (T1556.005) |
| T1556.006 | CRITICAL | Ultra-Pro Entra ID MFA Method Hijacking (T1556.006) |
| T1556.007 | CRITICAL | Ultra-Pro Hybrid Identity Sync Manipulation (T1556.007) |
| T1556.008 | CRITICAL | Ultra-Pro Network-to-Cloud Auth Hijacking (T1556.008) |
| T1557 | HIGH | Ultra-Pro High-Fidelity Adversary-in-the-Middle (T1557) |
| T1557.001 | CRITICAL | Ultra-Pro High-Fidelity LLMNR/NBT-NS Poisoning (T1557.001) |
| T1557.002 | HIGH | Ultra-Pro High-Fidelity ARP Poisoning Detection (T1557.002) |
| T1557.003 | CRITICAL | Ultra-Pro High-Fidelity DHCP Spoofing Detection (T1557.003) |
| T1558 | CRITICAL | Ultra-Pro High-Fidelity Kerberos Attack Detection (T1558) |
| T1558.001 | CRITICAL | Ultra-Pro High-Fidelity Golden Ticket Forgery & Injection (T1558.001) |
| T1558.002 | CRITICAL | Ultra-Pro High-Fidelity Silver Ticket Forgery & Injection (T1558.002) |
| T1558.003 | HIGH | Ultra-Pro High-Fidelity Kerberos Attack Detection (T1558), Gyanús Kerberos TGS jegykérés (Kerberoasting) |
| T1558.004 | CRITICAL | Ultra-Pro High-Fidelity Kerberos Attack Detection (T1558), Ultra-Pro High-Fidelity AS-REP Roasting & LDAP Enumeration (T1558.004) |
| T1559 | CRITICAL | High-Fidelity Indirect IPC and COM Execution |
| T1559.001 | HIGH | High-Fidelity Indirect IPC and COM Execution, Gyanús elnevezett csővezeték-létrehozás, amely utólagos kihasználási eszközökhöz kapcsolódik (High Fidelity) |
| T1559.002 | CRITICAL | High-Fidelity Office DDE Contextual Anomaly, High-Fidelity Indirect IPC and COM Execution |
| T1559.003 | HIGH | High-Fidelity Hypervisor API and VM Escape Research |
| T1560.001 | HIGH | Adatok gyanús archiválása exfiltráció céljából |
| T1562 | HIGH | Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services |
| T1562.001 | CRITICAL | Ransomware Preparation Activity Detected on Windows Host (High Fidelity), Windows Defender védelem kikapcsolása vagy módosítása PowerShell segítségével, Biztonsági szolgáltatások gyanús leállítása |
| T1562.002 | CRITICAL | Ultra-Pro High-Fidelity Disable Windows Event Logging (T1562.002) |
| T1562.003 | HIGH | Ultra-Pro High-Fidelity Command History Logging Impairment (T1562.003) |
| T1562.004 | HIGH | Suspicious Firewall Modification via Netsh.exe |
| T1562.006 | CRITICAL | Ultra-Pro High-Fidelity Indicator Blocking and Telemetry Silencing (T1562.006) |
| T1562.007 | CRITICAL | Ultra-Pro High-Fidelity Cloud Firewall Impairment (T1562.007) |
| T1562.008 | CRITICAL | Ultra-Pro High-Fidelity Cloud Logging Impairment (T1562.008) |
| T1562.009 | CRITICAL | Ultra-Pro High-Fidelity Safe Mode Defense Evasion (T1562.009) |
| T1562.010 | CRITICAL | Ultra-Pro High-Fidelity Defense Downgrade Attack (T1562.010) |
| T1562.011 | HIGH | Ultra-Pro High-Fidelity Virtualization and Sandbox Evasion (T1564.011) |
| T1562.012 | CRITICAL | Ultra-Pro High-Fidelity Cloud Security Infrastructure Impairment (T1562.012) |
| T1564 | HIGH | Ultra-Pro High-Fidelity Hide Artifacts Detection (T1564) |
| T1564.001 | HIGH | Ultra-Pro High-Fidelity Hidden File Attribute Manipulation (T1564.001), Ultra-Pro High-Fidelity Hide Artifacts Detection (T1564) |
| T1564.002 | CRITICAL | Ultra-Pro High-Fidelity Hide Artifacts Detection (T1564), Ultra-Pro High-Fidelity Hidden User Account Creation (T1564.002) |
| T1564.003 | HIGH | Ultra-Pro High-Fidelity Hidden Window Execution (T1564.003) |
| T1564.004 | HIGH | Ultra-Pro High-Fidelity Hide Artifacts Detection (T1564), Ultra-Pro High-Fidelity NTFS Alternative Data Stream (ADS) Abuse (T1564.004) |
| T1564.005 | HIGH | Ultra-Pro High-Fidelity Hidden File System Manipulation (T1564.005) |
| T1564.006 | HIGH | Ultra-Pro High-Fidelity Virtual Instance Execution Abuse (T1564.006) |
| T1564.007 | HIGH | Ultra-Pro High-Fidelity VBA Macro Security Evasion (T1564.007) |
| T1564.008 | CRITICAL | Ultra-Pro High-Fidelity Email Hiding Rules Detection (T1564.008) |
| T1564.009 | HIGH | Ultra-Pro High-Fidelity Resource Extraction and Abuse (T1564.009) |
| T1564.010 | HIGH | Ultra-Pro High-Fidelity Process Argument Spoofing Detection (T1564.010) |
| T1564.011 | HIGH | Ultra-Pro High-Fidelity Virtual Instance Abuse (T1564.011) |
| T1566 | CRITICAL | High-Fidelity Phishing Payload Execution from Communication Apps |
| T1566.001 | CRITICAL | High-Fidelity Spearphishing Attachment Execution |
| T1566.002 | CRITICAL | High-Fidelity Browser-Originating Payload Execution |
| T1566.003 | CRITICAL | High-Fidelity Process Spawn from Business Communication Service |
| T1566.004 | HIGH | High-Fidelity Detection of Post-Vishing Remote Tool Execution |
| T1569 | HIGH | High-Fidelity System Service Execution Detection |
| T1569.001 | CRITICAL | High-Fidelity Launch Daemon Persistence Detection |
| T1569.002 | HIGH | High-Fidelity System Service Execution Detection, High-Fidelity System Service Execution Detection (T1569.002) |
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
| T1574.013 | CRITICAL | Exploit-Grade KernelCallbackTable Manipulation via Remote Memory Write |
| T1578 | CRITICAL | Ultra-Pro High-Fidelity Cloud Snapshot Exfiltration (T1578.002), Ultra-Pro High-Fidelity Cloud Infrastructure Tampering (T1578) |
| T1578.001 | CRITICAL | Ultra-Pro High-Fidelity Suspicious Cloud Instance Creation (T1578.001) |
| T1578.002 | CRITICAL | Ultra-Pro High-Fidelity Cloud Snapshot Exfiltration (T1578.002) |
| T1578.003 | HIGH | Ultra-Pro High-Fidelity Cloud Instance Destruction (T1578.003) |
| T1578.004 | CRITICAL | Ultra-Pro High-Fidelity Cloud Image Tampering (T1578.004) |
| T1578.005 | CRITICAL | Ultra-Pro High-Fidelity Cloud Network Security Regression (T1578.005) |
| T1580 | HIGH | Ultra-Pro High-Fidelity Cloud Infrastructure Discovery (T1580) |
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
| T1599 | CRITICAL | Ultra-Pro High-Fidelity Logical Isolation Bypass (T1599.001), Ultra-Pro High-Fidelity Network Boundary Bridging (T1599) |
| T1599.001 | CRITICAL | Ultra-Pro High-Fidelity Logical Isolation Bypass (T1599.001) |
| T1600 | HIGH | Ultra-Pro High-Fidelity Weaken Encryption Attempt (T1600) |
| T1600.001 | CRITICAL | Ultra-Pro High-Fidelity System Image Patching (T1600.001) |
| T1600.002 | HIGH | Ultra-Pro High-Fidelity Disable Entity Verification (T1600.002) |
| T1601 | CRITICAL | Ultra-Pro High-Fidelity Network OS Image Modification (T1601) |
| T1601.001 | CRITICAL | Ultra-Pro High-Fidelity Network Binary Patching (T1601.001) |
| T1601.002 | CRITICAL | Ultra-Pro High-Fidelity Malicious Network OS Upgrade (T1601.002) |
| T1606 | CRITICAL | Ultra-Pro High-Fidelity Web Token Forgery (T1606) |
| T1606.001 | CRITICAL | Ultra-Pro High-Fidelity Web Cookie Harvesting (T1606.001) |
| T1606.002 | CRITICAL | Ultra-Pro High-Fidelity Web Token Forgery & Golden SAML (T1606.002) |
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
| T1620 | CRITICAL | Ultra-Pro High-Fidelity Reflective Code Loading (T1620) |
| T1621 | HIGH | Ultra-Pro High-Fidelity MFA Prompt Bombing Automation (T1621) |
| T1622 | HIGH | Ultra-Pro Stealthy Debugger Evasion (T1622) |
| T1647 | HIGH | Ultra-Pro High-Fidelity macOS Plist Persistence Modification (T1647) |
| T1648 | HIGH | High-Fidelity Serverless Function Persistence or Abuse |
| T1649 | CRITICAL | Ultra-Pro High-Fidelity Certificate & Private Key Theft (T1649) |
| T1650 | HIGH | High-Fidelity Cloud Account Acquisition and Initialization - T1650 |
| T1651 | CRITICAL | High-Fidelity Cloud Administration Agent Abuse |
| T1653 | MEDIUM | Ultra-Pro Power Settings Manipulation (T1137.001) |
| T1656 | HIGH | Ultra-Pro High-Fidelity Impersonation and Identity Hijacking (T1656) |
| T1659 | HIGH | Professional Content Impersonation and Infrastructure Mirroring |
