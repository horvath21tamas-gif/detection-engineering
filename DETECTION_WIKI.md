# 🛡️ Detection Rule Knowledge Base

### Suspicious Access to LSASS Process
- **Azonosító:** `T1003_001`
- **Leírás:** Detektalni a process dumpingot LSASS memoriaban
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** Antivirus or EDR solutions, System administrators hsznal debugging tool-t

---
### Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastol tavol levo hostra jelentkezik be
- **Azonosító:** `T1021`
- **Leírás:** Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastpl tavol levo hostra jelentkezik be
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** VPN bejelentkezés, jump host, admin script

---
### Gyanus RDP belepes
- **Azonosító:** `T1021_001`
- **Leírás:** Gyanus RDP belepes
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** Admin script, teszteles

---
### Detektalni a poweshellbol base64-encoded parancsot
- **Azonosító:** `T1027`
- **Leírás:** Detektalni a powershellbol a base64-encoded parancsot
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** admin scriptet futtat, pentesteles

---
### A tamado lemasol egy legitim Windows binarist
- **Azonosító:** `T1036_005`
- **Leírás:** A tamado lemasol egy legitim Windows binarist
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** legitim file, teszteles

---
### Tavoli hoston inditott folyamat wmic.exe segitsegevel
- **Azonosító:** `T1047`
- **Leírás:** Tavoli hoston inditott folyamat wmic.exe segitsegevel
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** admin scriptek, management tooling

---
### Gyanus Scheduled Task letrehozasa
- **Azonosító:** `T1053_005`
- **Leírás:** Gyanus Scheduled Task letrehozasa
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** admin automatizacio, backup

---
### Suspicious Credential API Hooking via Win32 APIs
- **Azonosító:** `T1056_004`
- **Leírás:** Detects suspicious processes loading Win32 libraries commonly abused for credential API hooking such as keylogging or credential interception.
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** Accessibility software, Screen recording or input method tools, Legitimate security software

---
### Gyanus Poweshell parancs vegrehajtasa
- **Azonosító:** `T1059_001`
- **Leírás:** Poweshell parancsok eszlelese, melyek hasznalhatoak rosszindulatu kodok futtatasara
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** Nincs megadva

---
### Gyanus System process melyet a user indit
- **Azonosító:** `T1068`
- **Leírás:** Gyanus System process melyet a user indit
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** fejlesztesek miatti alert, update/telepites

---
### wevtutil.exe security logokat torol
- **Azonosító:** `T1070_001`
- **Leírás:** wevtutil.exe security logokat torol
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** admin legitim script, pentesteles

---
### cmd.exe netuser vagy net localgroup parancsot futtat
- **Azonosító:** `T1087`
- **Leírás:** cmd.exe netuser vagy net localgroup parancsot futtat
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** admin futtat, pentesteles

---
### egy felhasznalo beepitett windows eszkozoket hasznal fajl letoltesre es kodfuttatasra
- **Azonosító:** `T1105`
- **Leírás:** rosszindulatu fajl letoltese / kod futtatasa
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** Nincs megadva

---
### tobbszori sikertelen bejelentkezes egy felhasznalohoz
- **Azonosító:** `T1110_001`
- **Leírás:** Egy adott ido alatt tortent sok sikertelen bejelentkezes egy felhasznalotol
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** Nincs megadva

---
### webszeren tortent XSS probakozas
- **Azonosító:** `T1190`
- **Leírás:** None
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** Nincs megadva

---
### bitsadmin.exe segitsegevel fajl letoltes
- **Azonosító:** `T1197`
- **Leírás:** bitsadmin.exe segitsegevel fajl letoltese
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** update, regebbi admin script

---
### Gyanus folyamatot inditott a Microsoft office valamelyik alkalmazasa
- **Azonosító:** `T1204`
- **Leírás:** Eszlelni a Microsoft Office altal letrehozott chilprocesseket
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** Nincs megadva

---
### Gyanus mshta.exe URL-rol futtat scriptet
- **Azonosító:** `T1218_005`
- **Leírás:** Gyanus mshta.exe URL-rol futtat scriptet
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** admin script futtatasa, pentesteles

---
### msiexec.exe URL-rol telepit csomagot
- **Azonosító:** `T1218_007`
- **Leírás:** misexec.exe URL-rol telepit csomagot
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** admin frissít, pentesteles

---
### Gyanus regsvr32.exe futtatasa
- **Azonosító:** `T1218_010`
- **Leírás:** Gyanus regsvr32.exe futtatasa
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** regi alkalmazasok, frissites

