# 🛡️ Észlelési szabály tudásbázis

### 📊 Detection Engineering Dashboard
| Kritikusság | Darabszám |
| :--- | :--- |
| 🔴 Critical | 361 |
| 🟠 High | 260 |
| 🟡 Medium | 7 |
| 🔵 Low | 0 |
| **Összesen** | **628** |

---
## 📖 Tartalomjegyzék
- [Ultra-Pro High-Fidelity szteganográfia és adatrekonstrukció (T1001)](#ultra-pro-high-fidelity-szteganográfia-és-adatrekonstrukció-(t1001))
- [Ultra-Pro High-Fidelity levélszemét adat és parancstömítés (T1001.001)](#ultra-pro-high-fidelity-levélszemét-adat-és-parancstömítés-(t1001001))
- [Ultra-Pro High-Fidelity szteganográfia és adatrekonstrukció (T1001.002)](#ultra-pro-high-fidelity-szteganográfia-és-adatrekonstrukció-(t1001002))
- [Ultra-Pro High-Fidelity Protocol megszemélyesítés (T1001.003)](#ultra-pro-high-fidelity-protocol-megszemélyesítés-(t1001003))
- [Ultra-Pro High-Fidelity LSASS hitelesítő adatok dömping (T1003)](#ultra-pro-high-fidelity-lsass-hitelesítő-adatok-dömping-(t1003))
- [Gyanús hozzáférés az LSASS folyamatmemóriához](#gyanús-hozzáférés-az-lsass-folyamatmemóriához)
- [Ultra-Pro High-Fidelity SAM & SYSTEM Registry Theft (T1003.002)](#ultra-pro-high-fidelity-sam-&-system-registry-theft-(t1003002))
- [Ultra-Pro High-Fidelity NTDS.dit kivonás (T1003.003)](#ultra-pro-high-fidelity-ntdsdit-kivonás-(t1003003))
- [Ultra-Pro High-Fidelity LSA titkok és biztonsági kaptárlopás (T1003.004)](#ultra-pro-high-fidelity-lsa-titkok-és-biztonsági-kaptárlopás-(t1003004))
- [Ultra-Pro High-Fidelity MSCASH/DCC extrakció (T1003.005)](#ultra-pro-high-fidelity-mscashdcc-extrakció-(t1003005))
- [Ultra-Pro High-Fidelity DCSync támadásészlelés (T1003.006)](#ultra-pro-high-fidelity-dcsync-támadásészlelés-(t1003006))
- [Ultra-Pro High-Fidelity LSASS memória kiíratása és LOLBin visszaélés (T1003.007)](#ultra-pro-high-fidelity-lsass-memória-kiíratása-és-lolbin-visszaélés-(t1003007))
- [Ultra-Pro High-Fidelity Linux Shadow File Extraction (T1003.008)](#ultra-pro-high-fidelity-linux-shadow-file-extraction-(t1003008))
- [Ultra-Pro, nagy pontosságú helyi adatgyűjtés (T1005)](#ultra-pro-nagy-pontosságú-helyi-adatgyűjtés-(t1005))
- [Ultra-Pro lopakodó közvetlen hangerő-hozzáférés (T1006)](#ultra-pro-lopakodó-közvetlen-hangerő-hozzáférés-(t1006))
- [Ultra-Pro High-Fidelity System Service Discovery (T1007)](#ultra-pro-high-fidelity-system-service-discovery-(t1007))
- [Ultra-Pro High-Fidelity tartalék csatornaérzékelés (T1008)](#ultra-pro-high-fidelity-tartalék-csatornaérzékelés-(t1008))
- [Ultra-Pro High-Fidelity Application Window Discovery (T1010)](#ultra-pro-high-fidelity-application-window-discovery-(t1010))
- [Ultra-Pro High-Fidelity Bluetooth Exfiltration (T1011)](#ultra-pro-high-fidelity-bluetooth-exfiltration-(t1011))
- [Ultra-Pro High-Fidelity BLE Advertising Exfiltration (T1011.001)](#ultra-pro-high-fidelity-ble-advertising-exfiltration-(t1011001))
- [Ultra-Pro High-Fidelity Query Registry Discovery (T1012)](#ultra-pro-high-fidelity-query-registry-discovery-(t1012))
- [Ultra-Pro High-Fidelity BYOVD Rootkit betöltése (T1014)](#ultra-pro-high-fidelity-byovd-rootkit-betöltése-(t1014))
- [Ultra-Pro High-Fidelity rendszer hálózati konfigurációjának felfedezése (T1016)](#ultra-pro-high-fidelity-rendszer-hálózati-konfigurációjának-felfedezése-(t1016))
- [Ultra-Pro High-Fidelity Internet IP Discovery (T1016.001)](#ultra-pro-high-fidelity-internet-ip-discovery-(t1016001))
- [Ultra-Pro High-Fidelity terminálszolgáltatások konfigurációs felderítése (T1016.002)](#ultra-pro-high-fidelity-terminálszolgáltatások-konfigurációs-felderítése-(t1016002))
- [Ultra-Pro High-Fidelity Remote System Discovery (T1018)](#ultra-pro-high-fidelity-remote-system-discovery-(t1018))
- [Ultra-Pro High-Fidelity automatizált szűrés (T1020)](#ultra-pro-high-fidelity-automatizált-szűrés-(t1020))
- [Client-Linked Cloud Exfil (T1020.001)](#client-linked-cloud-exfil-(t1020001))
- [Gyors bejelentkezés több távoli gépre ugyanazon felhasználó által](#gyors-bejelentkezés-több-távoli-gépre-ugyanazon-felhasználó-által)
- [Gyanús RDP bejelentkezés szokatlan forrásból](#gyanús-rdp-bejelentkezés-szokatlan-forrásból)
- [SMB Admin Share Mapping (T1021.002)](#smb-admin-share-mapping-(t1021002))
- [DCOM távoli végrehajtás (T1021.003)](#dcom-távoli-végrehajtás-(t1021003))
- [SSH Lateral Movement & Tunneling (T1021.004)](#ssh-lateral-movement-&-tunneling-(t1021004))
- [VNC oldalirányú mozgás és eltérítés (T1021.005)](#vnc-oldalirányú-mozgás-és-eltérítés-(t1021005))
- [WinRM távoli végrehajtás (T1021.006)](#winrm-távoli-végrehajtás-(t1021006))
- [Felhővezérlő sík eltérítése (T1021.007)](#felhővezérlő-sík-eltérítése-(t1021007))
- [macOS ARD távoli eltérítés (T1021.008)](#macos-ard-távoli-eltérítés-(t1021008))
- [Cserélhető adathordozó adatlopás (T1025)](#cserélhető-adathordozó-adatlopás-(t1025))
- [Gyanús Base64 kódolású PowerShell-parancs hálózati tevékenységgel](#gyanús-base64-kódolású-powershell-parancs-hálózati-tevékenységgel)
- [Bináris kitöltési tevékenység (T1027.001)](#bináris-kitöltési-tevékenység-(t1027001))
- [Szoftvercsomagolási esemény (T1027.002)](#szoftvercsomagolási-esemény-(t1027002))
- [Szteganográfia hasznos teher kivonás (T1027.003)](#szteganográfia-hasznos-teher-kivonás-(t1027003))
- [Szteganográfia hasznos teher kivonás (T1027.004)](#szteganográfia-hasznos-teher-kivonás-(t1027004))
- [Jelző eltávolítása és aláíráslopás (T1027.005)](#jelző-eltávolítása-és-aláíráslopás-(t1027005))
- [HTML-csempészet végrehajtása (T1027.006)](#html-csempészet-végrehajtása-(t1027006))
- [Bináris szimbólumok eltávolítása (T1027.007)](#bináris-szimbólumok-eltávolítása-(t1027007))
- [Bináris szimbólumok eltávolítása (T1027.008)](#bináris-szimbólumok-eltávolítása-(t1027008))
- [Beágyazott hasznos teher kivonás (T1027.009)](#beágyazott-hasznos-teher-kivonás-(t1027009))
- [Parancssori zavarás (T1027.010)](#parancssori-zavarás-(t1027010))
- [Gyanús archívum létrehozása (T1027.011)](#gyanús-archívum-létrehozása-(t1027011))
- [Windows LDR-eltérítés (T1027.012)](#windows-ldr-eltérítés-(t1027012))
- [Ütemezett transzfer (T1029)](#ütemezett-transzfer-(t1029))
- [Adatok darabolása és töredezettsége (T1030)](#adatok-darabolása-és-töredezettsége-(t1030))
- [Rendszertulajdonos/felhasználó felfedezése (T1033)](#rendszertulajdonosfelhasználó-felfedezése-(t1033))
- [Maszkolás és visszaélés a folyamat során (T1036)](#maszkolás-és-visszaélés-a-folyamat-során-(t1036))
- [Érvénytelen vagy hamisított kódaláírás (T1036.001)](#érvénytelen-vagy-hamisított-kódaláírás-(t1036001))
- [RTLO karaktervégrehajtás (T1036.002)](#rtlo-karaktervégrehajtás-(t1036002))
- [Átnevezett System Utility Detection (T1036.003)](#átnevezett-system-utility-detection-(t1036003))
- [Maszkírozás útvonal-anomálián keresztül (T1036.004)](#maszkírozás-útvonal-anomálián-keresztül-(t1036004))
- [Jogos Windows bináris fájl a felhasználó által írható helyre másolva](#jogos-windows-bináris-fájl-a-felhasználó-által-írható-helyre-másolva)
- [Szóköz a fájlnév maszkolása után (T1036.006)](#szóköz-a-fájlnév-maszkolása-után-(t1036006))
- [Dupla fájlkiterjesztés végrehajtása (T1036.007)](#dupla-fájlkiterjesztés-végrehajtása-(t1036007))
- [Masquerade via tolmács visszaélés (T1036.008)](#masquerade-via-tolmács-visszaélés-(t1036008))
- [Allure Document & RTLO Maszkírozás Detection](#allure-document-&-rtlo-maszkírozás-detection)
- [Nagy pontosságú bejelentkezési szkript fennmaradása (T1037)](#nagy-pontosságú-bejelentkezési-szkript-fennmaradása-(t1037))
- [High-Fidelity UserInitMprLogonScript perzisztencia](#high-fidelity-userinitmprlogonscript-perzisztencia)
- [High-Fidelity Netsh Helper DLL tartósság](#high-fidelity-netsh-helper-dll-tartósság)
- [Ultra-Pro hálózati bejelentkezési szkript/parancsikon módosítása (T1037.003)](#ultra-pro-hálózati-bejelentkezési-szkriptparancsikon-módosítása-(t1037003))
- [Ultra-Pro RC Script és Init.d Persistence (T1037.004)](#ultra-pro-rc-script-és-initd-persistence-(t1037004))
- [Ultra-Pro macOS indítási elemek tartóssága (T1037.005)](#ultra-pro-macos-indítási-elemek-tartóssága-(t1037005))
- [Hálózati megosztások felfedezése és gyűjtése (ATT&CK T1039)](#hálózati-megosztások-felfedezése-és-gyűjtése-(att&ck-t1039))
- [Hálózati szippantásérzékelés (ATT&CK T1040)](#hálózati-szippantásérzékelés-(att&ck-t1040))
- [Kiszűrés a C2 csatornán keresztül (ATT&CK T1041)](#kiszűrés-a-c2-csatornán-keresztül-(att&ck-t1041))
- [Hálózati szolgáltatáskeresés (ATT&CK T1046)](#hálózati-szolgáltatáskeresés-(att&ck-t1046))
- [Gyanús távoli folyamat létrehozása a WMIC-en keresztül](#gyanús-távoli-folyamat-létrehozása-a-wmic-en-keresztül)
- [Alternatív protokoll-szűrés (ATT&CK T1048)](#alternatív-protokoll-szűrés-(att&ck-t1048))
- [Szimmetrikus titkosított kiszűrés (ATT&CK T1048.001)](#szimmetrikus-titkosított-kiszűrés-(att&ck-t1048001))
- [Aszimmetrikus titkosított kiszűrés (ATT&CK T1048.002)](#aszimmetrikus-titkosított-kiszűrés-(att&ck-t1048002))
- [Titkosítatlan protokoll kiszűrése (ATT&CK T1048.003)](#titkosítatlan-protokoll-kiszűrése-(att&ck-t1048003))
- [Rendszerhálózati kapcsolatok felderítése (ATT&CK T1049)](#rendszerhálózati-kapcsolatok-felderítése-(att&ck-t1049))
- [Fizikai közeg kiszűrése (ATT&CK T1052)](#fizikai-közeg-kiszűrése-(att&ck-t1052))
- [USB kiszűrésérzékelés (ATT&CK T1052.001)](#usb-kiszűrésérzékelés-(att&ck-t1052001))
- [Gyanús ütemezett feladat vagy munkakör létrehozása a Persistence (T1053) miatt](#gyanús-ütemezett-feladat-vagy-munkakör-létrehozása-a-persistence-(t1053)-miatt)
- [High-Fidelity At.exe tevékenységészlelés](#high-fidelity-atexe-tevékenységészlelés)
- [High-Fidelity Cron perzisztencia és helyben történő módosítás](#high-fidelity-cron-perzisztencia-és-helyben-történő-módosítás)
- [Gyanús ütemezett feladat létrehozása PowerShell végrehajtása során](#gyanús-ütemezett-feladat-létrehozása-powershell-végrehajtása-során)
- [High-Fidelity Systemd szolgáltatás létrehozása vagy módosítása](#high-fidelity-systemd-szolgáltatás-létrehozása-vagy-módosítása)
- [High-Fidelity Systemd Timer Persistence Detection](#high-fidelity-systemd-timer-persistence-detection)
- [Befecskendezési folyamat észlelése (ATT&CK T1055)](#befecskendezési-folyamat-észlelése-(att&ck-t1055))
- [DLL befecskendezés észlelése (ATT&CK T1055.001)](#dll-befecskendezés-észlelése-(att&ck-t1055001))
- [PE befecskendezés észlelése (ATT&CK T1055.002)](#pe-befecskendezés-észlelése-(att&ck-t1055002))
- [Száleltérítés-észlelés (ATT&CK T1055.003)](#száleltérítés-észlelés-(att&ck-t1055003))
- [APC befecskendezés észlelése (ATT&CK T1055.004)](#apc-befecskendezés-észlelése-(att&ck-t1055004))
- [TLS befecskendezés észlelése (ATT&CK T1055.005)](#tls-befecskendezés-észlelése-(att&ck-t1055005))
- [Ptrace Injection Detection (ATT&CK T1055.008)](#ptrace-injection-detection-(att&ck-t1055008))
- [Lopakodó modul-felülírás (ATT&CK T1055.009)](#lopakodó-modul-felülírás-(att&ck-t1055009))
- [Lopakodó extra ablakmemória (EWM) befecskendezés (ATT&CK T1055.011)](#lopakodó-extra-ablakmemória-(ewm)-befecskendezés-(att&ck-t1055011))
- [Lopakodó eljárással történő kiürítés (ATT&CK T1055.012)](#lopakodó-eljárással-történő-kiürítés-(att&ck-t1055012))
- [Lopakodó eljárással történő kiürítés (ATT&CK T1055.013)](#lopakodó-eljárással-történő-kiürítés-(att&ck-t1055013))
- [Stealthy Process Ghosting (ATT&CK T1055.014)](#stealthy-process-ghosting-(att&ck-t1055014))
- [Stealthy List Planting Injection (ATT&CK T1055.015)](#stealthy-list-planting-injection-(att&ck-t1055015))
- [Bemeneti rögzítés észlelése (ATT&CK T1056)](#bemeneti-rögzítés-észlelése-(att&ck-t1056))
- [Keylogging & Input Hooking (ATT&CK T1056.001)](#keylogging-&-input-hooking-(att&ck-t1056001))
- [GUI bemenet rögzítése (ATT&CK T1056.002)](#gui-bemenet-rögzítése-(att&ck-t1056002))
- [Digitális tanúsítvány ellopása (ATT&CK T1056.003)](#digitális-tanúsítvány-ellopása-(att&ck-t1056003))
- [Gyanús hitelesítő adatok API-hozzákapcsolása a Win32 könyvtárakon keresztül](#gyanús-hitelesítő-adatok-api-hozzákapcsolása-a-win32-könyvtárakon-keresztül)
- [Folyamatfelderítés (ATT&CK T1057)](#folyamatfelderítés-(att&ck-t1057))
- [High-Fidelity Scripting Interpreter Contextual Anomália](#high-fidelity-scripting-interpreter-contextual-anomália)
- [Gyanús kódolt PowerShell-parancsvégrehajtás](#gyanús-kódolt-powershell-parancsvégrehajtás)
- [High-Fidelity AppleScript (osascript) visszaélés-észlelés](#high-fidelity-applescript-(osascript)-visszaélés-észlelés)
- [Speciális Windows Command Shell kontextuális anomália](#speciális-windows-command-shell-kontextuális-anomália)
- [High-Fidelity Unix shell visszaélés és fordított shell észlelés](#high-fidelity-unix-shell-visszaélés-és-fordított-shell-észlelés)
- [High-Fidelity VBScript kontextuális anomália észlelése](#high-fidelity-vbscript-kontextuális-anomália-észlelése)
- [High-Fidelity Python tolmács visszaélés észlelése](#high-fidelity-python-tolmács-visszaélés-észlelése)
- [High-Fidelity JScript Interpreter Contextual Anomália](#high-fidelity-jscript-interpreter-contextual-anomália)
- [High-Fidelity hálózati eszköz CLI-manipulációja](#high-fidelity-hálózati-eszköz-cli-manipulációja)
- [High-Fidelity Cloud Shell kihasználása és adatszivárgás](#high-fidelity-cloud-shell-kihasználása-és-adatszivárgás)
- [Gyanús RENDSZER folyamat a felhasználói kontextusból](#gyanús-rendszer-folyamat-a-felhasználói-kontextusból)
- [Engedélycsoportok felderítése (ATT&CK T1069)](#engedélycsoportok-felderítése-(att&ck-t1069))
- [Helyi csoportfelderítés (ATT&CK T1069.001)](#helyi-csoportfelderítés-(att&ck-t1069001))
- [Domaincsoport felfedezése (ATT&CK T1069.002)](#domaincsoport-felfedezése-(att&ck-t1069002))
- [Cloud Groups Discovery (ATT&CK T1069.003)](#cloud-groups-discovery-(att&ck-t1069003))
- [Jelző eltávolítása a gazdagépen (ATT&CK T1070)](#jelző-eltávolítása-a-gazdagépen-(att&ck-t1070))
- [A biztonsági eseménynapló törölve a wevtutil.exe használatával](#a-biztonsági-eseménynapló-törölve-a-wevtutilexe-használatával)
- [Linux naplótörlés és naplószabotázs (ATT&CK T1070.002)](#linux-naplótörlés-és-naplószabotázs-(att&ck-t1070002))
- [Postafiókadatok törlése és szabálymanipuláció (ATT&CK T1070.003)](#postafiókadatok-törlése-és-szabálymanipuláció-(att&ck-t1070003))
- [Törvényszéki műtermékek és fájltörlés (ATT&CK T1070.004)](#törvényszéki-műtermékek-és-fájltörlés-(att&ck-t1070004))
- [Hálózati megosztás és hitelesítő adatok tisztítása (ATT&CK T1070.005)](#hálózati-megosztás-és-hitelesítő-adatok-tisztítása-(att&ck-t1070005))
- [Timestomp és MACE attribútummanipuláció (T1070.006)](#timestomp-és-mace-attribútummanipuláció-(t1070006))
- [Hálózati előzmények és RDP nyomkövetés eltávolítása (T1070.007)](#hálózati-előzmények-és-rdp-nyomkövetés-eltávolítása-(t1070007))
- [E-mail tárolás és adatbázis-megsemmisítés (T1070.008)](#e-mail-tárolás-és-adatbázis-megsemmisítés-(t1070008))
- [Perzisztencia műtermékek eltávolítása (T1070.009)](#perzisztencia-műtermékek-eltávolítása-(t1070009))
- [Alkalmazási réteg C2 anomália (T1071)](#alkalmazási-réteg-c2-anomália-(t1071))
- [HTTPS C2 anomália (T1071.001)](#https-c2-anomália-(t1071001))
- [FTP/SFTP protokoll anomália (T1071.002)](#ftpsftp-protokoll-anomália-(t1071002))
- [Levelezési protokoll anomália (T1071.003)](#levelezési-protokoll-anomália-(t1071003))
- [DNS Tunneling & Beaconing (T1071.004)](#dns-tunneling-&-beaconing-(t1071004))
- [Nagy pontosságú szoftvertelepítési eszköz visszaélések észlelése](#nagy-pontosságú-szoftvertelepítési-eszköz-visszaélések-észlelése)
- [Adatállomási anomália (T1074)](#adatállomási-anomália-(t1074))
- [Helyi adatállomási anomália (T1074.001)](#helyi-adatállomási-anomália-(t1074001))
- [Távoli adatállomásozás (T1074.002)](#távoli-adatállomásozás-(t1074002))
- [Nagy pontosságú rendellenes bejelentkezés érvényes fiókon keresztül](#nagy-pontosságú-rendellenes-bejelentkezés-érvényes-fiókon-keresztül)
- [Nagy pontosságú alapértelmezett fiókkal való visszaélés észlelése](#nagy-pontosságú-alapértelmezett-fiókkal-való-visszaélés-észlelése)
- [High-Fidelity Domain Account Lateral Movement Anomália](#high-fidelity-domain-account-lateral-movement-anomália)
- [Nagy pontosságú helyi fiók távelérés észlelése](#nagy-pontosságú-helyi-fiók-távelérés-észlelése)
- [High-Fidelity Cloud-fiók kompromittálódása (Entra ID)](#high-fidelity-cloud-fiók-kompromittálódása-(entra-id))
- [Megosztott tartalom (T1080)](#megosztott-tartalom-(t1080))
- [Rendszerinformáció-felderítés (T1082)](#rendszerinformáció-felderítés-(t1082))
- [Fájl- és könyvtárfelderítés (T1083)](#fájl--és-könyvtárfelderítés-(t1083))
- [Net user vagy net localgroup gyanús használata a cmd.exe-n keresztül](#net-user-vagy-net-localgroup-gyanús-használata-a-cmdexe-n-keresztül)
- [Helyi fiókfelderítés (T1087.001)](#helyi-fiókfelderítés-(t1087001))
- [Domainfiók felderítése (T1087.002)](#domainfiók-felderítése-(t1087002))
- [E-mail fiók felderítése (T1087.003)](#e-mail-fiók-felderítése-(t1087003))
- [Cloud Account Discovery (T1087.004)](#cloud-account-discovery-(t1087004))
- [Proxy és forgáspont-észlelés (T1090)](#proxy-és-forgáspont-észlelés-(t1090))
- [Belső proxy és pivot észlelés (T1090.001)](#belső-proxy-és-pivot-észlelés-(t1090001))
- [Külső proxy és alagút (T1090.002)](#külső-proxy-és-alagút-(t1090002))
- [Többugrásos proxy és Tor észlelés (T1090.003)](#többugrásos-proxy-és-tor-észlelés-(t1090003))
- [Domain Fronting Detection (T1090.004)](#domain-fronting-detection-(t1090004))
- [Nagy pontosságú folyamatvégrehajtás cserélhető adathordozóról](#nagy-pontosságú-folyamatvégrehajtás-cserélhető-adathordozóról)
- [C2 cserélhető adathordozó anomália (T1071.002 / T1092)](#c2-cserélhető-adathordozó-anomália-(t1071002--t1092))
- [Nem alkalmazási réteg C2 (T1095)](#nem-alkalmazási-réteg-c2-(t1095))
- [Nagy pontosságú fiókmanipuláció – a kitartásra összpontosítva](#nagy-pontosságú-fiókmanipuláció-–-a-kitartásra-összpontosítva)
- [High-Fidelity Entra ID alkalmazás hitelesítő adatok kiegészítése](#high-fidelity-entra-id-alkalmazás-hitelesítő-adatok-kiegészítése)
- [High-Fidelity Exchange Mailbox Permission Grant (T1098.002)](#high-fidelity-exchange-mailbox-permission-grant-(t1098002))
- [High-Fidelity Entra ID App tanúsítvány kiegészítése](#high-fidelity-entra-id-app-tanúsítvány-kiegészítése)
- [High-Fidelity Azure-szerepkör-hozzárendelés eszkalációja](#high-fidelity-azure-szerepkör-hozzárendelés-eszkalációja)
- [High-Fidelity Device Registration Perzisztencia (T1098.005)](#high-fidelity-device-registration-perzisztencia-(t1098005))
- [High-Fidelity MFA módszer kiegészítés](#high-fidelity-mfa-módszer-kiegészítés)
- [Web Service C2 (T1102)](#web-service-c2-(t1102))
- [Dead Drop Resolver (T1102.001)](#dead-drop-resolver-(t1102001))
- [Kétirányú felhő C2 (T1102.002)](#kétirányú-felhő-c2-(t1102002))
- [Egyirányú webszolgáltatás C2 (T1102.003)](#egyirányú-webszolgáltatás-c2-(t1102003))
- [Többlépcsős C2 (T1104)](#többlépcsős-c2-(t1104))
- [Beépített Windows-eszközök gyanús használata fájlok letöltéséhez és kódvégrehajtáshoz](#beépített-windows-eszközök-gyanús-használata-fájlok-letöltéséhez-és-kódvégrehajtáshoz)
- [High-Fidelity Native API visszaélés LOLBins-en keresztül](#high-fidelity-native-api-visszaélés-lolbins-en-keresztül)
- [Brute Force & Tooling (T1110)](#brute-force-&-tooling-(t1110))
- [Egyetlen felhasználó többszöri sikertelen bejelentkezési kísérlete (lehetséges jelszókitalálás)](#egyetlen-felhasználó-többszöri-sikertelen-bejelentkezési-kísérlete-(lehetséges-jelszókitalálás))
- [Hitelesítési adatok exportálása és feltörése (T1110.002)](#hitelesítési-adatok-exportálása-és-feltörése-(t1110002))
- [Jelszó kiszórás (T1110.003)](#jelszó-kiszórás-(t1110003))
- [Hitelesítési adatokkal való visszaélés és a kombinált listákkal való visszaélés (T1110.004)](#hitelesítési-adatokkal-való-visszaélés-és-a-kombinált-listákkal-való-visszaélés-(t1110004))
- [MFA-kijátszás és munkamenet-eltérítés (T1111)](#mfa-kijátszás-és-munkamenet-eltérítés-(t1111))
- [Registry manipuláció kijátszás céljából (T1112)](#registry-manipuláció-kijátszás-céljából-(t1112))
- [Képernyőrögzítési anomália (T1113)](#képernyőrögzítési-anomália-(t1113))
- [E-mail betakarítási anomália (T1114)](#e-mail-betakarítási-anomália-(t1114))
- [Helyi e-mail-gyűjtési anomália (T1114.001)](#helyi-e-mail-gyűjtési-anomália-(t1114001))
- [Távoli e-mail exportálási rendellenesség (T1114.002)](#távoli-e-mail-exportálási-rendellenesség-(t1114002))
- [E-mail továbbítási szabály rendellenessége (T1114.003)](#e-mail-továbbítási-szabály-rendellenessége-(t1114003))
- [Vágólapadatok kémkedése (T1115)](#vágólapadatok-kémkedése-(t1115))
- [Automatizált begyűjtés (T1119)](#automatizált-begyűjtés-(t1119))
- [Perifériás eszköz felfedezése (T1120)](#perifériás-eszköz-felfedezése-(t1120))
- [Hangrögzítés és kémkedés (T1123)](#hangrögzítés-és-kémkedés-(t1123))
- [Rendszeridő-felderítés (T1124)](#rendszeridő-felderítés-(t1124))
- [Videórögzítési anomália (T1125)](#videórögzítési-anomália-(t1125))
- [Trusted Developer Utility Proxy (T1127)](#trusted-developer-utility-proxy-(t1127))
- [MSBuild proxy végrehajtása (T1127.001)](#msbuild-proxy-végrehajtása-(t1127001))
- [Nagy pontosságú megosztott modul betöltése nem megbízható útvonalról](#nagy-pontosságú-megosztott-modul-betöltése-nem-megbízható-útvonalról)
- [Adatkódolás és obfuszkálás (T1132)](#adatkódolás-és-obfuszkálás-(t1132))
- [Szabványos kódolás és hasznos terhelés beadása (T1132.001)](#szabványos-kódolás-és-hasznos-terhelés-beadása-(t1132001))
- [Nem szabványos kódolás és XOR obfuszkáció (T1132.002)](#nem-szabványos-kódolás-és-xor-obfuszkáció-(t1132002))
- [Rendellenes külső távoli szolgáltatás-hozzáférési kontextus](#rendellenes-külső-távoli-szolgáltatás-hozzáférési-kontextus)
- [Hozzáférési token manipuláció és megszemélyesítés (T1134)](#hozzáférési-token-manipuláció-és-megszemélyesítés-(t1134))
- [Token megszemélyesítés LSASS Handle Duplikáción keresztül (T1134.001)](#token-megszemélyesítés-lsass-handle-duplikáción-keresztül-(t1134001))
- [Folyamat létrehozása tokennel (T1134.002)](#folyamat-létrehozása-tokennel-(t1134002))
- [Gyári és megszemélyesítő token (T1134.003)](#gyári-és-megszemélyesítő-token-(t1134003))
- [Szülői PID-hamisítás és folyamatfa megsértése (T1134.004)](#szülői-pid-hamisítás-és-folyamatfa-megsértése-(t1134004))
- [SID-előzmény befecskendezés és DS-manipuláció (T1134.005)](#sid-előzmény-befecskendezés-és-ds-manipuláció-(t1134005))
- [Hálózati megosztás felfedezése (T1135)](#hálózati-megosztás-felfedezése-(t1135))
- [Ultra-Pro jogosulatlan fiók létrehozása (T1136)](#ultra-pro-jogosulatlan-fiók-létrehozása-(t1136))
- [Ultra-Pro jogosulatlan helyi fiók létrehozása (T1136.001)](#ultra-pro-jogosulatlan-helyi-fiók-létrehozása-(t1136001))
- [Ultra-Pro jogosulatlan domain fiók létrehozása (T1136.002)](#ultra-pro-jogosulatlan-domain-fiók-létrehozása-(t1136002))
- [Ultra-Pro jogosulatlan felhőfiók létrehozása (T1136.003)](#ultra-pro-jogosulatlan-felhőfiók-létrehozása-(t1136003))
- [Az Office-alkalmazások indítási állandósága (T1137)](#az-office-alkalmazások-indítási-állandósága-(t1137))
- [Az Office globális sablonjának gyanús módosítása (Normal.dotm)](#az-office-globális-sablonjának-gyanús-módosítása-(normaldotm))
- [Office teszt DLL-perzisztencia (T1137.002)](#office-teszt-dll-perzisztencia-(t1137002))
- [Outlook egyéni űrlapok állandósága (T1137.003)](#outlook-egyéni-űrlapok-állandósága-(t1137003))
- [Az Outlook kezdőlapjának eltérítése és megkerülése (T1137.004)](#az-outlook-kezdőlapjának-eltérítése-és-megkerülése-(t1137004))
- [Az Office biztonsági házirendjének manipulálása (T1137.005)](#az-office-biztonsági-házirendjének-manipulálása-(t1137005))
- [Office-bővítmény bináris állandósága (T1137.006)](#office-bővítmény-bináris-állandósága-(t1137006))
- [Lopakodó deobfuszkálás/dekódolás (T1140)](#lopakodó-deobfuszkálásdekódolás-(t1140))
- [Ultra-Pro Browser Extension Force-Install Persistence (T1176)](#ultra-pro-browser-extension-force-install-persistence-(t1176))
- [Böngészőmunkamenet-eltérítés (T1185)](#böngészőmunkamenet-eltérítés-(t1185))
- [Kényszerített hitelesítés (T1187)](#kényszerített-hitelesítés-(t1187))
- [Böngészőből származó shell vagy rendszereszköz végrehajtása](#böngészőből-származó-shell-vagy-rendszereszköz-végrehajtása)
- [Gyanús Cross-Site Scripting (XSS) kísérlet észlelve a webszerveren](#gyanús-cross-site-scripting-(xss)-kísérlet-észlelve-a-webszerveren)
- [Nagy pontosságú ellátási lánc-kompromittálódás észlelése (frissítés utáni anomália)](#nagy-pontosságú-ellátási-lánc-kompromittálódás-észlelése-(frissítés-utáni-anomália))
- [Nagy pontosságú függőségi mérgezés-észlelés](#nagy-pontosságú-függőségi-mérgezés-észlelés)
- [High-Fidelity veszélyeztetett bináris tevékenység (frissítés után)](#high-fidelity-veszélyeztetett-bináris-tevékenység-(frissítés-után))
- [Nagy pontosságú hardver/firmware manipuláció észlelése](#nagy-pontosságú-hardverfirmware-manipuláció-észlelése)
- [Gyanús fájlok letöltése a Bitsadmin segítségével (High Fidelity)](#gyanús-fájlok-letöltése-a-bitsadmin-segítségével-(high-fidelity))
- [Nagy pontosságú megbízható kapcsolati visszaélések észlelése](#nagy-pontosságú-megbízható-kapcsolati-visszaélések-észlelése)
- [Rosszindulatú hardver által kiváltott parancsvégrehajtás (HID-injektálás)](#rosszindulatú-hardver-által-kiváltott-parancsvégrehajtás-(hid-injektálás))
- [Jelszóházirend-felderítés észlelése (T1201)](#jelszóházirend-felderítés-észlelése-(t1201))
- [Közvetett parancsvégrehajtás proxy binárisokon keresztül (T1202)](#közvetett-parancsvégrehajtás-proxy-binárisokon-keresztül-(t1202))
- [High-Fidelity kliensoldali kihasználás és shell spawning](#high-fidelity-kliensoldali-kihasználás-és-shell-spawning)
- [Gyanús gyermekfolyamat, amelyet a Microsoft Office alkalmazás idézett elő (High Fidelity)](#gyanús-gyermekfolyamat-amelyet-a-microsoft-office-alkalmazás-idézett-elő-(high-fidelity))
- [A rosszindulatú hivatkozás nagy pontosságú felhasználói végrehajtása (T1204.001)](#a-rosszindulatú-hivatkozás-nagy-pontosságú-felhasználói-végrehajtása-(t1204001))
- [Rosszindulatú fájlok nagy pontosságú felhasználói végrehajtása](#rosszindulatú-fájlok-nagy-pontosságú-felhasználói-végrehajtása)
- [Nagy pontosságú végrehajtás a beépített virtuális lemezről (T1204.003)](#nagy-pontosságú-végrehajtás-a-beépített-virtuális-lemezről-(t1204003))
- [Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel](#adathalászat-rosszindulatú-linken-keresztül-domain-és-feladó-rendellenességekkel)
- [Forgalomjelző és port kopogtatási tevékenység (T1205)](#forgalomjelző-és-port-kopogtatási-tevékenység-(t1205))
- [Port Knocking vagy Raw Socket Listener telepítése (T1205.001)](#port-knocking-vagy-raw-socket-listener-telepítése-(t1205001))
- [WFP kiemelés regisztrációja vagy kernel-illesztőprogram-beállítás (T1205.002)](#wfp-kiemelés-regisztrációja-vagy-kernel-illesztőprogram-beállítás-(t1205002))
- [Rogue DC / DCSárnyékérzékelés (T1207)](#rogue-dc--dcsárnyékérzékelés-(t1207))
- [Remote Service RCE/Post Exploitation Spawn Detection (T1210)](#remote-service-rcepost-exploitation-spawn-detection-(t1210))
- [Sandbox Breakout / Privilege Escalation Exploitation (T1211)](#sandbox-breakout--privilege-escalation-exploitation-(t1211))
- [Hitelesítési adatok szolgáltatás kihasználásának észlelése (T1212)](#hitelesítési-adatok-szolgáltatás-kihasználásának-észlelése-(t1212))
- [Belső adattár tömegkiíratásának észlelése (T1213)](#belső-adattár-tömegkiíratásának-észlelése-(t1213))
- [Összefolyási tömeg kaparás észlelése (T1213.001)](#összefolyási-tömeg-kaparás-észlelése-(t1213001))
- [Vállalati SharePoint tömeges adatok kiszűrésének észlelése (T1213.002)](#vállalati-sharepoint-tömeges-adatok-kiszűrésének-észlelése-(t1213002))
- [Vállalati tudásbázis tömeges kaparás/tükrözés észlelése (T1213.003)](#vállalati-tudásbázis-tömeges-kaparástükrözés-észlelése-(t1213003))
- [Windows rendszerszkript proxy végrehajtása (T1216)](#windows-rendszerszkript-proxy-végrehajtása-(t1216))
- [Pubprn.vbs Script proxy végrehajtása (T1216.001)](#pubprnvbs-script-proxy-végrehajtása-(t1216001))
- [Böngészőinformációk felfedezése (T1217)](#böngészőinformációk-felfedezése-(t1217))
- [Windows rendszer bináris proxy végrehajtása](#windows-rendszer-bináris-proxy-végrehajtása)
- [HH.exe CHM/ITS proxy végrehajtás](#hhexe-chmits-proxy-végrehajtás)
- [Control.exe CPL/DLL proxy végrehajtása](#controlexe-cpldll-proxy-végrehajtása)
- [MsiExec proxy végrehajtás](#msiexec-proxy-végrehajtás)
- [InstallUtil .NET proxy végrehajtás](#installutil-net-proxy-végrehajtás)
- [A távoli szkript gyanús Mshta végrehajtása (high Fidelity)](#a-távoli-szkript-gyanús-mshta-végrehajtása-(high-fidelity))
- [Gyanús Msiexec telepítés távoli URL-ről (High Fidelity)](#gyanús-msiexec-telepítés-távoli-url-ről-(high-fidelity))
- [Odbcconf REGSVR proxy végrehajtás](#odbcconf-regsvr-proxy-végrehajtás)
- [Regsvcs/Regasm .NET proxy végrehajtás](#regsvcsregasm-net-proxy-végrehajtás)
- [Gyanús Regsvr32 végrehajtás, amely LOLBAS-visszaélést jelez (high Fidelity)](#gyanús-regsvr32-végrehajtás-amely-lolbas-visszaélést-jelez-(high-fidelity))
- [Gyanús Rundll32 végrehajtás szkripttel vagy távoli hasznos adattartalommal (high Fidelity)](#gyanús-rundll32-végrehajtás-szkripttel-vagy-távoli-hasznos-adattartalommal-(high-fidelity))
- [Verclsid proxy végrehajtása COM Object Abuse segítségével](#verclsid-proxy-végrehajtása-com-object-abuse-segítségével)
- [Rundll32 proxy végrehajtása (LOLBAS visszaélés)](#rundll32-proxy-végrehajtása-(lolbas-visszaélés))
- [Gyanús MMC-proxy-végrehajtás nem megbízható MSC-n vagy COM-eltérítésen keresztül](#gyanús-mmc-proxy-végrehajtás-nem-megbízható-msc-n-vagy-com-eltérítésen-keresztül)
- [Gyanús szolgáltatás létrehozása a távfelügyeleti eszközökön keresztül a jóváhagyott felügyeleti körön kívül](#gyanús-szolgáltatás-létrehozása-a-távfelügyeleti-eszközökön-keresztül-a-jóváhagyott-felügyeleti-körön-kívül)
- [XSL-szkript feldolgozás (T1220)](#xsl-szkript-feldolgozás-(t1220))
- [Irodai sablon befecskendezése (T1221)](#irodai-sablon-befecskendezése-(t1221))
- [Windows engedélyek módosítása (T1222)](#windows-engedélyek-módosítása-(t1222))
- [Windows fájlengedélyek módosítása (T1222.001)](#windows-fájlengedélyek-módosítása-(t1222001))
- [Linux fájlengedélyek módosítása (T1222.002)](#linux-fájlengedélyek-módosítása-(t1222002))
- [Execution Guardrails Discovery (T1480)](#execution-guardrails-discovery-(t1480))
- [Environmental Keying Discovery (T1480.001)](#environmental-keying-discovery-(t1480001))
- [Domain Trust Discovery (T1482)](#domain-trust-discovery-(t1482))
- [Domainházirend-manipuláció és csoportházirend-objektumokkal való visszaélés (T1484)](#domainházirend-manipuláció-és-csoportházirend-objektumokkal-való-visszaélés-(t1484))
- [Csoportházirend módosítása és visszaélés (T1484.001)](#csoportházirend-módosítása-és-visszaélés-(t1484001))
- [Domain Trust Tampering & SID Filtering Bypass (T1484.002)](#domain-trust-tampering-&-sid-filtering-bypass-(t1484002))
- [Adatmegsemmisítés (T1485/T1490)](#adatmegsemmisítés-(t1485t1490))
- [Ransomware-előkészítési tevékenység észlelve a Windows Host-on (High Fidelity)](#ransomware-előkészítési-tevékenység-észlelve-a-windows-host-on-(high-fidelity))
- [Szervizmegálló (T1489)](#szervizmegálló-(t1489))
- [Kötet árnyékmásolatok gyanús törlése a VSSAdminon keresztül (High Fidelity)](#kötet-árnyékmásolatok-gyanús-törlése-a-vssadminon-keresztül-(high-fidelity))
- [Elrontás (T1491)](#elrontás-(t1491))
- [Belső sérülés (T1491.001)](#belső-sérülés-(t1491001))
- [Külső rontás (T1491.002)](#külső-rontás-(t1491002))
- [Firmware korrupció (T1495)](#firmware-korrupció-(t1495))
- [Erőforrás-eltérítés (T1496)](#erőforrás-eltérítés-(t1496))
- [Virtualizáció/Sandbox Evasion (T1497)](#virtualizációsandbox-evasion-(t1497))
- [VM Artifact Discovery (T1497.001)](#vm-artifact-discovery-(t1497001))
- [Felhasználói interakciók elkerülése (T1497.002)](#felhasználói-interakciók-elkerülése-(t1497002))
- [Időalapú kijátszás (T1497.003)](#időalapú-kijátszás-(t1497003))
- [Network DoS (T1498)](#network-dos-(t1498))
- [Közvetlen áramlású árvíz (T1498.001)](#közvetlen-áramlású-árvíz-(t1498001))
- [Végpont szolgáltatásmegtagadás (T1499)](#végpont-szolgáltatásmegtagadás-(t1499))
- [OS önmegsemmisítés-észlelés (T1499.001)](#os-önmegsemmisítés-észlelés-(t1499001))
- [Szolgáltatás kimerülésének észlelése (T1499.002)](#szolgáltatás-kimerülésének-észlelése-(t1499002))
- [OS önmegsemmisítés-észlelés (T1499.003)](#os-önmegsemmisítés-észlelés-(t1499003))
- [Erőforrás-kimerülés észlelése (T1499.004)](#erőforrás-kimerülés-észlelése-(t1499004))
- [Web Shell végrehajtási minták (T1505)](#web-shell-végrehajtási-minták-(t1505))
- [SQL Server Command Shell végrehajtása (T1505.001)](#sql-server-command-shell-végrehajtása-(t1505001))
- [IIS natív modul-injekció (T1505.002)](#iis-natív-modul-injekció-(t1505002))
- [Webshell-feltöltés vagy interakcióészlelés (T1505.003)](#webshell-feltöltés-vagy-interakcióészlelés-(t1505003))
- [Alaplapi rendszerindítási kép és SPI Flash-szabotázs (T1505.004)](#alaplapi-rendszerindítási-kép-és-spi-flash-szabotázs-(t1505004))
- [Terminal Services DLL-eltérítés észlelése (T1505.005)](#terminal-services-dll-eltérítés-észlelése-(t1505005))
- [Szoftverfelderítés-észlelés (T1518)](#szoftverfelderítés-észlelés-(t1518))
- [Biztonsági szoftverfelderítés észlelése (T1518.001)](#biztonsági-szoftverfelderítés-észlelése-(t1518001))
- [Exploit-grade jogosulatlan tárolókép-végrehajtás (Implant Container Image)](#exploit-grade-jogosulatlan-tárolókép-végrehajtás-(implant-container-image))
- [Cloud Service Discovery Detection (T1526)](#cloud-service-discovery-detection-(t1526))
- [Alkalmazási token és munkamenet-eltérítés észlelése (T1528)](#alkalmazási-token-és-munkamenet-eltérítés-észlelése-(t1528))
- [Jogosulatlan rendszerleállítás/újraindítás észlelése (T1529)](#jogosulatlan-rendszerleállításújraindítás-észlelése-(t1529))
- [Cloud Storage Data Theft Detection (T1530)](#cloud-storage-data-theft-detection-(t1530))
- [Fiókhozzáférés eltávolításának észlelése (T1531)](#fiókhozzáférés-eltávolításának-észlelése-(t1531))
- [Belső adathalászat-észlelés (T1534)](#belső-adathalászat-észlelés-(t1534))
- [Nem használt szolgáltatás-manipuláció észlelése (T1535)](#nem-használt-szolgáltatás-manipuláció-észlelése-(t1535))
- [Felhőbeli fiókok kiszűrésének észlelése (T1537)](#felhőbeli-fiókok-kiszűrésének-észlelése-(t1537))
- [Cloud Service Dashboard Discovery (T1538)](#cloud-service-dashboard-discovery-(t1538))
- [Webböngésző munkamenet-cookie-k és hitelesítő adatok lopásának észlelése (T1539)](#webböngésző-munkamenet-cookie-k-és-hitelesítő-adatok-lopásának-észlelése-(t1539))
- [OS előtti rendszerindítási manipuláció (T1542)](#os-előtti-rendszerindítási-manipuláció-(t1542))
- [ROM készlet és UEFI firmware manipuláció (T1542.001)](#rom-készlet-és-uefi-firmware-manipuláció-(t1542001))
- [Komponens firmware-szabotázs (T1542.002)](#komponens-firmware-szabotázs-(t1542002))
- [Bootkit Persistence & EFI manipuláció (T1542.003)](#bootkit-persistence-&-efi-manipuláció-(t1542003))
- [Alaplapi rendszerindítási kép és SPI Flash-szabotázs (T1542.004)](#alaplapi-rendszerindítási-kép-és-spi-flash-szabotázs-(t1542004))
- [DHCP/PXE rendszerindítási eltérítés (T1542.005)](#dhcppxe-rendszerindítási-eltérítés-(t1542005))
- [Nem adminisztrátor felhasználó, aki több érzékeny Windows-szolgáltatást próbál leállítani vagy módosítani](#nem-adminisztrátor-felhasználó-aki-több-érzékeny-windows-szolgáltatást-próbál-leállítani-vagy-módosítani)
- [Ultra-Pro macOS Launch Agent Persistence Detection (T1543.001)](#ultra-pro-macos-launch-agent-persistence-detection-(t1543001))
- [Ultra-Pro Systemd Service Persistence (T1543.002)](#ultra-pro-systemd-service-persistence-(t1543002))
- [Ultra-Pro jogosulatlan Windows-szolgáltatás telepítése (T1543.003)](#ultra-pro-jogosulatlan-windows-szolgáltatás-telepítése-(t1543003))
- [Ultra-Pro jogosulatlan macOS Launch Daemon (T1543.004)](#ultra-pro-jogosulatlan-macos-launch-daemon-(t1543004))
- [Ultra-Pro WMI-esemény-előfizetés tartóssága (T1546.003)](#ultra-pro-wmi-esemény-előfizetés-tartóssága-(t1546003))
- [Ultra-Pro fájltársítás eltérítése (T1546.001)](#ultra-pro-fájltársítás-eltérítése-(t1546001))
- [Ultra-Pro képernyővédő tartós észlelés (T1546.002)](#ultra-pro-képernyővédő-tartós-észlelés-(t1546002))
- [WMI-esemény-előfizetés állandósága WMIC-en vagy PowerShell-en keresztül (High Fidelity)](#wmi-esemény-előfizetés-állandósága-wmic-en-vagy-powershell-en-keresztül-(high-fidelity))
- [Ultra-Pro AppCert DLL Perzisztencia Detection (T1546.004)](#ultra-pro-appcert-dll-perzisztencia-detection-(t1546004))
- [Ultra-Pro Shell Trap Perzisztencia-észlelés (T1546.005)](#ultra-pro-shell-trap-perzisztencia-észlelés-(t1546005))
- [Ultra-Pro Mach-O LC_LOAD_DYLIB befecskendezés (T1546.006)](#ultra-pro-mach-o-lc_load_dylib-befecskendezés-(t1546006))
- [Ultra-Pro Netsh Helper DLL-perzisztencia (T1546.007)](#ultra-pro-netsh-helper-dll-perzisztencia-(t1546007))
- [Ultra-Pro WER SilentProcessExit Persistence (T1546.008)](#ultra-pro-wer-silentprocessexit-persistence-(t1546008))
- [Ultra-Pro AppInit_DLLs Perzisztencia-észlelés (T1546.009)](#ultra-pro-appinit_dlls-perzisztencia-észlelés-(t1546009))
- [Ultra-Pro AppCert DLL Perzisztencia-észlelés (T1546.010)](#ultra-pro-appcert-dll-perzisztencia-észlelés-(t1546010))
- [Ultra-Pro Application Shimming Perzisztencia Detection (T1546.011)](#ultra-pro-application-shimming-perzisztencia-detection-(t1546011))
- [Ultra-Pro IFEO hibakereső eltérítés-észlelés (T1546.012)](#ultra-pro-ifeo-hibakereső-eltérítés-észlelés-(t1546012))
- [Ultra-Pro PowerShell Profile Injection Detection (T1546.013)](#ultra-pro-powershell-profile-injection-detection-(t1546013))
- [Ultra-Pro WMI-esemény-előfizetés tartóssága (T1546.014)](#ultra-pro-wmi-esemény-előfizetés-tartóssága-(t1546014))
- [Gyanús COM-eltérítés a felhasználói szintű tartósság érdekében (high Fidelity)](#gyanús-com-eltérítés-a-felhasználói-szintű-tartósság-érdekében-(high-fidelity))
- [Ultra-Pro MSI telepítő egyéni műveletek tartóssága (T1546.016)](#ultra-pro-msi-telepítő-egyéni-műveletek-tartóssága-(t1546016))
- [Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása](#gyanús-rendszerindítási-vagy-bejelentkezési-automatikus-indítás-végrehajtása)
- [Gyanús beállításjegyzék-futtatási kulcsmódosítás a felhasználói állandóság érdekében (high Fidelity)](#gyanús-beállításjegyzék-futtatási-kulcsmódosítás-a-felhasználói-állandóság-érdekében-(high-fidelity))
- [High-Fidelity LSA hitelesítési csomag tartóssága](#high-fidelity-lsa-hitelesítési-csomag-tartóssága)
- [Nagy pontosságú időszolgáltató tartóssága (T1547.003)](#nagy-pontosságú-időszolgáltató-tartóssága-(t1547003))
- [High-Fidelity Winlogon Helper DLL-perzisztencia (T1547.004)](#high-fidelity-winlogon-helper-dll-perzisztencia-(t1547004))
- [High-Fidelity SSP DLL-perzisztencia (T1547.005)](#high-fidelity-ssp-dll-perzisztencia-(t1547005))
- [High-Fidelity kernel-illesztőprogram regisztráció (T1547.006)](#high-fidelity-kernel-illesztőprogram-regisztráció-(t1547006))
- [High-Fidelity böngésző munkamenet-perzisztencia (T1547.007)](#high-fidelity-böngésző-munkamenet-perzisztencia-(t1547007))
- [High-Fidelity LSASS illesztőprogram/csomag tartósság (T1547.008)](#high-fidelity-lsass-illesztőprogramcsomag-tartósság-(t1547008))
- [Nagy pontosságú parancsikon módosítás észlelése](#nagy-pontosságú-parancsikon-módosítás-észlelése)
- [High-Fidelity AppCert DLL-perzisztencia (T1547.010)](#high-fidelity-appcert-dll-perzisztencia-(t1547010))
- [High-Fidelity alkalmazás Shimming Perzisztencia (T1547.011)](#high-fidelity-alkalmazás-shimming-perzisztencia-(t1547011))
- [High-Fidelity COM-eltérítés tartóssága (T1547.012)](#high-fidelity-com-eltérítés-tartóssága-(t1547012))
- [High-Fidelity E-mail Client Helper Perzisztencia (T1547.013)](#high-fidelity-e-mail-client-helper-perzisztencia-(t1547013))
- [High-Fidelity Active Setup Persistence (T1547.014)](#high-fidelity-active-setup-persistence-(t1547014))
- [High-Fidelity COM-eltérítés tartósság (T1547.015)](#high-fidelity-com-eltérítés-tartósság-(t1547015))
- [Jogosultság kiterjesztése rendszerleíró adatbázis eltérítésével (T1548)](#jogosultság-kiterjesztése-rendszerleíró-adatbázis-eltérítésével-(t1548))
- [Setuid/Setgid bitmanipuláció (T1548.001)](#setuidsetgid-bitmanipuláció-(t1548001))
- [UAC bypass a Fodhelper Registry Hijack segítségével (High Fidelity)](#uac-bypass-a-fodhelper-registry-hijack-segítségével-(high-fidelity))
- [Sudoer-manipuláció és szudóval való visszaélés (T1548.003)](#sudoer-manipuláció-és-szudóval-való-visszaélés-(t1548003))
- [AppleScript Privilege Escalation (T1548.004)](#applescript-privilege-escalation-(t1548004))
- [SUID Desktop Entry & Shortcut Abuse (T1548.005)](#suid-desktop-entry-&-shortcut-abuse-(t1548005))
- [Alternatív hitelesítési anyag (T1550)](#alternatív-hitelesítési-anyag-(t1550))
- [Alkalmazás-hozzáférési token visszaélés (T1550.001)](#alkalmazás-hozzáférési-token-visszaélés-(t1550001))
- [Pass-the-Hash Detection (T1550.002)](#pass-the-hash-detection-(t1550002))
- [Pass-the-Ticket Detection (T1550.003)](#pass-the-ticket-detection-(t1550003))
- [Pass-the-Session Detection (T1550.004)](#pass-the-session-detection-(t1550004))
- [Nem biztonságos hitelesítő adatok felfedezése (T1552)](#nem-biztonságos-hitelesítő-adatok-felfedezése-(t1552))
- [Hitelesítő adatok a Files Discoveryben (T1552.001)](#hitelesítő-adatok-a-files-discoveryben-(t1552001))
- [Hitelesítési adatok a rendszerleíró adatbázisban (T1552.002)](#hitelesítési-adatok-a-rendszerleíró-adatbázisban-(t1552002))
- [Shell History & Console Discovery (T1552.003)](#shell-history-&-console-discovery-(t1552003))
- [Privát kulcs felfedezése (T1552.004)](#privát-kulcs-felfedezése-(t1552004))
- [Cloud Credential Discovery (T1552.005)](#cloud-credential-discovery-(t1552005))
- [Hitelesítő adatok a Files Discoveryben (T1552.006)](#hitelesítő-adatok-a-files-discoveryben-(t1552006))
- [Container Secret Discovery (T1552.007)](#container-secret-discovery-(t1552007))
- [GPP jelszó felderítés (T1552.008)](#gpp-jelszó-felderítés-(t1552008))
- [Subvert Trust Controls (T1553)](#subvert-trust-controls-(t1553))
- [macOS Gatekeeper és Quarantine Bypass (T1553.001)](#macos-gatekeeper-és-quarantine-bypass-(t1553001))
- [SIP-eltérítés és bizalomfelforgatás (T1553.002)](#sip-eltérítés-és-bizalomfelforgatás-(t1553002))
- [Windows Catalog Database Subversion (T1553.003)](#windows-catalog-database-subversion-(t1553003))
- [Root Certificate Injection (T1553.004)](#root-certificate-injection-(t1553004))
- [Mark-of-the-Web (MotW) bypass & Zone Subversion Detection (T1553.005)](#mark-of-the-web-(motw)-bypass-&-zone-subversion-detection-(t1553005))
- [Windows Code Integrity & DSE Subversion Detection (T1553.006)](#windows-code-integrity-&-dse-subversion-detection-(t1553006))
- [Ultra-Pro Client Bináris Integritás Kompromisszum (T1554)](#ultra-pro-client-bináris-integritás-kompromisszum-(t1554))
- [Nem böngészős folyamat hozzáférése a böngésző hitelesítőadat-tárolóihoz (High Fidelity)](#nem-böngészős-folyamat-hozzáférése-a-böngésző-hitelesítőadat-tárolóihoz-(high-fidelity))
- [Windows Vault hitelesítő adatok legyűjtésének észlelése (T1555.001)](#windows-vault-hitelesítő-adatok-legyűjtésének-észlelése-(t1555001))
- [Biztonságos memóriakiürítés észlelése (T1555.002)](#biztonságos-memóriakiürítés-észlelése-(t1555002))
- [Böngésző hitelesítő adatok begyűjtésének észlelése (T1555.003)](#böngésző-hitelesítő-adatok-begyűjtésének-észlelése-(t1555003))
- [Windows Credential Manager begyűjtési észlelés (T1555.004)](#windows-credential-manager-begyűjtési-észlelés-(t1555004))
- [Jelszókezelő kivonatészlelés (T1555.005)](#jelszókezelő-kivonatészlelés-(t1555005))
- [Cloud Secret Harvesting Detection (T1555.006)](#cloud-secret-harvesting-detection-(t1555006))
- [Exploit-Grade hitelesítési folyamat eltérítése gyanús DLL-regisztráción keresztül](#exploit-grade-hitelesítési-folyamat-eltérítése-gyanús-dll-regisztráción-keresztül)
- [Exploit-Grade Security Support Provider Hijacking (LSA SSP)](#exploit-grade-security-support-provider-hijacking-(lsa-ssp))
- [Exploit-Grade jelszószűrő DLL-eltérítés LSA értesítési csomagokon keresztül](#exploit-grade-jelszószűrő-dll-eltérítés-lsa-értesítési-csomagokon-keresztül)
- [Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003)](#ultra-pro-pam-integrity-hijacking-&-backdoor-(t1556003))
- [Ultra-Pro hálózati eszköz hitelesítés eltérítése (T1556.004)](#ultra-pro-hálózati-eszköz-hitelesítés-eltérítése-(t1556004))
- [Ultra-Pro SID History Injection Correlation (T1556.005)](#ultra-pro-sid-history-injection-correlation-(t1556005))
- [Ultra-Pro Entra ID MFA módszereltérítés (T1556.006)](#ultra-pro-entra-id-mfa-módszereltérítés-(t1556006))
- [Hibrid identitás szinkronizálási manipuláció észlelése (T1556.007)](#hibrid-identitás-szinkronizálási-manipuláció-észlelése-(t1556007))
- [Hálózatról felhőre történő hitelesítés-eltérítés észlelése (T1556.008)](#hálózatról-felhőre-történő-hitelesítés-eltérítés-észlelése-(t1556008))
- [Ellenfél észlelése a középsőben (T1557)](#ellenfél-észlelése-a-középsőben-(t1557))
- [LLMNR/NBT-NS mérgezés és SMB-reléérzékelés (T1557.001)](#llmnrnbt-ns-mérgezés-és-smb-reléérzékelés-(t1557001))
- [Rogue ARP-mérgezés / MITM-észlelés (T1557.002)](#rogue-arp-mérgezés--mitm-észlelés-(t1557002))
- [Rogue DHCP / DHCP hamisítás-észlelés (T1557.003)](#rogue-dhcp--dhcp-hamisítás-észlelés-(t1557003))
- [Kerberos támadásészlelés](#kerberos-támadásészlelés)
- [Aranyjegy-hamisítás és befecskendezés](#aranyjegy-hamisítás-és-befecskendezés)
- [Ezüst jegyhamisítás és befecskendezés](#ezüst-jegyhamisítás-és-befecskendezés)
- [Gyanús Kerberos TGS jegykérés (Kerberoasting)](#gyanús-kerberos-tgs-jegykérés-(kerberoasting))
- [Ultra-Pro High-Fidelity AS-REP pörkölés és LDAP felsorolás](#ultra-pro-high-fidelity-as-rep-pörkölés-és-ldap-felsorolás)
- [High-Fidelity Indirekt IPC és COM végrehajtás](#high-fidelity-indirekt-ipc-és-com-végrehajtás)
- [Gyanús elnevezett csővezeték-létrehozás, amely utólagos kihasználási eszközökhöz kapcsolódik (High Fidelity)](#gyanús-elnevezett-csővezeték-létrehozás-amely-utólagos-kihasználási-eszközökhöz-kapcsolódik-(high-fidelity))
- [High-Fidelity Office DDE kontextuális anomália](#high-fidelity-office-dde-kontextuális-anomália)
- [High-Fidelity Hypervisor API és VM Escape Research](#high-fidelity-hypervisor-api-és-vm-escape-research)
- [Adatok gyanús archiválása exfiltráció céljából](#adatok-gyanús-archiválása-exfiltráció-céljából)
- [Adatarchiválás kiszűréshez](#adatarchiválás-kiszűréshez)
- [Adatarchiválás a könyvtáron keresztül](#adatarchiválás-a-könyvtáron-keresztül)
- [Archiválás egyéni módszerrel](#archiválás-egyéni-módszerrel)
- [Lemeztörlés](#lemeztörlés)
- [Lemeztartalom törlése](#lemeztartalom-törlése)
- [Lemezszerkezet törlése](#lemezszerkezet-törlése)
- [Biztonsági szolgáltatások gyanús leállítása](#biztonsági-szolgáltatások-gyanús-leállítása)
- [Windows Defender védelem kikapcsolása vagy módosítása PowerShell segítségével](#windows-defender-védelem-kikapcsolása-vagy-módosítása-powershell-segítségével)
- [A Windows eseménynapló szolgáltatásának károsodása](#a-windows-eseménynapló-szolgáltatásának-károsodása)
- [Parancselőzmények naplózási károsodása](#parancselőzmények-naplózási-károsodása)
- [Gyanús tűzfalmódosítás a Netsh.exe-n keresztül](#gyanús-tűzfalmódosítás-a-netshexe-n-keresztül)
- [Kijelző blokkolása és telemetria elnyomása](#kijelző-blokkolása-és-telemetria-elnyomása)
- [Cloud Firewall károsodás (T1562.007)](#cloud-firewall-károsodás-(t1562007))
- [Felhőnaplózás károsodása (T1562.008)](#felhőnaplózás-károsodása-(t1562008))
- [Csökkentett módú védelmi kijátszás (T1562.009)](#csökkentett-módú-védelmi-kijátszás-(t1562009))
- [Defense Downgrade Attack (T1562.010)](#defense-downgrade-attack-(t1562010))
- [Virtualizáció és Sandbox Evasion (T1564.011)](#virtualizáció-és-sandbox-evasion-(t1564011))
- [Felhőbiztonsági infrastruktúra károsodása (T1562.012)](#felhőbiztonsági-infrastruktúra-károsodása-(t1562012))
- [Távoli szolgáltatási munkamenet-eltérítés (T1563)](#távoli-szolgáltatási-munkamenet-eltérítés-(t1563))
- [Helyi munkamenet-eltérítés (T1563.001)](#helyi-munkamenet-eltérítés-(t1563001))
- [RDP munkamenet-eltérítés (T1563.002)](#rdp-munkamenet-eltérítés-(t1563002))
- [Műtermékek észlelésének elrejtése (T1564)](#műtermékek-észlelésének-elrejtése-(t1564))
- [Rejtett fájlattribútum-manipuláció (T1564.001)](#rejtett-fájlattribútum-manipuláció-(t1564001))
- [Rejtett felhasználói fiók létrehozása (T1564.002)](#rejtett-felhasználói-fiók-létrehozása-(t1564002))
- [Rejtett ablak végrehajtása (T1564.003)](#rejtett-ablak-végrehajtása-(t1564003))
- [NTFS alternatív adatfolyammal (ADS) való visszaélés (T1564.004)](#ntfs-alternatív-adatfolyammal-(ads)-való-visszaélés-(t1564004))
- [Rejtett fájlrendszer-manipuláció (T1564.005)](#rejtett-fájlrendszer-manipuláció-(t1564005))
- [Virtuális példány végrehajtási visszaélés (T1564.006)](#virtuális-példány-végrehajtási-visszaélés-(t1564006))
- [VBA Macro Security Evasion (T1564.007)](#vba-macro-security-evasion-(t1564007))
- [E-mailek elrejtésére vonatkozó szabályok észlelése (T1564.008)](#e-mailek-elrejtésére-vonatkozó-szabályok-észlelése-(t1564008))
- [Erőforrás-kivonás és visszaélés (T1564.009)](#erőforrás-kivonás-és-visszaélés-(t1564009))
- [Érveléshamisítás-észlelés feldolgozása (T1564.010)](#érveléshamisítás-észlelés-feldolgozása-(t1564010))
- [Virtuális példány visszaélés (T1564.011)](#virtuális-példány-visszaélés-(t1564011))
- [Adatkezelés (T1565)](#adatkezelés-(t1565))
- [Tárolt adatok kezelése (T1565.001)](#tárolt-adatok-kezelése-(t1565001))
- [Továbbított adatok kezelése (T1565.002)](#továbbított-adatok-kezelése-(t1565002))
- [Futásidejű folyamatmanipuláció (T1565.003)](#futásidejű-folyamatmanipuláció-(t1565003))
- [Nagy pontosságú adathalászat-végrehajtás kommunikációs alkalmazásokból](#nagy-pontosságú-adathalászat-végrehajtás-kommunikációs-alkalmazásokból)
- [High-Fidelity Spearphishing melléklet végrehajtás](#high-fidelity-spearphishing-melléklet-végrehajtás)
- [High-Fidelity böngészőből származó hasznos teher végrehajtás](#high-fidelity-böngészőből-származó-hasznos-teher-végrehajtás)
- [High-Fidelity Process Spawn az üzleti kommunikációs szolgáltatásból](#high-fidelity-process-spawn-az-üzleti-kommunikációs-szolgáltatásból)
- [A látás utáni távoli eszköz-végrehajtás nagy pontosságú észlelése](#a-látás-utáni-távoli-eszköz-végrehajtás-nagy-pontosságú-észlelése)
- [Webszolgáltatás kiszűrése (T1567)](#webszolgáltatás-kiszűrése-(t1567))
- [Exfil kódtár (T1567.001)](#exfil-kódtár-(t1567001))
- [Cloud Storage Exfil (T1567.002)](#cloud-storage-exfil-(t1567002))
- [Videotárhely Exfil (T1567.003)](#videotárhely-exfil-(t1567003))
- [Text Storage Exfil (T1567.004)](#text-storage-exfil-(t1567004))
- [Dinamikus felbontás és DGA (T1568)](#dinamikus-felbontás-és-dga-(t1568))
- [Fast Flux és DNS Cache Evasion (T1568.001)](#fast-flux-és-dns-cache-evasion-(t1568001))
- [Domaingenerációs algoritmus (DGA) észlelése (T1568.002)](#domaingenerációs-algoritmus-(dga)-észlelése-(t1568002))
- [DNS számítás és kinyerés (T1568.003)](#dns-számítás-és-kinyerés-(t1568003))
- [High-Fidelity rendszerszolgáltatás-végrehajtás észlelése](#high-fidelity-rendszerszolgáltatás-végrehajtás-észlelése)
- [High-Fidelity Launch Daemon Persistence Detection](#high-fidelity-launch-daemon-persistence-detection)
- [High-Fidelity rendszerszolgáltatás-végrehajtás észlelése (T1569.002)](#high-fidelity-rendszerszolgáltatás-végrehajtás-észlelése-(t1569002))
- [Oldalirányú szerszámátvitel (T1570)](#oldalirányú-szerszámátvitel-(t1570))
- [Nem szabványos C2 port (T1571)](#nem-szabványos-c2-port-(t1571))
- [Protokoll-alagút-észlelés (T1572)](#protokoll-alagút-észlelés-(t1572))
- [Titkosított C2 csatorna (T1573)](#titkosított-c2-csatorna-(t1573))
- [Szimmetrikus titkosítás C2 csatorna (T1573.001)](#szimmetrikus-titkosítás-c2-csatorna-(t1573001))
- [Aszimmetrikus titkosítás C2 (T1573.002)](#aszimmetrikus-titkosítás-c2-(t1573002))
- [Ultra-Pro DLL-eltérítés és oldalsó betöltés észlelése (T1574)](#ultra-pro-dll-eltérítés-és-oldalsó-betöltés-észlelése-(t1574))
- [Ultra-Pro DLL keresési rendelés-eltérítés észlelése (T1574.001)](#ultra-pro-dll-keresési-rendelés-eltérítés-észlelése-(t1574001))
- [Ultra-Pro DLL oldalsó betöltési integritáshiány-észlelés (T1574.002)](#ultra-pro-dll-oldalsó-betöltési-integritáshiány-észlelés-(t1574002))
- [Ultra-Pro Shell konfigurálás és útvonal elfogás (T1574.003)](#ultra-pro-shell-konfigurálás-és-útvonal-elfogás-(t1574003))
- [Ultra-Pro Library Search Order Hijacking & Integrity Gap (T1574.004)](#ultra-pro-library-search-order-hijacking-&-integrity-gap-(t1574004))
- [Ultra-Pro telepítőfájl engedélyek gyengesége (T1574.005)](#ultra-pro-telepítőfájl-engedélyek-gyengesége-(t1574005))
- [Dinamikus linker eltérítés a privilegizált bináris ellen](#dinamikus-linker-eltérítés-a-privilegizált-bináris-ellen)
- [PATH-eltérítés, amely privilegizált bináris végrehajtáshoz vezet](#path-eltérítés-amely-privilegizált-bináris-végrehajtáshoz-vezet)
- [.NET Assembly Search Megrendelés eltérítése User-Writable Directory segítségével](#net-assembly-search-megrendelés-eltérítése-user-writable-directory-segítségével)
- [.NET AppDomainManager eltérítés nem-GAC összeállításon keresztül](#net-appdomainmanager-eltérítés-nem-gac-összeállításon-keresztül)
- [Privilegizált szolgáltatás végrehajtható felülírva a felhasználó által írható helyről](#privilegizált-szolgáltatás-végrehajtható-felülírva-a-felhasználó-által-írható-helyről)
- [Privileged Service ImagePath vagy ServiceDll feltörve a rendszerleíró adatbázison keresztül](#privileged-service-imagepath-vagy-servicedll-feltörve-a-rendszerleíró-adatbázison-keresztül)
- [Exploit-Grade COR_PROFILER eltérítés a User-Writable Profiler DLL-en keresztül](#exploit-grade-cor_profiler-eltérítés-a-user-writable-profiler-dll-en-keresztül)
- [Exploit-grade KernelCallbackTable Manipulation](#exploit-grade-kernelcallbacktable-manipulation)
- [Felhő-infrastruktúra manipulálása (T1578)](#felhő-infrastruktúra-manipulálása-(t1578))
- [Gyanús felhőpéldány létrehozása (T1578.001)](#gyanús-felhőpéldány-létrehozása-(t1578001))
- [Cloud Snapshot Exfiltration (T1578.002)](#cloud-snapshot-exfiltration-(t1578002))
- [Felhőpéldány-megsemmisítés (T1578.003)](#felhőpéldány-megsemmisítés-(t1578003))
- [Felhőkép-szabotázs (T1578.004)](#felhőkép-szabotázs-(t1578004))
- [Cloud Network Security Regression (T1578.005)](#cloud-network-security-regression-(t1578005))
- [Cloud Infrastructure Discovery (T1580)](#cloud-infrastructure-discovery-(t1580))
- [High-Fidelity offensive Infrastructure Provisioning – T1583](#high-fidelity-offensive-infrastructure-provisioning-–-t1583)
- [High-Fidelity VPS infrastruktúra kiépítése – T1583.001](#high-fidelity-vps-infrastruktúra-kiépítése-–-t1583001)
- [Nagy pontosságú automatizált domainregisztráció és -szerzés – T1583.002](#nagy-pontosságú-automatizált-domainregisztráció-és--szerzés-–-t1583002)
- [High-Fidelity Cloud Network (VPC) kiépítése – T1583.003](#high-fidelity-cloud-network-(vpc)-kiépítése-–-t1583003)
- [High-Fidelity szerver nélküli infrastruktúra kiépítés - T1583.004](#high-fidelity-szerver-nélküli-infrastruktúra-kiépítés---t1583004)
- [High-Fidelity botnet infrastruktúra megszerzése – T1583.005](#high-fidelity-botnet-infrastruktúra-megszerzése-–-t1583005)
- [High-Fidelity webszolgáltatás beszerzése és kiépítése – T1583.006](#high-fidelity-webszolgáltatás-beszerzése-és-kiépítése-–-t1583006)
- [High-Fidelity szerver nélküli infrastruktúra kiépítés - T1583.007](#high-fidelity-szerver-nélküli-infrastruktúra-kiépítés---t1583007)
- [High-Fidelity Cloud-fiókszerzés és rendszerindítás – T1583.008](#high-fidelity-cloud-fiókszerzés-és-rendszerindítás-–-t1583008)
- [High-Fidelity kompromittált infrastruktúra és erőforrás-visszaélés – T1584](#high-fidelity-kompromittált-infrastruktúra-és-erőforrás-visszaélés-–-t1584)
- [Nagy pontosságú tartományi infrastruktúra eltérítése – T1584.001](#nagy-pontosságú-tartományi-infrastruktúra-eltérítése-–-t1584001)
- [Nagy pontosságú DNS-kiszolgáló konfigurációs szubverzió – T1584.002](#nagy-pontosságú-dns-kiszolgáló-konfigurációs-szubverzió-–-t1584002)
- [High-Fidelity Cloud Identity Felforgatás és tartósság – T1584.003](#high-fidelity-cloud-identity-felforgatás-és-tartósság-–-t1584003)
- [High-Fidelity Serverless Function Subversion – T1584.004](#high-fidelity-serverless-function-subversion-–-t1584004)
- [High-Fidelity Botnet Agent Perzisztencia és ellenőrzés – T1584.005](#high-fidelity-botnet-agent-perzisztencia-és-ellenőrzés-–-t1584005)
- [High-Fidelity Web Service és Cloud Storage Subversion – T1584.006](#high-fidelity-web-service-és-cloud-storage-subversion-–-t1584006)
- [High-Fidelity VPS vezérlés és alagút - T1584.007](#high-fidelity-vps-vezérlés-és-alagút---t1584007)
- [Gyanús felhasználói fiók létrehozása CLI/Scripting segítségével](#gyanús-felhasználói-fiók-létrehozása-cliscripting-segítségével)
- [Lehetséges automatizált közösségimédia-fiók létrehozása](#lehetséges-automatizált-közösségimédia-fiók-létrehozása)
- [Lopakodó e-mail fiók létrehozása és manipulálása](#lopakodó-e-mail-fiók-létrehozása-és-manipulálása)
- [Rendellenes Cloud felhasználói fiók létrehozása](#rendellenes-cloud-felhasználói-fiók-létrehozása)
- [Nagy pontosságú fiókkompromittálódás és személyazonosság-manipuláció - T1586](#nagy-pontosságú-fiókkompromittálódás-és-személyazonosság-manipuláció---t1586)
- [High-Fidelity automatizált közösségi média manipuláció - T1586.001](#high-fidelity-automatizált-közösségi-média-manipuláció---t1586001)
- [High-Fidelity e-mail továbbítási szabály manipulációja – T1586.002](#high-fidelity-e-mail-továbbítási-szabály-manipulációja-–-t1586002)
- [High-Fidelity Cloud-fiók átvétele és fennmaradása – T1586.003](#high-fidelity-cloud-fiók-átvétele-és-fennmaradása-–-t1586003)
- [High-Fidelity offenzív képességfejlesztés és összeállítás - T1587](#high-fidelity-offenzív-képességfejlesztés-és-összeállítás---t1587)
- [High-Fidelity kártevő-fejlesztési és kijátszási minták – T1587.001](#high-fidelity-kártevő-fejlesztési-és-kijátszási-minták-–-t1587001)
- [High-Fidelity jogosulatlan kódaláírási képesség fejlesztése - T1587.002](#high-fidelity-jogosulatlan-kódaláírási-képesség-fejlesztése---t1587002)
- [High-Fidelity jogosulatlan digitális tanúsítvány fejlesztés - T1587.003](#high-fidelity-jogosulatlan-digitális-tanúsítvány-fejlesztés---t1587003)
- [High-Fidelity exploit fejlesztés és fordítás észlelése - T1587.004](#high-fidelity-exploit-fejlesztés-és-fordítás-észlelése---t1587004)
- [Támadó képességek rendellenes beszerzése](#támadó-képességek-rendellenes-beszerzése)
- [A rosszindulatú programok rendellenes beszerzése](#a-rosszindulatú-programok-rendellenes-beszerzése)
- [Rendellenes támadóeszköz-beszerzés CLI-n keresztül](#rendellenes-támadóeszköz-beszerzés-cli-n-keresztül)
- [Rendellenes kód aláíró tanúsítvány exportálása vagy beszerzése](#rendellenes-kód-aláíró-tanúsítvány-exportálása-vagy-beszerzése)
- [Stratégiai megbízható gyökértanúsítvány-tárolási manipuláció](#stratégiai-megbízható-gyökértanúsítvány-tárolási-manipuláció)
- [Az Exploit vagy PoC kód rendellenes beszerzése](#az-exploit-vagy-poc-kód-rendellenes-beszerzése)
- [A sérülékenységkutatási műtermékek célzott begyűjtése](#a-sérülékenységkutatási-műtermékek-célzott-begyűjtése)
- [Nagy pontosságú identitásfelsorolás hitelesítési végpontokon keresztül](#nagy-pontosságú-identitásfelsorolás-hitelesítési-végpontokon-keresztül)
- [Hitelesítési adatok felsorolása Authentication API-n keresztül (magas megbízhatóság)](#hitelesítési-adatok-felsorolása-authentication-api-n-keresztül-(magas-megbízhatóság))
- [Magas megbízhatóságú OSINT identitásfeltárás nyilvános API-kon keresztül](#magas-megbízhatóságú-osint-identitásfeltárás-nyilvános-api-kon-keresztül)
- [Nyitott webhelyek és tartományok célzott OSINT felsorolása](#nyitott-webhelyek-és-tartományok-célzott-osint-felsorolása)
- [Hálózati felderítés magas kikötői sokféleséggel](#hálózati-felderítés-magas-kikötői-sokféleséggel)
- [Professzionális IP infrastruktúra felderítés - T1590.001](#professzionális-ip-infrastruktúra-felderítés---t1590001)
- [Advanced DNS Infrastructure Reconnaissance – T1590.002](#advanced-dns-infrastructure-reconnaissance-–-t1590002)
- [Advanced Network Trust Dependencies Reconnaissance – T1590.003](#advanced-network-trust-dependencies-reconnaissance-–-t1590003)
- [Advanced Certificate Information Reconnaissance – T1590.004](#advanced-certificate-information-reconnaissance-–-t1590004)
- [Advanced Cloud Infrastructure Reconnaissance – T1590.005](#advanced-cloud-infrastructure-reconnaissance-–-t1590005)
- [Advanced Victim Web Page Info Reconnaissance - T1590.006](#advanced-victim-web-page-info-reconnaissance---t1590006)
- [Fejlett szervezeti infrastruktúra felsorolása - T1591](#fejlett-szervezeti-infrastruktúra-felsorolása---t1591)
- [Haladó fizikai hely-infrastruktúra felsorolása – T1591.001](#haladó-fizikai-hely-infrastruktúra-felsorolása-–-t1591001)
- [Advanced Business Relationship Information Discovery – T1591.002](#advanced-business-relationship-information-discovery-–-t1591002)
- [Advanced Knowledge Management Discovery – T1591.003](#advanced-knowledge-management-discovery-–-t1591003)
- [Nagy pontosságú személyi információk felfedezése – T1591.004](#nagy-pontosságú-személyi-információk-felfedezése-–-t1591004)
- [High-Fidelity Host Information Reconnaissance Activity](#high-fidelity-host-information-reconnaissance-activity)
- [Magas megbízhatóságú hardverfelsorolás kezelőfelületeken keresztül](#magas-megbízhatóságú-hardverfelsorolás-kezelőfelületeken-keresztül)
- [Fejlett szoftverfelsorolási felderítés webes végpontokon keresztül](#fejlett-szoftverfelsorolási-felderítés-webes-végpontokon-keresztül)
- [Magas megbízhatóságú firmware-felsorolás a hálózati eszközökkel szemben](#magas-megbízhatóságú-firmware-felsorolás-a-hálózati-eszközökkel-szemben)
- [Nagy biztonságú ügyfélkonfigurációs ujjlenyomat (felderítés)](#nagy-biztonságú-ügyfélkonfigurációs-ujjlenyomat-(felderítés))
- [High-Fidelity automatizált webes felderítés - T1593](#high-fidelity-automatizált-webes-felderítés---t1593)
- [High-Fidelity Social Media Entity Harvesting – T1593.001](#high-fidelity-social-media-entity-harvesting-–-t1593001)
- [High-Fidelity automatizált keresőmotor felderítés - T1593.002](#high-fidelity-automatizált-keresőmotor-felderítés---t1593002)
- [High-Fidelity Social Media Entity Harvesting – T1593.003](#high-fidelity-social-media-entity-harvesting-–-t1593003)
- [High-Fidelity Information Repository Reconnaissance - T1594](#high-fidelity-information-repository-reconnaissance---t1594)
- [Nagy pontosságú aktív szkennelés észlelése (viselkedés alapú)](#nagy-pontosságú-aktív-szkennelés-észlelése-(viselkedés-alapú))
- [High-Fidelity külső IP-blokk szkennelés észlelése](#high-fidelity-külső-ip-blokk-szkennelés-észlelése)
- [Nagy biztonságú külső sebezhetőség vizsgálati tevékenység](#nagy-biztonságú-külső-sebezhetőség-vizsgálati-tevékenység)
- [Aktív szólista vizsgálat a hitelesítési végpontok ellen](#aktív-szólista-vizsgálat-a-hitelesítési-végpontok-ellen)
- [High-Fidelity Open Technical Database felderítés - T1596](#high-fidelity-open-technical-database-felderítés---t1596)
- [High-Fidelity WHOIS adatbázis-felderítés – T1596.001](#high-fidelity-whois-adatbázis-felderítés-–-t1596001)
- [High-Fidelity automatizált keresőmotor Dorking - T1596.002](#high-fidelity-automatizált-keresőmotor-dorking---t1596002)
- [High-Fidelity passzív DNS-felderítés – T1597.003](#high-fidelity-passzív-dns-felderítés-–-t1597003)
- [High-Fidelity digitális tanúsítvány felderítés - T1596.004](#high-fidelity-digitális-tanúsítvány-felderítés---t1596004)
- [High-Fidelity IP infrastruktúra felderítés - T1596.005](#high-fidelity-ip-infrastruktúra-felderítés---t1596005)
- [High-Fidelity áldozat tulajdonában lévő webhely-felderítés - T1597](#high-fidelity-áldozat-tulajdonában-lévő-webhely-felderítés---t1597)
- [High-Fidelity Domain Infrastructure Enumeration – T1597.001](#high-fidelity-domain-infrastructure-enumeration-–-t1597001)
- [High-Fidelity titkos vadászat kódtárolókban - T1597.002](#high-fidelity-titkos-vadászat-kódtárolókban---t1597002)
- [Speciális adathalászat információk és hitelesítő adatok begyűjtése céljából – T1598](#speciális-adathalászat-információk-és-hitelesítő-adatok-begyűjtése-céljából-–-t1598)
- [Advanced Spearphishing Link átirányítás – T1598.001](#advanced-spearphishing-link-átirányítás-–-t1598001)
- [Speciális BEC levelezési és pénzügyi adatok kiszűrése – T1598.002](#speciális-bec-levelezési-és-pénzügyi-adatok-kiszűrése-–-t1598002)
- [High-Fidelity MFA/OTP hamisítás és betakarítás – T1598.003](#high-fidelity-mfaotp-hamisítás-és-betakarítás-–-t1598003)
- [High-Fidelity Spearphishing Attachment Interaction – T1598.004](#high-fidelity-spearphishing-attachment-interaction-–-t1598004)
- [Hálózati határok áthidalása (T1599)](#hálózati-határok-áthidalása-(t1599))
- [Logikai leválasztás bypass (T1599.001)](#logikai-leválasztás-bypass-(t1599001))
- [Gyengítési kísérlet (T1600)](#gyengítési-kísérlet-(t1600))
- [Rendszerkép javítás (T1600.001)](#rendszerkép-javítás-(t1600001))
- [Entitásellenőrzés letiltása (T1600.002)](#entitásellenőrzés-letiltása-(t1600002))
- [Hálózati operációs rendszer képmódosítása (T1601)](#hálózati-operációs-rendszer-képmódosítása-(t1601))
- [Hálózati bináris javítás (T1601.001)](#hálózati-bináris-javítás-(t1601001))
- [Ultra-Pro High-Fidelity rosszindulatú hálózati operációs rendszer frissítése (T1601.002)](#ultra-pro-high-fidelity-rosszindulatú-hálózati-operációs-rendszer-frissítése-(t1601002))
- [Hálózati megosztás automatizált adatgyűjtés (T1602)](#hálózati-megosztás-automatizált-adatgyűjtés-(t1602))
- [Admin Share Data Exfiltration (T1602.001)](#admin-share-data-exfiltration-(t1602001))
- [Ultra-Pro High-Fidelity Cloud Share Exfiltration (T1602.002)](#ultra-pro-high-fidelity-cloud-share-exfiltration-(t1602002))
- [Ultra-Pro High-Fidelity webes token és hitelesítő adatok hamisítása (T1606)](#ultra-pro-high-fidelity-webes-token-és-hitelesítő-adatok-hamisítása-(t1606))
- [Ultra-Pro High-Fidelity webes cookie-k és böngésző hitelesítő adatok begyűjtése (T1606.001)](#ultra-pro-high-fidelity-webes-cookie-k-és-böngésző-hitelesítő-adatok-begyűjtése-(t1606001))
- [Ultra-Pro High-Fidelity webes token hamisítás és Golden SAML (T1606.002)](#ultra-pro-high-fidelity-webes-token-hamisítás-és-golden-saml-(t1606002))
- [Rendellenes infrastruktúra szakaszolás és erőforrás-kihelyezés](#rendellenes-infrastruktúra-szakaszolás-és-erőforrás-kihelyezés)
- [Rendellenes rosszindulatú programok áthelyezése a külső infrastruktúrába](#rendellenes-rosszindulatú-programok-áthelyezése-a-külső-infrastruktúrába)
- [Rendellenes támadóeszköz-beállítás és külső feltöltés](#rendellenes-támadóeszköz-beállítás-és-külső-feltöltés)
- [Stratégiai digitális tanúsítvány elhelyezése a Trusted Root Store-ban](#stratégiai-digitális-tanúsítvány-elhelyezése-a-trusted-root-store-ban)
- [Rendellenes webtartalom-módosítás a Drive-by Staging számára](#rendellenes-webtartalom-módosítás-a-drive-by-staging-számára)
- [Rosszindulatú linkcélok stratégiai állomásoztatása](#rosszindulatú-linkcélok-stratégiai-állomásoztatása)
- [Rendellenes SEO-mérgezés és metaadat-stopolás](#rendellenes-seo-mérgezés-és-metaadat-stopolás)
- [High-Fidelity Container interaktív shell végrehajtás](#high-fidelity-container-interaktív-shell-végrehajtás)
- [Nagy pontosságú rosszindulatú tárolótelepítés-észlelés](#nagy-pontosságú-rosszindulatú-tárolótelepítés-észlelés)
- [Ultra-Pro Container Escape & Host Access (T1611)](#ultra-pro-container-escape-&-host-access-(t1611))
- [Ultra-Pro Stealthy Local Image Build (T1612)](#ultra-pro-stealthy-local-image-build-(t1612))
- [Ultra-Pro High-Fidelity tároló és Kubernetes Discovery](#ultra-pro-high-fidelity-tároló-és-kubernetes-discovery)
- [High-Fidelity rendszer helymeghatározás és regionális Kill-Switch felfedezés](#high-fidelity-rendszer-helymeghatározás-és-regionális-kill-switch-felfedezés)
- [High-Fidelity rendszernyelv és billentyűzetkiosztás felfedezése](#high-fidelity-rendszernyelv-és-billentyűzetkiosztás-felfedezése)
- [Nagy pontosságú csoportházirend-felderítés észlelése](#nagy-pontosságú-csoportházirend-felderítés-észlelése)
- [Nagy pontosságú felhőalapú tárolási objektumfelderítés](#nagy-pontosságú-felhőalapú-tárolási-objektumfelderítés)
- [Nagy pontosságú tükröző kód betöltése és a memóriába épített összeállítás végrehajtása](#nagy-pontosságú-tükröző-kód-betöltése-és-a-memóriába-épített-összeállítás-végrehajtása)
- [Gyanús MFA azonnali bombázás vagy hitelesítési árvíz automatizálás](#gyanús-mfa-azonnali-bombázás-vagy-hitelesítési-árvíz-automatizálás)
- [Gyanús Anti-Debug API-hozzáférés nem támogatott vagy felhasználói memóriaterületről](#gyanús-anti-debug-api-hozzáférés-nem-támogatott-vagy-felhasználói-memóriaterületről)
- [Gyanús macOS LaunchAgent vagy LaunchDaemon Plist módosítás](#gyanús-macos-launchagent-vagy-launchdaemon-plist-módosítás)
- [High-Fidelity szerver nélküli funkció tartósság vagy visszaélés](#high-fidelity-szerver-nélküli-funkció-tartósság-vagy-visszaélés)
- [Gyanús tanúsítvány és privát kulcs exportálása vagy lopási tevékenység](#gyanús-tanúsítvány-és-privát-kulcs-exportálása-vagy-lopási-tevékenység)
- [High-Fidelity Cloud-fiók megszerzése és inicializálása – T1650](#high-fidelity-cloud-fiók-megszerzése-és-inicializálása-–-t1650)
- [High-Fidelity Cloud Administration Agent Agent Abuse](#high-fidelity-cloud-administration-agent-agent-abuse)
- [Gyanús eszközillesztő-felsorolás rendellenes kontextusból (BYOVD Recon)](#gyanús-eszközillesztő-felsorolás-rendellenes-kontextusból-(byovd-recon))
- [Ultra-Pro teljesítménybeállítások kezelése (T1137.001)](#ultra-pro-teljesítménybeállítások-kezelése-(t1137001))
- [Gyanús eseménynapló felsorolása rendellenes végrehajtási kontextusból](#gyanús-eseménynapló-felsorolása-rendellenes-végrehajtási-kontextusból)
- [Gyanús megszemélyesítés RunAs visszaélésen vagy megtévesztő helyi fiók létrehozásán keresztül](#gyanús-megszemélyesítés-runas-visszaélésen-vagy-megtévesztő-helyi-fiók-létrehozásán-keresztül)
- [Gyanús vágólap-manipuláció és pénzügyi dokumentumokhoz való hozzáférés nem megbízható szülői folyamatból](#gyanús-vágólap-manipuláció-és-pénzügyi-dokumentumokhoz-való-hozzáférés-nem-megbízható-szülői-folyamatból)
- [Professzionális tartalom megszemélyesítése és infrastruktúra tükrözése](#professzionális-tartalom-megszemélyesítése-és-infrastruktúra-tükrözése)
- [Gyanús hozzáférés az LSASS folyamatmemóriához (hitelesítő adatok kiürítési kísérlete)](#gyanús-hozzáférés-az-lsass-folyamatmemóriához-(hitelesítő-adatok-kiürítési-kísérlete))

---
## Ultra-Pro High-Fidelity szteganográfia és adatrekonstrukció (T1001)
- **ID:** `T1001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A rendellenes programozott hozzáférés azonosításával észleli az adatok desztiganográfiáját
képmanipulációs API-khoz (GDI+, System.Drawing) a szkript értelmezőktől,
kifejezetten pixel szintű adatkinyerési rutinokat keres.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity levélszemét adat és parancstömítés (T1001.001)
- **ID:** `T1001_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Az anomáliák azonosításával észleli a parancsok kitöltését és a kéretlen adatinjektálást
téreloszlás, ismétlődő környezeti változó-definíciók,
és rendkívül hosszú parancssori nem telepítő folyamatokban.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity szteganográfia és adatrekonstrukció (T1001.002)
- **ID:** `T1001_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A rendellenes programozott hozzáférés azonosításával észleli az adatok desztiganográfiáját
képmanipulációs API-khoz (GDI+, System.Drawing) a szkript értelmezőktől,
kifejezetten pixel szintű adatkinyerési rutinokat keres.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity Protocol megszemélyesítés (T1001.003)
- **ID:** `T1001_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a protokoll megszemélyesítését a hálózati fejlécek kézi manipulációjának azonosításával
és a rendellenes User-Agent karakterláncok a script interpreterekben, különösen
a nem böngésző folyamatokból származó mobileszközök vagy feltérképező robotok utánzására irányuló kísérletek célzása.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity LSASS hitelesítő adatok dömping (T1003)
- **ID:** `T1003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rendkívül kifinomult LSASS memóriadömping technikákat.
A DLL export sorszámára (#24), a duplikáció kezelésére,
és speciális LOLBin-ek, amelyek megkerülik a szabványos EDR karakterlánc-alapú észlelést.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús hozzáférés az LSASS folyamatmemóriához
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
- **Leírás:** Érzékeli a SAM, a SYSTEM és a SECURITY nyilvántartási kaptárak jogosulatlan kibontását.
A „reg.exe” visszaélésre, a VSS-alapú lopásra és az „esentutl.exe” fájlok másolására összpontosít
nem szabványos szülőfolyamatokból és nem megbízható végrehajtási útvonalakból.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity NTDS.dit kivonás (T1003.003)
- **ID:** `T1003_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [DISKSHADOW.EXE](https://lolbas-project.github.io/lolbas/), [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [NTDSUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az Active Directory adatbázis (NTDS.dit) jogosulatlan kibontását.
Az 'ntdsutil'-t rövidített parancsokkal, diskshadow szkriptekkel azonosítja,
és árnyékmásolat létrehozása nem biztonsági mentési folyamatokkal a tartományvezérlőkön.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity LSA titkok és biztonsági kaptárlopás (T1003.004)
- **ID:** `T1003_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az LSA-titkok jogosulatlan kimásolását a HKLM\SECURITY rendszerleíró adatbázisból.
A fejlett exportmintákra, az Impacket-stílusú távoli dumpokra és a
hitelesítő adatokhoz való hozzáférés nem megbízható szülői folyamatokon keresztül.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity MSCASH/DCC extrakció (T1003.005)
- **ID:** `T1003_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyorsítótárazott tartományi hitelesítő adatok (MSCASH/DCC) jogosulatlan kibontását.
Figyeli a speciális eszközök ujjlenyomatait, a rendszerleíró adatbázis mentési műveleteinek célzását
a gyorsítótár kulcs és a rendellenes szülő-gyermek folyamatkapcsolatok.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity DCSync támadásészlelés (T1003.006)
- **ID:** `T1003_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a DCSync támadásokat, amikor a támadó tartományvezérlőnek adja ki magát
hitelesítő adatokat kérni.Konkrét RPC-jelzőkre, rövidített eszközparancsokra összpontosít,
és rendellenes folyamatvonal a nem egyenáramú eszközökön.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity LSASS memória kiíratása és LOLBin visszaélés (T1003.007)
- **ID:** `T1003_007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kifinomult LSASS memória kiürítést.A Procdump argumentummintáira összpontosít,
Feladatkezelő által kezdeményezett kiíratások a WerFaulton keresztül, és COM+ (comsvcs.dll) exportálás
sorszám alapú hívások (#24) a karakterlánc-alapú észlelés megkerülésére.

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
- **Leírás:** Érzékeli az /etc/shadow fájl jogosulatlan kibontását.
A gyanús útvonalakra való átirányításra, archiválásra,
és kiszűrés hálózati eszközökön (LOLBins) keresztül interaktív héjakból.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Helyi adatgyűjtés (T1005)
- **ID:** `T1005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szisztematikus helyi adatgyűjtést a rekurzív fájlfelderítés azonosításával,
az érzékeny kiterjesztések célzása, valamint a nem szabványos kereső- vagy tömörítőeszközök használata
gyanús folyamatvonalakból.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lopakodó közvetlen hangerő-hozzáférés (T1006)
- **ID:** `T1006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy pontosságú közvetlen kötet-hozzáférést a nyers eszközútvonalak figyelésével
rendszeren kívüli folyamatok vagy gyanús szülők kezdeményezték.Gyakran megkerülésére használják
fájlrendszer-zárak és EDR-figyelés a hitelesítő adatok kiürítéséhez.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendszerszolgáltatás-felderítés (T1007)
- **ID:** `T1007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rendszerszolgáltatások célzott felfedezését.A gyanús szülői folyamatokra összpontosít
és a biztonsági termékek azonosítására használt specifikus parancssori argumentumok ill
rosszul konfigurált szolgáltatások a jogosultságok kiterjesztéséhez.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Tartalékcsatorna-észlelés (T1008)
- **ID:** `T1008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Felismeri a C2 tartalék mechanizmusait a protokollok közötti kapcsolási logika azonosításával
(pl. HTTP-ről DNS-re/ICMP-re) a kivételkezelési blokkon belül (try/catch/trap)
nem szabványos folyamatkörnyezetben előforduló csatlakozási hibák váltják ki.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Alkalmazásablak felfedezése (T1010)
- **ID:** `T1010.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A .NET figyelésével észleli a jogosulatlan alkalmazásablak-felderítést
MainWindowTitle tulajdonság elérése és Win32 API hívások CLI-n keresztül.
A nem szabványos vonalakra és a rosszindulatú programok által az ablakcímek kiszivárgására használt kimeneti átirányításokra összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Bluetooth Exfiltration (T1011)
- **ID:** `T1011.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A programozott azonosítással észleli a jogosulatlan Bluetooth-adatok kiszűrését
a nem szabványos Bluetooth átviteli varázslók (fsquirt.exe) kioldói
szülőfolyamatok vagy a rádióvezérlő eszközök gyanús parancssori végrehajtásai.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## BLE Advertising Exfiltration (T1011.001)
- **ID:** `T1011_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Azonosítással észleli a titkos adatszivárgást a BLE hirdetési kereteken keresztül
jogosulatlan folyamatok, amelyek WinRT BluetoothLEAdvertisementPublishert hívnak meg
API-k az egyéni gyártói adatátvitelhez.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Registry Discovery lekérdezése (T1012)
- **ID:** `T1012.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az érzékeny biztonsági konfigurációkat célzó rendszerleíró adatbázis-felderítést,
hitelesítő adatok tárolása és perzisztencia útvonalai.Rekurzív lekérdezésészlelést használ
és integritási szintű kapuzás a téves pozitívumok minimalizálása érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## BYOVD Rootkit betöltése (T1014)
- **ID:** `T1014.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a "Bring Your Own Vulnerable Driver" (BYOVD) technikát.
Az ismert illesztőprogram-betöltők végrehajtására vagy a kernel-mód regisztrációjára összpontosít
szolgáltatások nem szabványos útvonalakról, miközben kiszűri a jogos operációs rendszer-illesztőprogram-karbantartást.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendszerhálózati konfiguráció felfedezése (T1016)
- **ID:** `T1016.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a hálózati konfiguráció (IP, útválasztás, DNS, ARP) szisztematikus felfedezését.
Integritás segítségével kiszűri a VPN-kliensekből és a rendszerszolgáltatásokból származó nagy mennyiségű zajt
szintek, szülőfolyamatok kapuzása és parancssori kapcsolóelemzés.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Internet IP-felderítés (T1016.001)
- **ID:** `T1016_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Parancssori eszközök segítségével észleli a rendszer külső IP-címének felderítését
és általános IP-visszhangszolgáltatások.A szülő-gyermek elemzésével minimalizálja a hamis pozitív eredményeket
folyamatkapcsolat, integritási szintek és tipikus fejlesztői eszköz ujjlenyomatok.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Terminálszolgáltatások konfigurációs felderítése (T1016.002)
- **ID:** `T1016_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a terminálszolgáltatások és az RDP-konfigurációk célzott felfedezését.
A nem szabványos folyamatvonalakra összpontosít (pl. Office, Browsers) és
észleli az eltéríthető munkamenetek azonosítására használt parancssori kapcsolókat
vagy letiltotta a biztonsági beállításokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Remote System Discovery (T1018)
- **ID:** `T1018.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szisztematikus távoli rendszerfelderítést, a tartományvezérlő azonosítására összpontosítva
és hálózati topológia leképezés.Kiszűri a rendszerszolgáltatásokból származó nagy mennyiségű zajt,
böngészők és készletügynökök integritási szinteket és szülőfolyamat kapuzást használva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Automatizált szűrés (T1020)
- **ID:** `T1020.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli az automatikus kiszűrést azáltal, hogy azonosítja a szekvenciális mintát
jelszóval védett archiválás, majd azonnali hálózati átvitel
nem szabványos eszközök vagy felhőszinkronizáló binárisok gyanús helyekről.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Client-Linked Cloud Exfil (T1020.001)
- **ID:** `T1020_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Az adatok kiszűrését észleli a hivatalos felhőalapú tárolási ügyfelek azonosításával
(OneDrive, Dropbox, Google Drive, Box) a parancssoron keresztül manipulálható
a nem szabványos állomásoztatási könyvtárak szinkronizálásához vagy a nagy entrópiájú/script argumentumokkal való futtatáshoz.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyors bejelentkezés több távoli gépre ugyanazon felhasználó által
- **ID:** `T1021.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli, hogy egy felhasználó rövid időn belül sikeresen bejelentkezik több különböző gazdagépre.Ez a viselkedés ellopott hitelesítő adatokra, átengedésre vagy oldalirányú mozgásra utalhat érvényes fiókok használatával.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**


---
## Gyanús RDP bejelentkezés szokatlan forrásból
- **ID:** `T1021_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a szokatlan vagy nem vállalati forrásból származó sikeres RDP-bejelentkezéseket, különösen, ha kiszolgálókat céloz meg, és nem rendszergazdai vagy ritkán használt fiókok hajtják végre.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**


---
## SMB Admin Share Mapping (T1021.002)
- **ID:** `T1021_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Célzott hozzáférést észlel a rendszergazdai megosztásokhoz (C$, ADMIN$, IPC$) a használatával
natív eszközöket (net.exe, PowerShell), miközben kiszűri a szabványos IT-t
hangszerelés és szolgáltatási szintű zaj.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## DCOM távoli végrehajtás (T1021.003)
- **ID:** `T1021_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [VISIO.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az oldalirányú mozgást a DCOM-on keresztül a gyanús gyermekfolyamatok figyelésével
ismert sebezhető COM-objektumokból.Kifejezetten fej nélküli szűrők
végrehajtás és rendellenes hálózat-folyamat vonal.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## SSH Lateral Movement & Tunneling (T1021.004)
- **ID:** `T1021_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [SSH.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fejlett SSH oldalirányú mozgást és alagútképzést.A szűrők jogosak
A DevOps/Git tevékenység a szülőfolyamat vonalának, parancssoros elemzésével
entrópia és nem szabványos hitelesítési minták.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## VNC oldalirányú mozgás és eltérítés (T1021.005)
- **ID:** `T1021_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A hordozható VNC-végrehajtás figyelésével észleli a jogosulatlan VNC-tevékenységet
a gyanús útvonalaktól, a fordított kapcsolódási kísérletektől és a parancssortól
hitelesítő adatok beadása a vállalati távoli támogatási eszközök szűrése közben.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## WinRM távoli végrehajtás (T1021.006)
- **ID:** `T1021_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fejlett oldalirányú mozgást a WinRM segítségével a nagy entrópia figyelésével
PowerShell-parancsok, a memórián belüli végrehajtás és a gyanús folyamatok
a WinRM gazdafolyamatból származó üreges kísérletek.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Felhővezérlő sík eltérítése (T1021.007)
- **ID:** `T1021_007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Felhő-műszerfalakon keresztül korrelálással észleli az illetéktelen oldalirányú mozgást
nagy kockázatú műveletek rendellenes felhasználói ügynökökkel, szokatlan forrás IP-címekkel és
az MFA-elkerülés vagy az automatizált munkamenet-eltérítés jelei.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## macOS ARD távoli eltérítés (T1021.008)
- **ID:** `T1021_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli az Apple Remote Desktop (ARD) jogosulatlan aktiválását vagy módosítását
a „kickstart” segédprogram figyelésével a magas kockázatú jelzők esetében, amelyek engedélyezik
univerzális hozzáférés, miközben szűri a legitim MDM (Jamf, Kandji) hangszerelést.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cserélhető adathordozó adatlopás (T1025)
- **ID:** `T1025.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szisztematikus és automatizált adatgyűjtést cserélhető adathordozóról (USB/Külső meghajtók)
rekurzív felderítési minták, specifikus archiválási kapcsolók azonosításával és
gyanús folyamatvonalakat, miközben kiszűri a szabványos operációs rendszertevékenységeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús Base64 kódolású PowerShell-parancs hálózati tevékenységgel
- **ID:** `T1027.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a PowerShell-végrehajtásokat Base64-kódolású parancsokkal, hálózat alapú hasznos adatlekéréssel és nem interaktív végrehajtással kombinálva.Ez a minta erősen összefügg a rosszindulatú programok kézbesítésével, a betöltőkkel és a kizsákmányolás utáni keretrendszerekkel.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Bináris kitöltési tevékenység (T1027.001)
- **ID:** `T1027_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rosszindulatú bináris kitöltési kísérleteket, ahol a támadók mesterségesen növelik a fájlméretet, hogy megkerüljék a biztonsági szkennereket vagy módosítsák a fájlkivonatokat.Az fsutil, dd és bináris másolási parancsokra összpontosít, amelyek a gyanús könyvtárakban lévő végrehajtható fájlokat és rendszerfájlokat célozzák meg, miközben szűri a törvényes rendszerműveleteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szoftvercsomagolási esemény (T1027.002)
- **ID:** `T1027_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a bináris csomagolók (UPX, MPRESS, ASPack stb.) használatát nem szabványos vagy gyanús környezetben.A nagy tömörítési és elfedési parancssori mintákra, valamint a gyanús szülőfolyamatokra összpontosít, miközben szűri a jogszerű fejlesztéseket és a CI/CD munkafolyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szteganográfia hasznos teher kivonás (T1027.003)
- **ID:** `T1027_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a rejtett hasznos anyagok programozott kivonását a képfájlokból.Azokra a munkafolyamatokra összpontosít, amelyek kombinálják a pixel szintű adathozzáférést (GDI+) a dinamikus kódvégrehajtással Reflection vagy Invoke-Expression (IEX) segítségével ugyanabban a folyamatkörnyezetben, miközben szűri a megbízható grafikus eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szteganográfia hasznos teher kivonás (T1027.004)
- **ID:** `T1027_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Alacsony szintű GDI+ vagy .NET Bitmap metódusokkal észleli a rosszindulatú rakományok kibontását a képfájlokból.Az Invoke-PSImage vagy hasonló szteganográfiai keretrendszerre összpontosít, miközben szűri a jogos képmanipulációs szoftvereket és rendszerfolyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Jelző eltávolítása és aláíráslopás (T1027.005)
- **ID:** `T1027_005.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a binárisokon lévő indikátorok eltávolítására vagy a digitális aláírások manipulálására irányuló kísérleteket.Az aláíráslopásra (SigThief), a PE-fejlécek eltávolítására és a karakterláncok cseréjére összpontosít gyanús végrehajtási környezetben.Optimalizált, hogy csökkentse a törvényes építési eszközökből és fejlesztői környezetekből származó hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## HTML-csempészet végrehajtása (T1027.006)
- **ID:** `T1027_006.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús fájlok végrehajtását, amelyeket általában HTML-csempészeten keresztül szállítanak.Azokra a böngészőfolyamatokra összpontosít, amelyek szkript értelmezőket generálnak, vagy lemezképeket csatolnak ideiglenes vagy helyi alkalmazásadat-könyvtárakból.Optimalizált, hogy csökkentse a törvényes telepítők és frissítések téves pozitívumait.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Bináris szimbólumok eltávolítása (T1027.007)
- **ID:** `T1027_007.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a hibakeresési szimbólumok és a szakaszfejlécek aktív eltávolítását a binárisokból nem build rendszereken, a fejlesztői vagy CI/CD környezeteken kívüli eltávolító eszközök végrehajtására összpontosítva.Optimalizált, hogy csökkentse az engedélyezett építési folyamatokból és fejlesztőrendszerekből származó hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Bináris szimbólumok eltávolítása (T1027.008)
- **ID:** `T1027_008.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a hibakeresési szimbólumok és szakaszfejlécek aktív eltávolítását a binárisokból nem fejlesztői környezetben.Ez akadályozza a kriminalisztikai elemzést és a visszafejtést a függvénynevek és szimbólumtáblázatok eltávolításával.A CI/CD és a fejlesztési környezet kiszűrésére optimalizálva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Beágyazott hasznos teher kivonás (T1027.009)
- **ID:** `T1027_009.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [NGEN.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a beágyazott hasznos adatok kinyerését és végrehajtását csak a memóriát használó kódbetöltés (Reflection), a bájttömb manipuláció és a nem szabványos erőforrás-folyamok segítségével.A szabványos .NET futásidejű és telepítői műveletekből származó téves pozitívumok csökkentésére optimalizálva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Parancssori zavarás (T1027.010)
- **ID:** `T1027_010.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fejlett parancssori homályosítási technikákat, beleértve a túlzott escape-karaktereket, a környezeti változók szeletelését, a PowerShell-karakterlánc-rekonstrukciót és a kódolt parancsokat.A statikus észlelési szűrők megkerülésére optimalizálva, miközben szűri a törvényes telepítőket és a megbízható rendszerkarbantartó eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús archívum létrehozása (T1027.011)
- **ID:** `T1027_011.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MAKECAB.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Jelszóval védett vagy titkosított archívumok létrehozását észleli a szokásos CLI archiváló eszközök segítségével.A parancssori jelszó argumentumaira, a rekurzív műveletekre és a nem szabványos vagy érzékeny útvonalakra történő kimenetekre összpontosít.Kiszűri a jogos felhőalapú tárolást és az engedélyezett alkalmazáshasználatot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows LDR-eltérítés (T1027.012)
- **ID:** `T1027_012.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Windows betöltő (LDR) AppInit_DLL-eken vagy AppCertDLL-eken keresztüli eltérítési kísérleteit.Megcélozza a DLL-regisztrációkat nem rendszerútvonalakról (Temp, Nyilvános, Felhasználói profilok) és a LoadAppInit_DLLs jelző aktiválását gyanús szereplők által.Kiszűri a törvényes telepítőket és a rendszerkarbantartási folyamatokat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ütemezett transzfer (T1029)
- **ID:** `T1029.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az ütemezett feladatok létrehozását az automatikus adatkiszűréshez azáltal, hogy elemzi a Task XML-t a gyanús parancssori eszközök, felhőszinkronizálási argumentumok és nagyfrekvenciás vagy munkaidőn kívüli triggerek keresésére.Kiszűri a jogszerű rendszerfrissítéseket és a vállalatirányítási feladatokat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Adatok darabolása és töredezettsége (T1030)
- **ID:** `T1030.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Az alacsony szintű fájlfolyam-manipuláció, a pufferalapú felosztás, a Base64-konverziók és a nem szabványos archív kötet-létrehozás azonosításával észleli a lopakodó adattöredezési és kiszűrési technikákat.Gyanús végrehajtási útvonalakat céloz meg, miközben szűri a törvényes vállalati szoftvereket és a rendszerautomatizálást.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendszertulajdonos/felhasználó felfedezése (T1033)
- **ID:** `T1033.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az aktuális felhasználó, a bejelentkezett felhasználók és a token jogosultságok szisztematikus felderítését.Rendellenes folyamatsorokat (Office-alkalmazások, böngészők) és gyanús parancssori mintákat (/priv, /groups, /all) céloz meg, amelyeket gyakran használnak a jogosultság-kiterjesztési kísérletek előtt.Kiszűri a jogszerű rendszerautomatizálást és a vállalatirányítási zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Maszkolás és visszaélés a folyamat során (T1036)
- **ID:** `T1036.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fejlett maszkolási technikákat, beleértve a rendszer bináris útvonalának anomáliáit, a kettős kiterjesztést, a nem megbízható szülők által létrehozott kritikus rendszerfolyamatokat és a gyanús záró- vagy kezdő szóközöket tartalmazó végrehajtható fájlokat.A jogos Windows Update, a rendszerkarbantartás és az oldalsó betöltési viselkedés kiszűrésére optimalizálva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Érvénytelen vagy hamisított kódaláírás (T1036.001)
- **ID:** `T1036_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a kritikus Windows rendszerfolyamatokat (pl. lsass.exe, svchost.exe), amelyek érvénytelen, nem megbízható vagy hamisított digitális aláírással futnak.Az identitás-aláírás eltéréseire és a kiadói elírásokra összpontosít, miközben kiszűri a jogos aláírt binárisokat és a fejlesztői zajt.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## RTLO karaktervégrehajtás (T1036.002)
- **ID:** `T1036_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jobbról balra felülírás (RTLO) Unicode karaktert (U+202E) tartalmazó folyamatok végrehajtását.Többféle kódolásra és gyanús végrehajtási kontextusokra (Letöltések, Temp) optimalizálva, miközben szűri a rendszer és a fejlesztői zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Átnevezett System Utility Detection (T1036.003)
- **ID:** `T1036_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az átnevezett Windows rendszersegédprogramok (LOLBins) végrehajtását az aktuális folyamatnevek és a belső metaadatok (OriginalFileName) összehasonlításával.Útvonal-alapú szűrést és aláírás-figyelést használ, hogy csökkentse a telepítőktől, a rendszerkarbantartási feladatoktól és a legitim bináris fájloktól származó hamis pozitív üzeneteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Maszkírozás útvonal-anomálián keresztül (T1036.004)
- **ID:** `T1036_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Kifinomult maszkolást észlel, amikor a rendszer bináris fájljait nem megbízható, felhasználó által írható könyvtárakból vagy hamisított rendszerútvonalakból hajtják végre (pl. záró szóköz kitöltése).Kiszűri a legitim Side-by-Side (WinSxS) és Windows Update viselkedéseket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Jogos Windows bináris fájl a felhasználó által írható helyre másolva
- **ID:** `T1036_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogos Windows rendszerbinárisok gyanús másolását a felhasználó által írható könyvtárakba.Ezt a technikát a támadók gyakran használják álcázásra, DLL oldalbetöltésre vagy a végrehajtás kijátszására megbízható bináris nevekkel való visszaéléssel.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szóköz a fájlnév maszkolása után (T1036.006)
- **ID:** `T1036_006.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Szándékos maszkolást észlel a végrehajtható fájlnevekben vagy könyvtárnevekben (pl. "malware.exe") lévő szóközök használatával.Olyan csalásokat céloz meg, amelyek szóközt használnak a karakterlánc-alapú észlelések megkerülésére, miközben kiszűrik a gyakori Windows Update-, SCCM/MECM- és rendszerautomatizálási zajokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Dupla fájlkiterjesztés végrehajtása (T1036.007)
- **ID:** `T1036_007.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a dokumentumoknak álcázott binárisok végrehajtását kettős fájlkiterjesztéseken keresztül (pl. .pdf.exe, .docx.exe).Kiszűri a fejlesztői melléktermékeket (.min.js, .map), a rendszer bináris fájljait és az ellenőrzött telepítőket.A nagy kockázatú felhasználói könyvtárakra és a gyanús szülőfolyamatokra összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Masquerade via tolmács visszaélés (T1036.008)
- **ID:** `T1036_008.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nem egyező fájltípus-végrehajtást, ahol a legitim értelmezők (wscript, cscript, powershell, regsvr32, mshta, rundll32) nem szabványos kiterjesztésű fájlokat hajtanak végre (.jpg, .txt, .png stb.).A nem megbízható felhasználói könyvtárakra és a gyanús szülőfolyamatokra összpontosít, miközben szűri a rendszerszintű automatizálást és a fejlesztői műtermékeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Allure Document & RTLO Maszkírozás Detection
- **ID:** `T1036_009.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az álcázást kettős fájlkiterjesztések és jobbról balra felülbíráló (RTLO - U+202E) karakterek használatával.A felhasználó által írható könyvtárakból vagy gyanús szülőfolyamatokból, például böngészőkből, levelezőkliensekből és archiváló segédprogramokból történő végrehajtásra összpontosít.A fejlesztői és a rendszerzaj csökkentésére tervezték.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú bejelentkezési szkript fennmaradása (T1037)
- **ID:** `T1037.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a bejelentkezési szkriptek létrehozását vagy módosítását a beállításjegyzékben (UserInitMprLogonScript).
A támadók ezt arra használják, hogy megkerüljék a csoportházirend-alapú bejelentkezési szkripteket, és minden bejelentkezéskor rosszindulatú kódot hajtsanak végre.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity UserInitMprLogonScript perzisztencia
- **ID:** `T1037_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a UserInitMprLogonScript rendszerleíró kulcs jogosulatlan létrehozását vagy módosítását.
Ez egy nagy pontosságú szabály, mert kiszűri a szabványos GPO-frissítéseket, és azokra összpontosít
a felhasználó által írható útvonalak és gyanús végrehajtási minták.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Netsh Helper DLL tartósság
- **ID:** `T1037_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli egy új Netsh Helper DLL regisztrációját.
A támadók ezt arra használják, hogy egy rosszindulatú DLL betöltésével fenntartsák a kitartást
amikor a netsh.exe vagy egy kapcsolódó hálózati szolgáltatás elindul.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro hálózati bejelentkezési szkript/parancsikon módosítása (T1037.003)
- **ID:** `T1037_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Érzékeli a szkriptek (.bat, .ps1, .vbs) vagy parancsikonok (.lnk) jogosulatlan módosítását
olyan érzékeny hálózati megosztásokon belül, mint a NETLOGON vagy a SYSVOL.
Kifejezetten kiszűri a jogos DFS-replikációt és a rendszerszintű frissítéseket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro RC Script és Init.d Persistence (T1037.004)
- **ID:** `T1037_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli az RC szkriptek, init.d vagy systemd generátorok nem csomagkezelő folyamatok általi jogosulatlan módosítását.
A támadók ezeket arra használják, hogy Linux/macOS rendszereken root-megtartó képességet szerezzenek.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro macOS indítási elemek tartóssága (T1037.005)
- **ID:** `T1037_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Érzékeli a fájlok jogosulatlan létrehozását a régebbi StartupItems könyvtárakban.
A hivatalos macOS-telepítő engedélyezőlistára helyezésével minimalizálja a hamis pozitívumot
alrendszerben, és az aláíratlan vagy szkript által generált tartósságra összpontosítva.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati megosztások felfedezése és gyűjtése (ATT&CK T1039)
- **ID:** `T1039.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az érzékeny adatok szisztematikus felderítését és gyűjtését a hálózati megosztásokról az UNC-útvonalak rekurzív felsorolásának azonosításával, kombinálva állomásoztatással, kimenet átirányítással, tömörítéssel vagy érzékeny fájltípusok célzásával.A tömeges felfedezésre és a nem adminisztratív vagy gyanús folyamatkörnyezetekből végrehajtott gyűjtési viselkedésre összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati szippantásérzékelés (ATT&CK T1040)
- **ID:** `T1040.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [PKTMON.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan csomagrögzítési és hálózati szippantási tevékenységet a natív Windows rögzítő segédprogramok, harmadik féltől származó szippantási keretrendszerek, csomagelfogó illesztőprogram-telepítési kísérletek és gyanús felhasználói helyekről történő végrehajtás azonosításával.A téves pozitívumok csökkentése érdekében a rögzítési módú meghívásra összpontosít, nem pedig puszta eszköz jelenlétére.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Kiszűrés a C2 csatornán keresztül (ATT&CK T1041)
- **ID:** `T1041.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges adatszivárgást egy létrehozott Command-and-Control (C2) csatornán keresztül a fájl-memória olvasási műveletek, a Base64 kódolás, a tömörítési szakaszolás és a nem szabványos útvonalakról vagy gyanús szülőfolyamatokról végrehajtott, memórián belüli adatfolyam-manipulációk azonosításával.Az egyszerű kimenő forgalom helyett a fokozatos kiszűrési viselkedésre összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati szolgáltatáskeresés (ATT&CK T1046)
- **ID:** `T1046.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szisztematikus belső hálózati szolgáltatás-felderítést és portellenőrzést a hurok alapú felsorolási minták, a magas kockázatú portcélzás és a nem adminisztratív vagy gyanús szülői környezetből végrehajtott ellenőrző segédprogramok azonosításával.Az egyedi interaktív parancsok helyett a szkriptezett oldalsó felderítési tevékenységre összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús távoli folyamat létrehozása a WMIC-en keresztül
- **ID:** `T1047.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a wmic.exe gyanús használatát a távoli gazdagépeken folyamatok létrehozásához a „folyamathívás létrehozása” metódussal.Ezt a technikát általában a támadók használják oldalirányú mozgáshoz a hitelesítő adatokkal kapcsolatos kompromisszumot követően.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Alternatív protokoll-szűrés (ATT&CK T1048)
- **ID:** `T1048.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [SSH.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az alternatív vagy nem szabványos protokollokon (ICMP, SSH-alagút, TCP-relék, DNS-alagútkezelő segédprogramok) keresztül történő esetleges adatszivárgást az alagútjelzők, a rendellenes ICMP-rakományméretek és a gyanús felhasználói térútvonalakról végrehajtott hálózatképes LoLBin-ek azonosításával.A nem interaktív felhasználásra és a jogosultságokkal ellentmondó végrehajtási környezetre összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szimmetrikus titkosított kiszűrés (ATT&CK T1048.001)
- **ID:** `T1048_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [FTP.EXE](https://lolbas-project.github.io/lolbas/), [SFTP.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges titkosított adatok kiszűrését szimmetrikus titkosított protokollokon (SCP, SFTP, Rclone, WinSCP) azáltal, hogy azonosítja az automatizált, nem interaktív feltöltési viselkedéseket, amelyek gyanús végrehajtási útvonalakkal vagy szokatlan szülőfolyamat-vonallal kombinálódnak.A hitelesítő adatok jelzőire, a kötegelt végrehajtásra és a tömeges átviteli műveletekre összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Aszimmetrikus titkosított kiszűrés (ATT&CK T1048.002)
- **ID:** `T1048_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Az aszimmetrikus titkosított protokollokon (HTTPS) keresztül észleli a lehetséges adatszivárgást azáltal, hogy azonosítja a parancssori feltöltési viselkedést (curl, wget, PowerShell, BITS, certutil) a gyanús végrehajtási környezettel vagy szülőfolyamat vonallal kombinálva.Az explicit feltöltési jelzőkre, a nem biztonságos TLS-használatra és a felhasználói tér végrehajtási útvonalaira összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Titkosítatlan protokoll kiszűrése (ATT&CK T1048.003)
- **ID:** `T1048_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a titkosítatlan protokollokon (DNS, ICMP) keresztüli lopakodó adatszivárgást a rendellenes DNS TXT-lekérdezések, a nagy entrópiájú aldomainek, a túlméretezett ICMP hasznos terhelések és a gyanús végrehajtási vonalak (Office/makrók/scriptek) azonosításával.Úgy tervezték, hogy csökkentse a jogszerű adminisztratív használatból származó téves eredményeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendszerhálózati kapcsolatok felderítése (ATT&CK T1049)
- **ID:** `T1049.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az aktív hálózati kapcsolatok és a létrehozott munkamenetek célzott felfedezését.A támadó kereskedelmi eszközökre összpontosít, mint például a fejlett netstat/net használat, a PowerShell hálózati parancsmagok, a gyanús szülőfolyamatok (Office, webszolgáltatások, távoli felügyelet) és az automatizált kimeneti elemzés vagy átirányítás.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Fizikai közeg kiszűrése (ATT&CK T1052)
- **ID:** `T1052.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A nem interaktív másolási, áthelyezési vagy archiválási parancsok figyelésével észleli a célzott adatszivárgást a fizikai adathordozóra (USB/cserélhető lemezekre).A rejtett parancssori zászlókra, a gyanús szülőfolyamatokra összpontosít, és kizárja a jogszerű Windows Intéző és adminisztrátori műveleteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## USB kiszűrésérzékelés (ATT&CK T1052.001)
- **ID:** `T1052_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A nem interaktív fájlmásolási, -áthelyezési és -archiválási műveletek figyelésével észleli a célzott adatszivárgást az USB-/cserélhető meghajtókra.A gyanús parancssori argumentumokra, a rejtett automatizálási jelzőkre és a szokatlan szülőfolyamat-vonalra összpontosít.

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
## High-Fidelity At.exe tevékenységészlelés
- **ID:** `T1053_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Feladatütemezéshez észleli az at.exe végrehajtását.Mivel az „at” elavult,
minden interaktív használat vagy távoli gépcélzás (\\) erősen gyanúsnak minősül
és kitartást vagy oldalirányú mozgást jelez.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cron perzisztencia és helyben történő módosítás
- **ID:** `T1053_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Megfigyeléssel észleli a cron jobok jogosulatlan létrehozását vagy módosítását
közvetlen írások cron könyvtárakba és gyanús shell egysorosokba.
Szűri a jogos csomagkezelőket és konfigurációkezelő eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús ütemezett feladat létrehozása PowerShell végrehajtása során
- **ID:** `T1053_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az ütemezett feladatok gyanús létrehozását a schtasks.exe használatával, amelyek végrehajtják a PowerShell-t, amelyet a támadók gyakran visszaélnek rosszindulatú terhelések tartósságának vagy késleltetett végrehajtásának megállapítására.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Systemd szolgáltatás létrehozása vagy módosítása
- **ID:** `T1053_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a rendszeres szolgáltatási egységek létrehozását vagy módosítását, összpontosítva a
rendellenes végrehajtási utak (pl. /tmp, /dev/shm) és gyanús szülőfolyamatok
(pl. shell, webszerver).Kiszűri a legitim csomagkezelési és CM-eszközöket.

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
- **Leírás:** Érzékeli a tartósság érdekében használt rendszeridőzítők létrehozását vagy aktiválását.
Nem szabványos címtárhelyekre (felhasználói szintű egységek), interaktív shellre összpontosít
triggerek és gyanús végrehajtási terhelések (zavarás, hálózati eszközök).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Befecskendezési folyamat észlelése (ATT&CK T1055)
- **ID:** `T1055.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fejlett folyamatbefecskendezési technikákat (DLL-befecskendezés, PE-befecskendezés, száleltérítés, APC, TLS, EWM, Hollowing) a magas kockázatú GrantedAccess-maszkok, a gyanús forrás-cél folyamatkapcsolatok és a nem támogatott memóriarégiók figyelésével.Megbízható rendszerfolyamatok és AV-komponensek kizárva a téves pozitív eredmények csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## DLL befecskendezés észlelése (ATT&CK T1055.001)
- **ID:** `T1055_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a DLL-befecskendezést azáltal, hogy azonosítja a kritikus Windows-folyamatokat célzó távoli szál-létrehozást, ahol a kezdőcím a könyvtárbetöltési függvényeknek felel meg, vagy a forrásmemória-régió nem támogatott (shellkód).A megbízható rendszerfolyamatok és AV-komponensek nem tartoznak ide.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## PE befecskendezés észlelése (ATT&CK T1055.002)
- **ID:** `T1055_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a PE-injektálást a folyamatok közötti memóriamanipuláció azonosításával, ahol a hívás forrása nem támogatott memória (shellkód), és a cél egy kritikus Windows-rendszerfolyamat.Úgy tervezték, hogy kiszűrje a megbízható AV- és rendszerszolgáltatásokat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Száleltérítés-észlelés (ATT&CK T1055.003)
- **ID:** `T1055_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lopakodó szálvégrehajtás-eltérítést azáltal, hogy figyeli a folyamatok közötti hozzáférési kérelmeket szálkezelési jogokkal (SET_CONTEXT), ahol a hívó verem nem támogatott vagy beillesztett memóriából (shellkód) származik.Nagy értékű folyamatokat céloz meg a fejlett jogosultság-eszkalációs kísérletek azonosítása érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## APC befecskendezés észlelése (ATT&CK T1055.004)
- **ID:** `T1055_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy pontosságú APC (Asynchronous Procedure Call) befecskendezési kísérleteket, beleértve az Early Bird injekciót is, a szál hozzáférési maszkok (THREAD_SET_CONTEXT) figyelésével, ahol a hívó kód nem támogatott vagy nem megbízható memóriarégiókból származik.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## TLS befecskendezés észlelése (ATT&CK T1055.005)
- **ID:** `T1055_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a TLS-befecskendezést a folyamatok közötti memóriamanipuláció figyelésével, amely a PE-fejléceket célozza meg, ahol a végrehajtási folyamat nem támogatott memóriarégiókból (shellkód) származik, miközben kiszűri a megbízható rendszerfolyamatokat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ptrace Injection Detection (ATT&CK T1055.008)
- **ID:** `T1055_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a ptrace alapú folyamatinjektálást a gyanús binárisokból vagy több felhasználó közötti ptrace mellékletekből származó PTRACE_POKETEXT/DATA műveletek figyelésével, miközben kiszűri a jogos hibakereső és megfigyelő eszközöket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lopakodó modul-felülírás (ATT&CK T1055.009)
- **ID:** `T1055_009.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rejtett folyamat- vagy modul-felülírást a VM_WRITE engedélyekkel rendelkező, többfolyamat-memória-hozzáférés figyelésével, ahol a hívó verem nem támogatott memóriából (shellkód) származik, és a kritikus rendszerfolyamatokat célozza meg.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lopakodó extra ablakmemória (EWM) befecskendezés (ATT&CK T1055.011)
- **ID:** `T1055_011.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az extra ablakmemória (EWM) befecskendezését azáltal, hogy figyeli a gyanús, többfolyamat-memória-hozzáférési kéréseket, ahol a CallTrace a nem támogatott memóriából (shellkódból) történő végrehajtást jelzi, megcélozva a gyakori grafikus felhasználói felületi folyamatokat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lopakodó eljárással történő kiürítés (ATT&CK T1055.012)
- **ID:** `T1055_012.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy pontosságú folyamatok kiüresedését azáltal, hogy azonosítja azokat a VM_WRITE/VM_OPERATION engedéllyel rendelkező, többfolyamat-hozzáférési kérelmeket, ahol a hívó verem nem támogatott memóriából (shellkód) származik, és általános áldozati folyamatokat céloz meg.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lopakodó eljárással történő kiürítés (ATT&CK T1055.013)
- **ID:** `T1055_013.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy pontosságú folyamatok kiüresedését azáltal, hogy azonosítja azokat a VM_WRITE/VM_OPERATION engedéllyel rendelkező, többfolyamat-hozzáférési kérelmeket, ahol a hívó verem nem támogatott memóriából (shellkód) származik, és általános áldozati folyamatokat céloz meg.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Stealthy Process Ghosting (ATT&CK T1055.014)
- **ID:** `T1055_014.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Felismeri a Process Ghosting-ot azáltal, hogy azonosítja azokat a folyamatlétrehozási eseményeket, ahol az alapul szolgáló fájl „törlés-függő” állapotban van, amit a végrehajtás során hiányzó hash-ek bizonyítanak, és amelyek nem szabványos könyvtárakból származnak.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Stealthy List Planting Injection (ATT&CK T1055.015)
- **ID:** `T1055_015.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a ListPlanting injekciót azáltal, hogy azonosítja a ListView-képes folyamatokhoz intézett gyanús, többfolyamat-hozzáférési kérelmeket, ahol a végrehajtási folyamat nem aláírt modulokból, hanem nem támogatott memóriarégiókból (shellkódból) származik.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Bemeneti rögzítés észlelése (ATT&CK T1056)
- **ID:** `T1056.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kifinomult bemenetrögzítést (keylogging) azáltal, hogy azonosítja a gyanús API-val kapcsolatos parancssorokat, a jogosulatlan shell-alapú billentyűnaplózási kódrészleteket és a felhasználói bevitelt célzó rendellenes folyamatviselkedést.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Keylogging & Input Hooking (ATT&CK T1056.001)
- **ID:** `T1056_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fejlett billentyűnaplózást azáltal, hogy azonosítja a gyanús API-hívásokat a nem jogosult vagy átmeneti folyamatokból, és a SetWindowsHookEx és a GetAsyncKeyState használatát célozza meg nem szabványos végrehajtási környezetekben (például PowerShell, Rundll32).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## GUI bemenet rögzítése (ATT&CK T1056.002)
- **ID:** `T1056_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a hitelesítő adatok megtévesztő grafikus felhasználói felületen vagy átfedéseken keresztüli rögzítésére irányuló kísérleteket.A PowerShell/C# kódrészletekre összpontosít, amelyek modális párbeszédpaneleket hoznak létre gyanús szülőfolyamatokból (böngészők, irodai alkalmazások) és nem támogatott szkriptekből.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Digitális tanúsítvány ellopása (ATT&CK T1056.003)
- **ID:** `T1056_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a magánkulcsok és digitális tanúsítványok jogosulatlan kimásolását.Figyeli a „nem exportálható” kulcsok memóriafoltozáson keresztüli kibontását, a certutil vagy a PowerShell gyanús használatát PFX-létrehozáshoz, valamint a Windows Cryptographic Key Store közvetlen elérését.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús hitelesítő adatok API-hozzákapcsolása a Win32 könyvtárakon keresztül
- **ID:** `T1056_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús folyamatokat, és betölti a Win32-könyvtárak kombinációit, amelyeket gyakran visszaélnek hitelesítő adatok lehallgatása vagy API-beakasztás céljából, mint például a user32.dll, advapi32.dll és a win32u.dll.A szabály a rendszeren kívüli, a felhasználó által írható végrehajtási útvonalakra összpontosít, és kizárja a gyakori legitim szoftvereket a hamis pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Folyamatfelderítés (ATT&CK T1057)
- **ID:** `T1057.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a célzott folyamatfelderítést, amely a biztonsági termékek azonosítására és a memóriacélok felderítésére összpontosít.Kiszűri a böngészőkből és a törvényes frissítési szervezőkből származó nagyfrekvenciás zajokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Scripting Interpreter Contextual Anomália
- **ID:** `T1059.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús PowerShell- vagy CMD-végrehajtást a shell-értelmezések korrelációjával
magas kockázatú szülői folyamatokkal (Office, Böngészők, Webszerverek) és homályosítási technikákkal.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús kódolt PowerShell-parancsvégrehajtás
- **ID:** `T1059_001.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A PowerShell gyanús végrehajtását észleli kódolt parancsok használatával, amelyek végrehajtását megkerülő vagy homályos jelzőkkel kombinálják.Ezt a technikát általában a támadók használják az észlelés elkerülésére és a rosszindulatú terhelések végrehajtására a memóriában.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity AppleScript (osascript) visszaélés-észlelés
- **ID:** `T1059_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a gyanús osascript-végrehajtást a „do shell script” menekülések figyelésével,
base64 kódolású hasznos terhelések és nem megbízható szülőfolyamatokból származó végrehajtás
mint a böngészők vagy levelezőkliensek.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Speciális Windows Command Shell kontextuális anomália
- **ID:** `T1059_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús cmd.exe-végrehajtást a kockázatos szülőfolyamatok korrelációjával
(Webszerverek, Office, SQL) rendellenes parancssori mintákkal, mint pl
parancsláncolás és felfedezés.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Unix shell visszaélés és fordított shell észlelés
- **ID:** `T1059_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Parancsinjektálás figyelésével észleli a gyanús Unix shell-végrehajtást
webes folyamatoktól, fordított shell socket átirányítástól és fájl nélküli pipe-to-shell mintáktól.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity VBScript kontextuális anomália észlelése
- **ID:** `T1059_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [PUBPRN.VBS](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A jogos operációs rendszer-felügyeleti szkriptek kiszűrésével észleli a gyanús VBScript-végrehajtást
és a kockázatos szülői folyamatokra, a szokatlan fájlhelyekre összpontosítva és
a rosszindulatú programok kézbesítésénél használt gyakori elhomályosítási/letöltési minták.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Python tolmács visszaélés észlelése
- **ID:** `T1059_006.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Gyanús Python végrehajtási mintákat észlel, az egysoros fordított shellekre összpontosítva,
interaktív shell-frissítések és végrehajtás, amely a magas kockázatú hálózat felé való csatlakozásból származik
szülő folyamatok (Webszerverek, SQL).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity JScript Interpreter Contextual Anomália
- **ID:** `T1059_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús JScript-végrehajtást a wscript/cscript és a wscript/cscript korrelációval
kockázatos szülőfolyamatok, nem megbízható fájlhelyek és parancssori argumentumok
jellemzően homályosításra vagy távoli hasznos adatlekérésre használják.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity hálózati eszköz CLI-manipulációja
- **ID:** `T1059_008.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)
- **Leírás:** Érzékeli a kritikus, jogosulatlan konfigurációs változtatásokat a hálózati eszközökön,
a kriminalisztika elleni küzdelemre (naplók letiltása), a hitelesítő adatokra összpontosítva,
és jogosulatlan adatok kiszűrése (config export).

#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Shell kihasználása és adatszivárgás
- **ID:** `T1059_009.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Cloud Shell környezetekben észleli a jogosulatlan vagy rosszindulatú tevékenységeket,
a személyazonosság-lopásra, a naplózás elnyomására és a privát adatok átalakítására összpontosítva
felhő erőforrások nyilvános hozzáféréshez.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús RENDSZER folyamat a felhasználói kontextusból
- **ID:** `T1068.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a RENDSZER néven futó gyanús folyamatokat, amelyeket a felhasználó által kezdeményezett szülőfolyamatok (például Explorer, böngészők vagy Office-alkalmazások) hoztak létre.Ez a viselkedés a jogosultságok kiszélesítését, a jogkivonat manipulációját vagy az UAC-bypass kihasználását jelezheti.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Engedélycsoportok felderítése (ATT&CK T1069)
- **ID:** `T1069.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a helyi vagy tartományi engedélycsoportok szisztematikus felfedezését.A kiemelt fiókok azonosítására használt felderítési mintákra összpontosít, miközben az integritás és a szülő-folyamat elemzése révén kiszűri a legitim rendszer- és készletzajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Helyi csoportfelderítés (ATT&CK T1069.001)
- **ID:** `T1069_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a célzott helyi csoportos felderítést, a kiemelt fiókokra összpontosítva (Adminisztrátorok, RDP).Kiszűri a legitim rendszer- és készletzajt az integritási szint kapuzásán és a szülő-folyamat korreláción keresztül.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Domaincsoport felfedezése (ATT&CK T1069.002)
- **ID:** `T1069_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Szisztematikus AD-tartománycsoport-felderítést észlel a felderítő eszközökre (BloodHound, AdFind) és a gyanús PowerShell-mintákra összpontosítva.Integritási szintet és folyamatvonalat használ az adminisztrátori munkaállomásokról érkező téves pozitívumok minimalizálására.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Groups Discovery (ATT&CK T1069.003)
- **ID:** `T1069_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a szisztematikus felhőcsoport-felderítést a tömeges felderítési minták, az atipikus felhasználói ügynökök és az érzékeny csoporttulajdonságok kiterjesztése révén.Úgy tervezték, hogy kiszűrje a nagy mennyiségű CSPM-et és IaC-szolgáltatást.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Jelző eltávolítása a gazdagépen (ATT&CK T1070)
- **ID:** `T1070.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FSUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Windows eseménynaplóinak és a nagy értékű törvényszéki műtermékeknek (USN Journal, Prefetch) törlésére irányuló célzott kísérleteket.A nem szabványos végrehajtási láncokra és a biztonsági szempontból érzékeny szolgáltatók speciális elszámolására összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## A biztonsági eseménynapló törölve a wevtutil.exe használatával
- **ID:** `T1070_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Windows Security eseménynaplójának törlésére tett kísérleteket a wevtutil.exe használatával, amely egy gyakori támadótechnika, amelyet a hitelesítő adatokhoz való hozzáférés, oldalirányú mozgás vagy állandóság utáni nyomok lefedésére használnak.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Linux naplótörlés és naplószabotázs (ATT&CK T1070.002)
- **ID:** `T1070_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a Linux rendszernaplók és a naplózott pufferek törlésére vagy csonkolására irányuló célzott kísérleteket.A kézi parancssori mintákra, a naplófájlokba való shell-átirányításra és a rendszernaplók felszívására összpontosít az automatizált karbantartási ablakokon kívül.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Postafiókadatok törlése és szabálymanipuláció (ATT&CK T1070.003)
- **ID:** `T1070_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a postafiók adatok szisztematikus eltávolítását és a rosszindulatú beérkező levelek szabályainak létrehozását.A tömeges törlési parancsmagokra és az automatizált szabálykészletekre összpontosít, amelyek célja a biztonsági értesítések letiltása vagy a támadói kommunikáció elrejtése.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Törvényszéki műtermékek és fájltörlés (ATT&CK T1070.004)
- **ID:** `T1070_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CIPHER.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FSUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy értékű kriminalisztikai műtermékek (USN Journal, Prefetch, Amcache) célzott megsemmisítését és a biztonságos törlési segédprogramok használatát.A nem szabványos folyamatok eredetére és az elkerülési technikákra összpontosít, amelyek célja az incidens utáni helyreállítás megelőzése.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati megosztás és hitelesítő adatok tisztítása (ATT&CK T1070.005)
- **ID:** `T1070_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CMDKEY.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a leképezett hálózati megosztások és a tárolt hitelesítő adatok tömeges eltávolítását helyettesítő karakter törléssel, kényszerjelzőkkel vagy parancsfájllal ellátott hitelesítő adatok törlésével.Úgy tervezték, hogy megkülönböztesse az oldalirányú mozgás utáni automatizált igazságügyi szakértői tisztítást a rutin adminisztratív tevékenységtől.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Timestomp és MACE attribútummanipuláció (T1070.006)
- **ID:** `T1070_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fájlok időbélyegeinek (MACE attribútumainak) manipulálására irányuló kísérleteket, hogy elkerülje a törvényszéki elemzést.
A PowerShell-alapú objektumtulajdonságok módosítására és a speciális kriminalisztikai segédprogramokra összpontosít,
miközben szűri a jogszerű telepítői és rendszerkarbantartási tevékenységeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati előzmények és RDP nyomkövetés eltávolítása (T1070.007)
- **ID:** `T1070_007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a célzott próbálkozásokat a hálózati csatlakozási előzmények törlésére, az RDP-re összpontosítva
Terminal Server Client MRU listák, hálózati megosztási metaadatok eltávolítása és DNS-gyorsítótár
kipirul a gyanús folyamatláncokból.Kiszűri a gyakori adminisztrációkat
és az ügyfélszolgálati műveletek, hacsak nem részei szélesebb körű támadási tevékenységnek.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## E-mail tárolás és adatbázis-megsemmisítés (T1070.008)
- **ID:** `T1070_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az e-mail tárolófájlok (PST/OST) és az Exchange adatbázisok (EDB) célzott megsemmisítését.
A programozott törlésre, az adatbázis leválasztására és a törvényszéki törlési mintákra összpontosít
nem megbízható folyamatokból vagy gyanús szülő-gyermek folyamatláncokból erednek.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Perzisztencia műtermékek eltávolítása (T1070.009)
- **ID:** `T1070_009.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kitartási mechanizmusok szisztematikus eltávolítását, beleértve az ütemezett feladatokat,
Szolgáltatások és WMI objektumok, a kényszertörlési minták és a gyanús
feldolgozza a vonalakat.Kiszűri a gyakori szoftverfrissítési ciklusokat, az MSI telepítői tevékenységet,
és az ismert megbízható karbantartási folyamatok.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Alkalmazási réteg C2 anomália (T1071)
- **ID:** `T1071.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A rendellenes hálózat figyelésével észleli a potenciális C2 alkalmazási rétegű kommunikációt
nem böngésző folyamatok által kezdeményezett kapcsolatok.A gyanús szülő-gyermekre összpontosít
kapcsolatok, magas kockázatú LOLBins és könyvtár-alapú hálózati tevékenység (WinInet/WinHTTP).
Szűri a jogos böngészőforgalmat és a megbízható infrastruktúrát, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## HTTPS C2 anomália (T1071.001)
- **ID:** `T1071_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A hálózati kapcsolatok figyelésével észleli a rendellenes HTTP/S-alapú C2 kommunikációt
nem hálózatos folyamatokból vagy az üregesedés jeleit mutató folyamatokból, szokatlan
szülő-gyerek származás, vagy gyanús automatizálás.Kiszűri a legális böngészőket
és ismert biztonságos úticélok a hamis pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## FTP/SFTP protokoll anomália (T1071.002)
- **ID:** `T1071_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az FTP/SFTP és a kapcsolódó fájlátviteli protokollok jogosulatlan használatát
a nem interaktív munkamenetek, a gyanús szkript alapú átvitelek figyelésével,
és rendellenes szülő-gyermek folyamatkapcsolatok (pl. Office to FTP kliensek).

#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Levelezési protokoll anomália (T1071.003)
- **ID:** `T1071_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGEWEBVIEW2.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A direkt mail figyelésével észleli a jogosulatlan e-mail-alapú C2-t vagy a kiszűrést
protokoll kapcsolatok (SMTP, IMAP, POP3) a nem levelező folyamatokból.-ra összpontosít
automatizálás és szkriptekkel való visszaélés PowerShell-en, .NET-en és régi szkriptgazdagépeken keresztül,
és rendellenes folyamatvonalak.

#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## DNS Tunneling & Beaconing (T1071.004)
- **ID:** `T1071_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a DNS-alagút és a C2 tevékenységet a nagy entrópiájú aldomainek figyelésével,
szokatlan lekérdezéstípusok (TXT, NULL és SIG), hosszú vagy ismétlődő lekérdezések és DNS
tevékenység a nem hálózati natív folyamatokból.A rendellenes hosszra, gyakoriságra összpontosít,
és feldolgozza a kontextust a hamis pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú szoftvertelepítési eszköz visszaélések észlelése
- **ID:** `T1072.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a szoftvertelepítési ügynökök rosszindulatú rakományok végrehajtására irányuló visszaéléseit.
A rendellenes gyermekfolyamatokra összpontosít (PowerShell, BitsAdmin, CertUtil)
telepítési szolgáltatásokkal, kiszűrve a szabványos karbantartási mintákat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Adatállomási anomália (T1074)
- **ID:** `T1074.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MAKECAB.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Fájl-összesítési minták figyelésével észleli a rendellenes adatsorolást,
alacsony tömörítésű vagy jelszóval védett archiválási műveletek és tömeges másolás
parancsokat rejtett vagy ideiglenes rendszerkönyvtárakba nem megbízható shellekből
vagy forgatókönyveket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Helyi adatállomási anomália (T1074.001)
- **ID:** `T1074_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MAKECAB.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Felismeri a szisztematikus helyi adatsorolást a rendellenes fájlösszesítés azonosításával
minták, alacsony tömörítésű vagy jelszóval védett archiválási kapcsolók és tömeges másolás
műveleteket rejtett vagy érzékeny rendszerkönyvtárakba nem megbízható folyamatkörnyezetekből.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Távoli adatállomásozás (T1074.002)
- **ID:** `T1074_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a távoli adatsorolást azáltal, hogy azonosítja a rendellenes tömeges fájlmozgásokat a belső UNC útvonalakra,
Ezt követik az archiválási parancsok alacsony tömörítési/titkosítási jelzőkkel, amelyek innen származnak
megbízhatatlan folyamatvonalak.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú rendellenes bejelentkezés érvényes fiókon keresztül
- **ID:** `T1078.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a sikeres bejelentkezéseket olyan érvényes fiókok használatával, amelyek rendellenes jellemzőket mutatnak,
mint például a szolgáltatásfiókok szokatlan bejelentkezési típusai vagy az azonnali bejelentkezések
érzékeny parancsvégrehajtás.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú alapértelmezett fiókkal való visszaélés észlelése
- **ID:** `T1078_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a sikeres bejelentkezéseket jól ismert alapértelmezett fióknevekkel (Rendszergazda, Vendég, root)
nem szabványos hálózati helyekről vagy interaktív távoli munkameneteken (RDP) keresztül.
Kiszűri a gyakori helyi rendszerzajt és a belső automatizálást.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Domain Account Lateral Movement Anomália
- **ID:** `T1078_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a rendellenes RDP vagy hálózati bejelentkezést a kritikus infrastruktúrába (DC-k, SQL, fájlkiszolgálók)
jogosulatlan forrásalhálózatokból vagy nem rendszergazdai felhasználói fiókokból származik.
Szigorú szűrést valósít meg a gépfiókokhoz és az ismert ugrásszerverekhez.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú helyi fiók távelérés észlelése
- **ID:** `T1078_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Helyi fiókok használatával észleli a sikeres távoli bejelentkezéseket (RDP, SMB, WinRM).
Tartományi környezetben a helyi fiókokat csak a helyi konzolhoz szabad használni
hozzáférést.A távhasználat erősen jelzi az oldalirányú mozgást vagy a hitelesítő adatok ellopását.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud-fiók kompromittálódása (Entra ID)
- **ID:** `T1078_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a sikeres felhőbejelentkezéseket, amelyek magas kockázatú jelzéseket mutatnak:
MFA megkerülése privilegizált fiókokon, lehetetlen utazási minták,
vagy nem szabványos automatizálási felhasználói ügynökök emberi fiókok általi használata.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Megosztott tartalom (T1080)
- **ID:** `T1080.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a megosztott tartalom beszennyezésére irányuló kísérleteket azáltal, hogy figyeli a gyanús folyamat-fájl-megosztás interakciókat.
A makró-kompatibilis sablonokra, a parancsikon-eltérítésre és az UNC-útvonalak bináris cseréjére összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendszerinformáció-felderítés (T1082)
- **ID:** `T1082.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Szisztematikus rendszerinformáció-felderítést észlel (OS, javítások, architektúra)
a felderítésre összpontosítva az exploit kiválasztásához.Szűri a nagy mennyiségű zajt
készletügynökökből, felügyeleti eszközökből és integritási szintet használó böngészőkből
és a szülői folyamat kapuzása.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Fájl- és könyvtárfelderítés (T1083)
- **ID:** `T1083.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a célzott fájl- és könyvtárfelderítést, az érzékeny adatok begyűjtésére összpontosítva.
Elemzéssel kiszűri a jogszerű rendszerindexelést, az AV-vizsgálatokat és a fejlesztői tevékenységeket
folyamat integritását, szülő-gyermek kapcsolatokat és konkrét kulcsszómintákat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Net user vagy net localgroup gyanús használata a cmd.exe-n keresztül
- **ID:** `T1087.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a net user vagy net localgroup parancsokat végrehajtó cmd.exe gyanús használatát, amelyeket a támadók általában fiókfelderítésre vagy jogosultságok kiterjesztésére használnak.A szabály a támadószerű végrehajtási környezetre összpontosít, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Helyi fiókfelderítés (T1087.001)
- **ID:** `T1087_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szisztematikus helyi fiókok és csoportok felsorolását.A rendellenes folyamatvonalakra összpontosít
(pl. webszerverek vagy távoli héjak által indított felfedezőeszközök) és a modern
felsorolási módszerek, például a WMI/CIM.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Domainfiók felderítése (T1087.002)
- **ID:** `T1087_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az Active Directory szisztematikus felsorolását a támadó LDAP-szűrőkre összpontosítva
és nem szabványos folyamatvonalak.Szűri a jogos adminisztratív viselkedést
ismert szolgáltatásfiókok és felügyeleti eszközök kizárásával.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## E-mail fiók felderítése (T1087.003)
- **ID:** `T1087_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az e-mail fiókok és a globális címlisták (GAL) szisztematikus felfedezését
a nem interaktív PowerShell-munkamenetek, a tömeges exportálási parancsok és a
a nem megbízható folyamatok rendellenes hozzáférése a helyi Outlook/Exchange profilkonfigurációkhoz.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Account Discovery (T1087.004)
- **ID:** `T1087_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a felhőalapú fiókok (AWS, Azure, GCP) szisztematikus felfedezését
az interaktív CLI használat és a rendellenes parancsláncolás figyelése.
Kiszűri a jogos CI/CD-folyamatokat és az automatizálási munkaterheléseket
a folyamat vonaláról és a felhasználói kontextusról.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Proxy és forgáspont-észlelés (T1090)
- **ID:** `T1090.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Korrelációval észleli a hálózati proxy-k és porttovábbítási szabályok létrehozását
magas kockázatú natív bináris fájlok (Netsh, PowerShell) pivot-specifikus argumentumokkal, amelyek leképeznek
külső figyelő portok a belső hálózati eszközökhöz.Úgy tervezték, hogy kizárja a legitim
virtualizáció és visszacsatolási forgalom.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Belső proxy és pivot észlelés (T1090.001)
- **ID:** `T1090_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a belső hálózati forgást a konfiguráció azonosításával
porttovábbítás privát RFC 1918 IP-címekre nem rendszerről
folyamatok, kivéve a legitim helyi virtualizációt és a konténerforgalmat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Külső proxy és alagút (T1090.002)
- **ID:** `T1090_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nem szabványos külső proxy használatát a merevkódolt azonosítással
hitelesítő adatok, egyéni PAC-fájlok vagy proxy-felülírások magas kockázatú binárisokban
interaktív vagy script interpreterekből indítva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Többugrásos proxy és Tor észlelés (T1090.003)
- **ID:** `T1090_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a többugrásos proxyt és a Tor áramkört a jogosulatlanok azonosításával
proxy láncoló eszközök vagy rejtett Tor-kliensek, amelyek nem szabványostól futnak
könyvtárak, a vezérlőportok manipulálására és a SOCKS5 láncolására összpontosítva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Domain Fronting Detection (T1090.004)
- **ID:** `T1090_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a domain frontot a manuális HTTP Host fejléc felülírások azonosításával
az általános web-kompatibilis LoLBins parancssori argumentumain belül,
kifejezetten a CDN által támogatott infrastruktúra-átirányítást célozza meg.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú folyamatvégrehajtás cserélhető adathordozóról
- **ID:** `T1091.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SHELL32.DLL](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a parancsfájl-értelmezők és LOLBin-ek végrehajtását nem rendszermeghajtókról.
A férgek (például Raspberry Robin) és a kézi USB-alapú mintákra összpontosít
támadásokat, miközben kiszűri a gyakori hordozható alkalmazásokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## C2 cserélhető adathordozó anomália (T1071.002 / T1092)
- **ID:** `T1092.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Azonosítással észleli a jogosulatlan C2-t vagy adattovábbítást cserélhető adathordozón keresztül
nem interaktív folyamatok, amelyek hozzáférnek az USB-köteten lévő rejtett/rendszerfájlokhoz,
az automatikus szkript-végrehajtásra és az alternatív adatfolyammal (ADS) való visszaélésre összpontosítva.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nem alkalmazási réteg C2 (T1095)
- **ID:** `T1095.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az egyéni C2 kommunikációt a nyers TCP/UDP socketeken keresztül azáltal, hogy azonosítja a
alacsony szintű NetworkStreams és kézi byte-array puffer példányosítása
manipuláció, amelyet socket írási/olvasási műveletek követnek.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú fiókmanipuláció – a kitartásra összpontosítva
- **ID:** `T1098.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a gyanús és ritka módosításokat a felhasználói fiók attribútumain
erősen összefügg a kitartással és a privilégiumok eszkalációjával, mint pl
SID-előzmények beillesztése, Kerberos korlátozott delegálási módosítások és
jelszavak lejáratának letiltása érzékeny fiókoknál.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Entra ID alkalmazás hitelesítő adatok kiegészítése
- **ID:** `T1098_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli, ha új titkos vagy tanúsítvány kerül hozzáadásra egy Entra ID alkalmazáshoz.
A támadók ezt használják a hátsó ajtó létrehozására a szolgáltatási megbízókon keresztül.
Ez a szabály kiszűri a gyakori Microsoft belső alkalmazásokat és az ismert CI/CD-szolgáltatásokat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Exchange Mailbox Permission Grant (T1098.002)
- **ID:** `T1098_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a kritikus postafiók-engedélyek megadását (FullAccess, SendAs).
Kiszűri a gyakori szolgáltatásfiókokat, és a bérlőközi ill
jogosulatlan adminisztratív intézkedések, különösen nagy értékű célpontok esetében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Entra ID App tanúsítvány kiegészítése
- **ID:** `T1098_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli egy új tanúsítvány (nyilvános kulcs) hozzáadását egy Entra ID alkalmazáshoz.
A támadók ezt használják a hosszú távú kitartás érdekében, hogy az alkalmazás fő szolgáltatásaként működjenek.
Ez a szabály úgy van optimalizálva, hogy kiszűrje az automatizált Microsoft belső rotációkat és az ismert CI/CD-szolgáltatókat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Azure-szerepkör-hozzárendelés eszkalációja
- **ID:** `T1098_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a kiemelten privilegizált Azure-szerepkörök közvetlen hozzárendelését (tulajdonos, közreműködő, felhasználói hozzáférés-rendszergazda).
Kiszűri a PIM (Privileged Identity Management) aktiválásokat és az ismert automatizálási elveket
a zaj csökkentésére és a kézi jogosultság-kiterjesztésre összpontosítva.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Device Registration Perzisztencia (T1098.005)
- **ID:** `T1098_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a gyanús eszközregisztrációkat az Entra ID-ben.A támadók regisztrálják saját eszközeiket
a „regisztrált” eszközállapotot igénylő feltételes hozzáférési házirendek megkerüléséhez.
Ez a szabály kiszűri a felügyelt regisztrációkat, és a nem felügyelt vagy szkripttel ellátott regisztrációkra összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity MFA módszer kiegészítés
- **ID:** `T1098_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli, ha új MFA-módszert adnak hozzá egy felhasználói fiókhoz egy nem megbízható helyről
vagy friss MFA-kihívás nélkül.Ez a támadók elsődleges kitartási technikája
hogy fenntartsa a hozzáférést egy kezdeti fiókkompromittálódás után.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Web Service C2 (T1102)
- **ID:** `T1102.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a parancs- és vezérlési (C2) kommunikációt legitim felhőszolgáltatásokon keresztül
nyers API vagy nyers tartalmú végpontok azonosítása, amelyekhez nem böngésző LoLBins, szkript
értelmezők, vagy gyanús utakról futó binárisok.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Dead Drop Resolver (T1102.001)
- **ID:** `T1102_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A nyers tartalom lekérésének azonosításával észleli a holtpont-feloldók használatát
közösségi és kódplatformokról, a gyanús szülő-gyerek szűrésével
folyamatkapcsolatok és nem szabványos letöltési módszerek.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Kétirányú felhő C2 (T1102.002)
- **ID:** `T1102_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Azonosítással észleli az interaktív parancs- és vezérlési (C2) kommunikációt felhő API-kon keresztül
speciális írási/olvasási módszerek (POST/GET), amelyeket nem böngésző LoLBins vagy bináris fájl bocsát ki
gyanús útvonalakról fut, miközben kizárja a hivatalos kliens alkalmazásokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Egyirányú webszolgáltatás C2 (T1102.003)
- **ID:** `T1102_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az egyirányú parancs és vezérlés (C2) vagy az adatok felhőszolgáltatásokon keresztüli kiszűrését
specifikus API-feltöltési/letöltési módszerek korrelációja nem szabványos folyamathelyekkel
és a gyanús szülői folyamatok vonalai.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Többlépcsős C2 (T1104)
- **ID:** `T1104.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Fájl nélküli végrehajtási minták azonosításával érzékeli a többlépcsős parancs- és vezérlési (C2) tevékenységet
ahol a hálózati kérések eredménye közvetlenül a memóriaterhelési függvényekbe vagy a parancsfájl-kiértékelőkbe kerül
közbenső lemezírás nélkül.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Beépített Windows-eszközök gyanús használata fájlok letöltéséhez és kódvégrehajtáshoz
- **ID:** `T1105.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a beépített Windows-segédprogramok, például a PowerShell, a bitsadmin és a certutil gyanús használatát fájlok letöltésére és kód futtatására, amely egy gyakori támadó technika a rakomány állomásoztatására és végrehajtására.A szabály a támadókra jellemző mintákra és a végrehajtási környezetre összpontosít, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Native API visszaélés LOLBins-en keresztül
- **ID:** `T1106.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a natív API-végrehajtás gyanús használatát megbízható Windows rendszeren keresztül
binárisok (LOLBins).Azokra a forgatókönyvekre összpontosít, ahol fordítók vagy rendszereszközök
nem megbízható szülői folyamatok visszaélnek memóriainjektálás végrehajtása érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Brute Force & Tooling (T1110)
- **ID:** `T1110.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a brute force eszközök végrehajtását és a script-es hitelesítő adatok kitalálását azáltal, hogy
gyanús parancssori argumentumok (jelszavas listák, felhasználói fájlok) és jogosulatlanok
feldolgozza a nem megbízható helyekről származó vonalakat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Egyetlen felhasználó többszöri sikertelen bejelentkezési kísérlete (lehetséges jelszókitalálás)
- **ID:** `T1110_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Rövid időn belül észleli ugyanazon felhasználói fiók több sikertelen hitelesítési kísérletét, ami jelszókitalálásra vagy brute force tevékenységre utalhat.A szabály kizárja a hitelesítési zaj gyakori forrásait a hamis pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**


---
## Hitelesítési adatok exportálása és feltörése (T1110.002)
- **ID:** `T1110_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a hitelesítőadat-adatbázisok (SAM, SYSTEM, NTDS.dit) kibontási kísérleteit offline feltöréshez
és kiszűréssel nagy pontossággal azonosítja a jelszó-helyreállító eszközök végrehajtását
törvényes biztonsági mentési és rendszerkarbantartási folyamatok.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Jelszó kiszórás (T1110.003)
- **ID:** `T1110_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** A gyanús automatizált hitelesítés azonosításával észleli a jelszavas támadásokat
logika, ahol egyetlen folyamat iterál a fiókok listáján.Szűri
nem megbízható folyamathelyek és ismert támadási modul aláírások.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hitelesítési adatokkal való visszaélés és a kombinált listákkal való visszaélés (T1110.004)
- **ID:** `T1110_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Automatizált eszközök és tolmácsok azonosításával észleli a hitelesítő adatok kitöltését
(Python, .NET) nagy hitelesítő adatok kombinált listák feldolgozásával vagy ismert használatával
a keretrendszer argumentumainak kitöltése nem megbízható helyekről.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## MFA-kijátszás és munkamenet-eltérítés (T1111)
- **ID:** `T1111.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Észleli az MFA-kijátszást azáltal, hogy azonosítja a böngésző fő kulcsaihoz való jogosulatlan hozzáférést (helyi állam)
és munkamenet-adatbázisok (cookie-k) nem megbízható folyamatok által.Azt is figyeli
Reverse Proxy adathalászati keretrendszerek (Evilginx, Muraena) és token manipulációs eszközök.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Registry manipuláció kijátszás céljából (T1112)
- **ID:** `T1112.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Windows rendszerleíró adatbázisának letiltását célzó magas kockázatú módosításait
biztonsági ellenőrzések (Defender, UAC, LSA) vagy jogosulatlan távoli hozzáférés engedélyezése.
A szabványos rendszerfrissítések figyelmen kívül hagyására optimalizálva, és a nem szabványos folyamatviselkedésre összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Képernyőrögzítési anomália (T1113)
- **ID:** `T1113.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [PSR.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A gyanús .NET/GDI+ API azonosításával észleli a jogosulatlan képernyőrögzítést
hívások a PowerShellben, a rejtett PSR.exe-munkamenetek és az automatikus képfájl
szerializálás ideiglenes/nyilvános könyvtárakra.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## E-mail betakarítási anomália (T1114)
- **ID:** `T1114.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A gyanús e-mailek azonosításával észleli a jogosulatlan automatizált e-mail-gyűjtést
COM objektum példányosítás (Outlook.Application), postaláda export kérések,
és programozott hozzáférés az Inbox/Sent mappákhoz a nem szabványos shellekből.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Helyi e-mail-gyűjtési anomália (T1114.001)
- **ID:** `T1114_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A gyanús e-mailek azonosításával észleli a jogosulatlan automatizált helyi e-mail-gyűjtést
COM objektum példányosítás (Outlook.Application), mappaindex célzás (Beérkezett/Elküldött),
és programozott kijátszás (Visible=$false) a nem megbízható shellekből.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Távoli e-mail exportálási rendellenesség (T1114.002)
- **ID:** `T1114_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A szisztematikus azonosítással észleli a jogosulatlan távoli e-mail-gyűjtést
postafiók-exportálási kérelmek, amelyek érzékeny kulcsszószűrőket és átirányítást alkalmaznak
kimenet nem szabványos belső UNC-útvonalakra vagy adminisztrációs megosztásokra.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## E-mail továbbítási szabály rendellenessége (T1114.003)
- **ID:** `T1114_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Azonosítással észleli a jogosulatlan e-mail-továbbítási szabálykonfigurációkat
programozott átirányítás külső vagy nem megbízható domainekre, kombinálva ezzel
érzékeny kulcsszószűrés, amely gyanús folyamatvonalakból származik.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Vágólapadatok kémkedése (T1115)
- **ID:** `T1115.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Azonosítással észleli a vágólap megfigyelési és adatkiszűrési tevékenységeit
tartós lekérdezési hurkok, illetéktelen összeszerelési terhelések a vágólap eléréséhez,
és gyanús szülő-gyermek folyamatkapcsolatok (pl. webshellek, Office-makrók)
interakció a vágólap API-val.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Automatizált begyűjtés (T1119)
- **ID:** `T1119.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli az érzékeny fájlokat célzó, rendkívül gyanús automatizált adatgyűjtést.
A helyettesítő karakter alapú rekurzív fájlátvitelre összpontosít interaktív vagy webes shellekből,
másolás közös állomásozási területekre, kivéve a jogszerű rendszerkarbantartási és biztonsági mentési műveleteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Perifériás eszköz felfedezése (T1120)
- **ID:** `T1120.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a perifériás eszközök célzott felsorolását, az USB-re, lemezre és hálózati eszközökre összpontosítva.
A nagy pontosságú észlelés kiszűri a jogszerű PnP-tevékenységet és az illesztőprogram-kezelést
a folyamat integritásának, a szülő-gyermek kapcsolatok és a metaadatlekérdezési minták elemzésével.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hangrögzítés és kémkedés (T1123)
- **ID:** `T1123.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a jogosulatlan hangfelvételt és kémkedést.
A következőkre összpontosít:
- Alacsony szintű multimédiás API-hívások (winmm.dll, dsound.dll, NAudio)
- Szkript alapú hangrögzítési rutinok
- Gyanús szülő/gyermek folyamatkapcsolatok (irodai alkalmazások, héjak, webszerverek)
- A támadó eszközök által használt rosszindulatú parancssori minták
Szűri a legitim kommunikációs alkalmazásokat a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendszeridő-felderítés (T1124)
- **ID:** `T1124.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a célzott rendszeridő- és időzóna-felderítési technikákat.
A következőkre összpontosít:
- Gyanús folyamatvonalak (irodai alkalmazások, webszerverek, parancsfájl-gazdagépek)
- A homokozók elkerülésére vagy a geokerítésre általánosan használt automatizálási minták
- Az időszámláláshoz használt CLI-eszközök és PowerShell/.NET API-k
Nem tartalmazza az ismert rendszert, felügyeletet és jóindulatú automatizálást a hamis pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Videórögzítési anomália (T1125)
- **ID:** `T1125.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Felügyeli a jogosulatlan videórögzítést:
- Programozott hozzáférés a multimédiás API-khoz (DirectShow, Media Foundation)
- Önálló médiabinárisok (FFmpeg, VLC) használata rögzítési paraméterekkel
- Fej nélküli vagy szkript alapú végrehajtási környezetek (PowerShell, cmd, IIS-munkás)
Kiszűri a jogszerű konferencia-, együttműködési- és rendszerfolyamatokat, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Trusted Developer Utility Proxy (T1127)
- **ID:** `T1127.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Észleli a megbízható fejlesztői segédprogramokkal (MSBuild, CSC, JSC, VBC) való visszaélést a rosszindulatú kód végrehajtásának proxyjával:
- Figyeli a gyanús szülői folyamatokat (Office alkalmazások, böngészők, szkriptek)
- Érzékeli a rendellenes parancssori argumentumokat (távoli elérési utak, AppData, Temp)
- Kiszűri a jogos IDE/CI/CD tevékenységeket (Visual Studio, Jenkins, Build Agents)
A fájl nélküli vagy oldalsó C2-végrehajtási kísérletek nagy pontosságú riasztásaira összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## MSBuild proxy végrehajtása (T1127.001)
- **ID:** `T1127_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rosszindulatú MSBuild.exe proxy végrehajtását a következő megfigyeléssel:
- Rendellenes szülői folyamatok (irodai alkalmazások, böngészők, szkriptek)
- Gyanús parancssori argumentumok (inline XML feladatok, távoli elérési utak)
- Nem tartalmazza a szabványos fejlesztői és CI/CD környezeteket (Visual Studio, Jenkins, Build Agents)
Segít észlelni a fájl nélküli vagy C2 hasznos terhelések telepítését az MSBuild segítségével anélkül, hogy a szabványos fejlesztői eszköz riasztásait kiváltaná.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú megosztott modul betöltése nem megbízható útvonalról
- **ID:** `T1129.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a megbízható rendszerbináris fájlokat vagy a termelékenységet növelő alkalmazásokat, amelyek DLL-eket töltenek be
nem megbízható, világszerte írható könyvtárak.Ez annak elsődleges mutatója
DLL oldalsó betöltés vagy keresési rendelés eltérítése.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Adatkódolás és obfuszkálás (T1132)
- **ID:** `T1132.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a gyanús adatkódoló/dekódoló szekvenciákat, amelyeket a C2 titkosításhoz használnak:
- Programozott Base64/Hex konverzió (FromBase64String, ToBase64String, System.Text.Encoding)
- Beágyazott hasznos fejlécek (TVqQA, BXAAR)
- Magas entrópiájú parancssorok, amelyek az elhomályosított hasznos adatokat jelzik
- Nem szabványos folyamatvonalak, amelyek visszaélnek olyan eszközökkel, mint a rundll32, regsvr32, colorcpl
Szűri a jogos adminisztrációs és rendszerfolyamatokat a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szabványos kódolás és hasznos terhelés beadása (T1132.001)
- **ID:** `T1132_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Felismeri a gyanús szabványos kódoláshasználatot a következők figyelésével:
- Beágyazott végrehajtható fejlécek (MZ/PE) a Base64 karakterláncokon belül
- Programozott dekódolás FromBase64String, DeflateStream, MemoryStream vagy .NET konverziókkal
- Nagy entrópiájú parancssorok, amelyek a hasznos terhelés befecskendezését jelzik
- Nem adminisztratív folyamatok, amelyek kódolt hasznos adatokat hajtanak végre
Szűri a megbízható infrastruktúrát a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nem szabványos kódolás és XOR obfuszkáció (T1132.002)
- **ID:** `T1132_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Felismeri az egyéni kódolást és az obfuszkációt a következő megfigyeléssel:
- Byte szintű XOR manipulációk
- Backtick alapú karakterlánc-töredezettség
- Karakterkód rekonstrukció (pl. ::FromCharacterCode)
- Gyanús, nem interaktív folyamatkörnyezetek (rundll32, regsvr32, colorcpl)
Kiszűri a törvényes adminisztratív és infrastrukturális folyamatokat a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendellenes külső távoli szolgáltatás-hozzáférési kontextus
- **ID:** `T1133.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a gyanús sikeres bejelentkezéseket külső távoli szolgáltatásokon (RDP/VPN) keresztül.
Szűri a nem szabványos forrás IP-címeket, és a magas kockázatú fióktípusokra összpontosít
vagy a bejelentkezési esemény technikai anomáliái, amelyek az automatizáltra jellemzőek
hitelesítő adatok kitöltése vagy oldalirányú mozgás a külső ugródobozokból.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hozzáférési token manipuláció és megszemélyesítés (T1134)
- **ID:** `T1134.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Észleli a magas kockázatú hozzáférési jogkivonat-manipulációt és a megszemélyesítést a következők figyelésével:
- Az LSASS-szal együttműködő speciális eszközök tokenek ellopásához vagy másolásához
- Gyanús integritásszint-átmenetek, amelyek a token emelkedését jelzik
- Jogosulatlan LSASS kezelhetőség
Szűri az ismert megbízható rendszerfolyamatokat a téves pozitívumok minimalizálása érdekében

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Token megszemélyesítés LSASS Handle Duplikáción keresztül (T1134.001)
- **ID:** `T1134_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** A tokenlopást észleli az LSASS.exe fájlt célzó, gyanús fogantyúduplikáción keresztül.
Nagy pontosságú észlelés szűréssel:
- Ismert legitim rendszerfolyamatok
- Biztonsági ügynökök
- Normális adminisztratív tevékenység

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Folyamat létrehozása tokennel (T1134.002)
- **ID:** `T1134_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Felismeri a jogosulatlan folyamat-létrehozást duplikált tokenek használatával a következő megfigyeléssel:
- Támadó eszközök és token manipulációs parancsok
- Gyanús integritásszint-átmenet közepesről RENDSZERRE
- Kiszűri a legitim rendszerfolyamatokat, az UAC-emeléseket és a biztonsági ügynököket

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyári és megszemélyesítő token (T1134.003)
- **ID:** `T1134_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Figyelemmel kíséri a biztonsági tokenek jogosulatlan létrehozását és a hitelesítő adatok megszemélyesítését:
- Támadó eszközhasználat (Mimikatz, sekurlsa::pth, New-PassThroughToken)
- Gyanús parancssori argumentumok, például /netonly
- Nem megbízható szülői folyamatok generálják ezeket a műveleteket
- 9. bejelentkezési típus (NewCredentials) rendellenességek

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szülői PID-hamisítás és folyamatfa megsértése (T1134.004)
- **ID:** `T1134_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Felismeri a szülői PID-hamisítást és a folyamatfa megsértését a következők figyelésével:
- Kritikus rendszerfolyamatok (LSASS, CSRSS, Spooler) létrehozzák a shell-eket vagy értelmezőket
- A felhasználói szintű folyamatok szokatlan rendszer segédprogramokat eredményeznek
- Szűri a megbízható Windows viselkedést és a jogos WMI/ütemezett feladattevékenységet

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## SID-előzmény befecskendezés és DS-manipuláció (T1134.005)
- **ID:** `T1134_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli az sIDHistory injekciót és a címtárszolgáltatás jogosulatlan manipulációit a következők figyelésével:
- Az Active Directory objektum változásai (EventID 5136) az sIDHistory számára
- Jogosulatlan LSASS-leíró hozzáférés (EventID 10)
- Szűri a megbízható migrációs eszközöket és a rendszerfiókokat a hamis pozitívumok csökkentése érdekében

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati megosztás felfedezése (T1135)
- **ID:** `T1135.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Figyelemmel kíséri a szisztematikus hálózati megosztások felfedezését és a tartalom feltérképezését:
- Automatizált UNC felsorolási minták (hurkok, sweepek)
- Speciális eszközök, például Snaffler, SharpShares, PowerView és natív net parancsok
- Gyanús tartalom kulcsszavak a parancssori argumentumokban
- Nem szabványos szülőfolyamat vonal

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro jogosulatlan fiók létrehozása (T1136)
- **ID:** `T1136.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A gyanús folyamatvonalak azonosításával észleli a helyi vagy tartományi fiók létrehozását
és parancssori mintákat, miközben kiszűri az engedélyezett rendszer- és telepítési eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro jogosulatlan helyi fiók létrehozása (T1136.001)
- **ID:** `T1136_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A gyanús folyamatvonalak elemzésével észleli a helyi felhasználói fiók létrehozását
és parancssori argumentumokat.Kiszűri az automatizált MDM-et, a GPO-t és az ismert telepítőt
tevékenységek az alacsony álpozitív arány fenntartása érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro jogosulatlan domain fiók létrehozása (T1136.002)
- **ID:** `T1136_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Felismeri a domain fiók létrehozását a gyanús folyamatvonalak azonosításával és
nem szabványos végrehajtási környezetek.Kiszűri az engedélyezett IAM, HR-sync eszközöket,
és hivatalos AD kezelőkonzolok.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro jogosulatlan felhőfiók létrehozása (T1136.003)
- **ID:** `T1136_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a manuális felhőalapú fiók létrehozását a szereplő típusának korrelációjával,
a forrás IP-hírneve, valamint az engedélyezett kiépítési szolgáltatási tagok hiánya.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Az Office-alkalmazások indítási állandósága (T1137)
- **ID:** `T1137.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)
- **Leírás:** A rendszerleíró adatbázis módosításainak figyelésével észleli a jogosulatlan Office-maradványt:
- Nyomon követi a bővítmények terhelési viselkedését, az OPEN opciókat, a WebView URL-eket és a TrustRecords-t
- Megjelöli a nem szabványos folyamatokból vagy gyanús útvonalakból származó módosításokat
- Kiszűri a megbízható telepítőket és a rendszerútvonalakat, hogy csökkentse a hamis pozitívumot

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Az Office globális sablonjának gyanús módosítása (Normal.dotm)
- **ID:** `T1137_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Microsoft Office globális sablonok (Normal.dotm / NormalEmail.dotm) nem Office folyamatok általi vagy gyanús végrehajtási útvonalak általi nagy kockázatú módosítását vagy létrehozását.Ez makroalapú perzisztenciára utalhat (MITRE ATT&CK T1137.001).

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Office teszt DLL-perzisztencia (T1137.002)
- **ID:** `T1137_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)
- **Leírás:** Érzékeli az „Office Test” rendszerleíró kulcs létrehozását vagy módosítását, amelyet a DLL oldalbetöltésének fennmaradásához használnak:
- Figyeli a nem szabványos elérési utakat a potenciális DLL-adatokhoz
- Érzékeli a jogosulatlan szülői folyamatokat, amelyek erre a kulcsra írnak
- Kiszűri a legitim telepítői tevékenységet

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Outlook egyéni űrlapok állandósága (T1137.003)
- **ID:** `T1137_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)
- **Leírás:** Észleli az Outlook egyéni űrlapjainak jogosulatlan fennmaradását a következők figyelésével:
- Nem szabványos regisztrációs módosítások
- Gyanús folyamatok megjelenése űrlapszkriptekkel kapcsolatban
- DLL-eket, VBS-szkripteket vagy távoli tartalmat jelző hasznos terhek

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Az Outlook kezdőlapjának eltérítése és megkerülése (T1137.004)
- **ID:** `T1137_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)
- **Leírás:** Érzékeli az Outlook mappa kezdőlapjainak és a WebView áthidaló kulcsainak jogosulatlan módosítását:
- Nyomon követi azokat a rendszerleíró adatbázis-módosításokat, amelyek lehetővé teszik tetszőleges kód végrehajtását mappakattintásokkal
- Figyeli a gyanús URL-eket vagy a helyi fájlhivatkozásokat
- Érzékeli a nem szabványos folyamatokat, amelyek megpróbálják módosítani a rendszerleíró adatbázist

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Az Office biztonsági házirendjének manipulálása (T1137.005)
- **ID:** `T1137_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)
- **Leírás:** Felismeri a Microsoft Office biztonsági szabályzatainak jogosulatlan módosításait a következők figyelésével:
- Globális makró engedélyezési változások
- Nem megbízható hálózati helyek hozzáadása
- Szabványmódosítások nem szabványos folyamatokból

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Office-bővítmény bináris állandósága (T1137.006)
- **ID:** `T1137_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Felismeri a jogosulatlan Office-bővítmények (.wll, .xll) fennmaradását a következők figyelésével:
- Nem megbízható fájlhelyek (Word/Excel indító mappák, AddIns mappa)
- Office-bővítmények binárisai gyanús írókkal (PowerShell, beállítás, böngésző stb.)
- Kizárja az ismert megbízható alkalmazásokat a hamis pozitívumok csökkentése érdekében

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lopakodó deobfuszkálás/dekódolás (T1140)
- **ID:** `T1140.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a deobfuszkálási és dekódolási tevékenységet a következő megfigyeléssel:
- Natív Windows-eszközök (certutil, expand, extrac32)
- Binárisok dekódolása nem végrehajtható forrásokból (txt, jpg, xml, log)
- Gyanús szülőfolyamatok vagy érzékeny/nem megbízható könyvtárakat céloznak meg

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
- **Leírás:** Érzékeli az „ExtensionInstallForcelist” vagy „ExtensionInstallSources” rendszerleíró kulcsok létrehozását.
A támadók ezeket a rosszindulatú bővítmények telepítésére használják, amelyeket a felhasználó nem tud eltávolítani
és lehetővé tenni a nem hivatalos webáruházakból történő telepítést.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Böngészőmunkamenet-eltérítés (T1185)
- **ID:** `T1185.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Az illetéktelen hozzáférés figyelésével észleli a fejlett böngésző-munkamenet-eltérítést
a böngésző cookie-adatbázisaihoz nem megbízható vagy aláíratlan folyamatokból, vagy a
gyanús helyek, például \Temp vagy \AppData.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Kényszerített hitelesítés (T1187)
- **ID:** `T1187.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a kényszerített hitelesítési kísérleteket (NTLM Relay/Coercion) a következők figyelésével:
- Gyanús UNC útvonalminták
- WebDAV átirányítás
- RPC interfész visszaélés (EfsRpc, PrinterChangeNotification, LSARPC stb.)
- Nem megbízható folyamatokból származó kimenő hitelesítési triggerek

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Böngészőből származó shell vagy rendszereszköz végrehajtása
- **ID:** `T1189.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a webböngészők által keltett gyanús gyermekfolyamatokat.Ez a minta nagyon magas
a Drive-by Compromise (T1189) révén történő sikeres kiaknázást jelzi,
ahol egy exploit kit közvetlenül a böngésző memóriájából indít el egy hasznos terhelést vagy egy shellt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús Cross-Site Scripting (XSS) kísérlet észlelve a webszerveren
- **ID:** `T1190.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a potenciális Cross-Site Scripting (XSS) kísérleteket azáltal, hogy azonosítja a HTTP-kérésekben előforduló gyakori tükrözött és kódolt XSS-adatokat, a paraméter-alapú befecskendezési mintákra összpontosít, és kizárja a tipikus automatizált szkennereket a hamis pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**


---
## Nagy pontosságú ellátási lánc-kompromittálódás észlelése (frissítés utáni anomália)
- **ID:** `T1195.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WINGET.EXE](https://lolbas-project.github.io/lolbas/), [PROCDUMP.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a törvényes szoftverfrissítők által létrehozott vagy aláírt gyanús gyermekfolyamatokat
telepítők.Azokra a felderítési és hitelesítő adatokhoz való hozzáférési eszközökre összpontosít, amelyeknek soha nem szabadna lennie
egy szabványos szoftverkarbantartási vagy frissítési ciklus része.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú függőségi mérgezés-észlelés
- **ID:** `T1195_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a csomagkezelők vagy az összeállítási eszközök által létrehozott gyanús gyermekfolyamatokat.
A könyvtár ideje alatt elindított felderítési és kiszűrési tevékenységekre összpontosít
telepítés vagy fordítás (telepítés előtti/utáni szkriptek).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity veszélyeztetett bináris tevékenység (frissítés után)
- **ID:** `T1195_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús gyermekfolyamatokat, amelyeket megbízható üzleti alkalmazások szültek
bináris szinten kompromittálódott.Az átmenetre összpontosít
jogos alkalmazás-végrehajtás jogosulatlan felfedezés vagy szkript-végrehajtás.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú hardver/firmware manipuláció észlelése
- **ID:** `T1195_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a firmware-villogó eszközök végrehajtását vagy az alacsony szintű hardver-hozzáférést
segédprogramok gyanús környezetben.Ez a potenciális utólagos kizsákmányolást célozza meg
feltört hardver vagy UEFI rootkitek telepítési kísérletei.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús fájlok letöltése a Bitsadmin segítségével (High Fidelity)
- **ID:** `T1197.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a bitsadmin.exe, egy elavult, de még mindig visszaélt Windows LOLBAS segédprogram használatával végrehajtott gyanús fájlletöltéseket.A szabály a támadókra jellemző használati mintákra, a végrehajtási környezetre és a letöltési célokra összpontosít, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú megbízható kapcsolati visszaélések észlelése
- **ID:** `T1199.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Felderíti a gyanús felfedezési és felderítési tevékenységeket, amelyek innen származnak
megbízható bemeneti pontok (RDP, Citrix, VPN).Kiszűri a szabványos adminisztrációt
viselkedés konkrét szülő-gyermek folyamatláncokra és szokatlan érvekre összpontosítva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rosszindulatú hardver által kiváltott parancsvégrehajtás (HID-injektálás)
- **ID:** `T1200.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rosszindulatú HID-eszközökre (Rubber Ducky, Bash Bunny) jellemző gyanús parancsvégrehajtási mintákat.
A gyors shell spawningre összpontosít a felhasználói munkamenet környezetéből származó "lopakodó" jelzőkkel
szabványos GUI interakció nélkül.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Jelszóházirend-felderítés észlelése (T1201)
- **ID:** `T1201.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a tartományi vagy helyi jelszóházirendek célzott felsorolását.
A támadók által a kalibráláshoz használt felderítési mintákra összpontosít
brute-force támadások, miközben kiszűrik a legitim rendszer- vagy adminisztrátori tevékenységet.

Monitorok:
- Natív Windows-eszközök: net.exe, net1.exe
- PowerShell ActiveDirectory-parancsmagok a jelszóházirendekhez
- Gyanús kimeneti átirányítás vagy exportálási minták
- Végrehajtás nem megbízható vagy közepes integritású szülőfolyamatokból

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Közvetett parancsvégrehajtás proxy binárisokon keresztül (T1202)
- **ID:** `T1202.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FORFILES.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [PCALUA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a közvetett parancsvégrehajtáshoz vagy proxyhoz gyakran visszaélt binárisok végrehajtását.
A nem szabványos szülőfolyamatokra és a gyanús parancssori argumentumokra összpontosít:
- pcalua.exe
- forfiles.exe
- conhost.exe

Figyeli a váratlan alkalmazások által kezdeményezett szkriptek, binárisok és DLL-ek végrehajtását,
általában védelmi kikerülésre vagy földön kívüli támadásokra használják.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity kliensoldali kihasználás és shell spawning
- **ID:** `T1203.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús gyermekfolyamatokat, amelyeket az ügyfélalkalmazások (Office, Böngészők,
PDF olvasók).A shell-végrehajtásra, a felfedezőeszközökre és a LOLBin eredetére összpontosít
sandbox vagy alacsony integritású alkalmazási környezetből.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús gyermekfolyamat, amelyet a Microsoft Office alkalmazás idézett elő (High Fidelity)
- **ID:** `T1204.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [MSACCESS.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Microsoft Office-alkalmazások által generált gyanús gyermekfolyamatokat, amelyek makróval való visszaélésre, DDE-kihasználásra vagy dokumentum alapú rosszindulatú programok futtatására utalnak.A szabály a támadókra jellemző gyermekfolyamatokra, parancssori mintákra és a felhasználó által írható végrehajtási környezetre összpontosít, hogy minimalizálja a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## A rosszindulatú hivatkozás nagy pontosságú felhasználói végrehajtása (T1204.001)
- **ID:** `T1204_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús gyermekfolyamatokat, amelyeket webböngészők, e-mail kliensek, ill
azonnali üzenetküldők.A LOLBinekre és a szkript értelmezőkre összpontosít
hálózattal kapcsolatos vagy zavart argumentumok, amelyek rosszindulatú hivatkozás-végrehajtásra utalnak.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rosszindulatú fájlok nagy pontosságú felhasználói végrehajtása
- **ID:** `T1204_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az irodai hatékonyságnövelő alkalmazások által előidézett gyanús gyermekfolyamatokat,
PDF-olvasók vagy archiváló eszközök.Kifejezetten a makró által kezdeményezetteket célozza meg
vagy a rendszereszközök (LOLBins) kihasználás által vezérelt végrehajtása.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú végrehajtás a beépített virtuális lemezről (T1204.003)
- **ID:** `T1204_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a virtuális lemezmeghajtóról (ISO, VHD, VHDX) futó gyanús binárisokat vagy szkripteket.
A nem C: meghajtókról az explorer.exe-n keresztül elindított LOLBinekre és szkript értelmezőkre összpontosít,
a Mark-of-the-Web megkerülését szolgáló rosszindulatú programok gyakori mintája.

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
## Forgalomjelző és port kopogtatási tevékenység (T1205)
- **ID:** `T1205.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a port kopogtatás / közlekedési jelzés végrehajtására vagy kiváltására irányuló kísérleteket.
Monitorok:
- Nyers csomagrögzítő eszközök (Npcap/WinPcap/sniffer eszközök)
- Gyanús tűzfalszabály-módosítások, amelyek lehetővé teszik az UDP/ICMP/Bármely portot
- Végrehajtás nem megbízható parancsfájlokból vagy shell környezetekből

Ezt a technikát gyakran használják a támadók, hogy lopva jelezzék a C2-t,
megkerülheti a tűzfalakat, vagy rejtett szolgáltatásokat indíthat el.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Port Knocking vagy Raw Socket Listener telepítése (T1205.001)
- **ID:** `T1205_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Port Knocking vagy a nyers csomag jogosulatlan megvalósítását
hallgatók figyeléssel:
- nyers csomagrögzítő illesztőprogramok/eszközök regisztrációja
- gyanús tűzfalmódosítások, amelyek lehetővé teszik az UDP/ICMP/Bármely portot
- végrehajtás nem megbízható parancsfájlokból vagy shell környezetekből

A támadók kihasználhatják ezt a technikát, hogy lopva jelezzék a C2-t,
megkerülheti a tűzfalakat, vagy rejtett szolgáltatásokat indíthat el.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## WFP kiemelés regisztrációja vagy kernel-illesztőprogram-beállítás (T1205.002)
- **ID:** `T1205_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús Windows Filtering Platform (WFP) feliratot vagy szűrőt
manipuláció és kernel-illesztőprogramok állomásoztatása nem megbízható folyamatvonalból.
A támadók rosszindulatú WFP-feliratokat vagy socket-szűrőket regisztrálhatnak az engedélyezéshez
lopakodó port kopogtatás, rejtett C2 vagy forgalom elfogása.

Ez a szabály korrelál:
- WFP / kiemelés / szűrő módosítása netsh vagy PowerShell segítségével
- Kernel-illesztőprogram-szolgáltatás létrehozása gyanús útvonalakból
- Végrehajtás interaktív vagy script motorokból
- Nem tartalmazza az ismert EDR/biztonsági szerszámozási útvonalakat

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rogue DC / DCSárnyékérzékelés (T1207)
- **ID:** `T1207.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a gyanús tartományvezérlő topológia változásait, beleértve:
- nTDSDSA objektumok létrehozása nem DC fiókokkal
- A kritikus tartományvezérlő SPN-ek regisztrációja (E3514235 / GC)
- Rogue DC telepítésre vagy DCShadow támadásokra utal
A jogos domain rendszergazdák és a meglévő DC-fiókok kizárva a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Remote Service RCE/Post Exploitation Spawn Detection (T1210)
- **ID:** `T1210.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a távoli szolgáltatások kihasználását követő kihasználás utáni viselkedést
(SMB, RPC, Spooler, WMI, SQL, IIS).

A következőkre összpontosít:
- A szolgáltatás interaktív héjakat készít
- Kódolt vagy rejtett PowerShell-végrehajtás
- LOLBin proxy végrehajtás
- Gyanús végrehajtási utak
- RENDSZER/HÁLÓZATI SZOLGÁLTATÁS környezeti visszaélés

Úgy tervezték, hogy csökkentse a törvényes informatikai hangszerelésből származó zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Sandbox Breakout / Privilege Escalation Exploitation (T1211)
- **ID:** `T1211.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [COMPUTERDEFAULTS.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EVENTVWR.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a privilégiumok potenciális eszkalációját a sebezhető személyek kihasználása révén
ügyfélalkalmazások (böngészők, Office, PDF-olvasók) a következők azonosításával:
- Sandbox kitörési viselkedés
- Gyanús LOLBin gyermekfolyamatok
- Kódolt/rejtett parancsvégrehajtás
- UAC bypass és token-visszaélés jelzői
Úgy tervezték, hogy csökkentse a legális böngésző/Office alfolyamatok okozta zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hitelesítési adatok szolgáltatás kihasználásának észlelése (T1212)
- **ID:** `T1212.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a Windows hitelesítési szolgáltatások potenciális kihasználását
(LSASS, LogonUI, Spooler, LSM) figyeléssel:
- A hitelesítő szolgáltatások által kiváltott illegális gyermekfolyamatok
- Memória befecskendezése / fényvisszaverő terhelés / cső visszaélési kísérletek
- Gyanús végrehajtás a felhasználói ideiglenes vagy letöltési könyvtárakból
Nem tartalmazza a jogszerű biztonsági ügynöki tevékenységet és a Windows hibajelentést.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Belső adattár tömegkiíratásának észlelése (T1213)
- **ID:** `T1213.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan tömeges adatgyűjtést belső tudásbázisokból
(Confluence, Jira, SharePoint, Wiki) figyeléssel:
- Gyanús API-vezérelt exportparancsok
- Tömeges vagy rekurzív letöltési kísérletek
- Nem szabványos folyamatvégrehajtási környezetek
- Áthelyezés/exportálás ideiglenes vagy nyilvános könyvtárakba
Nem tartalmazza a megbízható automatizálást és a rendszerfolyamatokat a hamis pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Összefolyási tömeg kaparás észlelése (T1213.001)
- **ID:** `T1213_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli az Atlassian Confluence-ből az illetéktelen tömegtartalom-kinyerést a következő megfigyeléssel:
- Gyanús API-vezérelt olvasások és exportálások (/rest/api/content, /rest/api/space)
- CLI-alapú kaparóeszközök (curl, wget, confluence-cli)
- PowerShell/Python automatizálás
- Áthelyezés/exportálás ideiglenes vagy nyilvános könyvtárakba
A nem szabványos végrehajtási környezetek és a nem megbízható automatizálás megjelölve.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Vállalati SharePoint tömeges adatok kiszűrésének észlelése (T1213.002)
- **ID:** `T1213_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a SharePoint Online rendszerből származó, jogosulatlan tömeges adatgyűjtést a következők figyelésével:
- PnP PowerShell tevékenység
- Tömeges REST API lekérdezések
- SharePoint Online Management Shell használata
- Nem szabványos végrehajtási környezetek (nem rendszergazdai automatizálás)
Az exportált tartalom átmeneti/nyilvános könyvtárakban történő állomásoztatása szintén meg van jelölve.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Vállalati tudásbázis tömeges kaparás/tükrözés észlelése (T1213.003)
- **ID:** `T1213_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy mennyiségű belső tudásbázis kaparási és tükrözési tevékenységét
(Confluence, Wiki, Stack Overflow for Teams, Git-alapú dokumentáció)
rekurzív letöltési jelzők használata, REST API tartalombővítés, fej nélküli szkriptmotorok,
és tömeges levéltári minták.

Azokra a nem böngészőmotorokra összpontosít, amelyek szisztematikus gyűjtést végeznek indikatív módon
a szellemi tulajdon színpadi kiszivárgása.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows rendszerszkript proxy végrehajtása (T1216)
- **ID:** `T1216.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [MANAGE-BDE.WSF](https://lolbas-project.github.io/lolbas/), [PUBPRN.VBS](https://lolbas-project.github.io/lolbas/), [SYNCAPPVPUBLISHINGSERVER.VBS](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a megbízható Windows aláírt szkriptekkel (MITRE ATT&CK T1216) való nagy megbízhatóságú visszaélést a rosszindulatú kód proxy futtatása érdekében.Hálózati alapú triggerekre, anomális érvek befecskendezésére és gyanús szülő-gyermek folyamatkapcsolatokra összpontosít.Szűri a jogos adminisztratív környezeteket a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Pubprn.vbs Script proxy végrehajtása (T1216.001)
- **ID:** `T1216_001.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [PUBPRN.VBS](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a pubprn.vbs aláírt Windows-szkripttel való nagy megbízhatóságú visszaélést a távoli szkriptletek (.sct) végrehajtásának proxyjával (MITRE ATT&CK T1216.001).
A „script:” protokollt, HTTP/UNC hivatkozásokat, SOAP-hívásokat és gyanús folyamatsort használó anomális argumentumbefecskendezésre összpontosít, miközben kiszűri a legitim adminisztratív végrehajtási kontextusokat és a localhost-alapú szkripteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Böngészőinformációk felfedezése (T1217)
- **ID:** `T1217.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú, jogosulatlan böngészőinformációk felfedezését (MITRE ATT&CK T1217).Azokra a nem böngészős folyamatokra összpontosít, amelyek érzékeny profilfájlokhoz (SQLite/JSON) hozzáférnek, vagy rendellenes átirányítást/kibontást hajtanak végre parancssori vagy parancsfájl-eszközök használatával.
Tartalmazza a több böngésző támogatását (Chrome, Edge, Firefox, Brave) és a többprofil észlelést, miközben szűri a törvényes vállalati IT-eszközöket a hamis pozitívumok minimalizálása érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows rendszer bináris proxy végrehajtása
- **ID:** `T1218.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CMSTP.EXE](https://lolbas-project.github.io/lolbas/), [CONTROL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [HH.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [ODBCCONF.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a megbízható Windows binárisokkal való nagy megbízhatóságú visszaélést a rosszindulatú végrehajtás proxyja céljából (MITRE ATT&CK T1218).Az ellenfelek olyan bináris fájlokat használnak fel, mint a rundll32.exe, regsvr32.exe, msiexec.exe, installutil.exe, mshta.exe, control.exe, cmstp.exe, odbcconf.exe vagy hh.exe, hogy kódot hajtsanak végre nem szabványos útvonalakról, távoli forrásokból vagy többfolyamat-határhívásokon keresztül.
A rendellenes szülőfolyamatokra, a gyanús parancssori argumentumokra, a felhasználók által írható útvonalakra és az áthelyezett binárisokra összpontosít.Szűri a legitim rendszer által felügyelt végrehajtási kontextust, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## HH.exe CHM/ITS proxy végrehajtás
- **ID:** `T1218_001.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a hh.exe nagy megbízhatóságú visszaélést a proxy-végrehajtáshoz (MITRE ATT&CK T1218.001).Az ellenfelek a HTML Súgót (hh.exe) felhasználhatják rosszindulatú CHM-tartalom futtatására, CHM-fájlok visszafordítására vagy távoli hasznos adatok lekérésére ITS/MSITStore protokollokon keresztül.
A szabály a rendellenes szülőfolyamatokra, a távoli vagy felhasználó által írható CHM-végrehajtásra, a gyanús protokollkezelőkre, a visszafordítási visszaélésekre, az áthelyezett bináris fájlokra és a szokatlan integritási környezetekre összpontosít.
Úgy tervezték, hogy csökkentse az alkalmazás súgófájljainak használatából származó zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Control.exe CPL/DLL proxy végrehajtása
- **ID:** `T1218_002.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONTROL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Nagy megbízhatóságú visszaélést észlel a control.exe-vel a proxy végrehajtásához (MITRE ATT&CK T1218.002).Az ellenfelek kihasználhatják a control.exe fájlt, hogy rosszindulatú .cpl vagy DLL fájlokat töltsenek be a felhasználó által írható vagy távoli helyekről.
A szabály a rendellenes szülőfolyamatokra, a control.exe szabványos rendszerkönyvtárakon kívüli végrehajtására, a gyanús parancssori kiterjesztésekre, a felhasználók által írható útvonalakra és a szokatlan integritási környezetekre összpontosít.Az OriginalFileName az átnevezett bináris fájlok észlelésére szolgál.
Úgy tervezték, hogy csökkentse a vezérlőpult törvényes tevékenységéből származó zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## MsiExec proxy végrehajtás
- **ID:** `T1218_003.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli az msiexec.exe nagy megbízhatóságú visszaélést a proxy végrehajtásához (MITRE ATT&CK T1218.003).Az ellenfelek általában kihasználják az msiexec-et távoli MSI-csomagok letöltéséhez és végrehajtásához, vagy a hasznos terhek csendes telepítéséhez.
A szabály a távoli erőforrás-végrehajtásra, a csendes telepítési jelzőkre, a felhasználó által írható útvonal-végrehajtásra, a gyanús szülőfolyamatokra, az áthelyezett binárisokra és a rendellenes integritási környezetekre összpontosít.
Úgy tervezték, hogy csökkentse a legális vállalati szoftvertelepítési és -felügyeleti keretrendszerekből származó zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## InstallUtil .NET proxy végrehajtás
- **ID:** `T1218_004.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Az InstallUtil.exe nagy megbízhatóságú visszaélést észlel a proxy végrehajtásához (MITRE ATT&CK T1218.004).Az ellenfelek az InstallUtil alkalmazást használják fel rosszindulatú .NET-szerelvények futtatására telepítő/eltávolító módszerekkel.
A szabály a gyanús eltávolítási jelzőkre, a felhasználó által írható vagy távoli útvonalakról történő összeállítások végrehajtására, a rendellenes szülőfolyamatokra, az áthelyezett bináris használatra és a szokatlan integritási környezetekre összpontosít.
Úgy tervezték, hogy csökkentse a legitim .NET-keretrendszer telepítéséből és az MSI-vezérelt telepítési tevékenységből származó zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## A távoli szkript gyanús Mshta végrehajtása (high Fidelity)
- **ID:** `T1218_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az mshta.exe gyanús végrehajtását, amellyel közvetlenül távoli URL-címekről futtatják a szkripteket. Ez egy gyakori LOLBAS technika, amelyet a támadók a kezdeti végrehajtáshoz és a hasznos terhelés állomásoztatásához használnak.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús Msiexec telepítés távoli URL-ről (High Fidelity)
- **ID:** `T1218_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az msiexec.exe gyanús használatát az MSI-csomagok távoli URL-címekről történő közvetlen telepítésére. Ezzel a technikával a támadók LOLBAS-módszerként gyakran visszaélnek.A szabály a támadókra jellemző parancssori mintákra és a végrehajtási környezetre összpontosít, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Odbcconf REGSVR proxy végrehajtás
- **ID:** `T1218_008.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [ODBCCONF.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az odbcconf.exe nagy megbízhatóságú visszaélést a REGSVR-műveleten keresztül proxy-végrehajtáshoz (MITRE ATT&CK T1218.008).
A szabály a rendhagyó REGSVR-hívási mintákra, a felhasználó által írható vagy távoli útvonalakról való DLL-ek végrehajtására, a gyanús szülőfolyamatokra, az áthelyezett binárisokra és a szokatlan integritási környezetekre összpontosít.
Úgy tervezték, hogy csökkentse a legitim telepítő által vezérelt ODBC konfigurációs tevékenységből származó zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Regsvcs/Regasm .NET proxy végrehajtás
- **ID:** `T1218_009.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a regsvcs.exe vagy regasm.exe nagy megbízhatóságú visszaéléseit rosszindulatú .NET-szerelvények proxy futtatása céljából (MITRE ATT&CK T1218.009).
A szabály a gyanús eltávolítási jelzők (/U, /uninstall), a felhasználó által írható vagy távoli útvonalakról történő összeállítások végrehajtására, a rendellenes szülőfolyamatokra, az integritási szintű kontextusra és az alapértelmezett .NET-keretrendszer-könyvtárakon kívüli áthelyezett bináris végrehajtásra összpontosít.
Úgy tervezték, hogy csökkentse a törvényes .NET regisztrációból és az MSI-vezérelt telepítési tevékenységből származó zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús Regsvr32 végrehajtás, amely LOLBAS-visszaélést jelez (high Fidelity)
- **ID:** `T1218_010.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a regsvr32.exe gyanús használatát, amely általában a LOLBAS-visszaéléshez kapcsolódik (Squiblydoo-technika), beleértve a parancsfájlok, távoli rakományok vagy DLL-ek futtatását a felhasználó által írható helyekről, a támadókra jellemző parancssori argumentumokkal.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús Rundll32 végrehajtás szkripttel vagy távoli hasznos adattartalommal (high Fidelity)
- **ID:** `T1218_011.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [SHELL32.DLL](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rundll32.exe gyanús használatát, amely általában a LOLBAS-szal való visszaéléshez kapcsolódik, beleértve a JavaScript-végrehajtást, a HTML-alkalmazásokat, valamint a rakományok távoli vagy a felhasználó által írható helyekről történő betöltését.A szabály minimálisra csökkenti a hamis pozitívumot azáltal, hogy a támadókra jellemző parancssori mintákra és a végrehajtási környezetre összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Verclsid proxy végrehajtása COM Object Abuse segítségével
- **ID:** `T1218_012.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [VERCLSID.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a verclsid.exe nagy megbízhatóságú visszaélést a proxy végrehajtásához (MITRE ATT&CK T1218.012) rosszindulatú COM-objektum betöltése révén.
A szabály a rendellenes szülőfolyamatokra, a gyanús CLSID-hívási mintákra, a szabványos rendszerútvonalakon kívüli végrehajtásra, a felhasználó által írható címtárak bevonására és a szokatlan integritási környezetekre összpontosít.
Úgy tervezték, hogy csökkentse a legitim shell COM-érvényesítési tevékenységből származó zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rundll32 proxy végrehajtása (LOLBAS visszaélés)
- **ID:** `T1218_013.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [PCWUTL.DLL](https://lolbas-project.github.io/lolbas/), [SHELL32.DLL](https://lolbas-project.github.io/lolbas/), [URL.DLL](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a rundll32.exe nagy megbízhatóságú visszaélést a proxy végrehajtásához (MITRE ATT&CK T1218.013).A szabály a gyanús parancssori mintákra, a parancsfájl-alapú hívásokra, a nem DLL fájlkiterjesztésekre, a felhasználó által írható helyekről történő végrehajtásra, a távoli URL-hívásokra és a rendellenes szülőfolyamatokra összpontosít.
Nagy pontosságú vállalati észlelésre tervezték, csökkentett zajjal a törvényes vezérlőpultból és a rendszertevékenységből.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús MMC-proxy-végrehajtás nem megbízható MSC-n vagy COM-eltérítésen keresztül
- **ID:** `T1218_014.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az mmc.exe gyanús végrehajtását, amelyet proxy-végrehajtáshoz (T1218.014) lehet visszaélni rosszindulatú .msc konzolfájlokon vagy COM-eltérítésen keresztül.
A szabály azonosítja az mmc.exe fájlt, amely nem interaktív vagy parancsfájl-alapú szülőfolyamatokból indult, a konzolfájlok futtatását a felhasználó által írható helyekről, távoli elérési utakat vagy gyanús parancssori jelzőket.
Nagy pontosságú észlelésre tervezték vállalati környezetekben, csökkentett téves pozitív eredményekkel.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús szolgáltatás létrehozása a távfelügyeleti eszközökön keresztül a jóváhagyott felügyeleti körön kívül
- **ID:** `T1219.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a legális távoli adminisztrációs eszközökhöz (pl. PsExec, PAExec, RemCom) általában társított Windows-szolgáltatások létrehozását, ha azokat a jóváhagyott vállalati felügyeleti mintákon kívül hajtják végre.
Az ellenfelek gyakran visszaélnek ezekkel az eszközökkel oldalirányú mozgáshoz azáltal, hogy távolról hoznak létre ideiglenes szolgáltatásokat a célrendszereken.A szabály szűri az ismert felügyeleti gazdagépeket, szolgáltatásfiókokat és jóváhagyott vállalati szerszámozási útvonalakat a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## XSL-szkript feldolgozás (T1220)
- **ID:** `T1220.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WMIC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Nem szabványos könyvtárakban vagy távoli URL-címeken található XSL-stíluslapok segítségével észleli a gyanús WMIC-végrehajtásokat.Ezt a viselkedést általában az alkalmazások engedélyezőlistájának megkerülésére és tetszőleges parancsfájlok végrehajtására használják.Kiszűri az ismert legitim WBEM-könyvtárakat és a gyakori XSL-sablonokat, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Irodai sablon befecskendezése (T1221)
- **ID:** `T1221.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Microsoft Office-alkalmazásokat, amelyek távoli sablonokat töltenek le a nem Microsoft infrastruktúrából, ami potenciálisan rosszindulatú sabloninjektálást jelez.Figyeli az Office-alkalmazások és a gyanús külső gazdagépek közötti hálózati kapcsolatokat, kivéve a megbízható Microsoft-tartományokat és a belső IP-tartományokat.

#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows engedélyek módosítása (T1222)
- **ID:** `T1222.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús fájlengedély-módosításokat azáltal, hogy azonosítja a natív eszközök (icacls, takeown, cacls, attrib) használatát széles hozzáférésű jelzőkkel (Teljes felügyelet, Mindenki), amelyeket nem szabványos szülőfolyamatok vagy gyanús útvonalak kezdeményeztek.Kiszűri a megbízható rendszertelepítőket és a felügyeleti műveleteket a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows fájlengedélyek módosítása (T1222.001)
- **ID:** `T1222_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a célzott fájlengedély-módosításokat azáltal, hogy azonosítja a széles körű hozzáférési engedélyeket (pl. Teljes felügyelet, Mindenki) vagy az öröklődés blokkolását.A gyanús vagy nem megbízható folyamatok által kezdeményezett műveletekre és/vagy az érzékeny címtárak megcélzására összpontosít, miközben kiszűri a legitim rendszer- és adminisztrációs műveleteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Linux fájlengedélyek módosítása (T1222.002)
- **ID:** `T1222_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a célzott Linux-engedély-módosításokat azáltal, hogy azonosítja a nagy kockázatú attribútum-módosításokat, például a SUID-t, a megváltoztathatatlan vagy csak hozzáfűzhető jelzőket, valamint az érzékeny rendszerútvonalakon végrehajtott tömeges engedélymódosításokat.A privilegizált vagy webes szolgáltatásfiókok által kezdeményezett műveletekre összpontosít, miközben kiszűri a megbízható rendszerműveleteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Execution Guardrails Discovery (T1480)
- **ID:** `T1480.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a célzott végrehajtási korlátokat a nem privilegizált felhasználók vagy gyanús szülőfolyamatok által kezdeményezett rendellenes környezetfelderítési minták azonosításával.Kiszűri a gyakori adminisztrációs és rendszerzajt, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Environmental Keying Discovery (T1480.001)
- **ID:** `T1480_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a célzott környezeti kulcsozást a hardveres ujjlenyomatok és a gyanús, nem megbízható vagy nem szabványos szülői folyamatok által kezdeményezett, gépspecifikus regisztrációs vagy AD-keresések azonosításával.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Domain Trust Discovery (T1482)
- **ID:** `T1482.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a tartomány- és erdőtrösztök szisztematikus felsorolását, összpontosítva a rendellenes folyamatvonalra, például a munkaállomásokon lévő interaktív héjakra és az olyan eszközök által használt felderítési mintákra, mint a BloodHound/SharpHound.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Domainházirend-manipuláció és csoportházirend-objektumokkal való visszaélés (T1484)
- **ID:** `T1484.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kritikus tartományi szabályzatok jogosulatlan módosításait azáltal, hogy figyeli a fájlrendszer írásait a SYSVOL mappába és az Active Directory GPO hivatkozásmódosításait.Kiszűri a szabványos adminisztrációs műveleteket, például a GPMC-t és az ismert rendszerfolyamatokat a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Csoportházirend módosítása és visszaélés (T1484.001)
- **ID:** `T1484_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a csoportházirend-objektum (GPO) jogosulatlan módosításait azáltal, hogy figyeli a fájlrendszer kritikus házirend-sablonjaira írt írásait a SYSVOL-ban, és korrelálja azokat a gyanús folyamattevékenységekkel.Kiszűri a szabványos DFSR-replikációs és felügyeleti konzolműveleteket a hamis pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Domain Trust Tampering & SID Filtering Bypass (T1484.002)
- **ID:** `T1484_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli az Active Directory Domain Trust kapcsolatok magas kockázatú módosításait, beleértve a SID-szűrés (karantén) letiltását és a jogosulatlan bizalom létrehozását.Összeegyezteti az AD-objektum-módosításokat, a biztonsági eseményeket és az eszközvégrehajtást, hogy azonosítsa a potenciálisan rosszindulatú tevékenységeket a megbízható felügyeleti kontextusokon kívül.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Adatmegsemmisítés (T1485/T1490)
- **ID:** `T1485.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CIPHER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WBADMIN.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szisztematikus adatmegsemmisítési kísérleteket azáltal, hogy figyeli a folyamatlétrehozási eseményeket, amelyek magukban foglalják a Volume Shadow Copies (VSS) törlését, a biztonságos fájlmegsemmisítő segédprogramokat (sdelete, titkosítás) és a tömeges rekurzív törléseket.Figyelmeztetések gyanús szülőfolyamatokról vagy nem ideiglenes címtárakat célzó műveletekről.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ransomware-előkészítési tevékenység észlelve a Windows Host-on (High Fidelity)
- **ID:** `T1486.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a zsarolóvírus-előkészítési tevékenységet azáltal, hogy azonosítja a rövid időn belül végrehajtott több helyreállítási-gátlási és védekezési-elkerülési műveletet.Ez magában foglalja a helyreállítási lehetőségek letiltását, az árnyékmásolatok törlését és a biztonsággal kapcsolatos szolgáltatások leállítását.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szervizmegálló (T1489)
- **ID:** `T1489.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kritikus rendszer- és biztonsági szolgáltatások leállítására vagy letiltására irányuló jogosulatlan kísérleteket.Figyelemmel kíséri a gyanús szülőfolyamatokból kezdeményezett szolgáltatásvezérlő eszközöket vagy olyan nagy értékű védekező mechanizmusokat célzó folyamatlétrehozási eseményeket, mint az EDR, vírusirtó és rendszer-helyreállítási szolgáltatások.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Kötet árnyékmásolatok gyanús törlése a VSSAdminon keresztül (High Fidelity)
- **ID:** `T1490.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Volume Shadow Copies gyanús törlését a vssadmin.exe használatával, amely gyakran megfigyelhető zsarolóvírusok és pusztító támadások során.A szabály a támadókra jellemző parancssori argumentumokra, a nem szolgáltatási végrehajtási környezetre összpontosít, és kizárja az ismert biztonsági mentési megoldásokat a hamis pozitívumok minimalizálása érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Elrontás (T1491)
- **ID:** `T1491.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A gyanús fájlok figyelésével észleli a webhely jogosulatlan megrongálását
manipulációk (mozgatás, másolás, visszhang, Set-Content, csere) a web-rooton belül
nem szabványos vagy potenciálisan veszélyeztetett címtárak
webszolgáltatási folyamatok (pl. w3wp.exe, httpd.exe).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Belső sérülés (T1491.001)
- **ID:** `T1491_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A jogosulatlan módosítások figyelésével észleli a belső rendszer károsodását
asztali háttérképekhez, jogi közleményekhez és bejelentkezési szalaghirdetésekhez Registry-n vagy CLI-n keresztül,
miközben kiszűri a GPO által vezérelt és a rendszer által kezdeményezett változtatásokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Külső rontás (T1491.002)
- **ID:** `T1491_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A gyanús fájlok azonosításával észleli a külső webhely jogosulatlan megrongálását
webszerver által végrehajtott manipulációs parancsok (mozgatás, másolás, visszhang, Set-Content).
dolgozói folyamatok az érzékeny webroot könyvtárakban.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Firmware korrupció (T1495)
- **ID:** `T1495.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WBEMTEST.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Figyeléssel észleli a lehetséges firmware-sérülést vagy az illetéktelen villogást
alacsony szintű hardver-hozzáférési eszközök és firmware-frissítési segédprogramok
nem megbízható folyamatvonalakból (pl. böngészőkből, irodai alkalmazásokból vagy ideiglenes mappákból).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Erőforrás-eltérítés (T1496)
- **ID:** `T1496.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a jogosulatlan erőforrás-eltérítést (kriptomásolást) a következő megfigyelésével
specifikus bányászprotokollok (rétegek), algoritmusjelzők és hardver
nem megbízható folyamatvonalakból származó optimalizálási argumentumok.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Virtualizáció/Sandbox Evasion (T1497)
- **ID:** `T1497.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a kifinomult sandbox-elkerülést a gyors, több vektoros figyeléssel
virtualizációs ellenőrzések (BIOS, MAC, CPU, lemez) és késleltetési taktika
gyanús könyvtárakon belüli nem megbízható folyamatok indították el.

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
- **Leírás:** Érzékeli a virtualizációs műtermékek nem rendszer általi illetéktelen felfedezését,
megbízhatatlan folyamatok.Kiszűri a törvényes telepítőket és a rendszerszolgáltatásokat
hogy a rosszindulatú programok elkerülési technikáira összpontosítson.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Felhasználói interakciók elkerülése (T1497.002)
- **ID:** `T1497_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kifinomult felhasználói interakciók kijátszását azáltal, hogy azonosítja az aláíratlan vagy
gyanúsan elhelyezkedő folyamatok, amelyek emberközpontú API-kat kérnek le (egér, billentyűzet, legutóbbi fájlok)
legitim UI kontextus nélkül.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Időalapú kijátszás (T1497.003)
- **ID:** `T1497_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A nem szabványos késleltetési mechanizmusok figyelésével észleli a kifinomult időalapú kijátszást
(ping, választás, időtúllépés) nem megbízható binárisok által kezdeményezett.A hosszú távú istállókat célozza meg
a homokozó elemzési határok kimerítésére szolgál.

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
- **Leírás:** Érzékeli a célzott hálózati szolgáltatásmegtagadási kísérleteket (elárasztás, erősítés)
az alacsony szintű csomagkezelési eszközök és a nagy sávszélesség figyelésével
nem megbízható vagy gyanús folyamatvonalakból származó stressztesztek.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Közvetlen áramlású árvíz (T1498.001)
- **ID:** `T1498_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [PKTMON.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy pontosságú közvetlen hálózati elárasztási kísérleteket (SYN, UDP, ICMP)
a folyamatok agresszív csomaggenerálási paraméterekkel történő figyelésével
nem megbízható vagy gyanús folyamatvonalból származik.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Végpont szolgáltatásmegtagadás (T1499)
- **ID:** `T1499.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú végpont szolgáltatásmegtagadási (DoS) kísérleteket, beleértve a kényszerített
kritikus rendszerfolyamatok leállítása (LSASS, CSRSS, Wininit, SMSS, szolgáltatások)
és az erőforrások kimerülése végtelen hurkok vagy hatalmas memóriafoglalás révén.
A gyanús szülőfolyamatok vonalaira és a nem megbízható végrehajtási útvonalakra összpontosít
miközben szűri a jogszerű rendszerkarbantartási, -javítási és -felügyeleti tevékenységeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## OS önmegsemmisítés-észlelés (T1499.001)
- **ID:** `T1499_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [NTSD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy biztonságú operációs rendszer önmegsemmisítési kísérleteit, beleértve a kényszerített leállítást is
kritikus kernelfolyamatok (csrss.exe, wininit.exe, smss.exe, services.exe)
és rosszindulatú hibakereső visszaélés (ntsd.exe), amelynek célja az azonnali BSOD kiváltása.
Kiterjedt szűrést tartalmaz a megbízható kezeléshez, frissítési műveletekhez és
törvényes adminisztrációs automatizálás.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szolgáltatás kimerülésének észlelése (T1499.002)
- **ID:** `T1499_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges végpont-szolgáltatásmegtagadási (DoS) kísérleteket a célzott szolgáltatáson keresztül
kimerültség.Figyeli a jogosulatlan szervizleállásokat, a tartós konfigurációmódosításokat
(letiltás), valamint a biztonsági és kritikus bináris útvonal-módosítások
infrastrukturális szolgáltatások.Kiszűri a legitim rendszerkezelést, javításokat,
és a hamis pozitív eredmények csökkentésére irányuló tevékenységek ellenőrzése.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## OS önmegsemmisítés-észlelés (T1499.003)
- **ID:** `T1499_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [CDB.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [NTSD.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A kényszerített leállítás figyelésével észleli a célzott operációs rendszer önmegsemmisítési kísérleteit
kritikus Windows kernelfolyamatok (csrss.exe, wininit.exe, smss.exe, services.exe)
és a rendszerhibakeresők (ntsd.exe, cdb.exe) rosszindulatú használata a BSOD kiváltására.
A nagy pontosságú szűrők kizárják a megbízható kezelési, javítási és diagnosztikai folyamatokat
a téves pozitívumok minimalizálása érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Erőforrás-kimerülés észlelése (T1499.004)
- **ID:** `T1499_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Figyeléssel észleli a célzott erőforrás-kimerülési kísérleteket (CPU, RAM vagy IO).
végtelen hurok konstrukciók, hatalmas memóriafoglalások és rekurzív folyamatok
gyanús vagy nem szabványos szülőfolyamat-vonalból származnak.
Kiszűri a legitim automatizálást, a karbantartási szkripteket és a fejlesztői környezeteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Web Shell végrehajtási minták (T1505)
- **ID:** `T1505.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [BASH.EXE](https://lolbas-project.github.io/lolbas/), [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A webszerver figyelésével észleli a webes shell-tevékenység magas megbízhatóságú mutatóit
interaktív héjakat, felderítő segédprogramokat vagy oldalirányú mozgási eszközöket dolgoz fel.
Tartalmazza a szigorú szűrést a legális .NET-fordításokhoz, az IIS adminisztrációjához,
és engedélyezett szerverkarbantartási feladatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## SQL Server Command Shell végrehajtása (T1505.001)
- **ID:** `T1505_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az OS parancsok jogosulatlan végrehajtását a Microsoft SQL Server segítségével
kiterjesztett tárolt eljárások (xp_cmdshell) vagy CLR összeállítások.
A gyanús felderítési parancsokra, a konfigurációs módosításokra és a shell-végrehajtásra összpontosít
miközben szűri a jogos SQL Agent karbantartási és telepítői műveleteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## IIS natív modul-injekció (T1505.002)
- **ID:** `T1505_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NGEN.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Megfigyeléssel észleli a jogosulatlan IIS natív modul regisztrációját vagy befecskendezését
az appcmd.exe használata, az applicationHost.config vagy a web.config közvetlen szerkesztése,
és a DLL betöltése nem szabványos, felhasználó által írható vagy gyanús útvonalakról.
A minimalizálás érdekében a rendellenes parancssori argumentumokra és végrehajtási kontextusokra összpontosít
hamis pozitív eredmények a szabványos IIS vagy Windows szervizfolyamatokból.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Webshell-feltöltés vagy interakcióészlelés (T1505.003)
- **ID:** `T1505_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** A gyanús szkript-feltöltések azonosításával észleli a lehetséges webshell-tevékenységet
az interneten elérhető könyvtárakhoz és az azt követő támadó jellegű interakciókhoz
parancs-végrehajtási stílusparaméterek használatával.A rendellenes útvonalakra összpontosít, a HTTP-re
metódusokat, lekérdezési paramétereket és felhasználói ügynököket, miközben minimalizálja a hamis pozitívumot
törvényes CMS- vagy API-funkciókból.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Alaplapi rendszerindítási kép és SPI Flash-szabotázs (T1505.004)
- **ID:** `T1505_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Felügyelet segítségével észleli az illetéktelen firmware-manipulációt és az SPI-flash manipulációját
alacsony szintű hardver hozzáférési eszközök, gyanús parancssori jelzők és illesztőprogram
nem szabványos folyamatláncokból vagy felhasználói útvonalakból származó regisztrációk.
A rendszerindító képbefecskendezésre, az SPI írási műveletekre és a nem megbízható végrehajtási környezetekre összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Terminal Services DLL-eltérítés észlelése (T1505.005)
- **ID:** `T1505_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Terminal Services (RDP) szolgáltatás DLL-einek jogosulatlan módosítását vagy eltérítését
és szolgáltatók.Figyeli a ServiceDll és a ProviderPath rendszerleíró kulcsokat a manipulációra
megbízhatatlan folyamatok, szokatlan utak vagy gyanús szereplők, kiszűrve a törvényeseket
rendszer bináris fájljai és szolgáltatási műveletei a téves pozitívumok minimalizálása érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szoftverfelderítés-észlelés (T1518)
- **ID:** `T1518.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a célzott szoftverfelderítést, hangsúlyt fektetve a biztonsági termékek felsorolására.
Integritási szintű kapuzást, szülő-folyamat korrelációt, kimenet átirányítást és
kulcsszó alapú szűrés a törvényes rendszerleltárból származó téves pozitívumok minimalizálása érdekében
eszközök vagy adminisztrációs szkriptek.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Biztonsági szoftverfelderítés észlelése (T1518.001)
- **ID:** `T1518_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a biztonsági termékek, például AV, EDR, HIPS és sandbox környezetek célzott felfedezését.
A kulcsszó-specifikus felsorolásra, a gyanús parancssori használatra összpontosít (findstr, grep, Get-Process/Service),
és rendellenes szülőfolyamatok (irodai alkalmazások, webszerverek, nem emelt héjak).
Érzékeli a virtuális gépek ujjlenyomatának kísérleteit is.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-grade jogosulatlan tárolókép-végrehajtás (Implant Container Image)
- **ID:** `T1525.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a nem jóváhagyott nyilvántartásokból származó és a CI/CD-n vagy a rendszernévtereken kívül végrehajtott tárolóképek végrehajtását, jelezve a beültetett tárolóképek esetleges felhasználását a fennmaradás vagy a kezdeti hozzáférés érdekében.

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
- **Leírás:** Érzékeli a szisztematikus felhőszolgáltatás felsorolását, amelyek a Lambdát, a titkokat, a KeyVaultot,
Webalkalmazások és konténerszolgáltatások.A rendellenes végrehajtási környezetekre összpontosít, mint pl
interaktív parancsértelmezők nem fejlesztői gazdagépeken és automatizált kimeneti átirányítási minták
betakarítás vagy kiszűrés.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Alkalmazási token és munkamenet-eltérítés észlelése (T1528)
- **ID:** `T1528.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az alkalmazás-hozzáférési tokenek és a böngésző munkamenet-cookie-inak jogosulatlan kimásolását.
Figyeli a gyanús hozzáférést a felhőalapú CLI hitelesítő adatokhoz (Azure, AWS, GCP) és a böngésző hitelesítő adataihoz
tárolók, amelyek nem megbízható folyamatokból vagy nem szabványos szülőfolyamat-vonalakból származnak.
A megjelölések megkísérlik másolni, kinyerni vagy kiszűrni az érzékeny tokenadatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Jogosulatlan rendszerleállítás/újraindítás észlelése (T1529)
- **ID:** `T1529.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan vagy gyanús rendszerleállítási vagy újraindítási parancsokat.
Figyeli a nem megbízható folyamatvonalakból származó kényszerleállásokat vagy újraindításokat
(böngészők, Office-alkalmazások, szkriptek, ideiglenes mappák) és szűri a legitim rendszert
automatizálási, adminisztrációs vagy állapotfelmérési feladatok.

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
- **Leírás:** Érzékeli a felhőalapú tárolási szolgáltatóktól (AWS, Azure, GCP) származó jogosulatlan adatok kiszűrését
a gyanús CLI-argumentumok figyelésével, beépített hitelesítő adatok beszúrásával, rekurzív másolással
parancsok és rendellenes folyamatsorok, amelyek nem rendszergazdai vagy felhasználói kontextusból származnak.
Lefedi az aws, az, a gsutil, a rclone, az mc és más felhőalapú CLI eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Fiókhozzáférés eltávolításának észlelése (T1531)
- **ID:** `T1531.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan fiókeltávolítási vagy kizárási kísérleteket.Tömegesen figyel
törlések, adminisztratív fiókok célzása és romboló fiók
nem szabványos folyamatokból származó műveletek, például Office-alkalmazások, webszerverek,
vagy forgatókönyveket.Úgy tervezték, hogy csökkentse a hamis pozitív eredményeket a T1531 technikák észlelése közben.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Belső adathalászat-észlelés (T1534)
- **ID:** `T1534.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Az anomáliák figyelésével észleli a fejlett belső adathalász kísérleteket
programozott hozzáférés az Outlook MAPI felületéhez, gyanús gyermekfolyamatok,
veszélyes parancssori jelzők és abnormális fájlmellékletek.
A PowerShellre, a cmd-re, a parancsfájl-motorokra és a nem böngésző szülő anomáliáira összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nem használt szolgáltatás-manipuláció észlelése (T1535)
- **ID:** `T1535.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Windows szolgáltatás ImagePath értékeinek nem megbízható helyekre történő módosításait
vagy binárisok.Figyeli a rendszerleíró adatbázis változásait a szolgáltatásokban, és kiszűri a törvényeseket
Operációs rendszer szervizelése, svchost és általános, harmadik féltől származó frissítők a nagy pontosságú riasztások biztosítása érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Felhőbeli fiókok kiszűrésének észlelése (T1537)
- **ID:** `T1537.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A natív CLI-eszközökön keresztül észleli a felhőalapú fiókok esetleges kiszűrését.Monitorok
fiókok közötti szinkronizálás, kézi hitelesítő adatok beadása és átvitel
nem adminisztratív vagy gyanús folyamatvonalból indult.Borítók
AWS, Azure, GCP és Snowball környezetek.

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
- **Leírás:** Érzékeli a rendellenes felhőalapú irányítópult-hozzáférést és az egyesített bejelentkezési token generálását.
A gyanús CLI-parancsokra és a böngészőindításokra összpontosít, amelyek megkerülik az MFA-t vagy
nem interaktív héjakból származnak.Az AWS, Azure, GCP, Okta és
más SaaS-portálok.Érzékeli a lehetséges felderítést vagy oldalirányú mozgást
tevékenység felhőkörnyezetben.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Webböngésző munkamenet-cookie-k és hitelesítő adatok lopásának észlelése (T1539)
- **ID:** `T1539.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú böngésző munkamenet-cookie-kat és a hitelesítő adatok ellopását.
Azonosítja a Chromium és Firefox cookie-adatbázisokhoz hozzáférő nem böngésző folyamatokat,
titkosítási kulcsfájlok (Helyi állapot), vagy bejelentkezési adatbázisok.
A LOLBin-ekre, a szkriptmotorokra, a DPAPI-visszaélésekre és a staging/exfiltration viselkedésre összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## OS előtti rendszerindítási manipuláció (T1542)
- **ID:** `T1542.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a firmware vagy a rendszerbetöltő illetéktelen módosításait.Monitorok a
EFI partíció rögzítése, illetéktelen firmware flash eszköz használata és
Nem szabványos folyamatfákból kezdeményezett UEFI-változómanipuláció.
Kiszűri a megbízható szállítók frissítési segédprogramjait, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## ROM készlet és UEFI firmware manipuláció (T1542.001)
- **ID:** `T1542_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan firmware-manipulációt a magas kockázatú illesztőprogramok figyelésével
gyanústól kezdeményezett regisztrációk és firmware-frissítési segédprogramok
folyamatfák, kifejezetten a BYOVD és az SPI flash hozzáférést célozva.
Kiszűri a megbízható szállítók frissítő segédprogramjait, hogy minimalizálja a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Komponens firmware-szabotázs (T1542.002)
- **ID:** `T1542_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a perifériás firmware (NIC, SSD, GPU) jogosulatlan módosítását
a nem megbízható folyamatból indított önálló villogó eszközök figyelése
láncok vagy nem szabványos fájlhelyek.Kiszűri a megbízható kezelést
eszközök a hamis pozitív eredmények csökkentésére.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Bootkit Persistence & EFI manipuláció (T1542.003)
- **ID:** `T1542_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan rendszerbetöltő módosításokat a BCD integritás megkerülésének figyelésével,
kézi EFI-partíció csatlakoztatása és gyanús rendszerindítási útvonal-átirányítás.
Kiszűri a jogos operációs rendszer javításokat és a BitLocker műveleteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Alaplapi rendszerindítási kép és SPI Flash-szabotázs (T1542.004)
- **ID:** `T1542_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Az alacsony szintű hardver-hozzáférés figyelésével észleli a jogosulatlan firmware-manipulációt
nem szabványos folyamatláncokból kezdeményezett eszközök és illesztőprogram-regisztrációk.
Szűrés közben az SPI flash írásra és a képinjektálási kísérletekre összpontosít
megbízható menedzsment eszközök.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## DHCP/PXE rendszerindítási eltérítés (T1542.005)
- **ID:** `T1542_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a 66-os (Boot Server) és a 67-es (Bootfile Name) DHCP-opciók jogosulatlan módosítását,
amelyet a támadók a hálózati rendszerindítási kérelmek rosszindulatú TFTP-kiszolgálóra való átirányítására használnak.
Szűri a megbízható rendszerszolgáltatásokat a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nem adminisztrátor felhasználó, aki több érzékeny Windows-szolgáltatást próbál leállítani vagy módosítani
- **ID:** `T1543.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Gyanús viselkedést észlel, amikor egy nem adminisztratív felhasználó rövid időn belül megpróbál több érzékeny Windows-szolgáltatást leállítani vagy módosítani.Ezt a viselkedést általában a védekezés kijátszásával vagy a kitartásra való felkészülési tevékenységgel társítják.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro macOS Launch Agent Persistence Detection (T1543.001)
- **ID:** `T1543_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** A gyanús folyamatvonalak figyelésével észleli az indítási ügynökök jogosulatlan létrehozását
és az aláíratlan vagy parancsfájl-alapú végrehajtási célok azonosítása a .plist-en belül.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Systemd Service Persistence (T1543.002)
- **ID:** `T1543_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** Felügyelet segítségével észleli a rendszeregységek jogosulatlan létrehozását vagy módosítását
gyanús folyamatvonalak és szokatlan végrehajtható útvonalak a szolgáltatásfájlban.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro jogosulatlan Windows-szolgáltatás telepítése (T1543.003)
- **ID:** `T1543_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A 7045-ös eseményazonosító és a folyamatlétrehozás figyelésével észleli a jogosulatlan Windows-szolgáltatás létrehozását.
A gyanús bináris útvonalakra, a shell által létrehozott szolgáltatásokra és a nem szabványos szolgáltatás végrehajtható fájljaira összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro jogosulatlan macOS Launch Daemon (T1543.004)
- **ID:** `T1543_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)
- **Leírás:** A fájlesemények figyelésével észleli a System Launch Daemonok jogosulatlan létrehozását
valamint az írási folyamat és a cél bináris aláírás integritásának ellenőrzése.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro WMI-esemény-előfizetés tartóssága (T1546.003)
- **ID:** `T1546.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan WMI-esemény-előfizetéseket azáltal, hogy a fogyasztói típusokat korrelálja
gyanús parancssori minták és a megbízható rendszerkezelők kizárása.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro fájltársítás eltérítése (T1546.001)
- **ID:** `T1546_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Figyeléssel észleli a rendszerleíró adatbázis fájltársításainak jogosulatlan módosításait
gyanús szereplői folyamatok és nem szabványos végrehajtható útvonalak a 'shell\open\command'-ban.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro képernyővédő tartós észlelés (T1546.002)
- **ID:** `T1546_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONTROL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a jogosulatlan képernyővédő-eltérítést azáltal, hogy figyeli, hogy a rendszerleíró adatbázis az „SCRNSAVE.EXE” fájlba ír.
Kiszűri a csoportházirend-objektum által vezérelt változtatásokat, és érvényesíti a bináris kiterjesztéseket és a megbízható elérési utakat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## WMI-esemény-előfizetés állandósága WMIC-en vagy PowerShell-en keresztül (High Fidelity)
- **ID:** `T1546_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [WMIC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a perzisztencia érdekében használt állandó WMI-esemény-előfizetések létrehozását.A szabály az EventFilter, CommandLineEventConsumer és FilterToConsumerBinding támadókra jellemző kombinációira összpontosít, amelyeket WMIC vagy PowerShell segítségével hoztak létre a root\subscription névtérben, az ismert vállalati megfigyelő ügynökök kizárásával.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro AppCert DLL Perzisztencia Detection (T1546.004)
- **ID:** `T1546_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [REGEDIT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A Session Manager figyelésével észleli az AppCert DLL-ek jogosulatlan regisztrációját
Rendszerleíró kulcs.Kiszűri a megbízható rendszertelepítőket, és nem szabványosságot igényel
útvonalakat vagy gyanús folyamatvonalakat indítani.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Shell Trap Perzisztencia-észlelés (T1546.005)
- **ID:** `T1546_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a jogosulatlan shell trap fennmaradását a shell profilfájlokba történő írások figyelésével
amelyek „trap” parancsokat tartalmaznak gyanús hálózati hasznos adatokkal vagy végrehajtási mintákkal kombinálva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Mach-O LC_LOAD_DYLIB befecskendezés (T1546.006)
- **ID:** `T1546_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a Mach-O binárisok jogosulatlan módosítását rosszindulatú dylibek beszúrása érdekében.
Azokra a nem fejlesztői eszközökre összpontosít, amelyek módosítják az alkalmazás bináris fájljait és ellenőrzik a
gyanús dylib keresési útvonalak vagy aláíratlan könyvtárbetöltések.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Netsh Helper DLL-perzisztencia (T1546.007)
- **ID:** `T1546_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan Netsh Helper DLL regisztrációt a Registry írásainak figyelésével
és parancssori argumentumokat.Kiszűri az ismert jó telepítőket és az aláírt Microsoft bináris fájlokat.

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
- **Leírás:** A Windows Error Reporting (WER) SilentProcessExit segítségével észleli a jogosulatlan fennmaradást.
A folyamat során végrehajtott „MonitorProcess” parancsok regisztrálására összpontosít
összeomlik vagy kilép, kivéve az ismert hibakereső környezeteket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro AppInit_DLLs Perzisztencia-észlelés (T1546.009)
- **ID:** `T1546_009.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Az AppInit_DLL-eken keresztül észleli a jogosulatlan fennmaradást a beállításjegyzék írásainak figyelésével
az „AppInit_DLLs” és „LoadAppInit_DLLs” értékekhez.
Kiszűri az aláírt Microsoft bináris fájlokat és a megbízható rendszertelepítőket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro AppCert DLL Perzisztencia-észlelés (T1546.010)
- **ID:** `T1546_010.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [REGEDIT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A Session Manager figyelésével észleli az AppCert DLL-ek jogosulatlan regisztrációját
Rendszerleíró kulcs.Kiszűri a megbízható rendszertelepítőket, és nem szabványosságot igényel
útvonalakat vagy gyanús folyamatvonalakat indítani.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Application Shimming Perzisztencia Detection (T1546.011)
- **ID:** `T1546_011.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Az sdbinst.exe figyelésével észleli a Shim adatbázis jogosulatlan telepítését
végrehajtás gyanús forrásútvonalakkal és közvetlen Registry írással az InstalledSDB-re.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro IFEO hibakereső eltérítés-észlelés (T1546.012)
- **ID:** `T1546_012.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [ATBROKER.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan hibakereső befecskendezést az Image File Execution Options (IFEO) segítségével.
Kiszűri a legitim fejlesztői eszközöket, és a magas kockázatú rendszerbinárisokra összpontosít
és kisegítő lehetőségek (Sticky Keys, Utility Manager).

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
- **Leírás:** Érzékeli a PowerShell-profilok jogosulatlan automatizált módosítását.
Kiszűri a jogszerű kézi szerkesztést a szövegszerkesztőkön keresztül, és arra összpontosít
programozott befecskendezés shellekből vagy nem szabványos szülőfolyamatokból.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro WMI-esemény-előfizetés tartóssága (T1546.014)
- **ID:** `T1546_014.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan WMI-esemény-előfizetéseket a létrehozásának figyelésével
EventFilters és Command/Script Consumers.Kiszűri az ismert adminisztratív elemeket
eszközöket, és a nem szabványos parancsfájl-végrehajtásra összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús COM-eltérítés a felhasználói szintű tartósság érdekében (high Fidelity)
- **ID:** `T1546_015.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A CLSID InprocServer32 és LocalServer32 bejegyzéseinek nem szabványos végrehajtási útvonalakra mutató beállításjegyzék-módosításainak figyelésével észleli a gyanús COM-eltérítési kísérleteket, amelyeket a felhasználói szintű fennmaradás érdekében használnak.A szabály a HKCU-módosításokra összpontosít, amelyeket parancsfájlokkal vagy LOLBin-végrehajtással kombinálnak, hogy csökkentsék a hamis pozitív eredményeket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro MSI telepítő egyéni műveletek tartóssága (T1546.016)
- **ID:** `T1546_016.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nem szabványos fájlból származó, az msiexec.exe által létrehozott gyanús gyermekfolyamatokat
könyvtárakat.Ez a rosszindulatú MSI egyéni műveleteket célozza meg, amelyeket a fennmaradás vagy a jogosultságok kiterjesztésére használnak.

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
## Gyanús beállításjegyzék-futtatási kulcsmódosítás a felhasználói állandóság érdekében (high Fidelity)
- **ID:** `T1547_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús beállításjegyzék-módosításokat, amelyeket a Windows Run és RunOnce kulcsokon keresztül a felhasználói szintű fennmaradás biztosítására használnak.A szabály a nem szabványos végrehajtható helyekre összpontosít parancsfájl-motorokkal kombinálva, hogy csökkentse a jogszerű szoftvertelepítésekből származó hamis pozitív eredményeket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity LSA hitelesítési csomag tartóssága
- **ID:** `T1547_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan hitelesítési csomagok hozzáadását az LSA rendszerleíró kulcshoz.
A támadók ezt használják a RENDSZER szintű kitartáshoz és a hitelesítő adatok begyűjtéséhez.
Ez a szabály szűri a szabványos Windows-csomagokat és figyeli a System32-n kívüli DLL-eket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú időszolgáltató tartóssága (T1547.003)
- **ID:** `T1547_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli egy új Windows Time Provider regisztrációját.
A támadók ezt a RENDSZER-szintű fennmaradás érdekében használják fel egy rosszindulatú DLL betöltésével az svchost.exe fájlba.
Ez a szabály szűri a szabványos Windows DLL-eket, és a nem System32 útvonalakat célozza meg.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Winlogon Helper DLL-perzisztencia (T1547.004)
- **ID:** `T1547_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Winlogon segédkulcsok (Userinit, Shell) jogosulatlan módosításait.
Több végrehajtható fájl „hozzáfűzésére” vagy nem szabványos rendszerútvonalak használatára összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity SSP DLL-perzisztencia (T1547.005)
- **ID:** `T1547_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan DLL-ek hozzáadását az LSA Security Packages rendszerleíró kulcshoz.
A támadók ezt kitartásra és egyértelmű szöveges hitelesítő adatok ellopására használják.
Szűri a szabványos Windows SSP-ket és figyelmezteti a nem felügyelt módosításokat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity kernel-illesztőprogram regisztráció (T1547.006)
- **ID:** `T1547_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli egy új kernel-módú illesztőprogram-szolgáltatás regisztrációját.
A támadók ezt használják a rootkit szintű kitartásra és a biztonsági eszközök letiltására.
Az illesztőprogramok nem szabványos útvonalakon történő megjelölésére és a gyanús kézi szolgáltatás létrehozására optimalizálva.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity böngésző munkamenet-perzisztencia (T1547.007)
- **ID:** `T1547_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a böngésző munkameneteinek vagy preferenciáinak fájljainak nem böngésző folyamatok általi jogosulatlan módosítását.
A támadók ezt arra használják, hogy a böngészőket indításkor rosszindulatú URL-ek megnyitására kényszerítsék a fennmaradás érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity LSASS illesztőprogram/csomag tartósság (T1547.008)
- **ID:** `T1547_008.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az új LSA-bővítmények, értesítési csomagok vagy illesztőprogramok regisztrációját.
A támadók ezt arra használják, hogy rosszindulatú kódot töltsenek be az lsass.exe folyamatba
kitartás és valós idejű hitelesítő adatok begyűjtése.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú parancsikon módosítás észlelése
- **ID:** `T1547_009.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az LNK-fájlok gyanús folyamatok általi létrehozását vagy módosítását (PowerShell, CMD stb.)
az indítási mappákban vagy a tálca elérési útjain.Ez egy általános technika a kitartásra.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity AppCert DLL-perzisztencia (T1547.010)
- **ID:** `T1547_010.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az AppCert DLL-ek jogosulatlan regisztrációját.Ezek a DLL-ek betöltődnek
minden folyamat, amely a CreateProcess-t hívja, így ez egy erőteljes perzisztencia és befecskendezési vektor.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity alkalmazás Shimming Perzisztencia (T1547.011)
- **ID:** `T1547_011.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli egy új Shim adatbázis (.sdb) telepítését az sdbinst.exe használatával.
A támadók alátéteket használnak a DLL-ek beszúrására, a biztonsági ellenőrzések megkerülésére vagy a kitartás fenntartására.
Ez a szabály kiszűri a legális telepítőket, és megjelöli a gyanús szülő-gyermek kapcsolatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity COM-eltérítés tartóssága (T1547.012)
- **ID:** `T1547_012.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús helyekre mutató COM-objektumkezelők létrehozását a HKCU-ban.
Az InprocServer32 és LocalServer32 kulcsokra összpontosít, amelyek az eltérítés elsődleges célpontjai.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity E-mail Client Helper Perzisztencia (T1547.013)
- **ID:** `T1547_013.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan e-mail kliens segítők vagy COM-bővítmények regisztrációját.
A felhasználók által írható útvonalakon regisztrált DLL-ekre és a gyanús beállításjegyzék-írókra összpontosít.

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
- **Leírás:** Érzékeli az Active Setup 'StubPath' rendszerleíró kulcsainak nem rendszerfolyamatok általi létrehozását vagy módosítását.
A támadók ezt a perzisztencia eléréséhez használják, amely felhasználónként egyszer fut be bejelentkezéskor.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity COM-eltérítés tartósság (T1547.015)
- **ID:** `T1547_015.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli olyan COM objektumkezelők létrehozását a HKCU-ban, amelyek gyanús,
a felhasználó által írható helyek.A támadók eltérítik a CLSID-eket a lopakodó kitartás elérése érdekében
törvényes rendszerfolyamatokon belül, mint például az explorer.exe.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Jogosultság kiterjesztése rendszerleíró adatbázis eltérítésével (T1548)
- **ID:** `T1548.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [COMPUTERDEFAULTS.EXE](https://lolbas-project.github.io/lolbas/), [EVENTVWR.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az UAC megkerülési és jogosultság-kiterjesztési kísérleteket a jogosulatlanok figyelésével
A rendszerleíró adatbázis módosításai a shell open parancsokhoz.Kiszűri a megbízható telepítőket
és a rendszer által kezdeményezett változtatások a hamis pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Setuid/Setgid bitmanipuláció (T1548.001)
- **ID:** `T1548_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** A chmod/chown végrehajtás figyelésével észleli a jogosulatlan SUID/SGID bit-eszkalációt
a világra írható könyvtárakban, a gyanús shell-eredetű akciókban és a felderítésben
mintákat a find használatával, miközben kizárja a megbízható csomagkezelőket és automatizálási eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## UAC bypass a Fodhelper Registry Hijack segítségével (High Fidelity)
- **ID:** `T1548_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az UAC megkerülési kísérleteit a fodhelper.exe fájllal való visszaélésre, figyelve az ms-settings protokoll rendszerleíró adatbázis-eltérítését és gyanús gyermekfolyamat-végrehajtást.Ez a szabály a felhasználói kontextus automatikus emelésére összpontosít, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Sudoer-manipuláció és szudóval való visszaélés (T1548.003)
- **ID:** `T1548_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Észleli a jogosulatlan sudoers fájlmódosításokat és a sudo gyorsítótárazási visszaéléseket.
A NOPASSWD kiegészítésekre, a timestamp_timeout manipulációra és a
veszélyes környezeti változó injekciók, mint például az LD_PRELOAD.Kizár
megbízható automatizálási eszközök.

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
- **Leírás:** Az Osascript végrehajtásának figyelésével észleli a jogosulatlan AppleScript-emelési kísérleteket
"rendszergazdai jogosultságokkal" olyan nem megbízható szülői folyamatoktól, mint a böngészők, irodai programcsomagok,
együttműködési alkalmazások vagy ideiglenes címtárak, a megbízható rendszerfelügyeleti eszközök kizárása mellett.

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
- **Leírás:** Érzékeli az XDG asztali bejegyzések vagy parancsikonok jogosulatlan módosításait, amelyek megpróbálják
a SUID binárisok végrehajtásához vagy a pkexec kihasználásához a jogosultságok kiterjesztéséhez.
A felhasználók által írható könyvtárakban a nem megbízható folyamatok által végzett módosításokra összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Alternatív hitelesítési anyag (T1550)
- **ID:** `T1550.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Azonosítással észleli az ellopott hash-ek vagy jegyek oldalirányú mozgáshoz való használatát
NTLM/Kerberos protokoll anomáliák, beleértve az RC4 titkosítás visszaminősítését és
korlátozott rendszergazdai bejelentkezési típusok, ugyanakkor kizárják a legitim rendszerfelügyeleti eszközöket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Alkalmazás-hozzáférési token visszaélés (T1550.001)
- **ID:** `T1550_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A jogosulatlanok figyelésével észleli az alkalmazás-hozzáférési tokenek ellopását vagy azokkal való visszaélést
hozzáférés az IdentityCRL és TokenBroker üzletekhez, valamint a hordozó tokenek használata
parancssori segédprogramokban, kivéve a legitim Azure CLI-t és a böngészőfolyamatokat.

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
- **Leírás:** Felismeri a Pass-the-Hash (PtH) támadásokat a rendellenes NTLM loopback hitelesítés azonosításával,
korlátozott rendszergazdai bejelentkezés (LogonType 9 a seclogo-n keresztül) és a hitelesítő adatok beszúróeszköz-tevékenysége,
miközben kizárja a legitim szolgáltatás- és gépfiókokat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Pass-the-Ticket Detection (T1550.003)
- **ID:** `T1550_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a Pass-the-Ticket (PtH) támadásokat a Kerberos titkosítási leminősítések (RC4) azonosításával,
a Rubeus/Mimikatzra jellemző rendhagyó jegyzászlók és az illetéktelen jegybeadás
az LSA folyamatmemóriába.

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
- **Leírás:** A nem böngésző folyamatok figyelésével észleli a webes munkamenetek ellopására irányuló jogosulatlan kísérleteket
a titkosított AES-kulcs (Helyi állapot) és a böngésző cookie-adatbázisainak elérése.
Nem tartalmazza a legális böngészőfrissítési, segédprogram- és szinkronizálási folyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nem biztonságos hitelesítő adatok felfedezése (T1552)
- **ID:** `T1552.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a hitelesítő adatok célzott felderítését fájlok, rendszerleíró adatbázis,
és héjtörténet.Összefügg a keresési eszközökkel (findstr, grep, PowerShell)
magas kockázatú fájltípusokkal, érzékeny kulcsszavakkal és gyanús végrehajtással
kontextusokban, hogy minimalizálja a hamis pozitívumot, miközben azonosítja a hitelesítő adatok begyűjtését.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hitelesítő adatok a Files Discoveryben (T1552.001)
- **ID:** `T1552_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fájlokban tárolt hitelesítő adatok jogosulatlan, rekurzív felfedezését
és konfigurációs szkriptek (AWS, Git, SSH kulcsok, jelszó/konfig fájlok).
A keresőeszközöket érzékeny fájlkiterjesztésekkel, kiszűrési mintákkal,
és gyanús szülői folyamatok a hamis pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hitelesítési adatok a rendszerleíró adatbázisban (T1552.002)
- **ID:** `T1552_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a tárolt hitelesítő adatok jogosulatlan felfedezését vagy kimásolását
Windows Registry (PuTTY, WinSCP, RDP, LSA titkok, SAM, VPN kliensek).
Összekapcsolja a rendszerleíró adatbázis felsorolását vagy exportálását a gyanús parancsokkal
szülőfolyamatok, rekurzív keresési minták és nem rendszer felhasználói környezet
a hamis pozitívumok csökkentésére.

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
- **Leírás:** Érzékeli a héjtörténeti fájlok jogosulatlan felfedezését vagy kibontását
(bash, zsh, ConsoleHost, adatbázis-héjak, Python REPL).
A kiszűrési parancsokra, az előzményfájlokat elérő nem shell folyamatokra összpontosít,
homályos PowerShell-használat, valamint távoli vagy webszerver-kontextusok.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Privát kulcs felfedezése (T1552.004)
- **ID:** `T1552_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [SSH.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a privát kriptográfia célzott felderítési vagy gyűjtési kísérleteit
kulcsok (SSH, PGP, TLS tanúsítványok).A rekurzív fájlok felsorolására összpontosít,
privát kulcs fejléc keresések, érzékeny címtár bejárás, kódolás ill
export viselkedés és gyanús végrehajtási környezet.

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
- **Leírás:** Érzékeli a felhőalapú hitelesítő adatok jogosulatlan felfedezését vagy kimásolását
(AWS, Azure, GCP, Docker) a helyi konfigurációs fájlokból.-ra összpontosít
gyanús hozzáférési minták, kódolás, átirányítás, távoli végrehajtás
kontextus és abnormális folyamatvonal, miközben csökkenti a hamis pozitívumot
jogos CLI tevékenységből.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hitelesítő adatok a Files Discoveryben (T1552.006)
- **ID:** `T1552_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a tárolt hitelesítő adatok jogosulatlan kézi vagy parancsfájl-felderítését
konfigurációs vagy házirend-fájlokban, beleértve a csoportházirend-beállításokat (GPP),
felügyelet nélküli telepítőfájlok, web.config és egyéb egyszerű szöveges vagy gyengén
védett hitelesítő műtermékek.A karakterlánc-keresési tevékenységre összpontosít,
érzékeny fájlcélzás és távoli végrehajtási kontextus, ugyanakkor kizárás
törvényes rendszerfeldolgozás.

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
- **Leírás:** Érzékeli az érzékeny hitelesítő adatok célzott felfedezését a tárolókban,
beleértve a Kubernetes szolgáltatásfiók-tokeneket, a csatolt titkokat, a felhőt
szolgáltatói kulcsok és környezeti változók.Az interaktívra összpontosít
shell-végrehajtás, parancsláncolás és abnormális folyamatsor
miközben szűri a legitim belépési pontot és figyeli a tevékenységet.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## GPP jelszó felderítés (T1552.008)
- **ID:** `T1552_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a titkosított csoportházirend-beállítások (GPP) célzott felfedezését
jelszavak (cpassword) a SYSVOL megosztásokon belül.A parancssorra összpontosít
karakterlánc-keresések, PowerShell-felsorolás, távoli végrehajtási környezet,
és abnormális felhasználói tevékenység a hamis pozitív visszaszorítása érdekében a jogostól
Csoportházirend feldolgozás.

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
- **Leírás:** Érzékeli a Windows megbízhatósági vezérlőinek felforgatására tett kísérleteket, beleértve a kényszerített
gyökértanúsítvány telepítése és Mark-of-the-Web (MotW) / Biztonság
Zóna manipuláció.A gyanús végrehajtási kontextusra összpontosít, nem szabványos
forrásútvonalak és a rendellenes szülő-gyermek kapcsolatok csökkentése érdekében
vállalati telepítési téves pozitív eredmények.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## macOS Gatekeeper és Quarantine Bypass (T1553.001)
- **ID:** `T1553_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a Gatekeeper globális vagy programozott letiltására irányuló kísérleteket
távolítsa el a com.apple.quarantine attribútumot a fájlokból.-ra összpontosít
nem interaktív végrehajtás, gyanús fájlhelyek és rendellenes
a szülő-gyermek kapcsolatok a fejlesztői és adminisztratív csökkentése érdekében
hamis pozitívumok.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## SIP-eltérítés és bizalomfelforgatás (T1553.002)
- **ID:** `T1553_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a tárgyi interfész csomagok (SIP) gyanús módosítását,
Trust Providers vagy WinVerifyTrust-hoz kapcsolódó beállításkulcsok.-ra összpontosít
DLL átirányítás a felhasználó által írható útvonalakra, rendellenes végrehajtási környezet,
és a bizalommal általában összefüggő magas kockázatú szülői folyamatok
felforgató és aláírás-érvényesítési bypass technikák.

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
- **Leírás:** Érzékeli a katalógusfájlok gyanús manipulációját vagy jogosulatlan hozzáadását
a Windows Code Integrity Catalog Database adatbázisba (CatRoot / CatRoot2).
A nagy kockázatú eszközökre, a rendellenes szülő-gyerek kapcsolatokra összpontosít,
a nem szabványos forrásútvonalak és a ritka felhasználói kontextusok csökkentése
vállalati telepítési téves pozitív eredmények.

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
- **Leírás:** Érzékeli a gyökértanúsítvány magas kockázatú programozott telepítését
a Windows Trusted Root vagy AuthRoot áruházaiban.A gyanúsra összpontosít
parancssori jelzők, nem szabványos tanúsítványfájlok helyei és
nem mindennapi szülő-gyerek folyamat kapcsolatokat jelentősen csökkenteni
vállalati telepítési téves pozitív eredmények.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Mark-of-the-Web (MotW) bypass & Zone Subversion Detection (T1553.005)
- **ID:** `T1553_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Mark of the Web (MotW) programozott eltávolítását vagy hamisítását az alternatív adatfolyam (Zone.Identifier) ​​manipulációja vagy a rendszerleíró adatbázis alapú biztonsági zóna leminősítése révén.A nem interaktív szkript-végrehajtásra és a gyanús zónakonfiguráció-módosításokra összpontosít, miközben szűri a jogszerű telepítőket és a böngészőtevékenységet.

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
- **Leírás:** Érzékeli a Windows Code Integrity and Driver Signature Enforcement (DSE) felforgatására irányuló kísérleteket BCDEDIT jelzők vagy beállításjegyzék-módosítások révén, amelyek lehetővé teszik az aláíratlan kernel-illesztőprogramok betöltését, miközben szűri a jogos operációs rendszer-karbantartási, telepítői és megbízható rendszerfolyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Client Bináris Integritás Kompromisszum (T1554)
- **ID:** `T1554.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a megbízható ügyfél bináris fájljainak jogosulatlan folyamatok általi módosítását vagy cseréjét.
Azokra az esetekre összpontosít, amikor az írási folyamat LOLBin, vagy a fájl nem rendelkezik érvényes szállítói aláírással.

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
## Windows Vault hitelesítő adatok legyűjtésének észlelése (T1555.001)
- **ID:** `T1555_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Windows Vault hitelesítő adatok esetleges jogosulatlan kimásolását a vaultcmd.exe használatának, az API-karakterláncoknak és a nem megbízható kontextusokból származó gyanús parancssori adatok átirányításának figyelésével, miközben kiszűri a legitim böngészőket és rendszerfolyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Biztonságos memóriakiürítés észlelése (T1555.002)
- **ID:** `T1555_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a jogosulatlan kísérleteket a „securityd” folyamathoz vagy a kulcslánc-adatbázishoz való hozzáférésre vagy a memória törlésére a macOS rendszeren.Figyeli a gyanús hibakereső és memóriaeszközök használatát, miközben szűri az Apple által aláírt diagnosztikai segédprogramokat és Xcode fejlesztőeszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Böngésző hitelesítő adatok begyűjtésének észlelése (T1555.003)
- **ID:** `T1555_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A „Bejelentkezési adatok”, „Cookie-k”, „Webadatok”, „key4.db” vagy „logins.json” fájlokat célzó gyanús parancssori fájlműveletek figyelésével észleli a böngésző hitelesítőadatbázisainak (Chrome, Edge, Firefox, Brave) esetleges jogosulatlan hozzáférését és kiszűrését.Szűri a legitim böngészőfolyamatokat és a biztonsági mentési/szinkronizálási eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Windows Credential Manager begyűjtési észlelés (T1555.004)
- **ID:** `T1555_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CMDKEY.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges jogosulatlan hitelesítő adatok begyűjtését a Windows Credential Manager (cmdkey.exe) segítségével a gyanús parancssori használat, az átirányítás, a nem megbízható szülőfolyamatok és a nem interaktív végrehajtási környezetek figyelésével.Szűri a jogos IT-felügyeleti szkripteket és a felhasználói tevékenységeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Jelszókezelő kivonatészlelés (T1555.005)
- **ID:** `T1555_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jelszókezelő adatbázisok (pl. KeePass, 1Password, Bitwarden) lehetséges jogosulatlan hozzáférését vagy kiszűrését azáltal, hogy figyeli a vault fájlokat (.kdbx, .opvault, .agilekeychain, key3.db, key4.db folyamatokat) és nem végrehajtott kontextusokat célzó gyanús fájlműveleteket.

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
- **Leírás:** Érzékeli a felhőszolgáltató hitelesítő adatainak (AWS, Azure, GCP, Docker) jogosulatlan elérését vagy kiszűrését a gyanús parancssori tevékenységek és az érzékeny konfigurációs útvonalakat elérő eszközök figyelésével.Szűri a hivatalos felhőalapú CLI-binárisokat és az ismert DevOps-ügynököket, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-Grade hitelesítési folyamat eltérítése gyanús DLL-regisztráción keresztül
- **ID:** `T1556.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Windows hitelesítési folyamat kihasználtsági szintű módosítását, amikor egy nem rendszerfolyamat új hitelesítéssel kapcsolatos DLL-t regisztrál egy felhasználó által írható könyvtárból LSA, SSP vagy Credential Provider nyilvántartási helyekre, ami erősen jelzi a hitelesítő adatok elfogását.

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
- **Leírás:** Érzékeli a kihasználási szintű biztonsági támogatási szolgáltató (SSP) feltörését az LSA Security Packages rendszerleíró adatbázis értékének jogosulatlan módosításának azonosításával, hogy új, nem rendszerszintű DLL-t regisztráljon egy felhasználó által írható könyvtárból egy nem megbízható folyamat vagy fiók által.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-Grade jelszószűrő DLL-eltérítés LSA értesítési csomagokon keresztül
- **ID:** `T1556_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli egy rosszindulatú Jelszószűrő DLL kizsákmányolási szintű telepítését az LSA Notification Packages rendszerleíró adatbázis értékének jogosulatlan módosításának azonosításával, hogy egy új DLL-t adjon hozzá a felhasználó által írható könyvtárban egy nem megbízható folyamat vagy fiók által.Ez a viselkedés erősen jelzi a hitelesítő adatok elfogását a tartományvezérlőkön.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003)
- **ID:** `T1556_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a PAM konfiguráció vagy a bináris modulok jogosulatlan módosítását
az /etc/pam.d/ és /lib/security/ könyvtárba írt nem csomagkezelői írások azonosításával.
Kifejezetten az automatizált konfigurációs eszközök szűrői a hamis pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro hálózati eszköz hitelesítés eltérítése (T1556.004)
- **ID:** `T1556_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)
- **Leírás:** Érzékeli az AAA (Authentication, Authorization and Accounting) jogosulatlan módosításait
beállításokat vagy helyi felhasználói adatbázisokat a hálózati eszközökön.A kézi bypassokra összpontosít
engedélyezett felügyeleti alhálózatokon kívül hajtják végre.

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
- **Leírás:** Érzékeli a kiemelten privilegizált SID-ek beillesztését a felhasználó sIDHistory attribútumába.
Ez a „Ghost Admin” forgatókönyvet célozza meg, ahol a felhasználó tartományadminisztrátori jogokat szerez
anélkül, hogy tagja lett volna a csoportnak.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Entra ID MFA módszereltérítés (T1556.006)
- **ID:** `T1556_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Korrelációval észleli az Entra ID MFA-módszereinek magas kockázatú módosításait
sikeres metódusmódosítások gyanús belépési pontokkal vagy adminisztrációs anomáliákkal.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hibrid identitás szinkronizálási manipuláció észlelése (T1556.007)
- **ID:** `T1556_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az Entra ID/Azure AD Connect szinkronizálási folyamatok (MITRE ATT&CK T1556.007) lehetséges jogosulatlan manipulációját.Figyeli az MSOL-fiókkal való visszaélést a nem szinkronizáló kiszolgálókról, a jogosulatlan ADSync PowerShell-használatot és a gyanús adatbázis-hozzáférést a hitelesítő adatok vagy jelszavak manipulálása céljából.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózatról felhőre történő hitelesítés-eltérítés észlelése (T1556.008)
- **ID:** `T1556_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy kockázatú módosításokat a vállalati alkalmazásokban, az egyszerű szolgáltatásokban és a feltételes hozzáférési házirendekben az Azure-ban, amelyek hálózat-felhő hitelesítési feltörést jelezhetnek (MITRE ATT&CK T1556.008).Az MFA-megkerülésekre, a hitelesítő adatok jogosulatlan kiegészítésére és a gyanús szolgáltatási elv-módosításokra összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ellenfél észlelése a középsőben (T1557)
- **ID:** `T1557.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges Adversary-in-the-Middle (AiTM) támadásokat (MITRE ATT&CK T1557) az olyan jogosulatlan rendszerkonfiguráció-módosítások figyelésével, mint például az IP-továbbítás engedélyezése és az LLMNR/NetBIOS/ARP mérgező eszközök nem megbízható helyekről történő végrehajtása.Szűri a legitim virtualizációs és VPN-tevékenységet, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## LLMNR/NBT-NS mérgezés és SMB-reléérzékelés (T1557.001)
- **ID:** `T1557_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges LLMNR/NBT-NS mérgezést és az SMB továbbítási tevékenységet (MITRE ATT&CK T1557.001) azáltal, hogy figyeli a jogosulatlan folyamatokat, amelyek megpróbálnak kapcsolódni a hálózati feloldó portokhoz, és ismert támadási eszközöket futtatnak gyanús parancssori argumentumokkal.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rogue ARP-mérgezés / MITM-észlelés (T1557.002)
- **ID:** `T1557_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges ARP-mérgezéseket vagy MITM-kísérleteket (MITRE ATT&CK T1557.002) az IP-továbbítás engedélyezésének és a nem megbízható helyekről végrehajtott gyanús csomagkezelési eszközök figyelésével.Kiszűri a legitim virtualizációs, VPN- és hálózati diagnosztikai tevékenységeket, hogy csökkentse a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rogue DHCP / DHCP hamisítás-észlelés (T1557.003)
- **ID:** `T1557_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a DHCP-hamisításra utaló potenciális csaló DHCP-szervertevékenységet (MITRE ATT&CK T1557.003).A szabály azonosítja azokat a gyanús folyamatokat, amelyek nem szabványos helyekről és nem rendszerfelhasználókról próbálnak elindítani DHCP-vel kapcsolatos szolgáltatásokat átjáró/DNS-manipulációs argumentumokkal.Úgy tervezték, hogy csökkentse a hamis pozitív eredményeket a legitim virtualizáció és a natív DHCP-szolgáltatások szűrésével.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Kerberos támadásészlelés
- **ID:** `T1558.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fejlett Kerberos hitelesítő támadásokat, beleértve a jegyet is
hamisítás, AS-REP pörkölés, Kerberoasting és jegyinjekció.

Jellemzők:
- A titkosítás leépítésének (RC4/0x17) észlelése
- Támadó eszközjelzők (Rubeus, Mimikatz, Impacket, PowerView)
- Jegytípus-specifikus paraméterek (arany, ezüst, AS-REP)
- Szülőfolyamat és ideiglenes végrehajtási környezetkapuzás
- Vállalati FP szűrés (LSASS, SYSTEM, felügyeleti eszközök)

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Aranyjegy-hamisítás és befecskendezés
- **ID:** `T1558_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú Golden Ticket létrehozását és befecskendezési tevékenységét.

A fedezet a következőket tartalmazza:

- KRBTGT hash vagy AES kulcs követelmény
- SID specifikáció
- Pass-the-Ticket (/ptt) vagy kerberos::ptt injekció
- Mimikatz vagy Rubeus Golden Ticket használati minták
- Vállalati FP szűrők (LSASS/rendszer/monitoring)

Az ATT&CK T1558.001-re összpontosítva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ezüst jegyhamisítás és befecskendezés
- **ID:** `T1558_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú ezüst jegy létrehozását és befecskendezési tevékenységét.

A fedezet a következőket tartalmazza:

- Szolgáltatás-specifikus SPN-célzás (cifs, http, mssql, ldap)
- Szolgáltatási fiók hash anyaga (RC4 / AES128 / AES256)
- SID specifikáció
- Pass-the-ticket (/ptt) injekció
- Mimikatz és Rubeus Silver jegyhasználati szokások

Az ATT&CK T1558.002-re összpontosítva.

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
## Ultra-Pro High-Fidelity AS-REP pörkölés és LDAP felsorolás
- **ID:** `T1558_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú AS-REP pörkölési tevékenységet célzó fiókokat
DONT_REQ_PREAUTH (UAC 4194304).

A fedezet a következőket tartalmazza:

- LDAP bitenkénti szűrők a DONT_REQ_PREAUTH számára
- Rubeus / Impacket / PowerView AS-REP pörkölés használat
- Hash export formázás (hashcat / john)
- Gyanús PowerShell vagy távoli végrehajtási vonal

Az ATT&CK T1558.004-re összpontosítva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Indirekt IPC és COM végrehajtás
- **ID:** `T1559.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** COM/DDE/WMI-n keresztül észleli a gyanús közvetett folyamatlétrehozást.
Azokra az „árva” folyamatokra összpontosít, amelyeknél egy Office-alkalmazás vagy böngésző aktiválódik
rendszerproxy a kód végrehajtásához, megkerülve a szokásos szülő-gyermek felügyeletet.

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
## High-Fidelity Office DDE kontextuális anomália
- **ID:** `T1559_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A Microsoft Office Dynamic Data Exchange (DDE) segítségével észleli a gyanús folyamatok megjelenését.
Szűri a jogos pénzügyi adatkapcsolatokat (Excel), és az Office-alkalmazások elindítására összpontosít
értelmezők vagy LOLBins DDE-specifikus parancssori jelölőkkel.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Hypervisor API és VM Escape Research
- **ID:** `T1559_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan interakciót a hypervisor API-kkal és diagnosztikai eszközökkel.
Az interaktív shellekből és gyanús parancssorból történő kézi végrehajtásra összpontosít
a virtuális gép kilépésével vagy a sandbox kikerülésével kapcsolatos paraméterek.

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
## Adatarchiválás kiszűréshez
- **ID:** `T1560_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú adatkezelést harmadik fél általi kiszűréshez
archiváló segédprogramok vagy PowerShell-tömörítés.

A fedezet a következőket tartalmazza:

- 7-Zip / WinRAR / tar / zip archívum létrehozása
- Jelszóval védett archívumok
- Hangerő felosztása
- Az archívum törlése utáni viselkedés
- Érzékeny adatcélzás
- Gyanús interaktív vagy webes végrehajtási környezet

Az ATT&CK T1560.001-re összpontosít (archívum a segédprogramon keresztül).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Adatarchiválás a könyvtáron keresztül
- **ID:** `T1560_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú adatsorolást a .NET vagy a kiszűréshez
PowerShell tömörítési könyvtárak.

A fedezet a következőket tartalmazza:

- A System.IO.Compression API-k közvetlen használata
- PowerShell Compress-Archive felhasználói/szerver adatcélzással
- Archívum létrehozása, majd kódolási viselkedés
- Gyanús végrehajtási vonal (webszerver, makró, shell)

Az ATT&CK T1560.002-re összpontosít (archívum a könyvtáron keresztül).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Archiválás egyéni módszerrel
- **ID:** `T1560_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú egyéni adatgyűjtési és -staging tevékenységet
bájtszintű fájlhozzáférés és kézi kódolási/obfuszkációs rutinok.

A fedezet a következőket tartalmazza:

- Nyers bájt szintű fájlhozzáférés (ReadAllBytes, MemoryStream)
- Kézi Base64/XOR/bitenkénti kódolás
- Rekurzív fájlok felsorolása a szakaszoláshoz
- Gyanús végrehajtási környezet (webszerver, shell, ideiglenes végrehajtás)

Az ATT&CK T1560.003-ra összpontosít (archiválás egyéni módszerrel).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lemeztörlés
- **ID:** `T1561.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú romboló lemezműveleteket, beleértve:

- Nyers fizikai lemez felülírása (MBR / GPT megsemmisítése)
- Partíciós tábla törlése (lemezpart tisztítása/törlése)
- Teljes lemezes tartalom felülírása (dd, nulla/véletlen adatfolyam)
- Pusztító PowerShell lemeztörlés
- Gyanús végrehajtási környezet (makró/webshell/LOLBIN)

A zsarolóvírusokra és a pusztító ablaktörlő tevékenységre összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lemeztartalom törlése
- **ID:** `T1561_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú romboló lemeztörlési tevékenységet ezen keresztül
nyers eszköz hozzáférés vagy destruktív felülírási műveletek.

A fedezet a következőket tartalmazza:

- Közvetlen nyers lemez hozzáférés (\\.\PhysicalDrive, \\.\Harddisk)
- Felülírás nulla/véletlen adatfolyamokkal
- STörölje a biztonságos törlést több lépéssel
- PowerShell romboló lemeztörlés
- Gyanús végrehajtási környezet (makró, webshell, ideiglenes végrehajtás)

A ransomware-szerű hatástevékenységre összpontosít (T1561.001).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lemezszerkezet törlése
- **ID:** `T1561_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú romboló lemezszerkezeti műveleteket, beleértve:

- Partíciós tábla törlése (lemezpart tisztítása / partíció törlése)
- MBR felülírás (az első 512 bájtos felülírási minták)
- Nyers fizikai meghajtó ír
- Pusztító PowerShell lemeztörlés
- Gyanús végrehajtási környezet (makró/webshell/LOLBIN)

A zsarolóvírusokra és a pusztító törlő viselkedésre összpontosít (T1561.002).

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
## A Windows eseménynapló szolgáltatásának károsodása
- **ID:** `T1562_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú kísérleteket a Windows eseménynaplózás letiltására, leállítására vagy rontására.

A fedezet a következőket tartalmazza:
- wevtutil csatorna letiltása vagy napló törlése
- Az EventLog szolgáltatás leállítási/letiltási kísérletei (sc, net, PowerShell)
- Registry alapú szolgáltatás vagy csatorna módosítás
- Szolgáltatásfüggőség manipulálása (DependOnService)

A MITER ATT&CK T1562.002 szabványhoz igazítva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Parancselőzmények naplózási károsodása
- **ID:** `T1562_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú elnyomási, átirányítási vagy manipulálási kísérleteket
interaktív parancselőzmények naplózása Windows rendszereken.

Az észlelési lefedettség a következőket tartalmazza:

- PowerShell PSReadLine naplózás elnyomása (SaveNothing, HistorySavePath visszaélés)
- Előzményfájl törlése (ConsoleHost_history.txt, PSReadLine mappa, bash történelem)
- Registry alapú konzol előzménypuffer elnyomása
- Kódolt PowerShell módosító előzmények viselkedése

Igazítva a MITER ATT&CK T1562.003-mal (Parancselőzmények naplózása).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús tűzfalmódosítás a Netsh.exe-n keresztül
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
## Kijelző blokkolása és telemetria elnyomása
- **ID:** `T1562_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a nagy megbízhatóságú Windows letiltására, elnyomására vagy beavatkozására irányuló kísérleteket
biztonsági telemetriai és felügyeleti csővezetékek, beleértve:

- ETW nyomkövetési munkamenetek leállítása vagy törlése
- A Windows eseménytovábbítás (WEF) letiltása vagy módosítása
- Kimenő tűzfalszabályok létrehozása a biztonsági telemetria blokkolására (EDR/AV HTTPS-en keresztül)

A védelmi kijátszásra összpontosít a MITER ATT&CK T1562.006 szabvány szerint.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Firewall károsodás (T1562.007)
- **ID:** `T1562_007.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a felhőtűzfalak és biztonsági csoportok magas kockázatú módosításait
ami forrásokat tehet ki az internetnek vagy gyengítheti a szegmentációt.
A BÁRMILYEN/BÁRMILYEN szabályokra, a privilegizált port kitettségre és a rendellenes identitásokra összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Felhőnaplózás károsodása (T1562.008)
- **ID:** `T1562_008.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a felhőnaplózás láthatóságának rontására irányuló kísérleteket a
a CloudTrail és az Azure naplózási konfigurációinak törlése vagy gyengítése.
A nyomvonal törlésére, a naplóérvényesítés letiltására és az eseményválasztóra összpontosít
visszaminősítések és tárhely-szabotázsok, amelyeket rendellenes identitások kezdeményeztek.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Csökkentett módú védelmi kijátszás (T1562.009)
- **ID:** `T1562_009.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rosszindulatú próbálkozásokat, amelyek a Windows csökkentett módba kényszerítésére irányulnak
biztonsági ellenőrzések.A BCDEdit safeboot konfigurációs módosításaira összpontosít,
A SafeBoot rendszerleíró adatbázis manipulálása és összehangolt kényszerített újraindítási tevékenység
gyanús végrehajtási összefüggésekből származik.

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
- **Leírás:** Érzékeli a PowerShell motort célzó szándékos biztonsági leminősítési kísérleteket
visszaállítás (v2 AMSI bypass), NTLM hitelesítés gyengítése és titkosítás
protokoll csökkentése.A leminősítési szándékra és a gyanúsításra összpontosít
végrehajtási kontextus a törvényes adminisztrációból származó téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Virtualizáció és Sandbox Evasion (T1564.011)
- **ID:** `T1562_011.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a virtualizáció azonosítására használt célzott környezeti ujjlenyomatokat,
sandbox vagy rosszindulatú programelemző környezetek.Összefügg a WMI hardveres lekérdezésekkel,
Virtuálisgép-szállítói karakterlánc-ellenőrzések, MAC OUI-felderítés és virtuális gép-specifikus illesztőprogram
gyanús folyamatláncokból vagy a felhasználó által írható útvonalakból indított felfedezés.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Felhőbiztonsági infrastruktúra károsodása (T1562.012)
- **ID:** `T1562_012.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli az AWS-natív biztonsági vezérlők megsértésére irányuló célzott kísérleteket, mint pl
GuardDuty, Security Hub és a kapcsolódó fenyegetés-felderítési mechanizmusok.
Az érzékelő törlésére, az elnyomási szabályokkal való visszaélésre és a fenyegető információk manipulálására összpontosít
gyökér, nem MFA vagy nem automatizált identitások kezdeményezték.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Távoli szolgáltatási munkamenet-eltérítés (T1563)
- **ID:** `T1563.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az RDP/Terminal Services munkamenet-eltérítést a tscon.exe-n keresztül a következő korrelációval:
- Hijack-specifikus parancssori paraméterek
- RENDSZER integritás végrehajtása
- Oldalirányú mozgás vagy héj alapú szülőfolyamatok
Kifejezetten szűri a legitim RDS/VDI hangszerelési és szolgáltatási környezeteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Helyi munkamenet-eltérítés (T1563.001)
- **ID:** `T1563_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fejlett helyi munkamenet-eltérítési kísérleteket, ahol a tscon.exe fájlt használják
meglévő felhasználói munkamenetekhez való csatoláshoz.A nagy pontosságú érzékelés a következőket tartalmazza:
- Gyanús parancssori argumentumok, amelyek konzolt vagy RDP-munkameneteket céloznak meg
- RENDSZER szintű végrehajtási környezet
- Nem megbízható szülői folyamatok (héjak, oldalirányú mozgatási eszközök, Office-alkalmazások)
A törvényes RDS/VDI kezelőeszközök kifejezetten ki vannak szűrve.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## RDP munkamenet-eltérítés (T1563.002)
- **ID:** `T1563_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan RDP-munkamenet-eltérítési és árnyékolási kísérleteket.
A nagy pontosságú észlelési lehetőségek:
- RENDSZER szintű végrehajtási környezet
- Rendellenes szülői folyamatok (héjak, oldalirányú mozgási eszközök)
- 'No-consent' árnyékolási paraméterek
Nem tartalmazza a törvényes RDP és távoli támogatási eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Műtermékek észlelésének elrejtése (T1564)
- **ID:** `T1564.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a célzott műtermék-elrejtési technikákat, beleértve:
- NTFS alternatív adatfolyamok (ADS)
- Registry alapú felhasználói fiókok elrejtése
- Gyanús fájlattribútum-manipuláció
Nem megbízható szülői folyamatok vagy a felhasználó által írható/nem szabványos útvonalak kezdeményezik.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rejtett fájlattribútum-manipuláció (T1564.001)
- **ID:** `T1564_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Fájlok és könyvtárak elrejtésének gyanús használatát észleli a System (+s) és a Hidden (+h) attribútumokon keresztül.
A nem megbízható szülői folyamatokra, a felhasználók által írható érzékeny könyvtárakra összpontosít, és elkerüli
ismert biztonságos rendszer vagy automatizálási tevékenységek.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rejtett felhasználói fiók létrehozása (T1564.002)
- **ID:** `T1564_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BASH.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Windows felhasználói fiókok elrejtésére irányuló kísérleteket a bejelentkezési képernyőről
a „SpecialAccounts\UserList” és a kapcsolódó rendszerleíró kulcsok módosításainak figyelése.
A gyanús szülőfolyamatokra, a rendszeren kívüli felhasználókra és a nem megbízható végrehajtási útvonalakra összpontosít,
miközben kiszűri a legitim rendszertelepítőket és az adminisztrációs automatizálást.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rejtett ablak végrehajtása (T1564.003)
- **ID:** `T1564_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús folyamatvégrehajtást rejtett ablakokkal,
a lopakodó zászlókra, az obfuszkációs technikákra és a nem megbízható szülői folyamatokra összpontosítva.
Úgy tervezték, hogy felfogja a felhasználói és az EDR láthatóságának elkerülésére irányuló kísérleteket, miközben minimalizálja a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## NTFS alternatív adatfolyammal (ADS) való visszaélés (T1564.004)
- **ID:** `T1564_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az NTFS alternatív adatfolyamok (ADS) létrehozását, módosítását vagy végrehajtását
gyakran használják a rosszindulatú rakományok elrejtésére vagy a végpontfigyelés elkerülésére.
Összekapcsolja az átirányítási operátorokat, a LOLBineket és az adatfolyam-specifikus PowerShell-parancsokat
miközben minimalizálja a MOTW és a rendszerfájlok téves pozitívumait.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rejtett fájlrendszer-manipuláció (T1564.005)
- **ID:** `T1564_005.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a virtuális lemezképek gyanús csatlakoztatását, létrehozását vagy manipulálását
(VHD, VHDX, ISO) a nem megbízható szülőfolyamatok CLI-parancsainak figyelésével, ill
nem szabványos utak.Ezt a technikát általában a Mark-of-the-Web (MOTW) megkerülésére használják.
korlátozások vagy a rosszindulatú rakományok elrejtése.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Virtuális példány végrehajtási visszaélés (T1564.006)
- **ID:** `T1564_006.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a virtuális példányok gyanús végrehajtását (Docker, VirtualBox, VMware)
a kriminalisztikai jelzőtáblák (--rm), a kiemelt eszkalációs kísérletek megfigyelésével,
gazdagép hálózatának használata és végrehajtása nem megbízható szülői folyamatokból (Office alkalmazások,
webszerverek, szkriptek).Megbízható fejlesztői és hangszerelési környezetek szűrése.

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
- **Leírás:** Érzékeli a Microsoft Office makróbiztonság megkerülésére vagy a VBA-projektek elrejtésére irányuló kísérleteket
a rendszerleíró adatbázis módosításainak, az Office Object Modell visszaéléseknek és a gyanúsnak a figyelésével
tolmács végrehajtás.A nem rendszergazdai vagy nem megbízható szülői folyamatokra összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## E-mailek elrejtésére vonatkozó szabályok észlelése (T1564.008)
- **ID:** `T1564_008.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az e-mail postafiók szabályainak gyanús módosításait, amelyek célja az elrejtés,
a biztonsággal kapcsolatos riasztások törlése vagy továbbítása.Figyeli a nem rendszergazdai szülőt
folyamatok és nem megbízható parancsértelmezők olyan műveletekhez, amelyek megakadályozhatják az észlelést
adathalászat, MFA-riasztások vagy jogosulatlan hozzáférési értesítések.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Erőforrás-kivonás és visszaélés (T1564.009)
- **ID:** `T1564_009.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a bináris erőforrás-szakaszokkal és a súgófájl értelmezőivel való visszaélést
(hh.exe, winhlp32.exe) rejtett hasznos adatok kibontásához vagy végrehajtásához.
Figyeli a gyanús szülői folyamatokat, a protokollcsempészetet (its:, ms-its:),
dekompilációs kísérletek és a nem szabványos fájl elérési utak.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Érveléshamisítás-észlelés feldolgozása (T1564.010)
- **ID:** `T1564_010.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a lehetséges folyamatargumentum-hamisítást, ha érzékeny tolmácsok vannak
(PowerShell, CMD, WMIC, CertUtil, Svchost, SchTasks) üres
vagy a nem megbízható szülői folyamatokból származó általános érvek, amelyek a védekezés kijátszására utalnak
technikák.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Virtuális példány visszaélés (T1564.011)
- **ID:** `T1564_011.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [WSL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Windows Sandbox, WSL és a kapcsolódó virtuális példányok gyanús használatát
hogy elkerülje az EDR megfigyelését.Figyeli a nem megbízható szülői folyamatokat, nem szabványos
konfiguráció betöltése és közvetlen parancsvégrehajtás virtualizált környezetben.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Adatkezelés (T1565)
- **ID:** `T1565.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a tárolt vagy továbbított adatok jogosulatlan manipulálását, beleértve az adatfolyam szerkesztését,
naplótörlés CLI-n keresztül, SQL/adatbázis-frissítések és a kritikus rendszerfájlok módosításai
(gazdagépek, eseménynaplók, rendszerkonfigurációk), amelyek nem szabványos szülőfolyamatokból származnak.
Tartalmazza a T1565.001 (tárolt adatok manipulációja) és a T1565.002 (továbbított adatok manipulációja)

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Tárolt adatok kezelése (T1565.001)
- **ID:** `T1565_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a tárolt adatok jogosulatlan módosítását, beleértve a konfigurációs fájlokat,
adatbázisok és rendszernaplók.Figyeli a gyanús adatfolyam-szerkesztést, az SQL-parancsokat,
vagy a nem szabványos szülőfolyamatokból származó PowerShell-cserék vagy
a kritikus rendszerútvonalak megcélzása, a jogos adminisztrációs tevékenység kiszűrése.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Továbbított adatok kezelése (T1565.002)
- **ID:** `T1565_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan hálózati átirányítást és a felbontási manipulációkat, beleértve a DNS-t, a proxyt,
és fájlmódosításokat tárol.Figyeli a CLI-alapú konfigurációs változásokat, amelyek innen származnak
gyanús szülőfolyamatokat vagy kritikus rendszerleíró kulcsokat céloz meg.Szűri a jogos adminisztrációt
és a rendszer tevékenységei a téves pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Futásidejű folyamatmanipuláció (T1565.003)
- **ID:** `T1565_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a futásidejű folyamatkezelést, beleértve a gyanús memóriaelérési maszkokat (pl. PROCESS_ALL_ACCESS)
és távoli menetinjektálás a nem kapcsolódó folyamatok között.A nem szabványos végrehajtási kontextusokra összpontosít
és kiszűri az ismert jó adminisztrációs, biztonsági és felügyeleti eszközöket a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú adathalászat-végrehajtás kommunikációs alkalmazásokból
- **ID:** `T1566.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az e-mail kliensek, böngészők vagy csevegőalkalmazások által létrehozott gyanús gyermekfolyamatokat
ahol a hasznos adat egy felhasználó által írható könyvtárból származik.Ez a minta az
nagyon jellemző az adathalászatra (T1566.001/.002).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Spearphishing melléklet végrehajtás
- **ID:** `T1566_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [MSPUB.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [VISIO.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az e-mail kliensekből vagy Office-alkalmazásokból származó, nagyon gyanús gyermekfolyamatokat.
Kifejezetten a szkript értelmezőket és a kettős felhasználású binárisokat (LOLBins) célozza meg
a felhasználó által írható könyvtárakból származnak, jelentősen csökkentve a hamis pozitívumot
a jogszerű rendszerfrissítésektől és a szabványos grafikus felhasználói felület viselkedésétől.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity böngészőből származó hasznos teher végrehajtás
- **ID:** `T1566_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a webböngészők által generált gyanús gyermekfolyamatokat, ahol a parancssor
felhasználó által írható vagy ideiglenes könyvtárakra hivatkozik.Ez a minta nagyon magas
sikeres spearphishing link támadást jelez, amely azonnali végrehajtáshoz vezet.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Process Spawn az üzleti kommunikációs szolgáltatásból
- **ID:** `T1566_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az üzleti kommunikációs eszközök által előidézett, rendkívül gyanús gyermekfolyamatokat
(Teams, Slack, Discord, LinkedIn).Kifejezetten a szkript értelmezőket célozza meg
és kettős felhasználású binárisok (LOLBins), amelyek a felhasználó által írható könyvtárakból futnak le,
hatékonyan kiszűri a jogos alkalmazásfrissítéseket és böngészőindításokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## A látás utáni távoli eszköz-végrehajtás nagy pontosságú észlelése
- **ID:** `T1566_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a jogosulatlan távoli elérési eszközök (AnyDesk, TeamViewer stb.) végrehajtását.
különösen, ha a felhasználó által írható könyvtárakból fut (Letöltések, Temp).
Ez a minta egy sikeres vishing támadás nagy megbízhatóságú mutatója, ahol
az áldozatot utasítják, hogy futtasson "támogató" szoftvert.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Webszolgáltatás kiszűrése (T1567)
- **ID:** `T1567.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli az adatok szisztematikus kiszűrését webes vagy felhőszolgáltatásokba a következők figyelésével:
1. Fej nélküli átviteli eszközök (rclone, megatools, mega-put) és egyedi webkliensek.
2. Internetes végpontokat, felhőalapú tárolást vagy nyilvános beillesztési/webhook-szolgáltatásokat célzó automatizált feltöltések.
3. Végrehajtás nem megbízható könyvtárakból vagy nem adminisztratív szülőfolyamatokból (Office alkalmazások, rundll32, Explorer).
Szűri a jogos adminisztrációs eszközöket, a helyi gazdagép műveleteit és a rendszerfolyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exfil kódtár (T1567.001)
- **ID:** `T1567_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a forráskód szisztematikus kiszűrését nyilvános adattárakba azáltal, hogy figyeli:
1. Fej nélküli vagy automatizált Git/CLI műveletek (git.exe, gh.exe, curl, PowerShell)
nem fejlesztői szülőfolyamatokból vagy gyanús könyvtárakból hajtják végre.
2. Soron belüli hitelesítési tokenek vagy személyes hozzáférési jogkivonatok (PAT) a parancssorokban.
3. Távoli adattár újrakonfigurálása vagy jogosulatlan adatátvitelre utaló kényszerített leküldések.
Szűri a jogszerű fejlesztői IDE-használatot és a jóváhagyott adattárműveleteket.

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
- **Leírás:** Észleli az adatok szisztematikus kiszűrését a felhőalapú tárolási platformokra a következők figyelésével:
1. CLI eszközök (rclone, megatools, pcloud kliensek) beágyazott hitelesítő adatokkal
vagy egyéni konfigurációs fájlokat.
2. Nem adminisztratív vagy gyanús szülői folyamatok általi kiváltás
(Irodai alkalmazások, Beacon hostok, szkriptek).
3. Célzott felhő-végpontok, beleértve a mega.nz, Dropbox, Google Drive, pCloud,
és Transfer.sh.
Szűri a jogos rendszer-/adminisztrációs használatot, hogy csökkentse a hamis pozitív eredményeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Videotárhely Exfil (T1567.003)
- **ID:** `T1567_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a titkos adatszivárgást videotárhely-platformokon keresztül, figyelve:
1. Szteganográfiai beágyazás videofájlokba (metaadat-visszaélés, adatfolyam-csatolás).
2. Nyilvános videoplatformokat célzó CLI alapú feltöltések nem kreatív ill
nem engedélyezett eszközök.
Nem tartalmazza a legitim kreatív alkalmazásokat és rendszerfolyamatokat.

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
- **Leírás:** Érzékeli az érzékeny adatok programozott kiszűrését nyilvános szövegtároló platformokra
(Pastebin, Ghostbin, Hastebin, ControlC, Rentry) figyeléssel:
1. CLI-alapú POST kérések, amelyek API-kulcsokat vagy adathordozókat tartalmaznak.
2. Vágólap-kaparási parancsok vagy érzékeny fájlhozzáférés.
3. Végrehajtás nem adminisztratív vagy gyanús szülői folyamatokból.
Nem tartalmazza a jogos adminisztrációs és szoftverfrissítési tevékenységeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Dinamikus felbontás és DGA (T1568)
- **ID:** `T1568.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a dinamikus DNS-feloldást és a Domain Generation Algorithm (DGA) tevékenységet
figyeléssel:
1. Programozott DNS-lekérdezések ciklusokon belül vagy újrapróbálkozási logikán belül.
2. Alacsony szintű DNS API hívások szkript értelmezőktől.
3. Nagy entrópiás és rendellenes tartományminták a parancssorokban.
Kizárja a törvényes adminisztrációs, automatizálási és belső tartományokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Fast Flux és DNS Cache Evasion (T1568.001)
- **ID:** `T1568_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Felismeri a Fast Flux DNS-infrastruktúra használatát és a DNS-gyorsítótár-kijátszást a következők figyelésével:
1. Kényszerített DNS-gyorsítótár-öblítés rendszerparancsokkal vagy PowerShell-lel.
2. Programozott DNS-feloldás hurkos kapcsolódási ellenőrzésekkel kombinálva.
3. Végrehajtás nem szabványos parancsfájl- vagy értelmező folyamatokból.
Kizárja a jogos adminisztrációs és felhőalapú automatizálási tevékenységeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Domaingenerációs algoritmus (DGA) észlelése (T1568.002)
- **ID:** `T1568_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a programozott tartománygenerálási algoritmus (DGA) tevékenységét a következők figyelésével:
1. Gyors DNS-feloldási kísérletek API-n vagy CLI-n keresztül
2. Nagy entrópiájú vagy gyanús tartományminták a parancssorban
3. DNS-hibák elnyomása az észlelés elkerülése érdekében.
Kiszűri a legális szoftvereket, a felhőautomatizálást és a belső infrastruktúra forgalmat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## DNS számítás és kinyerés (T1568.003)
- **ID:** `T1568_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a C2 infrastruktúra címszámítását DNS-en keresztül a programozott figyeléssel
TXT/SRV rekordok lekérése, majd bájt szintű manipuláció vagy típuskonverzió
forgatókönyv-értelmezésekben.Kiszűri a jogszerű DNS-alapú automatizálást, a licencellenőrzéseket,
és domain-ellenőrzési folyamatok.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity rendszerszolgáltatás-végrehajtás észlelése
- **ID:** `T1569.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Gyanús jellemzőkkel rendelkező rendszerszolgáltatások létrehozását vagy végrehajtását észleli,
mint például a világszerte írható könyvtárakban található binárisok vagy a használt szolgáltatások
burkolók a shell parancsokhoz.A legális szoftvertelepítők kiszűrésére optimalizálva.

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
- **Leírás:** Figyeléssel észleli a Launch Daemonok létrehozását vagy módosítását
nem megbízható szülőfolyamatok és gyanús parancssori karakterláncok.
Az Apple és a gyakori külső telepítők kiszűrésére optimalizálva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity rendszerszolgáltatás-végrehajtás észlelése (T1569.002)
- **ID:** `T1569_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Az anomáliák figyelésével észleli a gyanús szolgáltatásvégrehajtást vagy -módosítást
szülőfolyamatok, világra írható bináris elérési utak és shell parancsburkolók.
Az alacsony téves pozitív arányra optimalizálva vállalati környezetben.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Oldalirányú szerszámátvitel (T1570)
- **ID:** `T1570.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan oldalirányú eszközátvitelt az adminisztrációs megosztásokon (C$, ADMIN$, IPC$) keresztül.
A nem szabványos leszármazási vonalakból származó magas kockázatú folyamattevékenységre összpontosít
(Irodai alkalmazások, böngészők, nem emelt héjak) és ismert átviteli segédprogramok
mint a robocopy, bitsadmin, xcopy vagy certutil.Kizárja a legitim rendszert
automatizálási és szoftverforgalmazási tevékenység.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nem szabványos C2 port (T1571)
- **ID:** `T1571.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a parancs és vezérlés (C2) kommunikációt a nem szabványos portokon keresztül
a magas kockázatú natív binárisok (LoLBins) korrelációja a kimenő nyilvános hálózattal
kapcsolatok a szabványos web-, levelezési és címtárszolgáltatási tartományon kívüli portokhoz.
Kiszűri a törvényes automatizálást, a belső hálózati forgalmat és a rendszerbináris fájlokat
a hamis pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Protokoll-alagút-észlelés (T1572)
- **ID:** `T1572.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az ellenfél protokoll-alagútját a nem szabványos tokozás azonosításával,
alacsony szintű socket proxy (SOCKS5/Reverse) és az ismert alagút CLI aláírásai
eszközöket.Kiszűri a legitim adminisztratív VPN/SSH-forgalmat és automatizálási eszközöket
a hamis pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Titkosított C2 csatorna (T1573)
- **ID:** `T1573.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Alacsony szintű korrelációval érzékeli az egyéni titkosított C2 csatornák létrehozását
szimmetrikus kriptográfia (AES/Rijndael, CryptoStream, ICryptoTransform)
kézi hálózati aljzathasználattal a szkript értelmezőktől.
Kiszűri a legitim automatizálást, felhőszolgáltatásokat és rendszerfolyamatokat
a hamis pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Szimmetrikus titkosítás C2 csatorna (T1573.001)
- **ID:** `T1573_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Egyéni szimmetrikus titkosítás (AES/Rijndael) gyanús használatát észleli a C2 csatornákon.
A CipherMode, PaddingMode és CryptoStreams programozott beállítására összpontosít
script motorok, amelyek kifejezetten a kézi IV/Kulcs hozzárendelést és az adatfolyam-vezetékeket célozzák meg
nem szabványos folyamatokból vagy nem megbízható végrehajtási környezetekből.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Aszimmetrikus titkosítás C2 (T1573.002)
- **ID:** `T1573_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Gyanús aszimmetrikus titkosítási használatot (RSA/ECC) észlel, ami arra utalhat,
C2 vagy adatkiszűrési tevékenység.A programozott megbízhatósági lánc felülírásaira összpontosít
(ServerCertificateValidationCallback) és nyers nyilvános kulcs importálása (FromXmlString,
ImportSubjectPublicKeyInfo) nem megbízható vagy nem szabványos folyamatokból.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro DLL-eltérítés és oldalsó betöltés észlelése (T1574)
- **ID:** `T1574.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A megbízható rendszer figyelésével észleli a lehetséges DLL-eltérítést vagy oldalbetöltést
bináris fájlok betöltik a DLL-eket nem szabványos, felhasználó által írható könyvtárakból, míg
a legitim aláírt modulok és az ismert alkalmazási viselkedések kiszűrése.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro DLL keresési rendelés-eltérítés észlelése (T1574.001)
- **ID:** `T1574_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a megbízható Windows rendszerbináris fájlokat, amelyek nem szabványos DLL-eket töltenek be,
potenciálisan a felhasználó által írható könyvtárak.Az érvényesen aláírtakat kiszűri
harmadik féltől származó modulok a téves pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro DLL oldalsó betöltési integritáshiány-észlelés (T1574.002)
- **ID:** `T1574_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges DLL oldalbetöltést azáltal, hogy azonosítja azokat az eseteket, amikor egy aláírt,
A megbízható végrehajtható fájl egy aláíratlan vagy gyanúsan elhelyezkedő DLL-t tölt be innen
a felhasználó által írható könyvtárak.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro Shell konfigurálás és útvonal elfogás (T1574.003)
- **ID:** `T1574_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a PATH környezeti változók jogosulatlan módosítását vagy a shell automatikus futtatását
rendszerleíró kulcsok.A "Path Prepending"-re összpontosít (rosszindulatú útvonalak elhelyezése a
kezdete) és a nem szabványos shell indítóparancsok.

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
- **Leírás:** A megbízható rendszerbinárisok figyelésével észleli a lehetséges könyvtár-eltérítést
aláíratlan vagy gyanúsan elhelyezkedő DLL-ek betöltése a felhasználó által írható könyvtárakból,
kifejezetten az EXE és a DLL közötti bizalmi eltéréseket keresi.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro telepítőfájl engedélyek gyengesége (T1574.005)
- **ID:** `T1574_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a felhasználó által írható helyekről származó bináris fájlok magas szintű végrehajtását.
Ez azokat a forgatókönyveket célozza meg, amikor egy támadó lecseréli a legitim telepítőt
rosszindulatúval a nem biztonságos címtárengedélyek miatt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Dinamikus linker eltérítés a privilegizált bináris ellen
- **ID:** `T1574_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Észleli a dinamikus linker-eltérítést azáltal, hogy azonosítja a privilegizált vagy SetUID Linux binárisok végrehajtását manipulált dinamikus linker környezeti változókkal, amelyek a felhasználó által írható megosztott könyvtárakra mutatnak.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## PATH-eltérítés, amely privilegizált bináris végrehajtáshoz vezet
- **ID:** `T1574_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a PATH környezeti változók eltérítését, amikor egy privilegizált Linux bináris fájl végrehajtásra kerül a PATH elején a felhasználó által írható könyvtárral, és egy nem abszolút parancsot feloldanak, jelezve, hogy egy életképes útvonalelfogó támadási lánc van.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## .NET Assembly Search Megrendelés eltérítése User-Writable Directory segítségével
- **ID:** `T1574_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges .NET-összeállítás-keresési sorrend feltörését, amikor egy legitim .NET futásidejű gazdagép betölt egy felügyelt összeállítást a GAC-on, a Microsoft.NET-keretrendszer elérési útjain vagy az alkalmazástelepítési könyvtáron kívüli, a felhasználó által írható könyvtárból.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## .NET AppDomainManager eltérítés nem-GAC összeállításon keresztül
- **ID:** `T1574_009.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a .NET AppDomainManager feltörését azáltal, hogy azonosítja azokat a .NET futásidejű gazdagépeket, amelyek a folyamat inicializálása során egy felügyelt összeállítást töltenek be a felhasználó által írható könyvtárból, a GAC ​​és a Microsoft .NET keretrendszer elérési útjain kívül.Ez a viselkedés erősen rosszindulatú AppDomainManager visszaélésre utal.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Privilegizált szolgáltatás végrehajtható felülírva a felhasználó által írható helyről
- **ID:** `T1574_010.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a gyenge szolgáltatásfájl-engedélyek kihasználását, amikor a magas jogosultságokkal futó regisztrált Windows szolgáltatás végrehajtható fájlját felülírja vagy módosítja a felhasználó által írható könyvtárból egy nem rendszerfolyamat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Privileged Service ImagePath vagy ServiceDll feltörve a rendszerleíró adatbázison keresztül
- **ID:** `T1574_011.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyenge Windows szolgáltatás-nyilvántartási engedélyek kihasználását, amikor egy nem rendszerfolyamat úgy módosítja a kritikus szolgáltatás-nyilvántartási értékeket, hogy a felhasználó által írható könyvtárban található végrehajtható fájlra vagy DLL-re mutasson, lehetővé téve a jogosultságok kiszélesítését a szolgáltatás indításakor vagy újraindításakor.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-Grade COR_PROFILER eltérítés a User-Writable Profiler DLL-en keresztül
- **ID:** `T1574_012.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/), [VSJITDEBUGGER.EXE](https://lolbas-project.github.io/lolbas/), [VSTEST.CONSOLE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a COR_PROFILER eltérítés kihasználását, amikor egy .NET futásidejű gazdagép úgy fut le, hogy a profilozás engedélyezve van, és egy egyéni profilkészítő DLL van megadva a felhasználó által írható könyvtárból, kizárva a Microsoft, a Visual Studio és az APM profilalkotási eseteit.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Exploit-grade KernelCallbackTable Manipulation
- **ID:** `T1574_013.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a GUI-folyamatokat célzó gyanús távoli memória írási műveleteket,
amelyek a KernelCallbackTable eltérítési kísérletekre utalnak.Ez a technika
általánosan használt lopakodó folyamatinjektáláshoz, amely megkerüli a hagyományos horog alapú felügyeletet.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Felhő-infrastruktúra manipulálása (T1578)
- **ID:** `T1578.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a felhő-infrastruktúra magas kockázatú módosításait, amelyek gyengítik a biztonsági helyzetet
vagy készüljön fel az adatok kiszűrésére.Kézi, megbízhatatlan vagy rendellenes dolgokra összpontosít
személyazonossági műveleteket, miközben kiszűri az automatizált és belső műveleteket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús felhőpéldány létrehozása (T1578.001)
- **ID:** `T1578_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy erőforrásigényű vagy drága felhőpéldányok létrehozását a nem megbízható forrásokból
identitások vagy jóváhagyott régiókon kívül.Cryptojacking-re optimalizálva és jogosulatlanul
erőforrás-visszaélés, miközben kiszűri a CI/CD és az automatikus skálázási műveleteket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Snapshot Exfiltration (T1578.002)
- **ID:** `T1578_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a felhőalapú számítási pillanatképek jogosulatlan megosztását, fiókok közötti hozzáférését vagy nyilvános közzétételét.
Az egyszerű pillanatkép-készítés helyett a magas kockázatú engedélymódosításokra összpontosít, és kiszűri
megbízható biztonsági mentési és replikációs folyamatok.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Felhőpéldány-megsemmisítés (T1578.003)
- **ID:** `T1578_003.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a felhőpéldányok jogosulatlan vagy tömeges törlését az Azure-ban, AWS-ben,
és GCP környezetek.Kézi, nem MFA vagy gyanús szkriptekre összpontosít
törlések, amelyek szabotázsra vagy védelmi kijátszásra utalhatnak, ugyanakkor kizárják
törvényes automatizált skálázási események.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Felhőkép-szabotázs (T1578.004)
- **ID:** `T1578_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a felhőalapú gépek képeinek (AMI, VHD, Managed Images) jogosulatlan módosításait.
Azokra az engedélymódosításokra összpontosít, amelyek külső fiókok vagy nyilvános internet számára teszik ki a képeket.
A környezettudatos észlelés kizárja a törvényes CI/CD- és képalkotási folyamatokat, miközben magában foglalja a gyanús interaktív munkameneteket is.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Cloud Network Security Regression (T1578.005)
- **ID:** `T1578_005.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a hálózati ACL-ek vagy biztonsági csoportok magas kockázatú módosításait, amelyek lehetővé teszik
széles körű belépés (0.0.0.0/0 vagy ::/0) érzékeny felügyeleti portokon (RDP, SSH, DB).
Tartalmazza a gyanús ügyféleszközök környezettudatos ellenőrzését, és letiltja az MFA használatát.
Kiszűri a törvényes IaC automatizálási és belső szolgáltatási műveleteket.

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
- **Leírás:** Érzékeli a felhő-infrastruktúra-erőforrások szisztematikus felfedezését (VM-ek, VPC-k, S3-tárolók, tárfiókok)
a rendellenes CLI-használat, a kimeneti kivonás és az interaktív szekciókontextusok figyelésével.
Kiszűri a legitim Infrastructure-as-Code (IaC) és CI/CD automatizálási eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity offensive Infrastructure Provisioning – T1583
- **ID:** `T1583.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az infrastruktúra (VPS, tartományok, kiszolgáló nélküli) automatizált megszerzését a CLI-alapú kiépítési eszközök és a domain regisztrációs API-hívások figyelésével.A szűrők az engedélyezett DevOps folyamatok és fejlesztői környezetek elkülönítésére összpontosítanak.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity VPS infrastruktúra kiépítése – T1583.001
- **ID:** `T1583_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a VPS-infrastruktúra (DigitalOcean, AWS, Azure, GCP) automatizált beszerzését.A kiépítési fázisra (VM létrehozására) összpontosít, miközben elkülöníti az engedélyezett DevOps folyamatokat és az interaktív fejlesztői munkafolyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú automatizált domainregisztráció és -szerzés – T1583.002
- **ID:** `T1583_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az automatikus domain regisztrációt regisztrátor API-kon és speciális kiépítési eszközökön keresztül.A curl/pythonon keresztüli programozott adatgyűjtésre összpontosít, miközben kiszűri az engedélyezett IT-infrastruktúra-kezelést (Certbot, Terraform).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Network (VPC) kiépítése – T1583.003
- **ID:** `T1583_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a felhőalapú hálózatok (VPC) megszerzését és konfigurálását.Az internetes kilépési pontok és a hálózatokon átívelő hidak létrehozásának azonosítására összpontosít az illetéktelen végpontoktól, valamint az automatizált CI/CD folyamatok elkülönítésére a kézi vagy parancsfájllal ellátott helyi visszaélésektől.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity szerver nélküli infrastruktúra kiépítés - T1583.004
- **ID:** `T1583_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kiszolgáló nélküli infrastruktúra (AWS Lambda, Azure Functions, GCP Functions) automatizált beszerzését és kiépítését.A CLI-alapú létrehozásra és a kritikus konfigurációs változtatásokra összpontosít, miközben elkülöníti az engedélyezett CI/CD-folyamatokat és az interaktív fejlesztői IDE környezeteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity botnet infrastruktúra megszerzése – T1583.005
- **ID:** `T1583_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a botnet infrastruktúra megszerzését és előkészítését.A több architektúrájú ügynökletöltések, az automatikus terjesztési kísérletek (brute-force) és a botnet C2 kliens használatának azonosítására összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity webszolgáltatás beszerzése és kiépítése – T1583.006
- **ID:** `T1583_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a webszolgáltatások (SaaS, Storage, Messaging) megszerzését és beállítását támadó infrastruktúrához.A nem adminisztratív vagy nem fejlesztői végpontokról a parancssori alapú tárolási kiépítésre (Rclone, AzCopy) és az üzenetküldő API inicializálására (Slack/Discord/Telegram botok) összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity szerver nélküli infrastruktúra kiépítés - T1583.007
- **ID:** `T1583_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kiszolgáló nélküli infrastruktúra (AWS Lambda, Azure Functions, GCP Functions) automatizált beszerzését és kiépítését.A CLI-alapú létrehozásra és a kritikus konfigurációs változtatásokra összpontosít, miközben elkülöníti az engedélyezett CI/CD-folyamatokat és az interaktív fejlesztői IDE környezeteket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud-fiókszerzés és rendszerindítás – T1583.008
- **ID:** `T1583_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a felhőalapú fiókok beszerzését és kezdeti konfigurációját.Célja a fiókszintű rendszerindítás (hitelesítési adatok beállítása, IAM-felhasználók létrehozása) és az automatikus identitásgyűjtés a nem szabványos folyamatokból, miközben kiszűri az engedélyezett DevOps folyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity kompromittált infrastruktúra és erőforrás-visszaélés – T1584
- **ID:** `T1584.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kompromittált infrastruktúra jelzéseit, különös tekintettel a webszerver-folyamatok felforgatására (Web Shell), a jogosulatlan fordított proxykra és a nem szabványos adminisztrációs környezetből futtatott alagútkezelő eszközökre.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú tartományi infrastruktúra eltérítése – T1584.001
- **ID:** `T1584_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A kritikus DNS-rekordtípusok (NS, SOA) és a Cloud Provider CLI-n keresztüli tömeges rekordok létrehozásának figyelésével észleli a jogosulatlan domain- vagy aldomain-eltérítést, miközben szűri az engedélyezett DevOps-automatizálást.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú DNS-kiszolgáló konfigurációs szubverzió – T1584.002
- **ID:** `T1584_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [DNSCMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan DNS-infrastruktúra-manipulációkat a kritikus konfigurációs változások (zóna-visszaállítások, főfrissítések) és a közvetlenül a DNS-szolgáltatásokból származó gyanús gyermekfolyamatok figyelésével.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Identity Felforgatás és tartósság – T1584.003
- **ID:** `T1584_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a felhőalapú fiókok jogosulatlan manipulálását azáltal, hogy figyeli a nagy kockázatú identitásmódosításokat (MFA eltávolítás, új hozzáférési kulcsok), amelyek az engedélyezett CI/CD folyamatokon vagy ismert adminisztratív ugrásgazdagépeken kívül hajtódnak végre.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Serverless Function Subversion – T1584.004
- **ID:** `T1584_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kiszolgáló nélküli funkciók (Lambda, Azure Functions, GCP) jogosulatlan módosításait azáltal, hogy olyan magas kockázatú paraméterekre összpontosít, mint a réteginjektálás és a környezeti változók manipulálása, miközben szigorúan szűri az engedélyezett CI/CD folyamatszolgáltatási fiókokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Botnet Agent Perzisztencia és ellenőrzés – T1584.005
- **ID:** `T1584_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a botnet ügynök tevékenységét a gyanús folyamatvonalak (például a WMI-ből származó LOLBinek), a P2P rendszerindítási argumentumok és az ismert DDoS-eszközminták azonosításával, miközben szűri az engedélyezett IT-felügyeleti és P2P-szoftvereket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Web Service és Cloud Storage Subversion – T1584.006
- **ID:** `T1584_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a webszolgáltatások és a felhőalapú tárolás jogosulatlan manipulálását az ACL-módosítások (a gyűjtőcsoportok nyilvánossá tétele), a gyanús fájltípusok (szkriptek/exe-k), valamint a harmadik féltől származó adatátviteli eszközök (rclone) engedélyezett kontextusokon kívüli használatának figyelésével.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity VPS vezérlés és alagút - T1584.007
- **ID:** `T1584_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan VPS-manipulációt a kritikus életciklus-módosítások (SSH-kulcs-injektálás, tűzfalnyitás) és a nem engedélyezett adminisztratív környezetből származó fordított alagútkezelési eszközök végrehajtásának azonosításával.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús felhasználói fiók létrehozása CLI/Scripting segítségével
- **ID:** `T1585.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az új felhasználói fiókok (T1585) létrehozását, amikor kezdeményezi
gyanús folyamatok, például CMD, PowerShell vagy net.exe helyett
szabványos felügyeleti konzolok (ADUC, Windows Admin Center).

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lehetséges automatizált közösségimédia-fiók létrehozása
- **ID:** `T1585_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Figyeléssel észleli a közösségi média fiókok regisztrációjának gyanús mintáit
hozzáférés több regisztrációs végponthoz egyetlen gazdagépről vagy azonosítóról
nem böngésző folyamatok, amelyek kéréseket küldenek ezekre a tartományokra.

#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Lopakodó e-mail fiók létrehozása és manipulálása
- **ID:** `T1585_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli az e-mail fiókok létrehozását, majd azonnali érzékeny
engedélymódosítások vagy továbbítási szabályok.A CLI-alapú végrehajtásra összpontosít
a szabványos HR-vezérelt grafikus felületi folyamatok zajának csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendellenes Cloud felhasználói fiók létrehozása
- **ID:** `T1585_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a felhőalapú fiókok létrehozását parancssori eszközökön vagy egyszerű szolgáltatásain keresztül,
kivéve az engedélyezett szinkronizálási fiókokat és az automatizált HR-ellátó rendszereket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú fiókkompromittálódás és személyazonosság-manipuláció - T1586
- **ID:** `T1586.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fiókkompromittálásra és -átvételre (ATO) utaló műveleteket, például a jogosulatlan MFA-módosítást, a bejelentkezési profil gyanús frissítéseit és a nem szabványos adminisztrációs folyamatokból származó hitelesítő adatok automatikus tesztelését.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity automatizált közösségi média manipuláció - T1586.001
- **ID:** `T1586_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az automatizált interakciót a közösségi média platformokkal fej nélküli böngésző kereteken keresztül (Selenium, Puppeteer, Playwright).A támadók ezeket a fiókok átvételére (ATO) használják, és lopott cookie-k beiktatásával megkerülik a biztonsági ellenőrzéseket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity e-mail továbbítási szabály manipulációja – T1586.002
- **ID:** `T1586_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az e-mail továbbítási/átirányítási szabályok létrehozását vagy módosítását parancssori eszközökön keresztül (PowerShell, Microsoft Graph CLI).Ez a fiókátvétel (ATO) nagy megbízhatóságú mutatója, amikor a támadó felhasználói beavatkozás nélkül próbál kiszivárogni az érzékeny e-mailekből (számlák, jelszó-visszaállítások).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud-fiók átvétele és fennmaradása – T1586.003
- **ID:** `T1586_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a felhőalapú fiókok jogosulatlan manipulációját, az identitás átvételére és fennmaradására összpontosítva.Új felhőalapú hitelesítési adatok létrehozását, MFA-eltávolítást és bejelentkezési profilfrissítéseket céloz meg nem engedélyezett folyamatokból, kifejezetten kiszűrve az ismert adminisztrációs és fejlesztői munkafolyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity offenzív képességfejlesztés és összeállítás - T1587
- **ID:** `T1587.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [JSC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a támadó eszközök fejlesztését és összeállítását azáltal, hogy figyeli a specifikus C2 keretrendszer felépítési argumentumait, a kódcsomagolók jogosulatlan használatát és az ellenőrzött CI/CD folyamatokon kívüli tanúsítványmanipulációt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity kártevő-fejlesztési és kijátszási minták – T1587.001
- **ID:** `T1587_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az egyéni rosszindulatú programok fejlesztését azáltal, hogy azonosítja a gyanús fordítóvégrehajtást, valamint az adókijátszással kapcsolatos API-karakterláncokat, az anti-analízis technikákat és a jogosulatlan összeállítási helyeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity jogosulatlan kódaláírási képesség fejlesztése - T1587.002
- **ID:** `T1587_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a kód-aláíró tanúsítványok létrehozását és a bináris fájlok kézi aláírását bizonyos OID-k (1.3.6.1.5.5.7.3.3) és ellenőrzött CI/CD-folyamatokon vagy Windows SDK-útvonalakon kívül használt aláírási eszközök figyelésével.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity jogosulatlan digitális tanúsítvány fejlesztés - T1587.003
- **ID:** `T1587_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan digitális tanúsítványt és a magánkulcs-generálást azáltal, hogy figyeli a magas kockázatú parancssori argumentumokat (önaláírás, kulcskiszűrés), amelyek nem szabványos könyvtárakban vagy jogosulatlan felhasználók által fordulnak elő.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity exploit fejlesztés és fordítás észlelése - T1587.004
- **ID:** `T1587_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Felismeri a kihasználás fejlesztésének mutatóit azáltal, hogy figyeli a memóriainjektáló primitíveket és shellkóddal kapcsolatos argumentumokat tartalmazó forráskód fordítását, különösen akkor, ha nem szabványos vagy ideiglenes könyvtárakból hajtják végre.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Támadó képességek rendellenes beszerzése
- **ID:** `T1588.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A gyanús kombinációk figyelésével észleli a támadó eszközök megszerzését
letölthető folyamatok és ismert hacktool aláírások vagy fájlkiterjesztések,
a legális informatikai szoftvertelepítési eszközök kiszűrése.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## A rosszindulatú programok rendellenes beszerzése
- **ID:** `T1588_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A gyanús letöltők figyelésével észleli a rosszindulatú programok megszerzését (LotL)
interakció a tömörített/tároló formátumokkal vagy ismert rosszindulatú programok elnevezési mintákkal
nem szabványos könyvtárakban.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendellenes támadóeszköz-beszerzés CLI-n keresztül
- **ID:** `T1588_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** A parancssori figyeléssel észleli a támadó eszközök (hacktools) megszerzését
nem szabványos könyvtárakat célzó letöltések.Kiszűri a legitim IT-t
adminisztráció a böngészőkből és az engedélyezett felügyeleti ügynökökből.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendellenes kód aláíró tanúsítvány exportálása vagy beszerzése
- **ID:** `T1588_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Gyanús tanúsítványműveleteket észlel (privát kulcsok exportálása vagy kényszerített tárolási kiegészítések)
szokatlan szülőfolyamatokból vagy egyszerű szöveges jelszavak használatával kezdeményezett parancssorban.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Stratégiai megbízható gyökértanúsítvány-tárolási manipuláció
- **ID:** `T1588_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Trusted Root Certification Authorities módosítására irányuló jogosulatlan kísérleteket
boltba.A támadók ezt azért teszik, hogy megkönnyítsék a MitM támadásokat vagy megkerüljék a biztonsági figyelmeztetéseket.
Kiszűri a legitim rendszerszintű telepítőket és az ismert biztonsági ügynököket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Az Exploit vagy PoC kód rendellenes beszerzése
- **ID:** `T1588_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Figyeléssel észleli a kihasználások vagy a Proof-of-Concept (PoC) kód megszerzését
gyanús letöltési minták, CLI-alapú átvitelek és ismert exploit elnevezések
konvenciókat, miközben kiszűri az engedélyezett biztonsági szkennereket és a fejlesztői tevékenységet.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## A sérülékenységkutatási műtermékek célzott begyűjtése
- **ID:** `T1588_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a sebezhetőségi kutatások, audit jelentések szisztematikus beszerzését, ill
nulladik napos PoC dokumentáció.A CLI-alapú betakarításra összpontosít a nem műszaki területen
felhasználói kontextusokat, miközben kiszűri az engedélyezett biztonsági kutatásokat.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú identitásfelsorolás hitelesítési végpontokon keresztül
- **ID:** `T1589.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy megbízhatóságú identitásfelderítési tevékenységet, ahol egy külső szereplő hitelesítéssel vagy fiókhoz kapcsolódó végpontokkal számba veszi az érvényes felhasználói identitásokat.Az észlelés a számlálási viselkedésen, az automatizálási mutatókon és a hitelesítési válaszmintákon alapul, kivéve a böngészőket, az egyszeri bejelentkezési folyamatokat és a megfigyelő eszközöket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hitelesítési adatok felsorolása Authentication API-n keresztül (magas megbízhatóság)
- **ID:** `T1589_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy megbízhatóságú hitelesítő adatok felsorolási tevékenységét a hitelesítési API-kkal szemben.A szabály az automatizált, nem interaktív vizsgálati viselkedésre összpontosít, amely megpróbálja ellenőrizni a hitelesítő adatok meglétét vagy helyességét.A hamis pozitívumok minimalizálása érdekében a böngésző alapú bejelentkezések, az SSO-folyamatok, a megfigyelőrendszerek és a legitim felhasználói hitelesítés kizárt.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Magas megbízhatóságú OSINT identitásfeltárás nyilvános API-kon keresztül
- **ID:** `T1589_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy megbízhatóságú nyílt forráskódú identitás-felsorolási kísérleteket nyilvános API-kon vagy címtárvégpontokon keresztül.Ez a szabály a felhasználói vagy alkalmazottak személyazonossági adatainak gyűjtésére tervezett, szkriptelt, automatizált felderítési viselkedésre összpontosít, miközben kizárja a normál böngészést, a keresőmotorokat és a törvényes bejárókat, hogy minimalizálja a hamis pozitív eredményeket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nyitott webhelyek és tartományok célzott OSINT felsorolása
- **ID:** `T1589_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy megbízhatóságú felderítési tevékenységet, amely nyitott webhelyeket és domaineket céloz meg, hogy összegyűjtse az áldozatok személyazonosságát.A szabály a keresési vagy címtár-stílusú végpontokkal szembeni parancsfájl-felsorolási viselkedésre összpontosít, kizárva a böngészőket, bejárókat és a törvényes figyelő forgalmat, hogy biztosítsa a nagyon alacsony hamis pozitív arányt.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati felderítés magas kikötői sokféleséggel
- **ID:** `T1590.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Kritikusan Magas (SIEM gyilkos kategória!)
- **Leírás:** Érzékeli a hálózati felderítési tevékenységet.A SIEM-ek közötti kompatibilitásra optimalizálva szabványos mezőnevek használatával, és elkerülve az összetett CIDR-logikát az alapszabályban.

#### 🚨 Response Playbook
1. **IP hírnév: Ellenőrizd a távoli IP címet hírnév-adatbázisokban.**
2. **Forgalom elemzés: Vizsgáld meg a küldött adatmennyiséget.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Professzionális IP infrastruktúra felderítés - T1590.001
- **ID:** `T1590_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a professzionális IP-felderítési technikákat azáltal, hogy a felderítés-specifikus parancs argumentumokra és a külső IP-keresési szolgáltatásokra összpontosít, miközben kiszűri a szabványos Windows hálózati zajokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**


---
## Advanced DNS Infrastructure Reconnaissance – T1590.002
- **ID:** `T1590_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [DNSCMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szisztematikus DNS-felderítést.Csökkenti a hamis pozitívumot azáltal, hogy kiszűri a legitim egygépes lekérdezéseket, és az egész infrastruktúrára kiterjedő számlálási kísérletekre összpontosít, mint például a zónaátvitel vagy a konkrét rekordgyűjtés.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Network Trust Dependencies Reconnaissance – T1590.003
- **ID:** `T1590_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a hálózati bizalmi kapcsolatok és a megosztott erőforrások szisztematikus felfedezését.Minimálisra csökkenti a zajt azáltal, hogy kiszűri a szabványos GPO-vezérelt meghajtóleképezéseket, és olyan nagy szándékú felsorolási parancsokra összpontosít, mint az nltest domain bizalom és a távoli munkamenet listázás.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Certificate Information Reconnaissance – T1590.004
- **ID:** `T1590_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a digitális tanúsítványok szakmai felderítését.Azokra az interaktív parancssori eszközökre összpontosít, amelyek a metaadatok kinyerésére szolgálnak a helyi tárolókból vagy távoli szerverekről, miközben kiszűri az automatikus aláírás-ellenőrzést.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Cloud Infrastructure Reconnaissance – T1590.005
- **ID:** `T1590_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a manuális vagy gyanús felhőinfrastruktúra felsorolását.Kiszűri a legitim CI/CD-folyamatokat és az automatizált szolgáltatásfiókokat, hogy az interaktív felfedezésre összpontosítson.

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
- **Leírás:** Érzékeli az automatikus webes felderítést és az érzékeny fájlfelderítési kísérleteket.A fejlesztői környezetek szűrésével és a CLI-eszközök nagy szándékú felderítési mintáira összpontosítva minimalizálja a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Fejlett szervezeti infrastruktúra felsorolása - T1591
- **ID:** `T1591.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [LDIFDE.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szervezeti metaadatok szisztematikus gyűjtését (OU-k, csoportok, felhasználók).Az ismert adminisztrációs konzolok szűrésével, a szolgáltatásfiókok szinkronizálásával és a nem szabványos végrehajtási kontextusokra összpontosítva minimalizálja a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Haladó fizikai hely-infrastruktúra felsorolása – T1591.001
- **ID:** `T1591_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [VISIO.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a fizikai infrastruktúra adatainak szisztematikus felfedezését (alaprajzok, jelvényrendszerek).Kiszűri az általános irodai használatot (Intranet, Visio), és a CLI-alapú tömeges keresési műveletekre összpontosít, amelyek jellemzőek a fizikai behatolás vagy a társadalmi manipuláció előtti felderítésre.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Business Relationship Information Discovery – T1591.002
- **ID:** `T1591_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az üzleti kapcsolatok szisztematikus és automatizált felfedezését.Kiszűri az általános irodai termelékenységi zajokat, és a nem szabványos szülőfolyamatokból származó tömeges keresési műveletekre összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Knowledge Management Discovery – T1591.003
- **ID:** `T1591_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a belső tudásmenedzsment rendszerek szisztematikus és automatizált felfedezését.A tömeges adatkinyerési mintákat és a parancssori felderítést célozza meg, miközben kiszűri a szabványos webböngészőhasználatot és az IT-automatizálást.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú személyi információk felfedezése – T1591.004
- **ID:** `T1591_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az alkalmazottak adatainak gyanús, tömeges kinyerését az Active Directoryból.A nem szabványos LDAP-lekérdezésekre és a széles körű PowerShell-szűrőkre összpontosít, amelyek eltérnek a rutin adminisztrációs viselkedéstől.

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
- **Leírás:** Érzékeli a nagy megbízhatóságú gazdagépinformáció-felderítési tevékenységet azáltal, hogy azonosítja a felhasználói kontextusból rövid időn belül végrehajtott több rendszerfelderítési parancsot.Úgy hangolt, hogy minimalizálja a hamis pozitívumot a RENDSZER tevékenység, a vállalati szerszámok és az egyszeri jóindulatú parancsvégrehajtások kizárásával.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Magas megbízhatóságú hardverfelsorolás kezelőfelületeken keresztül
- **ID:** `T1592_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy megbízhatóságú felderítési tevékenységet, amikor egy külső forrás megkísérli felsorolni a hardver jellemzőit, például a CPU-t, az architektúrát, a memóriát vagy az eszközmodellt felügyeleti vagy beágyazott rendszerinterfészeken keresztül.A szabály úgy van optimalizálva, hogy minimalizálja a hamis pozitívumot az automatizált vizsgálati viselkedésre összpontosítva.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Fejlett szoftverfelsorolási felderítés webes végpontokon keresztül
- **ID:** `T1592_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a haladó felderítési tevékenységet, amikor egy külső szereplő szisztematikusan felsorolja a telepített szoftvereket, alkalmazásneveket vagy verzióinformációkat több web-elérhető végponton keresztül, rövid idő alatt.A hamis pozitívumok minimalizálására hangolva automatizáláshoz hasonló viselkedést és ismételt vizsgálati mintákat igényel.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Magas megbízhatóságú firmware-felsorolás a hálózati eszközökkel szemben
- **ID:** `T1592_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy megbízhatóságú felderítési tevékenységet, amely a hálózati vagy beágyazott eszközök firmware- és verzióinformációit célozza meg.A szabály az eszközspecifikus felügyeleti végpontokhoz való automatikus, nem böngésző-hozzáférésre összpontosít, és a hamis pozitívumok minimalizálására van optimalizálva.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy biztonságú ügyfélkonfigurációs ujjlenyomat (felderítés)
- **ID:** `T1592_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy megbízhatóságú felderítési tevékenységet, amikor egy külső forrás ismétlődő, nem böngésző HTTP-kéréseket hajt végre vizsgáló módszerek és fejlécközpontú technikák segítségével az ügyfél- vagy infrastruktúra-konfigurációk számbavételéhez.A téves pozitívumok minimalizálására optimalizálva.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**


---
## High-Fidelity automatizált webes felderítés - T1593
- **ID:** `T1593.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a közösségi médiát és nyilvános webhelyeket célzó automatizált webkaparást és OSINT gyűjtési mintákat.A fej nélküli böngészőautomatizálásra és a speciális CLI-eszközökre összpontosít, miközben kiszűri a jogos HR- és marketingtevékenységeket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Social Media Entity Harvesting – T1593.001
- **ID:** `T1593_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a közösségi média profilok automatikus felderítését.A fej nélküli böngészőautomatizálást (Selenium/Puppeteer) és a speciális OSINT-eszközöket célozza meg, miközben kiszűri a rutin HR-toborzást és az interaktív böngészőhasználatot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity automatizált keresőmotor felderítés - T1593.002
- **ID:** `T1593_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az automatizált felderítést keresőmotorok segítségével, figyelve a fej nélküli böngészőjelzőket és a szisztematikus doppingmintákat.Kifejezetten kiszűri a jogos fejlesztői tevékenységet és az interaktív böngészőhasználatot, hogy minimalizálja a hamis pozitívumot.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Social Media Entity Harvesting – T1593.003
- **ID:** `T1593_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Fej nélküli böngészők vagy speciális OSINT-eszközök segítségével észleli az automatizált közösségimédia-felderítést.Arra összpontosít, hogy azonosítsa a szisztematikus adatlegyűjtést, miközben kizárja a legitim böngészőalapú felhasználói tevékenységet.

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
- **Leírás:** Érzékeli a nyilvános információtárak (GitHub, GitLab) automatizált felderítését.A speciális titkos szkennerekre és a tömeges API-gyűjtésre összpontosít, miközben kiszűri a szabványos fejlesztői munkafolyamatokat (git klón/lehívás) és az engedélyezett biztonsági eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú aktív szkennelés észlelése (viselkedés alapú)
- **ID:** `T1595.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy megbízhatóságú aktív vizsgálati viselkedést azáltal, hogy azonosítja az automatizált ügyfeleket, amelyek rövid időn belül szisztematikusan megvizsgálnak több érzékeny webes végpontot egy külső forrásból.Úgy tervezték, hogy minimalizálja a hamis pozitív eredményeket, kizárva a böngészőket, a megfigyelést, az állapotfelméréseket és az ismert jóindulatú szkennereket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity külső IP-blokk szkennelés észlelése
- **ID:** `T1595_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy megbízhatóságú aktív szkennelési viselkedést, amikor egyetlen külső forrás IP-címe rövid időablakon belül gyorsan megvizsgál több cél IP-címet.Az ismert szkennerek, bejárók és a felhőinfrastruktúra kizárásával optimalizálva a téves pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy biztonságú külső sebezhetőség vizsgálati tevékenység
- **ID:** `T1595_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy biztonságú sebezhetőségi vizsgálati tevékenységet az agresszív kérések viselkedésének, a felfedezési útvonalak kihasználásának, a hasznos terhelésjelzőknek és az ismert szkennereszközöknek a korrelációjával.Optimalizált, hogy minimalizálja a hamis pozitív eredményeket vállalati környezetben.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Aktív szólista vizsgálat a hitelesítési végpontok ellen
- **ID:** `T1595_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a nagy megbízhatóságú szólista-ellenőrzési tevékenységet, amikor egy külső forrás gyorsan megvizsgálja a hitelesítést vagy az adminisztrációs végpontokat változó felhasználónév-paraméterek használatával, összhangban az automatizált felderítéssel.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Open Technical Database felderítés - T1596
- **ID:** `T1596.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a CLI-eszközök szisztematikus használatát és a szkript alapú API-lekérdezéseket, amelyek olyan technikai adatbázisokra irányulnak, mint a Shodan, a Censys és a VirusTotal.A nem böngészős folyamatláncokra és az automatizált adatkinyerési mintákra összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity WHOIS adatbázis-felderítés – T1596.001
- **ID:** `T1596_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az automatizált WHOIS felderítési mintákat.A CLI-eszközökön és API-alapú szkripteken (RDAP) keresztül végzett tömeges tartományregisztrációs lekérdezésekre összpontosít, miközben kiszűri a szabványos böngészőalapú kutatásokat, a szoftverlicenceket és a rutin IT-diagnosztikát.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity automatizált keresőmotor Dorking - T1596.002
- **ID:** `T1596_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a keresőmotorok dorkjainak és a tömeges műszaki adatgyűjtéshez tervezett speciális CLI-eszközök automatizált használatát.Kiszűri az interaktív böngészőkereséseket és a jogszerű IDE által kiváltott hibakereséseket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity passzív DNS-felderítés – T1597.003
- **ID:** `T1596_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Passzív DNS (pDNS) adatbázisok segítségével észleli az automatikus felderítést.A nem szabványos folyamatláncokra és a CLI-alapú API interakciókra összpontosít, amelyek a technikai OSINT adattárakat célozzák meg, miközben kiszűri a rutin hálózati hibaelhárítást és a böngésző alapú kutatásokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity digitális tanúsítvány felderítés - T1596.004
- **ID:** `T1596_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az automatikus felderítési célzású digitális tanúsítványokat és CT-naplókat.A programozott CLI-mintákra (API-alapú scraping) összpontosít, miközben kiszűri a legitim rendszerszintű tanúsítvány-érvényesítést és a böngészőforgalmat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity IP infrastruktúra felderítés - T1596.005
- **ID:** `T1596_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az IP-cím metaadatainak automatikus felderítését.A speciális OSINT-eszközökre (Shodan, GreyNoise, Censys) és a CLI-alapú API-gyűjtésre összpontosít, miközben kiszűri a rutin hálózati hibaelhárítást, a böngészőforgalmat és az EDR-zajt.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity áldozat tulajdonában lévő webhely-felderítés - T1597
- **ID:** `T1597.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szervezet tulajdonában lévő webes infrastruktúra automatizált és szisztematikus felderítését.A tömeges adatkinyerésre, a rekurzív címtár-erőszakolásra és az érzékeny konfigurációs fájlok felfedezésére összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Domain Infrastructure Enumeration – T1597.001
- **ID:** `T1597_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a fejlett és automatizált domain/DNS-felderítést.A szokatlan DNS-lekérdezéstípusokra (AXFR, ANY) és a professzionális aldomain-felderítő eszközökre összpontosít, miközben kiszűri a rutin hálózati hibaelhárítást.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity titkos vadászat kódtárolókban - T1597.002
- **ID:** `T1597_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a professzionális titokkereső eszközöket és a kézi felderítési mintákat a kódtárolókban.A mélyreható előzmények elemzésére (diff-keresés) és az automatikus hitelesítő adatok kinyerésére összpontosít, miközben kiszűri a szabványos fejlesztési ciklusokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Speciális adathalászat információk és hitelesítő adatok begyűjtése céljából – T1598
- **ID:** `T1598.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az adathalászat utáni hitelesítő adatok begyűjtését és a munkamenet-token ellopását.Azokra a nem böngészőfolyamatokra összpontosít, amelyek hozzáférnek a böngészőprofil adataihoz és a gyanús interaktív hitelesítő adatkérésekhez.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Advanced Spearphishing Link átirányítás – T1598.001
- **ID:** `T1598_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a hatékonyságnövelő alkalmazásokból származó gyanús URL-végrehajtási mintákat.A közvetett böngészőindításokra (cmd/powershell-en keresztül) és az OAuth-specifikus hitelesítő adatok begyűjtési paramétereire összpontosít, miközben kiszűri az ismert SSO-szolgáltatókat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Speciális BEC levelezési és pénzügyi adatok kiszűrése – T1598.002
- **ID:** `T1598_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús parancssori hozzáférést a levélarchívumokhoz és a pénzügyi dokumentumokhoz, amelyek általában a BEC-kampányokat célozzák.Kiszűri a jogos Outlook indexelést, a OneDrive szinkronizálást és a rendszerszintű biztonsági mentéseket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity MFA/OTP hamisítás és betakarítás – T1598.003
- **ID:** `T1598_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Észleli a csalárd MFA/OTP bemeneti promptok létrehozását a szokatlan PowerShell UI osztálybetöltés és a konkrét CLI kulcsszavak figyelésével.Kiszűri a gyakori IT-automatizálási és szoftvertelepítési zajokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Spearphishing Attachment Interaction – T1598.004
- **ID:** `T1598_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús végrehajtási mintákat az e-mail mellékletekből.A HTML-csempészetre és az Office-szkriptek közötti átmenetekre összpontosít, miközben kiszűri a legitim SharePoint-, OneDrive- és vállalati szoftverfrissítési zajokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati határok áthidalása (T1599)
- **ID:** `T1599.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a jogosulatlan hálózati határáthidalást, beleértve a kézi létrehozást is
"Bármilyen belső" NAT-szabályok, érzékeny szolgáltatások port-továbbítása és
izolált interfészek hardver szintű áthidalása.Nem megbízható forrásokra összpontosít
és a kézi munkamenet-tevékenység, miközben kiszűri a legitim felügyeleti és VPN-műveleteket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Logikai leválasztás bypass (T1599.001)
- **ID:** `T1599_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a jogosulatlan logikai hálózatleválasztási megkerülési kísérleteket, beleértve a VRF útvonal kiszivárgását,
jogosulatlan VLAN trönkölés, L2 híd létrehozása és az EVPN hibás konfigurálása
áthidalják a biztonságos zónákat vagy a bypass szegmentációs vezérlőket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyengítési kísérlet (T1600)
- **ID:** `T1600.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Közepes (Mérsékelt zajszint)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rendszer titkosításának gyengítésére irányuló jogosulatlan kísérleteket, beleértve a TLS protokoll leminősítését
és a PowerShell-tanúsítvány érvényesítésének megkerülése.A rendszeren kívüli folyamatokra összpontosít és
gyanús helyeket, miközben kizárja a megbízható telepítőket és a böngészőfrissítéseket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendszerkép javítás (T1600.001)
- **ID:** `T1600_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rendszerkép integritásának veszélyeztetésére irányuló kísérleteket a Driver Signature Enforcement (DSE) megkerülésével,
a rendszerindítási konfigurációs adatok (BCD) módosítása vagy a kritikus rendszerbináris fájlok (CI.dll, NTOSKRNL.exe, LSASRV.dll, Winload.efi) javítása.
A nem megbízható folyamatokra összpontosít, és kizárja a szabványos rendszerfelügyeleti eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Entitásellenőrzés letiltása (T1600.002)
- **ID:** `T1600_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan kísérleteket a rendszer megbízhatóságának ellenőrzésének megkerülésére,
tanúsítvány érvényesítése és Authenticode/WinTrust ellenőrzések.-ra összpontosít
gyanús certutil-használat és rendszerleíró adatbázis-alapú házirend-módosítások
nem megbízható folyamatok hajtják végre.Kizárással minimalizálja a hamis pozitívumot
ismert IT menedzsment eszközök és aláírt szoftverfrissítők.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati operációs rendszer képmódosítása (T1601)
- **ID:** `T1601.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Érzékeli a hálózati eszközök operációs rendszer képeinek jogosulatlan módosítását vagy cseréjét.
Figyeli a bináris feltöltéseket nem biztonságos protokollokon (TFTP/FTP), firmware-frissítési parancsokon,
és a megbízható felügyeleti ablakokon vagy gazdagépeken kívül végrehajtott rendszerindítási rendszer felülírásai.
A rendellenes forráskontextus, az ellenőrzőösszeg-hibák és a nem szabványos gazdagépek észlelésére összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati bináris javítás (T1601.001)
- **ID:** `T1601_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Figyeléssel észleli a hálózati operációs rendszer bináris fájljainak jogosulatlan alacsony szintű javítását
fájlrendszer újracsatlakoztatásához (írás-olvasás), közvetlen bináris manipulációhoz (dd, xxd),
és a kernelmodul betöltése (insmod) az engedélyezett karbantartási ablakokon kívül.
A kritikus útvonalakra összpontosít, és kiszűri a jogos karbantartási és írásvédett műveleteket.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity rosszindulatú hálózati operációs rendszer frissítése (T1601.002)
- **ID:** `T1601_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** A frissítés korrelációjával észleli a jogosulatlan vagy rosszindulatú hálózati operációs rendszer frissítéseket
parancsok nem biztonságos protokollokkal, nem megbízható forrásokkal vagy kriptográfiai aláírási hibákkal.
A FortiOS naplókra összpontosít, de más hálózati eszközökhöz is illeszthető.Kiszűri
megbízható források és biztonságos csatornák a téves pozitívumok csökkentése érdekében.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Hálózati megosztás automatizált adatgyűjtés (T1602)
- **ID:** `T1602.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az érzékeny adatok nagyon gyanús, automatizált gyűjtését a hálózati megosztásokról.
Az UNC-útvonal bejárására, az érzékeny fájlkiterjesztésekre, a rekurzív másolási logikára és a
nem megbízható folyamatvonal.Szűri a jogszerű IT-kezelési, biztonsági mentési és rendszerfolyamatokat
a hamis pozitívumok csökkentésére.

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
- **Leírás:** Az adminisztratív megosztásokon keresztül észleli az adatok szakaszolásának és kiszűrésének nagy pontosságú mutatóit
(C$, ADMIN$, IPC$, print$).A rendellenes folyamatvonalakra összpontosít (webszerverek, héjak),
rekurzív felfedezés és nagy értékű fájlcélzás archiválási vagy átviteli eszközökkel kombinálva.
Szűri a jogos biztonsági mentési, áttelepítési és IT-automatizálási eszközöket, hogy csökkentse a hamis pozitívumot.

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
- **Leírás:** Érzékeli a tömeges adatgyűjtést és a felhőalapú tárolás szinkronizálási gyökereiből való kiszűrést
(OneDrive, SharePoint, Google Drive, Dropbox) a rekurzív másolás figyelésével,
archiválási és rendezési tevékenység a gyanús szülői folyamatokból.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity webes token és hitelesítő adatok hamisítása (T1606)
- **ID:** `T1606.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a webes hitelesítő adatok jogosulatlan hamisítását vagy ellopását, beleértve
SAML, OAuth és böngészőben tárolt tokenek/cookie-k.
A DPAPI főkulcsokhoz hozzáférő nem böngésző folyamatokra összpontosít, gyanús
adatbázis-lekérdezések jogkivonat-tárolókban, és Golden SAML műtermékek generálása.
Szűri a legális böngészőket, az Electron alkalmazásokat és az adminisztratív automatizálási eszközöket.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity webes cookie-k és böngésző hitelesítő adatok begyűjtése (T1606.001)
- **ID:** `T1606_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a böngésző cookie-jainak és titkosítási kulcsainak jogosulatlan kimásolását
(Chromium Local State AES kulcsok / DPAPI-védett hitelesítő adatok).
A gyanús fájlhozzáférésre, az SQLite dömpingre, a DPAPI visszafejtési mintákra összpontosít,
és végrehajtás nem megbízható vagy ideiglenes helyekről.
Szűri a böngésző, az Electron és a biztonsági eszközök szabályszerű viselkedését.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity webes token hamisítás és Golden SAML (T1606.002)
- **ID:** `T1606_002.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a jogosulatlan webes token-hamisítási tevékenységeket (Golden SAML / OAuth token visszaélés)
az AD FS-konfiguráció kibontásával, a tanúsítvánnyal való visszaélés aláírásával,
DPAPI főkulcs-hozzáférés és felhőjogkivonat-manipulációs keretrendszerek végrehajtva
legitim Identity Provider szolgáltatási környezeten kívül.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendellenes infrastruktúra szakaszolás és erőforrás-kihelyezés
- **ID:** `T1608.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a felhőalapú CLI-eszközök és az IaC-binárisok használatát az ellenséges erőforrások elhelyezésére.
A nem szabványos felhasználókra összpontosít, akik feltöltést vagy infrastruktúra-módosítást végeznek
műveletek, engedélyezett CI/CD csővezetékek kiszűrése és IT adminisztráció.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendellenes rosszindulatú programok áthelyezése a külső infrastruktúrába
- **ID:** `T1608_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Felügyelet segítségével észleli a rosszindulatú programok külső infrastruktúrára történő átmeneti állapotát
nem böngésző alapú feltöltés felhőalapú tárolási, fájlmegosztó és kódtárhelyre
parancssori eszközök vagy szokatlan folyamatok használatával.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendellenes támadóeszköz-beállítás és külső feltöltés
- **ID:** `T1608_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Felügyelet segítségével észleli a támadó eszközök külső infrastruktúrára történő áthelyezését
CLI-alapú feltöltések nem szabványos könyvtárakból.A „szerveződött, majd szállított”-ra összpontosít
minta, ahol a hacktools külső zónákba kerül.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Stratégiai digitális tanúsítvány elhelyezése a Trusted Root Store-ban
- **ID:** `T1608_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a tanúsítványok parancssori telepítését a Trusted Root tárolóba.
Az ellenfelek ezt azért teszik, hogy bizalmat alakítsanak ki a C2 infrastruktúrában, vagy hogy engedélyezzék
átlátszó SSL/TLS elfogás (MitM).

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendellenes webtartalom-módosítás a Drive-by Staging számára
- **ID:** `T1608_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Tárolás-igényes)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús módosításokat a webszerver tartalomkönyvtáraiban (web root)
nem szabványos folyamatok vagy interaktív héjak által kezdeményezett.Ez a viselkedés az
jellemző, amikor egy ellenfél elindít egy letöltési oldalt, vagy rosszindulatú szkripteket szúr be.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rosszindulatú linkcélok stratégiai állomásoztatása
- **ID:** `T1608_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Figyeléssel észleli a rosszindulatú linkcélok automatikus előkészítését
CLI-alapú interakciók URL-rövidítő API-kkal vagy felhőalapú átirányító-staging
jogosulatlan felhasználók vagy szokatlan szülői folyamatok kezdeményezték.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Rendellenes SEO-mérgezés és metaadat-stopolás
- **ID:** `T1608_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a SEO-mérgezési infrastruktúra előkészítését a figyeléssel
jogosulatlan CMS-manipuláció, automatizált tartalompörgetés és használata
ismert black-hat SEO eszközök webszervereken vagy állomásozó környezetekben.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Container interaktív shell végrehajtás
- **ID:** `T1609.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a jogosulatlan interaktív shell-hozzáférést a futó tárolókhoz
kubectl vagy docker exec.Szűri a jogos egészségügyi ellenőrzéseket és a CI/CD automatizálást
a manuális, nagy kockázatú beavatkozásokra összpontosítani.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú rosszindulatú tárolótelepítés-észlelés
- **ID:** `T1610.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a nagy kockázatú konfigurációkkal rendelkező tárolók telepítését
megkönnyíti a tartály kiszabadulását vagy fennmaradását.A kiemelt módra összpontosít,
gazdagép szintű erőforrás-megosztás és nem szabványos képforrások.

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
- **Leírás:** Érzékeli a jogosulatlan konténer-szökési kísérleteket és a gazdagép-hozzáférést.-ra összpontosít
nem szabványos privilegizált végrehajtások, veszélyes rögzítések és korlátlan biztonság
kontextusban, miközben kiszűri a legitim fürtinfrastruktúra-összetevőket.

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
- **Leírás:** Érzékeli a gyanús személyek által kezdeményezett nagy pontosságú helyi tárolókép-felépítéseket
felhasználók vagy folyamatok, a kizsákmányolás utáni képalkotásra összpontosítva és
a rendszerleíró adatbázis ellenőrzésének kijátszása.Kiszűri a megbízható CI/CD csővezetékeket és
ismert build rendszerek.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro High-Fidelity tároló és Kubernetes Discovery
- **ID:** `T1613.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a tárolók, Kubernetes-erőforrások és titkok nagy pontosságú felsorolását.
A személyazonosság önlekérdezésére (auth can-i), a titok- és konfigurációfeltárásra összpontosít,
és rendellenes folyamatvonal.Kiszűri a nagyfrekvenciás monitorozást és
rendszerszondák a téves pozitívumok csökkentésére.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity rendszer helymeghatározás és regionális Kill-Switch felfedezés
- **ID:** `T1614.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a rendszer célzott helyét és a zsarolóvírusok és rosszindulatú programok által általánosan használt területi felfedezést földrajzi célzáshoz vagy kizáráshoz (kill-switch logika).A rendszerleíró adatbázis-alapú billentyűzet-/helymeghatározásra összpontosít, és a gyanús végrehajtási kontextusokból érkező külső IP-földrajzi API-hívásokkal kombinálva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity rendszernyelv és billentyűzetkiosztás felfedezése
- **ID:** `T1614_001.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a célzott rendszernyelv és billentyűzetkiosztás felfedezését, a rosszindulatú programok „kill-switch” ellenőrzésére és a környezeti kulcsokra összpontosítva.Egyesíti a beállításjegyzék-lekérdezéseket, a CLI/PowerShell-parancsmagokat és a gyanús kimenet-átirányítást.Minimalizálja a hamis pozitívumot a szülőfolyamat, az integritási szint és a megbízható útvonal szűrése révén.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú csoportházirend-felderítés észlelése
- **ID:** `T1615.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szisztematikus csoportházirend-felderítést, beleértve a csoportházirend-objektumok jelentéseinek begyűjtését és a szabályzatok felsorolását szokatlan végrehajtási kontextusokból.Kiszűri a jogos adminisztrációs és Helpdesk tevékenységet parancssori, szülőfolyamatok és integritásszint-ellenőrzések segítségével.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú felhőalapú tárolási objektumfelderítés
- **ID:** `T1619.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a szisztematikus felhőtárhely-objektum-felderítést az AWS S3-ban, az Azure Blobs-ban és a Google Cloud Storage-ban a rekurzív listázás, a metaadat-igényes API-hívások és a rendellenes kimenet-átirányítás figyelésével.Szűri a nagy megbízhatóságú biztonsági mentési, ETL- és DevOps automatizálási fiókokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Nagy pontosságú tükröző kód betöltése és a memóriába épített összeállítás végrehajtása
- **ID:** `T1620.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a tükröző kódbetöltést és a memórián belüli összeállítás végrehajtását a memóriafoglalás végrehajtási jelzőkkel, a folyamatmemória írásaival és a .NET tükrözési összeállítás betöltési mintákkal kombinált megfigyelésével.Szűri a jogos fejlesztési és CI/CD folyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús MFA azonnali bombázás vagy hitelesítési árvíz automatizálás
- **ID:** `T1621.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges MFA-kérdések bombázását vagy hitelesítési árvíz-automatizálását PowerShell-identitásmodulok, Azure/Okta-eszközök vagy fej nélküli böngésző keretrendszerek segítségével, amelyek nem interaktív vagy rejtett kontextusban futnak.A huroklogikára összpontosít az identitás-hitelesítési eszközökkel kombinálva.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús Anti-Debug API-hozzáférés nem támogatott vagy felhasználói memóriaterületről
- **ID:** `T1622.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [VSJITDEBUGGER.EXE](https://lolbas-project.github.io/lolbas/), [WINDBG.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a lehetséges hibakereső-elkerülési technikákat azáltal, hogy azonosítja a folyamatokhoz való gyanús hozzáférést a CallTrace hibakeresési API-mintáival kombinálva, különösen, ha nem támogatott memóriarégiókból vagy nem szabványos végrehajtási útvonalakból származnak.Szűri az ismert fejlesztőeszközöket és a Windows hibajelentéseit.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús macOS LaunchAgent vagy LaunchDaemon Plist módosítás
- **ID:** `T1647.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Parancssori segédprogramok segítségével észleli a macOS LaunchAgent vagy LaunchDaemon tulajdonságlista-fájlok gyanús módosítását vagy létrehozását.A tartóssággal kapcsolatos kulcsokra és a rendellenes végrehajtási kontextusokra összpontosít, kiszűri a legitim Apple rendszerfolyamatokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity szerver nélküli funkció tartósság vagy visszaélés
- **ID:** `T1648.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)
- **Leírás:** Figyeléssel észleli az AWS Lambda funkcióinak gyanús létrehozását vagy frissítését
nem automatizált tevékenység, szokatlan forrás IP-címek és kockázatos konfigurációk.
A CI/CD csővezetékek megkerülésére összpontosít.

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús tanúsítvány és privát kulcs exportálása vagy lopási tevékenység
- **ID:** `T1649.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Észleli a digitális tanúsítványok és privát kulcsok esetleges ellopását certutil visszaélés, PowerShell-alapú kulcsexport vagy támadó eszközök (pl. Mimikatz crypto::export, Certify) révén.Az exportálási műveletekre, a privát kulcsokhoz való hozzáférésre és a gyanús kimeneti állomásozási útvonalakra összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud-fiók megszerzése és inicializálása – T1650
- **ID:** `T1650.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))
- **Leírás:** Érzékeli a felhőalapú fiókok megszerzését vagy jogosulatlan beállítását.A hitelesítő adatok konfigurálására, a profilok létrehozására és az automatikus SDK-alapú identitásgyűjtésre összpontosít, miközben kiszűri az engedélyezett DevOps automatizálást.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## High-Fidelity Cloud Administration Agent Agent Abuse
- **ID:** `T1651.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [AT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a felhőkezelési ügynökök (AWS SSM, Azure Guest Agent) által kezdeményezett rendellenes folyamatvégrehajtást.
A támadók ezeket a megbízható útvonalakat használják felderítési vagy hitelesítő adatok kiíratására
amelyek megkerülik a hagyományos hálózati peremvédelmet.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús eszközillesztő-felsorolás rendellenes kontextusból (BYOVD Recon)
- **ID:** `T1652.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [PNPUTIL.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a gyanús eszközillesztő-felderítési tevékenységet a natív Windows segédprogramok, WMI vagy PowerShell használatával rendellenes végrehajtási környezetekből.A Bring Your Own Vulnerable Driver (BYOVD) visszaélése előtt gyakran megfigyelt felderítési mintákra összpontosít.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Ultra-Pro teljesítménybeállítások kezelése (T1137.001)
- **ID:** `T1653.yaml`
- **Minőségi mutató:** `50/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟡 (medium)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a teljesítménybeállítás jogosulatlan módosításait, amelyek célja az alvás vagy az alvás megakadályozása
hibernálás.A suspicious segítségével a parancssori automatizálásra (powercfg) összpontosít
szülőfolyamatok, például a PowerShell vagy a CMD, miközben szűrik a jogos felhasználói felület alapú változtatásokat.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**


---
## Gyanús eseménynapló felsorolása rendellenes végrehajtási kontextusból
- **ID:** `T1654.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a Windows eseménynaplóinak gyanús felsorolását natív segédprogramok (wevtutil) vagy PowerShell-parancsmagok (Get-WinEvent, Get-EventLog) használatával rendellenes végrehajtási környezetekből.A naplócsatorna-felderítésre és a metaadatgyűjtésre összpontosít, amely potenciálisan a biztonsági eszközök azonosítására vagy az észlelés elkerülésére használható.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús megszemélyesítés RunAs visszaélésen vagy megtévesztő helyi fiók létrehozásán keresztül
- **ID:** `T1656.yaml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a technikai megszemélyesítési kísérleteket, beleértve a gyanús RunAs-használatot oldalirányú mozgáshoz és olyan megtévesztő helyi fiókok létrehozását, amelyek a szabványos IT-kiépítési folyamatokon kívüli vezetői vagy adminisztratív identitásokat utánoznak.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús vágólap-manipuláció és pénzügyi dokumentumokhoz való hozzáférés nem megbízható szülői folyamatból
- **ID:** `T1657.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a potenciális pénzügyi lopást vagy csalási tevékenységet, amely magában foglalja a vágólap manipulációját (pl. címcsere), a pénzügyi dokumentumokhoz való hozzáféréssel kombinálva, és amelyet gyanús szülői folyamatok (például böngészők, Office-alkalmazások vagy webes szolgáltatások) indítottak el.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Professzionális tartalom megszemélyesítése és infrastruktúra tükrözése
- **ID:** `T1659.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Magas (Erős szűrés javasolt (sok log))

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli a legitim webtartalom klónozására vagy megszemélyesítésére használt eszközöket és CLI-mintákat.
A belső portálok rekurzív tükrözésére és az adathalászat használatára összpontosít
keretrendszereket, kiszűrve a legitim fejlesztést és a böngésző alapú tevékenységet.

#### 🚨 Response Playbook
1. **Folyamat vizsgálata: Ellenőrizd a szülő folyamatot és a parancssort.**
2. **Bináris ellenőrzés: Futtasd le a fájl hash-ét VirusTotal-on.**
3. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**


---
## Gyanús hozzáférés az LSASS folyamatmemóriához (hitelesítő adatok kiürítési kísérlete)
- **ID:** `credential_dumping_lsass.yml`
- **Minőségi mutató:** `100/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Becsült zajszint:** Ismeretlen (Nincs adat)

> ⚠️ **LOLBAS Érintettség: Ez a szabály visszaélésre alkalmas gyári binárist érint:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/), [DUMP64.EXE](https://lolbas-project.github.io/lolbas/), [PROCDUMP.EXE](https://lolbas-project.github.io/lolbas/)
- **Leírás:** Érzékeli az LSASS folyamatmemóriához való gyanús hozzáférést, amely hitelesítő adatok kiíratását jelezheti (pl. Mimikatz, ProcDump, Feladatkezelő kiíratása, comsvcs.dll MiniDump vagy más memóriakiíratási technikák).

#### 🚨 Response Playbook
1. **Triage: Vizsgáld meg a nyers eseményeket a SIEM-ben.**
2. **Sürgős: Ha a gyanú beigazolódik, izoláld az érintett hostot!**

