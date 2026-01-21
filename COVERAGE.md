# 📘 Részletes MITRE ATT&CK Lefedettség

**Utolsó frissítés:** `2026-01-21 06:18:22`

## 📈 SIEM Platform Lefedettség

| Platform | Konvertált szabályok | Lefedettség |
| :--- | :---: | :---: |
| Sigma (Forrás) | 37 | 100% |
| Splunk (SPL) | 37 | 100.0% |
| QRadar (AQL) | 35 | 94.6% |
| RSA NetWitness | 37 | 100.0% |

## 🎯 Technika alapú bontás
| Technika ID | Szint | Kapcsolódó szabályok |
| :--- | :--- | :--- |
| T1003 | HIGH | Suspicious Access to LSASS Process |
| T1003.001 | HIGH | Suspicious Access to LSASS Process |
| T1021 | MEDIUM | Detektalni ugyanazon felhasznalotol rovid idon belul, tobb egymastol tavol levo hostra jelentkezik be |
| T1021.001 | MEDIUM | Gyanus RDP belepes |
| T1027 | HIGH | Detektalni a poweshellbol base64-encoded parancsot, Gyanus Poweshell parancs vegrehajtasa |
| T1036 | HIGH | A tamado lemasol egy legitim Windows binarist |
| T1036.005 | HIGH | A tamado lemasol egy legitim Windows binarist |
| T1047 | MEDIUM | Tavoli hoston inditott folyamat wmic.exe segitsegevel |
| T1053.005 | MEDIUM | Gyanus Scheduled Task letrehozasa |
| T1056.004 | HIGH | Suspicious Credential API Hooking via Win32 APIs |
| T1059 | HIGH | Gyanus folyamatot inditott a Microsoft office valamelyik alkalmazasa, webszerverre torteno webshellfeltoltese/ interakcioba lepese |
| T1059.001 | MEDIUM | Gyanus Poweshell parancs vegrehajtasa |
| T1068 | MEDIUM | Gyanus System process melyet a user indit |
| T1070.001 | MEDIUM | wevtutil.exe security logokat torol |
| T1087 | MEDIUM | cmd.exe netuser vagy net localgroup parancsot futtat |
| T1098 | MEDIUM | cmd.exe netuser vagy net localgroup parancsot futtat |
| T1105 | HIGH | Detektalni a poweshellbol base64-encoded parancsot, egy felhasznalo beepitett windows eszkozoket hasznal fajl letoltesre es kodfuttatasra |
| T1110.001 | MEDIUM | tobbszori sikertelen bejelentkezes egy felhasznalohoz |
| T1190 | MEDIUM | webszeren tortent XSS probakozas |
| T1197 | HIGH | bitsadmin.exe segitsegevel fajl letoltes |
| T1204 | HIGH | Gyanus folyamatot inditott a Microsoft office valamelyik alkalmazasa |
| T1218 | MEDIUM | egy felhasznalo beepitett windows eszkozoket hasznal fajl letoltesre es kodfuttatasra |
| T1218.005 | MEDIUM | Gyanus mshta.exe URL-rol futtat scriptet |
| T1218.007 | MEDIUM | msiexec.exe URL-rol telepit csomagot |
| T1218.010 | MEDIUM | Gyanus regsvr32.exe futtatasa |
| T1218.011 | HIGH | Gyanus rundll32.exe hasznalata |
| T1219 | HIGH | Detektalni, amikor egy legitim remote admin toolt nem a megszokott enterprise modon hasznalnak |
| T1486 | CRITICAL | Ransomware elokeszites eszlelese |
| T1490 | CRITICAL | vssadmin.exe shadow copy-t torol, Ransomware elokeszites eszlelese |
| T1505.003 | HIGH | webszerverre torteno webshellfeltoltese/ interakcioba lepese |
| T1543 | MEDIUM | egy nem admin felhasznalo rovid idon belul tobb kulonbozo, erzekeny windows szolgaltatsat proball leallitani vagy modositani |
| T1546 | HIGH | wmic.exe segitsegevel perzisztens esemenyt hoznak letre a tamadok, COM hijacking (perzisztencia) |
| T1546.003 | HIGH | wmic.exe segitsegevel perzisztens esemenyt hoznak letre a tamadok |
| T1546.015 | HIGH | COM hijacking (perzisztencia) |
| T1547.001 | HIGH | Gyanus Registry key modositas perzisztencia kiepitese erdekeben |
| T1548.002 | HIGH | UAC bypass Fodhelper segitsegevel |
| T1555 | MEDIUM | Detektalni, amikor nem a bongeszo folyamata fer hozza a bongeszo credential storejahoz |
| T1558.003 | HIGH | Szokatlan mennyisegu szolgaltatas jegy kerese |
| T1559.001 | HIGH | High Fidelity Suspicious Named Pipe Activity |
| T1560 | MEDIUM | Adatgyujtes es exfiltration elokeszitese Archiving segitsegevel |
| T1562 | MEDIUM | egy nem admin felhasznalo rovid idon belul tobb kulonbozo, erzekeny windows szolgaltatsat proball leallitani vagy modositani, Security tool leallitasa |
| T1562.001 | CRITICAL | Ransomware elokeszites eszlelese, Detektalni, amikor egy tamado megprobalja kikapcsolni a Windows funkcioit powershellbol, Security tool leallitasa |
| T1562.004 | MEDIUM | netsh.exe segitsegevel tuzfal szabalyt adnak hozza vagy modositanak |
