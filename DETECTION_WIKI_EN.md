# 🛡️ Detection Rule Knowledge Base

### 📊 Detection Engineering Dashboard
| Kritikusság | Darabszám |
| :--- | :--- |
| 🔴 Critical | 360 |
| 🟠 High | 261 |
| 🟡 Medium | 7 |
| 🔵 Low | 0 |
| **Összesen** | **628** |

---
## 📖 Tartalomjegyzék
- [Ultra-Pro High-Fidelity Steganography & Data Reconstruction (T1001)](#ultra-pro-high-fidelity-steganography-&-data-reconstruction-(t1001))
- [Ultra-Pro High-Fidelity Junk Data & Command Padding (T1001.001)](#ultra-pro-high-fidelity-junk-data-&-command-padding-(t1001001))
- [Ultra-Pro High-Fidelity Steganography & Data Reconstruction (T1001.002)](#ultra-pro-high-fidelity-steganography-&-data-reconstruction-(t1001002))
- [Ultra-Pro High-Fidelity Protocol Impersonation (T1001.003)](#ultra-pro-high-fidelity-protocol-impersonation-(t1001003))
- [Ultra-Pro High-Fidelity LSASS Credential Dumping (T1003)](#ultra-pro-high-fidelity-lsass-credential-dumping-(t1003))
- [Suspicious Access to LSASS Process Memory](#suspicious-access-to-lsass-process-memory)
- [Ultra-Pro High-Fidelity SAM & SYSTEM Registry Theft (T1003.002)](#ultra-pro-high-fidelity-sam-&-system-registry-theft-(t1003002))
- [Ultra-Pro High-Fidelity NTDS.dit Extraction (T1003.003)](#ultra-pro-high-fidelity-ntdsdit-extraction-(t1003003))
- [Ultra-Pro High-Fidelity LSA Secrets & Security Hive Theft (T1003.004)](#ultra-pro-high-fidelity-lsa-secrets-&-security-hive-theft-(t1003004))
- [Ultra-Pro High-Fidelity MSCASH/DCC Extraction (T1003.005)](#ultra-pro-high-fidelity-mscashdcc-extraction-(t1003005))
- [Ultra-Pro High-Fidelity DCSync Attack Detection (T1003.006)](#ultra-pro-high-fidelity-dcsync-attack-detection-(t1003006))
- [Ultra-Pro High-Fidelity LSASS Memory Dump & LOLBin Abuse (T1003.007)](#ultra-pro-high-fidelity-lsass-memory-dump-&-lolbin-abuse-(t1003007))
- [Ultra-Pro High-Fidelity Linux Shadow File Extraction (T1003.008)](#ultra-pro-high-fidelity-linux-shadow-file-extraction-(t1003008))
- [Ultra-Pro High-Fidelity Local Data Harvesting (T1005)](#ultra-pro-high-fidelity-local-data-harvesting-(t1005))
- [Ultra-Pro Stealthy Direct Volume Access (T1006)](#ultra-pro-stealthy-direct-volume-access-(t1006))
- [Ultra-Pro High-Fidelity System Service Discovery (T1007)](#ultra-pro-high-fidelity-system-service-discovery-(t1007))
- [Ultra-Pro High-Fidelity Fallback Channel Detection (T1008)](#ultra-pro-high-fidelity-fallback-channel-detection-(t1008))
- [Ultra-Pro High-Fidelity Application Window Discovery (T1010)](#ultra-pro-high-fidelity-application-window-discovery-(t1010))
- [Ultra-Pro High-Fidelity Bluetooth Exfiltration (T1011)](#ultra-pro-high-fidelity-bluetooth-exfiltration-(t1011))
- [Ultra-Pro High-Fidelity BLE Advertising Exfiltration (T1011.001)](#ultra-pro-high-fidelity-ble-advertising-exfiltration-(t1011001))
- [Ultra-Pro High-Fidelity Query Registry Discovery (T1012)](#ultra-pro-high-fidelity-query-registry-discovery-(t1012))
- [Ultra-Pro High-Fidelity BYOVD Rootkit Loading (T1014)](#ultra-pro-high-fidelity-byovd-rootkit-loading-(t1014))
- [Ultra-Pro High-Fidelity System Network Configuration Discovery (T1016)](#ultra-pro-high-fidelity-system-network-configuration-discovery-(t1016))
- [Ultra-Pro High-Fidelity Internet IP Discovery (T1016.001)](#ultra-pro-high-fidelity-internet-ip-discovery-(t1016001))
- [Ultra-Pro High-Fidelity Terminal Services Configuration Discovery (T1016.002)](#ultra-pro-high-fidelity-terminal-services-configuration-discovery-(t1016002))
- [Ultra-Pro High-Fidelity Remote System Discovery (T1018)](#ultra-pro-high-fidelity-remote-system-discovery-(t1018))
- [Ultra-Pro High-Fidelity Automated Exfiltration (T1020)](#ultra-pro-high-fidelity-automated-exfiltration-(t1020))
- [Ultra-Pro High-Fidelity Client-Linked Cloud Exfil (T1020.001)](#ultra-pro-high-fidelity-client-linked-cloud-exfil-(t1020001))
- [Rapid Logons to Multiple Distant Hosts by Same User](#rapid-logons-to-multiple-distant-hosts-by-same-user)
- [Suspicious RDP Logon from Unusual Source](#suspicious-rdp-logon-from-unusual-source)
- [Ultra-Pro High-Fidelity SMB Admin Share Mapping (T1021.002)](#ultra-pro-high-fidelity-smb-admin-share-mapping-(t1021002))
- [Ultra-Pro High-Fidelity DCOM Remote Execution (T1021.003)](#ultra-pro-high-fidelity-dcom-remote-execution-(t1021003))
- [Ultra-Pro High-Fidelity SSH Lateral Movement & Tunneling (T1021.004)](#ultra-pro-high-fidelity-ssh-lateral-movement-&-tunneling-(t1021004))
- [Ultra-Pro High-Fidelity VNC Lateral Movement & Hijacking (T1021.005)](#ultra-pro-high-fidelity-vnc-lateral-movement-&-hijacking-(t1021005))
- [Ultra-Pro High-Fidelity WinRM Remote Execution (T1021.006)](#ultra-pro-high-fidelity-winrm-remote-execution-(t1021006))
- [Ultra-Pro High-Fidelity Cloud Control Plane Hijacking (T1021.007)](#ultra-pro-high-fidelity-cloud-control-plane-hijacking-(t1021007))
- [Ultra-Pro High-Fidelity macOS ARD Remote Hijacking (T1021.008)](#ultra-pro-high-fidelity-macos-ard-remote-hijacking-(t1021008))
- [Ultra-Pro High-Fidelity Removable Media Data Theft (T1025)](#ultra-pro-high-fidelity-removable-media-data-theft-(t1025))
- [Suspicious Base64-Encoded PowerShell Command with Network Activity](#suspicious-base64-encoded-powershell-command-with-network-activity)
- [Ultra-Pro High-Fidelity Binary Padding Activity (T1027.001)](#ultra-pro-high-fidelity-binary-padding-activity-(t1027001))
- [Ultra-Pro High-Fidelity Software Packing Event (T1027.002)](#ultra-pro-high-fidelity-software-packing-event-(t1027002))
- [Ultra-Pro High-Fidelity Steganography Payload Extraction (T1027.003)](#ultra-pro-high-fidelity-steganography-payload-extraction-(t1027003))
- [Ultra-Pro High-Fidelity Steganography Payload Extraction (T1027.004)](#ultra-pro-high-fidelity-steganography-payload-extraction-(t1027004))
- [Ultra-Pro High-Fidelity Indicator Removal and Signature Theft (T1027.005)](#ultra-pro-high-fidelity-indicator-removal-and-signature-theft-(t1027005))
- [Ultra-Pro High-Fidelity HTML Smuggling Execution (T1027.006)](#ultra-pro-high-fidelity-html-smuggling-execution-(t1027006))
- [Ultra-Pro High-Fidelity Binary Symbol Stripping (T1027.007)](#ultra-pro-high-fidelity-binary-symbol-stripping-(t1027007))
- [Ultra-Pro High-Fidelity Binary Symbol Stripping (T1027.008)](#ultra-pro-high-fidelity-binary-symbol-stripping-(t1027008))
- [Ultra-Pro High-Fidelity Embedded Payload Extraction (T1027.009)](#ultra-pro-high-fidelity-embedded-payload-extraction-(t1027009))
- [Ultra-Pro High-Fidelity Command Line Obfuscation (T1027.010)](#ultra-pro-high-fidelity-command-line-obfuscation-(t1027010))
- [Ultra-Pro High-Fidelity Suspicious Archive Creation (T1027.011)](#ultra-pro-high-fidelity-suspicious-archive-creation-(t1027011))
- [Ultra-Pro High-Fidelity Windows LDR Hijacking (T1027.012)](#ultra-pro-high-fidelity-windows-ldr-hijacking-(t1027012))
- [Ultra-Pro High-Fidelity Scheduled Transfer (T1029)](#ultra-pro-high-fidelity-scheduled-transfer-(t1029))
- [Ultra-Pro High-Fidelity Data Chunking and Fragmentation (T1030)](#ultra-pro-high-fidelity-data-chunking-and-fragmentation-(t1030))
- [Ultra-Pro High-Fidelity System Owner/User Discovery (T1033)](#ultra-pro-high-fidelity-system-owneruser-discovery-(t1033))
- [Ultra-Pro High-Fidelity Masquerading and Process Path Abuse (T1036)](#ultra-pro-high-fidelity-masquerading-and-process-path-abuse-(t1036))
- [Ultra-Pro High-Fidelity Invalid or Forged Code Signature (T1036.001)](#ultra-pro-high-fidelity-invalid-or-forged-code-signature-(t1036001))
- [Ultra-Pro High-Fidelity RTLO Character Execution (T1036.002)](#ultra-pro-high-fidelity-rtlo-character-execution-(t1036002))
- [Ultra-Pro High-Fidelity Renamed System Utility (T1036.003)](#ultra-pro-high-fidelity-renamed-system-utility-(t1036003))
- [Ultra-Pro High-Fidelity Masquerading via Path Anomaly (T1036.004)](#ultra-pro-high-fidelity-masquerading-via-path-anomaly-(t1036004))
- [Legitimate Windows Binary Copied to User-Writable Location](#legitimate-windows-binary-copied-to-user-writable-location)
- [Ultra-Pro High-Fidelity Space After Filename Masquerading (T1036.006)](#ultra-pro-high-fidelity-space-after-filename-masquerading-(t1036006))
- [Ultra-Pro High-Fidelity Double File Extension Execution (T1036.007)](#ultra-pro-high-fidelity-double-file-extension-execution-(t1036007))
- [Ultra-Pro High-Fidelity Masquerade File Type via Interpreter Misuse (T1036.008)](#ultra-pro-high-fidelity-masquerade-file-type-via-interpreter-misuse-(t1036008))
- [Ultra-Pro High-Fidelity Allure Document and RTLO Masquerading (T1036.009)](#ultra-pro-high-fidelity-allure-document-and-rtlo-masquerading-(t1036009))
- [High-Fidelity Logon Script Persistence (T1037)](#high-fidelity-logon-script-persistence-(t1037))
- [High-Fidelity UserInitMprLogonScript Persistence](#high-fidelity-userinitmprlogonscript-persistence)
- [High-Fidelity Netsh Helper DLL Persistence](#high-fidelity-netsh-helper-dll-persistence)
- [Ultra-Pro Network Logon Script/Shortcut Modification (T1037.003)](#ultra-pro-network-logon-scriptshortcut-modification-(t1037003))
- [Ultra-Pro RC Script and Init.d Persistence (T1037.004)](#ultra-pro-rc-script-and-initd-persistence-(t1037004))
- [Ultra-Pro macOS Startup Items Persistence (T1037.005)](#ultra-pro-macos-startup-items-persistence-(t1037005))
- [Ultra-Pro High-Fidelity Network Share Discovery (T1039)](#ultra-pro-high-fidelity-network-share-discovery-(t1039))
- [Ultra-Pro High-Fidelity Network Sniffing Detection (T1040)](#ultra-pro-high-fidelity-network-sniffing-detection-(t1040))
- [Ultra-Pro High-Fidelity Exfiltration Over C2 Channel (T1041)](#ultra-pro-high-fidelity-exfiltration-over-c2-channel-(t1041))
- [Ultra-Pro High-Fidelity Network Service Discovery (T1046)](#ultra-pro-high-fidelity-network-service-discovery-(t1046))
- [Suspicious Remote Process Creation via WMIC](#suspicious-remote-process-creation-via-wmic)
- [Ultra-Pro High-Fidelity Alternative Protocol Exfiltration (T1048)](#ultra-pro-high-fidelity-alternative-protocol-exfiltration-(t1048))
- [Ultra-Pro High-Fidelity Symmetric Encrypted Exfiltration (T1048.001)](#ultra-pro-high-fidelity-symmetric-encrypted-exfiltration-(t1048001))
- [Ultra-Pro High-Fidelity Asymmetric Encrypted Exfiltration (T1048.002)](#ultra-pro-high-fidelity-asymmetric-encrypted-exfiltration-(t1048002))
- [Ultra-Pro High-Fidelity Unencrypted Protocol Exfil (T1048.003)](#ultra-pro-high-fidelity-unencrypted-protocol-exfil-(t1048003))
- [Ultra-Pro High-Fidelity System Network Connections Discovery (T1049)](#ultra-pro-high-fidelity-system-network-connections-discovery-(t1049))
- [Ultra-Pro High-Fidelity Physical Medium Exfiltration (T1052)](#ultra-pro-high-fidelity-physical-medium-exfiltration-(t1052))
- [Ultra-Pro High-Fidelity USB Exfiltration (T1052.001)](#ultra-pro-high-fidelity-usb-exfiltration-(t1052001))
- [Gyanús ütemezett feladat vagy munkakör létrehozása a Persistence (T1053) miatt](#gyanús-ütemezett-feladat-vagy-munkakör-létrehozása-a-persistence-(t1053)-miatt)
- [High-Fidelity At.exe Activity Detection](#high-fidelity-atexe-activity-detection)
- [High-Fidelity Cron Persistence and In-Place Modification](#high-fidelity-cron-persistence-and-in-place-modification)
- [Suspicious Scheduled Task Creation Executing PowerShell](#suspicious-scheduled-task-creation-executing-powershell)
- [High-Fidelity Systemd Service Creation or Modification](#high-fidelity-systemd-service-creation-or-modification)
- [High-Fidelity Systemd Timer Persistence Detection](#high-fidelity-systemd-timer-persistence-detection)
- [Ultra-Pro Stealthy Process Injection Detection (T1055)](#ultra-pro-stealthy-process-injection-detection-(t1055))
- [Ultra-Pro Stealthy DLL Injection (T1055.001)](#ultra-pro-stealthy-dll-injection-(t1055001))
- [Ultra-Pro Stealthy PE Injection (T1055.002)](#ultra-pro-stealthy-pe-injection-(t1055002))
- [Ultra-Pro Stealthy Thread Hijacking (T1055.003)](#ultra-pro-stealthy-thread-hijacking-(t1055003))
- [Ultra-Pro Stealthy APC Injection (T1055.004)](#ultra-pro-stealthy-apc-injection-(t1055004))
- [Ultra-Pro Stealthy TLS Injection (T1055.005)](#ultra-pro-stealthy-tls-injection-(t1055005))
- [Ultra-Pro Stealthy Ptrace Injection (T1055.008)](#ultra-pro-stealthy-ptrace-injection-(t1055008))
- [Ultra-Pro Stealthy Module Overwriting (T1055.009)](#ultra-pro-stealthy-module-overwriting-(t1055009))
- [Ultra-Pro Stealthy EWM Injection (T1055.011)](#ultra-pro-stealthy-ewm-injection-(t1055011))
- [Ultra-Pro Stealthy Process Hollowing (T1055.012)](#ultra-pro-stealthy-process-hollowing-(t1055012))
- [Ultra-Pro Stealthy Process Hollowing (T1055.013)](#ultra-pro-stealthy-process-hollowing-(t1055013))
- [Ultra-Pro Stealthy Process Ghosting (T1055.014)](#ultra-pro-stealthy-process-ghosting-(t1055014))
- [Ultra-Pro Stealthy ListPlanting Injection (T1055.015)](#ultra-pro-stealthy-listplanting-injection-(t1055015))
- [Ultra-Pro High-Fidelity Input Capture Detection (T1056)](#ultra-pro-high-fidelity-input-capture-detection-(t1056))
- [Ultra-Pro High-Fidelity Keylogging & Input Hooking (T1056.001)](#ultra-pro-high-fidelity-keylogging-&-input-hooking-(t1056001))
- [Ultra-Pro High-Fidelity GUI Input Capture (T1056.002)](#ultra-pro-high-fidelity-gui-input-capture-(t1056002))
- [Ultra-Pro High-Fidelity Digital Certificate Theft (T1056.003)](#ultra-pro-high-fidelity-digital-certificate-theft-(t1056003))
- [Suspicious Credential API Hooking via Win32 Libraries](#suspicious-credential-api-hooking-via-win32-libraries)
- [Ultra-Pro High-Fidelity Process Discovery (T1057)](#ultra-pro-high-fidelity-process-discovery-(t1057))
- [High-Fidelity Scripting Interpreter Contextual Anomaly](#high-fidelity-scripting-interpreter-contextual-anomaly)
- [Suspicious Encoded PowerShell Command Execution](#suspicious-encoded-powershell-command-execution)
- [High-Fidelity AppleScript (osascript) Abuse Detection](#high-fidelity-applescript-(osascript)-abuse-detection)
- [Advanced Windows Command Shell Contextual Anomaly](#advanced-windows-command-shell-contextual-anomaly)
- [High-Fidelity Unix Shell Abuse and Reverse Shell Detection](#high-fidelity-unix-shell-abuse-and-reverse-shell-detection)
- [High-Fidelity VBScript Contextual Anomaly Detection](#high-fidelity-vbscript-contextual-anomaly-detection)
- [High-Fidelity Python Interpreter Abuse Detection](#high-fidelity-python-interpreter-abuse-detection)
- [High-Fidelity JScript Interpreter Contextual Anomaly](#high-fidelity-jscript-interpreter-contextual-anomaly)
- [High-Fidelity Network Device CLI Manipulation](#high-fidelity-network-device-cli-manipulation)
- [High-Fidelity Cloud Shell Exploitation and Data Exfiltration](#high-fidelity-cloud-shell-exploitation-and-data-exfiltration)
- [Suspicious SYSTEM Process Spawned from User Context](#suspicious-system-process-spawned-from-user-context)
- [Ultra-Pro High-Fidelity Permission Groups Discovery (T1069)](#ultra-pro-high-fidelity-permission-groups-discovery-(t1069))
- [Ultra-Pro High-Fidelity Local Group Discovery (T1069.001)](#ultra-pro-high-fidelity-local-group-discovery-(t1069001))
- [Ultra-Pro High-Fidelity Domain Group Discovery (T1069.002)](#ultra-pro-high-fidelity-domain-group-discovery-(t1069002))
- [Ultra-Pro High-Fidelity Cloud Groups Discovery (T1069.003)](#ultra-pro-high-fidelity-cloud-groups-discovery-(t1069003))
- [Ultra-Pro High-Fidelity Indicator Removal on Host (T1070)](#ultra-pro-high-fidelity-indicator-removal-on-host-(t1070))
- [Security Event Log Cleared Using wevtutil.exe](#security-event-log-cleared-using-wevtutilexe)
- [Ultra-Pro High-Fidelity Linux Log Clearing and Journal Sabotage (T1070.002)](#ultra-pro-high-fidelity-linux-log-clearing-and-journal-sabotage-(t1070002))
- [Ultra-Pro High-Fidelity Mailbox Data Clearing and Rule Sabotage (T1070.003)](#ultra-pro-high-fidelity-mailbox-data-clearing-and-rule-sabotage-(t1070003))
- [Ultra-Pro High-Fidelity Forensic Artifact and File Deletion (T1070.004)](#ultra-pro-high-fidelity-forensic-artifact-and-file-deletion-(t1070004))
- [Ultra-Pro High-Fidelity Network Share and Credential Removal (T1070.005)](#ultra-pro-high-fidelity-network-share-and-credential-removal-(t1070005))
- [Ultra-Pro High-Fidelity Timestomp and MACE Attribute Manipulation (T1070.006)](#ultra-pro-high-fidelity-timestomp-and-mace-attribute-manipulation-(t1070006))
- [Ultra-Pro High-Fidelity Network History and RDP Trace Removal (T1070.007)](#ultra-pro-high-fidelity-network-history-and-rdp-trace-removal-(t1070007))
- [Ultra-Pro High-Fidelity Email Storage and Database Destruction (T1070.008)](#ultra-pro-high-fidelity-email-storage-and-database-destruction-(t1070008))
- [Ultra-Pro High-Fidelity Persistence Artifact Removal (T1070.009)](#ultra-pro-high-fidelity-persistence-artifact-removal-(t1070009))
- [Ultra-Pro High-Fidelity Application Layer C2 Anomaly (T1071)](#ultra-pro-high-fidelity-application-layer-c2-anomaly-(t1071))
- [Ultra-Pro High-Fidelity HTTP/S C2 Anomaly (T1071.001)](#ultra-pro-high-fidelity-https-c2-anomaly-(t1071001))
- [Ultra-Pro High-Fidelity FTP/SFTP Protocol Anomaly (T1071.002)](#ultra-pro-high-fidelity-ftpsftp-protocol-anomaly-(t1071002))
- [Ultra-Pro High-Fidelity Mail Protocol Anomaly (T1071.003)](#ultra-pro-high-fidelity-mail-protocol-anomaly-(t1071003))
- [Ultra-Pro High-Fidelity DNS Tunneling & Beaconing (T1071.004)](#ultra-pro-high-fidelity-dns-tunneling-&-beaconing-(t1071004))
- [High-Fidelity Software Deployment Tool Abuse Detection](#high-fidelity-software-deployment-tool-abuse-detection)
- [Ultra-Pro High-Fidelity Data Staging Anomaly (T1074)](#ultra-pro-high-fidelity-data-staging-anomaly-(t1074))
- [Ultra-Pro High-Fidelity Local Data Staging Anomaly (T1074.001)](#ultra-pro-high-fidelity-local-data-staging-anomaly-(t1074001))
- [Ultra-Pro High-Fidelity Remote Data Staging (T1074.002)](#ultra-pro-high-fidelity-remote-data-staging-(t1074002))
- [High-Fidelity Anomalous Logon via Valid Account](#high-fidelity-anomalous-logon-via-valid-account)
- [High-Fidelity Default Account Abuse Detection](#high-fidelity-default-account-abuse-detection)
- [High-Fidelity Domain Account Lateral Movement Anomaly](#high-fidelity-domain-account-lateral-movement-anomaly)
- [High-Fidelity Local Account Remote Access Detection](#high-fidelity-local-account-remote-access-detection)
- [High-Fidelity Cloud Account Compromise (Entra ID)](#high-fidelity-cloud-account-compromise-(entra-id))
- [Ultra-Pro High-Fidelity Taint Shared Content (T1080)](#ultra-pro-high-fidelity-taint-shared-content-(t1080))
- [Ultra-Pro High-Fidelity System Information Discovery (T1082)](#ultra-pro-high-fidelity-system-information-discovery-(t1082))
- [Ultra-Pro High-Fidelity File and Directory Discovery (T1083)](#ultra-pro-high-fidelity-file-and-directory-discovery-(t1083))
- [Suspicious Use of net user or net localgroup via cmd.exe](#suspicious-use-of-net-user-or-net-localgroup-via-cmdexe)
- [Ultra-Pro High-Fidelity Local Account Discovery (T1087.001)](#ultra-pro-high-fidelity-local-account-discovery-(t1087001))
- [Ultra-Pro High-Fidelity Domain Account Discovery (T1087.002)](#ultra-pro-high-fidelity-domain-account-discovery-(t1087002))
- [Ultra-Pro High-Fidelity Email Account Discovery (T1087.003)](#ultra-pro-high-fidelity-email-account-discovery-(t1087003))
- [Ultra-Pro High-Fidelity Cloud Account Discovery (T1087.004)](#ultra-pro-high-fidelity-cloud-account-discovery-(t1087004))
- [Ultra-Pro High-Fidelity Proxy & Pivot Point Detection (T1090)](#ultra-pro-high-fidelity-proxy-&-pivot-point-detection-(t1090))
- [Ultra-Pro High-Fidelity Internal Proxy & Pivot Detection (T1090.001)](#ultra-pro-high-fidelity-internal-proxy-&-pivot-detection-(t1090001))
- [Ultra-Pro High-Fidelity External Proxy & Tunneling (T1090.002)](#ultra-pro-high-fidelity-external-proxy-&-tunneling-(t1090002))
- [Ultra-Pro High-Fidelity Multi-hop Proxy & Tor Detection (T1090.003)](#ultra-pro-high-fidelity-multi-hop-proxy-&-tor-detection-(t1090003))
- [Ultra-Pro High-Fidelity Domain Fronting Detection (T1090.004)](#ultra-pro-high-fidelity-domain-fronting-detection-(t1090004))
- [High-Fidelity Process Execution from Removable Media](#high-fidelity-process-execution-from-removable-media)
- [Ultra-Pro High-Fidelity Removable Media C2 Anomaly (T1071.002 / T1092)](#ultra-pro-high-fidelity-removable-media-c2-anomaly-(t1071002--t1092))
- [Ultra-Pro High-Fidelity Non-Application Layer C2 (T1095)](#ultra-pro-high-fidelity-non-application-layer-c2-(t1095))
- [High-Fidelity Account Manipulation - Persistence Focused](#high-fidelity-account-manipulation---persistence-focused)
- [High-Fidelity Entra ID Application Credential Addition](#high-fidelity-entra-id-application-credential-addition)
- [High-Fidelity Exchange Mailbox Permission Grant (T1098.002)](#high-fidelity-exchange-mailbox-permission-grant-(t1098002))
- [High-Fidelity Entra ID App Certificate Addition](#high-fidelity-entra-id-app-certificate-addition)
- [High-Fidelity Azure Role Assignment Escalation](#high-fidelity-azure-role-assignment-escalation)
- [High-Fidelity Device Registration Persistence (T1098.005)](#high-fidelity-device-registration-persistence-(t1098005))
- [High-Fidelity MFA Method Addition](#high-fidelity-mfa-method-addition)
- [Ultra-Pro High-Fidelity Web Service C2 (T1102)](#ultra-pro-high-fidelity-web-service-c2-(t1102))
- [Ultra-Pro High-Fidelity Dead Drop Resolver (T1102.001)](#ultra-pro-high-fidelity-dead-drop-resolver-(t1102001))
- [Ultra-Pro High-Fidelity Bidirectional Cloud C2 (T1102.002)](#ultra-pro-high-fidelity-bidirectional-cloud-c2-(t1102002))
- [Ultra-Pro High-Fidelity One-Way Web Service C2 (T1102.003)](#ultra-pro-high-fidelity-one-way-web-service-c2-(t1102003))
- [Ultra-Pro High-Fidelity Multi-Stage C2 (T1104)](#ultra-pro-high-fidelity-multi-stage-c2-(t1104))
- [Suspicious Use of Built-in Windows Tools for File Download and Code Execution](#suspicious-use-of-built-in-windows-tools-for-file-download-and-code-execution)
- [High-Fidelity Native API Abuse via LOLBins](#high-fidelity-native-api-abuse-via-lolbins)
- [Ultra-Pro High-Fidelity Brute Force & Tooling (T1110)](#ultra-pro-high-fidelity-brute-force-&-tooling-(t1110))
- [Multiple Failed Login Attempts for Single User (Possible Password Guessing)](#multiple-failed-login-attempts-for-single-user-(possible-password-guessing))
- [Ultra-Pro High-Fidelity Credential Export & Cracking (T1110.002)](#ultra-pro-high-fidelity-credential-export-&-cracking-(t1110002))
- [Ultra-Pro High-Fidelity Password Spraying (T1110.003)](#ultra-pro-high-fidelity-password-spraying-(t1110003))
- [Ultra-Pro High-Fidelity Credential Stuffing & Combo-list Abuse (T1110.004)](#ultra-pro-high-fidelity-credential-stuffing-&-combo-list-abuse-(t1110004))
- [Ultra-Pro High-Fidelity MFA Evasion & Session Hijacking (T1111)](#ultra-pro-high-fidelity-mfa-evasion-&-session-hijacking-(t1111))
- [Ultra-Pro High-Fidelity Registry Tampering for Evasion (T1112)](#ultra-pro-high-fidelity-registry-tampering-for-evasion-(t1112))
- [Ultra-Pro High-Fidelity Screen Capture Anomaly (T1113)](#ultra-pro-high-fidelity-screen-capture-anomaly-(t1113))
- [Ultra-Pro High-Fidelity Email Harvesting Anomaly (T1114)](#ultra-pro-high-fidelity-email-harvesting-anomaly-(t1114))
- [Ultra-Pro High-Fidelity Local Email Harvesting Anomaly (T1114.001)](#ultra-pro-high-fidelity-local-email-harvesting-anomaly-(t1114001))
- [Ultra-Pro High-Fidelity Remote Email Export Anomaly (T1114.002)](#ultra-pro-high-fidelity-remote-email-export-anomaly-(t1114002))
- [Ultra-Pro High-Fidelity Email Forwarding Rule Anomaly (T1114.003)](#ultra-pro-high-fidelity-email-forwarding-rule-anomaly-(t1114003))
- [Ultra-Pro High-Fidelity Clipboard Data Spying (T1115)](#ultra-pro-high-fidelity-clipboard-data-spying-(t1115))
- [Ultra-Pro High-Fidelity Automated Collection (T1119)](#ultra-pro-high-fidelity-automated-collection-(t1119))
- [Ultra-Pro High-Fidelity Peripheral Device Discovery (T1120)](#ultra-pro-high-fidelity-peripheral-device-discovery-(t1120))
- [Ultra-Pro High-Fidelity Audio Capture & Spying (T1123)](#ultra-pro-high-fidelity-audio-capture-&-spying-(t1123))
- [Ultra-Pro High-Fidelity System Time Discovery (T1124)](#ultra-pro-high-fidelity-system-time-discovery-(t1124))
- [Ultra-Pro High-Fidelity Video Capture Anomaly (T1125)](#ultra-pro-high-fidelity-video-capture-anomaly-(t1125))
- [Ultra-Pro High-Fidelity Trusted Developer Utility Proxy (T1127)](#ultra-pro-high-fidelity-trusted-developer-utility-proxy-(t1127))
- [Ultra-Pro High-Fidelity MSBuild Proxy Execution (T1127.001)](#ultra-pro-high-fidelity-msbuild-proxy-execution-(t1127001))
- [High-Fidelity Shared Module Load from Untrusted Path](#high-fidelity-shared-module-load-from-untrusted-path)
- [Ultra-Pro High-Fidelity Data Encoding & Obfuscation (T1132)](#ultra-pro-high-fidelity-data-encoding-&-obfuscation-(t1132))
- [Ultra-Pro High-Fidelity Standard Encoding & Payload Injection (T1132.001)](#ultra-pro-high-fidelity-standard-encoding-&-payload-injection-(t1132001))
- [Ultra-Pro High-Fidelity Non-Standard Encoding & XOR Obfuscation (T1132.002)](#ultra-pro-high-fidelity-non-standard-encoding-&-xor-obfuscation-(t1132002))
- [Anomalous External Remote Service Access Context](#anomalous-external-remote-service-access-context)
- [Ultra-Pro Access Token Manipulation & Impersonation (T1134)](#ultra-pro-access-token-manipulation-&-impersonation-(t1134))
- [Ultra-Pro Token Impersonation via LSASS Handle Duplication (T1134.001)](#ultra-pro-token-impersonation-via-lsass-handle-duplication-(t1134001))
- [Ultra-Pro Create Process with Token (T1134.002)](#ultra-pro-create-process-with-token-(t1134002))
- [Ultra-Pro Make and Impersonate Token (T1134.003)](#ultra-pro-make-and-impersonate-token-(t1134003))
- [Ultra-Pro Parent PID Spoofing & Process Tree Violation (T1134.004)](#ultra-pro-parent-pid-spoofing-&-process-tree-violation-(t1134004))
- [Ultra-Pro SID-History Injection & DS Manipulation (T1134.005)](#ultra-pro-sid-history-injection-&-ds-manipulation-(t1134005))
- [Ultra-Pro High-Fidelity Network Share Discovery (T1135)](#ultra-pro-high-fidelity-network-share-discovery-(t1135))
- [Ultra-Pro Unauthorized Account Creation (T1136)](#ultra-pro-unauthorized-account-creation-(t1136))
- [Ultra-Pro Unauthorized Local Account Creation (T1136.001)](#ultra-pro-unauthorized-local-account-creation-(t1136001))
- [Ultra-Pro Unauthorized Domain Account Creation (T1136.002)](#ultra-pro-unauthorized-domain-account-creation-(t1136002))
- [Ultra-Pro Unauthorized Cloud Account Creation (T1136.003)](#ultra-pro-unauthorized-cloud-account-creation-(t1136003))
- [Ultra-Pro Office Application Startup Persistence (T1137)](#ultra-pro-office-application-startup-persistence-(t1137))
- [Suspicious Modification of Office Global Template (Normal.dotm)](#suspicious-modification-of-office-global-template-(normaldotm))
- [Ultra-Pro Office Test DLL Persistence (T1137.002)](#ultra-pro-office-test-dll-persistence-(t1137002))
- [Ultra-Pro Outlook Custom Forms Persistence (T1137.003)](#ultra-pro-outlook-custom-forms-persistence-(t1137003))
- [Ultra-Pro Outlook Home Page Hijacking & Bypass (T1137.004)](#ultra-pro-outlook-home-page-hijacking-&-bypass-(t1137004))
- [Ultra-Pro Office Security Policy Tampering (T1137.005)](#ultra-pro-office-security-policy-tampering-(t1137005))
- [Ultra-Pro Office Add-in Binary Persistence (T1137.006)](#ultra-pro-office-add-in-binary-persistence-(t1137006))
- [Ultra-Pro Stealthy Deobfuscation/Decoding (T1140)](#ultra-pro-stealthy-deobfuscationdecoding-(t1140))
- [Ultra-Pro Browser Extension Force-Install Persistence (T1176)](#ultra-pro-browser-extension-force-install-persistence-(t1176))
- [Ultra-Pro High-Fidelity Browser Session Hijacking (T1185)](#ultra-pro-high-fidelity-browser-session-hijacking-(t1185))
- [Ultra-Pro High-Fidelity Forced Authentication (T1187)](#ultra-pro-high-fidelity-forced-authentication-(t1187))
- [Browser-Originating Shell or System Tool Execution](#browser-originating-shell-or-system-tool-execution)
- [Suspicious Cross-Site Scripting (XSS) Attempt Detected on Web Server](#suspicious-cross-site-scripting-(xss)-attempt-detected-on-web-server)
- [High-Fidelity Supply Chain Compromise Detection (Post-Update Anomaly)](#high-fidelity-supply-chain-compromise-detection-(post-update-anomaly))
- [High-Fidelity Dependency Poisoning Detection](#high-fidelity-dependency-poisoning-detection)
- [High-Fidelity Compromised Binary Activity (Post-Update)](#high-fidelity-compromised-binary-activity-(post-update))
- [High-Fidelity Hardware/Firmware Manipulation Detection](#high-fidelity-hardwarefirmware-manipulation-detection)
- [Suspicious File Download via Bitsadmin (High Fidelity)](#suspicious-file-download-via-bitsadmin-(high-fidelity))
- [High-Fidelity Trusted Relationship Abuse Detection](#high-fidelity-trusted-relationship-abuse-detection)
- [Malicious Hardware-Induced Command Execution (HID Injection)](#malicious-hardware-induced-command-execution-(hid-injection))
- [Ultra-Pro High-Fidelity Password Policy Discovery (T1201)](#ultra-pro-high-fidelity-password-policy-discovery-(t1201))
- [Ultra-Pro High-Fidelity Indirect Command Execution (T1202)](#ultra-pro-high-fidelity-indirect-command-execution-(t1202))
- [High-Fidelity Client-Side Exploitation and Shell Spawning](#high-fidelity-client-side-exploitation-and-shell-spawning)
- [Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity)](#suspicious-child-process-spawned-by-microsoft-office-application-(high-fidelity))
- [High-Fidelity User Execution of Malicious Link (T1204.001)](#high-fidelity-user-execution-of-malicious-link-(t1204001))
- [High-Fidelity User Execution of Malicious File](#high-fidelity-user-execution-of-malicious-file)
- [High-Fidelity Execution from Mounted Virtual Disk (T1204.003)](#high-fidelity-execution-from-mounted-virtual-disk-(t1204003))
- [Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel](#adathalászat-rosszindulatú-linken-keresztül-domain-és-feladó-rendellenességekkel)
- [Ultra-Pro Traffic Signaling & Port Knocking (T1205)](#ultra-pro-traffic-signaling-&-port-knocking-(t1205))
- [Ultra-Pro Port Knocking & Raw Socket Listener (T1205.001)](#ultra-pro-port-knocking-&-raw-socket-listener-(t1205001))
- [Ultra-Pro Socket Filter & WFP Traffic Signaling (T1205.002)](#ultra-pro-socket-filter-&-wfp-traffic-signaling-(t1205002))
- [Ultra-Pro High-Fidelity Rogue DC Topology Manipulation (T1207)](#ultra-pro-high-fidelity-rogue-dc-topology-manipulation-(t1207))
- [Ultra-Pro High-Fidelity Exploitation of Remote Services (T1210)](#ultra-pro-high-fidelity-exploitation-of-remote-services-(t1210))
- [Ultra-Pro High-Fidelity Privilege Escalation Exploitation (T1211)](#ultra-pro-high-fidelity-privilege-escalation-exploitation-(t1211))
- [Ultra-Pro High-Fidelity Credential Service Exploitation (T1212)](#ultra-pro-high-fidelity-credential-service-exploitation-(t1212))
- [Ultra-Pro High-Fidelity Repository Dump (T1213)](#ultra-pro-high-fidelity-repository-dump-(t1213))
- [Ultra-Pro High-Fidelity Confluence Scraping (T1213.001)](#ultra-pro-high-fidelity-confluence-scraping-(t1213001))
- [Ultra-Pro High-Fidelity SharePoint Mass Data Exfiltration (T1213.002)](#ultra-pro-high-fidelity-sharepoint-mass-data-exfiltration-(t1213002))
- [Ultra-Pro High-Fidelity Knowledge Base Scraping (T1213.003)](#ultra-pro-high-fidelity-knowledge-base-scraping-(t1213003))
- [Ultra-Pro High-Fidelity System Script Proxy Execution (T1216)](#ultra-pro-high-fidelity-system-script-proxy-execution-(t1216))
- [Ultra-Pro High-Fidelity Pubprn Script Proxy Execution (T1216.001)](#ultra-pro-high-fidelity-pubprn-script-proxy-execution-(t1216001))
- [Ultra-Pro High-Fidelity Browser Information Discovery (T1217)](#ultra-pro-high-fidelity-browser-information-discovery-(t1217))
- [Ultra-Pro High-Fidelity System Binary Proxy Execution (T1218)](#ultra-pro-high-fidelity-system-binary-proxy-execution-(t1218))
- [Ultra-Pro High-Fidelity HH.exe Proxy Execution (T1218.001)](#ultra-pro-high-fidelity-hhexe-proxy-execution-(t1218001))
- [Ultra-Pro High-Fidelity Control.exe Proxy Execution (T1218.002)](#ultra-pro-high-fidelity-controlexe-proxy-execution-(t1218002))
- [Ultra-Pro High-Fidelity MsiExec Proxy Execution (T1218.003)](#ultra-pro-high-fidelity-msiexec-proxy-execution-(t1218003))
- [Ultra-Pro High-Fidelity InstallUtil Proxy Execution (T1218.004)](#ultra-pro-high-fidelity-installutil-proxy-execution-(t1218004))
- [Suspicious Mshta Execution of Remote Script (High Fidelity)](#suspicious-mshta-execution-of-remote-script-(high-fidelity))
- [Suspicious Msiexec Installation from Remote URL (High Fidelity)](#suspicious-msiexec-installation-from-remote-url-(high-fidelity))
- [Ultra-Pro High-Fidelity Odbcconf Proxy Execution (T1218.008)](#ultra-pro-high-fidelity-odbcconf-proxy-execution-(t1218008))
- [Ultra-Pro High-Fidelity Regsvcs/Regasm Proxy Execution (T1218.009)](#ultra-pro-high-fidelity-regsvcsregasm-proxy-execution-(t1218009))
- [Suspicious Regsvr32 Execution Indicative of LOLBAS Abuse (High Fidelity)](#suspicious-regsvr32-execution-indicative-of-lolbas-abuse-(high-fidelity))
- [Suspicious Rundll32 Execution with Script or Remote Payload (High Fidelity)](#suspicious-rundll32-execution-with-script-or-remote-payload-(high-fidelity))
- [Ultra-Pro High-Fidelity Verclsid Proxy Execution (T1218.012)](#ultra-pro-high-fidelity-verclsid-proxy-execution-(t1218012))
- [Ultra-Pro High-Fidelity Rundll32 Proxy Execution (T1218.013)](#ultra-pro-high-fidelity-rundll32-proxy-execution-(t1218013))
- [Ultra-Pro High-Fidelity MMC Proxy Execution (T1218.014)](#ultra-pro-high-fidelity-mmc-proxy-execution-(t1218014))
- [Suspicious Use of Legitimate Remote Administration Tools Outside Enterprise Pattern](#suspicious-use-of-legitimate-remote-administration-tools-outside-enterprise-pattern)
- [Ultra-Pro High-Fidelity XSL Script Processing (T1220)](#ultra-pro-high-fidelity-xsl-script-processing-(t1220))
- [Ultra-Pro High-Fidelity Office Template Injection (T1221)](#ultra-pro-high-fidelity-office-template-injection-(t1221))
- [Ultra-Pro High-Fidelity Permissions Modification (T1222)](#ultra-pro-high-fidelity-permissions-modification-(t1222))
- [Ultra-Pro High-Fidelity Windows File Permissions Modification (T1222.001)](#ultra-pro-high-fidelity-windows-file-permissions-modification-(t1222001))
- [Ultra-Pro High-Fidelity Linux File Permissions Modification (T1222.002)](#ultra-pro-high-fidelity-linux-file-permissions-modification-(t1222002))
- [Ultra-Pro High-Fidelity Execution Guardrails Discovery (T1480)](#ultra-pro-high-fidelity-execution-guardrails-discovery-(t1480))
- [Ultra-Pro Environmental Keying Discovery (T1480.001)](#ultra-pro-environmental-keying-discovery-(t1480001))
- [Ultra-Pro High-Fidelity Domain Trust Discovery (T1482)](#ultra-pro-high-fidelity-domain-trust-discovery-(t1482))
- [Ultra-Pro Domain Policy Manipulation & GPO Abuse (T1484)](#ultra-pro-domain-policy-manipulation-&-gpo-abuse-(t1484))
- [Ultra-Pro Group Policy Modification & Abuse (T1484.001)](#ultra-pro-group-policy-modification-&-abuse-(t1484001))
- [Ultra-Pro Domain Trust Tampering & SID Filtering Bypass (T1484.002)](#ultra-pro-domain-trust-tampering-&-sid-filtering-bypass-(t1484002))
- [Ultra-Pro High-Fidelity Data Destruction (T1485)](#ultra-pro-high-fidelity-data-destruction-(t1485))
- [Ransomware Preparation Activity Detected on Windows Host (High Fidelity)](#ransomware-preparation-activity-detected-on-windows-host-(high-fidelity))
- [Ultra-Pro High-Fidelity Service Stop (T1489)](#ultra-pro-high-fidelity-service-stop-(t1489))
- [Suspicious Deletion of Volume Shadow Copies via VSSAdmin (High Fidelity)](#suspicious-deletion-of-volume-shadow-copies-via-vssadmin-(high-fidelity))
- [Ultra-Pro High-Fidelity Defacement (T1491)](#ultra-pro-high-fidelity-defacement-(t1491))
- [Ultra-Pro High-Fidelity Internal Defacement (T1491.001)](#ultra-pro-high-fidelity-internal-defacement-(t1491001))
- [Ultra-Pro High-Fidelity External Defacement (T1491.002)](#ultra-pro-high-fidelity-external-defacement-(t1491002))
- [Ultra-Pro High-Fidelity Firmware Corruption (T1495)](#ultra-pro-high-fidelity-firmware-corruption-(t1495))
- [Ultra-Pro High-Fidelity Resource Hijacking (T1496)](#ultra-pro-high-fidelity-resource-hijacking-(t1496))
- [Ultra-Pro High-Fidelity Virtualization/Sandbox Evasion (T1497)](#ultra-pro-high-fidelity-virtualizationsandbox-evasion-(t1497))
- [Ultra-Pro High-Fidelity VM Artifact Discovery (T1497.001)](#ultra-pro-high-fidelity-vm-artifact-discovery-(t1497001))
- [Ultra-Pro High-Fidelity User Interaction Evasion (T1497.002)](#ultra-pro-high-fidelity-user-interaction-evasion-(t1497002))
- [Ultra-Pro High-Fidelity Time-based Evasion (T1497.003)](#ultra-pro-high-fidelity-time-based-evasion-(t1497003))
- [Ultra-Pro High-Fidelity Network DoS (T1498)](#ultra-pro-high-fidelity-network-dos-(t1498))
- [Direct Flow Flood (T1498.001)](#direct-flow-flood-(t1498001))
- [Endpoint Denial of Service (T1499)](#endpoint-denial-of-service-(t1499))
- [OS Self-Destruction Detection (T1499.001)](#os-self-destruction-detection-(t1499001))
- [Service Exhaustion Detection (T1499.002)](#service-exhaustion-detection-(t1499002))
- [OS Self-Destruction Detection (T1499.003)](#os-self-destruction-detection-(t1499003))
- [Resource Exhaustion Detection (T1499.004)](#resource-exhaustion-detection-(t1499004))
- [Web Shell Execution Patterns (T1505)](#web-shell-execution-patterns-(t1505))
- [SQL Server Command Shell Execution (T1505.001)](#sql-server-command-shell-execution-(t1505001))
- [IIS Native Module Injection (T1505.002)](#iis-native-module-injection-(t1505002))
- [Webshell Upload or Interaction Detection (T1505.003)](#webshell-upload-or-interaction-detection-(t1505003))
- [Mainboard Boot Image & SPI Flash Tampering (T1505.004)](#mainboard-boot-image-&-spi-flash-tampering-(t1505004))
- [Terminal Services DLL Hijacking Detection (T1505.005)](#terminal-services-dll-hijacking-detection-(t1505005))
- [Software Discovery Detection (T1518)](#software-discovery-detection-(t1518))
- [Security Software Discovery Detection (T1518.001)](#security-software-discovery-detection-(t1518001))
- [Exploit-Grade Unauthorized Container Image Execution (Implant Container Image)](#exploit-grade-unauthorized-container-image-execution-(implant-container-image))
- [Cloud Service Discovery Detection (T1526)](#cloud-service-discovery-detection-(t1526))
- [Application Token & Session Hijacking Detection (T1528)](#application-token-&-session-hijacking-detection-(t1528))
- [Unauthorized System Shutdown/Reboot Detection (T1529)](#unauthorized-system-shutdownreboot-detection-(t1529))
- [Cloud Storage Data Theft Detection (T1530)](#cloud-storage-data-theft-detection-(t1530))
- [Account Access Removal Detection (T1531)](#account-access-removal-detection-(t1531))
- [Internal Spearphishing Detection (T1534)](#internal-spearphishing-detection-(t1534))
- [Unused Service Manipulation Detection (T1535)](#unused-service-manipulation-detection-(t1535))
- [Cloud Account Exfiltration Detection (T1537)](#cloud-account-exfiltration-detection-(t1537))
- [Cloud Service Dashboard Discovery (T1538)](#cloud-service-dashboard-discovery-(t1538))
- [Web Browser Session Cookie & Credential Theft Detection (T1539)](#web-browser-session-cookie-&-credential-theft-detection-(t1539))
- [Pre-OS Boot Manipulation (T1542)](#pre-os-boot-manipulation-(t1542))
- [ROM Kit & UEFI Firmware Tampering (T1542.001)](#rom-kit-&-uefi-firmware-tampering-(t1542001))
- [Component Firmware Tampering (T1542.002)](#component-firmware-tampering-(t1542002))
- [Bootkit Persistence & EFI Tampering (T1542.003)](#bootkit-persistence-&-efi-tampering-(t1542003))
- [Mainboard Boot Image & SPI Flash Tampering (T1542.004)](#mainboard-boot-image-&-spi-flash-tampering-(t1542004))
- [DHCP/PXE Boot Hijacking (T1542.005)](#dhcppxe-boot-hijacking-(t1542005))
- [Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services](#non-admin-user-attempting-to-stop-or-modify-multiple-sensitive-windows-services)
- [Ultra-Pro macOS Launch Agent Persistence Detection (T1543.001)](#ultra-pro-macos-launch-agent-persistence-detection-(t1543001))
- [Ultra-Pro Systemd Service Persistence (T1543.002)](#ultra-pro-systemd-service-persistence-(t1543002))
- [Ultra-Pro Unauthorized Windows Service Installation (T1543.003)](#ultra-pro-unauthorized-windows-service-installation-(t1543003))
- [Ultra-Pro Unauthorized macOS Launch Daemon (T1543.004)](#ultra-pro-unauthorized-macos-launch-daemon-(t1543004))
- [Ultra-Pro WMI Event Subscription Persistence (T1546.003)](#ultra-pro-wmi-event-subscription-persistence-(t1546003))
- [Ultra-Pro File Association Hijacking (T1546.001)](#ultra-pro-file-association-hijacking-(t1546001))
- [Ultra-Pro Screensaver Persistence Detection (T1546.002)](#ultra-pro-screensaver-persistence-detection-(t1546002))
- [WMI Event Subscription Persistence via WMIC or PowerShell (High Fidelity)](#wmi-event-subscription-persistence-via-wmic-or-powershell-(high-fidelity))
- [Ultra-Pro AppCert DLL Persistence Detection (T1546.004)](#ultra-pro-appcert-dll-persistence-detection-(t1546004))
- [Ultra-Pro Shell Trap Persistence Detection (T1546.005)](#ultra-pro-shell-trap-persistence-detection-(t1546005))
- [Ultra-Pro Mach-O LC_LOAD_DYLIB Injection (T1546.006)](#ultra-pro-mach-o-lc_load_dylib-injection-(t1546006))
- [Ultra-Pro Netsh Helper DLL Persistence (T1546.007)](#ultra-pro-netsh-helper-dll-persistence-(t1546007))
- [Ultra-Pro WER SilentProcessExit Persistence (T1546.008)](#ultra-pro-wer-silentprocessexit-persistence-(t1546008))
- [Ultra-Pro AppInit_DLLs Persistence Detection (T1546.009)](#ultra-pro-appinit_dlls-persistence-detection-(t1546009))
- [Ultra-Pro AppCert DLL Persistence Detection (T1546.010)](#ultra-pro-appcert-dll-persistence-detection-(t1546010))
- [Ultra-Pro Application Shimming Persistence Detection (T1546.011)](#ultra-pro-application-shimming-persistence-detection-(t1546011))
- [Ultra-Pro IFEO Debugger Hijacking Detection (T1546.012)](#ultra-pro-ifeo-debugger-hijacking-detection-(t1546012))
- [Ultra-Pro PowerShell Profile Injection Detection (T1546.013)](#ultra-pro-powershell-profile-injection-detection-(t1546013))
- [Ultra-Pro WMI Event Subscription Persistence (T1546.014)](#ultra-pro-wmi-event-subscription-persistence-(t1546014))
- [Suspicious COM Hijacking for User-Level Persistence (High Fidelity)](#suspicious-com-hijacking-for-user-level-persistence-(high-fidelity))
- [Ultra-Pro MSI Installer Custom Action Persistence (T1546.016)](#ultra-pro-msi-installer-custom-action-persistence-(t1546016))
- [Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása](#gyanús-rendszerindítási-vagy-bejelentkezési-automatikus-indítás-végrehajtása)
- [Suspicious Registry Run Key Modification for User Persistence (High Fidelity)](#suspicious-registry-run-key-modification-for-user-persistence-(high-fidelity))
- [High-Fidelity LSA Authentication Package Persistence](#high-fidelity-lsa-authentication-package-persistence)
- [High-Fidelity Time Provider Persistence (T1547.003)](#high-fidelity-time-provider-persistence-(t1547003))
- [High-Fidelity Winlogon Helper DLL Persistence (T1547.004)](#high-fidelity-winlogon-helper-dll-persistence-(t1547004))
- [High-Fidelity SSP DLL Persistence (T1547.005)](#high-fidelity-ssp-dll-persistence-(t1547005))
- [High-Fidelity Kernel Driver Registration (T1547.006)](#high-fidelity-kernel-driver-registration-(t1547006))
- [High-Fidelity Browser Session Persistence (T1547.007)](#high-fidelity-browser-session-persistence-(t1547007))
- [High-Fidelity LSASS Driver/Package Persistence (T1547.008)](#high-fidelity-lsass-driverpackage-persistence-(t1547008))
- [High-Fidelity Shortcut Modification Detection](#high-fidelity-shortcut-modification-detection)
- [High-Fidelity AppCert DLL Persistence (T1547.010)](#high-fidelity-appcert-dll-persistence-(t1547010))
- [High-Fidelity Application Shimming Persistence (T1547.011)](#high-fidelity-application-shimming-persistence-(t1547011))
- [High-Fidelity COM Hijacking Persistence (T1547.012)](#high-fidelity-com-hijacking-persistence-(t1547012))
- [High-Fidelity Email Client Helper Persistence (T1547.013)](#high-fidelity-email-client-helper-persistence-(t1547013))
- [High-Fidelity Active Setup Persistence (T1547.014)](#high-fidelity-active-setup-persistence-(t1547014))
- [High-Fidelity COM Hijacking Persistence (T1547.015)](#high-fidelity-com-hijacking-persistence-(t1547015))
- [Privilege Escalation via Registry Hijacking (T1548)](#privilege-escalation-via-registry-hijacking-(t1548))
- [Setuid/Setgid Bit Manipulation (T1548.001)](#setuidsetgid-bit-manipulation-(t1548001))
- [UAC Bypass via Fodhelper Registry Hijack (High Fidelity)](#uac-bypass-via-fodhelper-registry-hijack-(high-fidelity))
- [Sudoers Manipulation and Sudo Abuse (T1548.003)](#sudoers-manipulation-and-sudo-abuse-(t1548003))
- [AppleScript Privilege Escalation (T1548.004)](#applescript-privilege-escalation-(t1548004))
- [SUID Desktop Entry & Shortcut Abuse (T1548.005)](#suid-desktop-entry-&-shortcut-abuse-(t1548005))
- [Alternate Authentication Material (T1550)](#alternate-authentication-material-(t1550))
- [Application Access Token Abuse (T1550.001)](#application-access-token-abuse-(t1550001))
- [Pass-the-Hash Detection (T1550.002)](#pass-the-hash-detection-(t1550002))
- [Pass-the-Ticket Detection (T1550.003)](#pass-the-ticket-detection-(t1550003))
- [Pass-the-Session Detection (T1550.004)](#pass-the-session-detection-(t1550004))
- [Unsecured Credentials Discovery (T1552)](#unsecured-credentials-discovery-(t1552))
- [Credentials In Files Discovery (T1552.001)](#credentials-in-files-discovery-(t1552001))
- [Credentials In Registry Discovery (T1552.002)](#credentials-in-registry-discovery-(t1552002))
- [Shell History & Console Discovery (T1552.003)](#shell-history-&-console-discovery-(t1552003))
- [Private Key Discovery (T1552.004)](#private-key-discovery-(t1552004))
- [Cloud Credential Discovery (T1552.005)](#cloud-credential-discovery-(t1552005))
- [Credentials in Files Discovery (T1552.006)](#credentials-in-files-discovery-(t1552006))
- [Container Secret Discovery (T1552.007)](#container-secret-discovery-(t1552007))
- [GPP Password Discovery (T1552.008)](#gpp-password-discovery-(t1552008))
- [Subvert Trust Controls (T1553)](#subvert-trust-controls-(t1553))
- [macOS Gatekeeper and Quarantine Bypass (T1553.001)](#macos-gatekeeper-and-quarantine-bypass-(t1553001))
- [SIP Hijacking and Trust Subversion (T1553.002)](#sip-hijacking-and-trust-subversion-(t1553002))
- [Windows Catalog Database Subversion (T1553.003)](#windows-catalog-database-subversion-(t1553003))
- [Root Certificate Injection (T1553.004)](#root-certificate-injection-(t1553004))
- [Mark-of-the-Web (MotW) Bypass & Zone Subversion Detection (T1553.005)](#mark-of-the-web-(motw)-bypass-&-zone-subversion-detection-(t1553005))
- [Windows Code Integrity & DSE Subversion Detection (T1553.006)](#windows-code-integrity-&-dse-subversion-detection-(t1553006))
- [Ultra-Pro Client Binary Integrity Compromise (T1554)](#ultra-pro-client-binary-integrity-compromise-(t1554))
- [Nem böngészős folyamat hozzáférése a böngésző hitelesítőadat-tárolóihoz (High Fidelity)](#nem-böngészős-folyamat-hozzáférése-a-böngésző-hitelesítőadat-tárolóihoz-(high-fidelity))
- [Windows Vault Credential Harvesting Detection (T1555.001)](#windows-vault-credential-harvesting-detection-(t1555001))
- [Securityd Memory Dumping Detection (T1555.002)](#securityd-memory-dumping-detection-(t1555002))
- [Browser Credential Harvesting Detection (T1555.003)](#browser-credential-harvesting-detection-(t1555003))
- [Windows Credential Manager Harvesting Detection (T1555.004)](#windows-credential-manager-harvesting-detection-(t1555004))
- [Password Manager Extraction Detection (T1555.005)](#password-manager-extraction-detection-(t1555005))
- [Cloud Secret Harvesting Detection (T1555.006)](#cloud-secret-harvesting-detection-(t1555006))
- [Exploit-Grade Authentication Process Hijack via Suspicious DLL Registration](#exploit-grade-authentication-process-hijack-via-suspicious-dll-registration)
- [Exploit-Grade Security Support Provider Hijacking (LSA SSP)](#exploit-grade-security-support-provider-hijacking-(lsa-ssp))
- [Exploit-Grade Password Filter DLL Hijacking via LSA Notification Packages](#exploit-grade-password-filter-dll-hijacking-via-lsa-notification-packages)
- [Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003)](#ultra-pro-pam-integrity-hijacking-&-backdoor-(t1556003))
- [Ultra-Pro Network Device Authentication Hijacking (T1556.004)](#ultra-pro-network-device-authentication-hijacking-(t1556004))
- [Ultra-Pro SID History Injection Correlation (T1556.005)](#ultra-pro-sid-history-injection-correlation-(t1556005))
- [Ultra-Pro Entra ID MFA Method Hijacking (T1556.006)](#ultra-pro-entra-id-mfa-method-hijacking-(t1556006))
- [Hybrid Identity Sync Manipulation Detection (T1556.007)](#hybrid-identity-sync-manipulation-detection-(t1556007))
- [Network-to-Cloud Auth Hijacking Detection (T1556.008)](#network-to-cloud-auth-hijacking-detection-(t1556008))
- [Adversary-in-the-Middle Detection (T1557)](#adversary-in-the-middle-detection-(t1557))
- [LLMNR/NBT-NS Poisoning & SMB Relay Detection (T1557.001)](#llmnrnbt-ns-poisoning-&-smb-relay-detection-(t1557001))
- [Rogue ARP Poisoning / MITM Detection (T1557.002)](#rogue-arp-poisoning--mitm-detection-(t1557002))
- [Rogue DHCP / DHCP Spoofing Detection (T1557.003)](#rogue-dhcp--dhcp-spoofing-detection-(t1557003))
- [Kerberos Attack Detection](#kerberos-attack-detection)
- [Golden Ticket Forgery & Injection](#golden-ticket-forgery-&-injection)
- [Silver Ticket Forgery & Injection](#silver-ticket-forgery-&-injection)
- [Gyanús Kerberos TGS jegykérés (Kerberoasting)](#gyanús-kerberos-tgs-jegykérés-(kerberoasting))
- [Ultra-Pro High-Fidelity AS-REP Roasting & LDAP Enumeration](#ultra-pro-high-fidelity-as-rep-roasting-&-ldap-enumeration)
- [High-Fidelity Indirect IPC and COM Execution](#high-fidelity-indirect-ipc-and-com-execution)
- [Gyanús elnevezett csővezeték-létrehozás, amely utólagos kihasználási eszközökhöz kapcsolódik (High Fidelity)](#gyanús-elnevezett-csővezeték-létrehozás-amely-utólagos-kihasználási-eszközökhöz-kapcsolódik-(high-fidelity))
- [High-Fidelity Office DDE Contextual Anomaly](#high-fidelity-office-dde-contextual-anomaly)
- [High-Fidelity Hypervisor API and VM Escape Research](#high-fidelity-hypervisor-api-and-vm-escape-research)
- [Adatok gyanús archiválása exfiltráció céljából](#adatok-gyanús-archiválása-exfiltráció-céljából)
- [Data Archiving for Exfiltration](#data-archiving-for-exfiltration)
- [Data Archiving via Library](#data-archiving-via-library)
- [Archive via Custom Method](#archive-via-custom-method)
- [Disk Wipe](#disk-wipe)
- [Disk Content Wipe](#disk-content-wipe)
- [Disk Structure Wipe](#disk-structure-wipe)
- [Biztonsági szolgáltatások gyanús leállítása](#biztonsági-szolgáltatások-gyanús-leállítása)
- [Windows Defender védelem kikapcsolása vagy módosítása PowerShell segítségével](#windows-defender-védelem-kikapcsolása-vagy-módosítása-powershell-segítségével)
- [Windows Event Log Service Impairment](#windows-event-log-service-impairment)
- [Command History Logging Impairment](#command-history-logging-impairment)
- [Suspicious Firewall Modification via Netsh.exe](#suspicious-firewall-modification-via-netshexe)
- [Indicator Blocking and Telemetry Suppression](#indicator-blocking-and-telemetry-suppression)
- [Cloud Firewall Impairment (T1562.007)](#cloud-firewall-impairment-(t1562007))
- [Cloud Logging Impairment (T1562.008)](#cloud-logging-impairment-(t1562008))
- [Safe Mode Defense Evasion (T1562.009)](#safe-mode-defense-evasion-(t1562009))
- [Defense Downgrade Attack (T1562.010)](#defense-downgrade-attack-(t1562010))
- [Virtualization and Sandbox Evasion (T1564.011)](#virtualization-and-sandbox-evasion-(t1564011))
- [Cloud Security Infrastructure Impairment (T1562.012)](#cloud-security-infrastructure-impairment-(t1562012))
- [Remote Service Session Hijacking (T1563)](#remote-service-session-hijacking-(t1563))
- [Local Session Hijacking (T1563.001)](#local-session-hijacking-(t1563001))
- [RDP Session Hijacking (T1563.002)](#rdp-session-hijacking-(t1563002))
- [Hide Artifacts Detection (T1564)](#hide-artifacts-detection-(t1564))
- [Hidden File Attribute Manipulation (T1564.001)](#hidden-file-attribute-manipulation-(t1564001))
- [Hidden User Account Creation (T1564.002)](#hidden-user-account-creation-(t1564002))
- [Hidden Window Execution (T1564.003)](#hidden-window-execution-(t1564003))
- [NTFS Alternative Data Stream (ADS) Abuse (T1564.004)](#ntfs-alternative-data-stream-(ads)-abuse-(t1564004))
- [Hidden File System Manipulation (T1564.005)](#hidden-file-system-manipulation-(t1564005))
- [Virtual Instance Execution Abuse (T1564.006)](#virtual-instance-execution-abuse-(t1564006))
- [VBA Macro Security Evasion (T1564.007)](#vba-macro-security-evasion-(t1564007))
- [Email Hiding Rules Detection (T1564.008)](#email-hiding-rules-detection-(t1564008))
- [Resource Extraction and Abuse (T1564.009)](#resource-extraction-and-abuse-(t1564009))
- [Process Argument Spoofing Detection (T1564.010)](#process-argument-spoofing-detection-(t1564010))
- [Virtual Instance Abuse (T1564.011)](#virtual-instance-abuse-(t1564011))
- [Data Manipulation (T1565)](#data-manipulation-(t1565))
- [Stored Data Manipulation (T1565.001)](#stored-data-manipulation-(t1565001))
- [Transmitted Data Manipulation (T1565.002)](#transmitted-data-manipulation-(t1565002))
- [Runtime Process Manipulation (T1565.003)](#runtime-process-manipulation-(t1565003))
- [High-Fidelity Phishing Payload Execution from Communication Apps](#high-fidelity-phishing-payload-execution-from-communication-apps)
- [High-Fidelity Spearphishing Attachment Execution](#high-fidelity-spearphishing-attachment-execution)
- [High-Fidelity Browser-Originating Payload Execution](#high-fidelity-browser-originating-payload-execution)
- [High-Fidelity Process Spawn from Business Communication Service](#high-fidelity-process-spawn-from-business-communication-service)
- [High-Fidelity Detection of Post-Vishing Remote Tool Execution](#high-fidelity-detection-of-post-vishing-remote-tool-execution)
- [Web Service Exfiltration (T1567)](#web-service-exfiltration-(t1567))
- [Code Repository Exfil (T1567.001)](#code-repository-exfil-(t1567001))
- [Cloud Storage Exfil (T1567.002)](#cloud-storage-exfil-(t1567002))
- [Video Hosting Exfil (T1567.003)](#video-hosting-exfil-(t1567003))
- [Text Storage Exfil (T1567.004)](#text-storage-exfil-(t1567004))
- [Dynamic Resolution & DGA (T1568)](#dynamic-resolution-&-dga-(t1568))
- [Fast Flux & DNS Cache Evasion (T1568.001)](#fast-flux-&-dns-cache-evasion-(t1568001))
- [Domain Generation Algorithm (DGA) Detection (T1568.002)](#domain-generation-algorithm-(dga)-detection-(t1568002))
- [DNS Calculation & Extraction (T1568.003)](#dns-calculation-&-extraction-(t1568003))
- [High-Fidelity System Service Execution Detection](#high-fidelity-system-service-execution-detection)
- [High-Fidelity Launch Daemon Persistence Detection](#high-fidelity-launch-daemon-persistence-detection)
- [High-Fidelity System Service Execution Detection (T1569.002)](#high-fidelity-system-service-execution-detection-(t1569002))
- [Lateral Tool Transfer (T1570)](#lateral-tool-transfer-(t1570))
- [Non-Standard Port C2 (T1571)](#non-standard-port-c2-(t1571))
- [Protocol Tunneling Detection (T1572)](#protocol-tunneling-detection-(t1572))
- [Encrypted C2 Channel (T1573)](#encrypted-c2-channel-(t1573))
- [Symmetric Encryption C2 Channel (T1573.001)](#symmetric-encryption-c2-channel-(t1573001))
- [Asymmetric Encryption C2 (T1573.002)](#asymmetric-encryption-c2-(t1573002))
- [Ultra-Pro DLL Hijacking & Side-Loading Detection (T1574)](#ultra-pro-dll-hijacking-&-side-loading-detection-(t1574))
- [Ultra-Pro DLL Search Order Hijacking Detection (T1574.001)](#ultra-pro-dll-search-order-hijacking-detection-(t1574001))
- [Ultra-Pro DLL Side-Loading Integrity Gap Detection (T1574.002)](#ultra-pro-dll-side-loading-integrity-gap-detection-(t1574002))
- [Ultra-Pro Shell Configuration & Path Interception (T1574.003)](#ultra-pro-shell-configuration-&-path-interception-(t1574003))
- [Ultra-Pro Library Search Order Hijacking & Integrity Gap (T1574.004)](#ultra-pro-library-search-order-hijacking-&-integrity-gap-(t1574004))
- [Ultra-Pro Installer File Permissions Weakness (T1574.005)](#ultra-pro-installer-file-permissions-weakness-(t1574005))
- [Dynamic Linker Hijacking Against Privileged Binary](#dynamic-linker-hijacking-against-privileged-binary)
- [PATH Hijacking Leading to Privileged Binary Execution](#path-hijacking-leading-to-privileged-binary-execution)
- [.NET Assembly Search Order Hijacking via User-Writable Directory](#net-assembly-search-order-hijacking-via-user-writable-directory)
- [.NET AppDomainManager Hijacking via Non-GAC Assembly](#net-appdomainmanager-hijacking-via-non-gac-assembly)
- [Privileged Service Executable Overwritten from User-Writable Location](#privileged-service-executable-overwritten-from-user-writable-location)
- [Privileged Service ImagePath or ServiceDll Hijacked via Registry](#privileged-service-imagepath-or-servicedll-hijacked-via-registry)
- [Exploit-Grade COR_PROFILER Hijacking via User-Writable Profiler DLL](#exploit-grade-cor_profiler-hijacking-via-user-writable-profiler-dll)
- [Exploit-Grade KernelCallbackTable Manipulation](#exploit-grade-kernelcallbacktable-manipulation)
- [Cloud Infrastructure Tampering (T1578)](#cloud-infrastructure-tampering-(t1578))
- [Suspicious Cloud Instance Creation (T1578.001)](#suspicious-cloud-instance-creation-(t1578001))
- [Cloud Snapshot Exfiltration (T1578.002)](#cloud-snapshot-exfiltration-(t1578002))
- [Cloud Instance Destruction (T1578.003)](#cloud-instance-destruction-(t1578003))
- [Cloud Image Tampering (T1578.004)](#cloud-image-tampering-(t1578004))
- [Cloud Network Security Regression (T1578.005)](#cloud-network-security-regression-(t1578005))
- [Cloud Infrastructure Discovery (T1580)](#cloud-infrastructure-discovery-(t1580))
- [High-Fidelity Offensive Infrastructure Provisioning - T1583](#high-fidelity-offensive-infrastructure-provisioning---t1583)
- [High-Fidelity VPS Infrastructure Provisioning - T1583.001](#high-fidelity-vps-infrastructure-provisioning---t1583001)
- [High-Fidelity Automated Domain Registration & Acquisition - T1583.002](#high-fidelity-automated-domain-registration-&-acquisition---t1583002)
- [High-Fidelity Cloud Network (VPC) Provisioning - T1583.003](#high-fidelity-cloud-network-(vpc)-provisioning---t1583003)
- [High-Fidelity Serverless Infrastructure Provisioning - T1583.004](#high-fidelity-serverless-infrastructure-provisioning---t1583004)
- [High-Fidelity Botnet Infrastructure Acquisition - T1583.005](#high-fidelity-botnet-infrastructure-acquisition---t1583005)
- [High-Fidelity Web Service Acquisition and Provisioning - T1583.006](#high-fidelity-web-service-acquisition-and-provisioning---t1583006)
- [High-Fidelity Serverless Infrastructure Provisioning - T1583.007](#high-fidelity-serverless-infrastructure-provisioning---t1583007)
- [High-Fidelity Cloud Account Acquisition and Bootstrap - T1583.008](#high-fidelity-cloud-account-acquisition-and-bootstrap---t1583008)
- [High-Fidelity Compromised Infrastructure and Resource Abuse - T1584](#high-fidelity-compromised-infrastructure-and-resource-abuse---t1584)
- [High-Fidelity Domain Infrastructure Hijacking - T1584.001](#high-fidelity-domain-infrastructure-hijacking---t1584001)
- [High-Fidelity DNS Server Configuration Subversion - T1584.002](#high-fidelity-dns-server-configuration-subversion---t1584002)
- [High-Fidelity Cloud Identity Subversion and Persistence - T1584.003](#high-fidelity-cloud-identity-subversion-and-persistence---t1584003)
- [High-Fidelity Serverless Function Subversion - T1584.004](#high-fidelity-serverless-function-subversion---t1584004)
- [High-Fidelity Botnet Agent Persistence and Control - T1584.005](#high-fidelity-botnet-agent-persistence-and-control---t1584005)
- [High-Fidelity Web Service and Cloud Storage Subversion - T1584.006](#high-fidelity-web-service-and-cloud-storage-subversion---t1584006)
- [High-Fidelity VPS Control and Tunneling - T1584.007](#high-fidelity-vps-control-and-tunneling---t1584007)
- [Suspicious User Account Creation via CLI/Scripting](#suspicious-user-account-creation-via-cliscripting)
- [Potential Automated Social Media Account Establishment](#potential-automated-social-media-account-establishment)
- [Stealthy Email Account Establishment and Manipulation](#stealthy-email-account-establishment-and-manipulation)
- [Anomalous Cloud User Account Creation](#anomalous-cloud-user-account-creation)
- [High-Fidelity Account Compromise and Identity Manipulation - T1586](#high-fidelity-account-compromise-and-identity-manipulation---t1586)
- [High-Fidelity Automated Social Media Manipulation - T1586.001](#high-fidelity-automated-social-media-manipulation---t1586001)
- [High-Fidelity Email Forwarding Rule Manipulation - T1586.002](#high-fidelity-email-forwarding-rule-manipulation---t1586002)
- [High-Fidelity Cloud Account Takeover and Persistence - T1586.003](#high-fidelity-cloud-account-takeover-and-persistence---t1586003)
- [High-Fidelity Offensive Capability Development and Compilation - T1587](#high-fidelity-offensive-capability-development-and-compilation---t1587)
- [High-Fidelity Malware Development and Evasion Patterns - T1587.001](#high-fidelity-malware-development-and-evasion-patterns---t1587001)
- [High-Fidelity Unauthorized Code Signing Capability Development - T1587.002](#high-fidelity-unauthorized-code-signing-capability-development---t1587002)
- [High-Fidelity Unauthorized Digital Certificate Development - T1587.003](#high-fidelity-unauthorized-digital-certificate-development---t1587003)
- [High-Fidelity Exploit Development and Compilation Detection - T1587.004](#high-fidelity-exploit-development-and-compilation-detection---t1587004)
- [Anomalous Procurement of Offensive Capabilities](#anomalous-procurement-of-offensive-capabilities)
- [Anomalous Procurement of Malware Capabilities](#anomalous-procurement-of-malware-capabilities)
- [Anomalous Offensive Tool Acquisition via CLI](#anomalous-offensive-tool-acquisition-via-cli)
- [Anomalous Code Signing Certificate Export or Acquisition](#anomalous-code-signing-certificate-export-or-acquisition)
- [Strategic Trusted Root Certificate Store Manipulation](#strategic-trusted-root-certificate-store-manipulation)
- [Anomalous Procurement of Exploit or PoC Code](#anomalous-procurement-of-exploit-or-poc-code)
- [Targeted Harvesting of Vulnerability Research Artifacts](#targeted-harvesting-of-vulnerability-research-artifacts)
- [High-Fidelity Identity Enumeration via Authentication Endpoints](#high-fidelity-identity-enumeration-via-authentication-endpoints)
- [Credential Enumeration via Authentication API (High Confidence)](#credential-enumeration-via-authentication-api-(high-confidence))
- [High-Confidence OSINT Identity Enumeration via Public APIs](#high-confidence-osint-identity-enumeration-via-public-apis)
- [Targeted OSINT Enumeration of Open Websites and Domains](#targeted-osint-enumeration-of-open-websites-and-domains)
- [Network Reconnaissance with High Port Diversity](#network-reconnaissance-with-high-port-diversity)
- [Professional IP Infrastructure Reconnaissance - T1590.001](#professional-ip-infrastructure-reconnaissance---t1590001)
- [Advanced DNS Infrastructure Reconnaissance - T1590.002](#advanced-dns-infrastructure-reconnaissance---t1590002)
- [Advanced Network Trust Dependencies Reconnaissance - T1590.003](#advanced-network-trust-dependencies-reconnaissance---t1590003)
- [Advanced Certificate Information Reconnaissance - T1590.004](#advanced-certificate-information-reconnaissance---t1590004)
- [Advanced Cloud Infrastructure Reconnaissance - T1590.005](#advanced-cloud-infrastructure-reconnaissance---t1590005)
- [Advanced Victim Web Page Info Reconnaissance - T1590.006](#advanced-victim-web-page-info-reconnaissance---t1590006)
- [Advanced Organizational Infrastructure Enumeration - T1591](#advanced-organizational-infrastructure-enumeration---t1591)
- [Advanced Physical Location Infrastructure Enumeration - T1591.001](#advanced-physical-location-infrastructure-enumeration---t1591001)
- [Advanced Business Relationship Information Discovery - T1591.002](#advanced-business-relationship-information-discovery---t1591002)
- [Advanced Knowledge Management Discovery - T1591.003](#advanced-knowledge-management-discovery---t1591003)
- [High-Fidelity Personnel Information Discovery - T1591.004](#high-fidelity-personnel-information-discovery---t1591004)
- [High-Fidelity Host Information Reconnaissance Activity](#high-fidelity-host-information-reconnaissance-activity)
- [High-Confidence Hardware Enumeration via Management Interfaces](#high-confidence-hardware-enumeration-via-management-interfaces)
- [Advanced Software Enumeration Reconnaissance via Web Endpoints](#advanced-software-enumeration-reconnaissance-via-web-endpoints)
- [High-Confidence Firmware Enumeration Against Network Devices](#high-confidence-firmware-enumeration-against-network-devices)
- [High-Confidence Client Configuration Fingerprinting (Reconnaissance)](#high-confidence-client-configuration-fingerprinting-(reconnaissance))
- [High-Fidelity Automated Web Reconnaissance - T1593](#high-fidelity-automated-web-reconnaissance---t1593)
- [High-Fidelity Social Media Entity Harvesting - T1593.001](#high-fidelity-social-media-entity-harvesting---t1593001)
- [High-Fidelity Automated Search Engine Reconnaissance - T1593.002](#high-fidelity-automated-search-engine-reconnaissance---t1593002)
- [High-Fidelity Social Media Entity Harvesting - T1593.003](#high-fidelity-social-media-entity-harvesting---t1593003)
- [High-Fidelity Information Repository Reconnaissance - T1594](#high-fidelity-information-repository-reconnaissance---t1594)
- [High-Fidelity Active Scanning Detection (Behavior-Based)](#high-fidelity-active-scanning-detection-(behavior-based))
- [High-Fidelity External IP Block Scanning Detection](#high-fidelity-external-ip-block-scanning-detection)
- [High-Confidence External Vulnerability Scanning Activity](#high-confidence-external-vulnerability-scanning-activity)
- [Active Wordlist Scanning Against Authentication Endpoints](#active-wordlist-scanning-against-authentication-endpoints)
- [High-Fidelity Open Technical Database Reconnaissance - T1596](#high-fidelity-open-technical-database-reconnaissance---t1596)
- [High-Fidelity WHOIS Database Reconnaissance - T1596.001](#high-fidelity-whois-database-reconnaissance---t1596001)
- [High-Fidelity Automated Search Engine Dorking - T1596.002](#high-fidelity-automated-search-engine-dorking---t1596002)
- [High-Fidelity Passive DNS Reconnaissance - T1597.003](#high-fidelity-passive-dns-reconnaissance---t1597003)
- [High-Fidelity Digital Certificate Reconnaissance - T1596.004](#high-fidelity-digital-certificate-reconnaissance---t1596004)
- [High-Fidelity IP Infrastructure Reconnaissance - T1596.005](#high-fidelity-ip-infrastructure-reconnaissance---t1596005)
- [High-Fidelity Victim-Owned Website Reconnaissance - T1597](#high-fidelity-victim-owned-website-reconnaissance---t1597)
- [High-Fidelity Domain Infrastructure Enumeration - T1597.001](#high-fidelity-domain-infrastructure-enumeration---t1597001)
- [High-Fidelity Secret Hunting in Code Repositories - T1597.002](#high-fidelity-secret-hunting-in-code-repositories---t1597002)
- [Advanced Phishing for Info & Credential Harvesting - T1598](#advanced-phishing-for-info-&-credential-harvesting---t1598)
- [Advanced Spearphishing Link Redirection - T1598.001](#advanced-spearphishing-link-redirection---t1598001)
- [Advanced BEC Mail & Financial Data Exfiltration - T1598.002](#advanced-bec-mail-&-financial-data-exfiltration---t1598002)
- [High-Fidelity MFA/OTP Spoofing & Harvesting - T1598.003](#high-fidelity-mfaotp-spoofing-&-harvesting---t1598003)
- [High-Fidelity Spearphishing Attachment Interaction - T1598.004](#high-fidelity-spearphishing-attachment-interaction---t1598004)
- [Network Boundary Bridging (T1599)](#network-boundary-bridging-(t1599))
- [Logical Isolation Bypass (T1599.001)](#logical-isolation-bypass-(t1599001))
- [Weaken Encryption Attempt (T1600)](#weaken-encryption-attempt-(t1600))
- [System Image Patching (T1600.001)](#system-image-patching-(t1600001))
- [Disable Entity Verification (T1600.002)](#disable-entity-verification-(t1600002))
- [Network OS Image Modification (T1601)](#network-os-image-modification-(t1601))
- [Network Binary Patching (T1601.001)](#network-binary-patching-(t1601001))
- [Ultra-Pro High-Fidelity Malicious Network OS Upgrade (T1601.002)](#ultra-pro-high-fidelity-malicious-network-os-upgrade-(t1601002))
- [Network Share Automated Collection (T1602)](#network-share-automated-collection-(t1602))
- [Admin Share Data Exfiltration (T1602.001)](#admin-share-data-exfiltration-(t1602001))
- [Ultra-Pro High-Fidelity Cloud Share Exfiltration (T1602.002)](#ultra-pro-high-fidelity-cloud-share-exfiltration-(t1602002))
- [Ultra-Pro High-Fidelity Web Token & Credential Forgery (T1606)](#ultra-pro-high-fidelity-web-token-&-credential-forgery-(t1606))
- [Ultra-Pro High-Fidelity Web Cookie & Browser Credential Harvesting (T1606.001)](#ultra-pro-high-fidelity-web-cookie-&-browser-credential-harvesting-(t1606001))
- [Ultra-Pro High-Fidelity Web Token Forgery & Golden SAML (T1606.002)](#ultra-pro-high-fidelity-web-token-forgery-&-golden-saml-(t1606002))
- [Anomalous Infrastructure Staging and Resource Deployment](#anomalous-infrastructure-staging-and-resource-deployment)
- [Anomalous Malware Staging to External Infrastructure](#anomalous-malware-staging-to-external-infrastructure)
- [Anomalous Offensive Tool Staging and External Upload](#anomalous-offensive-tool-staging-and-external-upload)
- [Strategic Digital Certificate Staging in Trusted Root Store](#strategic-digital-certificate-staging-in-trusted-root-store)
- [Anomalous Web Content Modification for Drive-by Staging](#anomalous-web-content-modification-for-drive-by-staging)
- [Strategic Staging of Malicious Link Targets](#strategic-staging-of-malicious-link-targets)
- [Anomalous SEO Poisoning and Metadata Staging](#anomalous-seo-poisoning-and-metadata-staging)
- [High-Fidelity Container Interactive Shell Execution](#high-fidelity-container-interactive-shell-execution)
- [High-Fidelity Malicious Container Deployment Detection](#high-fidelity-malicious-container-deployment-detection)
- [Ultra-Pro Container Escape & Host Access (T1611)](#ultra-pro-container-escape-&-host-access-(t1611))
- [Ultra-Pro Stealthy Local Image Build (T1612)](#ultra-pro-stealthy-local-image-build-(t1612))
- [Ultra-Pro High-Fidelity Container and Kubernetes Discovery](#ultra-pro-high-fidelity-container-and-kubernetes-discovery)
- [High-Fidelity System Location and Regional Kill-Switch Discovery](#high-fidelity-system-location-and-regional-kill-switch-discovery)
- [High-Fidelity System Language and Keyboard Layout Discovery](#high-fidelity-system-language-and-keyboard-layout-discovery)
- [High-Fidelity Group Policy Discovery Detection](#high-fidelity-group-policy-discovery-detection)
- [High-Fidelity Cloud Storage Object Discovery Detection](#high-fidelity-cloud-storage-object-discovery-detection)
- [High-Fidelity Reflective Code Loading and In-Memory Assembly Execution](#high-fidelity-reflective-code-loading-and-in-memory-assembly-execution)
- [Suspicious MFA Prompt Bombing or Authentication Flood Automation](#suspicious-mfa-prompt-bombing-or-authentication-flood-automation)
- [Suspicious Anti-Debug API Access From Unbacked or User-Space Memory](#suspicious-anti-debug-api-access-from-unbacked-or-user-space-memory)
- [Suspicious macOS LaunchAgent or LaunchDaemon Plist Modification](#suspicious-macos-launchagent-or-launchdaemon-plist-modification)
- [High-Fidelity Serverless Function Persistence or Abuse](#high-fidelity-serverless-function-persistence-or-abuse)
- [Suspicious Certificate and Private Key Export or Theft Activity](#suspicious-certificate-and-private-key-export-or-theft-activity)
- [High-Fidelity Cloud Account Acquisition and Initialization - T1650](#high-fidelity-cloud-account-acquisition-and-initialization---t1650)
- [High-Fidelity Cloud Administration Agent Abuse](#high-fidelity-cloud-administration-agent-abuse)
- [Suspicious Device Driver Enumeration From Anomalous Context (BYOVD Recon)](#suspicious-device-driver-enumeration-from-anomalous-context-(byovd-recon))
- [Ultra-Pro Power Settings Manipulation (T1137.001)](#ultra-pro-power-settings-manipulation-(t1137001))
- [Suspicious Event Log Enumeration from Anomalous Execution Context](#suspicious-event-log-enumeration-from-anomalous-execution-context)
- [Suspicious Impersonation via RunAs Abuse or Deceptive Local Account Creation](#suspicious-impersonation-via-runas-abuse-or-deceptive-local-account-creation)
- [Suspicious Clipboard Manipulation and Financial Document Access From Untrusted Parent Process](#suspicious-clipboard-manipulation-and-financial-document-access-from-untrusted-parent-process)
- [Professional Content Impersonation and Infrastructure Mirroring](#professional-content-impersonation-and-infrastructure-mirroring)
- [Suspicious Access to LSASS Process Memory (Credential Dumping Attempt)](#suspicious-access-to-lsass-process-memory-(credential-dumping-attempt))

---
## Ultra-Pro High-Fidelity Steganography & Data Reconstruction (T1001)
- **ID:** `T1001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects data de-steganography by identifying anomalous programmatic access 
to image manipulation APIs (GDI+, System.Drawing) from script interpreters, 
specifically looking for pixel-level data extraction routines.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Junk Data & Command Padding (T1001.001)
- **ID:** `T1001_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects command padding and junk data injection by identifying anomalous 
white-space distribution, repetitive environmental variable definitions, 
and extreme command line lengths in non-installer processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Steganography & Data Reconstruction (T1001.002)
- **ID:** `T1001_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects data de-steganography by identifying anomalous programmatic access 
to image manipulation APIs (GDI+, System.Drawing) from script interpreters, 
specifically looking for pixel-level data extraction routines.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Protocol Impersonation (T1001.003)
- **ID:** `T1001_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects protocol impersonation by identifying manual manipulation of network headers 
and anomalous User-Agent strings within script interpreters, specifically 
targeting attempts to mimic mobile devices or search crawlers from non-browser processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity LSASS Credential Dumping (T1003)
- **ID:** `T1003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects highly sophisticated LSASS memory dumping techniques. 
Focuses on DLL export ordinals (#24), handle duplication, 
and specialized LOLBins that bypass standard EDR string-based detection.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Access to LSASS Process Memory
- **ID:** `T1003_001.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Észleli a gyanús hozzáférést az LSASS folyamat memóriájához, ami hitelesítő adatok ellopására (Credential Dumping) utalhat.  A szabály figyeli a gyanús GrantedAccess maszkokat és szűri a gyakori legális folyamatokat.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity SAM & SYSTEM Registry Theft (T1003.002)
- **ID:** `T1003_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized extraction of the SAM, SYSTEM, and SECURITY registry hives. 
Focuses on 'reg.exe' abuse, VSS-based theft, and 'esentutl.exe' file copying 
from non-standard parent processes and untrusted execution paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity NTDS.dit Extraction (T1003.003)
- **ID:** `T1003_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [DISKSHADOW.EXE](https://lolbas-project.github.io/lolbas/), [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [NTDSUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized extraction of the Active Directory database (NTDS.dit).
Identifies 'ntdsutil' with abbreviated commands, diskshadow scripts, 
and shadow copy creation by non-backup processes on Domain Controllers.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity LSA Secrets & Security Hive Theft (T1003.004)
- **ID:** `T1003_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized extraction of LSA Secrets from the HKLM\SECURITY registry hive. 
Focuses on advanced export patterns, Impacket-style remote dumps, and 
credential access via untrusted parent processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity MSCASH/DCC Extraction (T1003.005)
- **ID:** `T1003_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized extraction of Cached Domain Credentials (MSCASH/DCC).
Monitors for specialized tool fingerprints, registry save operations targeting 
the Cache key, and anomalous parent-child process relationships.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity DCSync Attack Detection (T1003.006)
- **ID:** `T1003_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects DCSync attacks where an attacker impersonates a Domain Controller 
to request credentials. Focuses on specific RPC flags, abbreviated tool commands, 
and anomalous process lineage on non-DC assets.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity LSASS Memory Dump & LOLBin Abuse (T1003.007)
- **ID:** `T1003_007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects sophisticated LSASS memory dumping. Focuses on Procdump argument patterns, 
Task Manager-initiated dumps via WerFault, and COM+ (comsvcs.dll) exports using 
ordinal-based calls (#24) to bypass string-based detection.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Linux Shadow File Extraction (T1003.008)
- **ID:** `T1003_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized extraction of the /etc/shadow file. 
Focuses on redirection to suspicious paths, archiving, 
and exfiltration via network tools (LOLBins) from interactive shells.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Local Data Harvesting (T1005)
- **ID:** `T1005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic local data collection by identifying the combination of 
recursive file discovery, targeted sensitive extensions, and the use of 
non-standard search tools or suspicious process lineages.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy Direct Volume Access (T1006)
- **ID:** `T1006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-fidelity direct volume access by monitoring for raw device paths 
initiated by non-system processes or suspicious parents, often used to bypass 
file system locks and EDR monitoring for credential dumping.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity System Service Discovery (T1007)
- **ID:** `T1007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted discovery of system services. Focuses on suspicious parent processes 
and specific command-line arguments used to identify security products or 
misconfigured services for privilege escalation.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Fallback Channel Detection (T1008)
- **ID:** `T1008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects C2 fallback mechanisms by identifying cross-protocol switching logic 
(e.g., HTTP to DNS/ICMP) within exception handling blocks (try/catch/trap) 
triggered by connection failures in non-standard process contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Application Window Discovery (T1010)
- **ID:** `T1010.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized application window discovery by monitoring for .NET 
MainWindowTitle property access and Win32 API calls via CLI. 
Focuses on non-standard lineages and output redirection used by malware to exfiltrate window titles.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Bluetooth Exfiltration (T1011)
- **ID:** `T1011.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized Bluetooth data exfiltration by identifying programmatic 
triggers of Bluetooth transfer wizards (fsquirt.exe) from non-standard 
parent processes or suspicious command-line executions of radio-control tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity BLE Advertising Exfiltration (T1011.001)
- **ID:** `T1011_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects covert data exfiltration via BLE Advertising frames by identifying 
unauthorized processes invoking WinRT BluetoothLEAdvertisementPublisher 
APIs to broadcast custom manufacturer data payloads.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Query Registry Discovery (T1012)
- **ID:** `T1012.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic Registry discovery targeting sensitive security configurations, 
credential storage, and persistence paths. Uses recursive query detection 
and integrity level gating to minimize false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity BYOVD Rootkit Loading (T1014)
- **ID:** `T1014.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the "Bring Your Own Vulnerable Driver" (BYOVD) technique. 
Focuses on the execution of known driver loaders or the registration of kernel-mode 
services from non-standard paths, while filtering out legitimate OS driver maintenance.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity System Network Configuration Discovery (T1016)
- **ID:** `T1016.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic discovery of network configuration (IP, routing, DNS, ARP). 
Filters high-volume noise from VPN clients and system services using integrity 
levels, parent process gating, and command-line switch analysis.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Internet IP Discovery (T1016.001)
- **ID:** `T1016_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to discover the system's external IP address using command-line tools 
and common IP-echo services. Minimizes false positives by analyzing the parent-child 
process relationship, integrity levels, and typical developer tool fingerprints.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Terminal Services Configuration Discovery (T1016.002)
- **ID:** `T1016_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted discovery of Terminal Services and RDP configurations. 
Focuses on non-standard process lineages (e.g., Office, Browsers) and 
detects specific command-line switches used to identify hijackable sessions 
or disabled security settings.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Remote System Discovery (T1018)
- **ID:** `T1018.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic remote system discovery with a focus on Domain Controller identification 
and network topology mapping. Filters out high-volume noise from system services, 
browsers, and inventory agents using integrity levels and parent process gating.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Automated Exfiltration (T1020)
- **ID:** `T1020.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects automated exfiltration by identifying the sequential pattern of 
password-protected archiving followed by immediate network transfer using 
non-standard tools or cloud-sync binaries from suspicious locations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Client-Linked Cloud Exfil (T1020.001)
- **ID:** `T1020_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects data exfiltration by identifying official cloud storage clients 
(OneDrive, Dropbox, etc.) being manipulated via command-line to sync 
non-standard staging directories or running with high-entropy/scripted arguments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rapid Logons to Multiple Distant Hosts by Same User
- **ID:** `T1021.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects a single user successfully logging on to multiple different hosts within a short time window. This behavior may indicate stolen credentials, pass-the-hash, or lateral movement using valid accounts.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**


---
## Suspicious RDP Logon from Unusual Source
- **ID:** `T1021_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects successful RDP logons originating from unusual or non-enterprise sources, especially when targeting servers and performed by non-admin or rarely used accounts.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**


---
## Ultra-Pro High-Fidelity SMB Admin Share Mapping (T1021.002)
- **ID:** `T1021_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted access to administrative shares (C$, ADMIN$, IPC$) using 
native tools (net.exe, PowerShell) while filtering out standard IT 
orchestration and service-level noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity DCOM Remote Execution (T1021.003)
- **ID:** `T1021_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [VISIO.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects lateral movement via DCOM by monitoring suspicious child processes 
from known vulnerable COM objects. Specifically filters for headless 
execution and anomalous network-to-process lineage.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity SSH Lateral Movement & Tunneling (T1021.004)
- **ID:** `T1021_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [SSH.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects advanced SSH lateral movement and tunneling. Filters legitimate 
DevOps/Git activity by analyzing parent process lineage, command-line 
entropy, and non-standard authentication patterns.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity VNC Lateral Movement & Hijacking (T1021.005)
- **ID:** `T1021_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized VNC activity by monitoring for portable VNC execution 
from suspicious paths, reverse connection attempts, and command-line 
credential injection while filtering enterprise remote support tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity WinRM Remote Execution (T1021.006)
- **ID:** `T1021_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects advanced lateral movement via WinRM by monitoring for high-entropy 
PowerShell commands, in-memory execution, and suspicious process 
hollowing attempts originating from the WinRM host process.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Cloud Control Plane Hijacking (T1021.007)
- **ID:** `T1021_007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized lateral movement through cloud dashboards by correlating 
high-risk operations with anomalous user agents, unusual source IPs, and 
signs of MFA-evasion/automated session hijacking.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity macOS ARD Remote Hijacking (T1021.008)
- **ID:** `T1021_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized activation or modification of Apple Remote Desktop (ARD) 
by monitoring the 'kickstart' utility for high-risk flags that grant 
universal access, while filtering legitimate MDM (Jamf, Kandji) orchestration.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Removable Media Data Theft (T1025)
- **ID:** `T1025.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic and automated data collection from removable media (USB/External Drives) 
by identifying recursive discovery patterns, specific archival switches, and 
suspicious process lineages, while filtering out standard OS activities.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Base64-Encoded PowerShell Command with Network Activity
- **ID:** `T1027.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects PowerShell executions using Base64-encoded commands combined with network-based payload retrieval and non-interactive execution. This pattern is strongly associated with malware delivery, loaders, and post-exploitation frameworks.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Binary Padding Activity (T1027.001)
- **ID:** `T1027_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects binary padding where attackers increase file size to bypass security 
scanners or alter hashes. Focuses on tools like fsutil, dd, and binary copy 
commands targeting executable files in suspicious paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Software Packing Event (T1027.002)
- **ID:** `T1027_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the use of binary packers (UPX, MPRESS, etc.) in non-standard environments. 
Focuses on command-line patterns used for high-compression/obfuscation and 
suspicious parent process lineages.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Steganography Payload Extraction (T1027.003)
- **ID:** `T1027_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects the programmatic extraction of hidden payloads from image files. 
Focuses on the transition from pixel-level data access (GDI+) to dynamic 
code execution (Reflection/IEX) within the same process context.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Steganography Payload Extraction (T1027.004)
- **ID:** `T1027_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects the extraction of malicious payloads from image files using 
low-level GDI+ or .NET Bitmap methods often seen in Invoke-PSImage or similar 
steganography frameworks.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Indicator Removal and Signature Theft (T1027.005)
- **ID:** `T1027_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects attempts to remove indicators or manipulate digital signatures on binaries. 
Focuses on signature theft (SigThief), PE header stripping, and string replacement 
in suspicious locations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity HTML Smuggling Execution (T1027.006)
- **ID:** `T1027_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the execution of suspicious files typically delivered via HTML Smuggling. 
Focuses on browser processes spawning script interpreters or mounting disk images 
from temporary or local app data directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Binary Symbol Stripping (T1027.007)
- **ID:** `T1027_007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the active stripping of debug symbols and section headers from binaries. 
Focuses on the execution of stripping tools on non-build systems to hinder forensics.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Binary Symbol Stripping (T1027.008)
- **ID:** `T1027_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the active stripping of debug symbols and section headers from binaries 
in non-development environments. This hinders forensic analysis and reverse engineering 
by removing function names and symbol tables.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Embedded Payload Extraction (T1027.009)
- **ID:** `T1027_009.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [NGEN.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the extraction and execution of embedded payloads by monitoring 
suspicious memory-only code loading (Reflection) and byte-array manipulation 
targeting non-standard resource locations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Command Line Obfuscation (T1027.010)
- **ID:** `T1027_010.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects advanced command line obfuscation techniques. Focuses on excessive 
escape character density, environment variable slicing, and PowerShell string 
deconstruction used to bypass static detection filters.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Suspicious Archive Creation (T1027.011)
- **ID:** `T1027_011.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MAKECAB.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation of password-protected and/or encrypted archives using common CLI tools. 
Focuses on command-line password arguments and recursive collection from sensitive paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Windows LDR Hijacking (T1027.012)
- **ID:** `T1027_012.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to hijack the Windows loader (LDR) via AppInit_DLLs or AppCertDLLs. 
It specifically targets DLL registrations originating from non-system paths (Temp, Public, User profiles) 
and the activation of the LoadAppInit_DLLs flag by suspicious processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Scheduled Transfer (T1029)
- **ID:** `T1029.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation of scheduled tasks for automated data exfiltration by 
analyzing Task XML for suspicious CLI tools, cloud-sync arguments, and 
high-frequency or off-hours triggers, while filtering legitimate system updates.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Data Chunking and Fragmentation (T1030)
- **ID:** `T1030.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects stealthy data fragmentation for exfiltration by identifying 
low-level file stream manipulation, custom buffer-based splitting, 
and non-standard archive volume creation from suspicious execution paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity System Owner/User Discovery (T1033)
- **ID:** `T1033.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic discovery of the current user, logged-on users, and token privileges. 
Focuses on anomalous process lineages (Office, Browsers) and specific switch 
combinations (/priv, /groups) used before privilege escalation attempts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Masquerading and Process Path Abuse (T1036)
- **ID:** `T1036.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects advanced masquerading techniques including system binary path anomalies, 
double extensions, and critical system processes spawned by untrusted parents. 
Optimized to filter out legitimate Windows Update and side-loading behaviors.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Invalid or Forged Code Signature (T1036.001)
- **ID:** `T1036_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects critical system processes (e.g., lsass, svchost) running with invalid, 
untrusted, or forged digital signatures. Focuses on identity-signature 
mismatch and publisher typosquatting to eliminate developer noise.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity RTLO Character Execution (T1036.002)
- **ID:** `T1036_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the execution of processes containing the Right-to-Left Override (RTLO) 
Unicode character (U+202E). Optimized to detect various encodings and 
suspicious execution contexts (Downloads, Temp) while filtering system noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Renamed System Utility (T1036.003)
- **ID:** `T1036_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the execution of renamed Windows system utilities (LOLBins) by comparing 
current process names with internal metadata. Uses path-based filtering 
and signature-awareness to eliminate false positives from installers.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Masquerading via Path Anomaly (T1036.004)
- **ID:** `T1036_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects sophisticated masquerading where system binaries are executed from 
untrusted, user-writable directories or from spoofed system paths (e.g., space padding). 
Filters out legitimate Side-by-Side (WinSxS) and Windows Update behaviors.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Legitimate Windows Binary Copied to User-Writable Location
- **ID:** `T1036_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious copying of legitimate Windows system binaries into user-writable directories. This technique is commonly used by attackers for masquerading, DLL sideloading, or execution evasion by abusing trusted binary names.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Space After Filename Masquerading (T1036.006)
- **ID:** `T1036_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects intentional masquerading using trailing spaces in filenames or directory names. 
Focuses on executable extensions followed by spaces to evade string-based detection 
while filtering common Windows Update and SCCM/MECM noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Double File Extension Execution (T1036.007)
- **ID:** `T1036_007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects execution of binaries masquerading as documents via double extensions. 
Strictly filters developer artifacts (.min.js, .map) and verified installers, 
focusing on high-risk user directories and suspicious parent lineages.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Masquerade File Type via Interpreter Misuse (T1036.008)
- **ID:** `T1036_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects mismatched file type execution where legitimate interpreters (wscript, cscript, powershell, regsvr32) 
execute files with non-standard extensions (e.g., .jpg, .txt, .png). 
Filters out system-level automation and focuses on untrusted user directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Allure Document and RTLO Masquerading (T1036.009)
- **ID:** `T1036_009.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects sophisticated masquerading using allure documents and RTLO characters. 
Focuses on execution from untrusted user directories and suspicious parent 
processes (browsers, mail clients) while filtering common developer noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Logon Script Persistence (T1037)
- **ID:** `T1037.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation or modification of logon scripts in the registry (UserInitMprLogonScript).
Attackers use this to bypass GPO-based logon scripts and execute malicious code at every logon.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity UserInitMprLogonScript Persistence
- **ID:** `T1037_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized creation or modification of the UserInitMprLogonScript registry key.
This is a high-fidelity rule because it filters out standard GPO updates and focuses on 
user-writable paths and suspicious execution patterns.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Netsh Helper DLL Persistence
- **ID:** `T1037_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the registration of a new Netsh Helper DLL. 
Attackers use this to maintain persistence by loading a malicious DLL 
whenever netsh.exe or a related networking service starts.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Network Logon Script/Shortcut Modification (T1037.003)
- **ID:** `T1037_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Detects unauthorized modification of scripts (.bat, .ps1, .vbs) or shortcuts (.lnk) 
within sensitive network shares like NETLOGON or SYSVOL. 
It specifically filters out legitimate DFS replication and system-level updates.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro RC Script and Init.d Persistence (T1037.004)
- **ID:** `T1037_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized modification of RC scripts, init.d, or systemd generators by non-package manager processes.
Attackers use these to gain root persistence on Linux/macOS systems.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro macOS Startup Items Persistence (T1037.005)
- **ID:** `T1037_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Detects unauthorized creation of files in legacy StartupItems directories.
It minimizes false positives by whitelisting the official macOS installer 
subsystem and focusing on unsigned or script-generated persistence.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Network Share Discovery (T1039)
- **ID:** `T1039.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic discovery and collection of sensitive data from network shares 
by identifying recursive file enumeration using UNC paths, combined with 
output redirection or mass archival from non-standard process contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Network Sniffing Detection (T1040)
- **ID:** `T1040.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [PKTMON.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized network sniffing by monitoring for administrative tools 
used in capture mode, driver installation for packet interception, 
and offensive sniffing frameworks running from untrusted paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Exfiltration Over C2 Channel (T1041)
- **ID:** `T1041.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects data exfiltration over an established C2 channel by correlating 
systematic file read operations, memory-stream encoding, and long-standing 
outbound network connections from non-browser processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Network Service Discovery (T1046)
- **ID:** `T1046.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic network service discovery and internal port scanning. 
Focuses on loop-based scanning patterns in PowerShell, CMD, and specialized 
binaries originating from non-IT admin contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Remote Process Creation via WMIC
- **ID:** `T1047.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious usage of wmic.exe to create processes on remote hosts using the "process call create" method. This technique is commonly used by attackers for lateral movement after credential compromise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Alternative Protocol Exfiltration (T1048)
- **ID:** `T1048.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects data exfiltration over non-standard protocols by identifying 
abnormal ICMP buffer sizes, SSH/tunneling flags in non-admin contexts, 
and network-capable LoLBins executing from suspicious paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Symmetric Encrypted Exfiltration (T1048.001)
- **ID:** `T1048_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [FTP.EXE](https://lolbas-project.github.io/lolbas/), [SFTP.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects encrypted data exfiltration by identifying SCP/SFTP/Rclone 
usage from non-standard paths, focusing on automated (non-interactive) 
flags and suspicious parent process lineages.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Asymmetric Encrypted Exfiltration (T1048.002)
- **ID:** `T1048_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects data exfiltration over asymmetric encrypted protocols (HTTPS) 
by identifying command-line tools (curl, powershell) using upload-specific 
flags from untrusted paths or launched by suspicious parent processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Unencrypted Protocol Exfil (T1048.003)
- **ID:** `T1048_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects stealthy data exfiltration via DNS and ICMP by correlating 
anomalous payload sizes and non-standard query types with suspicious 
process lineages and untrusted execution paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity System Network Connections Discovery (T1049)
- **ID:** `T1049.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted discovery of active network connections and established sessions. 
Focuses on non-standard process lineages (Office, Browsers, Web Servers) and 
detects specific command-line switch combinations used by attackers to map 
the network landscape.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Physical Medium Exfiltration (T1052)
- **ID:** `T1052.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic data exfiltration to physical media by monitoring 
non-interactive copy/archive commands targeting removable disk volumes, 
filtering out legitimate Windows Explorer GUI operations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity USB Exfiltration (T1052.001)
- **ID:** `T1052_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic data exfiltration to USB devices by monitoring 
non-interactive copy/move/archive commands targeting removable drives, 
focusing on suspicious process lineages and stealthy CLI arguments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús ütemezett feladat vagy munkakör létrehozása a Persistence (T1053) miatt
- **ID:** `T1053.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli az ütemezett feladatok vagy a több operációs rendszeren keresztüli adatmegőrzéshez használt feladatok gyanús létrehozását. A támadószerű végrehajtási mintákra összpontosít.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity At.exe Activity Detection
- **ID:** `T1053_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the execution of at.exe for task scheduling. Since 'at' is deprecated, 
any interactive use or remote machine targeting (\\) is considered highly suspicious 
and indicative of persistence or lateral movement.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cron Persistence and In-Place Modification
- **ID:** `T1053_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized creation or modification of cron jobs by monitoring 
direct writes to cron directories and suspicious shell one-liners. 
Filters legitimate package managers and configuration management tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Scheduled Task Creation Executing PowerShell
- **ID:** `T1053_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious creation of scheduled tasks using schtasks.exe that execute PowerShell, commonly abused by attackers to establish persistence or delayed execution of malicious payloads.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Systemd Service Creation or Modification
- **ID:** `T1053_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects the creation or modification of systemd service units with a focus on 
anomalous execution paths (e.g., /tmp, /dev/shm) and suspicious parent processes 
(e.g., shells, web servers). Filters out legitimate package management and CM tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Systemd Timer Persistence Detection
- **ID:** `T1053_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects the creation or activation of systemd timers used for persistence. 
Focuses on non-standard directory locations (user-level units), interactive shell 
triggers, and suspicious execution payloads (obfuscation, network tools).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy Process Injection Detection (T1055)
- **ID:** `T1055.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects advanced process injection (e.g. DLL injection, Thread Hijacking) by 
monitoring for specific high-risk GrantedAccess masks combined with 
suspicious source-target relationships and unbacked memory regions.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy DLL Injection (T1055.001)
- **ID:** `T1055_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-fidelity DLL injection by identifying remote thread creation 
where the start address is a known library-loading function or the source 
memory region is not backed by a file on disk (unbacked memory).


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy PE Injection (T1055.002)
- **ID:** `T1055_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-fidelity PE injection by identifying cross-process memory 
manipulation where the source of the call is an unbacked memory region 
(shellcode) and the target is a critical system process.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy Thread Hijacking (T1055.003)
- **ID:** `T1055_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects thread execution hijacking by identifying cross-process access 
requests with thread manipulation rights (SET_CONTEXT) where the 
calling stack originates from unbacked memory (shellcode).


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy APC Injection (T1055.004)
- **ID:** `T1055_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-fidelity APC injection attempts (including Early Bird) by monitoring for 
specific thread access masks (THREAD_SET_CONTEXT) where the calling code originates 
from unbacked or untrusted memory regions (CallTrace analysis).


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy TLS Injection (T1055.005)
- **ID:** `T1055_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-fidelity TLS injection by monitoring for cross-process memory 
manipulation targeting PE headers where the execution flow originates 
from unbacked memory (shellcode).


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy Ptrace Injection (T1055.008)
- **ID:** `T1055_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-fidelity ptrace-based process injection by identifying 
PTRACE_POKETEXT/DATA operations from suspicious sources or 
cross-user ptrace attachments, filtering out legitimate debuggers.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy Module Overwriting (T1055.009)
- **ID:** `T1055_009.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects process or module overwriting by identifying cross-process access 
requests with VM_WRITE permissions where the calling stack originates from 
unbacked memory (shellcode) rather than a signed on-disk module.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy EWM Injection (T1055.011)
- **ID:** `T1055_011.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects Extra Window Memory (EWM) injection by monitoring for suspicious 
cross-process access with memory manipulation rights where the CallTrace 
indicates execution from unbacked memory (shellcode) targeting GUI processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy Process Hollowing (T1055.012)
- **ID:** `T1055_012.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-fidelity process hollowing by identifying cross-process access 
requests with VM_WRITE/VM_OPERATION permissions where the calling stack 
originates from unbacked memory (shellcode) and targets common sacrificial processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy Process Hollowing (T1055.013)
- **ID:** `T1055_013.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-fidelity process hollowing by identifying cross-process access 
requests with VM_WRITE/VM_OPERATION permissions where the calling stack 
originates from unbacked memory (shellcode) and targets common sacrificial processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy Process Ghosting (T1055.014)
- **ID:** `T1055_014.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects Process Ghosting by identifying process creation events where the 
underlying file is in a 'delete-pending' state, evidenced by missing hashes 
at execution time and originating from non-standard directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy ListPlanting Injection (T1055.015)
- **ID:** `T1055_015.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects ListPlanting injection by identifying suspicious cross-process access 
requests to ListView-capable processes where the execution flow originates 
from unbacked memory regions (shellcode) rather than signed modules.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Input Capture Detection (T1056)
- **ID:** `T1056.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects sophisticated input capture (keylogging) by identifying suspicious 
API-related command lines, unauthorized shell-based keylogging snippets, 
and anomalous process behavior targeting user input.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Keylogging & Input Hooking (T1056.001)
- **ID:** `T1056_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects advanced keylogging by identifying suspicious API calls from unprivileged 
or ephemeral processes, targeting the use of SetWindowsHookEx and GetAsyncKeyState 
within non-standard execution contexts (e.g., PowerShell, Rundll32).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity GUI Input Capture (T1056.002)
- **ID:** `T1056_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to capture credentials through deceptive GUI prompts or overlays. 
Focuses on PowerShell/C# snippets creating modal dialogs from suspicious parent 
processes (browsers, office apps) and unbacked scripts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Digital Certificate Theft (T1056.003)
- **ID:** `T1056_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized extraction of private keys and digital certificates. 
Monitors for 'non-exportable' key extraction via memory patching, 
suspicious use of certutil/PowerShell for PFX creation, and direct 
access to the Windows Cryptographic Key Store.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Credential API Hooking via Win32 Libraries
- **ID:** `T1056_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious processes loading combinations of Win32 libraries commonly abused for credential interception or API hooking, such as user32.dll, advapi32.dll, and win32u.dll. The rule focuses on non-system, user-writable execution paths and excludes common legitimate software to reduce false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Process Discovery (T1057)
- **ID:** `T1057.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted process discovery focusing on security product identification 
and memory target reconnaissance. Filters high-frequency noise from 
browsers and legitimate update orchestrators.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Scripting Interpreter Contextual Anomaly
- **ID:** `T1059.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious PowerShell or CMD execution by correlating shell interpreters 
with high-risk parent processes (Office, Browsers, Web Servers) and obfuscation techniques.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Encoded PowerShell Command Execution
- **ID:** `T1059_001.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious execution of PowerShell using encoded commands combined with execution bypass or obfuscation flags. This technique is commonly used by attackers to evade detection and execute malicious payloads in memory.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity AppleScript (osascript) Abuse Detection
- **ID:** `T1059_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects suspicious osascript execution by monitoring for 'do shell script' escapes, 
base64 encoded payloads, and execution originating from untrusted parent processes 
like browsers or mail clients.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Windows Command Shell Contextual Anomaly
- **ID:** `T1059_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious cmd.exe execution by correlating risky parent processes 
(Web Servers, Office, SQL) with anomalous command-line patterns like 
command chaining and discovery.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Unix Shell Abuse and Reverse Shell Detection
- **ID:** `T1059_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects suspicious Unix shell execution by monitoring for command injection 
from web processes, reverse shell socket redirection, and fileless pipe-to-shell patterns.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity VBScript Contextual Anomaly Detection
- **ID:** `T1059_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [PUBPRN.VBS](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious VBScript execution by filtering legitimate OS management scripts 
and focusing on risky parent processes, unusual file locations, and 
common obfuscation/download patterns used in malware delivery.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Python Interpreter Abuse Detection
- **ID:** `T1059_006.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects suspicious Python execution patterns, focusing on one-liner reverse shells, 
interactive shell upgrades, and execution originating from high-risk network-facing 
parent processes (Web Servers, SQL).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity JScript Interpreter Contextual Anomaly
- **ID:** `T1059_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious JScript execution by correlating wscript/cscript with 
risky parent processes, untrusted file locations, and command-line arguments 
typically used for obfuscation or remote payload retrieval.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Network Device CLI Manipulation
- **ID:** `T1059_008.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)
- **Leírás:** Detects critical unauthorized configuration changes on network devices, 
focusing on anti-forensics (disabling logs), credential exposure, 
and unauthorized data exfiltration (config export).


#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Shell Exploitation and Data Exfiltration
- **ID:** `T1059_009.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized or malicious activities within Cloud Shell environments, 
focusing on identity theft, log suppression, and the conversion of private 
cloud resources to public access.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious SYSTEM Process Spawned from User Context
- **ID:** `T1068.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious processes running as SYSTEM that are spawned from user-initiated parent processes such as Explorer, browsers, or Office applications. This behavior may indicate privilege escalation, token manipulation, or UAC bypass exploitation.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Permission Groups Discovery (T1069)
- **ID:** `T1069.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic discovery of local or domain permission groups. 
Focuses on reconnaissance patterns used to identify privileged accounts 
while filtering out legitimate system/inventory noise through integrity and parent analysis.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Local Group Discovery (T1069.001)
- **ID:** `T1069_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted local group reconnaissance focusing on privileged accounts 
(Administrators, RDP). Filters out legitimate system/inventory noise 
through integrity level gating and parent-process correlation.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Domain Group Discovery (T1069.002)
- **ID:** `T1069_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic AD domain group discovery focusing on reconnaissance tools 
(BloodHound, AdFind) and suspicious PowerShell patterns. Uses integrity level 
and process lineage to minimize false positives from admin workstations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Cloud Groups Discovery (T1069.003)
- **ID:** `T1069_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects systematic cloud group discovery by identifying mass reconnaissance patterns, 
atypical User-Agents, and expansion of sensitive group properties. 
Designed to filter out high-volume CSPM and IaC service principals.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Indicator Removal on Host (T1070)
- **ID:** `T1070.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [FSUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted attempts to clear Windows Event Logs and high-value forensic artifacts 
(USN Journal, Prefetch). Focuses on non-standard execution chains and specific 
clearing of security-sensitive providers.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Security Event Log Cleared Using wevtutil.exe
- **ID:** `T1070_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to clear the Windows Security event log using wevtutil.exe, a common attacker technique used to cover tracks after credential access, lateral movement, or persistence.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Linux Log Clearing and Journal Sabotage (T1070.002)
- **ID:** `T1070_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects targeted attempts to clear or truncate Linux system logs and journald buffers. 
Focuses on manual command-line patterns, shell redirection to log files, and 
vacuuming of systemd journals outside of automated maintenance windows.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Mailbox Data Clearing and Rule Sabotage (T1070.003)
- **ID:** `T1070_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic mailbox data removal and the creation of malicious inbox rules. 
Focuses on bulk deletion cmdlets and automated rule sets designed to suppress 
security notifications or hide attacker communication.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Forensic Artifact and File Deletion (T1070.004)
- **ID:** `T1070_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CIPHER.EXE](https://lolbas-project.github.io/lolbas/), [FSUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted destruction of high-value forensic artifacts (USN Journal, Prefetch, Amcache) 
and the use of secure wipe utilities. Focuses on non-standard process origins and 
evasion techniques used to prevent post-incident recovery.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Network Share and Credential Removal (T1070.005)
- **ID:** `T1070_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CMDKEY.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic removal of network shares and stored credentials using wildcard 
deletion and force flags. Distinguishes between manual user activity and 
automated anti-forensic cleanup post-lateral movement.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Timestomp and MACE Attribute Manipulation (T1070.006)
- **ID:** `T1070_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to modify file timestamps (MACE attributes) to evade forensic analysis. 
Focuses on direct object property manipulation in PowerShell and specialized 
anti-forensic utilities, while filtering out legitimate installer behavior.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Network History and RDP Trace Removal (T1070.007)
- **ID:** `T1070_007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted attempts to clear network connection history, focusing on RDP 
Terminal Server Client MRU lists and network share metadata removal. 
Filters out common helpdesk troubleshooting (DNS flush) unless part of a broader attack.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Email Storage and Database Destruction (T1070.008)
- **ID:** `T1070_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted destruction of email storage (PST/OST) and Exchange Databases (EDB). 
Focuses on programmatic deletion, database dismounting, and forensic wiping 
patterns from untrusted processes or suspicious parent-child chains.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Persistence Artifact Removal (T1070.009)
- **ID:** `T1070_009.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the systematic removal of persistence mechanisms (Scheduled Tasks, Services, WMI) 
focusing on forced deletion patterns and suspicious process lineages. 
Filters out common software update cycles and MSI installer noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Application Layer C2 Anomaly (T1071)
- **ID:** `T1071.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential C2 communication by identifying anomalous network connections 
initiated by non-browser processes, focusing on library loads (WinInet/WinHTTP) 
and suspicious parent-child relationships.


#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity HTTP/S C2 Anomaly (T1071.001)
- **ID:** `T1071_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential C2 communication over HTTP/S by identifying anomalous 
network connections from processes that typically lack networking logic, 
or show signs of process hollowing and suspicious parent-child lineage.


#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity FTP/SFTP Protocol Anomaly (T1071.002)
- **ID:** `T1071_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized use of file transfer protocols by monitoring for 
non-interactive FTP/SFTP sessions, suspicious script-based transfers, 
and anomalous parent-child process relationships (e.g., Office to FTP).


#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Mail Protocol Anomaly (T1071.003)
- **ID:** `T1071_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGEWEBVIEW2.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized email-based C2 or exfiltration by identifying direct 
mail protocol (SMTP, IMAP, POP3) connections from non-mail processes, 
focusing on .NET/PowerShell automation and suspicious process lineages.


#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity DNS Tunneling & Beaconing (T1071.004)
- **ID:** `T1071_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects DNS tunneling and C2 by monitoring for high-entropy subdomains, 
unusual query types (TXT, NULL), and DNS activity from non-network 
native processes with specific focus on length and frequency.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Software Deployment Tool Abuse Detection
- **ID:** `T1072.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of software deployment agents to execute malicious payloads. 
Focuses on anomalous child processes (PowerShell, BitsAdmin, CertUtil) spawned 
by deployment services, filtering out standard maintenance patterns.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Data Staging Anomaly (T1074)
- **ID:** `T1074.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MAKECAB.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects data staging by identifying anomalous file aggregation patterns, 
low-compression archival switches, and mass-copy operations into 
hidden or temporary system directories from untrusted shells.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Local Data Staging Anomaly (T1074.001)
- **ID:** `T1074_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MAKECAB.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic local data staging by identifying anomalous file aggregation 
patterns, specific low-compression or password-protected archival switches, 
and mass-copy operations into hidden system directories from untrusted contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Remote Data Staging (T1074.002)
- **ID:** `T1074_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects remote data staging by identifying anomalous mass-file movements to 
internal UNC paths, followed by archival commands with low-compression/encryption 
flags, originating from untrusted process lineages.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Anomalous Logon via Valid Account
- **ID:** `T1078.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects successful logons using valid accounts that exhibit anomalous characteristics, 
such as unusual logon types for service accounts or logons followed by immediate 
sensitive command execution.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Default Account Abuse Detection
- **ID:** `T1078_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects successful logons using well-known default account names (Administrator, Guest, root) 
originating from non-standard network locations or via interactive remote sessions (RDP). 
Filters out common local system noise and internal automation.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Domain Account Lateral Movement Anomaly
- **ID:** `T1078_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects anomalous RDP or Network logons to critical infrastructure (DCs, SQL, File Servers) 
originating from unauthorized source subnets or non-admin user accounts. 
Implements strict filtering for machine accounts and known jump servers.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Local Account Remote Access Detection
- **ID:** `T1078_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects successful remote logons (RDP, SMB, WinRM) using local accounts. 
In a domain environment, local accounts should only be used for local console 
access. Remote usage is a strong indicator of lateral movement or credential theft.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Account Compromise (Entra ID)
- **ID:** `T1078_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects successful cloud logons that exhibit high-risk indicators: 
MFA bypass on privileged accounts, impossible travel patterns, 
or the use of non-standard automation User-Agents by human accounts.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Taint Shared Content (T1080)
- **ID:** `T1080.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to taint shared content by monitoring for suspicious 
process-to-file-share interactions, focusing on macro-enabled templates, 
shortcut hijacking, and binary replacement on UNC paths.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity System Information Discovery (T1082)
- **ID:** `T1082.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic system information discovery (OS, patches, architecture) 
focusing on reconnaissance for exploit selection. Filters high-volume noise 
from inventory agents and browsers using integrity levels and parent process gating.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity File and Directory Discovery (T1083)
- **ID:** `T1083.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted file and directory discovery focusing on sensitive data harvesting.
Filters out legitimate system indexing, AV scans, and developer activities by analyzing 
process integrity, parent-child relationships, and specific keyword patterns.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Use of net user or net localgroup via cmd.exe
- **ID:** `T1087.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious usage of cmd.exe executing net user or net localgroup commands, commonly used by attackers for account discovery or privilege escalation. The rule focuses on attacker-like execution context to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Local Account Discovery (T1087.001)
- **ID:** `T1087_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic local account and group enumeration. 
Focuses on anomalous process lineages (e.g., discovery tools launched by web servers or 
remote shells) and the use of modern enumeration methods like WMI/CIM.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Domain Account Discovery (T1087.002)
- **ID:** `T1087_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic Active Directory enumeration focusing on offensive LDAP filters 
and non-standard process lineages. Filters legitimate administrative behavior 
by excluding known service accounts and management tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Email Account Discovery (T1087.003)
- **ID:** `T1087_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic discovery of email accounts and Global Address Lists (GAL). 
Focuses on non-interactive PowerShell sessions, mass-exporting recipients, 
and anomalous access to local mail profile configurations by untrusted processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Cloud Account Discovery (T1087.004)
- **ID:** `T1087_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic discovery of cloud accounts (AWS, Azure, GCP) focusing on 
interactive shell sessions and anomalous command chaining. Filters legitimate 
CI/CD and automation workloads based on process lineage and user context.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Proxy & Pivot Point Detection (T1090)
- **ID:** `T1090.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation of network proxies and port forwarding rules by correlating 
high-risk native binaries (Netsh) with pivot-specific arguments that map 
external listening ports to internal network assets.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Internal Proxy & Pivot Detection (T1090.001)
- **ID:** `T1090_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects internal network pivoting by identifying the configuration of 
port forwarding to private RFC 1918 IP addresses from non-system 
processes, excluding legitimate local virtualization and container traffic.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity External Proxy & Tunneling (T1090.002)
- **ID:** `T1090_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the use of non-standard external proxies by identifying hardcoded 
credentials, custom PAC files, or proxy-overrides in high-risk binaries 
launched from interactive or script interpreters.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Multi-hop Proxy & Tor Detection (T1090.003)
- **ID:** `T1090_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects multi-hop proxying and Tor circuitry by identifying unauthorized 
proxy chaining tools or hidden Tor clients running from non-standard 
directories, focusing on control port manipulation and SOCKS5 chaining.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Domain Fronting Detection (T1090.004)
- **ID:** `T1090_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects domain fronting by identifying manual HTTP Host header overrides 
within command-line arguments of common web-enabled LoLBins, 
specifically targeting CDN-backed infrastructure redirection.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Process Execution from Removable Media
- **ID:** `T1091.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SHELL32.DLL](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the execution of script interpreters and LOLBins from non-system drives. 
Focuses on patterns used by worms (like Raspberry Robin) and manual USB-based 
attacks while filtering out common portable applications.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Removable Media C2 Anomaly (T1071.002 / T1092)
- **ID:** `T1092.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized C2 or data staging via removable media by identifying 
non-interactive processes accessing hidden/system files on USB volumes, 
focusing on automated script execution and Alternate Data Stream (ADS) abuse.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Non-Application Layer C2 (T1095)
- **ID:** `T1095.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects custom C2 communication via raw TCP/UDP sockets by identifying 
the instantiation of low-level NetworkStreams and manual byte-array 
buffer manipulation followed by socket write operations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Account Manipulation - Persistence Focused
- **ID:** `T1098.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects suspicious and rare modifications to user account attributes that are 
strongly associated with persistence and privilege escalation, such as 
SID History injection, Kerberos Constrained Delegation changes, and 
disabling password expiration for sensitive accounts.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Entra ID Application Credential Addition
- **ID:** `T1098_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects when a new secret or certificate is added to an Entra ID application.
Attackers use this to establish a backdoor via Service Principals.
This rule filters out common Microsoft first-party apps and known CI/CD service principals.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Exchange Mailbox Permission Grant (T1098.002)
- **ID:** `T1098_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects the granting of critical mailbox permissions (FullAccess, SendAs). 
Filters out common service accounts and focuses on cross-tenant or 
unauthorized administrative actions, especially on high-value targets.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Entra ID App Certificate Addition
- **ID:** `T1098_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects the addition of a new certificate (public key) to an Entra ID application.
Attackers use this for long-term persistence to act as the application's service principal.
This rule is optimized to filter out automated Microsoft internal rotations and known CI/CD providers.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Azure Role Assignment Escalation
- **ID:** `T1098_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects direct assignment of highly privileged Azure roles (Owner, Contributor, User Access Admin). 
Filters out PIM (Privileged Identity Management) activations and known automation principals 
to reduce noise and focus on manual privilege escalation.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Device Registration Persistence (T1098.005)
- **ID:** `T1098_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects suspicious device registrations in Entra ID. Attackers register their own devices 
to bypass Conditional Access policies that require a "registered" device state.
This rule filters out managed enrollments and focuses on unmanaged or scripted registrations.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity MFA Method Addition
- **ID:** `T1098_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects when a new MFA method is added to a user account from a non-trusted location 
or without a fresh MFA challenge. This is a primary persistence technique for attackers 
to maintain access after an initial account compromise.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Web Service C2 (T1102)
- **ID:** `T1102.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects C2 communication via legitimate cloud services by identifying 
raw API or raw-content subdomains accessed by non-browser LoLBins, 
script interpreters, or binaries running from suspicious paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Dead Drop Resolver (T1102.001)
- **ID:** `T1102_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the use of dead drop resolvers by identifying raw content retrieval 
from social/code platforms, specifically filtering for suspicious parent-child 
relationships and non-standard download methods.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Bidirectional Cloud C2 (T1102.002)
- **ID:** `T1102_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects interactive C2 communication via cloud APIs by identifying 
specific write/read methods (POST/GET) issued by non-browser LoLBins 
or binaries running from suspicious paths, excluding official clients.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity One-Way Web Service C2 (T1102.003)
- **ID:** `T1102_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects one-way C2 or data exfiltration via cloud services by correlating 
specific API upload/download methods with non-standard process locations 
and suspicious parent process lineages.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Multi-Stage C2 (T1104)
- **ID:** `T1104.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects multi-stage C2 communication by identifying fileless execution patterns 
where the result of a network request is piped directly into memory-load 
functions or script evaluators without intermediate disk writes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Use of Built-in Windows Tools for File Download and Code Execution
- **ID:** `T1105.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious usage of built-in Windows utilities such as PowerShell, bitsadmin, and certutil to download files and execute code, a common attacker technique for payload staging and execution. The rule focuses on attacker-typical patterns and execution context to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Native API Abuse via LOLBins
- **ID:** `T1106.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the suspicious use of Native API execution through trusted Windows 
binaries (LOLBins). Focuses on scenarios where compilers or system tools 
are abused by untrusted parent processes to perform memory injection.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Brute Force & Tooling (T1110)
- **ID:** `T1110.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the execution of brute-force tools and scripted credential guessing by identifying 
suspicious command-line arguments (password lists, user files) and unauthorized 
process lineages from untrusted locations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Multiple Failed Login Attempts for Single User (Possible Password Guessing)
- **ID:** `T1110_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects multiple failed authentication attempts for the same user account within a short time window, which may indicate password guessing or brute-force activity. The rule excludes common sources of authentication noise to reduce false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**


---
## Ultra-Pro High-Fidelity Credential Export & Cracking (T1110.002)
- **ID:** `T1110_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to extract credential databases (SAM, SYSTEM, NTDS.dit) for offline 
cracking and identifies the execution of password recovery tools with high precision 
by filtering out legitimate backup and system maintenance processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Password Spraying (T1110.003)
- **ID:** `T1110_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects password spraying attacks by identifying suspicious automated authentication 
logic where a single process iterates through a list of accounts. It filters for 
untrusted process locations and known attack module signatures.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Credential Stuffing & Combo-list Abuse (T1110.004)
- **ID:** `T1110_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects credential stuffing by identifying automated tools and interpreters 
(Python, .NET) processing large credential combo-lists or using known 
stuffing framework arguments from untrusted locations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity MFA Evasion & Session Hijacking (T1111)
- **ID:** `T1111.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects MFA evasion by identifying unauthorized access to browser master keys (Local State) 
and session databases (Cookies) by untrusted processes. It also monitors for 
Reverse Proxy phishing frameworks (Evilginx, Muraena) and token manipulation tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Registry Tampering for Evasion (T1112)
- **ID:** `T1112.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-risk modifications to the Windows Registry aimed at disabling 
security controls (Defender, UAC, LSA) or enabling unauthorized remote access.
Optimized to ignore standard system updates and focus on non-standard process behavior.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Screen Capture Anomaly (T1113)
- **ID:** `T1113.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [PSR.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized screen capture by identifying suspicious .NET/GDI+ API 
calls within PowerShell, hidden PSR.exe sessions, and automated image 
serialization to temporary/public directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Email Harvesting Anomaly (T1114)
- **ID:** `T1114.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized automated email collection by identifying suspicious 
COM object instantiation (Outlook.Application), mailbox export requests, 
and programmatic access to Inbox/Sent folders from non-standard shells.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Local Email Harvesting Anomaly (T1114.001)
- **ID:** `T1114_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized automated local email collection by identifying suspicious 
COM object instantiation (Outlook.Application), folder index targeting (Inbox/Sent), 
and programmatic evasion (Visible=$false) from untrusted shells.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Remote Email Export Anomaly (T1114.002)
- **ID:** `T1114_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized remote email collection by identifying systematic 
mailbox export requests that use sensitive keyword filters and redirect 
output to non-standard internal UNC paths or administrative shares.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Email Forwarding Rule Anomaly (T1114.003)
- **ID:** `T1114_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized email forwarding rules by identifying programmatic 
redirection to external/untrusted domains combined with sensitive keyword 
filtering, originating from suspicious process lineages.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Clipboard Data Spying (T1115)
- **ID:** `T1115.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated clipboard monitoring and theft by identifying persistent 
polling loops, unmanaged assembly loads for clipboard access, and 
suspicious process lineages (Webshells, Office macros) accessing the API.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Automated Collection (T1119)
- **ID:** `T1119.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects highly suspicious, automated data collection by monitoring for 
wildcard-based recursive file transfers of sensitive extensions into 
common staging areas, originating from interactive or web shells.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Peripheral Device Discovery (T1120)
- **ID:** `T1120.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [PNPUTIL.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted peripheral device enumeration focusing on USB and storage devices.
Filters out legitimate system PnP activity and driver management by analyzing 
process integrity, parent-child relationships, and specific metadata queries.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Audio Capture & Spying (T1123)
- **ID:** `T1123.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized audio recording by correlating low-level multimedia API 
calls (winmm, dsound) with suspicious process lineages (Shells, Office, W3WP) 
and anomalous command-line arguments used by offensive toolsets.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity System Time Discovery (T1124)
- **ID:** `T1124.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted system time or time zone discovery. Focuses on anomalous process 
lineages (e.g., Office apps, Web servers) and specific automation patterns 
used for sandbox evasion or geofencing checks.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Video Capture Anomaly (T1125)
- **ID:** `T1125.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized video capture by identifying programmatic access to 
multimedia frameworks (DirectShow, Media Foundation) via suspicious interpreters, 
standalone media binaries (FFmpeg) with redirection, or headless shell sessions.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Trusted Developer Utility Proxy (T1127)
- **ID:** `T1127.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [JSC.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of trusted developer utilities (MSBuild, CSC, JSC) to proxy 
malicious code execution. Filters out legitimate CI/CD and IDE activity 
by focusing on suspicious parentage and command-line anomalies.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity MSBuild Proxy Execution (T1127.001)
- **ID:** `T1127_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects malicious MSBuild.exe execution by identifying anomalous parent processes, 
untrusted command-line arguments (like inline XML tasks), and excluding 
standard development and CI/CD environments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Shared Module Load from Untrusted Path
- **ID:** `T1129.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects trusted system binaries or productivity apps loading DLLs from 
untrusted, world-writable directories. This is a primary indicator of 
DLL Side-Loading or Search Order Hijacking.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Data Encoding & Obfuscation (T1132)
- **ID:** `T1132.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious data encoding/decoding sequences used for C2 stealth. 
Focuses on programmatic Base64/Hex conversion within non-standard process 
lineages and the abuse of Certutil for payload deployment.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Standard Encoding & Payload Injection (T1132.001)
- **ID:** `T1132_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious standard encoding usage by identifying embedded 
executable headers (MZ/PE) within Base64 strings, anomalous 
programmatic decoding, and high-entropy command lines from 
non-administrative processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Non-Standard Encoding & XOR Obfuscation (T1132.002)
- **ID:** `T1132_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects custom encoding and obfuscation by identifying programmatic byte-level 
manipulation (XOR), backtick-based string fragmentation, and character-code 
reconstruction in non-interactive process contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous External Remote Service Access Context
- **ID:** `T1133.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects suspicious successful logins via external remote services (RDP/VPN). 
It filters for non-standard source IPs and focuses on high-risk account types 
or technical anomalies in the logon event that are typical for automated 
credential stuffing or lateral movement from external jump boxes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Access Token Manipulation & Impersonation (T1134)
- **ID:** `T1134.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-risk access token manipulation by monitoring for suspicious 
Integrity Level transitions and the use of specialized tools that interact 
with LSASS to duplicate or steal security tokens.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Token Impersonation via LSASS Handle Duplication (T1134.001)
- **ID:** `T1134_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects token theft by monitoring for suspicious handle duplication requests 
targeting LSASS.exe. It filters for known legitimate system processes and 
security agents to ensure high-fidelity alerts.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Create Process with Token (T1134.002)
- **ID:** `T1134_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized process creation using duplicated tokens. 
Monitors for suspicious integrity level transitions from Medium to System 
without standard UAC elevation (Consent.exe) or legitimate service startup.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Make and Impersonate Token (T1134.003)
- **ID:** `T1134_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized creation of security tokens using explicit credentials. 
Monitors for suspicious command line arguments from offensive tools and 
correlates with Logon Type 9 (NewCredentials) anomalies from untrusted parents.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Parent PID Spoofing & Process Tree Violation (T1134.004)
- **ID:** `T1134_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BASH.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects Parent PID spoofing by identifying violations of the Windows process 
hierarchical model. Specifically targets critical system processes (LSASS, 
Spooler, CSRSS) spawning shells or script interpreters, which is architecturally 
impossible in a healthy environment.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro SID-History Injection & DS Manipulation (T1134.005)
- **ID:** `T1134_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects sIDHistory injection by monitoring Directory Service object changes (Event 5136) 
and correlating them with suspicious RPC calls or unauthorized LSASS access on Domain Controllers.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Network Share Discovery (T1135)
- **ID:** `T1135.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic network share discovery and content crawling. 
Focuses on automated enumeration patterns (loops, UNC sweeps) 
originating from non-standard parent processes and specialized tools like Snaffler.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Unauthorized Account Creation (T1136)
- **ID:** `T1136.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects local or domain account creation by identifying suspicious process lineages 
and command-line patterns while filtering out authorized system and deployment tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Unauthorized Local Account Creation (T1136.001)
- **ID:** `T1136_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects local user account creation by analyzing suspicious process lineages 
and command-line arguments. Filters out automated MDM, GPO, and known installer 
activities to maintain a low false-positive rate.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Unauthorized Domain Account Creation (T1136.002)
- **ID:** `T1136_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects domain account creation by identifying suspicious process lineages and 
non-standard execution environments. Filters out authorized IAM, HR-sync tools, 
and official AD management consoles.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Unauthorized Cloud Account Creation (T1136.003)
- **ID:** `T1136_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects manual cloud account creation by correlating the actor type, 
source IP reputation, and the absence of authorized provisioning service principals.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Office Application Startup Persistence (T1137)
- **ID:** `T1137.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized Office persistence by monitoring Registry modifications
originating from non-standard processes or pointing to suspicious file locations.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Modification of Office Global Template (Normal.dotm)
- **ID:** `T1137_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-risk modification or creation of Microsoft Office global  templates (Normal.dotm / NormalEmail.dotm) by non-Office processes or  from suspicious execution paths. This may indicate macro-based persistence  (MITRE ATT&CK T1137.001).


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Office Test DLL Persistence (T1137.002)
- **ID:** `T1137_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation or modification of the 'Office Test' Registry key used for 
DLL sideloading persistence. High-fidelity detection filters for non-standard 
paths and unauthorized parent processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Outlook Custom Forms Persistence (T1137.003)
- **ID:** `T1137_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized Outlook Custom Forms persistence by monitoring 
non-standard Registry modifications and suspicious process spawning 
from Outlook related to form script execution.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Outlook Home Page Hijacking & Bypass (T1137.004)
- **ID:** `T1137_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized modification of Outlook Folder Home Pages and the 
enabling of WebView bypass keys. This technique is used to execute 
arbitrary code when a user clicks on an Outlook folder.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Office Security Policy Tampering (T1137.005)
- **ID:** `T1137_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized weakening of Microsoft Office security policies. 
Focuses on global macro enablement, addition of untrusted network locations, 
and policy modifications originating from non-standard processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Office Add-in Binary Persistence (T1137.006)
- **ID:** `T1137_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized Office Add-in (.wll, .xll) persistence by filtering for 
untrusted file locations, unsigned binaries, and suspicious writing processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy Deobfuscation/Decoding (T1140)
- **ID:** `T1140.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPAND.EXE](https://lolbas-project.github.io/lolbas/), [EXTRAC32.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-fidelity deobfuscation by monitoring native tools (certutil, expand) 
decoding binaries from non-executable extensions (txt, jpg, xml) initiated 
by suspicious parents or targeting sensitive temp directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Browser Extension Force-Install Persistence (T1176)
- **ID:** `T1176.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation of 'ExtensionInstallForcelist' or 'ExtensionInstallSources' registry keys.
Attackers use these to force-install malicious extensions that cannot be removed by the user 
and to allow installation from non-official webstores.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Browser Session Hijacking (T1185)
- **ID:** `T1185.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects advanced browser session hijacking by monitoring unauthorized access 
to cookie databases from untrusted/unsigned processes or suspicious locations 
like \Temp or \AppData.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Forced Authentication (T1187)
- **ID:** `T1187.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects forced authentication attempts (NTLM Relay/Coercion) by monitoring 
suspicious UNC path patterns, WebDAV redirection, and specific RPC 
interface exploitation used to trigger outbound authentication.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Browser-Originating Shell or System Tool Execution
- **ID:** `T1189.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by web browsers. This pattern is highly 
indicative of successful exploitation via a Drive-by Compromise (T1189), 
where an exploit kit triggers a payload or a shell directly from the browser's memory.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Cross-Site Scripting (XSS) Attempt Detected on Web Server
- **ID:** `T1190.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects potential Cross-Site Scripting (XSS) attempts by identifying common reflected and encoded XSS payloads in HTTP requests, focusing on parameter-based injection patterns and excluding typical automated scanners to reduce false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**


---
## High-Fidelity Supply Chain Compromise Detection (Post-Update Anomaly)
- **ID:** `T1195.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WINGET.EXE](https://lolbas-project.github.io/lolbas/), [PROCDUMP.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by legitimate software updaters or signed 
installers. Focuses on discovery and credential access tools that should never be 
part of a standard software maintenance or update cycle.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Dependency Poisoning Detection
- **ID:** `T1195_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by package managers or build tools. 
Focuses on reconnaissance and exfiltration activities triggered during library 
installation or compilation (pre/post-install scripts).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Compromised Binary Activity (Post-Update)
- **ID:** `T1195_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by trusted business applications that 
have been compromised at the binary level. It focuses on the transition from 
legitimate app execution to unauthorized discovery or script execution.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Hardware/Firmware Manipulation Detection
- **ID:** `T1195_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the execution of firmware-flashing tools or low-level hardware access 
utilities in suspicious contexts. This targets potential post-exploitation 
of compromised hardware or attempts to install UEFI rootkits.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious File Download via Bitsadmin (High Fidelity)
- **ID:** `T1197.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious file downloads performed using bitsadmin.exe, a deprecated but still abused Windows LOLBAS utility. The rule focuses on attacker-typical usage patterns, execution context, and download targets to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Trusted Relationship Abuse Detection
- **ID:** `T1199.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious discovery and reconnaissance activities originating from 
trusted ingress points (RDP, Citrix, VPN). It filters out standard administrative 
behavior by focusing on specific parent-child process chains and unusual arguments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Malicious Hardware-Induced Command Execution (HID Injection)
- **ID:** `T1200.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious command execution patterns typical for malicious HID devices (Rubber Ducky, Bash Bunny). 
Focuses on rapid shell spawning with "stealth" flags originating from the user session context 
without standard GUI interaction.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Password Policy Discovery (T1201)
- **ID:** `T1201.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted enumeration of domain/local password policies. 
Focuses on reconnaissance patterns used to calibrate brute-force 
attacks while filtering out legitimate system/admin noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Indirect Command Execution (T1202)
- **ID:** `T1202.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FORFILES.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [PCALUA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the execution of binaries that can be used to proxy command execution. 
Focuses on non-standard parent processes and specific command-line arguments 
for pcalua.exe, conhost.exe, and forfiles.exe to minimize false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Client-Side Exploitation and Shell Spawning
- **ID:** `T1203.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by client applications (Office, Browsers, 
PDF Readers). Focuses on shell execution, discovery tools, and LOLBins originating 
from sandboxed or low-integrity application contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity)
- **ID:** `T1204.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [MSACCESS.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by Microsoft Office applications that are indicative of macro abuse, DDE exploitation, or document-based malware execution. The rule focuses on attacker- typical child processes, command-line patterns, and user-writable execution context to minimize false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity User Execution of Malicious Link (T1204.001)
- **ID:** `T1204_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by web browsers, email clients, or 
instant messengers. Focuses on LOLBins and script interpreters launched with 
network-related or obfuscated arguments, indicative of malicious link execution.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity User Execution of Malicious File
- **ID:** `T1204_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by office productivity apps, 
PDF readers, or archive tools. Specifically targets macro-initiated 
or exploit-driven execution of system tools (LOLBins).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Execution from Mounted Virtual Disk (T1204.003)
- **ID:** `T1204_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious binaries or scripts executing from a virtual disk drive (ISO, VHD, VHDX).
Focuses on LOLBins and script interpreters launched via explorer.exe from non-C: drives,
a common pattern for malware bypassing Mark-of-the-Web.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel
- **ID:** `T1204_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Alacsony (Jól monitorozható)
- **Leírás:** Észleli a rosszindulatú linkeket tartalmazó adathalász e-maileket URL-rövidítők, újonnan regisztrált domainek és feladó spoofing alapján.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Traffic Signaling & Port Knocking (T1205)
- **ID:** `T1205.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to implement or trigger Port Knocking/Traffic Signaling. 
Focuses on the registration of raw packet capturing drivers (Npcap/WinPcap) 
and suspicious firewall rule modifications initiated from untrusted shells.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Port Knocking & Raw Socket Listener (T1205.001)
- **ID:** `T1205_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized implementation of Port Knocking by monitoring the 
registration of raw packet capturing drivers and suspicious firewall 
modifications (UDP/ICMP/LocalPort Any) initiated from untrusted shells.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Socket Filter & WFP Traffic Signaling (T1205.002)
- **ID:** `T1205_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FLTMC.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized registration of network socket filters or WFP callouts. 
Monitors for low-level driver loading and WFP database manipulation from 
untrusted process lineages, a common technique for stealthy port knocking.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Rogue DC Topology Manipulation (T1207)
- **ID:** `T1207.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects the creation of a new nTDSDSA object or the registration of critical 
Domain Controller SPNs by a non-DC account. This is indicative of a Rogue DC 
or DCShadow attack.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Exploitation of Remote Services (T1210)
- **ID:** `T1210.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects successful post-exploitation patterns where a network service spawns an 
interactive shell or a proxy binary. Specifically tuned to catch RCE via SMB, 
RPC, Spooler, and WMI while ignoring standard IT orchestration.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Privilege Escalation Exploitation (T1211)
- **ID:** `T1211.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential exploitation for privilege escalation by identifying 
anomalous child processes from vulnerable parents with specific focus on 
breaking out of application sandboxes (browsers, office, pdf).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Credential Service Exploitation (T1212)
- **ID:** `T1212.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential exploitation of authentication services (LSASS, LogonUI, Spooler) 
by identifying illegal child processes, unbacked memory execution, and known 
exploitation patterns while filtering legitimate security tool interference.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Repository Dump (T1213)
- **ID:** `T1213.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized mass data collection from internal knowledge bases (Confluence, Jira, SharePoint) 
by identifying suspicious API-driven export commands originating from untrusted 
process contexts or temporary directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Confluence Scraping (T1213.001)
- **ID:** `T1213_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized mass content extraction from Atlassian Confluence by 
identifying suspicious API-driven read/export patterns originating from 
untrusted shell contexts or temporary directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity SharePoint Mass Data Exfiltration (T1213.002)
- **ID:** `T1213_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized mass data collection from SharePoint by identifying 
suspicious PnP PowerShell usage, bulk REST API queries, and unauthorized 
SharePoint Online Management Shell activity from non-standard contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Knowledge Base Scraping (T1213.003)
- **ID:** `T1213_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic knowledge base exfiltration (Wiki, Stack Overflow for Teams) 
by identifying recursive mirroring flags, mass archival logic, and 
non-browser scripting engines targeting internal documentation URLs.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity System Script Proxy Execution (T1216)
- **ID:** `T1216.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [MANAGE-BDE.WSF](https://lolbas-project.github.io/lolbas/), [PUBPRN.VBS](https://lolbas-project.github.io/lolbas/), [SYNCAPPVPUBLISHINGSERVER.VBS](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of trusted Windows signed scripts to proxy malicious code. 
Focuses on network-based execution triggers and anomalous parent-child 
process relationships to minimize false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Pubprn Script Proxy Execution (T1216.001)
- **ID:** `T1216_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [PUBPRN.VBS](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of the signed Windows script 'pubprn.vbs' to proxy the execution 
of remote scriptlets (.sct). Focuses on argument injection using the 'script:' 
protocol and anomalous process lineage.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Browser Information Discovery (T1217)
- **ID:** `T1217.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized discovery of browser metadata and history. 
Focuses on non-browser processes accessing sensitive profile files (SQLite/JSON) 
using command-line tools or anomalous redirection patterns.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity System Binary Proxy Execution (T1218)
- **ID:** `T1218.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMSTP.EXE](https://lolbas-project.github.io/lolbas/), [CONTROL.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [ODBCCONF.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects anomalous execution of trusted Windows binaries used to proxy malicious code. 
Focuses on cross-process boundary calls (e.g., Office to Rundll32) and suspicious 
command-line arguments like URLs or non-DLL extensions.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity HH.exe Proxy Execution (T1218.001)
- **ID:** `T1218_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of hh.exe to execute malicious code via CHM files or remote ITS protocols. 
Focuses on non-standard parent processes and command-line flags used for de-compilation 
or fetching remote payloads, while filtering out legitimate help file usage.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Control.exe Proxy Execution (T1218.002)
- **ID:** `T1218_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONTROL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of control.exe to load malicious .CPL or DLL files from untrusted paths.
Leverages OriginalFileName to catch renamed binaries and focuses on cross-boundary 
process execution (e.g., Office or Scripting hosts launching Control Panel).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity MsiExec Proxy Execution (T1218.003)
- **ID:** `T1218_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of msiexec.exe to execute malicious payloads. 
Focuses on non-standard parent-child relationships (e.g., Office to MsiExec) 
and remote resource fetching while filtering out legitimate enterprise installers.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity InstallUtil Proxy Execution (T1218.004)
- **ID:** `T1218_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the execution of InstallUtil.exe to proxy malicious code. 
Focuses on the /u flag, non-standard parent processes, and execution 
from writable directories, while filtering out legitimate .NET installations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Mshta Execution of Remote Script (High Fidelity)
- **ID:** `T1218_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious execution of mshta.exe used to run scripts directly from remote URLs, a common LOLBAS technique used by attackers for initial execution and payload staging.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Msiexec Installation from Remote URL (High Fidelity)
- **ID:** `T1218_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious use of msiexec.exe to install MSI packages directly from remote URLs, a technique commonly abused by attackers as a LOLBAS method. The rule focuses on attacker-typical command-line patterns and execution context to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Odbcconf Proxy Execution (T1218.008)
- **ID:** `T1218_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [ODBCCONF.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of odbcconf.exe to load malicious DLLs via the REGSVR action. 
Focuses on command-line anomalies, suspicious parent processes, and 
non-standard file paths to minimize false positives from legitimate installers.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Regsvcs/Regasm Proxy Execution (T1218.009)
- **ID:** `T1218_009.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of regsvcs.exe or regasm.exe to execute malicious .NET assemblies. 
Focuses on the /U flag for proxy execution, non-standard parent processes, 
and execution from writable/untrusted paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Regsvr32 Execution Indicative of LOLBAS Abuse (High Fidelity)
- **ID:** `T1218_010.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious usage of regsvr32.exe commonly associated with LOLBAS abuse (Squiblydoo technique), including execution of scriptlets, remote payloads, or DLLs from user-writable locations using attacker- typical command-line arguments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Rundll32 Execution with Script or Remote Payload (High Fidelity)
- **ID:** `T1218_011.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [SHELL32.DLL](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious usage of rundll32.exe commonly associated with LOLBAS abuse, including JavaScript execution, HTML applications, and loading payloads from remote or user-writable locations. The rule minimizes false positives by focusing on attacker-typical command-line patterns and execution context.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Verclsid Proxy Execution (T1218.012)
- **ID:** `T1218_012.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [VERCLSID.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of verclsid.exe to proxy the execution of malicious COM objects (DLLs). 
Filters out legitimate system-initiated verifications by focusing on suspicious 
parent-child relationships and anomalous command-line triggers.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Rundll32 Proxy Execution (T1218.013)
- **ID:** `T1218_013.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [PCWUTL.DLL](https://lolbas-project.github.io/lolbas/), [SHELL32.DLL](https://lolbas-project.github.io/lolbas/), [URL.DLL](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects anomalous rundll32.exe execution by focusing on suspicious command-line 
arguments, non-standard file extensions, and untrusted execution paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity MMC Proxy Execution (T1218.014)
- **ID:** `T1218_014.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the abuse of mmc.exe to execute malicious code via Component Object Model (COM) 
hijacking or untrusted console files (.msc). Filters out legitimate administrative actions.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Use of Legitimate Remote Administration Tools Outside Enterprise Pattern
- **ID:** `T1219.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects suspicious creation of services associated with legitimate remote administration tools (e.g. PsExec) when used outside approved enterprise management patterns. This behavior is commonly observed during lateral movement by attackers abusing admin tools.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity XSL Script Processing (T1220)
- **ID:** `T1220.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WMIC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious WMIC execution with XSL stylesheets located in non-standard 
directories or remote URLs, which is a common technique to bypass application 
whitelisting and execute arbitrary scripts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Office Template Injection (T1221)
- **ID:** `T1221.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects Microsoft Office applications fetching remote templates from non-Microsoft 
infrastructure, followed by the creation of temporary template files.


#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Permissions Modification (T1222)
- **ID:** `T1222.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious file permission modifications by identifying native tools 
(icacls, takeown) used with broad access flags (Full Control, Everyone) 
initiated by non-standard parent processes or from suspicious paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Windows File Permissions Modification (T1222.001)
- **ID:** `T1222_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted file permission modifications by identifying broad access 
grants (Full Control, Everyone) or inheritance blocking, initiated by 
suspicious/untrusted processes or targeting sensitive directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Linux File Permissions Modification (T1222.002)
- **ID:** `T1222_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects targeted Linux permission tampering by identifying high-risk 
attribute changes (SUID, Immutability) or mass modifications in sensitive 
system paths initiated by non-privileged or web-facing service accounts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Execution Guardrails Discovery (T1480)
- **ID:** `T1480.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted execution guardrails by identifying anomalous environment 
discovery patterns initiated by non-privileged users or suspicious parents, 
filtering out common administrative and system noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Environmental Keying Discovery (T1480.001)
- **ID:** `T1480_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted environmental keying by identifying hardware fingerprinting 
and machine-specific registry lookups initiated by suspicious, unbacked, 
or non-standard parent processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Domain Trust Discovery (T1482)
- **ID:** `T1482.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic enumeration of domain and forest trusts. 
Focuses on anomalous process lineage (e.g., interactive shells on workstations) 
and specific reconnaissance patterns used by tools like BloodHound/SharpHound.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Domain Policy Manipulation & GPO Abuse (T1484)
- **ID:** `T1484.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized modifications to critical Domain Policies by monitoring 
file system writes to the SYSVOL folder and GPO link changes, filtering out 
standard administrative tools (GPMC).


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Group Policy Modification & Abuse (T1484.001)
- **ID:** `T1484_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized GPO modifications by correlating file system writes to critical 
policy templates in SYSVOL with process-level anomalies. Filters out DFSR 
replication and standard GPMC management consoles to minimize false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Domain Trust Tampering & SID Filtering Bypass (T1484.002)
- **ID:** `T1484_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-risk modifications to Domain Trust relationships, focusing on 
the disabling of SID Filtering (Quarantine) and unauthorized trust creation. 
Correlates AD object changes with known administrative context.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Data Destruction (T1485)
- **ID:** `T1485.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CIPHER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WBADMIN.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic data destruction by monitoring for VSS deletion, 
secure file shredding (sdelete, cipher), and bulk recursive deletions 
initiated from suspicious parent processes or targeting non-temp directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ransomware Preparation Activity Detected on Windows Host (High Fidelity)
- **ID:** `T1486.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects ransomware preparation activity by identifying multiple recovery-inhibition and defense-evasion actions executed within a short time window. This includes disabling recovery options, deleting shadow copies, and stopping security-related services.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Service Stop (T1489)
- **ID:** `T1489.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized stopping of critical system and security services 
by monitoring service control tools originating from suspicious process 
lineages or targeting high-value defense mechanisms (EDR, VSS, AV).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Deletion of Volume Shadow Copies via VSSAdmin (High Fidelity)
- **ID:** `T1490.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious deletion of Volume Shadow Copies using vssadmin.exe, commonly observed during ransomware and destructive attacks. The rule focuses on attacker-typical command-line arguments, non-service execution context, and excludes known backup solutions to minimize false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Defacement (T1491)
- **ID:** `T1491.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized website defacement by monitoring for suspicious file 
manipulations (move, copy, echo) within web-root directories originating 
from non-standard or compromised service processes (e.g., w3wp.exe, httpd.exe).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Internal Defacement (T1491.001)
- **ID:** `T1491_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects internal system defacement by monitoring for unauthorized modifications 
to desktop wallpapers, legal notices, and logon banners via Registry or CLI, 
specifically filtering out GPO-driven and system-initiated changes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity External Defacement (T1491.002)
- **ID:** `T1491_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized external website defacement by identifying suspicious file 
manipulation commands (move, copy, echo) executed by web server worker processes 
within sensitive webroot directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Firmware Corruption (T1495)
- **ID:** `T1495.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WBEMTEST.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential firmware corruption or unauthorized flashing by monitoring 
low-level hardware access tools and firmware update utilities originating 
from untrusted process lineages (e.g., browsers, office apps, or temp folders).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Resource Hijacking (T1496)
- **ID:** `T1496.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized resource hijacking (cryptomining) by monitoring for 
specific miner protocols (stratum), algorithm flags, and hardware 
optimization arguments originating from untrusted process lineages.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Virtualization/Sandbox Evasion (T1497)
- **ID:** `T1497.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects sophisticated sandbox evasion by monitoring for rapid, multi-vector 
virtualization checks (BIOS, MAC, CPU, Disk) initiated by untrusted processes 
within suspicious directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## VM Artifact Discovery (T1497.001)
- **ID:** `T1497_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized discovery of virtualization artifacts by non-system, 
untrusted processes. Filters out legitimate installers and system services 
to focus on malware evasion techniques.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## User Interaction Evasion (T1497.002)
- **ID:** `T1497_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects sophisticated user interaction evasion by identifying un-signed or 
suspiciously located processes that query human-centric APIs (mouse, keyboard, recent files) 
without a legitimate UI context.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Time-based Evasion (T1497.003)
- **ID:** `T1497_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects sophisticated time-based evasion by monitoring non-standard delay mechanisms 
(ping, choice, timeout) initiated by untrusted binaries. Targets long-duration stalls 
used to exhaust sandbox analysis limits.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Network DoS (T1498)
- **ID:** `T1498.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [PKTMON.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted network denial of service attempts (flooding, amplification) 
by monitoring for low-level packet manipulation tools and high-bandwidth 
stress tests originating from untrusted or suspicious process lineages.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Direct Flow Flood (T1498.001)
- **ID:** `T1498_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [PKTMON.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-fidelity direct network flooding attempts (SYN, UDP, ICMP) 
by monitoring processes with aggressive packet generation parameters 
originating from untrusted or suspicious process lineages.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Endpoint Denial of Service (T1499)
- **ID:** `T1499.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence endpoint denial of service (DoS) attempts, including forced
termination of critical system processes (LSASS, CSRSS, Wininit, SMSS, Services)
and resource exhaustion via infinite loops or massive memory allocation.
Focuses on suspicious parent process lineages and untrusted execution paths
while filtering legitimate system maintenance, patching, and monitoring activities.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## OS Self-Destruction Detection (T1499.001)
- **ID:** `T1499_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [NTSD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence OS self-destruction attempts, including forced termination
of critical kernel processes (csrss.exe, wininit.exe, smss.exe, services.exe)
and malicious debugger abuse (ntsd.exe) aimed at triggering immediate BSOD.
Includes extensive filtering for trusted management, update operations, and
legitimate administrative automation.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Service Exhaustion Detection (T1499.002)
- **ID:** `T1499_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential endpoint denial-of-service (DoS) attempts via targeted service
exhaustion. Monitors unauthorized service stops, persistent configuration changes 
(disabling), and binary path modifications targeting security and critical 
infrastructure services. Filters out legitimate system management, patching, 
and monitoring activities to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## OS Self-Destruction Detection (T1499.003)
- **ID:** `T1499_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [CDB.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [NTSD.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted OS self-destruction attempts by monitoring forced termination
of critical Windows kernel processes (csrss.exe, wininit.exe, smss.exe, services.exe)
and malicious usage of system debuggers (ntsd.exe, cdb.exe) to trigger BSOD.
High-fidelity filters exclude trusted management, patching, and diagnostic processes
to minimize false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Resource Exhaustion Detection (T1499.004)
- **ID:** `T1499_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted resource exhaustion attempts (CPU, RAM, or IO) by monitoring
infinite loop constructs, massive memory allocations, and recursive process spawns
originating from suspicious or non-standard parent process lineages. 
Filters out legitimate automation, maintenance scripts, and development environments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Web Shell Execution Patterns (T1505)
- **ID:** `T1505.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [BASH.EXE](https://lolbas-project.github.io/lolbas/), [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence indicators of web shell activity by monitoring web server 
processes spawning interactive shells, reconnaissance utilities, or lateral movement tools. 
Includes strict filtering for legitimate .NET compilation, IIS administration, 
and authorized server maintenance tasks.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## SQL Server Command Shell Execution (T1505.001)
- **ID:** `T1505_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized OS command execution via Microsoft SQL Server using
extended stored procedures (xp_cmdshell) or CLR assemblies. 
Focuses on suspicious discovery commands, configuration changes, and shell execution
while filtering legitimate SQL Agent maintenance and installer operations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## IIS Native Module Injection (T1505.002)
- **ID:** `T1505_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NGEN.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized IIS native module registration or injection by monitoring
usage of appcmd.exe, direct edits to applicationHost.config or web.config, 
and DLL loads from non-standard, user-writable, or suspicious paths.
Focuses on anomalous command-line arguments and execution contexts to minimize
false positives from standard IIS or Windows servicing processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Webshell Upload or Interaction Detection (T1505.003)
- **ID:** `T1505_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects potential webshell activity by identifying suspicious script uploads
to web-accessible directories and subsequent attacker-style interactions
using command-execution style parameters. Focuses on anomalous paths, HTTP
methods, query parameters, and user agents, while minimizing false positives
from legitimate CMS or API functionality.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Mainboard Boot Image & SPI Flash Tampering (T1505.004)
- **ID:** `T1505_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized firmware manipulation and SPI flash tampering by monitoring
low-level hardware access tools, suspicious command-line flags, and driver 
registrations originating from non-standard process chains or user paths.
Focuses on boot image injection, SPI write operations, and untrusted execution contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Terminal Services DLL Hijacking Detection (T1505.005)
- **ID:** `T1505_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized modification or hijacking of Terminal Services (RDP) service DLLs 
and providers. Monitors ServiceDll and ProviderPath registry keys for tampering by 
untrusted processes, unusual paths, or suspicious actors, filtering legitimate 
system binaries and service operations to minimize false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Software Discovery Detection (T1518)
- **ID:** `T1518.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted software discovery with emphasis on security product enumeration.
Uses integrity level gating, parent-process correlation, output redirection, and
keyword-based filtering to minimize false positives from legitimate system inventory
tools or administrative scripts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Security Software Discovery Detection (T1518.001)
- **ID:** `T1518_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted discovery of security products such as AV, EDR, HIPS, and sandbox environments.
Focuses on keyword-specific enumeration, suspicious command-line usage (findstr, grep, Get-Process/Service),
and anomalous parent process lineages (Office apps, web servers, non-elevated shells).  
Also detects attempts to fingerprint virtual machines.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-Grade Unauthorized Container Image Execution (Implant Container Image)
- **ID:** `T1525.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects execution of container images that are not sourced from approved registries and are executed outside of CI/CD or system namespaces, indicating potential use of implanted container images for persistence or initial access.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Service Discovery Detection (T1526)
- **ID:** `T1526.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic cloud service enumeration targeting Lambda, Secrets, KeyVault,
WebApps, and container services. Focuses on anomalous execution environments such as
interactive shells on non-dev hosts and output redirection patterns used for automated
harvesting or exfiltration.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Application Token & Session Hijacking Detection (T1528)
- **ID:** `T1528.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized extraction of application access tokens and browser session cookies.
Monitors suspicious access to cloud CLI credentials (Azure, AWS, GCP) and browser credential
stores, originating from untrusted processes or non-standard parent process lineages. 
Flags attempts to copy, extract, or exfiltrate sensitive token data.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Unauthorized System Shutdown/Reboot Detection (T1529)
- **ID:** `T1529.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized or suspicious system shutdown or reboot commands.
Monitors forced shutdowns or reboots originating from untrusted process lineages 
(browsers, Office apps, scripts, temp folders) and filters legitimate system 
automation, administrative, or health check tasks.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Storage Data Theft Detection (T1530)
- **ID:** `T1530.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized data exfiltration from cloud storage providers (AWS, Azure, GCP)
by monitoring suspicious CLI arguments, inline credential injection, recursive copy
commands, and anomalous process lineages originating from non-admin or user contexts.
Covers aws, az, gsutil, rclone, mc and other cloud CLI tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Account Access Removal Detection (T1531)
- **ID:** `T1531.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized account removal or lockout attempts. Monitors bulk 
deletions, targeting of administrative accounts, and destructive account 
actions originating from non-standard processes such as Office apps, web servers, 
or scripts. Designed to reduce false positives while detecting T1531 techniques.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Internal Spearphishing Detection (T1534)
- **ID:** `T1534.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects advanced internal spearphishing attempts by monitoring anomalous 
programmatic access to the Outlook MAPI interface, suspicious child processes, 
dangerous command-line flags, and abnormal file attachments. 
Focuses on PowerShell, cmd, scripting engines, and non-browser parent anomalies.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Unused Service Manipulation Detection (T1535)
- **ID:** `T1535.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects modifications of Windows service ImagePath values to untrusted locations
or binaries. Monitors registry changes in services and filters out legitimate 
OS servicing, svchost, and common third-party updaters to ensure high-fidelity alerts.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Account Exfiltration Detection (T1537)
- **ID:** `T1537.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential cloud account exfiltration via native CLI tools. Monitors
cross-account synchronization, manual credential injection, and transfers 
initiated from non-administrative or suspicious process lineages. Covers 
AWS, Azure, GCP, and Snowball environments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Service Dashboard Discovery (T1538)
- **ID:** `T1538.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects anomalous cloud dashboard access and federated login token generation.
Focuses on suspicious CLI commands and browser launches that bypass MFA or
originate from non-interactive shells. Covers AWS, Azure, GCP, Okta, and 
other SaaS portals. Detects potential reconnaissance or lateral movement 
activity in cloud environments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Web Browser Session Cookie & Credential Theft Detection (T1539)
- **ID:** `T1539.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence browser session cookie and credential theft activity.
Identifies non-browser processes accessing Chromium and Firefox cookie databases,
encryption key files (Local State), or login databases. 
Focuses on LOLBins, scripting engines, DPAPI abuse, and staging/exfiltration behavior.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Pre-OS Boot Manipulation (T1542)
- **ID:** `T1542.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized firmware or bootloader modifications. Monitors for 
EFI partition mounting, unauthorized firmware flashing tool usage, and 
UEFI variable manipulation initiated from non-standard process trees. 
Filters out trusted vendor update utilities to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## ROM Kit & UEFI Firmware Tampering (T1542.001)
- **ID:** `T1542_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized firmware manipulation by monitoring high-risk driver 
registrations and firmware update utilities initiated from suspicious 
process trees, specifically targeting BYOVD and SPI flash access. 
Filters out trusted vendor update utilities to minimize false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Component Firmware Tampering (T1542.002)
- **ID:** `T1542_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized peripheral firmware (NIC, SSD, GPU) modification by 
monitoring stand-alone flashing tools initiated from untrusted process 
chains or non-standard file locations. Filters out trusted management 
tools to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Bootkit Persistence & EFI Tampering (T1542.003)
- **ID:** `T1542_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized bootloader modification by monitoring BCD integrity bypasses, 
manual EFI partition mounting, and suspicious boot path redirection. 
Filters out legitimate OS repairs and BitLocker operations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Mainboard Boot Image & SPI Flash Tampering (T1542.004)
- **ID:** `T1542_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized firmware manipulation by monitoring low-level hardware access 
tools and driver registrations initiated from non-standard process chains. 
Focuses on SPI flash writing and image injection attempts, while filtering 
trusted management tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## DHCP/PXE Boot Hijacking (T1542.005)
- **ID:** `T1542_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized modification of DHCP Options 66 (Boot Server) and 67 (Bootfile Name), 
which attackers use to redirect network boot requests to a malicious TFTP server. 
Filters trusted system services to reduce false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services
- **ID:** `T1543.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects suspicious behavior where a non-administrative user attempts to stop or modify multiple sensitive Windows services within a short time window. This behavior is commonly associated with defense evasion or persistence preparation activities.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro macOS Launch Agent Persistence Detection (T1543.001)
- **ID:** `T1543_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Detects unauthorized creation of Launch Agents by monitoring suspicious process lineages 
and identifying unsigned or script-based execution targets within the .plist.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Systemd Service Persistence (T1543.002)
- **ID:** `T1543_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Detects unauthorized creation or modification of systemd units by monitoring 
suspicious process lineages and unusual executable paths within the service file.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Unauthorized Windows Service Installation (T1543.003)
- **ID:** `T1543_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized Windows service creation by monitoring Event ID 7045 and process creation. 
Focuses on suspicious binary paths, shell-spawned services, and non-standard service executables.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Unauthorized macOS Launch Daemon (T1543.004)
- **ID:** `T1543_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Detects unauthorized creation of System Launch Daemons by monitoring file events 
and verifying the integrity of the writing process and the target binary signature.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro WMI Event Subscription Persistence (T1546.003)
- **ID:** `T1546.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized WMI event subscriptions by correlating consumer types with 
suspicious command-line patterns and excluding trusted system orchestrators.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro File Association Hijacking (T1546.001)
- **ID:** `T1546_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized changes to file associations in the Registry by monitoring 
suspicious actor processes and non-standard executable paths in 'shell\open\command'.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Screensaver Persistence Detection (T1546.002)
- **ID:** `T1546_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONTROL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized screensaver hijacking by monitoring Registry writes to 'SCRNSAVE.EXE'. 
Filters out GPO-driven changes and validates binary extensions and trusted paths.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## WMI Event Subscription Persistence via WMIC or PowerShell (High Fidelity)
- **ID:** `T1546_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WMIC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation of permanent WMI event subscriptions used for persistence. The rule focuses on attacker-typical combinations of EventFilter, CommandLineEventConsumer, and FilterToConsumerBinding created via WMIC or PowerShell within the root\subscription namespace, while excluding known enterprise monitoring agents.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro AppCert DLL Persistence Detection (T1546.004)
- **ID:** `T1546_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [REGEDIT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized registration of AppCert DLLs by monitoring the Session Manager 
Registry key. It filters out trusted system installers and requires non-standard 
paths or suspicious process lineages to trigger.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Shell Trap Persistence Detection (T1546.005)
- **ID:** `T1546_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized shell trap persistence by monitoring writes to shell profile files 
that include 'trap' commands combined with suspicious network payloads or execution patterns.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Mach-O LC_LOAD_DYLIB Injection (T1546.006)
- **ID:** `T1546_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized modification of Mach-O binaries to inject malicious dylibs. 
Focuses on non-developer tools modifying Application binaries and checks for 
suspicious dylib search paths or unsigned library loads.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Netsh Helper DLL Persistence (T1546.007)
- **ID:** `T1546_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized Netsh Helper DLL registration by monitoring Registry writes 
and command-line arguments. Filters out known-good installers and signed Microsoft binaries.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro WER SilentProcessExit Persistence (T1546.008)
- **ID:** `T1546_008.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WINDBG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized persistence via Windows Error Reporting (WER) SilentProcessExit. 
Focuses on the registration of 'MonitorProcess' commands which execute when a process 
crashes or exits, excluding known debugging environments.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro AppInit_DLLs Persistence Detection (T1546.009)
- **ID:** `T1546_009.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized persistence via AppInit_DLLs by monitoring Registry writes 
to the 'AppInit_DLLs' and 'LoadAppInit_DLLs' values. 
Filters out signed Microsoft binaries and trusted system installers.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro AppCert DLL Persistence Detection (T1546.010)
- **ID:** `T1546_010.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [REGEDIT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized registration of AppCert DLLs by monitoring the Session Manager 
Registry key. It filters out trusted system installers and requires non-standard 
paths or suspicious process lineages to trigger.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Application Shimming Persistence Detection (T1546.011)
- **ID:** `T1546_011.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized Shim database installation by monitoring sdbinst.exe 
execution with suspicious source paths and direct Registry writes to InstalledSDB.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro IFEO Debugger Hijacking Detection (T1546.012)
- **ID:** `T1546_012.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [ATBROKER.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized Debugger injection via Image File Execution Options (IFEO). 
Filters out legitimate developer tools and focuses on high-risk system binaries 
and accessibility features (Sticky Keys, Utility Manager).


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro PowerShell Profile Injection Detection (T1546.013)
- **ID:** `T1546_013.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized automated modification of PowerShell profiles. 
Filters out legitimate manual editing via text editors and focuses on 
programmatic injection from shells or non-standard parent processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro WMI Event Subscription Persistence (T1546.014)
- **ID:** `T1546_014.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized WMI event subscriptions by monitoring the creation of 
EventFilters and Command/Script Consumers. Filters out known administrative 
tools and focuses on non-standard scripted execution.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious COM Hijacking for User-Level Persistence (High Fidelity)
- **ID:** `T1546_015.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious COM hijacking attempts used for user-level persistence by monitoring registry modifications of CLSID InprocServer32 and LocalServer32 entries pointing to non-standard execution paths. The rule focuses on HKCU modifications combined with scripting or LOLBin execution to reduce false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro MSI Installer Custom Action Persistence (T1546.016)
- **ID:** `T1546_016.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by msiexec.exe originating from non-standard 
directories. This targets malicious MSI Custom Actions used for persistence or privilege escalation.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása
- **ID:** `T1547.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a gyanús beállításjegyzékbeli vagy indítómappák módosításait, amelyeket az adatok megőrzése érdekében használnak, a nem szabványos elérési utakra és a gyanús végrehajtókra összpontosítva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Registry Run Key Modification for User Persistence (High Fidelity)
- **ID:** `T1547_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious registry modifications used to establish user-level persistence via Windows Run and RunOnce keys. The rule focuses on non-standard executable locations combined with scripting engines to reduce false positives from legitimate software installations.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity LSA Authentication Package Persistence
- **ID:** `T1547_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the addition of unauthorized Authentication Packages in the LSA registry key.
Attackers use this for SYSTEM-level persistence and credential harvesting.
This rule filters standard Windows packages and monitors for DLLs outside System32.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Time Provider Persistence (T1547.003)
- **ID:** `T1547_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects the registration of a new Windows Time Provider. 
Attackers use this for SYSTEM-level persistence by loading a malicious DLL into svchost.exe.
This rule filters standard Windows DLLs and targets non-System32 paths.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Winlogon Helper DLL Persistence (T1547.004)
- **ID:** `T1547_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized modifications to Winlogon helper keys (Userinit, Shell). 
Focuses on 'appending' multiple executables or using non-standard system paths.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity SSP DLL Persistence (T1547.005)
- **ID:** `T1547_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the addition of unauthorized DLLs to the LSA Security Packages registry key.
Attackers use this for persistence and cleartext credential theft.
Filters standard Windows SSPs and alerts on unmanaged modifications.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Kernel Driver Registration (T1547.006)
- **ID:** `T1547_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the registration of a new kernel-mode driver service.
Attackers use this for rootkit-level persistence and to disable security tools.
Optimized to flag drivers in non-standard paths and suspicious manual service creation.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Browser Session Persistence (T1547.007)
- **ID:** `T1547_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized modification of browser session or preference files by non-browser processes. 
Attackers use this to force browsers to open malicious URLs upon startup for persistence.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity LSASS Driver/Package Persistence (T1547.008)
- **ID:** `T1547_008.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the registration of new LSA plugins, notification packages, or drivers. 
Attackers use this to load malicious code into the lsass.exe process for 
persistence and real-time credential harvesting.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Shortcut Modification Detection
- **ID:** `T1547_009.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation or modification of LNK files by suspicious processes (PowerShell, CMD, etc.)
in startup folders or taskbar paths. This is a common technique for persistence.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity AppCert DLL Persistence (T1547.010)
- **ID:** `T1547_010.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized registration of AppCert DLLs. These DLLs are loaded into 
every process that calls CreateProcess, making it a powerful persistence and injection vector.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Application Shimming Persistence (T1547.011)
- **ID:** `T1547_011.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the installation of a new Shim database (.sdb) using sdbinst.exe.
Attackers use shims to inject DLLs, bypass security controls, or maintain persistence.
This rule filters legit installers and flags suspicious parent-child relationships.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity COM Hijacking Persistence (T1547.012)
- **ID:** `T1547_012.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation of COM object handlers in HKCU that point to suspicious locations.
Focuses on InprocServer32 and LocalServer32 keys, which are primary targets for hijacking.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Email Client Helper Persistence (T1547.013)
- **ID:** `T1547_013.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the registration of unauthorized email client helpers or COM add-ins.
Focuses on DLLs registered from user-writable paths and suspicious registry writers.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Active Setup Persistence (T1547.014)
- **ID:** `T1547_014.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation or modification of Active Setup 'StubPath' registry keys by non-system processes.
Attackers use this to achieve persistence that executes once per user upon logon.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity COM Hijacking Persistence (T1547.015)
- **ID:** `T1547_015.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation of COM object handlers in HKCU that point to suspicious, 
user-writable locations. Attackers hijack CLSIDs to achieve stealthy persistence 
within legitimate system processes like explorer.exe.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Privilege Escalation via Registry Hijacking (T1548)
- **ID:** `T1548.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [COMPUTERDEFAULTS.EXE](https://lolbas-project.github.io/lolbas/), [EVENTVWR.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects UAC bypass and privilege escalation attempts by monitoring unauthorized 
Registry modifications to shell open commands. Filters out trusted installers 
and system-initiated changes to reduce false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Setuid/Setgid Bit Manipulation (T1548.001)
- **ID:** `T1548_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized SUID/SGID bit escalation by monitoring chmod/chown execution 
in world-writable directories, suspicious shell-origin actions, and reconnaissance 
patterns using find, while excluding trusted package managers and automation tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## UAC Bypass via Fodhelper Registry Hijack (High Fidelity)
- **ID:** `T1548_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects UAC bypass attempts abusing fodhelper.exe by monitoring registry hijacking of the ms-settings protocol combined with suspicious child process execution. This rule focuses on user-context auto-elevation to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Sudoers Manipulation and Sudo Abuse (T1548.003)
- **ID:** `T1548_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized sudoers file modifications and sudo caching abuse. 
Focuses on NOPASSWD additions, timestamp_timeout manipulation, and 
dangerous environment variable injections like LD_PRELOAD. Excludes 
trusted automation tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## AppleScript Privilege Escalation (T1548.004)
- **ID:** `T1548_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized AppleScript elevation attempts by monitoring osascript execution 
with "administrator privileges" from untrusted parent processes such as browsers, office suites, 
collaboration apps, or temporary directories, while excluding trusted system management tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## SUID Desktop Entry & Shortcut Abuse (T1548.005)
- **ID:** `T1548_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Detects unauthorized modifications of XDG desktop entries or shortcuts that attempt 
to execute SUID binaries or leverage pkexec for privilege escalation. 
Focuses on modifications in user-writable directories by untrusted processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Alternate Authentication Material (T1550)
- **ID:** `T1550.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects the use of stolen hashes or tickets for lateral movement by identifying 
NTLM/Kerberos protocol anomalies, including RC4 encryption downgrades and 
restricted admin logon types, while excluding legitimate system management tools.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Application Access Token Abuse (T1550.001)
- **ID:** `T1550_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the theft or misuse of application access tokens by monitoring unauthorized 
access to IdentityCRL and TokenBroker stores, as well as the use of bearer tokens 
in command-line utilities, excluding legitimate Azure CLI and browser processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Pass-the-Hash Detection (T1550.002)
- **ID:** `T1550_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects Pass-the-Hash (PtH) attacks by identifying anomalous NTLM loopback authentication, 
restricted admin logons (LogonType 9 via seclogo), and credential injection tool activity, 
while excluding legitimate service and machine accounts.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Pass-the-Ticket Detection (T1550.003)
- **ID:** `T1550_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects Pass-the-Ticket (PtH) attacks by identifying Kerberos encryption downgrades (RC4), 
anomalous ticket flags typical of Rubeus/Mimikatz, and unauthorized ticket injection 
into LSA process memory.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Pass-the-Session Detection (T1550.004)
- **ID:** `T1550_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized attempts to steal web sessions by monitoring non-browser processes 
accessing both the encrypted AES key (Local State) and browser cookie databases.
Excludes legitimate browser update, utility, and synchronization processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Unsecured Credentials Discovery (T1552)
- **ID:** `T1552.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted discovery of credentials across files, registry, 
and shell history. Correlates search tools (findstr, grep, PowerShell)
with high-risk file types, sensitive keywords, and suspicious execution
contexts to minimize false positives while identifying credential harvesting.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Credentials In Files Discovery (T1552.001)
- **ID:** `T1552_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized, recursive discovery of credentials stored in files 
and configuration scripts (AWS, Git, SSH keys, password/config files). 
Correlates search tools with sensitive file extensions, exfiltration patterns, 
and suspicious parent processes to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Credentials In Registry Discovery (T1552.002)
- **ID:** `T1552_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized discovery or extraction of credentials stored in
Windows Registry (PuTTY, WinSCP, RDP, LSA secrets, SAM, VPN clients).
Correlates registry enumeration or export commands with suspicious
parent processes, recursive search patterns, and non-system user context
to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Shell History & Console Discovery (T1552.003)
- **ID:** `T1552_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BASH.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized discovery or extraction of shell history files 
(bash, zsh, ConsoleHost, database shells, Python REPL). 
Focuses on exfiltration commands, non-shell processes accessing history files, 
obfuscated PowerShell usage, and remote or web server contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Private Key Discovery (T1552.004)
- **ID:** `T1552_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [SSH.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted discovery or collection attempts of private cryptographic
keys (SSH, PGP, TLS certificates). Focuses on recursive file enumeration,
private key header searches, sensitive directory traversal, encoding or
export behavior, and suspicious execution context.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Credential Discovery (T1552.005)
- **ID:** `T1552_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized discovery or extraction of cloud credentials
(AWS, Azure, GCP, Docker) from local configuration files. Focuses on
suspicious access patterns, encoding, redirection, remote execution
context, and abnormal process lineage while reducing false positives
from legitimate CLI activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Credentials in Files Discovery (T1552.006)
- **ID:** `T1552_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized manual or scripted discovery of credentials stored
in configuration or policy files, including Group Policy Preferences (GPP),
unattended installation files, web.config, and other plaintext or weakly
protected credential artifacts. Focuses on string-search activity,
sensitive file targeting, and remote execution context while excluding
legitimate system processing.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Container Secret Discovery (T1552.007)
- **ID:** `T1552_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects targeted discovery of sensitive credentials inside containers,
including Kubernetes service account tokens, mounted secrets, cloud
provider keys, and environment variables. Focuses on interactive
shell execution, command chaining, and abnormal process lineage
while filtering legitimate entrypoint and monitoring activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## GPP Password Discovery (T1552.008)
- **ID:** `T1552_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted discovery of encrypted Group Policy Preference (GPP)
passwords (cpassword) within SYSVOL shares. Focuses on command-line
string searches, PowerShell enumeration, remote execution context,
and abnormal user activity to reduce false positives from legitimate
Group Policy processing.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Subvert Trust Controls (T1553)
- **ID:** `T1553.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to subvert Windows trust controls including forced
root certificate installation and Mark-of-the-Web (MotW) / Security
Zone manipulation. Focuses on suspicious execution context, non-standard
source paths, and abnormal parent-child relationships to reduce
enterprise deployment false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## macOS Gatekeeper and Quarantine Bypass (T1553.001)
- **ID:** `T1553_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects attempts to globally disable Gatekeeper or programmatically
remove the com.apple.quarantine attribute from files. Focuses on
non-interactive execution, suspicious file locations, and abnormal
parent-child relationships to reduce developer and administrative
false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## SIP Hijacking and Trust Subversion (T1553.002)
- **ID:** `T1553_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious modification of Subject Interface Packages (SIP),
Trust Providers, or WinVerifyTrust-related registry keys. Focuses on
DLL redirection to user-writable paths, anomalous execution context,
and high-risk parent processes commonly associated with trust
subversion and signature validation bypass techniques.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows Catalog Database Subversion (T1553.003)
- **ID:** `T1553_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious manipulation or unauthorized addition of catalog files
to the Windows Code Integrity Catalog Database (CatRoot / CatRoot2).
Focuses on high-risk tooling, abnormal parent-child relationships,
non-standard source paths, and uncommon user contexts to reduce
enterprise deployment false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Root Certificate Injection (T1553.004)
- **ID:** `T1553_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-risk programmatic installation of a Root Certificate into
the Windows Trusted Root or AuthRoot stores. Focuses on suspicious
command-line flags, non-standard certificate file locations, and
uncommon parent-child process relationships to significantly reduce
enterprise deployment false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Mark-of-the-Web (MotW) Bypass & Zone Subversion Detection (T1553.005)
- **ID:** `T1553_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects programmatic removal or tampering of the Mark of the Web (MotW) via Alternate Data Stream (Zone.Identifier) manipulation or registry-based security zone downgrades. Focuses on non-interactive script execution and suspicious zone configuration changes while filtering legitimate installers and browser activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows Code Integrity & DSE Subversion Detection (T1553.006)
- **ID:** `T1553_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to subvert Windows Code Integrity and Driver Signature Enforcement (DSE) via BCDEDIT flags or registry modifications that allow unsigned kernel drivers to load, while filtering legitimate OS maintenance, installer, and trusted system processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Client Binary Integrity Compromise (T1554)
- **ID:** `T1554.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the modification or replacement of trusted client binaries by unauthorized processes. 
Focuses on cases where the writing process is a LOLBin or the file lacks a valid vendor signature.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nem böngészős folyamat hozzáférése a böngésző hitelesítőadat-tárolóihoz (High Fidelity)
- **ID:** `T1555.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a böngésző hitelesítőadat-tároló fájljaihoz való gyanús hozzáférést nem böngészőfolyamatok által. A szabály az ismert hitelesítőadat-adatbázisokhoz való olvasási hozzáférésre összpontosít, valamint a gyanús végrehajtási kontextusra, hogy csökkentse a téves riasztásokat, amelyek a biztonsági mentési ügynököktől, víruskereső szoftverektől és böngészőfrissítésektől származnak.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows Vault Credential Harvesting Detection (T1555.001)
- **ID:** `T1555_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential unauthorized extraction of Windows Vault credentials by monitoring vaultcmd.exe usage, API strings, and suspicious command-line data redirection from  untrusted contexts, while filtering legitimate browsers and system processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Securityd Memory Dumping Detection (T1555.002)
- **ID:** `T1555_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized attempts to access or dump memory of the 'securityd' process or keychain database on macOS. Monitors suspicious debugger and memory tools usage while filtering legitimate Apple-signed diagnostic utilities and Xcode development tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Browser Credential Harvesting Detection (T1555.003)
- **ID:** `T1555_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential unauthorized access and exfiltration of browser credential databases  (Chrome, Edge, Firefox, Brave) by monitoring suspicious command-line file operations  targeting 'Login Data', 'Cookies', 'Web Data', 'key4.db', or 'logins.json'. Filters  legitimate browser processes and backup/sync tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows Credential Manager Harvesting Detection (T1555.004)
- **ID:** `T1555_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CMDKEY.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential unauthorized credential harvesting via Windows Credential Manager (cmdkey.exe) by monitoring suspicious command-line usage, redirection, untrusted parent processes, and  non-interactive execution contexts. Filters legitimate IT management scripts and user activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Password Manager Extraction Detection (T1555.005)
- **ID:** `T1555_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential unauthorized access or exfiltration of password manager  databases (e.g., KeePass, 1Password, Bitwarden) by monitoring suspicious  file operations targeting vault files (.kdbx, .opvault, .agilekeychain, key3.db, key4.db)  and untrusted process execution contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Secret Harvesting Detection (T1555.006)
- **ID:** `T1555_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized access or exfiltration of cloud provider credentials  (AWS, Azure, GCP, Docker) by monitoring suspicious command-line activity and  tools accessing sensitive configuration paths. Filters official cloud CLI binaries  and known DevOps agents to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-Grade Authentication Process Hijack via Suspicious DLL Registration
- **ID:** `T1556.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects exploitation-grade modification of the Windows authentication process where a non-system process registers a new authentication-related DLL from a user-writable directory into LSA, SSP, or Credential Provider registry locations, strongly indicating credential interception.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-Grade Security Support Provider Hijacking (LSA SSP)
- **ID:** `T1556_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects exploitation-grade Security Support Provider (SSP) hijacking by identifying unauthorized modification of the LSA Security Packages registry value to register a new, non-system DLL from a user-writable directory by a non-trusted process or account.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-Grade Password Filter DLL Hijacking via LSA Notification Packages
- **ID:** `T1556_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects exploitation-grade installation of a malicious Password Filter DLL by identifying unauthorized modification of the LSA Notification Packages registry value to add a new DLL located in a user-writable directory by a non-trusted process or account. This behavior strongly indicates credential interception on Domain Controllers.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003)
- **ID:** `T1556_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized modification of PAM configuration or binary modules 
by identifying non-package-manager writes to /etc/pam.d/ and /lib/security/.
Specifically filters for automated configuration tools to reduce false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Network Device Authentication Hijacking (T1556.004)
- **ID:** `T1556_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)
- **Leírás:** Detects unauthorized modifications to AAA (Authentication, Authorization, and Accounting) 
settings or local user databases on network devices. Focuses on manual bypasses 
performed outside of authorized management subnets.


#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro SID History Injection Correlation (T1556.005)
- **ID:** `T1556_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects the injection of highly privileged SIDs into the sIDHistory attribute of a user. 
This targets the "Ghost Admin" scenario where a user gains Domain Admin rights 
without being a member of the group.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Entra ID MFA Method Hijacking (T1556.006)
- **ID:** `T1556_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-risk modifications to MFA methods in Entra ID by correlating 
successful method changes with suspicious entry points or administrative anomalies.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hybrid Identity Sync Manipulation Detection (T1556.007)
- **ID:** `T1556_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential unauthorized manipulation of Entra ID / Azure AD Connect  synchronization processes (MITRE ATT&CK T1556.007). Monitors MSOL account abuse  from non-sync servers, unauthorized ADSync PowerShell usage, and suspicious  database access for credential or password manipulation.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Network-to-Cloud Auth Hijacking Detection (T1556.008)
- **ID:** `T1556_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-risk modifications to enterprise applications, service principals,  and conditional access policies in Azure that could indicate network-to-cloud  authentication hijacking (MITRE ATT&CK T1556.008). Focuses on MFA bypasses,  unauthorized credential additions, and suspicious service principal changes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Adversary-in-the-Middle Detection (T1557)
- **ID:** `T1557.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential Adversary-in-the-Middle (AiTM) attacks (MITRE ATT&CK T1557)  by monitoring unauthorized system configuration changes such as IP forwarding  enablement and execution of LLMNR/NetBIOS/ARP poisoning tools from untrusted locations.  Filters legitimate virtualization and VPN activity to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## LLMNR/NBT-NS Poisoning & SMB Relay Detection (T1557.001)
- **ID:** `T1557_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential LLMNR/NBT-NS poisoning and SMB relay activity (MITRE ATT&CK T1557.001)  by monitoring unauthorized processes attempting to bind to network resolution ports  and executing known attack tools with suspicious command-line arguments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rogue ARP Poisoning / MITM Detection (T1557.002)
- **ID:** `T1557_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential ARP poisoning or MITM attempts (MITRE ATT&CK T1557.002) by monitoring  IP forwarding enablement and suspicious packet manipulation tools executed from untrusted locations. Filters out legitimate virtualization, VPN, and network diagnostic activity to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rogue DHCP / DHCP Spoofing Detection (T1557.003)
- **ID:** `T1557_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential rogue DHCP server activity indicative of DHCP spoofing (MITRE ATT&CK T1557.003). The rule identifies suspicious processes attempting to launch DHCP-related services with gateway/DNS manipulation arguments from non-standard locations and non-system users. Designed to reduce false positives by filtering legitimate virtualization and native DHCP services.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Kerberos Attack Detection
- **ID:** `T1558.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects advanced Kerberos credential attacks including ticket 
forgery, AS-REP roasting, Kerberoasting, and ticket injection.

Features:
  - Encryption downgrade (RC4/0x17) detection
  - Offensive tool flags (Rubeus, Mimikatz, Impacket, PowerView)
  - Ticket type-specific parameters (Golden, Silver, AS-REP)
  - Parent process and temp execution context gating
  - Enterprise FP filtering (LSASS, SYSTEM, monitoring tools)


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Golden Ticket Forgery & Injection
- **ID:** `T1558_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence Golden Ticket creation and injection activity.

Coverage includes:

  - KRBTGT hash or AES key requirement
  - SID specification
  - Pass-the-Ticket (/ptt) or kerberos::ptt injection
  - Mimikatz or Rubeus Golden Ticket usage patterns
  - Enterprise FP filters (LSASS/system/monitoring)

Focused on ATT&CK T1558.001.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Silver Ticket Forgery & Injection
- **ID:** `T1558_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence Silver Ticket creation and injection activity.

Coverage includes:

  - Service-specific SPN targeting (cifs, http, mssql, ldap)
  - Service account hash material (RC4 / AES128 / AES256)
  - SID specification
  - Pass-the-ticket (/ptt) injection
  - Mimikatz and Rubeus Silver ticket usage patterns

Focused on ATT&CK T1558.002.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús Kerberos TGS jegykérés (Kerberoasting)
- **ID:** `T1558_003.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Észleli a gyanús Kerberos Service Ticket (TGS) kéréseket, amelyek Kerberoasting támadásra utalhatnak.  A szabály fókuszál a gyenge titkosítási típusokra (RC4) és szűri a gyakori legális zajt.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity AS-REP Roasting & LDAP Enumeration
- **ID:** `T1558_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence AS-REP Roasting activity targeting accounts with
DONT_REQ_PREAUTH (UAC 4194304).

Coverage includes:

  - LDAP bitwise filters for DONT_REQ_PREAUTH
  - Rubeus / Impacket / PowerView AS-REP roasting usage
  - Hash export formatting (hashcat / john)
  - Suspicious PowerShell or remote execution lineage

Focused on ATT&CK T1558.004.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Indirect IPC and COM Execution
- **ID:** `T1559.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious indirect process creation via COM/DDE/WMI. 
Focuses on 'orphan' processes where an Office app or browser triggers 
a system proxy to execute code, bypassing standard parent-child monitoring.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús elnevezett csővezeték-létrehozás, amely utólagos kihasználási eszközökhöz kapcsolódik (High Fidelity)
- **ID:** `T1559_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A gyanús nevesített csővezetékek létrehozásának nagy pontosságú észlelése, amelyek gyakran kapcsolódnak az oldalirányú mozgáshoz és a kihasználás utáni keretrendszerekhez. A szabály az ismert rosszindulatú csővezeték-neveket, a véletlenszerű csővezeték-mintákat, a LOLBin végrehajtási kontextust és a szigorú engedélyezési listákat ötvözi a téves riasztások minimalizálása érdekében.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Office DDE Contextual Anomaly
- **ID:** `T1559_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious process spawning via Microsoft Office Dynamic Data Exchange (DDE). 
Filters legitimate financial data links (Excel) and focuses on Office apps launching 
interpreters or LOLBins with DDE-specific command-line markers.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Hypervisor API and VM Escape Research
- **ID:** `T1559_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized interaction with hypervisor APIs and diagnostic tools. 
Focuses on manual execution from interactive shells and suspicious command-line 
parameters associated with VM escape or sandbox evasion.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Adatok gyanús archiválása exfiltráció céljából
- **ID:** `T1560.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a fájlok gyanús tömörítését és archiválását (7z, rar, tar, PowerShell), különösen ha jelszavas védelmet  alkalmaznak vagy gyanús ideiglenes könyvtárakat használnak célhelyként.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Data Archiving for Exfiltration
- **ID:** `T1560_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence data staging for exfiltration using third-party
archiving utilities or PowerShell compression.

Coverage includes:

  - 7-Zip / WinRAR / tar / zip archive creation
  - Password-protected archives
  - Volume splitting
  - Delete-after-archive behavior
  - Sensitive data targeting
  - Suspicious interactive or web execution context

Focused on ATT&CK T1560.001 (Archive via Utility).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Data Archiving via Library
- **ID:** `T1560_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence data staging for exfiltration using .NET or 
PowerShell compression libraries.

Coverage includes:

  - Direct use of System.IO.Compression APIs
  - PowerShell Compress-Archive with user/server data targeting
  - Archive creation followed by encoding behavior
  - Suspicious execution lineage (webserver, macro, shell)

Focused on ATT&CK T1560.002 (Archive via Library).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Archive via Custom Method
- **ID:** `T1560_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence custom data collection and staging activity using
byte-level file access and manual encoding/obfuscation routines.

Coverage includes:

  - Raw byte-level file access (ReadAllBytes, MemoryStream)
  - Manual Base64/XOR/bitwise encoding
  - Recursive file enumeration for staging
  - Suspicious execution context (web server, shell, temp execution)

Focused on ATT&CK T1560.003 (Archive via Custom Method).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Disk Wipe
- **ID:** `T1561.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence destructive disk operations including:

  - Raw physical disk overwrite (MBR / GPT destruction)
  - Partition table wiping (diskpart clean/delete)
  - Full-disk content overwrite (dd, zero/random streams)
  - Destructive PowerShell disk clearing
  - Suspicious execution context (macro/webshell/LOLBIN)

Focused on ransomware and destructive wiper activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Disk Content Wipe
- **ID:** `T1561_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence destructive disk wiping activity via
raw device access or destructive overwrite operations.

Coverage includes:

  - Direct raw disk access (\\.\PhysicalDrive, \\.\Harddisk)
  - Overwrite using zero/random data streams
  - SDelete secure wipe with multiple passes
  - PowerShell destructive disk clearing
  - Suspicious execution context (macro, webshell, temp execution)

Focused on ransomware-style impact activity (T1561.001).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Disk Structure Wipe
- **ID:** `T1561_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence destructive disk structure operations including:

  - Partition table wiping (diskpart clean / delete partition)
  - MBR overwrite (first 512 bytes overwrite patterns)
  - Raw physical drive writes
  - Destructive PowerShell disk clearing
  - Suspicious execution context (macro/webshell/LOLBIN)

Focused on ransomware and destructive wiper behavior (T1561.002).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Biztonsági szolgáltatások gyanús leállítása
- **ID:** `T1562.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a kritikus biztonsági szolgáltatások (Antivírus, EDR, Tűzfal) leállítására irányuló kísérleteket  olyan eszközökkel, mint a net.exe, sc.exe vagy PowerShell. Ez a védelem kiiktatására irányuló támadói tevékenység.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows Defender védelem kikapcsolása vagy módosítása PowerShell segítségével
- **ID:** `T1562_001.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli, amikor a támadók PowerShell segítségével próbálják megváltoztatni a Windows Defender beállításait,  például a valós idejű védelem kikapcsolásával vagy kivételek hozzáadásával. Ez a technika a védelem megkerülésére szolgál.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows Event Log Service Impairment
- **ID:** `T1562_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence attempts to disable, stop, or impair Windows Event Logging.

Coverage includes:
  - wevtutil channel disabling or log clearing
  - EventLog service stop/disable attempts (sc, net, PowerShell)
  - Registry-based service or channel modification
  - Service dependency tampering (DependOnService)

Aligned with MITRE ATT&CK T1562.002.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Command History Logging Impairment
- **ID:** `T1562_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence attempts to suppress, redirect, or tamper with
interactive command history logging on Windows systems.

Detection coverage includes:

  - PowerShell PSReadLine logging suppression (SaveNothing, HistorySavePath abuse)
  - History file deletion (ConsoleHost_history.txt, PSReadLine folder, bash history)
  - Registry-based console history buffer suppression
  - Encoded PowerShell modifying history behavior

Aligned with MITRE ATT&CK T1562.003 (Impair Command History Logging).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Firewall Modification via Netsh.exe
- **ID:** `T1562_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli, amikor a támadók a netsh.exe eszközt használják a Windows tűzfal szabályainak módosítására vagy új,  engedékeny szabályok hozzáadására. Ez gyakran a védelem megkerülésére (Impair Defenses) utal.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Indicator Blocking and Telemetry Suppression
- **ID:** `T1562_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence attempts to disable, suppress, or interfere with Windows
security telemetry and monitoring pipelines, including:

  - Stopping or deleting ETW trace sessions
  - Disabling or modifying Windows Event Forwarding (WEF)
  - Creating outbound firewall rules to block security telemetry (EDR/AV over HTTPS)

Focuses on defense evasion aligned to MITRE ATT&CK T1562.006.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Firewall Impairment (T1562.007)
- **ID:** `T1562_007.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-risk modifications to cloud firewalls and security groups
that may expose resources to the internet or weaken segmentation.
Focuses on ANY/ANY rules, privileged port exposure, and anomalous identities.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Logging Impairment (T1562.008)
- **ID:** `T1562_008.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects attempts to impair cloud logging visibility by disabling,
deleting, or weakening CloudTrail and Azure logging configurations.
Focuses on trail deletion, log validation disablement, event selector
downgrades, and storage tampering initiated by anomalous identities.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Safe Mode Defense Evasion (T1562.009)
- **ID:** `T1562_009.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects malicious attempts to force Windows into Safe Mode to bypass 
security controls. Focuses on BCDEdit safeboot configuration changes, 
SafeBoot registry manipulation, and coordinated forced reboot activity 
originating from suspicious execution contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Defense Downgrade Attack (T1562.010)
- **ID:** `T1562_010.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects deliberate security downgrade attempts targeting PowerShell engine
rollback (v2 AMSI bypass), NTLM authentication weakening, and encryption
protocol reduction. Focuses on downgrade intent combined with suspicious
execution context to reduce false positives from legitimate administration.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Virtualization and Sandbox Evasion (T1564.011)
- **ID:** `T1562_011.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted environment fingerprinting used to identify virtualization,
sandbox, or malware analysis environments. Correlates WMI hardware queries,
VM vendor string checks, MAC OUI reconnaissance, and VM-specific driver
discovery initiated from suspicious process chains or user-writable paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Security Infrastructure Impairment (T1562.012)
- **ID:** `T1562_012.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects targeted attempts to impair AWS-native security controls such as 
GuardDuty, Security Hub, and related threat intelligence mechanisms.
Focuses on detector deletion, suppression rule abuse, and threat intel tampering 
initiated by root, non-MFA, or non-automated identities.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Remote Service Session Hijacking (T1563)
- **ID:** `T1563.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects RDP/Terminal Services session hijacking via tscon.exe by correlating:
- Hijack-specific command-line parameters
- SYSTEM integrity execution
- Lateral movement or shell-based parent processes
Explicitly filters legitimate RDS/VDI orchestration and service contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Local Session Hijacking (T1563.001)
- **ID:** `T1563_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects advanced local session hijacking attempts where tscon.exe is used 
to attach to existing user sessions. High-fidelity detection combines:
- Suspicious command-line arguments targeting console or RDP sessions
- SYSTEM-level execution context
- Untrusted parent processes (shells, lateral movement tools, Office apps)
Legitimate RDS/VDI management tools are explicitly filtered out.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## RDP Session Hijacking (T1563.002)
- **ID:** `T1563_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized RDP session hijacking and shadowing attempts.
High-fidelity detection leverages:
- SYSTEM-level execution context
- Anomalous parent processes (shells, lateral movement tools)
- 'No-consent' shadowing parameters
Excludes legitimate RDP and remote support tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hide Artifacts Detection (T1564)
- **ID:** `T1564.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted artifact hiding techniques including:
- NTFS Alternative Data Streams (ADS)
- Registry-based user account hiding
- Suspicious file attribute manipulation
Initiated by untrusted parent processes or from user-writable/non-standard paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hidden File Attribute Manipulation (T1564.001)
- **ID:** `T1564_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious use of file and directory hiding via System (+s) and Hidden (+h) attributes.
Focuses on untrusted parent processes, sensitive user-writable directories, and avoids 
known safe system or automation activities.  


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hidden User Account Creation (T1564.002)
- **ID:** `T1564_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BASH.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to hide Windows user accounts from the logon screen by 
monitoring modifications to 'SpecialAccounts\UserList' and related registry keys.
Focuses on suspicious parent processes, non-system users, and untrusted execution paths,
while filtering out legitimate system installers and administrative automation.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hidden Window Execution (T1564.003)
- **ID:** `T1564_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious process execution with hidden windows, 
focusing on stealth flags, obfuscation techniques, and untrusted parent processes. 
Designed to catch attempts to evade user and EDR visibility while minimizing false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## NTFS Alternative Data Stream (ADS) Abuse (T1564.004)
- **ID:** `T1564_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects creation, modification, or execution of NTFS Alternative Data Streams (ADS) 
often used to hide malicious payloads or evade endpoint monitoring. 
Correlates redirection operators, LOLBins, and stream-specific PowerShell commands 
while minimizing false positives from MOTW and system files.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hidden File System Manipulation (T1564.005)
- **ID:** `T1564_005.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious mounting, creation, or manipulation of virtual disk images 
(VHD, VHDX, ISO) by monitoring CLI commands from untrusted parent processes or 
non-standard paths. This technique is commonly used to bypass Mark-of-the-Web (MOTW) 
restrictions or to hide malicious payloads.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Virtual Instance Execution Abuse (T1564.006)
- **ID:** `T1564_006.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious execution of virtual instances (Docker, VirtualBox, VMware)
by monitoring for anti-forensic flags (--rm), privileged escalation attempts,
host network usage, and execution from untrusted parent processes (Office apps, 
web servers, scripts). Trusted developer and orchestration environments are filtered.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## VBA Macro Security Evasion (T1564.007)
- **ID:** `T1564_007.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to bypass Microsoft Office macro security or hide VBA projects
by monitoring registry modifications, Office Object Model abuse, and suspicious
interpreter execution. Focuses on non-admin or untrusted parent processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Email Hiding Rules Detection (T1564.008)
- **ID:** `T1564_008.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious modifications of email inbox rules aimed at hiding, 
deleting, or forwarding security-related alerts. Monitors non-admin parent 
processes and untrusted shells for actions that could suppress detection of 
phishing, MFA alerts, or unauthorized access notifications.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Resource Extraction and Abuse (T1564.009)
- **ID:** `T1564_009.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects abuse of binary resource sections and help file interpreters
(hh.exe, winhlp32.exe) for extracting or executing hidden payloads. 
Monitors suspicious parent processes, protocol smuggling (its:, ms-its:),
decompilation attempts, and non-standard file paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Process Argument Spoofing Detection (T1564.010)
- **ID:** `T1564_010.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential process argument spoofing where sensitive interpreters
(PowerShell, CMD, WMIC, CertUtil, Svchost, SchTasks) are spawned with empty
or generic arguments from untrusted parent processes, indicating defense evasion
techniques.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Virtual Instance Abuse (T1564.011)
- **ID:** `T1564_011.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [WSL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious use of Windows Sandbox, WSL, and related virtual instances
to evade EDR monitoring. Monitors untrusted parent processes, non-standard
configuration loading, and direct command execution within virtualized environments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Data Manipulation (T1565)
- **ID:** `T1565.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized manipulation of stored or transmitted data, including stream editing,
log clearing via CLI, SQL/database updates, and modifications to critical system files
(hosts, event logs, system configs) originating from non-standard parent processes.
Covers T1565.001 (Stored Data Manipulation) and T1565.002 (Transmitted Data Manipulation).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Stored Data Manipulation (T1565.001)
- **ID:** `T1565_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized modification of stored data including configuration files,
databases, and system logs. Monitors suspicious stream editing, SQL commands, 
or PowerShell replacements originating from non-standard parent processes or
targeting critical system paths, filtering out legitimate administrative activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Transmitted Data Manipulation (T1565.002)
- **ID:** `T1565_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized network redirection and resolution manipulation including DNS, proxy,
and hosts file modifications. Monitors CLI-based configuration changes originating from
suspicious parent processes or targeting critical registry keys. Filters legitimate administrative
and system activities to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Runtime Process Manipulation (T1565.003)
- **ID:** `T1565_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects runtime process manipulation including suspicious memory access masks (e.g., PROCESS_ALL_ACCESS)
and remote thread injection between unrelated processes. Focuses on non-standard execution contexts
and filters known-good administrative, security, and monitoring tools to reduce false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Phishing Payload Execution from Communication Apps
- **ID:** `T1566.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by email clients, browsers, or chat apps 
where the payload originates from a user-writable directory. This pattern is 
highly characteristic of spearphishing (T1566.001/.002).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Spearphishing Attachment Execution
- **ID:** `T1566_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [MSPUB.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [VISIO.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects highly suspicious child processes spawned from email clients or Office applications. 
It specifically targets script interpreters and dual-use binaries (LOLBins) that 
originate from user-writable directories, significantly reducing false positives 
from legitimate system updates and standard GUI behavior.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Browser-Originating Payload Execution
- **ID:** `T1566_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious child processes spawned by web browsers where the command line 
references user-writable or temporary directories. This pattern is highly 
indicative of a successful spearphishing link attack leading to immediate execution.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Process Spawn from Business Communication Service
- **ID:** `T1566_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects highly suspicious child processes spawned by business communication tools 
(Teams, Slack, Discord, LinkedIn). It specifically targets script interpreters 
and dual-use binaries (LOLBins) executing from user-writable directories, 
effectively filtering out legitimate application updates and browser launches.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Detection of Post-Vishing Remote Tool Execution
- **ID:** `T1566_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects the execution of unauthorized remote access tools (AnyDesk, TeamViewer, etc.) 
specifically when run from user-writable directories (Downloads, Temp). 
This pattern is a high-confidence indicator of a successful vishing attack where 
the victim is instructed to run "support" software.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Web Service Exfiltration (T1567)
- **ID:** `T1567.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic data exfiltration to web or cloud services by monitoring:
1. Headless transfer tools (rclone, megatools, mega-put) and custom web clients.
2. Programmatic uploads targeting web endpoints, cloud storage, or public paste/webhook services.
3. Execution from untrusted directories or non-administrative parent processes (Office apps, rundll32, explorer). 
Filters legitimate administrative tools, local host operations, and system processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Code Repository Exfil (T1567.001)
- **ID:** `T1567_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic exfiltration of source code to public repositories by monitoring:
1. Headless or automated Git/CLI operations (git.exe, gh.exe, curl, PowerShell) 
   executed from non-development parent processes or suspicious directories.
2. Inline authentication tokens or Personal Access Tokens (PATs) in command lines.
3. Remote repository reconfiguration or forced pushes indicative of unauthorized data transfer.
Filters legitimate developer IDE usage and approved repository operations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Storage Exfil (T1567.002)
- **ID:** `T1567_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic data exfiltration to cloud storage platforms by monitoring:
1. CLI tools (rclone, megatools, pcloud clients) using embedded credentials 
   or custom config files.
2. Triggering by non-administrative or suspicious parent processes 
   (Office apps, Beacon hosts, scripts).
3. Targeted cloud endpoints including mega.nz, Dropbox, Google Drive, pCloud, 
   and Transfer.sh.
Filters legitimate system/administrative usage to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Video Hosting Exfil (T1567.003)
- **ID:** `T1567_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects covert data exfiltration via video hosting platforms by monitoring:
1. Steganographic embedding in video files (metadata abuse, stream attachment).
2. CLI-based uploads targeting public video platforms from non-creative or 
   non-authorized assets.
Excludes legitimate creative applications and system processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Text Storage Exfil (T1567.004)
- **ID:** `T1567_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects programmatic exfiltration of sensitive data to public text storage platforms
(Pastebin, Ghostbin, Hastebin, ControlC, Rentry) by monitoring:
1. CLI-based POST requests containing API keys or data payloads.
2. Clipboard scraping commands or sensitive file access.
3. Execution from non-administrative or suspicious parent processes.
Excludes legitimate administrative and software update activities.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Dynamic Resolution & DGA (T1568)
- **ID:** `T1568.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects dynamic DNS resolution and Domain Generation Algorithm (DGA) activity 
by monitoring:
1. Programmatic DNS queries executed within loops or retry logic.
2. Low-level DNS API calls from scripting interpreters.
3. High-entropy and anomalous domain patterns in command lines.
Excludes legitimate administrative, automation, and internal domains.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Fast Flux & DNS Cache Evasion (T1568.001)
- **ID:** `T1568_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects Fast Flux DNS infrastructure usage and DNS cache evasion by monitoring:
1. Forced DNS cache flushing via system commands or PowerShell.
2. Programmatic DNS resolution combined with looped connectivity checks.
3. Execution from non-standard scripting or interpreter processes.
Excludes legitimate administrative and cloud automation activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Domain Generation Algorithm (DGA) Detection (T1568.002)
- **ID:** `T1568_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects programmatic Domain Generation Algorithm (DGA) activity by monitoring:
1. Rapid DNS resolution attempts via API or CLI
2. High-entropy or suspicious domain patterns in command lines
3. Suppression of DNS errors to evade detection.
Filters out legitimate software, cloud automation, and internal infrastructure traffic.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## DNS Calculation & Extraction (T1568.003)
- **ID:** `T1568_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects C2 infrastructure address calculation via DNS by monitoring programmatic 
retrieval of TXT/SRV records followed by byte-level manipulation or type conversion 
in script interpreters. Filters out legitimate DNS-based automation, license checks, 
and domain verification processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity System Service Execution Detection
- **ID:** `T1569.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation or execution of system services with suspicious characteristics, 
such as binaries located in world-writable directories or services used as 
wrappers for shell commands. Optimized to filter out legitimate software installers.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Launch Daemon Persistence Detection
- **ID:** `T1569_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects the creation or modification of Launch Daemons by monitoring 
untrusted parent processes and suspicious command-line strings. 
Optimized to filter out Apple and common third-party installers.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity System Service Execution Detection (T1569.002)
- **ID:** `T1569_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious service execution or modification by monitoring anomalous 
parent processes, world-writable binary paths, and shell command wrappers. 
Optimized for low false positive rates in enterprise environments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lateral Tool Transfer (T1570)
- **ID:** `T1570.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized lateral tool transfer across administrative shares (C$, ADMIN$, IPC$).
Focuses on high-risk process activity originating from non-standard lineages 
(Office apps, browsers, non-elevated shells) and known transfer utilities 
like robocopy, bitsadmin, xcopy, or certutil. Excludes legitimate system 
automation and software distribution activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Non-Standard Port C2 (T1571)
- **ID:** `T1571.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects command-and-control (C2) communication over non-standard ports by 
correlating high-risk native binaries (LoLBins) with outbound public network 
connections to ports outside standard web, mail, and directory service ranges. 
Filters out legitimate automation, internal network traffic, and system binaries 
to reduce false positives.


#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Protocol Tunneling Detection (T1572)
- **ID:** `T1572.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects adversary protocol tunneling by identifying non-standard encapsulation, 
low-level socket proxying (SOCKS5/Reverse), and CLI signatures of known tunneling 
tools. Filters out legitimate administrative VPN/SSH traffic and automation tools 
to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Encrypted C2 Channel (T1573)
- **ID:** `T1573.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects creation of custom encrypted C2 channels by correlating low-level
symmetric cryptography (AES/Rijndael, CryptoStream, ICryptoTransform)
with manual network socket usage from scripting interpreters.
Filters out legitimate automation, cloud services, and system processes
to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Symmetric Encryption C2 Channel (T1573.001)
- **ID:** `T1573_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious use of custom symmetric encryption (AES/Rijndael) for C2 channels.
Focuses on programmatic setup of CipherMode, PaddingMode, and CryptoStreams within
scripting engines, specifically targeting manual IV/Key assignment and stream piping
from non-standard processes or untrusted execution contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Asymmetric Encryption C2 (T1573.002)
- **ID:** `T1573_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious asymmetric encryption usage (RSA/ECC) that may indicate 
C2 or data exfiltration activity. Focuses on programmatic trust chain overrides 
(ServerCertificateValidationCallback) and raw public key imports (FromXmlString, 
ImportSubjectPublicKeyInfo) from untrusted or non-standard processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro DLL Hijacking & Side-Loading Detection (T1574)
- **ID:** `T1574.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential DLL hijacking or side-loading by monitoring trusted system 
binaries loading DLLs from non-standard, user-writable directories, while 
filtering out legitimate signed modules and known application behaviors.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro DLL Search Order Hijacking Detection (T1574.001)
- **ID:** `T1574_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects trusted Windows system binaries loading DLLs from non-standard, 
potentially user-writable directories. It filters out validly signed 
third-party modules to reduce false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro DLL Side-Loading Integrity Gap Detection (T1574.002)
- **ID:** `T1574_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential DLL side-loading by identifying cases where a signed, 
trusted executable loads an unsigned or suspiciously-located DLL from 
user-writable directories.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Shell Configuration & Path Interception (T1574.003)
- **ID:** `T1574_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized modification of PATH environment variables or shell autorun 
registry keys. Focuses on "Path Prepending" (placing malicious paths at the 
beginning) and non-standard shell startup commands.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Library Search Order Hijacking & Integrity Gap (T1574.004)
- **ID:** `T1574_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential library hijacking by monitoring trusted system binaries 
loading unsigned or suspiciously-located DLLs from user-writable directories, 
specifically looking for trust mismatches between the EXE and the DLL.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Installer File Permissions Weakness (T1574.005)
- **ID:** `T1574_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-privilege execution of binaries from user-writable locations. 
This targets scenarios where an attacker replaces a legitimate installer 
with a malicious one due to insecure directory permissions.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Dynamic Linker Hijacking Against Privileged Binary
- **ID:** `T1574_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects Dynamic Linker Hijacking by identifying execution of privileged or SetUID Linux binaries with manipulated dynamic linker environment variables pointing to user-writable shared libraries.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## PATH Hijacking Leading to Privileged Binary Execution
- **ID:** `T1574_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects PATH environment variable hijacking where a privileged Linux binary is executed with a user-writable directory at the beginning of PATH, and a non-absolute command is resolved, indicating a viable path interception attack chain.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## .NET Assembly Search Order Hijacking via User-Writable Directory
- **ID:** `T1574_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential .NET Assembly Search Order Hijacking where a legitimate .NET runtime host loads a managed assembly from a user-writable directory outside of the GAC, Microsoft.NET framework paths, or the application installation directory.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## .NET AppDomainManager Hijacking via Non-GAC Assembly
- **ID:** `T1574_009.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects .NET AppDomainManager hijacking by identifying .NET runtime hosts that load a managed assembly from a user-writable directory at process initialization, outside of the GAC and Microsoft .NET framework paths. This behavior is highly indicative of malicious AppDomainManager abuse.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Privileged Service Executable Overwritten from User-Writable Location
- **ID:** `T1574_010.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects exploitation of weak service file permissions where a registered Windows service executable running with high privileges is overwritten or modified from a user-writable directory by a non-system process.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Privileged Service ImagePath or ServiceDll Hijacked via Registry
- **ID:** `T1574_011.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects exploitation of weak Windows service registry permissions where a non-system process modifies critical service registry values to point to an executable or DLL located in a user-writable directory, enabling privilege escalation upon service start or restart.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-Grade COR_PROFILER Hijacking via User-Writable Profiler DLL
- **ID:** `T1574_012.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/), [VSJITDEBUGGER.EXE](https://lolbas-project.github.io/lolbas/), [VSTEST.CONSOLE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects exploitation of COR_PROFILER hijacking where a .NET runtime host is executed with profiling enabled and a custom profiler DLL specified from a user-writable directory, excluding legitimate Microsoft, Visual Studio, and APM profiling use cases.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-Grade KernelCallbackTable Manipulation
- **ID:** `T1574_013.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious remote memory write operations targeting GUI processes, 
which are indicative of KernelCallbackTable hijacking attempts. This technique 
is commonly used for stealthy process injection that bypasses traditional hook-based monitoring.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Infrastructure Tampering (T1578)
- **ID:** `T1578.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-risk modifications to cloud infrastructure that weaken security posture 
or prepare for data exfiltration. Focuses on manual, untrusted, or anomalous 
identity actions while filtering out automated and internal operations.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Cloud Instance Creation (T1578.001)
- **ID:** `T1578_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects creation of high-resource or expensive cloud instances from untrusted 
identities or outside approved regions. Optimized for Cryptojacking and unauthorized 
resource abuse, while filtering out CI/CD and autoscaling operations.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Snapshot Exfiltration (T1578.002)
- **ID:** `T1578_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized sharing, cross-account access, or public exposure of cloud compute snapshots.
Focuses on high-risk permission changes rather than simple snapshot creation, and filters out 
trusted backup and replication processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Instance Destruction (T1578.003)
- **ID:** `T1578_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized or mass deletion of cloud instances across Azure, AWS, 
and GCP environments. Focuses on manual, non-MFA, or suspicious scripted 
deletions that may indicate sabotage or defense evasion, while excluding 
legitimate automated scaling events.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Image Tampering (T1578.004)
- **ID:** `T1578_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized modifications to cloud machine images (AMI, VHD, Managed Images). 
Focuses on permission changes that expose images to external accounts or the public internet. 
Context-aware detection excludes legitimate CI/CD and image build pipelines while including suspicious interactive sessions.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Network Security Regression (T1578.005)
- **ID:** `T1578_005.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-risk modifications to Network ACLs or Security Groups that allow 
wide-open ingress (0.0.0.0/0 or ::/0) on sensitive management ports (RDP, SSH, DB). 
Includes context-aware checks for suspicious client tools and disables MFA usage.
Filters out legitimate IaC automation and internal service operations.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Infrastructure Discovery (T1580)
- **ID:** `T1580.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic discovery of cloud infrastructure resources (VMs, VPCs, S3 buckets, storage accounts)
by monitoring anomalous CLI usage, output extraction, and interactive session contexts.
Filters out legitimate Infrastructure-as-Code (IaC) and CI/CD automation tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Offensive Infrastructure Provisioning - T1583
- **ID:** `T1583.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the automated acquisition of infrastructure (VPS, Domains, Serverless)  by monitoring for CLI-based provisioning tools and domain registration API calls.  Filters focus on isolating authorized DevOps pipelines and developer environments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity VPS Infrastructure Provisioning - T1583.001
- **ID:** `T1583_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the automated acquisition of VPS infrastructure (DigitalOcean, AWS, Azure, GCP).  Focuses on the provisioning phase (VM creation) while isolating authorized DevOps  pipelines and interactive developer workflows.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Automated Domain Registration & Acquisition - T1583.002
- **ID:** `T1583_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated domain registration through registrar APIs and specialized  provisioning tools. Focuses on programmatic acquisition via curl/python  while filtering out authorized IT infrastructure management (Certbot, Terraform).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Network (VPC) Provisioning - T1583.003
- **ID:** `T1583_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the acquisition and configuration of cloud networking (VPC).  Focuses on identifying the creation of internet egress points and  cross-network bridges from unauthorized endpoints, isolating automated  CI/CD pipelines from manual or scripted local abuse.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Serverless Infrastructure Provisioning - T1583.004
- **ID:** `T1583_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the automated acquisition and provisioning of serverless infrastructure  (AWS Lambda, Azure Functions, GCP Functions). Focuses on CLI-based creation  and critical configuration changes while isolating authorized CI/CD pipelines  and interactive developer IDE contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Botnet Infrastructure Acquisition - T1583.005
- **ID:** `T1583_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the acquisition and preparation of botnet infrastructure.  Focuses on identifying multi-architecture agent downloads, automated  propagation attempts (brute-force), and botnet C2 client usage.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Web Service Acquisition and Provisioning - T1583.006
- **ID:** `T1583_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the acquisition and setup of web services (SaaS, Storage, Messaging)  for offensive infrastructure. Focuses on command-line based storage provisioning  (Rclone, AzCopy) and messaging API initialization (Slack/Discord/Telegram bots)  from non-administrative or non-developer endpoints.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Serverless Infrastructure Provisioning - T1583.007
- **ID:** `T1583_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the automated acquisition and provisioning of serverless infrastructure  (AWS Lambda, Azure Functions, GCP Functions). Focuses on CLI-based creation  and critical configuration changes while isolating authorized CI/CD pipelines  and interactive developer IDE contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Account Acquisition and Bootstrap - T1583.008
- **ID:** `T1583_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the acquisition and initial configuration of cloud accounts.  Targets account-level bootstrapping (credential setup, IAM user creation)  and automated identity harvesting from non-standard processes,  while filtering out authorized DevOps pipelines.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Compromised Infrastructure and Resource Abuse - T1584
- **ID:** `T1584.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects indicators of compromised infrastructure, specifically focusing on  web server process subversion (Web Shells), unauthorized reverse proxies,  and tunneling tools executed from non-standard administrative contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Domain Infrastructure Hijacking - T1584.001
- **ID:** `T1584_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized domain or subdomain hijacking by monitoring for  critical DNS record types (NS, SOA) and mass record creation via  Cloud Provider CLIs, while filtering for authorized DevOps automation.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity DNS Server Configuration Subversion - T1584.002
- **ID:** `T1584_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [DNSCMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized DNS infrastructure manipulation by monitoring for  critical configuration changes (zone resets, master updates) and  suspicious child processes spawned directly from DNS services.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Identity Subversion and Persistence - T1584.003
- **ID:** `T1584_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized cloud account manipulation by monitoring for  high-risk identity changes (MFA removal, new access keys) executed  outside of authorized CI/CD pipelines or known administrative jump-hosts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Serverless Function Subversion - T1584.004
- **ID:** `T1584_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized modification of serverless functions (Lambda, Azure Functions, GCP) by focusing on high-risk parameters like layer injection and environment variable manipulation, while strictly filtering for authorized CI/CD pipeline service accounts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Botnet Agent Persistence and Control - T1584.005
- **ID:** `T1584_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects botnet agent activity by identifying suspicious process lineages  (e.g., LOLBins spawning from WMI), P2P bootstrap arguments, and known  DDoS tool patterns while filtering authorized IT management and P2P software.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Web Service and Cloud Storage Subversion - T1584.006
- **ID:** `T1584_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized manipulation of web services and cloud storage by  monitoring for ACL changes (making buckets public), suspicious file types  being hosted (scripts/exes), and the use of third-party data transfer  tools (rclone) outside of authorized contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity VPS Control and Tunneling - T1584.007
- **ID:** `T1584_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized VPS manipulation by identifying critical lifecycle changes  (SSH key injection, firewall opening) and the execution of reverse tunneling tools  from non-authorized administrative contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious User Account Creation via CLI/Scripting
- **ID:** `T1585.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation of new user accounts (T1585) when initiated from 
suspicious processes like CMD, PowerShell, or net.exe, rather than 
standard Administrative consoles (ADUC, Windows Admin Center).


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Potential Automated Social Media Account Establishment
- **ID:** `T1585_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious patterns of social media account registration by monitoring 
access to multiple sign-up endpoints from a single host or identifying 
non-browser processes making requests to these domains.


#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Stealthy Email Account Establishment and Manipulation
- **ID:** `T1585_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects the creation of email accounts followed by immediate sensitive 
permission changes or forwarding rules. Focuses on CLI-based execution 
to reduce noise from standard HR-driven GUI processes.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous Cloud User Account Creation
- **ID:** `T1585_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects the creation of cloud accounts via command-line tools or service principals, 
excluding authorized synchronization accounts and automated HR provisioning systems.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Account Compromise and Identity Manipulation - T1586
- **ID:** `T1586.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects actions indicative of account compromise and takeover (ATO), such as  unauthorized MFA modification, suspicious login profile updates, and automated  credential testing from non-standard administrative processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Automated Social Media Manipulation - T1586.001
- **ID:** `T1586_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated interaction with social media platforms via headless browser  frameworks (Selenium, Puppeteer, Playwright). Attackers use these to scale  account takeover (ATO) and bypass security controls by injecting stolen cookies.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Email Forwarding Rule Manipulation - T1586.002
- **ID:** `T1586_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation or modification of email forwarding/redirection rules via  command-line tools (PowerShell, Microsoft Graph CLI). This is a high-confidence  indicator of Account Takeover (ATO) where an attacker attempts to exfiltrate  sensitive emails (invoices, password resets) without user interaction.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Account Takeover and Persistence - T1586.003
- **ID:** `T1586_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized cloud account manipulation focusing on identity takeover  and persistence. Targets the creation of new cloud credentials, MFA removal,  and login profile updates from non-authorized processes, specifically filtering  out known administrative and developer workflows.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Offensive Capability Development and Compilation - T1587
- **ID:** `T1587.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [JSC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the development and compilation of offensive tools by monitoring  for specific C2 framework build arguments, unauthorized use of code packers,  and certificate manipulation outside of verified CI/CD pipelines.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Malware Development and Evasion Patterns - T1587.001
- **ID:** `T1587_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects custom malware development by identifying suspicious compiler execution  combined with evasion-related API strings, anti-analysis techniques,  and unauthorized build locations.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Unauthorized Code Signing Capability Development - T1587.002
- **ID:** `T1587_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the creation of code-signing certificates and the manual signing of binaries  by monitoring for specific OIDs (1.3.6.1.5.5.7.3.3) and signing tools used outside  of verified CI/CD pipelines or Windows SDK paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Unauthorized Digital Certificate Development - T1587.003
- **ID:** `T1587_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized digital certificate and private key generation by monitoring  for high-risk command-line arguments (self-signing, key exfiltration) occurring  in non-standard directories or by unauthorized users.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Exploit Development and Compilation Detection - T1587.004
- **ID:** `T1587_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects indicators of exploit development by monitoring for the compilation of  source code containing memory injection primitives and shellcode-related  arguments, specifically when executed from non-standard or temporary directories.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous Procurement of Offensive Capabilities
- **ID:** `T1588.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the acquisition of offensive tools by monitoring suspicious combinations 
of download-capable processes and known hacktool signatures or file extensions, 
filtering out legitimate IT software deployment tools.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous Procurement of Malware Capabilities
- **ID:** `T1588_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the acquisition of malware by monitoring suspicious downloaders (LotL) 
interacting with compressed/container formats or known malware naming patterns 
in non-standard directories.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous Offensive Tool Acquisition via CLI
- **ID:** `T1588_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the acquisition of offensive tools (hacktools) by monitoring command-line 
downloads targeting non-standard directories. Filters out legitimate IT 
administration from browsers and authorized management agents.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous Code Signing Certificate Export or Acquisition
- **ID:** `T1588_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious certificate operations (exporting private keys or forced store additions) 
initiated from unusual parent processes or using plaintext passwords in the command line.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Strategic Trusted Root Certificate Store Manipulation
- **ID:** `T1588_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized attempts to modify the Trusted Root Certification Authorities 
store. Attackers do this to facilitate MitM attacks or bypass security warnings. 
Filters out legitimate system-level installers and known security agents.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous Procurement of Exploit or PoC Code
- **ID:** `T1588_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the acquisition of exploits or Proof-of-Concept (PoC) code by monitoring 
suspicious download patterns, CLI-based transfers, and known exploit naming 
conventions while filtering out authorized security scanners and developer activity.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Targeted Harvesting of Vulnerability Research Artifacts
- **ID:** `T1588_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the systematic acquisition of vulnerability research, audit reports, or 
zero-day PoC documentation. Focuses on CLI-based harvesting in non-technical 
user contexts while filtering out authorized security research.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Identity Enumeration via Authentication Endpoints
- **ID:** `T1589.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence identity reconnaissance activity where an external actor enumerates valid user identities via authentication or account-related endpoints. Detection is based on enumeration behavior, automation indicators, and authentication response patterns, excluding browsers, SSO flows, and monitoring tools.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Credential Enumeration via Authentication API (High Confidence)
- **ID:** `T1589_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence credential enumeration activity against authentication APIs. The rule focuses on automated, non-interactive probing behavior attempting to validate the existence or correctness of credentials. Browser-based logins, SSO flows, monitoring systems, and legitimate user authentication are excluded to minimize false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Confidence OSINT Identity Enumeration via Public APIs
- **ID:** `T1589_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence open-source identity enumeration attempts via public-facing APIs or directory endpoints. This rule focuses on scripted, automated reconnaissance behavior designed to collect user or employee identity data, while excluding normal browsing, search engines, and legitimate crawlers to minimize false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Targeted OSINT Enumeration of Open Websites and Domains
- **ID:** `T1589_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence reconnaissance activity targeting open websites and domains to gather victim identity information. The rule focuses on scripted enumeration behavior against search or directory-style endpoints, excluding browsers, crawlers, and legitimate monitoring traffic to ensure very low false positive rates.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Network Reconnaissance with High Port Diversity
- **ID:** `T1590.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)
- **Leírás:** Detects network reconnaissance activity. Optimized for cross-SIEM compatibility by using standard field names and avoiding complex CIDR logic in the core rule.


#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Professional IP Infrastructure Reconnaissance - T1590.001
- **ID:** `T1590_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects professional IP discovery techniques by focusing on reconnaissance-specific  command arguments and external IP lookup services, while filtering out  standard Windows networking noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**


---
## Advanced DNS Infrastructure Reconnaissance - T1590.002
- **ID:** `T1590_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [DNSCMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic DNS reconnaissance. It reduces false positives by filtering  legitimate single-host lookups and focusing on infrastructure-wide enumeration  attempts like Zone Transfers or specific record harvesting.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Network Trust Dependencies Reconnaissance - T1590.003
- **ID:** `T1590_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic discovery of network trust relationships and shared resources.  It minimizes noise by filtering standard GPO-driven drive mappings and focused  on high-intent enumeration commands like nltest domain trusts and remote session listing.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Certificate Information Reconnaissance - T1590.004
- **ID:** `T1590_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects professional reconnaissance of digital certificates. Focuses on  interactive command-line tools used to extract metadata from local stores  or remote servers while filtering out automated signature verification.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Cloud Infrastructure Reconnaissance - T1590.005
- **ID:** `T1590_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects manual or suspicious cloud infrastructure enumeration.  It filters out legitimate CI/CD pipelines and automated service accounts  to focus on interactive discovery.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Victim Web Page Info Reconnaissance - T1590.006
- **ID:** `T1590_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated web reconnaissance and sensitive file discovery attempts.  It minimizes false positives by filtering development environments and focusing  on high-intent reconnaissance patterns across CLI tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Organizational Infrastructure Enumeration - T1591
- **ID:** `T1591.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [LDIFDE.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic gathering of organizational metadata (OUs, groups, users).  It minimizes false positives by filtering known administrative consoles,  service account syncs, and focusing on non-standard execution contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Physical Location Infrastructure Enumeration - T1591.001
- **ID:** `T1591_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [VISIO.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic discovery of physical infrastructure data (floor plans, badge systems).  It filters out common office usage (Intranet, Visio) and focuses on CLI-based  bulk search operations which are characteristic of reconnaissance before physical  intrusion or social engineering.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Business Relationship Information Discovery - T1591.002
- **ID:** `T1591_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic and automated discovery of business relationships.  It filters out common office productivity noise and focuses on bulk  search operations originating from non-standard parent processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Knowledge Management Discovery - T1591.003
- **ID:** `T1591_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic and automated discovery of internal knowledge management systems.  It targets bulk data extraction patterns and command-line reconnaissance  while filtering out standard web browser usage and IT automation.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Personnel Information Discovery - T1591.004
- **ID:** `T1591_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious, bulk extraction of employee data from Active Directory.  Focuses on non-standard LDAP queries and broad PowerShell filters that  deviate from routine administrative behavior.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Host Information Reconnaissance Activity
- **ID:** `T1592.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-confidence host information reconnaissance activity by identifying multiple system discovery commands executed in a short timeframe from a user context. Tuned to minimize false positives by excluding SYSTEM activity, enterprise tooling, and single benign command executions.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Confidence Hardware Enumeration via Management Interfaces
- **ID:** `T1592_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence reconnaissance activity where an external source attempts to enumerate hardware characteristics such as CPU, architecture, memory, or device model via management or embedded system interfaces. The rule is optimized to minimize false positives by focusing on automated probing behavior.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Software Enumeration Reconnaissance via Web Endpoints
- **ID:** `T1592_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects advanced reconnaissance activity where an external actor systematically enumerates installed software, application names, or version information through multiple web-accessible endpoints in a short time window. Tuned to minimize false positives by requiring automation-like behavior and repeated probing patterns.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Confidence Firmware Enumeration Against Network Devices
- **ID:** `T1592_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence reconnaissance activity targeting firmware and version information of network or embedded devices. The rule focuses on automated, non-browser access to device-specific management endpoints and is optimized to minimize false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Confidence Client Configuration Fingerprinting (Reconnaissance)
- **ID:** `T1592_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence reconnaissance activity where an external source performs repeated non-browser HTTP requests using probing methods and header-focused techniques to enumerate client or infrastructure configurations. Optimized to minimize false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**


---
## High-Fidelity Automated Web Reconnaissance - T1593
- **ID:** `T1593.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated web scraping and OSINT collection patterns targeting  social media and public sites. Focuses on headless browser automation  and specialized CLI tools while filtering out legitimate HR and Marketing activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Social Media Entity Harvesting - T1593.001
- **ID:** `T1593_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated reconnaissance of social media profiles. It targets headless  browser automation (Selenium/Puppeteer) and specialized OSINT tools while  filtering out routine HR recruitment and interactive browser usage.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Automated Search Engine Reconnaissance - T1593.002
- **ID:** `T1593_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated reconnaissance using search engines by monitoring for headless  browser flags and systematic dorking patterns. Specifically filters out  legitimate developer activity and interactive browser usage to minimize false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Social Media Entity Harvesting - T1593.003
- **ID:** `T1593_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated social media reconnaissance using headless browsers or specialized OSINT tools.  Focuses on identifying systematic data scraping while excluding legitimate browser-based user activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Information Repository Reconnaissance - T1594
- **ID:** `T1594.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated reconnaissance of public information repositories (GitHub, GitLab).  Focuses on specialized secret scanners and bulk API harvesting while filtering out  standard developer workflows (git clone/pull) and authorized security tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Active Scanning Detection (Behavior-Based)
- **ID:** `T1595.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence active scanning behavior by identifying automated clients systematically probing multiple sensitive web endpoints from an external source within a short timeframe. Designed to minimize false positives by excluding browsers, monitoring, health checks, and known benign scanners.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity External IP Block Scanning Detection
- **ID:** `T1595_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence active scanning behavior where a single external source IP rapidly probes multiple destination IP addresses within a short time window. Optimized to reduce false positives by excluding known scanners, crawlers, and cloud infrastructure.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Confidence External Vulnerability Scanning Activity
- **ID:** `T1595_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence vulnerability scanning activity by correlating aggressive request behavior, exploit discovery paths, payload indicators, and known scanner tooling. Optimized to minimize false positives in enterprise environments.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Active Wordlist Scanning Against Authentication Endpoints
- **ID:** `T1595_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects high-confidence wordlist scanning activity where an external source rapidly probes authentication or administrative endpoints using varying username parameters, consistent with automated reconnaissance.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Open Technical Database Reconnaissance - T1596
- **ID:** `T1596.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the systematic use of CLI tools and script-based API queries directed  at technical databases like Shodan, Censys, and VirusTotal.  Focuses on non-browser process chains and automated data extraction patterns.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity WHOIS Database Reconnaissance - T1596.001
- **ID:** `T1596_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated WHOIS reconnaissance patterns. Focuses on bulk domain registration  queries via CLI tools and API-based scripts (RDAP) while filtering out standard  browser-based research, software licensing, and routine IT diagnostics.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Automated Search Engine Dorking - T1596.002
- **ID:** `T1596_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the automated use of search engine dorks and specialized CLI tools  designed for bulk technical data harvesting. Filters out interactive browser  searches and legitimate IDE-triggered error lookups.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Passive DNS Reconnaissance - T1597.003
- **ID:** `T1596_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated reconnaissance using Passive DNS (pDNS) databases.  Focuses on non-standard process chains and CLI-based API interactions  targeting technical OSINT repositories while filtering out routine  network troubleshooting and browser-based research.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Digital Certificate Reconnaissance - T1596.004
- **ID:** `T1596_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated reconnaissance targeting Digital Certificates and CT logs.  Focuses on programmatic CLI patterns (API-based scraping) while filtering  out legitimate system-level certificate validation and browser traffic.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity IP Infrastructure Reconnaissance - T1596.005
- **ID:** `T1596_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated reconnaissance of IP address metadata. Focuses on specialized  OSINT tools (Shodan, GreyNoise, Censys) and CLI-based API harvesting while  filtering out routine network troubleshooting, browser traffic, and EDR noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Victim-Owned Website Reconnaissance - T1597
- **ID:** `T1597.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects automated and systematic reconnaissance of organization-owned  web infrastructure. Focuses on bulk data extraction, recursive directory  brute-forcing, and the discovery of sensitive configuration files.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Domain Infrastructure Enumeration - T1597.001
- **ID:** `T1597_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects advanced and automated domain/DNS reconnaissance. Focuses on  unusual DNS query types (AXFR, ANY) and professional sub-domain discovery  tools while filtering out routine network troubleshooting.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Secret Hunting in Code Repositories - T1597.002
- **ID:** `T1597_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects professional secret-hunting tools and manual reconnaissance patterns  within code repositories. Focuses on deep history analysis (diff-searching)  and automated credential extraction while filtering out standard dev-cycles.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Phishing for Info & Credential Harvesting - T1598
- **ID:** `T1598.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects post-phishing credential harvesting and session token theft.  Focuses on non-browser processes accessing browser profile data and  suspicious interactive credential prompts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Spearphishing Link Redirection - T1598.001
- **ID:** `T1598_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious URL execution patterns originating from productivity apps.  Focuses on indirect browser launches (via cmd/powershell) and OAuth-specific  credential harvesting parameters while filtering out known SSO providers.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced BEC Mail & Financial Data Exfiltration - T1598.002
- **ID:** `T1598_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious command-line access to mail archives and financial documents  typically targeted in BEC campaigns. It filters out legitimate Outlook  indexing, OneDrive synchronization, and system-level backups.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity MFA/OTP Spoofing & Harvesting - T1598.003
- **ID:** `T1598_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects the creation of fraudulent MFA/OTP input prompts by monitoring  unusual PowerShell UI class loading and specific CLI keywords.  Filters out common IT automation and software deployment noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Spearphishing Attachment Interaction - T1598.004
- **ID:** `T1598_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious execution patterns from email attachments. Focuses on HTML  smuggling and Office-to-script transitions while filtering out legitimate  SharePoint, OneDrive, and enterprise software update noise.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Network Boundary Bridging (T1599)
- **ID:** `T1599.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized network boundary bridging, including manual creation of
"Any-to-Internal" NAT rules, port forwarding of sensitive services, and
hardware-level bridging of isolated interfaces. Focuses on untrusted sources
and manual session activity while filtering out legitimate management and VPN operations.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Logical Isolation Bypass (T1599.001)
- **ID:** `T1599_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized logical network isolation bypass attempts, including VRF route leaking,
unauthorized VLAN trunking, L2 bridge creation, and EVPN misconfigurations that could
bridge secure zones or bypass segmentation controls.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Weaken Encryption Attempt (T1600)
- **ID:** `T1600.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized attempts to weaken system encryption, including TLS protocol downgrades
and PowerShell certificate validation bypasses. Focuses on non-system processes and
suspicious locations while excluding trusted installers and browser updates.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## System Image Patching (T1600.001)
- **ID:** `T1600_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects attempts to compromise system image integrity by bypassing Driver Signature Enforcement (DSE), 
modifying Boot Configuration Data (BCD), or patching critical system binaries (CI.dll, NTOSKRNL.exe, LSASRV.dll, Winload.efi). 
Focuses on untrusted processes and excludes standard system management tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Disable Entity Verification (T1600.002)
- **ID:** `T1600_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized attempts to bypass system trust verification, 
certificate validation, and Authenticode/WinTrust checks. Focuses on 
suspicious certutil usage and registry-based policy modifications 
executed by untrusted processes. Minimizes false positives by excluding 
known IT management tools and signed software updaters.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Network OS Image Modification (T1601)
- **ID:** `T1601.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized modification or replacement of network device operating system images.
Monitors binary uploads via insecure protocols (TFTP/FTP), firmware update commands,
and boot-system overrides performed outside trusted management windows or hosts.
Focuses on detecting anomalous source context, checksum failures, and non-standard hosts.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Network Binary Patching (T1601.001)
- **ID:** `T1601_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized low-level patching of network OS binaries by monitoring 
for filesystem remounting (read-write), direct binary manipulation (dd, xxd), 
and kernel module loading (insmod) outside of authorized maintenance windows. 
Focuses on critical paths and filters out legitimate maintenance and read-only operations.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Malicious Network OS Upgrade (T1601.002)
- **ID:** `T1601_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects unauthorized or malicious network OS upgrades by correlating upgrade 
commands with insecure protocols, untrusted sources, or cryptographic signature failures.
Focuses on FortiOS logs but can be adapted to other network appliances. Filters out 
trusted sources and secure channels to reduce false positives.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Network Share Automated Collection (T1602)
- **ID:** `T1602.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects highly suspicious, automated collection of sensitive data from network shares.
Focuses on UNC path traversal, sensitive file extensions, recursive copy logic, and 
untrusted process lineage. Filters legitimate IT management, backup, and system processes
to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Admin Share Data Exfiltration (T1602.001)
- **ID:** `T1602_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects high-fidelity indicators of data staging and exfiltration via administrative shares
(C$, ADMIN$, IPC$, print$). Focuses on anomalous process lineages (web servers, shells),
recursive discovery, and high-value file targeting combined with archival or transfer tools.
Filters legitimate backup, migration, and IT automation tools to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Cloud Share Exfiltration (T1602.002)
- **ID:** `T1602_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [ONEDRIVESTANDALONEUPDATER.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects mass data collection and exfiltration from cloud storage sync roots 
(OneDrive, SharePoint, Google Drive, Dropbox) by monitoring recursive copy, 
archival, and staging activity from suspicious parent processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Web Token & Credential Forgery (T1606)
- **ID:** `T1606.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized forging or theft of web credentials including 
SAML, OAuth, and browser-stored tokens/cookies. 
Focuses on non-browser processes accessing DPAPI master keys, suspicious 
database queries on token stores, and Golden SAML artifact generation.
Filters legitimate browsers, Electron apps, and administrative automation tools.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Web Cookie & Browser Credential Harvesting (T1606.001)
- **ID:** `T1606_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized extraction of browser cookies and encryption keys 
(Chromium Local State AES keys / DPAPI-protected credentials). 
Focuses on suspicious file access, SQLite dumping, DPAPI decryption patterns, 
and execution from untrusted or temporary locations. 
Filters legitimate browser, Electron, and security tooling behavior.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Web Token Forgery & Golden SAML (T1606.002)
- **ID:** `T1606_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized web token forging activities (Golden SAML / OAuth token abuse) 
by correlating AD FS configuration extraction, signing certificate abuse, 
DPAPI masterkey access, and cloud token manipulation frameworks executed 
outside legitimate Identity Provider service context.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous Infrastructure Staging and Resource Deployment
- **ID:** `T1608.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects the use of cloud CLI tools and IaC binaries to stage adversary resources. 
It focuses on non-standard users performing upload or infrastructure modification 
actions, filtering out authorized CI/CD pipelines and IT administration.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous Malware Staging to External Infrastructure
- **ID:** `T1608_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the staging of malware to external infrastructure by monitoring 
non-browser based uploads to cloud storage, file-sharing, and code-hosting platforms 
using command-line tools or unusual processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous Offensive Tool Staging and External Upload
- **ID:** `T1608_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the staging of offensive tools to external infrastructure by monitoring 
CLI-based uploads from non-standard directories. Focuses on the "staged-then-shipped" 
pattern where hacktools are moved to external drop zones.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Strategic Digital Certificate Staging in Trusted Root Store
- **ID:** `T1608_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the command-line installation of certificates into the Trusted Root store. 
Adversaries do this to establish trust for C2 infrastructure or to enable 
transparent SSL/TLS interception (MitM).


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous Web Content Modification for Drive-by Staging
- **ID:** `T1608_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious modifications to web server content directories (web root) 
initiated by non-standard processes or interactive shells. This behavior is 
typical when an adversary stages a drive-by download site or injects malicious scripts.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Strategic Staging of Malicious Link Targets
- **ID:** `T1608_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the automated preparation of malicious link targets by monitoring 
CLI-based interactions with URL shortener APIs or cloud-based redirector staging 
initiated by unauthorized users or unusual parent processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Anomalous SEO Poisoning and Metadata Staging
- **ID:** `T1608_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects the preparation of SEO poisoning infrastructure by monitoring for 
unauthorized CMS manipulation, automated content spinning, and the use of 
known black-hat SEO tools on web servers or staging environments.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Container Interactive Shell Execution
- **ID:** `T1609.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized interactive shell access to running containers using 
kubectl or docker exec. Filters legitimate health checks and CI/CD automation 
to focus on manual, high-risk interventions.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Malicious Container Deployment Detection
- **ID:** `T1610.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects the deployment of containers with high-risk configurations that 
facilitate container escape or persistence. Focuses on privileged mode, 
host-level resource sharing, and non-standard image sources.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Container Escape & Host Access (T1611)
- **ID:** `T1611.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects unauthorized container escape attempts and host access. Focuses on 
non-standard privileged executions, dangerous mounts, and unconfined security 
contexts, while filtering out legitimate cluster infrastructure components.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Stealthy Local Image Build (T1612)
- **ID:** `T1612.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects high-fidelity local container image builds initiated by suspicious 
users or processes, focusing on post-exploitation image creation and 
evasion of registry scanning. Filters out trusted CI/CD pipelines and 
known build systems.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Container and Kubernetes Discovery
- **ID:** `T1613.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects high-fidelity enumeration of containers, Kubernetes resources, and secrets.
Focuses on identity self-interrogation (auth can-i), secret and config discovery, 
and anomalous process lineage. Filters out high-frequency monitoring and 
system probes to reduce false positives.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity System Location and Regional Kill-Switch Discovery
- **ID:** `T1614.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted system location and regional discovery commonly used by  ransomware and malware for geographic targeting or exclusion (kill-switch logic).  Focuses on registry-based keyboard/locale enumeration combined with  external IP-to-geo API calls from suspicious execution contexts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity System Language and Keyboard Layout Discovery
- **ID:** `T1614_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects targeted system language and keyboard layout discovery, focusing on malware "kill-switch" checks and environment keying. Combines registry queries, CLI/PowerShell cmdlets, and suspicious output redirection. Minimizes false positives via parent process, integrity level, and trusted path filtering.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Group Policy Discovery Detection
- **ID:** `T1615.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic Group Policy reconnaissance, including GPO report harvesting  and policy enumeration from unusual execution contexts. Filters out legitimate  administrative and Helpdesk activity using command-line, parent process, and  integrity level checks.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Storage Object Discovery Detection
- **ID:** `T1619.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects systematic cloud storage object discovery in AWS S3, Azure Blobs,  and Google Cloud Storage by monitoring recursive listing, metadata-heavy  API calls, and anomalous output redirection. Filters high-trust backup,  ETL, and DevOps automation accounts.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Reflective Code Loading and In-Memory Assembly Execution
- **ID:** `T1620.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects reflective code loading and in-memory assembly execution by monitoring  memory allocation with execution flags, process memory writes, and .NET reflection  assembly loading patterns in combination. Filters legitimate development and CI/CD processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious MFA Prompt Bombing or Authentication Flood Automation
- **ID:** `T1621.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential MFA prompt bombing or authentication flood automation  using PowerShell identity modules, Azure/Okta tooling, or headless browser  frameworks executed in non-interactive or hidden contexts. Focuses on loop  logic combined with identity authentication tooling.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Anti-Debug API Access From Unbacked or User-Space Memory
- **ID:** `T1622.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [VSJITDEBUGGER.EXE](https://lolbas-project.github.io/lolbas/), [WINDBG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential debugger evasion techniques by identifying suspicious access to processes combined with anti-debug API patterns in CallTrace, especially when originating from unbacked memory regions or non-standard execution paths. Filters known development tools and Windows error reporting.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious macOS LaunchAgent or LaunchDaemon Plist Modification
- **ID:** `T1647.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects suspicious modification or creation of macOS LaunchAgent or  LaunchDaemon property list files using command-line utilities. Focuses on persistence-related keys and abnormal execution contexts, filtering legitimate Apple system processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Serverless Function Persistence or Abuse
- **ID:** `T1648.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Detects suspicious creation or update of AWS Lambda functions by monitoring 
non-automated activity, unusual source IPs, and risky configurations. 
Focuses on bypassing CI/CD pipelines.


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Certificate and Private Key Export or Theft Activity
- **ID:** `T1649.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential theft of digital certificates and private keys via certutil abuse, PowerShell-based key export, or offensive tooling (e.g. Mimikatz crypto::export, Certify). Focuses on export operations, private key access, and suspicious output staging paths.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Account Acquisition and Initialization - T1650
- **ID:** `T1650.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Detects the acquisition or unauthorized setup of cloud accounts. Focuses on  credential configuration, profile creation, and automated SDK-based  identity harvesting while filtering out authorized DevOps automation.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Administration Agent Abuse
- **ID:** `T1651.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects anomalous process execution initiated by cloud management agents (AWS SSM, Azure Guest Agent). 
Attackers use these trusted paths to execute reconnaissance or credential dumping commands 
that bypass traditional network perimeter defenses.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Device Driver Enumeration From Anomalous Context (BYOVD Recon)
- **ID:** `T1652.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [PNPUTIL.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious device driver discovery activity using native Windows  utilities, WMI, or PowerShell from anomalous execution contexts.  Focuses on reconnaissance patterns commonly observed prior to  Bring Your Own Vulnerable Driver (BYOVD) abuse.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Power Settings Manipulation (T1137.001)
- **ID:** `T1653.yaml`
- **Minőségi mutató:** `50/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects unauthorized power setting modifications aimed at preventing sleep or 
hibernation. Focuses on command-line automation (powercfg) via suspicious 
parent processes like PowerShell or CMD, while filtering legitimate UI-based changes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**


---
## Suspicious Event Log Enumeration from Anomalous Execution Context
- **ID:** `T1654.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious enumeration of Windows event logs using native utilities  (wevtutil) or PowerShell cmdlets (Get-WinEvent, Get-EventLog) from anomalous  execution contexts. Focuses on log channel discovery and metadata harvesting  potentially used to identify security tooling or evade detection.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Impersonation via RunAs Abuse or Deceptive Local Account Creation
- **ID:** `T1656.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects technical impersonation attempts including suspicious RunAs usage  for lateral movement and creation of deceptive local accounts that mimic  executive or administrative identities outside standard IT provisioning processes.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Clipboard Manipulation and Financial Document Access From Untrusted Parent Process
- **ID:** `T1657.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects potential financial theft or fraud activity involving clipboard manipulation (e.g. address swapping) combined with access to financial documents, initiated from suspicious parent processes such as browsers, Office applications, or web-facing services.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Professional Content Impersonation and Infrastructure Mirroring
- **ID:** `T1659.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects tools and CLI patterns used to clone or impersonate legitimate web content. 
Focuses on recursive mirroring of internal portals and the use of phishing 
frameworks, filtering out legitimate development and browser-based activity.


#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Suspicious Access to LSASS Process Memory (Credential Dumping Attempt)
- **ID:** `credential_dumping_lsass.yml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/), [DUMP64.EXE](https://lolbas-project.github.io/lolbas/), [PROCDUMP.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Detects suspicious access to the LSASS process memory which may indicate credential dumping activity (e.g. Mimikatz, ProcDump, Task Manager dump, comsvcs.dll MiniDump, or other memory dumping techniques).


#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**

