# 🛡️ Detection Rule Knowledge Base

## 📖 Tartalomjegyzék
- [Suspicious Access to LSASS Process Memory](#suspicious-access-to-lsass-process-memory)
- [Rapid Logons to Multiple Distant Hosts by Same User](#rapid-logons-to-multiple-distant-hosts-by-same-user)
- [Suspicious RDP Logon from Unusual Source](#suspicious-rdp-logon-from-unusual-source)
- [Suspicious Base64-Encoded PowerShell Command with Network Activity](#suspicious-base64-encoded-powershell-command-with-network-activity)
- [Legitimate Windows Binary Copied to User-Writable Location](#legitimate-windows-binary-copied-to-user-writable-location)
- [Suspicious Remote Process Creation via WMIC](#suspicious-remote-process-creation-via-wmic)
- [Gyanús ütemezett feladat vagy munkakör létrehozása a Persistence (T1053) miatt](#gyanús-ütemezett-feladat-vagy-munkakör-létrehozása-a-persistence-(t1053)-miatt)
- [Suspicious Scheduled Task Creation Executing PowerShell](#suspicious-scheduled-task-creation-executing-powershell)
- [Suspicious Credential API Hooking via Win32 Libraries](#suspicious-credential-api-hooking-via-win32-libraries)
- [Suspicious Encoded PowerShell Command Execution](#suspicious-encoded-powershell-command-execution)
- [Suspicious SYSTEM Process Spawned from User Context](#suspicious-system-process-spawned-from-user-context)
- [Security Event Log Cleared Using wevtutil.exe](#security-event-log-cleared-using-wevtutilexe)
- [Suspicious Use of net user or net localgroup via cmd.exe](#suspicious-use-of-net-user-or-net-localgroup-via-cmdexe)
- [Suspicious Use of Built-in Windows Tools for File Download and Code Execution](#suspicious-use-of-built-in-windows-tools-for-file-download-and-code-execution)
- [Multiple Failed Login Attempts for Single User (Possible Password Guessing)](#multiple-failed-login-attempts-for-single-user-(possible-password-guessing))
- [Suspicious Cross-Site Scripting (XSS) Attempt Detected on Web Server](#suspicious-cross-site-scripting-(xss)-attempt-detected-on-web-server)
- [Suspicious File Download via Bitsadmin (High Fidelity)](#suspicious-file-download-via-bitsadmin-(high-fidelity))
- [Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity)](#suspicious-child-process-spawned-by-microsoft-office-application-(high-fidelity))
- [Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel](#adathalászat-rosszindulatú-linken-keresztül-domain-és-feladó-rendellenességekkel)
- [Suspicious Mshta Execution of Remote Script (High Fidelity)](#suspicious-mshta-execution-of-remote-script-(high-fidelity))
- [Suspicious Msiexec Installation from Remote URL (High Fidelity)](#suspicious-msiexec-installation-from-remote-url-(high-fidelity))
- [Suspicious Regsvr32 Execution Indicative of LOLBAS Abuse (High Fidelity)](#suspicious-regsvr32-execution-indicative-of-lolbas-abuse-(high-fidelity))
- [Suspicious Rundll32 Execution with Script or Remote Payload (High Fidelity)](#suspicious-rundll32-execution-with-script-or-remote-payload-(high-fidelity))
- [Suspicious Use of Legitimate Remote Administration Tools Outside Enterprise Pattern](#suspicious-use-of-legitimate-remote-administration-tools-outside-enterprise-pattern)
- [Ransomware Preparation Activity Detected on Windows Host (High Fidelity)](#ransomware-preparation-activity-detected-on-windows-host-(high-fidelity))
- [Suspicious Deletion of Volume Shadow Copies via VSSAdmin (High Fidelity)](#suspicious-deletion-of-volume-shadow-copies-via-vssadmin-(high-fidelity))
- [Webshell Upload or Interaction Detected on Web Server (High Fidelity)](#webshell-upload-or-interaction-detected-on-web-server-(high-fidelity))
- [Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services](#non-admin-user-attempting-to-stop-or-modify-multiple-sensitive-windows-services)
- [WMI Event Subscription Persistence via WMIC or PowerShell (High Fidelity)](#wmi-event-subscription-persistence-via-wmic-or-powershell-(high-fidelity))
- [Suspicious COM Hijacking for User-Level Persistence (High Fidelity)](#suspicious-com-hijacking-for-user-level-persistence-(high-fidelity))
- [Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása](#gyanús-rendszerindítási-vagy-bejelentkezési-automatikus-indítás-végrehajtása)
- [Suspicious Registry Run Key Modification for User Persistence (High Fidelity)](#suspicious-registry-run-key-modification-for-user-persistence-(high-fidelity))
- [UAC Bypass via Fodhelper Registry Hijack (High Fidelity)](#uac-bypass-via-fodhelper-registry-hijack-(high-fidelity))
- [Nem böngészős folyamat hozzáférése a böngésző hitelesítőadat-tárolóihoz (High Fidelity)](#nem-böngészős-folyamat-hozzáférése-a-böngésző-hitelesítőadat-tárolóihoz-(high-fidelity))
- [Gyanús Kerberos TGS jegykérés (Kerberoasting)](#gyanús-kerberos-tgs-jegykérés-(kerberoasting))
- [Gyanús elnevezett csővezeték-létrehozás, amely utólagos kihasználási eszközökhöz kapcsolódik (High Fidelity)](#gyanús-elnevezett-csővezeték-létrehozás-amely-utólagos-kihasználási-eszközökhöz-kapcsolódik-(high-fidelity))
- [Adatok gyanús archiválása exfiltráció céljából](#adatok-gyanús-archiválása-exfiltráció-céljából)
- [Biztonsági szolgáltatások gyanús leállítása](#biztonsági-szolgáltatások-gyanús-leállítása)
- [Windows Defender védelem kikapcsolása vagy módosítása PowerShell segítségével](#windows-defender-védelem-kikapcsolása-vagy-módosítása-powershell-segítségével)
- [Suspicious Firewall Modification via Netsh.exe](#suspicious-firewall-modification-via-netshexe)
- [High-Fidelity Offensive Infrastructure Provisioning - T1583](#high-fidelity-offensive-infrastructure-provisioning---t1583)
- [High-Fidelity Botnet Infrastructure Acquisition - T1583.005](#high-fidelity-botnet-infrastructure-acquisition---t1583005)
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
- [High-Fidelity Cloud Account Acquisition and Initialization - T1650](#high-fidelity-cloud-account-acquisition-and-initialization---t1650)
- [Credential Dumping LSASS](#credential-dumping-lsass)

---

## Suspicious Access to LSASS Process Memory
- **Azonosító:** `T1003_001.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Észleli a gyanús hozzáférést az LSASS folyamat memóriájához, ami hitelesítő adatok ellopására (Credential Dumping) utalhat.  A szabály figyeli a gyanús GrantedAccess maszkokat és szűri a gyakori legális folyamatokat.
- **Hamis pozitívok:** Antivírus szoftverek és EDR ügynökök mélyvizsgálata, Rendszerfelügyeleti eszközök (pl. SCCM, Tanium), Debuggerek használata jogosult adminisztrátorok által
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Rapid Logons to Multiple Distant Hosts by Same User
- **Azonosító:** `T1021.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Detects a single user successfully logging on to multiple different hosts within a short time window. This behavior may indicate stolen credentials, pass-the-hash, or lateral movement using valid accounts.
- **Hamis pozitívok:** Legitimate VPN reconnects causing new source IPs, Admin activity via multiple servers during maintenance, Misconfigured jump host naming conventions
- **MITRE ATT&CK:** `T1021`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## Suspicious RDP Logon from Unusual Source
- **Azonosító:** `T1021_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Detects successful RDP logons originating from unusual or non-enterprise sources, especially when targeting servers and performed by non-admin or rarely used accounts.
- **Hamis pozitívok:** First-time legitimate remote access from new location, Approved administrator working remotely via new VPN, Cloud-hosted management access not yet allowlisted
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## Suspicious Base64-Encoded PowerShell Command with Network Activity
- **Azonosító:** `T1027.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects PowerShell executions using Base64-encoded commands combined with network-based payload retrieval and non-interactive execution. This pattern is strongly associated with malware delivery, loaders, and post-exploitation frameworks.
- **Hamis pozitívok:** Rare advanced administrative automation using encoded commands, Approved red team or penetration testing activity
- **MITRE ATT&CK:** `T1027, T1105`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Legitimate Windows Binary Copied to User-Writable Location
- **Azonosító:** `T1036_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious copying of legitimate Windows system binaries into user-writable directories. This technique is commonly used by attackers for masquerading, DLL sideloading, or execution evasion by abusing trusted binary names.
- **Hamis pozitívok:** Rare advanced troubleshooting by administrators, Approved red team or malware simulation activity
- **MITRE ATT&CK:** `T1036, 005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Remote Process Creation via WMIC
- **Azonosító:** `T1047.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious usage of wmic.exe to create processes on remote hosts using the "process call create" method. This technique is commonly used by attackers for lateral movement after credential compromise.
- **Hamis pozitívok:** Rare administrative remote troubleshooting, Approved red team or penetration testing activity
- **MITRE ATT&CK:** `T1047`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Gyanús ütemezett feladat vagy munkakör létrehozása a Persistence (T1053) miatt
- **Azonosító:** `T1053.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Észleli az ütemezett feladatok vagy a több operációs rendszeren keresztüli adatmegőrzéshez használt feladatok gyanús létrehozását. A támadószerű végrehajtási mintákra összpontosít.
- **Hamis pozitívok:** Ritka adminisztratív automatizálás felhasználó által írható könyvtárak használatával, Egyedi IT karbantartási szkriptek végrehajtása ütemezett feladatokon keresztül
- **MITRE ATT&CK:** `T1053`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Scheduled Task Creation Executing PowerShell
- **Azonosító:** `T1053_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious creation of scheduled tasks using schtasks.exe that execute PowerShell, commonly abused by attackers to establish persistence or delayed execution of malicious payloads.
- **Hamis pozitívok:** Rare custom administrative automation, Approved red team or malware simulation activity
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Credential API Hooking via Win32 Libraries
- **Azonosító:** `T1056_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious processes loading combinations of Win32 libraries commonly abused for credential interception or API hooking, such as user32.dll, advapi32.dll, and win32u.dll. The rule focuses on non-system, user-writable execution paths and excludes common legitimate software to reduce false positives.
- **Hamis pozitívok:** Custom accessibility or assistive input software, Internally developed monitoring tools, Rare GUI utilities running from user directories
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Encoded PowerShell Command Execution
- **Azonosító:** `T1059_001.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious execution of PowerShell using encoded commands combined with execution bypass or obfuscation flags. This technique is commonly used by attackers to evade detection and execute malicious payloads in memory.
- **Hamis pozitívok:** Rare advanced administrative automation, Approved red team activity
- **MITRE ATT&CK:** `001, T1027`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious SYSTEM Process Spawned from User Context
- **Azonosító:** `T1068.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious processes running as SYSTEM that are spawned from user-initiated parent processes such as Explorer, browsers, or Office applications. This behavior may indicate privilege escalation, token manipulation, or UAC bypass exploitation.
- **Hamis pozitívok:** Rare custom administrative tooling, Approved software installation using custom launchers
- **MITRE ATT&CK:** `T1068`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Security Event Log Cleared Using wevtutil.exe
- **Azonosító:** `T1070_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects attempts to clear the Windows Security event log using wevtutil.exe, a common attacker technique used to cover tracks after credential access, lateral movement, or persistence.
- **Hamis pozitívok:** Rare emergency log maintenance by administrators, Approved red team or penetration testing activity
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Use of net user or net localgroup via cmd.exe
- **Azonosító:** `T1087.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious usage of cmd.exe executing net user or net localgroup commands, commonly used by attackers for account discovery or privilege escalation. The rule focuses on attacker-like execution context to reduce false positives.
- **Hamis pozitívok:** Rare administrative troubleshooting, Approved penetration testing activity
- **MITRE ATT&CK:** `T1087, T1098`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Use of Built-in Windows Tools for File Download and Code Execution
- **Azonosító:** `T1105.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious usage of built-in Windows utilities such as PowerShell, bitsadmin, and certutil to download files and execute code, a common attacker technique for payload staging and execution. The rule focuses on attacker-typical patterns and execution context to reduce false positives.
- **Hamis pozitívok:** Rare advanced administrative automation, Approved red team or malware simulation activity
- **MITRE ATT&CK:** `T1105, T1218`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Multiple Failed Login Attempts for Single User (Possible Password Guessing)
- **Azonosító:** `T1110_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Detects multiple failed authentication attempts for the same user account within a short time window, which may indicate password guessing or brute-force activity. The rule excludes common sources of authentication noise to reduce false positives.
- **Hamis pozitívok:** User repeatedly entering wrong password, Misconfigured application using user credentials, Legacy systems retrying authentication
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## Suspicious Cross-Site Scripting (XSS) Attempt Detected on Web Server
- **Azonosító:** `T1190.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Detects potential Cross-Site Scripting (XSS) attempts by identifying common reflected and encoded XSS payloads in HTTP requests, focusing on parameter-based injection patterns and excluding typical automated scanners to reduce false positives.
- **Hamis pozitívok:** Manual security testing by administrators, Approved penetration testing, Rare application-specific encoding behavior
- **MITRE ATT&CK:** `T1190`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## Suspicious File Download via Bitsadmin (High Fidelity)
- **Azonosító:** `T1197.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious file downloads performed using bitsadmin.exe, a deprecated but still abused Windows LOLBAS utility. The rule focuses on attacker-typical usage patterns, execution context, and download targets to reduce false positives.
- **Hamis pozitívok:** Rare legacy administrative scripts, Approved red team or malware simulation
- **MITRE ATT&CK:** `T1197`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity)
- **Azonosító:** `T1204.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious child processes spawned by Microsoft Office applications that are indicative of macro abuse, DDE exploitation, or document-based malware execution. The rule focuses on attacker- typical child processes, command-line patterns, and user-writable execution context to minimize false positives.
- **Hamis pozitívok:** Rare developer automation using Office COM, Approved red team / phishing simulation exercises
- **MITRE ATT&CK:** `T1204, T1059`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel
- **Azonosító:** `T1204_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Észleli a rosszindulatú linkeket tartalmazó adathalász e-maileket URL-rövidítők, újonnan regisztrált domainek és feladó spoofing alapján.
- **Hamis pozitívok:** Belső biztonsági kampányok, Legális tömeges levelezők
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Header elemzés:** Ellenőrizd a feladó valódi IP címét és az SPF/DKIM/DMARC státuszt.
2. **Link/Melléklet:** Vizsgáld meg az URL-t sandbox környezetben (pl. URLScan.io).
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Mshta Execution of Remote Script (High Fidelity)
- **Azonosító:** `T1218_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious execution of mshta.exe used to run scripts directly from remote URLs, a common LOLBAS technique used by attackers for initial execution and payload staging.
- **Hamis pozitívok:** Rare administrative scripts executed from internal web servers, Approved red team or penetration testing activity
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Msiexec Installation from Remote URL (High Fidelity)
- **Azonosító:** `T1218_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious use of msiexec.exe to install MSI packages directly from remote URLs, a technique commonly abused by attackers as a LOLBAS method. The rule focuses on attacker-typical command-line patterns and execution context to reduce false positives.
- **Hamis pozitívok:** Rare manual software installation by advanced administrators, Approved red team or penetration testing activity
- **MITRE ATT&CK:** `007`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Regsvr32 Execution Indicative of LOLBAS Abuse (High Fidelity)
- **Azonosító:** `T1218_010.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious usage of regsvr32.exe commonly associated with LOLBAS abuse (Squiblydoo technique), including execution of scriptlets, remote payloads, or DLLs from user-writable locations using attacker- typical command-line arguments.
- **Hamis pozitívok:** Rare legacy applications using scriptlets, Approved red team activity
- **MITRE ATT&CK:** `010`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Rundll32 Execution with Script or Remote Payload (High Fidelity)
- **Azonosító:** `T1218_011.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious usage of rundll32.exe commonly associated with LOLBAS abuse, including JavaScript execution, HTML applications, and loading payloads from remote or user-writable locations. The rule minimizes false positives by focusing on attacker-typical command-line patterns and execution context.
- **Hamis pozitívok:** Rare legacy applications abusing rundll32 for scripting, Approved red team or malware research activity
- **MITRE ATT&CK:** `011`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Use of Legitimate Remote Administration Tools Outside Enterprise Pattern
- **Azonosító:** `T1219.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious creation of services associated with legitimate remote administration tools (e.g. PsExec) when used outside approved enterprise management patterns. This behavior is commonly observed during lateral movement by attackers abusing admin tools.
- **Hamis pozitívok:** Approved penetration testing, Emergency troubleshooting from non-standard hosts (rare)
- **MITRE ATT&CK:** `T1219`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ransomware Preparation Activity Detected on Windows Host (High Fidelity)
- **Azonosító:** `T1486.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects ransomware preparation activity by identifying multiple recovery-inhibition and defense-evasion actions executed within a short time window. This includes disabling recovery options, deleting shadow copies, and stopping security-related services.
- **Hamis pozitívok:** Rare manual disaster recovery testing, Advanced troubleshooting by senior administrators
- **MITRE ATT&CK:** `T1486, T1490, 001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Deletion of Volume Shadow Copies via VSSAdmin (High Fidelity)
- **Azonosító:** `T1490.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious deletion of Volume Shadow Copies using vssadmin.exe, commonly observed during ransomware and destructive attacks. The rule focuses on attacker-typical command-line arguments, non-service execution context, and excludes known backup solutions to minimize false positives.
- **Hamis pozitívok:** Rare manual administrative maintenance, Approved disaster recovery testing
- **MITRE ATT&CK:** `T1490`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Webshell Upload or Interaction Detected on Web Server (High Fidelity)
- **Azonosító:** `T1505_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects potential webshell activity by identifying suspicious script uploads to web-accessible directories and subsequent interactions using command-execution style parameters. The rule minimizes false positives by focusing on attacker-typical paths, parameters, and access patterns.
- **Hamis pozitívok:** Legitimate file upload functionality with misconfiguration, Developer debugging on non-production systems, Approved penetration testing
- **MITRE ATT&CK:** `003, T1059`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Non-Admin User Attempting to Stop or Modify Multiple Sensitive Windows Services
- **Azonosító:** `T1543.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious behavior where a non-administrative user attempts to stop or modify multiple sensitive Windows services within a short time window. This behavior is commonly associated with defense evasion or persistence preparation activities.
- **Hamis pozitívok:** Rare helpdesk troubleshooting using non-standard privileges, Misconfigured enterprise automation
- **MITRE ATT&CK:** `T1543, T1562`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## WMI Event Subscription Persistence via WMIC or PowerShell (High Fidelity)
- **Azonosító:** `T1546_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation of permanent WMI event subscriptions used for persistence. The rule focuses on attacker-typical combinations of EventFilter, CommandLineEventConsumer, and FilterToConsumerBinding created via WMIC or PowerShell within the root\subscription namespace, while excluding known enterprise monitoring agents.
- **Hamis pozitívok:** Custom enterprise monitoring or compliance scripts, DFIR or red team activities
- **MITRE ATT&CK:** `T1546, 003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious COM Hijacking for User-Level Persistence (High Fidelity)
- **Azonosító:** `T1546_015.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious COM hijacking attempts used for user-level persistence by monitoring registry modifications of CLSID InprocServer32 and LocalServer32 entries pointing to non-standard execution paths. The rule focuses on HKCU modifications combined with scripting or LOLBin execution to reduce false positives.
- **Hamis pozitívok:** Rare legacy applications using user-level COM registration, Custom enterprise automation frameworks
- **MITRE ATT&CK:** `T1546, 015`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása
- **Azonosító:** `T1547.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Észleli a gyanús beállításjegyzékbeli vagy indítómappák módosításait, amelyeket az adatok megőrzése érdekében használnak, a nem szabványos elérési utakra és a gyanús végrehajtókra összpontosítva.
- **Hamis pozitívok:** Szoftverfrissítők, amelyek ideiglenes mappából futtatnak telepítőt a következő bejelentkezéskor., Egyedi vállalati scriptek a Startup mappában.
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Registry Run Key Modification for User Persistence (High Fidelity)
- **Azonosító:** `T1547_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious registry modifications used to establish user-level persistence via Windows Run and RunOnce keys. The rule focuses on non-standard executable locations combined with scripting engines to reduce false positives from legitimate software installations.
- **Hamis pozitívok:** Custom enterprise logon scripts, Rare legacy software using user-level Run keys
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## UAC Bypass via Fodhelper Registry Hijack (High Fidelity)
- **Azonosító:** `T1548_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects UAC bypass attempts abusing fodhelper.exe by monitoring registry hijacking of the ms-settings protocol combined with suspicious child process execution. This rule focuses on user-context auto-elevation to reduce false positives.
- **Hamis pozitívok:** Advanced administrative automation using fodhelper (rare), DFIR or red team activity
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Nem böngészős folyamat hozzáférése a böngésző hitelesítőadat-tárolóihoz (High Fidelity)
- **Azonosító:** `T1555.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Észleli a böngésző hitelesítőadat-tároló fájljaihoz való gyanús hozzáférést nem böngészőfolyamatok által. A szabály az ismert hitelesítőadat-adatbázisokhoz való olvasási hozzáférésre összpontosít, valamint a gyanús végrehajtási kontextusra, hogy csökkentse a téves riasztásokat, amelyek a biztonsági mentési ügynököktől, víruskereső szoftverektől és böngészőfrissítésektől származnak.
- **Hamis pozitívok:** Egyedi jelszókezelő eszközök, Kriminalisztikai vagy DFIR tevékenységek, Ritka vállalati végpontkezelési feladatok
- **MITRE ATT&CK:** `T1555`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Gyanús Kerberos TGS jegykérés (Kerberoasting)
- **Azonosító:** `T1558_003.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Észleli a gyanús Kerberos Service Ticket (TGS) kéréseket, amelyek Kerberoasting támadásra utalhatnak.  A szabály fókuszál a gyenge titkosítási típusokra (RC4) és szűri a gyakori legális zajt.
- **Hamis pozitívok:** Régi (legacy) alkalmazások, amelyek csak RC4 titkosítást támogatnak, Olyan környezetek, ahol a "Kerberos AES" nincs kényszerítve a szervizfiókokon, Bizonyos szkennerek vagy adminisztratív eszközök
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Gyanús elnevezett csővezeték-létrehozás, amely utólagos kihasználási eszközökhöz kapcsolódik (High Fidelity)
- **Azonosító:** `T1559_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** A gyanús nevesített csővezetékek létrehozásának nagy pontosságú észlelése, amelyek gyakran kapcsolódnak az oldalirányú mozgáshoz és a kihasználás utáni keretrendszerekhez. A szabály az ismert rosszindulatú csővezeték-neveket, a véletlenszerű csővezeték-mintákat, a LOLBin végrehajtási kontextust és a szigorú engedélyezési listákat ötvözi a téves riasztások minimalizálása érdekében.
- **Hamis pozitívok:** Custom in-house IPC mechanisms, Rare administrative tooling using randomized pipe names
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Adatok gyanús archiválása exfiltráció céljából
- **Azonosító:** `T1560.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Észleli a fájlok gyanús tömörítését és archiválását (7z, rar, tar, PowerShell), különösen ha jelszavas védelmet  alkalmaznak vagy gyanús ideiglenes könyvtárakat használnak célhelyként.
- **Hamis pozitívok:** Rendszergazdai mentési scriptek, Szoftverfrissítések, amelyek ideiglenes mappákban tömörítenek, Felhasználók, akik jelszóval védett tömörítményt készítenek legális célból
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Biztonsági szolgáltatások gyanús leállítása
- **Azonosító:** `T1562.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Észleli a kritikus biztonsági szolgáltatások (Antivírus, EDR, Tűzfal) leállítására irányuló kísérleteket  olyan eszközökkel, mint a net.exe, sc.exe vagy PowerShell. Ez a védelem kiiktatására irányuló támadói tevékenység.
- **Hamis pozitívok:** Rendszergazdák által végzett hibaelhárítás vagy szoftvercsere, Biztonsági ügynökök frissítése (néha leállítják és újraindítják magukat)
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Windows Defender védelem kikapcsolása vagy módosítása PowerShell segítségével
- **Azonosító:** `T1562_001.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Észleli, amikor a támadók PowerShell segítségével próbálják megváltoztatni a Windows Defender beállításait,  például a valós idejű védelem kikapcsolásával vagy kivételek hozzáadásával. Ez a technika a védelem megkerülésére szolgál.
- **Hamis pozitívok:** Központilag kezelt biztonsági beállítások módosítása Group Policy-n keresztül, IT biztonsági csapat által végzett tesztelés vagy karbantartás, Szoftvertelepítők, amelyek automatikusan adnak hozzá kivételeket (pl. SQL Server)
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious Firewall Modification via Netsh.exe
- **Azonosító:** `T1562_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Észleli, amikor a támadók a netsh.exe eszközt használják a Windows tűzfal szabályainak módosítására vagy új,  engedékeny szabályok hozzáadására. Ez gyakran a védelem megkerülésére (Impair Defenses) utal.
- **Hamis pozitívok:** Legitim szoftvertelepítők (pl. VPN kliensek, hálózati eszközök), SCCM vagy egyéb távoli felügyeleti eszközök által futtatott konfigurációs szkriptek, Rendszergazdák manuális hibajavítása
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Offensive Infrastructure Provisioning - T1583
- **Azonosító:** `T1583.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the automated acquisition of infrastructure (VPS, Domains, Serverless)  by monitoring for CLI-based provisioning tools and domain registration API calls.  Filters focus on isolating authorized DevOps pipelines and developer environments.
- **Hamis pozitívok:** IT administrators testing Terraform scripts locally., Authorized developers managing secondary testing domains., Automated billing or monitoring scripts that use VPS APIs.
- **MITRE ATT&CK:** `T1583`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Botnet Infrastructure Acquisition - T1583.005
- **Azonosító:** `T1583_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the acquisition and preparation of botnet infrastructure.  Focuses on identifying multi-architecture agent downloads, automated  propagation attempts (brute-force), and botnet C2 client usage.
- **Hamis pozitívok:** Authorized vulnerability scanners or red team exercises., Network admins performing bulk configuration changes via SSH scripts., Security researchers in isolated malware analysis environments.
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Identity Enumeration via Authentication Endpoints
- **Azonosító:** `T1589.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence identity reconnaissance activity where an external actor enumerates valid user identities via authentication or account-related endpoints. Detection is based on enumeration behavior, automation indicators, and authentication response patterns, excluding browsers, SSO flows, and monitoring tools.
- **Hamis pozitívok:** Explicitly approved external identity testing, Rare API-based account validation by trusted partners
- **MITRE ATT&CK:** `T1589`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Credential Enumeration via Authentication API (High Confidence)
- **Azonosító:** `T1589_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence credential enumeration activity against authentication APIs. The rule focuses on automated, non-interactive probing behavior attempting to validate the existence or correctness of credentials. Browser-based logins, SSO flows, monitoring systems, and legitimate user authentication are excluded to minimize false positives.
- **Hamis pozitívok:** Explicitly approved red team credential enumeration, Rare third-party integration misconfiguration
- **MITRE ATT&CK:** `T1589, 001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Confidence OSINT Identity Enumeration via Public APIs
- **Azonosító:** `T1589_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence open-source identity enumeration attempts via public-facing APIs or directory endpoints. This rule focuses on scripted, automated reconnaissance behavior designed to collect user or employee identity data, while excluding normal browsing, search engines, and legitimate crawlers to minimize false positives.
- **Hamis pozitívok:** Explicitly approved OSINT or data aggregation jobs, Rare third-party integrations misconfigured to scrape directories
- **MITRE ATT&CK:** `T1589, 002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Targeted OSINT Enumeration of Open Websites and Domains
- **Azonosító:** `T1589_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence reconnaissance activity targeting open websites and domains to gather victim identity information. The rule focuses on scripted enumeration behavior against search or directory-style endpoints, excluding browsers, crawlers, and legitimate monitoring traffic to ensure very low false positive rates.
- **Hamis pozitívok:** Explicitly approved OSINT or red team reconnaissance, Rare third-party integrations misconfigured to enumerate directories
- **MITRE ATT&CK:** `T1589, 003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Network Reconnaissance with High Port Diversity
- **Azonosító:** `T1590.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects network reconnaissance activity. Optimized for cross-SIEM compatibility by using standard field names and avoiding complex CIDR logic in the core rule.
- **Hamis pozitívok:** Authorized vulnerability scanners
- **MITRE ATT&CK:** `T1590`

#### 🚨 Response Playbook
1. **IP hírnév:** Ellenőrizd a távoli IP címet hírnév-adatbázisokban.
2. **Forgalom elemzés:** Vizsgáld meg a küldött adatmennyiséget és a protokoll típusát.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Professional IP Infrastructure Reconnaissance - T1590.001
- **Azonosító:** `T1590_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Detects professional IP discovery techniques by focusing on reconnaissance-specific  command arguments and external IP lookup services, while filtering out  standard Windows networking noise.
- **Hamis pozitívok:** IT Support troubleshooting network issues, Automated software update checks
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## Advanced DNS Infrastructure Reconnaissance - T1590.002
- **Azonosító:** `T1590_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects systematic DNS reconnaissance. It reduces false positives by filtering  legitimate single-host lookups and focusing on infrastructure-wide enumeration  attempts like Zone Transfers or specific record harvesting.
- **Hamis pozitívok:** High-level network troubleshooting by Domain Admins, Automated IT inventory or audit scripts
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Network Trust Dependencies Reconnaissance - T1590.003
- **Azonosító:** `T1590_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects systematic discovery of network trust relationships and shared resources.  It minimizes noise by filtering standard GPO-driven drive mappings and focused  on high-intent enumeration commands like nltest domain trusts and remote session listing.
- **Hamis pozitívok:** System administrators auditing domain trusts., Legacy login scripts mapping drives on old workstations., Automated security assessment tools (authorized).
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Certificate Information Reconnaissance - T1590.004
- **Azonosító:** `T1590_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects professional reconnaissance of digital certificates. Focuses on  interactive command-line tools used to extract metadata from local stores  or remote servers while filtering out automated signature verification.
- **Hamis pozitívok:** Security engineers troubleshooting TLS issues., Automated certificate renewal agents (e.g., Let's Encroll).
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Cloud Infrastructure Reconnaissance - T1590.005
- **Azonosító:** `T1590_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects manual or suspicious cloud infrastructure enumeration.  It filters out legitimate CI/CD pipelines and automated service accounts  to focus on interactive discovery.
- **Hamis pozitívok:** Legitimate manual cloud audit by certified admins., New automation scripts not yet added to filters.
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Victim Web Page Info Reconnaissance - T1590.006
- **Azonosító:** `T1590_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated web reconnaissance and sensitive file discovery attempts.  It minimizes false positives by filtering development environments and focusing  on high-intent reconnaissance patterns across CLI tools.
- **Hamis pozitívok:** Developers debugging cloud configurations or APIs., Legitimate security auditing or automated penetration testing.
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Organizational Infrastructure Enumeration - T1591
- **Azonosító:** `T1591.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects systematic gathering of organizational metadata (OUs, groups, users).  It minimizes false positives by filtering known administrative consoles,  service account syncs, and focusing on non-standard execution contexts.
- **Hamis pozitívok:** Identity Management synchronization tasks., IT audits or mass user updates., Vulnerability scanners with domain credentials.
- **MITRE ATT&CK:** `T1591`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Physical Location Infrastructure Enumeration - T1591.001
- **Azonosító:** `T1591_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects systematic discovery of physical infrastructure data (floor plans, badge systems).  It filters out common office usage (Intranet, Visio) and focuses on CLI-based  bulk search operations which are characteristic of reconnaissance before physical  intrusion or social engineering.
- **Hamis pozitívok:** Facilities staff or architects working on building plans., New employees searching for company maps via command line (unlikely)., Automated backup of CAD/Visio servers.
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Business Relationship Information Discovery - T1591.002
- **Azonosító:** `T1591_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects systematic and automated discovery of business relationships.  It filters out common office productivity noise and focuses on bulk  search operations originating from non-standard parent processes.
- **Hamis pozitívok:** Legal or Finance team performing legitimate data migration., Desktop search tools indexing local documents.
- **MITRE ATT&CK:** `002, T1591`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Knowledge Management Discovery - T1591.003
- **Azonosító:** `T1591_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects systematic and automated discovery of internal knowledge management systems.  It targets bulk data extraction patterns and command-line reconnaissance  while filtering out standard web browser usage and IT automation.
- **Hamis pozitívok:** IT administrators performing site migrations or bulk edits via API., Authorized security scanners auditing internal documentation., Legitimate automated backup tasks.
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Personnel Information Discovery - T1591.004
- **Azonosító:** `T1591_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious, bulk extraction of employee data from Active Directory.  Focuses on non-standard LDAP queries and broad PowerShell filters that  deviate from routine administrative behavior.
- **Hamis pozitívok:** Bulk user audits by internal compliance teams., New HR system integration testing., Complex AD reporting scripts by senior admins.
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Host Information Reconnaissance Activity
- **Azonosító:** `T1592.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence host information reconnaissance activity by identifying multiple system discovery commands executed in a short timeframe from a user context. Tuned to minimize false positives by excluding SYSTEM activity, enterprise tooling, and single benign command executions.
- **Hamis pozitívok:** Rare advanced troubleshooting directly from user shell, Approved red team or DFIR activity
- **MITRE ATT&CK:** `T1592`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Confidence Hardware Enumeration via Management Interfaces
- **Azonosító:** `T1592_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence reconnaissance activity where an external source attempts to enumerate hardware characteristics such as CPU, architecture, memory, or device model via management or embedded system interfaces. The rule is optimized to minimize false positives by focusing on automated probing behavior.
- **Hamis pozitívok:** Vendor support accessing hardware management interfaces from external networks, Approved red team activity not allowlisted
- **MITRE ATT&CK:** `T1592, 001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Software Enumeration Reconnaissance via Web Endpoints
- **Azonosító:** `T1592_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects advanced reconnaissance activity where an external actor systematically enumerates installed software, application names, or version information through multiple web-accessible endpoints in a short time window. Tuned to minimize false positives by requiring automation-like behavior and repeated probing patterns.
- **Hamis pozitívok:** Explicitly approved external vulnerability scanning, Vendor troubleshooting performed from non-browser tools
- **MITRE ATT&CK:** `T1592, 002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Confidence Firmware Enumeration Against Network Devices
- **Azonosító:** `T1592_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence reconnaissance activity targeting firmware and version information of network or embedded devices. The rule focuses on automated, non-browser access to device-specific management endpoints and is optimized to minimize false positives.
- **Hamis pozitívok:** Vendor support accessing device management interfaces from external networks, Approved red team activity not allowlisted
- **MITRE ATT&CK:** `T1592, 003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Confidence Client Configuration Fingerprinting (Reconnaissance)
- **Azonosító:** `T1592_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Detects high-confidence reconnaissance activity where an external source performs repeated non-browser HTTP requests using probing methods and header-focused techniques to enumerate client or infrastructure configurations. Optimized to minimize false positives.
- **Hamis pozitívok:** Custom external API clients without browser User-Agent (rare), Approved red team activity if not allowlisted
- **MITRE ATT&CK:** `T1592, 004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## High-Fidelity Automated Web Reconnaissance - T1593
- **Azonosító:** `T1593.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated web scraping and OSINT collection patterns targeting  social media and public sites. Focuses on headless browser automation  and specialized CLI tools while filtering out legitimate HR and Marketing activity.
- **Hamis pozitívok:** Marketing teams using automated tools for brand monitoring., HR department using LinkedIn automation for bulk recruiting., Software testing (QA) using Selenium/Webdriver.
- **MITRE ATT&CK:** `T1593`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Social Media Entity Harvesting - T1593.001
- **Azonosító:** `T1593_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated reconnaissance of social media profiles. It targets headless  browser automation (Selenium/Puppeteer) and specialized OSINT tools while  filtering out routine HR recruitment and interactive browser usage.
- **Hamis pozitívok:** Authorized recruiters using browser automation for bulk messaging., QA engineers testing social auth flows via Selenium., Marketing analytics scripts (if not run from a server).
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Automated Search Engine Reconnaissance - T1593.002
- **Azonosító:** `T1593_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated reconnaissance using search engines by monitoring for headless  browser flags and systematic dorking patterns. Specifically filters out  legitimate developer activity and interactive browser usage to minimize false positives.
- **Hamis pozitívok:** SEO/Marketing tools performing automated ranking checks., Developers using CLI-based search for error code resolution., Vulnerability scanners (authorized).
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Social Media Entity Harvesting - T1593.003
- **Azonosító:** `T1593_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated social media reconnaissance using headless browsers or specialized OSINT tools.  Focuses on identifying systematic data scraping while excluding legitimate browser-based user activity.
- **Hamis pozitívok:** Authorized recruitment automation tools used by HR., Social media management platforms (Hootsuite, etc.)., QA engineers testing web applications with Selenium.
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Information Repository Reconnaissance - T1594
- **Azonosító:** `T1594.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated reconnaissance of public information repositories (GitHub, GitLab).  Focuses on specialized secret scanners and bulk API harvesting while filtering out  standard developer workflows (git clone/pull) and authorized security tools.
- **Hamis pozitívok:** Security engineers performing authorized secret scanning., Developers using automated scripts for local repo management., Automated backup scripts for code repositories.
- **MITRE ATT&CK:** `T1594`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Active Scanning Detection (Behavior-Based)
- **Azonosító:** `T1595.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence active scanning behavior by identifying automated clients systematically probing multiple sensitive web endpoints from an external source within a short timeframe. Designed to minimize false positives by excluding browsers, monitoring, health checks, and known benign scanners.
- **Hamis pozitívok:** Explicitly approved external vulnerability scans, Rare external troubleshooting using CLI tools
- **MITRE ATT&CK:** `T1595`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity External IP Block Scanning Detection
- **Azonosító:** `T1595_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence active scanning behavior where a single external source IP rapidly probes multiple destination IP addresses within a short time window. Optimized to reduce false positives by excluding known scanners, crawlers, and cloud infrastructure.
- **Hamis pozitívok:** Rare misconfigured external services, Newly deployed monitoring not yet allowlisted
- **MITRE ATT&CK:** `T1595, 001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Confidence External Vulnerability Scanning Activity
- **Azonosító:** `T1595_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence vulnerability scanning activity by correlating aggressive request behavior, exploit discovery paths, payload indicators, and known scanner tooling. Optimized to minimize false positives in enterprise environments.
- **Hamis pozitívok:** Approved external penetration tests not yet allowlisted, Newly onboarded security vendors performing scans
- **MITRE ATT&CK:** `T1595, 002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Active Wordlist Scanning Against Authentication Endpoints
- **Azonosító:** `T1595_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-confidence wordlist scanning activity where an external source rapidly probes authentication or administrative endpoints using varying username parameters, consistent with automated reconnaissance.
- **Hamis pozitívok:** Custom API clients without browser User-Agent (rare), Approved red team activity not allowlisted
- **MITRE ATT&CK:** `T1595, 003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Open Technical Database Reconnaissance - T1596
- **Azonosító:** `T1596.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the systematic use of CLI tools and script-based API queries directed  at technical databases like Shodan, Censys, and VirusTotal.  Focuses on non-browser process chains and automated data extraction patterns.
- **Hamis pozitívok:** Authorized vulnerability assessments., Threat hunters performing manual investigations., Automated cloud asset inventory scripts.
- **MITRE ATT&CK:** `T1596`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity WHOIS Database Reconnaissance - T1596.001
- **Azonosító:** `T1596_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated WHOIS reconnaissance patterns. Focuses on bulk domain registration  queries via CLI tools and API-based scripts (RDAP) while filtering out standard  browser-based research, software licensing, and routine IT diagnostics.
- **Hamis pozitívok:** Domain administrators verifying registration details via CLI., Legal departments using WHOIS APIs for trademark enforcement., Procurement auditing vendor domain ownership.
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Automated Search Engine Dorking - T1596.002
- **Azonosító:** `T1596_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the automated use of search engine dorks and specialized CLI tools  designed for bulk technical data harvesting. Filters out interactive browser  searches and legitimate IDE-triggered error lookups.
- **Hamis pozitívok:** Security analysts performing authorized audits for exposed files., Marketing or SEO tools using automated scripts for ranking checks., Developers using CLI-based search tools for documentation.
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Passive DNS Reconnaissance - T1597.003
- **Azonosító:** `T1596_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated reconnaissance using Passive DNS (pDNS) databases.  Focuses on non-standard process chains and CLI-based API interactions  targeting technical OSINT repositories while filtering out routine  network troubleshooting and browser-based research.
- **Hamis pozitívok:** Security analysts performing authorized incident investigations., IT automation scripts verifying public DNS records for service health., Authorized red-team exercises.
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Digital Certificate Reconnaissance - T1596.004
- **Azonosító:** `T1596_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated reconnaissance targeting Digital Certificates and CT logs.  Focuses on programmatic CLI patterns (API-based scraping) while filtering  out legitimate system-level certificate validation and browser traffic.
- **Hamis pozitívok:** DevOps automation for SSL certificate renewal (e.g., ACME/Let's Encrypt)., Internal PKI health checks performed by network admins., Security analysts performing authorized external audits.
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity IP Infrastructure Reconnaissance - T1596.005
- **Azonosító:** `T1596_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated reconnaissance of IP address metadata. Focuses on specialized  OSINT tools (Shodan, GreyNoise, Censys) and CLI-based API harvesting while  filtering out routine network troubleshooting, browser traffic, and EDR noise.
- **Hamis pozitívok:** Security analysts manually investigating an IP address via CLI., Authorized vulnerability management tools performing asset inventory., IT automation scripts verifying public-facing service exposure.
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Victim-Owned Website Reconnaissance - T1597
- **Azonosító:** `T1597.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated and systematic reconnaissance of organization-owned  web infrastructure. Focuses on bulk data extraction, recursive directory  brute-forcing, and the discovery of sensitive configuration files.
- **Hamis pozitívok:** Web developers performing site migrations or integrity checks., Legitimate vulnerability scanners (e.g., Nessus, Burp Suite) if not excluded by IP., Automated SEO crawling tools used by marketing.
- **MITRE ATT&CK:** `T1597`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Domain Infrastructure Enumeration - T1597.001
- **Azonosító:** `T1597_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects advanced and automated domain/DNS reconnaissance. Focuses on  unusual DNS query types (AXFR, ANY) and professional sub-domain discovery  tools while filtering out routine network troubleshooting.
- **Hamis pozitívok:** Network engineers performing deep DNS audits or migrations., Security vulnerability scanners performing asset discovery., Automated cloud-sync tools verifying domain ownership (e.g., Let's Encrypt).
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Secret Hunting in Code Repositories - T1597.002
- **Azonosító:** `T1597_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects professional secret-hunting tools and manual reconnaissance patterns  within code repositories. Focuses on deep history analysis (diff-searching)  and automated credential extraction while filtering out standard dev-cycles.
- **Hamis pozitívok:** Security engineers performing authorized baseline scans of repositories., Pre-commit hooks that use gitleaks or similar tools to prevent secrets from being pushed., Developers searching for a specific past change where a credential was used as a placeholder.
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Phishing for Info & Credential Harvesting - T1598
- **Azonosító:** `T1598.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects post-phishing credential harvesting and session token theft.  Focuses on non-browser processes accessing browser profile data and  suspicious interactive credential prompts.
- **Hamis pozitívok:** IT support scripts used for legitimate credential collection., Browser profile backup tools., User-initiated manual profile migration.
- **MITRE ATT&CK:** `T1598`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Spearphishing Link Redirection - T1598.001
- **Azonosító:** `T1598_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious URL execution patterns originating from productivity apps.  Focuses on indirect browser launches (via cmd/powershell) and OAuth-specific  credential harvesting parameters while filtering out known SSO providers.
- **Hamis pozitívok:** Security awareness training platforms (e.g., KnowBe4)., Legitimate OAuth flows for third-party business apps (e.g., Zoom, Trello)., External HR or Payroll portals using complex redirect strings.
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced BEC Mail & Financial Data Exfiltration - T1598.002
- **Azonosító:** `T1598_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious command-line access to mail archives and financial documents  typically targeted in BEC campaigns. It filters out legitimate Outlook  indexing, OneDrive synchronization, and system-level backups.
- **Hamis pozitívok:** Manual PST migration by IT support during workstation refresh., User manually zipping their own mail folder for archiving., Accounting software running local search/export tasks.
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity MFA/OTP Spoofing & Harvesting - T1598.003
- **Azonosító:** `T1598_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation of fraudulent MFA/OTP input prompts by monitoring  unusual PowerShell UI class loading and specific CLI keywords.  Filters out common IT automation and software deployment noise.
- **Hamis pozitívok:** Legitimate IT support tools that prompt users for a temporary password or code., In-house applications using PowerShell wrappers for basic UI interaction.
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Spearphishing Attachment Interaction - T1598.004
- **Azonosító:** `T1598_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious execution patterns from email attachments. Focuses on HTML  smuggling and Office-to-script transitions while filtering out legitimate  SharePoint, OneDrive, and enterprise software update noise.
- **Hamis pozitívok:** Internal business automation using Excel macros to pull data via PowerShell., Software installers opening "ReadMe" or "Release Notes" in HTML format., Users saving legitimate web pages for offline viewing.
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Cloud Account Acquisition and Initialization - T1650
- **Azonosító:** `T1650.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the acquisition or unauthorized setup of cloud accounts. Focuses on  credential configuration, profile creation, and automated SDK-based  identity harvesting while filtering out authorized DevOps automation.
- **Hamis pozitívok:** Cloud administrators configuring their local environment for the first time., Legitimate automated deployment scripts not run through central engines., Developers debugging cloud integration locally.
- **MITRE ATT&CK:** `T1650`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Credential Dumping LSASS
- **Azonosító:** `credential_dumping_lsass.yml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** a hitelesito adatok LSASS folyamatmemoriabol torteno kiirasara tett kiserlet
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1003, 001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

