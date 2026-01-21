# 🛡️ Detection Rule Knowledge Base

### Suspicious Access to LSASS Process
- **Azonosító:** `T1003_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detektalni a process dumpingot LSASS memoriaban
- **Hamis pozitívok:** Antivirus or EDR solutions, System administrators hsznal debugging tool-t
- **MITRE ATT&CK:** `001, T1003`

---

### Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastol tavol levo hostra jelentkezik be
- **Azonosító:** `T1021.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastpl tavol levo hostra jelentkezik be
- **Hamis pozitívok:** VPN bejelentkezés, jump host, admin script
- **MITRE ATT&CK:** `T1021`

---

### Gyanus RDP belepes
- **Azonosító:** `T1021_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Gyanus RDP belepes
- **Hamis pozitívok:** Admin script, teszteles
- **MITRE ATT&CK:** `001`

---

### Detektalni a poweshellbol base64-encoded parancsot
- **Azonosító:** `T1027.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detektalni a powershellbol a base64-encoded parancsot
- **Hamis pozitívok:** admin scriptet futtat, pentesteles
- **MITRE ATT&CK:** `T1027, T1105`

---

### A tamado lemasol egy legitim Windows binarist
- **Azonosító:** `T1036_005.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** A tamado lemasol egy legitim Windows binarist
- **Hamis pozitívok:** legitim file, teszteles
- **MITRE ATT&CK:** `005, T1036`

---

### Tavoli hoston inditott folyamat wmic.exe segitsegevel
- **Azonosító:** `T1047.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Tavoli hoston inditott folyamat wmic.exe segitsegevel
- **Hamis pozitívok:** admin scriptek, management tooling
- **MITRE ATT&CK:** `T1047`

---

### Gyanus Scheduled Task letrehozasa
- **Azonosító:** `T1053_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Gyanus Scheduled Task letrehozasa
- **Hamis pozitívok:** admin automatizacio, backup
- **MITRE ATT&CK:** `005`

---

### Suspicious Credential API Hooking via Win32 APIs
- **Azonosító:** `T1056_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious processes loading Win32 libraries commonly abused for credential API hooking such as keylogging or credential interception.
- **Hamis pozitívok:** Accessibility software, Screen recording or input method tools, Legitimate security software
- **MITRE ATT&CK:** `004`

---

### Gyanus Poweshell parancs vegrehajtasa
- **Azonosító:** `T1059_001.yaml`
- **Minőségi mutató:** `50/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Poweshell parancsok eszlelese, melyek hasznalhatoak rosszindulatu kodok futtatasara
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001, T1027`

---

### Gyanus System process melyet a user indit
- **Azonosító:** `T1068.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Gyanus System process melyet a user indit
- **Hamis pozitívok:** fejlesztesek miatti alert, update/telepites
- **MITRE ATT&CK:** `T1068`

---

### wevtutil.exe security logokat torol
- **Azonosító:** `T1070_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** wevtutil.exe security logokat torol
- **Hamis pozitívok:** admin legitim script, pentesteles
- **MITRE ATT&CK:** `001`

---

### cmd.exe netuser vagy net localgroup parancsot futtat
- **Azonosító:** `T1087.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** cmd.exe netuser vagy net localgroup parancsot futtat
- **Hamis pozitívok:** admin futtat, pentesteles
- **MITRE ATT&CK:** `T1087, T1098`

---

### egy felhasznalo beepitett windows eszkozoket hasznal fajl letoltesre es kodfuttatasra
- **Azonosító:** `T1105.yaml`
- **Minőségi mutató:** `50/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** rosszindulatu fajl letoltese / kod futtatasa
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1105, T1218`

---

### tobbszori sikertelen bejelentkezes egy felhasznalohoz
- **Azonosító:** `T1110_001.yaml`
- **Minőségi mutató:** `50/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Egy adott ido alatt tortent sok sikertelen bejelentkezes egy felhasznalotol
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

---

### webszeren tortent XSS probakozas
- **Azonosító:** `T1190.yaml`
- **Minőségi mutató:** `40/100` ⭐⭐ (Fejlesztendő)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** None
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1190`

---

### bitsadmin.exe segitsegevel fajl letoltes
- **Azonosító:** `T1197.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** bitsadmin.exe segitsegevel fajl letoltese
- **Hamis pozitívok:** update, regebbi admin script
- **MITRE ATT&CK:** `T1197`

---

### Gyanus folyamatot inditott a Microsoft office valamelyik alkalmazasa
- **Azonosító:** `T1204.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Eszlelni a Microsoft Office altal letrehozott chilprocesseket
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1204, T1059`

---

### Gyanus mshta.exe URL-rol futtat scriptet
- **Azonosító:** `T1218_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Gyanus mshta.exe URL-rol futtat scriptet
- **Hamis pozitívok:** admin script futtatasa, pentesteles
- **MITRE ATT&CK:** `005`

---

### msiexec.exe URL-rol telepit csomagot
- **Azonosító:** `T1218_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** misexec.exe URL-rol telepit csomagot
- **Hamis pozitívok:** admin frissít, pentesteles
- **MITRE ATT&CK:** `007`

---