---
### Gyanus rundll32.exe hasznalata
- **Azonosító:** `T1218_011`
- **Leírás:** Gyanus rundll32.exe hasznalata
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** legit alkalmazasok, driver telepito

---
### Detektalni, amikor egy legitim remote admin toolt nem a megszokott enterprise modon hasznalnak
- **Azonosító:** `T1219`
- **Leírás:** Detektalni, amikor egy ligitim remote admin toolt nem a megszokott enterprise modon hasznalnak
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** pentest gyakorlat, admin fejlesztés

---
### Ransomware elokeszites eszlelese
- **Azonosító:** `T1486`
- **Leírás:** Ransomware elokeszites eszlelese
- **Szint:** `critical`
- **Kritikusság:** 🔴
- **Hamis pozitívok:** Nincs megadva

---
### vssadmin.exe shadow copy-t torol
- **Azonosító:** `T1490`
- **Leírás:** vssadmin.exe shadow copy-t torol
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** legitem admin fejlesztesek, backup tool

---
### webszerverre torteno webshellfeltoltese/ interakcioba lepese
- **Azonosító:** `T1505_003`
- **Leírás:** Detektalni a potenciális webshell feltolteseket es az interakciokat
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** Nincs megadva

---
### egy nem admin felhasznalo rovid idon belul tobb kulonbozo, erzekeny windows szolgaltatsat proball leallitani vagy modositani
- **Azonosító:** `T1543`
- **Leírás:** windows szolgaltatas leallitas vagy modositas
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** legitim admin tevekenyseg, szoftver telepites

---
### wmic.exe segitsegevel perzisztens esemenyt hoznak letre a tamadok
- **Azonosító:** `T1546_003`
- **Leírás:** wmic.exe segitsegevel perzisztens esemenyt hoznak letre
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** enterprise monitoring agent

---
### COM hijacking (perzisztencia)
- **Azonosító:** `T1546_015`
- **Leírás:** COM hijacking (perzisztencia)
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** alkalmazas update

---
### Gyanus Registry key modositas perzisztencia kiepitese erdekeben
- **Azonosító:** `T1547_001`
- **Leírás:** Detektalni a gyanus Registry key modositasokat
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** Legitim software run inditasa, Software telepites vagy update

---
### UAC bypass Fodhelper segitsegevel
- **Azonosító:** `T1548_002`
- **Leírás:** UAC bypass Fodhelper segitsegevel
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** nincs

---
### Detektalni, amikor nem a bongeszo folyamata fer hozza a bongeszo credential storejahoz
- **Azonosító:** `T1555`
- **Leírás:** None
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** Nincs megadva

---
### Szokatlan mennyisegu szolgaltatas jegy kerese
- **Azonosító:** `T1558_003`
- **Leírás:** szokatlan mennyisegu szolgaltatas jegy kerese
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** Nincs megadva

---
### High Fidelity Suspicious Named Pipe Activity
- **Azonosító:** `T1559_001`
- **Leírás:** High fidelity detection of suspicious named pipe creation or connection with minimal false positives, focusing on non-Microsoft signed binaries and abnormal pipe names.
- **Szint:** `high`
- **Kritikusság:** 🟠
- **Hamis pozitívok:** Custom in-house software using random named pipes, Rare unsigned legacy applications

---
### Adatgyujtes es exfiltration elokeszitese Archiving segitsegevel
- **Azonosító:** `T1560`
- **Leírás:** Adatgyujtes es exfiltration elokeszitese Archiving segitsegevel
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** pentesteles a kornyezetben

---
### Security tool leallitasa
- **Azonosító:** `T1562`
- **Leírás:** Security tool leallitasa
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** admin allitja le fejlesztes celjabol, pentesteles

---
### Detektalni, amikor egy tamado megprobalja kikapcsolni a Windows funkcioit powershellbol
- **Azonosító:** `T1562_001`
- **Leírás:** Egy tamado megprobalja kikapcsolni a Windows funkcioit poweshellbol
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** admin scriptet futtat, IT security update

---
### netsh.exe segitsegevel tuzfal szabalyt adnak hozza vagy modositanak
- **Azonosító:** `T1562_004`
- **Leírás:** netsh.exe segitsegevel tuzfal szabalyt adnak hozza vagy modositanak
- **Szint:** `medium`
- **Kritikusság:** 🟡
- **Hamis pozitívok:** admin hasznalja, pentesteles

---
