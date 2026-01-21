# 🛡️ Detection Rule Knowledge Base

## 📖 Tartalomjegyzék
- [Suspicious Access to LSASS Process Memory](#suspicious-access-to-lsass-process-memory)
- [Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastol tavol levo hostra jelentkezik be](#detektalni-ugyanazon-felhasznalotol-rovid-idon-belul,-tobb-egymastol-tavol-levo-hostra-jelentkezik-be)
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
- [egy felhasznalo beepitett windows eszkozoket hasznal fajl letoltesre es kodfuttatasra](#egy-felhasznalo-beepitett-windows-eszkozoket-hasznal-fajl-letoltesre-es-kodfuttatasra)
- [tobbszori sikertelen bejelentkezes egy felhasznalohoz](#tobbszori-sikertelen-bejelentkezes-egy-felhasznalohoz)
- [webszeren tortent XSS probakozas](#webszeren-tortent-xss-probakozas)
- [bitsadmin.exe segitsegevel fajl letoltes](#bitsadminexe-segitsegevel-fajl-letoltes)
- [Gyanus folyamatot inditott a Microsoft office valamelyik alkalmazasa](#gyanus-folyamatot-inditott-a-microsoft-office-valamelyik-alkalmazasa)
- [Gyanus mshta.exe URL-rol futtat scriptet](#gyanus-mshtaexe-url-rol-futtat-scriptet)
- [msiexec.exe URL-rol telepit csomagot](#msiexecexe-url-rol-telepit-csomagot)
- [Gyanus regsvr32.exe futtatasa](#gyanus-regsvr32exe-futtatasa)
- [Gyanus rundll32.exe hasznalata](#gyanus-rundll32exe-hasznalata)
- [Detektalni, amikor egy legitim remote admin toolt nem a megszokott enterprise modon hasznalnak](#detektalni,-amikor-egy-legitim-remote-admin-toolt-nem-a-megszokott-enterprise-modon-hasznalnak)
- [Ransomware elokeszites eszlelese](#ransomware-elokeszites-eszlelese)
- [vssadmin.exe shadow copy-t torol](#vssadminexe-shadow-copy-t-torol)
- [webszerverre torteno webshellfeltoltese/ interakcioba lepese](#webszerverre-torteno-webshellfeltoltese-interakcioba-lepese)
- [egy nem admin felhasznalo rovid idon belul tobb kulonbozo, erzekeny windows szolgaltatsat proball leallitani vagy modositani](#egy-nem-admin-felhasznalo-rovid-idon-belul-tobb-kulonbozo,-erzekeny-windows-szolgaltatsat-proball-leallitani-vagy-modositani)
- [wmic.exe segitsegevel perzisztens esemenyt hoznak letre a tamadok](#wmicexe-segitsegevel-perzisztens-esemenyt-hoznak-letre-a-tamadok)
- [COM hijacking (perzisztencia)](#com-hijacking-(perzisztencia))
- [Gyanus Registry key modositas perzisztencia kiepitese erdekeben](#gyanus-registry-key-modositas-perzisztencia-kiepitese-erdekeben)
- [UAC bypass Fodhelper segitsegevel](#uac-bypass-fodhelper-segitsegevel)
- [Detektalni, amikor nem a bongeszo folyamata fer hozza a bongeszo credential storejahoz](#detektalni,-amikor-nem-a-bongeszo-folyamata-fer-hozza-a-bongeszo-credential-storejahoz)
- [Szokatlan mennyisegu szolgaltatas jegy kerese](#szokatlan-mennyisegu-szolgaltatas-jegy-kerese)
- [High Fidelity Suspicious Named Pipe Activity](#high-fidelity-suspicious-named-pipe-activity)
- [Adatgyujtes es exfiltration elokeszitese Archiving segitsegevel](#adatgyujtes-es-exfiltration-elokeszitese-archiving-segitsegevel)
- [Security tool leallitasa](#security-tool-leallitasa)
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
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

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
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

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
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

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
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

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
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

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

## egy felhasznalo beepitett windows eszkozoket hasznal fajl letoltesre es kodfuttatasra
- **Azonosító:** `T1105.yaml`
- **Minőségi mutató:** `50/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** rosszindulatu fajl letoltese / kod futtatasa
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1105, T1218`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## tobbszori sikertelen bejelentkezes egy felhasznalohoz
- **Azonosító:** `T1110_001.yaml`
- **Minőségi mutató:** `50/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Egy adott ido alatt tortent sok sikertelen bejelentkezes egy felhasznalotol
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## webszeren tortent XSS probakozas
- **Azonosító:** `T1190.yaml`
- **Minőségi mutató:** `40/100` ⭐⭐ (Fejlesztendő)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** None
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1190`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## bitsadmin.exe segitsegevel fajl letoltes
- **Azonosító:** `T1197.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** bitsadmin.exe segitsegevel fajl letoltese
- **Hamis pozitívok:** update, regebbi admin script
- **MITRE ATT&CK:** `T1197`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## Gyanus folyamatot inditott a Microsoft office valamelyik alkalmazasa
- **Azonosító:** `T1204.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Eszlelni a Microsoft Office altal letrehozott chilprocesseket
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1204, T1059`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## Gyanus mshta.exe URL-rol futtat scriptet
- **Azonosító:** `T1218_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Gyanus mshta.exe URL-rol futtat scriptet
- **Hamis pozitívok:** admin script futtatasa, pentesteles
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## msiexec.exe URL-rol telepit csomagot
- **Azonosító:** `T1218_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** misexec.exe URL-rol telepit csomagot
- **Hamis pozitívok:** admin frissít, pentesteles
- **MITRE ATT&CK:** `007`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## Gyanus regsvr32.exe futtatasa
- **Azonosító:** `T1218_010.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Gyanus regsvr32.exe futtatasa
- **Hamis pozitívok:** regi alkalmazasok, frissites
- **MITRE ATT&CK:** `010`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## Gyanus rundll32.exe hasznalata
- **Azonosító:** `T1218_011.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Gyanus rundll32.exe hasznalata
- **Hamis pozitívok:** legit alkalmazasok, driver telepito
- **MITRE ATT&CK:** `011`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## Detektalni, amikor egy legitim remote admin toolt nem a megszokott enterprise modon hasznalnak
- **Azonosító:** `T1219.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detektalni, amikor egy ligitim remote admin toolt nem a megszokott enterprise modon hasznalnak
- **Hamis pozitívok:** pentest gyakorlat, admin fejlesztés
- **MITRE ATT&CK:** `T1219`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## Ransomware elokeszites eszlelese
- **Azonosító:** `T1486.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Ransomware elokeszites eszlelese
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1486, T1490, 001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## vssadmin.exe shadow copy-t torol
- **Azonosító:** `T1490.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** vssadmin.exe shadow copy-t torol
- **Hamis pozitívok:** legitem admin fejlesztesek, backup tool
- **MITRE ATT&CK:** `T1490`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## webszerverre torteno webshellfeltoltese/ interakcioba lepese
- **Azonosító:** `T1505_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detektalni a potenciális webshell feltolteseket es az interakciokat
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003, T1059`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## egy nem admin felhasznalo rovid idon belul tobb kulonbozo, erzekeny windows szolgaltatsat proball leallitani vagy modositani
- **Azonosító:** `T1543.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** windows szolgaltatas leallitas vagy modositas
- **Hamis pozitívok:** legitim admin tevekenyseg, szoftver telepites
- **MITRE ATT&CK:** `T1543, T1562`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## wmic.exe segitsegevel perzisztens esemenyt hoznak letre a tamadok
- **Azonosító:** `T1546_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** wmic.exe segitsegevel perzisztens esemenyt hoznak letre
- **Hamis pozitívok:** enterprise monitoring agent
- **MITRE ATT&CK:** `003, T1546`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## COM hijacking (perzisztencia)
- **Azonosító:** `T1546_015.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** COM hijacking (perzisztencia)
- **Hamis pozitívok:** alkalmazas update
- **MITRE ATT&CK:** `015, T1546`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## Gyanus Registry key modositas perzisztencia kiepitese erdekeben
- **Azonosító:** `T1547_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detektalni a gyanus Registry key modositasokat
- **Hamis pozitívok:** Legitim software run inditasa, Software telepites vagy update
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## UAC bypass Fodhelper segitsegevel
- **Azonosító:** `T1548_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** UAC bypass Fodhelper segitsegevel
- **Hamis pozitívok:** nincs
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## Detektalni, amikor nem a bongeszo folyamata fer hozza a bongeszo credential storejahoz
- **Azonosító:** `T1555.yaml`
- **Minőségi mutató:** `40/100` ⭐⭐ (Fejlesztendő)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** None
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1555`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.

---

## Szokatlan mennyisegu szolgaltatas jegy kerese
- **Azonosító:** `T1558_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** szokatlan mennyisegu szolgaltatas jegy kerese
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## High Fidelity Suspicious Named Pipe Activity
- **Azonosító:** `T1559_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** High fidelity detection of suspicious named pipe creation or connection with minimal false positives, focusing on non-Microsoft signed binaries and abnormal pipe names.
- **Hamis pozitívok:** Custom in-house software using random named pipes, Rare unsigned legacy applications
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

## Adatgyujtes es exfiltration elokeszitese Archiving segitsegevel
- **Azonosító:** `T1560.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Adatgyujtes es exfiltration elokeszitese Archiving segitsegevel
- **Hamis pozitívok:** pentesteles a kornyezetben
- **MITRE ATT&CK:** `T1560`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## Security tool leallitasa
- **Azonosító:** `T1562.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Security tool leallitasa
- **Hamis pozitívok:** admin allitja le fejlesztes celjabol, pentesteles
- **MITRE ATT&CK:** `T1562, 001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

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
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

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
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

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
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld a hostot a hálózatról!

---