### Gyanus regsvr32.exe futtatasa
- **Azonosító:** `T1218_010.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Gyanus regsvr32.exe futtatasa
- **Hamis pozitívok:** regi alkalmazasok, frissites
- **MITRE ATT&CK:** `010`

---

### Gyanus rundll32.exe hasznalata
- **Azonosító:** `T1218_011.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Gyanus rundll32.exe hasznalata
- **Hamis pozitívok:** legit alkalmazasok, driver telepito
- **MITRE ATT&CK:** `011`

---

### Detektalni, amikor egy legitim remote admin toolt nem a megszokott enterprise modon hasznalnak
- **Azonosító:** `T1219.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detektalni, amikor egy ligitim remote admin toolt nem a megszokott enterprise modon hasznalnak
- **Hamis pozitívok:** pentest gyakorlat, admin fejlesztés
- **MITRE ATT&CK:** `T1219`

---

### Ransomware elokeszites eszlelese
- **Azonosító:** `T1486.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Ransomware elokeszites eszlelese
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1486, T1490, 001`

---

### vssadmin.exe shadow copy-t torol
- **Azonosító:** `T1490.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** vssadmin.exe shadow copy-t torol
- **Hamis pozitívok:** legitem admin fejlesztesek, backup tool
- **MITRE ATT&CK:** `T1490`

---

### webszerverre torteno webshellfeltoltese/ interakcioba lepese
- **Azonosító:** `T1505_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detektalni a potenciális webshell feltolteseket es az interakciokat
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003, T1059`

---

### egy nem admin felhasznalo rovid idon belul tobb kulonbozo, erzekeny windows szolgaltatsat proball leallitani vagy modositani
- **Azonosító:** `T1543.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** windows szolgaltatas leallitas vagy modositas
- **Hamis pozitívok:** legitim admin tevekenyseg, szoftver telepites
- **MITRE ATT&CK:** `T1543, T1562`

---

### wmic.exe segitsegevel perzisztens esemenyt hoznak letre a tamadok
- **Azonosító:** `T1546_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** wmic.exe segitsegevel perzisztens esemenyt hoznak letre
- **Hamis pozitívok:** enterprise monitoring agent
- **MITRE ATT&CK:** `003, T1546`

---

### COM hijacking (perzisztencia)
- **Azonosító:** `T1546_015.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** COM hijacking (perzisztencia)
- **Hamis pozitívok:** alkalmazas update
- **MITRE ATT&CK:** `015, T1546`

---

### Gyanus Registry key modositas perzisztencia kiepitese erdekeben
- **Azonosító:** `T1547_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detektalni a gyanus Registry key modositasokat
- **Hamis pozitívok:** Legitim software run inditasa, Software telepites vagy update
- **MITRE ATT&CK:** `001`

---

### UAC bypass Fodhelper segitsegevel
- **Azonosító:** `T1548_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** UAC bypass Fodhelper segitsegevel
- **Hamis pozitívok:** nincs
- **MITRE ATT&CK:** `002`

---

### Detektalni, amikor nem a bongeszo folyamata fer hozza a bongeszo credential storejahoz
- **Azonosító:** `T1555.yaml`
- **Minőségi mutató:** `40/100` ⭐⭐ (Fejlesztendő)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** None
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1555`

---

### Szokatlan mennyisegu szolgaltatas jegy kerese
- **Azonosító:** `T1558_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** szokatlan mennyisegu szolgaltatas jegy kerese
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

---

### High Fidelity Suspicious Named Pipe Activity
- **Azonosító:** `T1559_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** High fidelity detection of suspicious named pipe creation or connection with minimal false positives, focusing on non-Microsoft signed binaries and abnormal pipe names.
- **Hamis pozitívok:** Custom in-house software using random named pipes, Rare unsigned legacy applications
- **MITRE ATT&CK:** `001`

---

### Adatgyujtes es exfiltration elokeszitese Archiving segitsegevel
- **Azonosító:** `T1560.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Adatgyujtes es exfiltration elokeszitese Archiving segitsegevel
- **Hamis pozitívok:** pentesteles a kornyezetben
- **MITRE ATT&CK:** `T1560`

---

### Security tool leallitasa
- **Azonosító:** `T1562.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Security tool leallitasa
- **Hamis pozitívok:** admin allitja le fejlesztes celjabol, pentesteles
- **MITRE ATT&CK:** `T1562, 001`

---

### Detektalni, amikor egy tamado megprobalja kikapcsolni a Windows funkcioit powershellbol
- **Azonosító:** `T1562_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Egy tamado megprobalja kikapcsolni a Windows funkcioit poweshellbol
- **Hamis pozitívok:** admin scriptet futtat, IT security update
- **MITRE ATT&CK:** `001`

---

### netsh.exe segitsegevel tuzfal szabalyt adnak hozza vagy modositanak
- **Azonosító:** `T1562_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** netsh.exe segitsegevel tuzfal szabalyt adnak hozza vagy modositanak
- **Hamis pozitívok:** admin hasznalja, pentesteles
- **MITRE ATT&CK:** `004`

---

### Credential Dumping LSASS
- **Azonosító:** `credential_dumping_lsass.yml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** a hitelesito adatok LSASS folyamatmemoriabol torteno kiirasara tett kiserlet
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1003, 001`

---

