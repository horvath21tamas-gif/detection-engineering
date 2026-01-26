# 🛡️ Detection Rule Knowledge Base

## 📖 Tartalomjegyzék
- [Suspicious Access to LSASS Process Memory](#suspicious-access-to-lsass-process-memory)
- [Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastol tavol levo hostra jelentkezik be](#detektalni-ugyanazon-felhasznalotol-rovid-idon-belul-tobb-egymastol-tavol-levo-hostra-jelentkezik-be)
- [Gyanus RDP belepes](#gyanus-rdp-belepes)
- [Detektalni a poweshellbol base64-encoded parancsot](#detektalni-a-poweshellbol-base64-encoded-parancsot)
- [A tamado lemasol egy legitim Windows binarist](#a-tamado-lemasol-egy-legitim-windows-binarist)
- [Tavoli hoston inditott folyamat wmic.exe segitsegevel](#tavoli-hoston-inditott-folyamat-wmicexe-segitsegevel)
- [Gyanús ütemezett feladat vagy munkakör létrehozása a Persistence (T1053) miatt](#gyanús-ütemezett-feladat-vagy-munkakör-létrehozása-a-persistence-(t1053)-miatt)
- [Gyanus Scheduled Task letrehozasa](#gyanus-scheduled-task-letrehozasa)
- [Suspicious Credential API Hooking via Win32 APIs](#suspicious-credential-api-hooking-via-win32-apis)
- [Gyanus Poweshell parancs vegrehajtasa](#gyanus-poweshell-parancs-vegrehajtasa)
- [Gyanus System process melyet a user indit](#gyanus-system-process-melyet-a-user-indit)
- [wevtutil.exe security logokat torol](#wevtutilexe-security-logokat-torol)
- [cmd.exe netuser vagy net localgroup parancsot futtat](#cmdexe-netuser-vagy-net-localgroup-parancsot-futtat)
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

## Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastol tavol levo hostra jelentkezik be
- **Azonosító:** `T1021.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastpl tavol levo hostra jelentkezik be
- **Hamis pozitívok:** VPN bejelentkezés, jump host, admin script
- **MITRE ATT&CK:** `T1021`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## Gyanus RDP belepes
- **Azonosító:** `T1021_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Gyanus RDP belepes
- **Hamis pozitívok:** Admin script, teszteles
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## Detektalni a poweshellbol base64-encoded parancsot
- **Azonosító:** `T1027.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detektalni a powershellbol a base64-encoded parancsot
- **Hamis pozitívok:** admin scriptet futtat, pentesteles
- **MITRE ATT&CK:** `T1027, T1105`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## A tamado lemasol egy legitim Windows binarist
- **Azonosító:** `T1036_005.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** A tamado lemasol egy legitim Windows binarist
- **Hamis pozitívok:** legitim file, teszteles
- **MITRE ATT&CK:** `005, T1036`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Tavoli hoston inditott folyamat wmic.exe segitsegevel
- **Azonosító:** `T1047.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Tavoli hoston inditott folyamat wmic.exe segitsegevel
- **Hamis pozitívok:** admin scriptek, management tooling
- **MITRE ATT&CK:** `T1047`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

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

## Gyanus Scheduled Task letrehozasa
- **Azonosító:** `T1053_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Gyanus Scheduled Task letrehozasa
- **Hamis pozitívok:** admin automatizacio, backup
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## Suspicious Credential API Hooking via Win32 APIs
- **Azonosító:** `T1056_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious processes loading Win32 libraries commonly abused for credential API hooking such as keylogging or credential interception.
- **Hamis pozitívok:** Accessibility software, Screen recording or input method tools, Legitimate security software
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Gyanus Poweshell parancs vegrehajtasa
- **Azonosító:** `T1059_001.yaml`
- **Minőségi mutató:** `50/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Poweshell parancsok eszlelese, melyek hasznalhatoak rosszindulatu kodok futtatasara
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001, T1027`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## Gyanus System process melyet a user indit
- **Azonosító:** `T1068.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Gyanus System process melyet a user indit
- **Hamis pozitívok:** fejlesztesek miatti alert, update/telepites
- **MITRE ATT&CK:** `T1068`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## wevtutil.exe security logokat torol
- **Azonosító:** `T1070_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** wevtutil.exe security logokat torol
- **Hamis pozitívok:** admin legitim script, pentesteles
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## cmd.exe netuser vagy net localgroup parancsot futtat
- **Azonosító:** `T1087.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** cmd.exe netuser vagy net localgroup parancsot futtat
- **Hamis pozitívok:** admin futtat, pentesteles
- **MITRE ATT&CK:** `T1087, T1098`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

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

