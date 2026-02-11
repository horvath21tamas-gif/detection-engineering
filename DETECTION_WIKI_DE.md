# 🛡️ Wissensdatenbank zu Erkennungsregeln

### 📊 Erkennungstechnik-Dashboard
| Kritikalität | Stückzahl |
| :--- | :--- |
| 🔴 Critical | 359 |
| 🟠 High | 262 |
| 🟡 Medium | 7 |
| 🔵 Low | 0 |
| **Alle** | **628** |

---
## 📖 Inhaltsverzeichnis
- [Ultraprofessionelle High-Fidelity-Steganographie und Datenrekonstruktion (T1001)](#ultraprofessionelle-high-fidelity-steganographie-und-datenrekonstruktion-(t1001))
- [Ultra-Pro High-Fidelity Junk Data & Command Padding (T1001.001)](#ultra-pro-high-fidelity-junk-data-&-command-padding-(t1001001))
- [Ultra-Pro High-Fidelity-Steganographie und Datenrekonstruktion (T1001.002)](#ultra-pro-high-fidelity-steganographie-und-datenrekonstruktion-(t1001002))
- [Ultra-Pro High-Fidelity-Protokoll-Imitation (T1001.003)](#ultra-pro-high-fidelity-protokoll-imitation-(t1001003))
- [Ultra-Pro High-Fidelity LSASS Credential Dumping (T1003)](#ultra-pro-high-fidelity-lsass-credential-dumping-(t1003))
- [Verdächtiger Zugriff auf den LSASS-Prozessspeicher](#verdächtiger-zugriff-auf-den-lsass-prozessspeicher)
- [Ultra-Pro High-Fidelity SAM & SYSTEM-Registrierungsdiebstahl (T1003.002)](#ultra-pro-high-fidelity-sam-&-system-registrierungsdiebstahl-(t1003002))
- [Ultra-Pro High-Fidelity NTDS.dit-Extraktion (T1003.003)](#ultra-pro-high-fidelity-ntdsdit-extraktion-(t1003003))
- [Ultra-Pro High-Fidelity LSA Secrets & Security Hive Theft (T1003.004)](#ultra-pro-high-fidelity-lsa-secrets-&-security-hive-theft-(t1003004))
- [Ultra-Pro High-Fidelity MSCASH/DCC-Extraktion (T1003.005)](#ultra-pro-high-fidelity-mscashdcc-extraktion-(t1003005))
- [Ultra-Pro High-Fidelity DCSync-Angriffserkennung (T1003.006)](#ultra-pro-high-fidelity-dcsync-angriffserkennung-(t1003006))
- [Ultra-Pro High-Fidelity LSASS Memory Dump & LOLBin-Missbrauch (T1003.007)](#ultra-pro-high-fidelity-lsass-memory-dump-&-lolbin-missbrauch-(t1003007))
- [Ultra-Pro High-Fidelity-Linux-Schattendateiextraktion (T1003.008)](#ultra-pro-high-fidelity-linux-schattendateiextraktion-(t1003008))
- [Ultraprofessionelle lokale Datenerfassung mit hoher Wiedergabetreue (T1005)](#ultraprofessionelle-lokale-datenerfassung-mit-hoher-wiedergabetreue-(t1005))
- [Ultra-Pro Stealthy Direct Volume Access (T1006)](#ultra-pro-stealthy-direct-volume-access-(t1006))
- [Ultra-Pro High-Fidelity System Service Discovery (T1007)](#ultra-pro-high-fidelity-system-service-discovery-(t1007))
- [Ultraprofessionelle High-Fidelity-Fallback-Kanalerkennung (T1008)](#ultraprofessionelle-high-fidelity-fallback-kanalerkennung-(t1008))
- [Ultra-Pro High-Fidelity-Anwendungsfenstererkennung (T1010)](#ultra-pro-high-fidelity-anwendungsfenstererkennung-(t1010))
- [Ultra-Pro High-Fidelity-Bluetooth-Exfiltration (T1011)](#ultra-pro-high-fidelity-bluetooth-exfiltration-(t1011))
- [Ultra-Pro High-Fidelity BLE-Werbe-Exfiltration (T1011.001)](#ultra-pro-high-fidelity-ble-werbe-exfiltration-(t1011001))
- [Ultra-Pro High-Fidelity Query Registry Discovery (T1012)](#ultra-pro-high-fidelity-query-registry-discovery-(t1012))
- [Laden von Ultra-Pro High-Fidelity BYOVD-Rootkits (T1014)](#laden-von-ultra-pro-high-fidelity-byovd-rootkits-(t1014))
- [Ultra-Pro High-Fidelity-System-Netzwerkkonfigurationserkennung (T1016)](#ultra-pro-high-fidelity-system-netzwerkkonfigurationserkennung-(t1016))
- [Ultraprofessionelle High-Fidelity-Internet-IP-Erkennung (T1016.001)](#ultraprofessionelle-high-fidelity-internet-ip-erkennung-(t1016001))
- [Ultra-Pro High-Fidelity Terminal Services Configuration Discovery (T1016.002)](#ultra-pro-high-fidelity-terminal-services-configuration-discovery-(t1016002))
- [Ultra-Pro High-Fidelity Remote System Discovery (T1018)](#ultra-pro-high-fidelity-remote-system-discovery-(t1018))
- [Ultra-Pro High-Fidelity Automatisierte Exfiltration (T1020)](#ultra-pro-high-fidelity-automatisierte-exfiltration-(t1020))
- [Ultra-Pro High-Fidelity Client-Linked Cloud Exfil (T1020.001)](#ultra-pro-high-fidelity-client-linked-cloud-exfil-(t1020001))
- [Schnelle Anmeldungen desselben Benutzers an mehreren entfernten Hosts](#schnelle-anmeldungen-desselben-benutzers-an-mehreren-entfernten-hosts)
- [Verdächtige RDP-Anmeldung aus ungewöhnlicher Quelle](#verdächtige-rdp-anmeldung-aus-ungewöhnlicher-quelle)
- [Ultra-Pro High-Fidelity-KMU-Admin-Freigabezuordnung (T1021.002)](#ultra-pro-high-fidelity-kmu-admin-freigabezuordnung-(t1021002))
- [Ultra-Pro High-Fidelity DCOM Remote Execution (T1021.003)](#ultra-pro-high-fidelity-dcom-remote-execution-(t1021003))
- [Ultra-Pro High-Fidelity SSH Lateral Movement & Tunneling (T1021.004)](#ultra-pro-high-fidelity-ssh-lateral-movement-&-tunneling-(t1021004))
- [Ultra-Pro High-Fidelity VNC Lateral Movement & Hijacking (T1021.005)](#ultra-pro-high-fidelity-vnc-lateral-movement-&-hijacking-(t1021005))
- [Ultra-Pro High-Fidelity WinRM Remote Execution (T1021.006)](#ultra-pro-high-fidelity-winrm-remote-execution-(t1021006))
- [Ultra-Pro High-Fidelity Cloud Control Plane Hijacking (T1021.007)](#ultra-pro-high-fidelity-cloud-control-plane-hijacking-(t1021007))
- [Ultra-Pro High-Fidelity macOS ARD Remote Hijacking (T1021.008)](#ultra-pro-high-fidelity-macos-ard-remote-hijacking-(t1021008))
- [Ultra-Pro High-Fidelity-Wechselmedien-Datendiebstahl (T1025)](#ultra-pro-high-fidelity-wechselmedien-datendiebstahl-(t1025))
- [Verdächtiger Base64-codierter PowerShell-Befehl mit Netzwerkaktivität](#verdächtiger-base64-codierter-powershell-befehl-mit-netzwerkaktivität)
- [Ultra-Pro High-Fidelity Binary Padding-Aktivität (T1027.001)](#ultra-pro-high-fidelity-binary-padding-aktivität-(t1027001))
- [Ultra-Pro High-Fidelity-Software-Verpackungsveranstaltung (T1027.002)](#ultra-pro-high-fidelity-software-verpackungsveranstaltung-(t1027002))
- [Ultra-Pro High-Fidelity-Steganographie-Nutzlastextraktion (T1027.003)](#ultra-pro-high-fidelity-steganographie-nutzlastextraktion-(t1027003))
- [Ultra-Pro High-Fidelity-Steganographie-Nutzlastextraktion (T1027.004)](#ultra-pro-high-fidelity-steganographie-nutzlastextraktion-(t1027004))
- [Ultra-Pro High-Fidelity-Indikatorentfernung und Signaturdiebstahl (T1027.005)](#ultra-pro-high-fidelity-indikatorentfernung-und-signaturdiebstahl-(t1027005))
- [Ultraprofessionelle High-Fidelity-HTML-Schmuggelausführung (T1027.006)](#ultraprofessionelle-high-fidelity-html-schmuggelausführung-(t1027006))
- [Ultra-Pro High-Fidelity-Binärsymbol-Stripping (T1027.007)](#ultra-pro-high-fidelity-binärsymbol-stripping-(t1027007))
- [Ultra-Pro High-Fidelity-Binärsymbol-Stripping (T1027.008)](#ultra-pro-high-fidelity-binärsymbol-stripping-(t1027008))
- [Ultra-Pro High-Fidelity Embedded Payload Extraction (T1027.009)](#ultra-pro-high-fidelity-embedded-payload-extraction-(t1027009))
- [Ultra-Pro High-Fidelity-Befehlszeilenverschleierung (T1027.010)](#ultra-pro-high-fidelity-befehlszeilenverschleierung-(t1027010))
- [Ultra-Pro High-Fidelity-Erstellung verdächtiger Archive (T1027.011)](#ultra-pro-high-fidelity-erstellung-verdächtiger-archive-(t1027011))
- [Ultra-Pro High-Fidelity Windows LDR Hijacking (T1027.012)](#ultra-pro-high-fidelity-windows-ldr-hijacking-(t1027012))
- [Geplante Ultra-Pro High-Fidelity-Übertragung (T1029)](#geplante-ultra-pro-high-fidelity-übertragung-(t1029))
- [Ultra-Pro High-Fidelity-Daten-Chunking und -Fragmentierung (T1030)](#ultra-pro-high-fidelity-daten-chunking-und--fragmentierung-(t1030))
- [Besitzer-/Benutzererkennung für Ultra-Pro-High-Fidelity-Systeme (T1033)](#besitzer-benutzererkennung-für-ultra-pro-high-fidelity-systeme-(t1033))
- [Ultra-Pro High-Fidelity-Masquerading und Prozesspfadmissbrauch (T1036)](#ultra-pro-high-fidelity-masquerading-und-prozesspfadmissbrauch-(t1036))
- [Ultra-Pro High-Fidelity ungültige oder gefälschte Code-Signatur (T1036.001)](#ultra-pro-high-fidelity-ungültige-oder-gefälschte-code-signatur-(t1036001))
- [Ultra-Pro High-Fidelity RTLO-Charakterausführung (T1036.002)](#ultra-pro-high-fidelity-rtlo-charakterausführung-(t1036002))
- [Ultra-Pro High-Fidelity umbenanntes System-Dienstprogramm (T1036.003)](#ultra-pro-high-fidelity-umbenanntes-system-dienstprogramm-(t1036003))
- [Ultra-Pro High-Fidelity Masquerading über Path Anomaly (T1036.004)](#ultra-pro-high-fidelity-masquerading-über-path-anomaly-(t1036004))
- [Legitime Windows-Binärdatei an einen vom Benutzer beschreibbaren Speicherort kopiert](#legitime-windows-binärdatei-an-einen-vom-benutzer-beschreibbaren-speicherort-kopiert)
- [Ultra-Pro High-Fidelity-Speicherplatz nach Dateinamenmaskierung (T1036.006)](#ultra-pro-high-fidelity-speicherplatz-nach-dateinamenmaskierung-(t1036006))
- [Ultra-Pro High-Fidelity-Doppeldateierweiterungsausführung (T1036.007)](#ultra-pro-high-fidelity-doppeldateierweiterungsausführung-(t1036007))
- [Ultra-Pro High-Fidelity-Masquerade-Dateityp durch Interpreter-Missbrauch (T1036.008)](#ultra-pro-high-fidelity-masquerade-dateityp-durch-interpreter-missbrauch-(t1036008))
- [Ultra-Pro High-Fidelity Allure Document und RTLO Masquerading (T1036.009)](#ultra-pro-high-fidelity-allure-document-und-rtlo-masquerading-(t1036009))
- [Persistenz des High-Fidelity-Anmeldeskripts (T1037)](#persistenz-des-high-fidelity-anmeldeskripts-(t1037))
- [High-Fidelity UserInitMprLogonScript-Persistenz](#high-fidelity-userinitmprlogonscript-persistenz)
- [High-Fidelity-Netsh-Helper-DLL-Persistenz](#high-fidelity-netsh-helper-dll-persistenz)
- [Ultra-Pro-Netzwerk-Anmeldeskript/Verknüpfungsänderung (T1037.003)](#ultra-pro-netzwerk-anmeldeskriptverknüpfungsänderung-(t1037003))
- [Ultra-Pro RC-Skript und Init.d-Persistenz (T1037.004)](#ultra-pro-rc-skript-und-initd-persistenz-(t1037004))
- [Persistenz von Ultra-Pro macOS-Startelementen (T1037.005)](#persistenz-von-ultra-pro-macos-startelementen-(t1037005))
- [Ultra-Pro High-Fidelity Network Share Discovery (T1039)](#ultra-pro-high-fidelity-network-share-discovery-(t1039))
- [Ultraprofessionelle High-Fidelity-Netzwerk-Sniffing-Erkennung (T1040)](#ultraprofessionelle-high-fidelity-netzwerk-sniffing-erkennung-(t1040))
- [Ultra-Pro High-Fidelity-Exfiltration über C2-Kanal (T1041)](#ultra-pro-high-fidelity-exfiltration-über-c2-kanal-(t1041))
- [Ultra-Pro High-Fidelity-Netzwerkdiensterkennung (T1046)](#ultra-pro-high-fidelity-netzwerkdiensterkennung-(t1046))
- [Verdächtige Remote-Prozesserstellung über WMIC](#verdächtige-remote-prozesserstellung-über-wmic)
- [Ultra-Pro High-Fidelity Alternative Protocol Exfiltration (T1048)](#ultra-pro-high-fidelity-alternative-protocol-exfiltration-(t1048))
- [Ultra-Pro High-Fidelity Symmetric Encrypted Exfiltration (T1048.001)](#ultra-pro-high-fidelity-symmetric-encrypted-exfiltration-(t1048001))
- [Ultra-Pro High-Fidelity Asymmetrische verschlüsselte Exfiltration (T1048.002)](#ultra-pro-high-fidelity-asymmetrische-verschlüsselte-exfiltration-(t1048002))
- [Ultra-Pro High-Fidelity unverschlüsseltes Protokoll Exfil (T1048.003)](#ultra-pro-high-fidelity-unverschlüsseltes-protokoll-exfil-(t1048003))
- [Ultra-Pro High-Fidelity-System-Netzwerkverbindungserkennung (T1049)](#ultra-pro-high-fidelity-system-netzwerkverbindungserkennung-(t1049))
- [Ultra-Pro High-Fidelity-Physical-Medium-Exfiltration (T1052)](#ultra-pro-high-fidelity-physical-medium-exfiltration-(t1052))
- [Ultra-Pro High-Fidelity USB-Exfiltration (T1052.001)](#ultra-pro-high-fidelity-usb-exfiltration-(t1052001))
- [Verdächtige geplante Aufgaben- oder Joberstellung aufgrund von Persistenz (T1053).](#verdächtige-geplante-aufgaben--oder-joberstellung-aufgrund-von-persistenz-(t1053))
- [Hochpräzise At.exe-Aktivitätserkennung](#hochpräzise-atexe-aktivitätserkennung)
- [High-Fidelity-Cron-Persistenz und In-Place-Änderung](#high-fidelity-cron-persistenz-und-in-place-änderung)
- [Verdächtige geplante Aufgabenerstellung beim Ausführen von PowerShell](#verdächtige-geplante-aufgabenerstellung-beim-ausführen-von-powershell)
- [Erstellung oder Änderung eines High-Fidelity-Systemd-Dienstes](#erstellung-oder-änderung-eines-high-fidelity-systemd-dienstes)
- [High-Fidelity-Systemd-Timer-Persistenzerkennung](#high-fidelity-systemd-timer-persistenzerkennung)
- [Ultra-Pro-Stealthy-Prozessinjektionserkennung (T1055)](#ultra-pro-stealthy-prozessinjektionserkennung-(t1055))
- [Ultra-Pro Stealthy DLL-Injektion (T1055.001)](#ultra-pro-stealthy-dll-injektion-(t1055001))
- [Ultra-Pro Stealthy PE-Injektion (T1055.002)](#ultra-pro-stealthy-pe-injektion-(t1055002))
- [Ultra-Pro Stealthy Thread Hijacking (T1055.003)](#ultra-pro-stealthy-thread-hijacking-(t1055003))
- [Ultra-Pro Stealthy APC-Injektion (T1055.004)](#ultra-pro-stealthy-apc-injektion-(t1055004))
- [Ultra-Pro Stealthy TLS-Injektion (T1055.005)](#ultra-pro-stealthy-tls-injektion-(t1055005))
- [Ultra-Pro Stealthy Ptrace-Injektion (T1055.008)](#ultra-pro-stealthy-ptrace-injektion-(t1055008))
- [Überschreiben des Ultra-Pro-Stealthy-Moduls (T1055.009)](#überschreiben-des-ultra-pro-stealthy-moduls-(t1055009))
- [Ultra-Pro Stealthy EWM-Injektion (T1055.011)](#ultra-pro-stealthy-ewm-injektion-(t1055011))
- [Ultra-Pro Stealthy Process Hollowing (T1055.012)](#ultra-pro-stealthy-process-hollowing-(t1055012))
- [Ultra-Pro Stealthy Process Hollowing (T1055.013)](#ultra-pro-stealthy-process-hollowing-(t1055013))
- [Ultra-Pro Stealthy Process Ghosting (T1055.014)](#ultra-pro-stealthy-process-ghosting-(t1055014))
- [Ultra-Pro Stealthy ListPlanting-Injektion (T1055.015)](#ultra-pro-stealthy-listplanting-injektion-(t1055015))
- [Ultra-Pro High-Fidelity-Eingangserfassungserkennung (T1056)](#ultra-pro-high-fidelity-eingangserfassungserkennung-(t1056))
- [Ultraprofessionelles High-Fidelity-Keylogging und Input-Hooking (T1056.001)](#ultraprofessionelles-high-fidelity-keylogging-und-input-hooking-(t1056001))
- [Ultra-Pro High-Fidelity-GUI-Eingabeerfassung (T1056.002)](#ultra-pro-high-fidelity-gui-eingabeerfassung-(t1056002))
- [Ultra-Pro High-Fidelity-Digitalzertifikat-Diebstahl (T1056.003)](#ultra-pro-high-fidelity-digitalzertifikat-diebstahl-(t1056003))
- [Verdächtiges Einbinden der Anmeldeinformations-API über Win32-Bibliotheken](#verdächtiges-einbinden-der-anmeldeinformations-api-über-win32-bibliotheken)
- [Ultra-Pro High-Fidelity-Prozesserkennung (T1057)](#ultra-pro-high-fidelity-prozesserkennung-(t1057))
- [Kontextuelle Anomalie des High-Fidelity-Scripting-Interpreters](#kontextuelle-anomalie-des-high-fidelity-scripting-interpreters)
- [Verdächtige verschlüsselte PowerShell-Befehlsausführung](#verdächtige-verschlüsselte-powershell-befehlsausführung)
- [High-Fidelity-AppleScript-Missbrauchserkennung (Osascript).](#high-fidelity-applescript-missbrauchserkennung-(osascript))
- [Erweiterte Kontextanomalie der Windows-Befehlsshell](#erweiterte-kontextanomalie-der-windows-befehlsshell)
- [High-Fidelity-Unix-Shell-Missbrauch und Reverse-Shell-Erkennung](#high-fidelity-unix-shell-missbrauch-und-reverse-shell-erkennung)
- [Hochpräzise kontextbezogene Anomalieerkennung mit VBScript](#hochpräzise-kontextbezogene-anomalieerkennung-mit-vbscript)
- [High-Fidelity-Python-Interpreter-Missbrauchserkennung](#high-fidelity-python-interpreter-missbrauchserkennung)
- [Kontextuelle Anomalie des High-Fidelity-JScript-Interpreters](#kontextuelle-anomalie-des-high-fidelity-jscript-interpreters)
- [CLI-Manipulation von High-Fidelity-Netzwerkgeräten](#cli-manipulation-von-high-fidelity-netzwerkgeräten)
- [High-Fidelity-Cloud-Shell-Ausnutzung und Datenexfiltration](#high-fidelity-cloud-shell-ausnutzung-und-datenexfiltration)
- [Verdächtiger SYSTEM-Prozess, der aus dem Benutzerkontext hervorgegangen ist](#verdächtiger-system-prozess-der-aus-dem-benutzerkontext-hervorgegangen-ist)
- [Ultra-Pro High-Fidelity-Berechtigungsgruppenerkennung (T1069)](#ultra-pro-high-fidelity-berechtigungsgruppenerkennung-(t1069))
- [Ultra-Pro High-Fidelity Local Group Discovery (T1069.001)](#ultra-pro-high-fidelity-local-group-discovery-(t1069001))
- [Ultra-Pro High-Fidelity-Domänengruppenerkennung (T1069.002)](#ultra-pro-high-fidelity-domänengruppenerkennung-(t1069002))
- [Ultra-Pro High-Fidelity Cloud Groups Discovery (T1069.003)](#ultra-pro-high-fidelity-cloud-groups-discovery-(t1069003))
- [Entfernung des Ultra-Pro High-Fidelity-Indikators auf dem Host (T1070)](#entfernung-des-ultra-pro-high-fidelity-indikators-auf-dem-host-(t1070))
- [Sicherheitsereignisprotokoll mit wevtutil.exe gelöscht](#sicherheitsereignisprotokoll-mit-wevtutilexe-gelöscht)
- [Ultra-Pro High-Fidelity-Linux-Protokolllöschung und Journalsabotage (T1070.002)](#ultra-pro-high-fidelity-linux-protokolllöschung-und-journalsabotage-(t1070002))
- [Ultra-Pro High-Fidelity-Mailbox-Datenlöschung und Regelsabotage (T1070.003)](#ultra-pro-high-fidelity-mailbox-datenlöschung-und-regelsabotage-(t1070003))
- [Ultra-Pro High-Fidelity forensische Artefakt- und Dateilöschung (T1070.004)](#ultra-pro-high-fidelity-forensische-artefakt--und-dateilöschung-(t1070004))
- [Ultra-Pro High-Fidelity-Netzwerkfreigabe und Entfernung von Anmeldeinformationen (T1070.005)](#ultra-pro-high-fidelity-netzwerkfreigabe-und-entfernung-von-anmeldeinformationen-(t1070005))
- [Ultra-Pro High-Fidelity Timestomp und MACE-Attributmanipulation (T1070.006)](#ultra-pro-high-fidelity-timestomp-und-mace-attributmanipulation-(t1070006))
- [Ultra-Pro High-Fidelity-Netzwerkverlauf und RDP-Trace-Entfernung (T1070.007)](#ultra-pro-high-fidelity-netzwerkverlauf-und-rdp-trace-entfernung-(t1070007))
- [Ultra-Pro High-Fidelity-E-Mail-Speicherung und Datenbankvernichtung (T1070.008)](#ultra-pro-high-fidelity-e-mail-speicherung-und-datenbankvernichtung-(t1070008))
- [Ultra-Pro High-Fidelity-Entfernung von Persistenzartefakten (T1070.009)](#ultra-pro-high-fidelity-entfernung-von-persistenzartefakten-(t1070009))
- [Ultra-Pro High-Fidelity-Anwendungsschicht-C2-Anomalie (T1071)](#ultra-pro-high-fidelity-anwendungsschicht-c2-anomalie-(t1071))
- [Ultra-Pro High-Fidelity HTTP/S C2-Anomalie (T1071.001)](#ultra-pro-high-fidelity-https-c2-anomalie-(t1071001))
- [Ultra-Pro High-Fidelity FTP/SFTP-Protokollanomalie (T1071.002)](#ultra-pro-high-fidelity-ftpsftp-protokollanomalie-(t1071002))
- [Anomalie des Ultra-Pro High-Fidelity-Mail-Protokolls (T1071.003)](#anomalie-des-ultra-pro-high-fidelity-mail-protokolls-(t1071003))
- [Ultraprofessionelles High-Fidelity-DNS-Tunneling und -Beaconing (T1071.004)](#ultraprofessionelles-high-fidelity-dns-tunneling-und--beaconing-(t1071004))
- [Erkennung von Missbrauch durch High-Fidelity-Softwarebereitstellungstools](#erkennung-von-missbrauch-durch-high-fidelity-softwarebereitstellungstools)
- [Ultra-Pro High-Fidelity-Daten-Staging-Anomalie (T1074)](#ultra-pro-high-fidelity-daten-staging-anomalie-(t1074))
- [Ultra-Pro High-Fidelity Local Data Staging-Anomalie (T1074.001)](#ultra-pro-high-fidelity-local-data-staging-anomalie-(t1074001))
- [Ultra-Pro High-Fidelity Remote Data Staging (T1074.002)](#ultra-pro-high-fidelity-remote-data-staging-(t1074002))
- [Anomale High-Fidelity-Anmeldung über ein gültiges Konto](#anomale-high-fidelity-anmeldung-über-ein-gültiges-konto)
- [High-Fidelity-Standard-Kontomissbrauchserkennung](#high-fidelity-standard-kontomissbrauchserkennung)
- [Anomalie der seitlichen Bewegung des High-Fidelity-Domänenkontos](#anomalie-der-seitlichen-bewegung-des-high-fidelity-domänenkontos)
- [High-Fidelity-Fernzugriffserkennung für lokale Konten](#high-fidelity-fernzugriffserkennung-für-lokale-konten)
- [Kompromittierung eines High-Fidelity-Cloud-Kontos (Entra-ID)](#kompromittierung-eines-high-fidelity-cloud-kontos-(entra-id))
- [Ultra-Pro High-Fidelity Taint Shared Content (T1080)](#ultra-pro-high-fidelity-taint-shared-content-(t1080))
- [Ultra-Pro High-Fidelity-Systeminformationserkennung (T1082)](#ultra-pro-high-fidelity-systeminformationserkennung-(t1082))
- [Ultra-Pro High-Fidelity-Datei- und Verzeichniserkennung (T1083)](#ultra-pro-high-fidelity-datei--und-verzeichniserkennung-(t1083))
- [Verdächtige Verwendung von Net User oder Net Localgroup über cmd.exe](#verdächtige-verwendung-von-net-user-oder-net-localgroup-über-cmdexe)
- [Ultra-Pro High-Fidelity Local Account Discovery (T1087.001)](#ultra-pro-high-fidelity-local-account-discovery-(t1087001))
- [Ultra-Pro High-Fidelity-Domänenkontoerkennung (T1087.002)](#ultra-pro-high-fidelity-domänenkontoerkennung-(t1087002))
- [Ultra-Pro High-Fidelity-E-Mail-Kontoerkennung (T1087.003)](#ultra-pro-high-fidelity-e-mail-kontoerkennung-(t1087003))
- [Ultra-Pro High-Fidelity-Cloud-Kontoerkennung (T1087.004)](#ultra-pro-high-fidelity-cloud-kontoerkennung-(t1087004))
- [Ultraprofessioneller High-Fidelity-Proxy und Pivot-Punkt-Erkennung (T1090)](#ultraprofessioneller-high-fidelity-proxy-und-pivot-punkt-erkennung-(t1090))
- [Ultra-Pro High-Fidelity Interner Proxy und Pivot-Erkennung (T1090.001)](#ultra-pro-high-fidelity-interner-proxy-und-pivot-erkennung-(t1090001))
- [Ultra-Profi-externer High-Fidelity-Proxy und Tunneling (T1090.002)](#ultra-profi-externer-high-fidelity-proxy-und-tunneling-(t1090002))
- [Ultra-Pro High-Fidelity-Multi-Hop-Proxy- und Tor-Erkennung (T1090.003)](#ultra-pro-high-fidelity-multi-hop-proxy--und-tor-erkennung-(t1090003))
- [Ultra-Pro High-Fidelity Domain Fronting Detection (T1090.004)](#ultra-pro-high-fidelity-domain-fronting-detection-(t1090004))
- [High-Fidelity-Prozessausführung von Wechselmedien](#high-fidelity-prozessausführung-von-wechselmedien)
- [Ultra-Pro High-Fidelity-Wechselmedien C2-Anomalie (T1071.002 / T1092)](#ultra-pro-high-fidelity-wechselmedien-c2-anomalie-(t1071002--t1092))
- [Ultra-Pro High-Fidelity Non-Application Layer C2 (T1095)](#ultra-pro-high-fidelity-non-application-layer-c2-(t1095))
- [High-Fidelity-Kontomanipulation – auf Persistenz ausgerichtet](#high-fidelity-kontomanipulation-–-auf-persistenz-ausgerichtet)
- [High-Fidelity-Entra-ID-Anwendungszugangsberechtigungszusatz](#high-fidelity-entra-id-anwendungszugangsberechtigungszusatz)
- [Berechtigungsgewährung für High-Fidelity-Exchange-Postfächer (T1098.002)](#berechtigungsgewährung-für-high-fidelity-exchange-postfächer-(t1098002))
- [Zusätzliches High-Fidelity-Entra-ID-App-Zertifikat](#zusätzliches-high-fidelity-entra-id-app-zertifikat)
- [Hochpräzise Eskalation der Azure-Rollenzuweisung](#hochpräzise-eskalation-der-azure-rollenzuweisung)
- [Persistenz der High-Fidelity-Geräteregistrierung (T1098.005)](#persistenz-der-high-fidelity-geräteregistrierung-(t1098005))
- [Ergänzung der High-Fidelity-MFA-Methode](#ergänzung-der-high-fidelity-mfa-methode)
- [Ultra-Pro High-Fidelity Web Service C2 (T1102)](#ultra-pro-high-fidelity-web-service-c2-(t1102))
- [Ultra-Pro High-Fidelity Dead Drop Resolver (T1102.001)](#ultra-pro-high-fidelity-dead-drop-resolver-(t1102001))
- [Ultra-Pro High-Fidelity Bidirektional Cloud C2 (T1102.002)](#ultra-pro-high-fidelity-bidirektional-cloud-c2-(t1102002))
- [Ultra-Pro High-Fidelity One-Way Web Service C2 (T1102.003)](#ultra-pro-high-fidelity-one-way-web-service-c2-(t1102003))
- [Ultra-Pro High-Fidelity Multi-Stage C2 (T1104)](#ultra-pro-high-fidelity-multi-stage-c2-(t1104))
- [Verdächtige Verwendung integrierter Windows-Tools zum Herunterladen von Dateien und zur Codeausführung](#verdächtige-verwendung-integrierter-windows-tools-zum-herunterladen-von-dateien-und-zur-codeausführung)
- [Missbrauch von nativen High-Fidelity-APIs über LOLBins](#missbrauch-von-nativen-high-fidelity-apis-über-lolbins)
- [Ultra-Pro High-Fidelity Brute Force & Tooling (T1110)](#ultra-pro-high-fidelity-brute-force-&-tooling-(t1110))
- [Mehrere fehlgeschlagene Anmeldeversuche für einen einzelnen Benutzer (mögliches Erraten des Passworts)](#mehrere-fehlgeschlagene-anmeldeversuche-für-einen-einzelnen-benutzer-(mögliches-erraten-des-passworts))
- [Ultra-Pro High-Fidelity-Zugangsdatenexport und -knacken (T1110.002)](#ultra-pro-high-fidelity-zugangsdatenexport-und--knacken-(t1110002))
- [Ultra-Pro High-Fidelity-Passwort-Sprühen (T1110.003)](#ultra-pro-high-fidelity-passwort-sprühen-(t1110003))
- [Ultra-Pro High-Fidelity Credential Stuffing und Combo-List-Missbrauch (T1110.004)](#ultra-pro-high-fidelity-credential-stuffing-und-combo-list-missbrauch-(t1110004))
- [Ultra-Pro High-Fidelity MFA Evasion & Session Hijacking (T1111)](#ultra-pro-high-fidelity-mfa-evasion-&-session-hijacking-(t1111))
- [Ultra-Pro High-Fidelity-Registrierungsmanipulation zur Umgehung (T1112)](#ultra-pro-high-fidelity-registrierungsmanipulation-zur-umgehung-(t1112))
- [Anomalie bei der Ultra-Pro-High-Fidelity-Bildschirmaufnahme (T1113)](#anomalie-bei-der-ultra-pro-high-fidelity-bildschirmaufnahme-(t1113))
- [Ultra-Pro-High-Fidelity-E-Mail-Ernte-Anomalie (T1114)](#ultra-pro-high-fidelity-e-mail-ernte-anomalie-(t1114))
- [Ultra-Pro High-Fidelity Local Email Harvesting-Anomalie (T1114.001)](#ultra-pro-high-fidelity-local-email-harvesting-anomalie-(t1114001))
- [Anomalie beim Remote-E-Mail-Export von Ultra-Pro High-Fidelity (T1114.002)](#anomalie-beim-remote-e-mail-export-von-ultra-pro-high-fidelity-(t1114002))
- [Ultra-Pro High-Fidelity-E-Mail-Weiterleitungsregelanomalie (T1114.003)](#ultra-pro-high-fidelity-e-mail-weiterleitungsregelanomalie-(t1114003))
- [Ultra-Pro High-Fidelity-Zwischenablage-Datenspionage (T1115)](#ultra-pro-high-fidelity-zwischenablage-datenspionage-(t1115))
- [Ultra-Pro High-Fidelity Automatisierte Sammlung (T1119)](#ultra-pro-high-fidelity-automatisierte-sammlung-(t1119))
- [Ultra-Pro High-Fidelity-Peripheriegeräteerkennung (T1120)](#ultra-pro-high-fidelity-peripheriegeräteerkennung-(t1120))
- [Ultraprofessionelle High-Fidelity-Audioaufnahme und -Spionage (T1123)](#ultraprofessionelle-high-fidelity-audioaufnahme-und--spionage-(t1123))
- [Ultra-Pro High-Fidelity-Systemzeiterkennung (T1124)](#ultra-pro-high-fidelity-systemzeiterkennung-(t1124))
- [Ultra-Pro High-Fidelity-Videoaufnahmeanomalie (T1125)](#ultra-pro-high-fidelity-videoaufnahmeanomalie-(t1125))
- [Ultra-Pro High-Fidelity Trusted Developer Utility Proxy (T1127)](#ultra-pro-high-fidelity-trusted-developer-utility-proxy-(t1127))
- [Ultra-Pro High-Fidelity MSBuild Proxy Execution (T1127.001)](#ultra-pro-high-fidelity-msbuild-proxy-execution-(t1127001))
- [Gemeinsames Laden von High-Fidelity-Modulen aus einem nicht vertrauenswürdigen Pfad](#gemeinsames-laden-von-high-fidelity-modulen-aus-einem-nicht-vertrauenswürdigen-pfad)
- [Ultraprofessionelle High-Fidelity-Datenkodierung und -Verschleierung (T1132)](#ultraprofessionelle-high-fidelity-datenkodierung-und--verschleierung-(t1132))
- [Ultra-Pro High-Fidelity-Standardkodierung und Nutzlastinjektion (T1132.001)](#ultra-pro-high-fidelity-standardkodierung-und-nutzlastinjektion-(t1132001))
- [Ultraprofessionelle, nicht standardmäßige High-Fidelity-Kodierung und XOR-Verschleierung (T1132.002)](#ultraprofessionelle-nicht-standardmäßige-high-fidelity-kodierung-und-xor-verschleierung-(t1132002))
- [Anomaler externer Remote-Service-Zugriffskontext](#anomaler-externer-remote-service-zugriffskontext)
- [Ultra-Pro-Access-Token-Manipulation und -Imitation (T1134)](#ultra-pro-access-token-manipulation-und--imitation-(t1134))
- [Ultra-Pro-Token-Imitation über LSASS-Handle-Duplizierung (T1134.001)](#ultra-pro-token-imitation-über-lsass-handle-duplizierung-(t1134001))
- [Ultra-Pro-Erstellungsprozess mit Token (T1134.002)](#ultra-pro-erstellungsprozess-mit-token-(t1134002))
- [Ultra-Pro Make-and-Imitate-Token (T1134.003)](#ultra-pro-make-and-imitate-token-(t1134003))
- [Ultra-Pro-Parent-PID-Spoofing und Prozessbaumverletzung (T1134.004)](#ultra-pro-parent-pid-spoofing-und-prozessbaumverletzung-(t1134004))
- [Ultra-Pro SID-History-Injektion und DS-Manipulation (T1134.005)](#ultra-pro-sid-history-injektion-und-ds-manipulation-(t1134005))
- [Ultra-Pro High-Fidelity Network Share Discovery (T1135)](#ultra-pro-high-fidelity-network-share-discovery-(t1135))
- [Unbefugte Ultra-Pro-Kontoerstellung (T1136)](#unbefugte-ultra-pro-kontoerstellung-(t1136))
- [Unbefugte Erstellung eines lokalen Ultra-Pro-Kontos (T1136.001)](#unbefugte-erstellung-eines-lokalen-ultra-pro-kontos-(t1136001))
- [Ultra-Pro-Erstellung eines nicht autorisierten Domänenkontos (T1136.002)](#ultra-pro-erstellung-eines-nicht-autorisierten-domänenkontos-(t1136002))
- [Unbefugte Erstellung eines Ultra-Pro-Cloud-Kontos (T1136.003)](#unbefugte-erstellung-eines-ultra-pro-cloud-kontos-(t1136003))
- [Ultra-Pro Office-Anwendungsstartpersistenz (T1137)](#ultra-pro-office-anwendungsstartpersistenz-(t1137))
- [Verdächtige Änderung der globalen Office-Vorlage (Normal.dotm)](#verdächtige-änderung-der-globalen-office-vorlage-(normaldotm))
- [Ultra-Pro Office Test-DLL-Persistenz (T1137.002)](#ultra-pro-office-test-dll-persistenz-(t1137002))
- [Persistenz benutzerdefinierter Outlook-Formulare von Ultra-Pro (T1137.003)](#persistenz-benutzerdefinierter-outlook-formulare-von-ultra-pro-(t1137003))
- [Ultra-Pro Outlook Home Page Hijacking & Bypass (T1137.004)](#ultra-pro-outlook-home-page-hijacking-&-bypass-(t1137004))
- [Manipulation von Ultra-Pro Office-Sicherheitsrichtlinien (T1137.005)](#manipulation-von-ultra-pro-office-sicherheitsrichtlinien-(t1137005))
- [Ultra-Pro Office Add-in Binäre Persistenz (T1137.006)](#ultra-pro-office-add-in-binäre-persistenz-(t1137006))
- [Ultra-Pro Stealthy Deobfuscation/Dekodierung (T1140)](#ultra-pro-stealthy-deobfuscationdekodierung-(t1140))
- [Ultra-Pro-Browsererweiterung Force-Install Persistence (T1176)](#ultra-pro-browsererweiterung-force-install-persistence-(t1176))
- [Ultra-Pro High-Fidelity-Browser-Sitzungs-Hijacking (T1185)](#ultra-pro-high-fidelity-browser-sitzungs-hijacking-(t1185))
- [Ultra-Pro High-Fidelity-Zwangsauthentifizierung (T1187)](#ultra-pro-high-fidelity-zwangsauthentifizierung-(t1187))
- [Vom Browser stammende Shell- oder Systemtool-Ausführung](#vom-browser-stammende-shell--oder-systemtool-ausführung)
- [Auf dem Webserver wurde ein verdächtiger Cross-Site-Scripting-Versuch (XSS) erkannt](#auf-dem-webserver-wurde-ein-verdächtiger-cross-site-scripting-versuch-(xss)-erkannt)
- [High-Fidelity-Erkennung von Kompromittierungen in der Lieferkette (Anomalie nach der Aktualisierung)](#high-fidelity-erkennung-von-kompromittierungen-in-der-lieferkette-(anomalie-nach-der-aktualisierung))
- [High-Fidelity-Erkennung von Abhängigkeitsvergiftungen](#high-fidelity-erkennung-von-abhängigkeitsvergiftungen)
- [Kompromittierte binäre High-Fidelity-Aktivität (nach dem Update)](#kompromittierte-binäre-high-fidelity-aktivität-(nach-dem-update))
- [Hochpräzise Hardware-/Firmware-Manipulationserkennung](#hochpräzise-hardware-firmware-manipulationserkennung)
- [Download verdächtiger Dateien über Bitsadmin (High Fidelity)](#download-verdächtiger-dateien-über-bitsadmin-(high-fidelity))
- [High-Fidelity-Missbrauchserkennung in vertrauenswürdigen Beziehungen](#high-fidelity-missbrauchserkennung-in-vertrauenswürdigen-beziehungen)
- [Schädliche hardwareinduzierte Befehlsausführung (HID-Injection)](#schädliche-hardwareinduzierte-befehlsausführung-(hid-injection))
- [Ultra-Pro High-Fidelity-Kennwortrichtlinienerkennung (T1201)](#ultra-pro-high-fidelity-kennwortrichtlinienerkennung-(t1201))
- [Ultra-Pro High-Fidelity Indirekte Befehlsausführung (T1202)](#ultra-pro-high-fidelity-indirekte-befehlsausführung-(t1202))
- [High-Fidelity-Client-seitige Ausbeutung und Shell-Spawning](#high-fidelity-client-seitige-ausbeutung-und-shell-spawning)
- [Verdächtiger untergeordneter Prozess, der von einer Microsoft Office-Anwendung erzeugt wurde (High Fidelity)](#verdächtiger-untergeordneter-prozess-der-von-einer-microsoft-office-anwendung-erzeugt-wurde-(high-fidelity))
- [High-Fidelity-Benutzerausführung eines schädlichen Links (T1204.001)](#high-fidelity-benutzerausführung-eines-schädlichen-links-(t1204001))
- [High-Fidelity-Benutzerausführung einer schädlichen Datei](#high-fidelity-benutzerausführung-einer-schädlichen-datei)
- [High-Fidelity-Ausführung von gemounteter virtueller Festplatte (T1204.003)](#high-fidelity-ausführung-von-gemounteter-virtueller-festplatte-(t1204003))
- [Phishing über einen bösartigen Link mit Domänen- und Absenderanomalien](#phishing-über-einen-bösartigen-link-mit-domänen--und-absenderanomalien)
- [Ultraprofessionelle Verkehrssignalisierung und Port-Knocking (T1205)](#ultraprofessionelle-verkehrssignalisierung-und-port-knocking-(t1205))
- [Ultra-Pro Port Knocking & Raw Socket Listener (T1205.001)](#ultra-pro-port-knocking-&-raw-socket-listener-(t1205001))
- [Ultra-Pro-Steckdosenfilter und WFP-Verkehrssignalisierung (T1205.002)](#ultra-pro-steckdosenfilter-und-wfp-verkehrssignalisierung-(t1205002))
- [Ultra-Pro High-Fidelity-Rogue-DC-Topologiemanipulation (T1207)](#ultra-pro-high-fidelity-rogue-dc-topologiemanipulation-(t1207))
- [Ultraprofessionelle High-Fidelity-Nutzung von Remote-Diensten (T1210)](#ultraprofessionelle-high-fidelity-nutzung-von-remote-diensten-(t1210))
- [Ultra-Pro High-Fidelity-Berechtigungseskalationsausnutzung (T1211)](#ultra-pro-high-fidelity-berechtigungseskalationsausnutzung-(t1211))
- [Ultra-Pro High-Fidelity Credential Service Exploitation (T1212)](#ultra-pro-high-fidelity-credential-service-exploitation-(t1212))
- [Ultra-Pro High-Fidelity-Repository-Dump (T1213)](#ultra-pro-high-fidelity-repository-dump-(t1213))
- [Ultra-Pro High-Fidelity Confluence Scraping (T1213.001)](#ultra-pro-high-fidelity-confluence-scraping-(t1213001))
- [Ultra-Pro High-Fidelity-SharePoint-Massendaten-Exfiltration (T1213.002)](#ultra-pro-high-fidelity-sharepoint-massendaten-exfiltration-(t1213002))
- [Ultra-Pro High-Fidelity Knowledge Base Scraping (T1213.003)](#ultra-pro-high-fidelity-knowledge-base-scraping-(t1213003))
- [Ultra-Pro High-Fidelity-System-Skript-Proxy-Ausführung (T1216)](#ultra-pro-high-fidelity-system-skript-proxy-ausführung-(t1216))
- [Ultra-Pro High-Fidelity-Pubprn-Skript-Proxy-Ausführung (T1216.001)](#ultra-pro-high-fidelity-pubprn-skript-proxy-ausführung-(t1216001))
- [Ultra-Pro High-Fidelity Browser Information Discovery (T1217)](#ultra-pro-high-fidelity-browser-information-discovery-(t1217))
- [Ultra-Pro High-Fidelity-System-Binär-Proxy-Ausführung (T1218)](#ultra-pro-high-fidelity-system-binär-proxy-ausführung-(t1218))
- [Ultra-Pro High-Fidelity HH.exe Proxy-Ausführung (T1218.001)](#ultra-pro-high-fidelity-hhexe-proxy-ausführung-(t1218001))
- [Ultra-Pro High-Fidelity Control.exe Proxy-Ausführung (T1218.002)](#ultra-pro-high-fidelity-controlexe-proxy-ausführung-(t1218002))
- [Ultra-Pro High-Fidelity MsiExec Proxy Execution (T1218.003)](#ultra-pro-high-fidelity-msiexec-proxy-execution-(t1218003))
- [Ultra-Pro High-Fidelity InstallUtil Proxy-Ausführung (T1218.004)](#ultra-pro-high-fidelity-installutil-proxy-ausführung-(t1218004))
- [Verdächtige Mshta-Ausführung von Remote-Skript (High Fidelity)](#verdächtige-mshta-ausführung-von-remote-skript-(high-fidelity))
- [Verdächtige Msiexec-Installation von einer Remote-URL (High Fidelity)](#verdächtige-msiexec-installation-von-einer-remote-url-(high-fidelity))
- [Ultra-Pro High-Fidelity Odbcconf Proxy Execution (T1218.008)](#ultra-pro-high-fidelity-odbcconf-proxy-execution-(t1218008))
- [Ultra-Pro High-Fidelity Regsvcs/Regasm Proxy Execution (T1218.009)](#ultra-pro-high-fidelity-regsvcsregasm-proxy-execution-(t1218009))
- [Verdächtige Regsvr32-Ausführung, die auf LOLBAS-Missbrauch hinweist (High Fidelity)](#verdächtige-regsvr32-ausführung-die-auf-lolbas-missbrauch-hinweist-(high-fidelity))
- [Verdächtige Rundll32-Ausführung mit Skript oder Remote-Payload (High Fidelity)](#verdächtige-rundll32-ausführung-mit-skript-oder-remote-payload-(high-fidelity))
- [Ultra-Pro High-Fidelity Verclsid Proxy Execution (T1218.012)](#ultra-pro-high-fidelity-verclsid-proxy-execution-(t1218012))
- [Ultra-Pro High-Fidelity Rundll32 Proxy-Ausführung (T1218.013)](#ultra-pro-high-fidelity-rundll32-proxy-ausführung-(t1218013))
- [Ultra-Pro High-Fidelity MMC Proxy Execution (T1218.014)](#ultra-pro-high-fidelity-mmc-proxy-execution-(t1218014))
- [Verdächtige Verwendung legitimer Remote-Verwaltungstools außerhalb des Unternehmensmusters](#verdächtige-verwendung-legitimer-remote-verwaltungstools-außerhalb-des-unternehmensmusters)
- [Ultraprofessionelle High-Fidelity-XSL-Skriptverarbeitung (T1220)](#ultraprofessionelle-high-fidelity-xsl-skriptverarbeitung-(t1220))
- [Ultra-Pro High-Fidelity-Office-Vorlageninjektion (T1221)](#ultra-pro-high-fidelity-office-vorlageninjektion-(t1221))
- [Änderung der Ultra-Pro High-Fidelity-Berechtigungen (T1222)](#änderung-der-ultra-pro-high-fidelity-berechtigungen-(t1222))
- [Änderung der Dateiberechtigungen für Ultra-Pro High-Fidelity Windows (T1222.001)](#änderung-der-dateiberechtigungen-für-ultra-pro-high-fidelity-windows-(t1222001))
- [Änderung der Dateiberechtigungen für Ultra-Pro High-Fidelity Linux (T1222.002)](#änderung-der-dateiberechtigungen-für-ultra-pro-high-fidelity-linux-(t1222002))
- [Ultra-Pro High-Fidelity Execution Guardrails Discovery (T1480)](#ultra-pro-high-fidelity-execution-guardrails-discovery-(t1480))
- [Ultra-Pro Environmental Keying Discovery (T1480.001)](#ultra-pro-environmental-keying-discovery-(t1480001))
- [Ultra-Pro High-Fidelity Domain Trust Discovery (T1482)](#ultra-pro-high-fidelity-domain-trust-discovery-(t1482))
- [Manipulation von Ultra-Pro-Domänenrichtlinien und GPO-Missbrauch (T1484)](#manipulation-von-ultra-pro-domänenrichtlinien-und-gpo-missbrauch-(t1484))
- [Änderung und Missbrauch der Ultra-Pro-Gruppenrichtlinien (T1484.001)](#änderung-und-missbrauch-der-ultra-pro-gruppenrichtlinien-(t1484001))
- [Ultra-Pro Domain Trust Tampering & SID Filtering Bypass (T1484.002)](#ultra-pro-domain-trust-tampering-&-sid-filtering-bypass-(t1484002))
- [Ultra-Pro High-Fidelity-Datenvernichtung (T1485)](#ultra-pro-high-fidelity-datenvernichtung-(t1485))
- [Ransomware-Vorbereitungsaktivität auf Windows-Host erkannt (High Fidelity)](#ransomware-vorbereitungsaktivität-auf-windows-host-erkannt-(high-fidelity))
- [Ultra-Pro High-Fidelity Service Stop (T1489)](#ultra-pro-high-fidelity-service-stop-(t1489))
- [Verdächtiges Löschen von Volume-Schattenkopien über VSSAdmin (High Fidelity)](#verdächtiges-löschen-von-volume-schattenkopien-über-vssadmin-(high-fidelity))
- [Ultra-Pro High-Fidelity-Verunstaltung (T1491)](#ultra-pro-high-fidelity-verunstaltung-(t1491))
- [Ultra-Pro High-Fidelity interne Verunstaltung (T1491.001)](#ultra-pro-high-fidelity-interne-verunstaltung-(t1491001))
- [Ultra-Pro High-Fidelity externe Verunstaltung (T1491.002)](#ultra-pro-high-fidelity-externe-verunstaltung-(t1491002))
- [Ultra-Pro High-Fidelity-Firmware-Beschädigung (T1495)](#ultra-pro-high-fidelity-firmware-beschädigung-(t1495))
- [Ultra-Pro High-Fidelity-Ressourcen-Hijacking (T1496)](#ultra-pro-high-fidelity-ressourcen-hijacking-(t1496))
- [Ultra-Pro High-Fidelity-Virtualisierung/Sandbox-Umgehung (T1497)](#ultra-pro-high-fidelity-virtualisierungsandbox-umgehung-(t1497))
- [Ultra-Pro High-Fidelity VM Artifact Discovery (T1497.001)](#ultra-pro-high-fidelity-vm-artifact-discovery-(t1497001))
- [Ultra-Pro High-Fidelity User Interaction Evasion (T1497.002)](#ultra-pro-high-fidelity-user-interaction-evasion-(t1497002))
- [Ultra-Pro High-Fidelity Time-based Evasion (T1497.003)](#ultra-pro-high-fidelity-time-based-evasion-(t1497003))
- [Ultra-Pro High-Fidelity-Netzwerk-DoS (T1498)](#ultra-pro-high-fidelity-netzwerk-dos-(t1498))
- [Ultra-Pro High-Fidelity Direct Flow Flood (T1498.001)](#ultra-pro-high-fidelity-direct-flow-flood-(t1498001))
- [Ultra-Pro High-Fidelity-Endpunkt-DoS (T1499)](#ultra-pro-high-fidelity-endpunkt-dos-(t1499))
- [Ultra-Pro High-Fidelity-OS-Selbstzerstörung (T1499.001)](#ultra-pro-high-fidelity-os-selbstzerstörung-(t1499001))
- [Ultra-Pro High-Fidelity-Service-Erschöpfung (T1499.002)](#ultra-pro-high-fidelity-service-erschöpfung-(t1499002))
- [Ultra-Pro High-Fidelity OS-Selbstzerstörung (T1499.003)](#ultra-pro-high-fidelity-os-selbstzerstörung-(t1499003))
- [Ultra-Pro High-Fidelity-Ressourcenerschöpfung (T1499.004)](#ultra-pro-high-fidelity-ressourcenerschöpfung-(t1499004))
- [Ultra-Pro-Web-Shell-Ausführungsmuster (T1505.003)](#ultra-pro-web-shell-ausführungsmuster-(t1505003))
- [Ultra-Pro SQL Server-Befehls-Shell-Ausführung (T1505.001)](#ultra-pro-sql-server-befehls-shell-ausführung-(t1505001))
- [Ultra-Pro IIS Native Module Injection (T1505.002)](#ultra-pro-iis-native-module-injection-(t1505002))
- [Webshell-Upload oder Interaktion auf dem Webserver erkannt (High Fidelity)](#webshell-upload-oder-interaktion-auf-dem-webserver-erkannt-(high-fidelity))
- [Ultra-Pro Mainboard-Boot-Image und SPI-Flash-Manipulation (T1542.004)](#ultra-pro-mainboard-boot-image-und-spi-flash-manipulation-(t1542004))
- [Ultra-Pro Terminal Services DLL-Hijacking (T1505.005)](#ultra-pro-terminal-services-dll-hijacking-(t1505005))
- [Ultra-Pro High-Fidelity Software Discovery (T1518)](#ultra-pro-high-fidelity-software-discovery-(t1518))
- [Ultra-Pro High-Fidelity-Sicherheitssoftware-Erkennung (T1518.001)](#ultra-pro-high-fidelity-sicherheitssoftware-erkennung-(t1518001))
- [Unautorisierte Container-Image-Ausführung mit Exploit-Grad (Implant-Container-Image)](#unautorisierte-container-image-ausführung-mit-exploit-grad-(implant-container-image))
- [Ultra-Pro High-Fidelity Cloud Service Discovery (T1526)](#ultra-pro-high-fidelity-cloud-service-discovery-(t1526))
- [Ultra-Pro High-Fidelity-Anwendungstoken und Session-Hijacking (T1528)](#ultra-pro-high-fidelity-anwendungstoken-und-session-hijacking-(t1528))
- [Herunterfahren/Neustarten des Ultra-Pro High-Fidelity-Systems (T1529)](#herunterfahrenneustarten-des-ultra-pro-high-fidelity-systems-(t1529))
- [Ultra-Pro High-Fidelity-Cloud-Speicher-Datendiebstahl (T1530)](#ultra-pro-high-fidelity-cloud-speicher-datendiebstahl-(t1530))
- [Entfernen des Ultra-Pro High-Fidelity-Kontozugriffs (T1531)](#entfernen-des-ultra-pro-high-fidelity-kontozugriffs-(t1531))
- [Ultra-Pro High-Fidelity interne Spearphishing-Erkennung (T1534)](#ultra-pro-high-fidelity-interne-spearphishing-erkennung-(t1534))
- [Ultra-Pro High-Fidelity-Manipulation ungenutzter Dienste (T1535)](#ultra-pro-high-fidelity-manipulation-ungenutzter-dienste-(t1535))
- [Ultra-Pro High-Fidelity-Cloud-Konto-Exfil (T1537)](#ultra-pro-high-fidelity-cloud-konto-exfil-(t1537))
- [Ultra-Pro High-Fidelity-Cloud-Service-Dashboard-Erkennung (T1538)](#ultra-pro-high-fidelity-cloud-service-dashboard-erkennung-(t1538))
- [Ultra-Pro High-Fidelity-Websitzungs-Cookie-Diebstahl (T1539)](#ultra-pro-high-fidelity-websitzungs-cookie-diebstahl-(t1539))
- [Ultra-Pro Pre-OS-Boot-Manipulation (T1542)](#ultra-pro-pre-os-boot-manipulation-(t1542))
- [Ultra-Pro ROM-Kit und UEFI-Firmware-Manipulation (T1542.001)](#ultra-pro-rom-kit-und-uefi-firmware-manipulation-(t1542001))
- [Manipulation der Ultra-Pro-Komponenten-Firmware (T1542.002)](#manipulation-der-ultra-pro-komponenten-firmware-(t1542002))
- [Ultra-Pro Bootkit-Persistenz und EFI-Manipulation (T1542.003)](#ultra-pro-bootkit-persistenz-und-efi-manipulation-(t1542003))
- [Ultra-Pro Mainboard-Boot-Image und SPI-Flash-Manipulation (T1542.004)](#ultra-pro-mainboard-boot-image-und-spi-flash-manipulation-(t1542004))
- [Ultra-Pro DHCP/PXE-Boot-Hijacking (T1542.005)](#ultra-pro-dhcppxe-boot-hijacking-(t1542005))
- [Benutzer ohne Administratorrechte versuchen, mehrere sensible Windows-Dienste zu stoppen oder zu ändern](#benutzer-ohne-administratorrechte-versuchen-mehrere-sensible-windows-dienste-zu-stoppen-oder-zu-ändern)
- [Ultra-Pro macOS Launch Agent-Persistenzerkennung (T1543.001)](#ultra-pro-macos-launch-agent-persistenzerkennung-(t1543001))
- [Ultra-Pro Systemd-Dienstpersistenz (T1543.002)](#ultra-pro-systemd-dienstpersistenz-(t1543002))
- [Nicht autorisierte Installation des Ultra-Pro-Windows-Dienstes (T1543.003)](#nicht-autorisierte-installation-des-ultra-pro-windows-dienstes-(t1543003))
- [Ultra-Pro Unautorisierter macOS-Startdaemon (T1543.004)](#ultra-pro-unautorisierter-macos-startdaemon-(t1543004))
- [Persistenz des Ultra-Pro WMI-Ereignisabonnements (T1546.003)](#persistenz-des-ultra-pro-wmi-ereignisabonnements-(t1546003))
- [Ultra-Pro File Association-Hijacking (T1546.001)](#ultra-pro-file-association-hijacking-(t1546001))
- [Ultra-Pro-Bildschirmschoner-Persistenzerkennung (T1546.002)](#ultra-pro-bildschirmschoner-persistenzerkennung-(t1546002))
- [Persistenz des WMI-Ereignisabonnements über WMIC oder PowerShell (High Fidelity)](#persistenz-des-wmi-ereignisabonnements-über-wmic-oder-powershell-(high-fidelity))
- [Ultra-Pro AppCert DLL-Persistenzerkennung (T1546.004)](#ultra-pro-appcert-dll-persistenzerkennung-(t1546004))
- [Ultra-Pro Persistenzerkennung für Granatenfallen (T1546.005)](#ultra-pro-persistenzerkennung-für-granatenfallen-(t1546005))
- [Ultra-Pro Mach-O LC_LOAD_DYLIB-Injektion (T1546.006)](#ultra-pro-mach-o-lc_load_dylib-injektion-(t1546006))
- [Ultra-Pro Netsh Helper DLL-Persistenz (T1546.007)](#ultra-pro-netsh-helper-dll-persistenz-(t1546007))
- [Ultra-Pro WER SilentProcessExit Persistenz (T1546.008)](#ultra-pro-wer-silentprocessexit-persistenz-(t1546008))
- [Ultra-Pro AppInit_DLLs Persistenzerkennung (T1546.009)](#ultra-pro-appinit_dlls-persistenzerkennung-(t1546009))
- [Ultra-Pro AppCert DLL-Persistenzerkennung (T1546.010)](#ultra-pro-appcert-dll-persistenzerkennung-(t1546010))
- [Ultra-Pro-Anwendungs-Shimming-Persistenzerkennung (T1546.011)](#ultra-pro-anwendungs-shimming-persistenzerkennung-(t1546011))
- [Ultra-Pro IFEO Debugger Hijacking-Erkennung (T1546.012)](#ultra-pro-ifeo-debugger-hijacking-erkennung-(t1546012))
- [Ultra-Pro PowerShell-Profilinjektionserkennung (T1546.013)](#ultra-pro-powershell-profilinjektionserkennung-(t1546013))
- [Persistenz des Ultra-Pro WMI-Ereignisabonnements (T1546.014)](#persistenz-des-ultra-pro-wmi-ereignisabonnements-(t1546014))
- [Verdächtiges COM-Hijacking zur Persistenz auf Benutzerebene (High Fidelity)](#verdächtiges-com-hijacking-zur-persistenz-auf-benutzerebene-(high-fidelity))
- [Benutzerdefinierte Aktionspersistenz des Ultra-Pro MSI-Installationsprogramms (T1546.016)](#benutzerdefinierte-aktionspersistenz-des-ultra-pro-msi-installationsprogramms-(t1546016))
- [Es wird ein verdächtiger Start- oder Anmelde-Autorun durchgeführt](#es-wird-ein-verdächtiger-start--oder-anmelde-autorun-durchgeführt)
- [Verdächtige Änderung des Registrierungsschlüssels für Benutzerpersistenz (High Fidelity)](#verdächtige-änderung-des-registrierungsschlüssels-für-benutzerpersistenz-(high-fidelity))
- [Persistenz des High-Fidelity-LSA-Authentifizierungspakets](#persistenz-des-high-fidelity-lsa-authentifizierungspakets)
- [Persistenz des High-Fidelity-Zeitanbieters (T1547.003)](#persistenz-des-high-fidelity-zeitanbieters-(t1547003))
- [High-Fidelity-Winlogon-Hilfsprogramm-DLL-Persistenz (T1547.004)](#high-fidelity-winlogon-hilfsprogramm-dll-persistenz-(t1547004))
- [High-Fidelity-SSP-DLL-Persistenz (T1547.005)](#high-fidelity-ssp-dll-persistenz-(t1547005))
- [Registrierung des High-Fidelity-Kernel-Treibers (T1547.006)](#registrierung-des-high-fidelity-kernel-treibers-(t1547006))
- [High-Fidelity-Browser-Sitzungspersistenz (T1547.007)](#high-fidelity-browser-sitzungspersistenz-(t1547007))
- [High-Fidelity-LSASS-Treiber/Paketpersistenz (T1547.008)](#high-fidelity-lsass-treiberpaketpersistenz-(t1547008))
- [High-Fidelity-Erkennung von Verknüpfungsänderungen](#high-fidelity-erkennung-von-verknüpfungsänderungen)
- [High-Fidelity AppCert DLL-Persistenz (T1547.010)](#high-fidelity-appcert-dll-persistenz-(t1547010))
- [Shimming-Persistenz für High-Fidelity-Anwendungen (T1547.011)](#shimming-persistenz-für-high-fidelity-anwendungen-(t1547011))
- [High-Fidelity-COM-Hijacking-Persistenz (T1547.012)](#high-fidelity-com-hijacking-persistenz-(t1547012))
- [High-Fidelity-E-Mail-Client-Helper-Persistenz (T1547.013)](#high-fidelity-e-mail-client-helper-persistenz-(t1547013))
- [High-Fidelity Active Setup Persistence (T1547.014)](#high-fidelity-active-setup-persistence-(t1547014))
- [High-Fidelity-COM-Hijacking-Persistenz (T1547.015)](#high-fidelity-com-hijacking-persistenz-(t1547015))
- [Ultra-Pro-Berechtigungsausweitung durch Registry-Hijacking (T1548.002)](#ultra-pro-berechtigungsausweitung-durch-registry-hijacking-(t1548002))
- [Ultra-Pro Setuid/Setgid-Bit-Manipulation (T1548.001)](#ultra-pro-setuidsetgid-bit-manipulation-(t1548001))
- [UAC-Umgehung über Fodhelper Registry Hijack (High Fidelity)](#uac-umgehung-über-fodhelper-registry-hijack-(high-fidelity))
- [Ultra-Pro-Sudo-Manipulation und Sudo-Missbrauch (T1548.003)](#ultra-pro-sudo-manipulation-und-sudo-missbrauch-(t1548003))
- [Ultra-Pro-AppleScript-Berechtigungseskalation (T1548.004)](#ultra-pro-applescript-berechtigungseskalation-(t1548004))
- [Ultra-Pro SUID-Desktop-Eintrag und Missbrauch von Verknüpfungen (T1548.005)](#ultra-pro-suid-desktop-eintrag-und-missbrauch-von-verknüpfungen-(t1548005))
- [Ultra-Pro High-Fidelity Alternatives Authentifizierungsmaterial (T1550)](#ultra-pro-high-fidelity-alternatives-authentifizierungsmaterial-(t1550))
- [Missbrauch von Ultra-Pro High-Fidelity-Anwendungszugriffstoken (T1550.001)](#missbrauch-von-ultra-pro-high-fidelity-anwendungszugriffstoken-(t1550001))
- [Ultra-Pro High-Fidelity Pass-the-Hash-Erkennung (T1550.002)](#ultra-pro-high-fidelity-pass-the-hash-erkennung-(t1550002))
- [Ultraprofessionelle High-Fidelity-Pass-the-Ticket-Erkennung (T1550.003)](#ultraprofessionelle-high-fidelity-pass-the-ticket-erkennung-(t1550003))
- [Ultra-Pro High-Fidelity Pass-the-Session-Erkennung (T1550.004)](#ultra-pro-high-fidelity-pass-the-session-erkennung-(t1550004))
- [Ultra-Pro High-Fidelity-Erkennung ungesicherter Anmeldeinformationen (T1552)](#ultra-pro-high-fidelity-erkennung-ungesicherter-anmeldeinformationen-(t1552))
- [Ultra-Pro High-Fidelity-Anmeldeinformationen bei der Dateierkennung (T1552.001)](#ultra-pro-high-fidelity-anmeldeinformationen-bei-der-dateierkennung-(t1552001))
- [Ultra-Pro High-Fidelity-Anmeldeinformationen bei der Registrierungserkennung (T1552.002)](#ultra-pro-high-fidelity-anmeldeinformationen-bei-der-registrierungserkennung-(t1552002))
- [Ultra-Pro High-Fidelity Shell-Verlauf und Konsolenerkennung (T1552.003)](#ultra-pro-high-fidelity-shell-verlauf-und-konsolenerkennung-(t1552003))
- [Ultra-Pro High-Fidelity Private Key Discovery (T1552.004)](#ultra-pro-high-fidelity-private-key-discovery-(t1552004))
- [Ultra-Pro High-Fidelity Cloud Credential Discovery (T1552.005)](#ultra-pro-high-fidelity-cloud-credential-discovery-(t1552005))
- [Ultra-Pro High-Fidelity-GPP-Passworterkennung (T1552.006)](#ultra-pro-high-fidelity-gpp-passworterkennung-(t1552006))
- [Ultra-Pro High-Fidelity Container Secret Discovery (T1552.007)](#ultra-pro-high-fidelity-container-secret-discovery-(t1552007))
- [Ultra-Pro High-Fidelity-GPP-Passworterkennung (T1552.008)](#ultra-pro-high-fidelity-gpp-passworterkennung-(t1552008))
- [Ultra-Pro High-Fidelity Subvert Trust Controls (T1553)](#ultra-pro-high-fidelity-subvert-trust-controls-(t1553))
- [Ultra-Pro High-Fidelity macOS Gatekeeper und Quarantäne-Bypass (T1553.001)](#ultra-pro-high-fidelity-macos-gatekeeper-und-quarantäne-bypass-(t1553001))
- [Ultraprofessionelles High-Fidelity-SIP-Hijacking und Trust-Subversion (T1553.002)](#ultraprofessionelles-high-fidelity-sip-hijacking-und-trust-subversion-(t1553002))
- [Ultra-Pro High-Fidelity Windows Catalog Database Subversion (T1553.003)](#ultra-pro-high-fidelity-windows-catalog-database-subversion-(t1553003))
- [Ultra-Pro High-Fidelity-Root-Zertifikat-Injektion (T1553.004)](#ultra-pro-high-fidelity-root-zertifikat-injektion-(t1553004))
- [Ultra-Pro High-Fidelity MotW Bypass & Zone Subversion (T1553.005)](#ultra-pro-high-fidelity-motw-bypass-&-zone-subversion-(t1553005))
- [Ultra-Pro High-Fidelity-Codeintegrität und DSE-Subversion (T1553.006)](#ultra-pro-high-fidelity-codeintegrität-und-dse-subversion-(t1553006))
- [Kompromittierung der Binärintegrität des Ultra-Pro-Clients (T1554)](#kompromittierung-der-binärintegrität-des-ultra-pro-clients-(t1554))
- [Nicht-Browser-Prozesszugriff auf Browser-Anmeldeinformationsspeicher (High Fidelity)](#nicht-browser-prozesszugriff-auf-browser-anmeldeinformationsspeicher-(high-fidelity))
- [Ultra-Pro High-Fidelity Vault-Zugangsdatenerfassung (T1555.001)](#ultra-pro-high-fidelity-vault-zugangsdatenerfassung-(t1555001))
- [Ultra-Pro High-Fidelity-Sicherheitsspeicher-Dumping (T1555.002)](#ultra-pro-high-fidelity-sicherheitsspeicher-dumping-(t1555002))
- [Ultra-Pro High-Fidelity-Browser-Anmeldedatenerfassung (T1555.003)](#ultra-pro-high-fidelity-browser-anmeldedatenerfassung-(t1555003))
- [Ultra-Pro High-Fidelity Windows Credential Manager Harvesting (T1555.004)](#ultra-pro-high-fidelity-windows-credential-manager-harvesting-(t1555004))
- [Ultra-Pro High-Fidelity-Passwort-Manager-Extraktion (T1555.005)](#ultra-pro-high-fidelity-passwort-manager-extraktion-(t1555005))
- [Ultra-Pro High-Fidelity Cloud Secret Harvesting (T1555.006)](#ultra-pro-high-fidelity-cloud-secret-harvesting-(t1555006))
- [Exploit-Authentifizierungsprozess-Hijacking über verdächtige DLL-Registrierung](#exploit-authentifizierungsprozess-hijacking-über-verdächtige-dll-registrierung)
- [Exploit-Grade-Hijacking von Sicherheits-Support-Anbietern (LSA SSP)](#exploit-grade-hijacking-von-sicherheits-support-anbietern-(lsa-ssp))
- [Exploit-Grade-Passwortfilter-DLL-Hijacking über LSA-Benachrichtigungspakete](#exploit-grade-passwortfilter-dll-hijacking-über-lsa-benachrichtigungspakete)
- [Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003)](#ultra-pro-pam-integrity-hijacking-&-backdoor-(t1556003))
- [Ultra-Pro-Hijacking der Netzwerkgeräteauthentifizierung (T1556.004)](#ultra-pro-hijacking-der-netzwerkgeräteauthentifizierung-(t1556004))
- [Ultra-Pro SID-Verlaufsinjektionskorrelation (T1556.005)](#ultra-pro-sid-verlaufsinjektionskorrelation-(t1556005))
- [Ultra-Pro Entra ID MFA-Methoden-Hijacking (T1556.006)](#ultra-pro-entra-id-mfa-methoden-hijacking-(t1556006))
- [Ultra-Pro-Hybrid-Identitätssynchronisierungsmanipulation (T1556.007)](#ultra-pro-hybrid-identitätssynchronisierungsmanipulation-(t1556007))
- [Ultra-Pro-Netzwerk-zu-Cloud-Auth-Hijacking (T1556.008)](#ultra-pro-netzwerk-zu-cloud-auth-hijacking-(t1556008))
- [Ultra-Pro High-Fidelity Adversary-in-the-Middle (T1557)](#ultra-pro-high-fidelity-adversary-in-the-middle-(t1557))
- [Ultra-Pro High-Fidelity LLMNR/NBT-NS-Vergiftung (T1557.001)](#ultra-pro-high-fidelity-llmnrnbt-ns-vergiftung-(t1557001))
- [Ultra-Pro High-Fidelity ARP-Vergiftungserkennung (T1557.002)](#ultra-pro-high-fidelity-arp-vergiftungserkennung-(t1557002))
- [Ultra-Pro High-Fidelity DHCP-Spoofing-Erkennung (T1557.003)](#ultra-pro-high-fidelity-dhcp-spoofing-erkennung-(t1557003))
- [Ultra-Pro High-Fidelity-Kerberos-Angriffserkennung (T1558)](#ultra-pro-high-fidelity-kerberos-angriffserkennung-(t1558))
- [Ultra-Profi-High-Fidelity-Golden-Ticket-Fälschung und -Injektion (T1558.001)](#ultra-profi-high-fidelity-golden-ticket-fälschung-und--injektion-(t1558001))
- [Ultra-Pro High-Fidelity-Silber-Ticketfälschung und -Injektion (T1558.002)](#ultra-pro-high-fidelity-silber-ticketfälschung-und--injektion-(t1558002))
- [Verdächtige Kerberos TGS-Ticketanfrage (Kerberoasting)](#verdächtige-kerberos-tgs-ticketanfrage-(kerberoasting))
- [Ultra-Pro High-Fidelity AS-REP-Röstung und LDAP-Enumeration (T1558.004)](#ultra-pro-high-fidelity-as-rep-röstung-und-ldap-enumeration-(t1558004))
- [Indirekte IPC- und COM-Ausführung mit hoher Wiedergabetreue](#indirekte-ipc--und-com-ausführung-mit-hoher-wiedergabetreue)
- [Verdächtige Pipeline-Erstellung im Zusammenhang mit Post-Exploitation-Tools (High Fidelity)](#verdächtige-pipeline-erstellung-im-zusammenhang-mit-post-exploitation-tools-(high-fidelity))
- [High-Fidelity-Office-DDE-Kontextanomalie](#high-fidelity-office-dde-kontextanomalie)
- [High-Fidelity-Hypervisor-API und VM-Escape-Forschung](#high-fidelity-hypervisor-api-und-vm-escape-forschung)
- [Verdächtige Archivierung von Daten zu Exfiltrationszwecken](#verdächtige-archivierung-von-daten-zu-exfiltrationszwecken)
- [Ultra-Pro High-Fidelity-Datenarchivierung für Exfiltration (T1560.001)](#ultra-pro-high-fidelity-datenarchivierung-für-exfiltration-(t1560001))
- [Ultraprofessionelle High-Fidelity-Datenarchivierung über die Bibliothek (T1560.002)](#ultraprofessionelle-high-fidelity-datenarchivierung-über-die-bibliothek-(t1560002))
- [Ultra-Pro High-Fidelity-Archiv über benutzerdefinierte Methode (T1560.003)](#ultra-pro-high-fidelity-archiv-über-benutzerdefinierte-methode-(t1560003))
- [Ultra-Pro High-Fidelity Disk Wipe (T1561)](#ultra-pro-high-fidelity-disk-wipe-(t1561))
- [Ultra-Pro High-Fidelity-Datenträgerinhaltslöschung (T1561.001)](#ultra-pro-high-fidelity-datenträgerinhaltslöschung-(t1561001))
- [Ultra-Pro High-Fidelity Disk Structure Wipe (T1561.002)](#ultra-pro-high-fidelity-disk-structure-wipe-(t1561002))
- [Verdächtige Beendigung von Sicherheitsdiensten](#verdächtige-beendigung-von-sicherheitsdiensten)
- [Deaktivieren oder ändern Sie den Windows Defender-Schutz mit PowerShell](#deaktivieren-oder-ändern-sie-den-windows-defender-schutz-mit-powershell)
- [Ultra-Pro High-Fidelity Deaktivieren Sie die Windows-Ereignisprotokollierung (T1562.002)](#ultra-pro-high-fidelity-deaktivieren-sie-die-windows-ereignisprotokollierung-(t1562002))
- [Beeinträchtigung der Ultra-Pro High-Fidelity-Befehlsverlaufsprotokollierung (T1562.003)](#beeinträchtigung-der-ultra-pro-high-fidelity-befehlsverlaufsprotokollierung-(t1562003))
- [Verdächtige Firewall-Änderung über Netsh.exe](#verdächtige-firewall-änderung-über-netshexe)
- [Ultra-Pro High-Fidelity-Indikatorblockierung und Telemetrie-Stummschaltung (T1562.006)](#ultra-pro-high-fidelity-indikatorblockierung-und-telemetrie-stummschaltung-(t1562006))
- [Beeinträchtigung der Ultra-Pro High-Fidelity Cloud Firewall (T1562.007)](#beeinträchtigung-der-ultra-pro-high-fidelity-cloud-firewall-(t1562007))
- [Beeinträchtigung der Ultra-Pro High-Fidelity-Cloud-Protokollierung (T1562.008)](#beeinträchtigung-der-ultra-pro-high-fidelity-cloud-protokollierung-(t1562008))
- [Ultra-Pro High-Fidelity Safe Mode Defense Evasion (T1562.009)](#ultra-pro-high-fidelity-safe-mode-defense-evasion-(t1562009))
- [Ultra-Pro High-Fidelity-Verteidigungs-Downgrade-Angriff (T1562.010)](#ultra-pro-high-fidelity-verteidigungs-downgrade-angriff-(t1562010))
- [Ultra-Pro High-Fidelity-Virtualisierung und Sandbox-Umgehung (T1564.011)](#ultra-pro-high-fidelity-virtualisierung-und-sandbox-umgehung-(t1564011))
- [Beeinträchtigung der Ultra-Pro High-Fidelity Cloud-Sicherheitsinfrastruktur (T1562.012)](#beeinträchtigung-der-ultra-pro-high-fidelity-cloud-sicherheitsinfrastruktur-(t1562012))
- [Ultra-Pro High-Fidelity Remote Service Session Hijacking (T1563)](#ultra-pro-high-fidelity-remote-service-session-hijacking-(t1563))
- [Ultra-Pro High-Fidelity Local Session Hijacking (T1563.001)](#ultra-pro-high-fidelity-local-session-hijacking-(t1563001))
- [Ultra-Pro High-Fidelity RDP Session Hijacking (T1563.002)](#ultra-pro-high-fidelity-rdp-session-hijacking-(t1563002))
- [Ultraprofessionelle High-Fidelity-Erkennung versteckter Artefakte (T1564)](#ultraprofessionelle-high-fidelity-erkennung-versteckter-artefakte-(t1564))
- [Ultra-Pro High-Fidelity-Manipulation versteckter Dateiattribute (T1564.001)](#ultra-pro-high-fidelity-manipulation-versteckter-dateiattribute-(t1564001))
- [Ultra-Pro High-Fidelity-Erstellung versteckter Benutzerkonten (T1564.002)](#ultra-pro-high-fidelity-erstellung-versteckter-benutzerkonten-(t1564002))
- [Ultra-Pro High-Fidelity Hidden Window Execution (T1564.003)](#ultra-pro-high-fidelity-hidden-window-execution-(t1564003))
- [Ultra-Pro High-Fidelity NTFS Alternative Data Stream (ADS) Missbrauch (T1564.004)](#ultra-pro-high-fidelity-ntfs-alternative-data-stream-(ads)-missbrauch-(t1564004))
- [Ultra-Pro High-Fidelity-Manipulation versteckter Dateisysteme (T1564.005)](#ultra-pro-high-fidelity-manipulation-versteckter-dateisysteme-(t1564005))
- [Missbrauch der Ausführung virtueller Ultra-Pro-High-Fidelity-Instanzen (T1564.006)](#missbrauch-der-ausführung-virtueller-ultra-pro-high-fidelity-instanzen-(t1564006))
- [Ultra-Pro High-Fidelity VBA Macro Security Evasion (T1564.007)](#ultra-pro-high-fidelity-vba-macro-security-evasion-(t1564007))
- [Ultra-Pro High-Fidelity-Erkennung von E-Mail-Versteckregeln (T1564.008)](#ultra-pro-high-fidelity-erkennung-von-e-mail-versteckregeln-(t1564008))
- [Ultra-Pro High-Fidelity-Ressourcenextraktion und -missbrauch (T1564.009)](#ultra-pro-high-fidelity-ressourcenextraktion-und--missbrauch-(t1564009))
- [Ultra-Pro High-Fidelity-Prozessargument-Spoofing-Erkennung (T1564.010)](#ultra-pro-high-fidelity-prozessargument-spoofing-erkennung-(t1564010))
- [Missbrauch virtueller Ultra-Pro-High-Fidelity-Instanzen (T1564.011)](#missbrauch-virtueller-ultra-pro-high-fidelity-instanzen-(t1564011))
- [Ultraprofessionelle High-Fidelity-Datenmanipulation (T1565)](#ultraprofessionelle-high-fidelity-datenmanipulation-(t1565))
- [Ultra-Pro High-Fidelity-Manipulation gespeicherter Daten (T1565.001)](#ultra-pro-high-fidelity-manipulation-gespeicherter-daten-(t1565001))
- [Ultra-Pro High-Fidelity-Manipulation übertragener Daten (T1565.002)](#ultra-pro-high-fidelity-manipulation-übertragener-daten-(t1565002))
- [Ultra-Pro High-Fidelity-Laufzeitprozessmanipulation (T1565.003)](#ultra-pro-high-fidelity-laufzeitprozessmanipulation-(t1565003))
- [High-Fidelity-Phishing-Payload-Ausführung aus Kommunikations-Apps](#high-fidelity-phishing-payload-ausführung-aus-kommunikations-apps)
- [High-Fidelity-Ausführung von Spearphishing-Anhängen](#high-fidelity-ausführung-von-spearphishing-anhängen)
- [High-Fidelity-Browser-basierte Nutzlastausführung](#high-fidelity-browser-basierte-nutzlastausführung)
- [High-Fidelity-Prozess-Spawn vom Business Communication Service](#high-fidelity-prozess-spawn-vom-business-communication-service)
- [Hochpräzise Erkennung der Remote-Tool-Ausführung nach dem Vishing](#hochpräzise-erkennung-der-remote-tool-ausführung-nach-dem-vishing)
- [Ultra-Pro High-Fidelity Web Service Exfiltration (T1567)](#ultra-pro-high-fidelity-web-service-exfiltration-(t1567))
- [Ultra-Pro High-Fidelity Code Repo Exfil (T1567.001)](#ultra-pro-high-fidelity-code-repo-exfil-(t1567001))
- [Ultra-Pro High-Fidelity Cloud Storage Exfil (T1567.002)](#ultra-pro-high-fidelity-cloud-storage-exfil-(t1567002))
- [Ultraprofessionelles High-Fidelity-Video-Hosting Exfil (T1567.003)](#ultraprofessionelles-high-fidelity-video-hosting-exfil-(t1567003))
- [Ultra-Pro High-Fidelity-Textspeicher Exfil (T1567.004)](#ultra-pro-high-fidelity-textspeicher-exfil-(t1567004))
- [Ultraprofessionelle, dynamische Auflösung und DGA (T1568)](#ultraprofessionelle-dynamische-auflösung-und-dga-(t1568))
- [Ultra-Pro High-Fidelity Fast Flux & DNS Cache Evasion (T1568.001)](#ultra-pro-high-fidelity-fast-flux-&-dns-cache-evasion-(t1568001))
- [Ultra-Pro High-Fidelity Domain Generation Algorithmus (DGA) (T1568.002)](#ultra-pro-high-fidelity-domain-generation-algorithmus-(dga)-(t1568002))
- [Ultra-Pro High-Fidelity-DNS-Berechnung und -Extraktion (T1568.003)](#ultra-pro-high-fidelity-dns-berechnung-und--extraktion-(t1568003))
- [High-Fidelity-Erkennung der Ausführung von Systemdiensten](#high-fidelity-erkennung-der-ausführung-von-systemdiensten)
- [High-Fidelity-Launch-Daemon-Persistenzerkennung](#high-fidelity-launch-daemon-persistenzerkennung)
- [High-Fidelity-Systemdienstausführungserkennung (T1569.002)](#high-fidelity-systemdienstausführungserkennung-(t1569002))
- [Ultra-Pro High-Fidelity-lateraler Werkzeugtransfer (T1570)](#ultra-pro-high-fidelity-lateraler-werkzeugtransfer-(t1570))
- [Ultra-Pro High-Fidelity Nicht-Standard-Port C2 (T1571)](#ultra-pro-high-fidelity-nicht-standard-port-c2-(t1571))
- [Ultra-Pro High-Fidelity-Protokoll-Tunneling-Erkennung (T1571)](#ultra-pro-high-fidelity-protokoll-tunneling-erkennung-(t1571))
- [Ultra-Pro High-Fidelity-verschlüsselter C2-Kanal (T1573)](#ultra-pro-high-fidelity-verschlüsselter-c2-kanal-(t1573))
- [Ultra-Pro High-Fidelity Symmetric Encryption C2-Kanal (T1573.001)](#ultra-pro-high-fidelity-symmetric-encryption-c2-kanal-(t1573001))
- [Ultra-Pro High-Fidelity Asymmetric Encryption C2 (T1573.002)](#ultra-pro-high-fidelity-asymmetric-encryption-c2-(t1573002))
- [Ultra-Pro DLL-Hijacking und Sideloading-Erkennung (T1574)](#ultra-pro-dll-hijacking-und-sideloading-erkennung-(t1574))
- [Ultra-Pro DLL-Suchreihenfolge-Hijacking-Erkennung (T1574.001)](#ultra-pro-dll-suchreihenfolge-hijacking-erkennung-(t1574001))
- [Ultra-Pro DLL Side-Loading Integrity Gap Detection (T1574.002)](#ultra-pro-dll-side-loading-integrity-gap-detection-(t1574002))
- [Ultra-Pro-Shell-Konfiguration und Pfadabfang (T1574.003)](#ultra-pro-shell-konfiguration-und-pfadabfang-(t1574003))
- [Entführung von Ultra-Pro-Bibliothekssuchaufträgen und Integritätslücke (T1574.004)](#entführung-von-ultra-pro-bibliothekssuchaufträgen-und-integritätslücke-(t1574004))
- [Schwäche bei Dateiberechtigungen des Ultra-Pro-Installationsprogramms (T1574.005)](#schwäche-bei-dateiberechtigungen-des-ultra-pro-installationsprogramms-(t1574005))
- [Dynamic Linker-Hijacking gegen privilegierte Binärdateien](#dynamic-linker-hijacking-gegen-privilegierte-binärdateien)
- [PATH-Hijacking führt zur privilegierten Binärausführung](#path-hijacking-führt-zur-privilegierten-binärausführung)
- [Entführung der .NET-Assembly-Suchreihenfolge über ein vom Benutzer beschreibbares Verzeichnis](#entführung-der-net-assembly-suchreihenfolge-über-ein-vom-benutzer-beschreibbares-verzeichnis)
- [.NET AppDomainManager-Hijacking über Nicht-GAC-Assembly](#net-appdomainmanager-hijacking-über-nicht-gac-assembly)
- [Ausführbare Datei des privilegierten Dienstes vom vom Benutzer beschreibbaren Speicherort überschrieben](#ausführbare-datei-des-privilegierten-dienstes-vom-vom-benutzer-beschreibbaren-speicherort-überschrieben)
- [Privilegierter Dienst ImagePath oder ServiceDll über die Registrierung gekapert](#privilegierter-dienst-imagepath-oder-servicedll-über-die-registrierung-gekapert)
- [COR_PROFILER-Hijacking der Exploit-Klasse über eine vom Benutzer beschreibbare Profiler-DLL](#cor_profiler-hijacking-der-exploit-klasse-über-eine-vom-benutzer-beschreibbare-profiler-dll)
- [Exploit-Grade-KernelCallbackTable-Manipulation über Remote-Speicher-Schreiben](#exploit-grade-kernelcallbacktable-manipulation-über-remote-speicher-schreiben)
- [Manipulation der Ultra-Pro-High-Fidelity-Cloud-Infrastruktur (T1578)](#manipulation-der-ultra-pro-high-fidelity-cloud-infrastruktur-(t1578))
- [Ultra-Pro High-Fidelity-Erstellung verdächtiger Cloud-Instanzen (T1578.001)](#ultra-pro-high-fidelity-erstellung-verdächtiger-cloud-instanzen-(t1578001))
- [Ultra-Pro High-Fidelity Cloud Snapshot Exfiltration (T1578.002)](#ultra-pro-high-fidelity-cloud-snapshot-exfiltration-(t1578002))
- [Ultra-Pro High-Fidelity-Cloud-Instanzzerstörung (T1578.003)](#ultra-pro-high-fidelity-cloud-instanzzerstörung-(t1578003))
- [Ultra-Pro High-Fidelity Cloud Image Manipulation (T1578.004)](#ultra-pro-high-fidelity-cloud-image-manipulation-(t1578004))
- [Ultra-Pro High-Fidelity-Cloud-Netzwerk-Sicherheitsregression (T1578.005)](#ultra-pro-high-fidelity-cloud-netzwerk-sicherheitsregression-(t1578005))
- [Ultraprofessionelle High-Fidelity-Cloud-Infrastrukturerkennung (T1580)](#ultraprofessionelle-high-fidelity-cloud-infrastrukturerkennung-(t1580))
- [Bereitstellung einer High-Fidelity-Offensiv-Infrastruktur – T1583](#bereitstellung-einer-high-fidelity-offensiv-infrastruktur-–-t1583)
- [Bereitstellung einer High-Fidelity-VPS-Infrastruktur – T1583.001](#bereitstellung-einer-high-fidelity-vps-infrastruktur-–-t1583001)
- [Automatisierte High-Fidelity-Domainregistrierung und -Akquise – T1583.002](#automatisierte-high-fidelity-domainregistrierung-und--akquise-–-t1583002)
- [Bereitstellung von High-Fidelity-Cloud-Netzwerken (VPC) – T1583.003](#bereitstellung-von-high-fidelity-cloud-netzwerken-(vpc)-–-t1583003)
- [Serverlose Infrastrukturbereitstellung mit hoher Wiedergabetreue – T1583.004](#serverlose-infrastrukturbereitstellung-mit-hoher-wiedergabetreue-–-t1583004)
- [Erwerb einer High-Fidelity-Botnet-Infrastruktur – T1583.005](#erwerb-einer-high-fidelity-botnet-infrastruktur-–-t1583005)
- [Erwerb und Bereitstellung von High-Fidelity-Webdiensten – T1583.006](#erwerb-und-bereitstellung-von-high-fidelity-webdiensten-–-t1583006)
- [Serverlose Infrastrukturbereitstellung mit hoher Wiedergabetreue – T1583.007](#serverlose-infrastrukturbereitstellung-mit-hoher-wiedergabetreue-–-t1583007)
- [High-Fidelity-Cloud-Kontoerwerb und Bootstrap – T1583.008](#high-fidelity-cloud-kontoerwerb-und-bootstrap-–-t1583008)
- [Kompromittierte High-Fidelity-Infrastruktur und Ressourcenmissbrauch – T1584](#kompromittierte-high-fidelity-infrastruktur-und-ressourcenmissbrauch-–-t1584)
- [Hijacking der High-Fidelity-Domain-Infrastruktur – T1584.001](#hijacking-der-high-fidelity-domain-infrastruktur-–-t1584001)
- [Subversion der High-Fidelity-DNS-Serverkonfiguration – T1584.002](#subversion-der-high-fidelity-dns-serverkonfiguration-–-t1584002)
- [High-Fidelity-Cloud-Identitätssubversion und -Persistenz – T1584.003](#high-fidelity-cloud-identitätssubversion-und--persistenz-–-t1584003)
- [Serverlose High-Fidelity-Funktionssubversion – T1584.004](#serverlose-high-fidelity-funktionssubversion-–-t1584004)
- [High-Fidelity-Botnet-Agent-Persistenz und -Kontrolle – T1584.005](#high-fidelity-botnet-agent-persistenz-und--kontrolle-–-t1584005)
- [High-Fidelity-Webdienst und Cloud-Speicher-Subversion – T1584.006](#high-fidelity-webdienst-und-cloud-speicher-subversion-–-t1584006)
- [High-Fidelity-VPS-Steuerung und Tunneling – T1584.007](#high-fidelity-vps-steuerung-und-tunneling-–-t1584007)
- [Verdächtige Benutzerkontoerstellung über CLI/Scripting](#verdächtige-benutzerkontoerstellung-über-cliscripting)
- [Mögliche automatisierte Einrichtung eines Social-Media-Kontos](#mögliche-automatisierte-einrichtung-eines-social-media-kontos)
- [Heimliche Einrichtung und Manipulation von E-Mail-Konten](#heimliche-einrichtung-und-manipulation-von-e-mail-konten)
- [Anomale Erstellung eines Cloud-Benutzerkontos](#anomale-erstellung-eines-cloud-benutzerkontos)
- [Kompromittierung von High-Fidelity-Konten und Identitätsmanipulation – T1586](#kompromittierung-von-high-fidelity-konten-und-identitätsmanipulation-–-t1586)
- [Automatisierte Social-Media-Manipulation mit hoher Wiedergabetreue – T1586.001](#automatisierte-social-media-manipulation-mit-hoher-wiedergabetreue-–-t1586001)
- [Manipulation von High-Fidelity-E-Mail-Weiterleitungsregeln – T1586.002](#manipulation-von-high-fidelity-e-mail-weiterleitungsregeln-–-t1586002)
- [Übernahme und Persistenz von High-Fidelity-Cloud-Konten – T1586.003](#übernahme-und-persistenz-von-high-fidelity-cloud-konten-–-t1586003)
- [Entwicklung und Zusammenstellung von High-Fidelity-Offensivfähigkeiten – T1587](#entwicklung-und-zusammenstellung-von-high-fidelity-offensivfähigkeiten-–-t1587)
- [High-Fidelity-Malware-Entwicklungs- und Umgehungsmuster – T1587.001](#high-fidelity-malware-entwicklungs--und-umgehungsmuster-–-t1587001)
- [Entwicklung von High-Fidelity-Funktionen für nicht autorisierte Code-Signierung – T1587.002](#entwicklung-von-high-fidelity-funktionen-für-nicht-autorisierte-code-signierung-–-t1587002)
- [Unbefugte Entwicklung digitaler High-Fidelity-Zertifikate – T1587.003](#unbefugte-entwicklung-digitaler-high-fidelity-zertifikate-–-t1587003)
- [High-Fidelity-Exploit-Entwicklung und Kompilierungserkennung – T1587.004](#high-fidelity-exploit-entwicklung-und-kompilierungserkennung-–-t1587004)
- [Anomale Beschaffung von Angriffsfähigkeiten](#anomale-beschaffung-von-angriffsfähigkeiten)
- [Anomale Beschaffung von Malware-Fähigkeiten](#anomale-beschaffung-von-malware-fähigkeiten)
- [Anomale Offensiv-Tool-Erfassung über CLI](#anomale-offensiv-tool-erfassung-über-cli)
- [Anomaler Export oder Erwerb von Code Signing-Zertifikaten](#anomaler-export-oder-erwerb-von-code-signing-zertifikaten)
- [Strategische Manipulation des Speichers vertrauenswürdiger Stammzertifikate](#strategische-manipulation-des-speichers-vertrauenswürdiger-stammzertifikate)
- [Anomale Beschaffung von Exploit- oder PoC-Code](#anomale-beschaffung-von-exploit--oder-poc-code)
- [Gezielte Ernte von Artefakten der Schwachstellenforschung](#gezielte-ernte-von-artefakten-der-schwachstellenforschung)
- [High-Fidelity-Identitätsaufzählung über Authentifizierungsendpunkte](#high-fidelity-identitätsaufzählung-über-authentifizierungsendpunkte)
- [Aufzählung der Anmeldeinformationen über die Authentifizierungs-API (hohes Vertrauen)](#aufzählung-der-anmeldeinformationen-über-die-authentifizierungs-api-(hohes-vertrauen))
- [Hochzuverlässige OSINT-Identitätsaufzählung über öffentliche APIs](#hochzuverlässige-osint-identitätsaufzählung-über-öffentliche-apis)
- [Gezielte OSINT-Enumeration offener Websites und Domains](#gezielte-osint-enumeration-offener-websites-und-domains)
- [Netzwerkaufklärung mit hoher Portvielfalt](#netzwerkaufklärung-mit-hoher-portvielfalt)
- [Professionelle Aufklärung der IP-Infrastruktur – T1590.001](#professionelle-aufklärung-der-ip-infrastruktur-–-t1590001)
- [Erweiterte Aufklärung der DNS-Infrastruktur – T1590.002](#erweiterte-aufklärung-der-dns-infrastruktur-–-t1590002)
- [Erweiterte Aufklärung von Netzwerkvertrauensabhängigkeiten – T1590.003](#erweiterte-aufklärung-von-netzwerkvertrauensabhängigkeiten-–-t1590003)
- [Erweiterte Informationsaufklärung für Zertifikate – T1590.004](#erweiterte-informationsaufklärung-für-zertifikate-–-t1590004)
- [Erweiterte Aufklärung der Cloud-Infrastruktur – T1590.005](#erweiterte-aufklärung-der-cloud-infrastruktur-–-t1590005)
- [Erweiterte Aufklärung über Opfer-Webseiteninformationen – T1590.006](#erweiterte-aufklärung-über-opfer-webseiteninformationen-–-t1590006)
- [Erweiterte Aufzählung der organisatorischen Infrastruktur – T1591](#erweiterte-aufzählung-der-organisatorischen-infrastruktur-–-t1591)
- [Erweiterte Aufzählung der physischen Standortinfrastruktur – T1591.001](#erweiterte-aufzählung-der-physischen-standortinfrastruktur-–-t1591001)
- [Erweiterte Erkennung von Geschäftsbeziehungsinformationen – T1591.002](#erweiterte-erkennung-von-geschäftsbeziehungsinformationen-–-t1591002)
- [Advanced Knowledge Management Discovery – T1591.003](#advanced-knowledge-management-discovery-–-t1591003)
- [High-Fidelity-Ermittlung von Personalinformationen – T1591.004](#high-fidelity-ermittlung-von-personalinformationen-–-t1591004)
- [High-Fidelity-Host-Informationsaufklärungsaktivität](#high-fidelity-host-informationsaufklärungsaktivität)
- [Hochzuverlässige Hardware-Enumeration über Verwaltungsschnittstellen](#hochzuverlässige-hardware-enumeration-über-verwaltungsschnittstellen)
- [Erweiterte Software-Enumerationsaufklärung über Web-Endpunkte](#erweiterte-software-enumerationsaufklärung-über-web-endpunkte)
- [Hochzuverlässige Firmware-Enumeration für Netzwerkgeräte](#hochzuverlässige-firmware-enumeration-für-netzwerkgeräte)
- [Hochzuverlässiges Client-Konfigurations-Fingerprinting (Aufklärung)](#hochzuverlässiges-client-konfigurations-fingerprinting-(aufklärung))
- [Automatisierte Webaufklärung mit hoher Wiedergabetreue – T1593](#automatisierte-webaufklärung-mit-hoher-wiedergabetreue-–-t1593)
- [High-Fidelity Social Media Entity Harvesting – T1593.001](#high-fidelity-social-media-entity-harvesting-–-t1593001)
- [Automatisierte Suchmaschinenaufklärung mit hoher Wiedergabetreue – T1593.002](#automatisierte-suchmaschinenaufklärung-mit-hoher-wiedergabetreue-–-t1593002)
- [High-Fidelity Social Media Entity Harvesting – T1593.003](#high-fidelity-social-media-entity-harvesting-–-t1593003)
- [High-Fidelity Information Repository Reconnaissance – T1594](#high-fidelity-information-repository-reconnaissance-–-t1594)
- [High-Fidelity Active Scanning-Erkennung (verhaltensbasiert)](#high-fidelity-active-scanning-erkennung-(verhaltensbasiert))
- [High-Fidelity-Erkennung externer IP-Block-Scans](#high-fidelity-erkennung-externer-ip-block-scans)
- [Hochzuverlässige externe Schwachstellen-Scan-Aktivität](#hochzuverlässige-externe-schwachstellen-scan-aktivität)
- [Aktives Scannen von Wortlisten anhand von Authentifizierungsendpunkten](#aktives-scannen-von-wortlisten-anhand-von-authentifizierungsendpunkten)
- [Offene technische Datenbankaufklärung mit hoher Wiedergabetreue – T1596](#offene-technische-datenbankaufklärung-mit-hoher-wiedergabetreue-–-t1596)
- [Hochpräzise WHOIS-Datenbankaufklärung – T1596.001](#hochpräzise-whois-datenbankaufklärung-–-t1596001)
- [Automatisierte High-Fidelity-Suchmaschine Dorking – T1596.002](#automatisierte-high-fidelity-suchmaschine-dorking-–-t1596002)
- [Passive High-Fidelity-DNS-Aufklärung – T1597.003](#passive-high-fidelity-dns-aufklärung-–-t1597003)
- [High-Fidelity-Aufklärung digitaler Zertifikate – T1596.004](#high-fidelity-aufklärung-digitaler-zertifikate-–-t1596004)
- [High-Fidelity-IP-Infrastrukturaufklärung – T1596.005](#high-fidelity-ip-infrastrukturaufklärung-–-t1596005)
- [High-Fidelity-Website-Erkundung im Besitz von Opfern – T1597](#high-fidelity-website-erkundung-im-besitz-von-opfern-–-t1597)
- [High-Fidelity-Domäneninfrastrukturaufzählung – T1597.001](#high-fidelity-domäneninfrastrukturaufzählung-–-t1597001)
- [High-Fidelity-Geheimnisjagd in Code-Repositories – T1597.002](#high-fidelity-geheimnisjagd-in-code-repositories-–-t1597002)
- [Erweitertes Phishing zum Sammeln von Informationen und Anmeldeinformationen – T1598](#erweitertes-phishing-zum-sammeln-von-informationen-und-anmeldeinformationen-–-t1598)
- [Erweiterte Spearphishing-Linkumleitung – T1598.001](#erweiterte-spearphishing-linkumleitung-–-t1598001)
- [Erweiterte BEC-Mail- und Finanzdaten-Exfiltration – T1598.002](#erweiterte-bec-mail--und-finanzdaten-exfiltration-–-t1598002)
- [High-Fidelity-MFA/OTP-Spoofing und -Ernte – T1598.003](#high-fidelity-mfaotp-spoofing-und--ernte-–-t1598003)
- [High-Fidelity-Interaktion mit Spearphishing-Anhängen – T1598.004](#high-fidelity-interaktion-mit-spearphishing-anhängen-–-t1598004)
- [Ultra-Pro High-Fidelity-Netzwerk-Boundary-Bridging (T1599)](#ultra-pro-high-fidelity-netzwerk-boundary-bridging-(t1599))
- [Ultra-Pro High-Fidelity Logical Isolation Bypass (T1599.001)](#ultra-pro-high-fidelity-logical-isolation-bypass-(t1599001))
- [Ultra-Pro High-Fidelity-Verschlüsselungsversuch schwächen (T1600)](#ultra-pro-high-fidelity-verschlüsselungsversuch-schwächen-(t1600))
- [Ultra-Pro High-Fidelity-System-Image-Patching (T1600.001)](#ultra-pro-high-fidelity-system-image-patching-(t1600001))
- [Ultra-Pro High-Fidelity-Entitätsüberprüfung deaktivieren (T1600.002)](#ultra-pro-high-fidelity-entitätsüberprüfung-deaktivieren-(t1600002))
- [Ultra-Pro High-Fidelity-Netzwerk-OS-Image-Modifikation (T1601)](#ultra-pro-high-fidelity-netzwerk-os-image-modifikation-(t1601))
- [Ultra-Pro High-Fidelity-Netzwerk-Binär-Patching (T1601.001)](#ultra-pro-high-fidelity-netzwerk-binär-patching-(t1601001))
- [Ultra-Pro High-Fidelity-Upgrade für bösartige Netzwerk-Betriebssysteme (T1601.002)](#ultra-pro-high-fidelity-upgrade-für-bösartige-netzwerk-betriebssysteme-(t1601002))
- [Automatisierte Ultra-Pro-High-Fidelity-Netzwerkfreigabeerfassung (T1602)](#automatisierte-ultra-pro-high-fidelity-netzwerkfreigabeerfassung-(t1602))
- [Ultra-Pro High-Fidelity Admin-Share-Datenexfiltration (T1602.001)](#ultra-pro-high-fidelity-admin-share-datenexfiltration-(t1602001))
- [Ultra-Pro High-Fidelity Cloud Share Exfiltration (T1602.002)](#ultra-pro-high-fidelity-cloud-share-exfiltration-(t1602002))
- [Ultra-Pro High-Fidelity-Web-Token-Fälschung (T1606)](#ultra-pro-high-fidelity-web-token-fälschung-(t1606))
- [Ultra-Pro High-Fidelity-Web-Cookie-Ernte (T1606.001)](#ultra-pro-high-fidelity-web-cookie-ernte-(t1606001))
- [Ultra-Pro High-Fidelity Web Token Forgery & Golden SAML (T1606.002)](#ultra-pro-high-fidelity-web-token-forgery-&-golden-saml-(t1606002))
- [Anomale Infrastrukturbereitstellung und Ressourcenbereitstellung](#anomale-infrastrukturbereitstellung-und-ressourcenbereitstellung)
- [Anomale Malware-Bereitstellung in der externen Infrastruktur](#anomale-malware-bereitstellung-in-der-externen-infrastruktur)
- [Anomales offensives Tool-Staging und externer Upload](#anomales-offensives-tool-staging-und-externer-upload)
- [Strategisches Staging digitaler Zertifikate im vertrauenswürdigen Stammspeicher](#strategisches-staging-digitaler-zertifikate-im-vertrauenswürdigen-stammspeicher)
- [Anomale Webinhaltsmodifikation für Drive-by-Staging](#anomale-webinhaltsmodifikation-für-drive-by-staging)
- [Strategische Inszenierung bösartiger Link-Ziele](#strategische-inszenierung-bösartiger-link-ziele)
- [Anomale SEO-Vergiftung und Metadaten-Staging](#anomale-seo-vergiftung-und-metadaten-staging)
- [Interaktive Shell-Ausführung für High-Fidelity-Container](#interaktive-shell-ausführung-für-high-fidelity-container)
- [High-Fidelity-Erkennung der Bereitstellung bösartiger Container](#high-fidelity-erkennung-der-bereitstellung-bösartiger-container)
- [Ultra-Pro Container-Flucht und Host-Zugriff (T1611)](#ultra-pro-container-flucht-und-host-zugriff-(t1611))
- [Ultra-Pro Stealthy Local Image Build (T1612)](#ultra-pro-stealthy-local-image-build-(t1612))
- [Ultra-Pro High-Fidelity-Container- und Instanzerkennung (T1613)](#ultra-pro-high-fidelity-container--und-instanzerkennung-(t1613))
- [Ultra-Pro High-Fidelity-System zur Standorterkennung (T1614)](#ultra-pro-high-fidelity-system-zur-standorterkennung-(t1614))
- [Erkennung von High-Fidelity-Systemsprache und Tastaturlayout](#erkennung-von-high-fidelity-systemsprache-und-tastaturlayout)
- [High-Fidelity-Erkennung von Gruppenrichtlinien](#high-fidelity-erkennung-von-gruppenrichtlinien)
- [High-Fidelity-Erkennung von Cloud-Speicherobjekten](#high-fidelity-erkennung-von-cloud-speicherobjekten)
- [High-Fidelity-Reflective-Code-Laden und In-Memory-Assembly-Ausführung](#high-fidelity-reflective-code-laden-und-in-memory-assembly-ausführung)
- [Verdächtige MFA-Prompt-Bombing- oder Authentifizierungs-Flood-Automatisierung](#verdächtige-mfa-prompt-bombing--oder-authentifizierungs-flood-automatisierung)
- [Verdächtiger Anti-Debug-API-Zugriff aus nicht gesichertem oder User-Space-Speicher](#verdächtiger-anti-debug-api-zugriff-aus-nicht-gesichertem-oder-user-space-speicher)
- [Verdächtige macOS LaunchAgent- oder LaunchDaemon Plist-Änderung](#verdächtige-macos-launchagent--oder-launchdaemon-plist-änderung)
- [Persistenz oder Missbrauch von serverlosen High-Fidelity-Funktionen](#persistenz-oder-missbrauch-von-serverlosen-high-fidelity-funktionen)
- [Verdächtige Aktivität beim Exportieren oder Diebstahl von Zertifikaten und privaten Schlüsseln](#verdächtige-aktivität-beim-exportieren-oder-diebstahl-von-zertifikaten-und-privaten-schlüsseln)
- [High-Fidelity-Cloud-Kontoerwerb und -Initialisierung – T1650](#high-fidelity-cloud-kontoerwerb-und--initialisierung-–-t1650)
- [Missbrauch von High-Fidelity-Cloud-Verwaltungsagenten](#missbrauch-von-high-fidelity-cloud-verwaltungsagenten)
- [Aufzählung verdächtiger Gerätetreiber aus anomalem Kontext (BYOVD Recon)](#aufzählung-verdächtiger-gerätetreiber-aus-anomalem-kontext-(byovd-recon))
- [Manipulation der Ultra-Pro-Energieeinstellungen (T1137.001)](#manipulation-der-ultra-pro-energieeinstellungen-(t1137001))
- [Aufzählung verdächtiger Ereignisprotokolle aufgrund eines anomalen Ausführungskontexts](#aufzählung-verdächtiger-ereignisprotokolle-aufgrund-eines-anomalen-ausführungskontexts)
- [Verdächtiger Identitätswechsel durch RunAs-Missbrauch oder irreführende lokale Kontoerstellung](#verdächtiger-identitätswechsel-durch-runas-missbrauch-oder-irreführende-lokale-kontoerstellung)
- [Verdächtige Manipulation der Zwischenablage und Zugriff auf Finanzdokumente über einen nicht vertrauenswürdigen übergeordneten Prozess](#verdächtige-manipulation-der-zwischenablage-und-zugriff-auf-finanzdokumente-über-einen-nicht-vertrauenswürdigen-übergeordneten-prozess)
- [Professionelle Content-Impersonation und Infrastrukturspiegelung](#professionelle-content-impersonation-und-infrastrukturspiegelung)
- [Verdächtiger Zugriff auf den LSASS-Prozessspeicher (Credential Dumping-Versuch)](#verdächtiger-zugriff-auf-den-lsass-prozessspeicher-(credential-dumping-versuch))

---
## Ultraprofessionelle High-Fidelity-Steganographie und Datenrekonstruktion (T1001)
- **ID:** `T1001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Daten-Desteganographie durch Identifizierung anomaler programmatischer Zugriffe
zu Bildbearbeitungs-APIs (GDI+, System.Drawing) von Skriptinterpretern,
Ich suche speziell nach Datenextraktionsroutinen auf Pixelebene.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Junk Data & Command Padding (T1001.001)
- **ID:** `T1001_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Befehlsauffüllung und Junk-Data-Injection durch Identifizierung von Anomalien
Leerraumverteilung, sich wiederholende Umgebungsvariablendefinitionen,
und extreme Befehlszeilenlängen in Nicht-Installer-Prozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Steganographie und Datenrekonstruktion (T1001.002)
- **ID:** `T1001_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Daten-Desteganographie durch Identifizierung anomaler programmatischer Zugriffe
zu Bildbearbeitungs-APIs (GDI+, System.Drawing) von Skriptinterpretern,
Ich suche speziell nach Datenextraktionsroutinen auf Pixelebene.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Protokoll-Imitation (T1001.003)
- **ID:** `T1001_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Protokollfälschungen durch Identifizierung manueller Manipulationen von Netzwerk-Headern
und insbesondere anomale User-Agent-Zeichenfolgen innerhalb von Skriptinterpretern
Targeting-Versuche, mobile Geräte nachzuahmen oder Crawler aus Nicht-Browser-Prozessen zu durchsuchen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity LSASS Credential Dumping (T1003)
- **ID:** `T1003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt hochentwickelte LSASS-Speicherauszugstechniken.
Konzentriert sich auf DLL-Export-Ordinalzahlen (#24), die Handhabung von Duplikaten,
und spezielle LOLBins, die die standardmäßige EDR-String-basierte Erkennung umgehen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtiger Zugriff auf den LSASS-Prozessspeicher
- **ID:** `T1003_001.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt verdächtige Zugriffe auf den Speicher des LSASS-Prozesses, die auf ein Dumping von Anmeldeinformationen hinweisen können.Die Regel überwacht verdächtige GrantedAccess-Masken und filtert häufige legitime Prozesse.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity SAM & SYSTEM-Registrierungsdiebstahl (T1003.002)
- **ID:** `T1003_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes Extrahieren der Registrierungsstrukturen SAM, SYSTEM und SECURITY.
Konzentriert sich auf den Missbrauch von „reg.exe“, VSS-basierten Diebstahl und das Kopieren von „esentutl.exe“-Dateien
von nicht standardmäßigen übergeordneten Prozessen und nicht vertrauenswürdigen Ausführungspfaden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity NTDS.dit-Extraktion (T1003.003)
- **ID:** `T1003_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [DISKSHADOW.EXE](https://lolbas-project.github.io/lolbas/), [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [NTDSUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes Extrahieren der Active Directory-Datenbank (NTDS.dit).
Identifiziert „ntdsutil“ mit abgekürzten Befehlen, Diskshadow-Skripten,
und Erstellung von Schattenkopien durch Nicht-Backup-Prozesse auf Domänencontrollern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity LSA Secrets & Security Hive Theft (T1003.004)
- **ID:** `T1003_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Extraktion von LSA-Geheimnissen aus der Registrierungsstruktur HKLM\SECURITY.
Konzentriert sich auf erweiterte Exportmuster, Remote-Dumps im Impacket-Stil und
Anmeldeinformationszugriff über nicht vertrauenswürdige übergeordnete Prozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity MSCASH/DCC-Extraktion (T1003.005)
- **ID:** `T1003_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Extraktion von zwischengespeicherten Domänenanmeldeinformationen (MSCASH/DCC).
Überwacht die Fingerabdrücke spezieller Tools und zielt auf Registrierungsspeichervorgänge ab
der Cache-Schlüssel und anomale Eltern-Kind-Prozessbeziehungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity DCSync-Angriffserkennung (T1003.006)
- **ID:** `T1003_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt DCSync-Angriffe, bei denen sich ein Angreifer als Domänencontroller ausgibt
Anmeldeinformationen anzufordern.Konzentriert sich auf bestimmte RPC-Flags, abgekürzte Toolbefehle,
und anomale Prozessherkunft bei Nicht-DC-Assets.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity LSASS Memory Dump & LOLBin-Missbrauch (T1003.007)
- **ID:** `T1003_007.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt anspruchsvolles LSASS-Speicher-Dumping.Konzentriert sich auf Procdump-Argumentmuster,
Vom Task-Manager initiierte Dumps über WerFault und COM+-Exporte (comsvcs.dll) mit
Ordinalbasierte Aufrufe (#24), um die stringbasierte Erkennung zu umgehen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Linux-Schattendateiextraktion (T1003.008)
- **ID:** `T1003_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt unbefugtes Extrahieren der Datei /etc/shadow.
Konzentriert sich auf die Umleitung auf verdächtige Pfade, die Archivierung,
und Exfiltration über Netzwerktools (LOLBins) aus interaktiven Shells.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle lokale Datenerfassung mit hoher Wiedergabetreue (T1005)
- **ID:** `T1005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische lokale Datenerfassung durch Identifizierung der Kombination von
rekursive Dateierkennung, gezielte sensible Erweiterungen und die Verwendung von
nicht standardmäßige Suchwerkzeuge oder verdächtige Prozessabstammungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy Direct Volume Access (T1006)
- **ID:** `T1006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt direkten High-Fidelity-Volume-Zugriff durch Überwachung auf Rohgerätepfade
Initiiert durch systemfremde Prozesse oder misstrauische Eltern, oft zur Umgehung verwendet
Dateisystemsperren und EDR-Überwachung für das Dumping von Anmeldeinformationen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity System Service Discovery (T1007)
- **ID:** `T1007.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Entdeckung von Systemdiensten.Konzentriert sich auf verdächtige übergeordnete Prozesse
und spezifische Befehlszeilenargumente zur Identifizierung von Sicherheitsprodukten oder
falsch konfigurierte Dienste zur Rechteausweitung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Fallback-Kanalerkennung (T1008)
- **ID:** `T1008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt C2-Fallback-Mechanismen durch Identifizierung protokollübergreifender Switching-Logik
(z. B. HTTP zu DNS/ICMP) innerhalb von Ausnahmebehandlungsblöcken (try/catch/trap)
ausgelöst durch Verbindungsfehler in nicht standardmäßigen Prozesskontexten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Anwendungsfenstererkennung (T1010)
- **ID:** `T1010.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die nicht autorisierte Erkennung von Anwendungsfenstern durch Überwachung auf .NET
Zugriff auf die MainWindowTitle-Eigenschaft und Win32-API-Aufrufe über CLI.
Konzentriert sich auf nicht standardmäßige Abstammungslinien und Ausgabeumleitungen, die von Malware zum Herausfiltern von Fenstertiteln verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Bluetooth-Exfiltration (T1011)
- **ID:** `T1011.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Datenexfiltration über Bluetooth durch Identifizierung programmgesteuerter Daten
Auslöser von Bluetooth-Übertragungsassistenten (fsquirt.exe) von nicht standardmäßig
übergeordnete Prozesse oder verdächtige Befehlszeilenausführungen von Funksteuerungstools.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity BLE-Werbe-Exfiltration (T1011.001)
- **ID:** `T1011_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdeckte Datenexfiltration über BLE-Werberahmen durch Identifizierung
Nicht autorisierte Prozesse, die WinRT BluetoothLEAdvertisementPublisher aufrufen
APIs zur Übertragung benutzerdefinierter Herstellerdatennutzlasten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Query Registry Discovery (T1012)
- **ID:** `T1012.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische Registrierungserkennung, die auf sensible Sicherheitskonfigurationen abzielt.
Anmeldeinformationsspeicher und Persistenzpfade.Verwendet rekursive Abfrageerkennung
und Integritätslevel-Gating, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Laden von Ultra-Pro High-Fidelity BYOVD-Rootkits (T1014)
- **ID:** `T1014.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Technik „Bring Your Own Vulnerable Driver“ (BYOVD).
Konzentriert sich auf die Ausführung bekannter Treiberlader oder die Registrierung des Kernelmodus
Dienste von nicht standardmäßigen Pfaden und filtert gleichzeitig die legitime Wartung von Betriebssystemtreibern heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-System-Netzwerkkonfigurationserkennung (T1016)
- **ID:** `T1016.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung der Netzwerkkonfiguration (IP, Routing, DNS, ARP).
Filtert hochvolumiges Rauschen von VPN-Clients und Systemdiensten mithilfe von Integrität
Ebenen, Gating des übergeordneten Prozesses und Analyse von Befehlszeilenschaltern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Internet-IP-Erkennung (T1016.001)
- **ID:** `T1016_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, die externe IP-Adresse des Systems mithilfe von Befehlszeilentools zu ermitteln
und gängige IP-Echo-Dienste.Minimiert Fehlalarme durch Analyse des Eltern-Kind-Verhältnisses
Prozessbeziehung, Integritätsstufen und typische Fingerabdrücke von Entwicklertools.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Terminal Services Configuration Discovery (T1016.002)
- **ID:** `T1016_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Erkennung von Terminaldiensten und RDP-Konfigurationen.
Konzentriert sich auf nicht standardmäßige Prozesslinien (z. B. Office, Browser) und
Erkennt bestimmte Befehlszeilenschalter, die zur Identifizierung entführerbarer Sitzungen verwendet werden
oder deaktivierte Sicherheitseinstellungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Remote System Discovery (T1018)
- **ID:** `T1018.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische Remote-Systemerkennung mit Schwerpunkt auf der Identifizierung von Domänencontrollern
und Netzwerktopologiekartierung.Filtert lautstarkes Rauschen von Systemdiensten heraus,
Browser und Inventarisierungsagenten mithilfe von Integritätsebenen und übergeordnetem Prozess-Gating.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Automatisierte Exfiltration (T1020)
- **ID:** `T1020.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt automatisierte Exfiltration durch Identifizierung des sequentiellen Musters von
passwortgeschützte Archivierung mit anschließender sofortiger Netzwerkübertragung über
nicht standardmäßige Tools oder Cloud-Sync-Binärdateien von verdächtigen Speicherorten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Client-Linked Cloud Exfil (T1020.001)
- **ID:** `T1020_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Datenexfiltration durch Identifizierung offizieller Cloud-Speicher-Clients
(OneDrive, Dropbox usw.) werden über die Befehlszeile zur Synchronisierung manipuliert
nicht standardmäßige Staging-Verzeichnisse oder die Ausführung mit Argumenten mit hoher Entropie/Skripten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Schnelle Anmeldungen desselben Benutzers an mehreren entfernten Hosts
- **ID:** `T1021.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟡 (medium)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt, dass sich ein einzelner Benutzer innerhalb eines kurzen Zeitfensters erfolgreich bei mehreren verschiedenen Hosts angemeldet hat.Dieses Verhalten kann auf gestohlene Zugangsdaten, Pass-the-Hash oder laterale Bewegung unter Verwendung gültiger Konten hinweisen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**


---
## Verdächtige RDP-Anmeldung aus ungewöhnlicher Quelle
- **ID:** `T1021_001.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟡 (medium)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt erfolgreiche RDP-Anmeldungen, die von ungewöhnlichen oder nicht unternehmensbezogenen Quellen stammen, insbesondere wenn sie auf Server abzielen und von Nicht-Administratorkonten oder selten verwendeten Konten durchgeführt werden.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**


---
## Ultra-Pro High-Fidelity-KMU-Admin-Freigabezuordnung (T1021.002)
- **ID:** `T1021_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Zugriffe auf administrative Freigaben (C$, ADMIN$, IPC$).
native Tools (net.exe, PowerShell) und filtert gleichzeitig Standard-IT heraus
Orchestrierung und Lärm auf Serviceebene.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity DCOM Remote Execution (T1021.003)
- **ID:** `T1021_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [VISIO.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt laterale Bewegungen über DCOM durch Überwachung verdächtiger untergeordneter Prozesse
von bekanntermaßen anfälligen COM-Objekten.Speziell für Headless-Filter
Ausführung und anomale Netzwerk-zu-Prozess-Herkunft.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity SSH Lateral Movement & Tunneling (T1021.004)
- **ID:** `T1021_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [SSH.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt fortgeschrittene seitliche SSH-Bewegungen und Tunneling.Filter legitim
DevOps/Git-Aktivität durch Analyse der Abstammung des übergeordneten Prozesses und der Befehlszeile
Entropie und nicht standardmäßige Authentifizierungsmuster.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity VNC Lateral Movement & Hijacking (T1021.005)
- **ID:** `T1021_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte VNC-Aktivitäten durch Überwachung der tragbaren VNC-Ausführung
von verdächtigen Pfaden, umgekehrten Verbindungsversuchen und der Befehlszeile
Credential-Injection beim Filtern von Remote-Support-Tools für Unternehmen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity WinRM Remote Execution (T1021.006)
- **ID:** `T1021_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt fortgeschrittene laterale Bewegungen über WinRM durch Überwachung auf hohe Entropie
PowerShell-Befehle, In-Memory-Ausführung und verdächtiger Prozess
Hollowing-Versuche, die vom WinRM-Hostprozess ausgehen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Cloud Control Plane Hijacking (T1021.007)
- **ID:** `T1021_007.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt unbefugte seitliche Bewegungen über Cloud-Dashboards durch Korrelation
Hochriskante Vorgänge mit anomalen Benutzeragenten, ungewöhnlichen Quell-IPs usw
Anzeichen einer MFA-Umgehung/automatisierten Sitzungsentführung.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity macOS ARD Remote Hijacking (T1021.008)
- **ID:** `T1021_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt unbefugte Aktivierung oder Änderung von Apple Remote Desktop (ARD)
durch Überwachung des Dienstprogramms „kickstart“ auf Hochrisiko-Flags, die die Gewährung ermöglichen
universeller Zugriff, während legitime MDM-Orchestrierung (Jamf, Kandji) gefiltert wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Wechselmedien-Datendiebstahl (T1025)
- **ID:** `T1025.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische und automatisierte Datenerfassung von Wechselmedien (USB/externe Laufwerke)
durch die Identifizierung rekursiver Erkennungsmuster, spezifischer Archivwechsel usw
verdächtige Prozesslinien und filtert gleichzeitig Standardaktivitäten des Betriebssystems heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtiger Base64-codierter PowerShell-Befehl mit Netzwerkaktivität
- **ID:** `T1027.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt PowerShell-Ausführungen mithilfe von Base64-codierten Befehlen in Kombination mit netzwerkbasiertem Nutzlastabruf und nicht interaktiver Ausführung.Dieses Muster steht in engem Zusammenhang mit der Bereitstellung von Malware, Loadern und Post-Exploitation-Frameworks.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Binary Padding-Aktivität (T1027.001)
- **ID:** `T1027_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt binäres Auffüllen, bei dem Angreifer die Dateigröße erhöhen, um die Sicherheit zu umgehen
scannen oder Hashes ändern.Konzentriert sich auf Tools wie fsutil, dd und Binärkopie
Befehle, die auf ausführbare Dateien in verdächtigen Pfaden abzielen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Software-Verpackungsveranstaltung (T1027.002)
- **ID:** `T1027_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Verwendung von Binärpackern (UPX, MPRESS usw.) in nicht standardmäßigen Umgebungen.
Konzentriert sich auf Befehlszeilenmuster, die für hohe Komprimierung/Verschleierung verwendet werden
verdächtige übergeordnete Prozesslinien.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Steganographie-Nutzlastextraktion (T1027.003)
- **ID:** `T1027_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die programmgesteuerte Extraktion versteckter Nutzlasten aus Bilddateien.
Konzentriert sich auf den Übergang vom Datenzugriff auf Pixelebene (GDI+) zum dynamischen Datenzugriff
Codeausführung (Reflection/IEX) innerhalb desselben Prozesskontexts.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Steganographie-Nutzlastextraktion (T1027.004)
- **ID:** `T1027_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die Extraktion bösartiger Payloads aus Bilddateien mithilfe von
Low-Level-GDI+- oder .NET-Bitmap-Methoden, die häufig in Invoke-PSImage oder ähnlichem vorkommen
Steganographie-Frameworks.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Indikatorentfernung und Signaturdiebstahl (T1027.005)
- **ID:** `T1027_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt Versuche, Indikatoren zu entfernen oder digitale Signaturen auf Binärdateien zu manipulieren.
Konzentriert sich auf Signaturdiebstahl (SigThief), PE-Header-Stripping und String-Ersetzung
an verdächtigen Orten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-HTML-Schmuggelausführung (T1027.006)
- **ID:** `T1027_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung verdächtiger Dateien, die typischerweise über HTML-Schmuggel übermittelt werden.
Konzentriert sich auf Browserprozesse, die Skriptinterpreter erzeugen oder Datenträgerabbilder bereitstellen
aus temporären oder lokalen App-Datenverzeichnissen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Binärsymbol-Stripping (T1027.007)
- **ID:** `T1027_007.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das aktive Entfernen von Debugsymbolen und Abschnittsüberschriften aus Binärdateien.
Konzentriert sich auf die Ausführung von Stripping-Tools auf Nicht-Build-Systemen, um die Forensik zu behindern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Binärsymbol-Stripping (T1027.008)
- **ID:** `T1027_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das aktive Entfernen von Debugsymbolen und Abschnittsüberschriften aus Binärdateien
in Nicht-Entwicklungsumgebungen.Dies behindert forensische Analysen und Reverse Engineering
durch Entfernen von Funktionsnamen und Symboltabellen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Embedded Payload Extraction (T1027.009)
- **ID:** `T1027_009.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [NGEN.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Extraktion und Ausführung eingebetteter Nutzlasten durch Überwachung
verdächtiges Laden von Nur-Speicher-Code (Reflection) und Byte-Array-Manipulation
Ausrichtung auf nicht standardmäßige Ressourcenstandorte.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Befehlszeilenverschleierung (T1027.010)
- **ID:** `T1027_010.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt erweiterte Befehlszeilen-Verschleierungstechniken.Konzentriert sich auf Übermaß
Escape-Zeichendichte, Slicing von Umgebungsvariablen und PowerShell-String
Dekonstruktion zur Umgehung statischer Erkennungsfilter.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Erstellung verdächtiger Archive (T1027.011)
- **ID:** `T1027_011.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MAKECAB.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung passwortgeschützter und/oder verschlüsselter Archive mithilfe gängiger CLI-Tools.
Der Schwerpunkt liegt auf Befehlszeilen-Passwortargumenten und der rekursiven Erfassung sensibler Pfade.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Windows LDR Hijacking (T1027.012)
- **ID:** `T1027_012.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, den Windows Loader (LDR) über AppInit_DLLs oder AppCertDLLs zu kapern.
Es zielt speziell auf DLL-Registrierungen ab, die von Nicht-Systempfaden (Temp, Öffentlich, Benutzerprofile) stammen.
und die Aktivierung des LoadAppInit_DLLs-Flags durch verdächtige Prozesse.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Geplante Ultra-Pro High-Fidelity-Übertragung (T1029)
- **ID:** `T1029.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung geplanter Aufgaben zur automatisierten Datenexfiltration durch
Analysieren von Aufgaben-XML auf verdächtige CLI-Tools, Cloud-Synchronisierungsargumente usw
hochfrequente oder außerhalb der Geschäftszeiten auftretende Auslöser und filtert gleichzeitig legitime Systemaktualisierungen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Daten-Chunking und -Fragmentierung (T1030)
- **ID:** `T1030.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt heimliche Datenfragmentierung zur Exfiltration durch Identifizierung
Dateistream-Manipulation auf niedriger Ebene, benutzerdefinierte pufferbasierte Aufteilung,
und nicht standardmäßige Archiv-Volume-Erstellung aus verdächtigen Ausführungspfaden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Besitzer-/Benutzererkennung für Ultra-Pro-High-Fidelity-Systeme (T1033)
- **ID:** `T1033.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung des aktuellen Benutzers, angemeldeter Benutzer und Token-Berechtigungen.
Konzentriert sich auf anomale Prozesslinien (Office, Browser) und bestimmte Switches
Kombinationen (/priv, /groups), die vor Versuchen zur Rechteausweitung verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Masquerading und Prozesspfadmissbrauch (T1036)
- **ID:** `T1036.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt fortgeschrittene Maskierungstechniken, einschließlich System-Binärpfad-Anomalien,
doppelte Erweiterungen und kritische Systemprozesse, die von nicht vertrauenswürdigen übergeordneten Systemen erzeugt werden.
Optimiert, um legitimes Windows Update- und Seitenladeverhalten herauszufiltern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity ungültige oder gefälschte Code-Signatur (T1036.001)
- **ID:** `T1036_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt kritische Systemprozesse (z. B. lsass, svchost), die mit ungültigen,
nicht vertrauenswürdige oder gefälschte digitale Signaturen.Konzentriert sich auf Identitätssignatur
Nichtübereinstimmungen und Tippfehler des Herausgebers, um Entwicklerlärm zu eliminieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity RTLO-Charakterausführung (T1036.002)
- **ID:** `T1036_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung von Prozessen, die das Right-to-Left Override (RTLO) enthalten.
Unicode-Zeichen (U+202E).Optimiert, um verschiedene Kodierungen zu erkennen und
verdächtige Ausführungskontexte (Downloads, Temp) und filtert gleichzeitig Systemrauschen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity umbenanntes System-Dienstprogramm (T1036.003)
- **ID:** `T1036_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung umbenannter Windows-Systemdienstprogramme (LOLBins) durch Vergleich
aktuelle Prozessnamen mit internen Metadaten.Verwendet pfadbasierte Filterung
und Signaturerkennung, um Fehlalarme von Installateuren zu vermeiden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Masquerading über Path Anomaly (T1036.004)
- **ID:** `T1036_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt ausgefeiltes Masquerading, von dem aus Systembinärdateien ausgeführt werden
nicht vertrauenswürdige, vom Benutzer beschreibbare Verzeichnisse oder aus gefälschten Systempfaden (z. B. Leerzeichenauffüllung).
Filtert legitimes Side-by-Side- (WinSxS) und Windows Update-Verhalten heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Legitime Windows-Binärdatei an einen vom Benutzer beschreibbaren Speicherort kopiert
- **ID:** `T1036_005.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtiges Kopieren legitimer Windows-Systembinärdateien in vom Benutzer beschreibbare Verzeichnisse.Diese Technik wird häufig von Angreifern zur Maskierung, zum Sideloading von DLLs oder zur Umgehung der Ausführung durch Missbrauch vertrauenswürdiger Binärnamen verwendet.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Speicherplatz nach Dateinamenmaskierung (T1036.006)
- **ID:** `T1036_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt absichtliche Maskierung durch nachgestellte Leerzeichen in Dateinamen oder Verzeichnisnamen.
Konzentriert sich auf ausführbare Erweiterungen gefolgt von Leerzeichen, um der stringbasierten Erkennung zu entgehen
Gleichzeitig werden häufig auftretende Windows Update- und SCCM/MECM-Rauschen gefiltert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Doppeldateierweiterungsausführung (T1036.007)
- **ID:** `T1036_007.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung von Binärdateien, die sich über doppelte Erweiterungen als Dokumente ausgeben.
Filtert strikt Entwicklerartefakte (.min.js, .map) und verifizierte Installationsprogramme.
Der Schwerpunkt liegt auf Benutzerverzeichnissen mit hohem Risiko und verdächtigen übergeordneten Abstammungslinien.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Masquerade-Dateityp durch Interpreter-Missbrauch (T1036.008)
- **ID:** `T1036_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung nicht übereinstimmender Dateitypen, wenn legitime Interpreter (wscript, cscript, powershell, regsvr32)
Dateien mit nicht standardmäßigen Erweiterungen ausführen (z. B. .jpg, .txt, .png).
Filtert die Automatisierung auf Systemebene heraus und konzentriert sich auf nicht vertrauenswürdige Benutzerverzeichnisse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Allure Document und RTLO Masquerading (T1036.009)
- **ID:** `T1036_009.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt raffiniertes Maskieren mithilfe von Allure-Dokumenten und RTLO-Zeichen.
Konzentriert sich auf die Ausführung aus nicht vertrauenswürdigen Benutzerverzeichnissen und verdächtigen übergeordneten Verzeichnissen
Prozesse (Browser, E-Mail-Clients) und filtert gleichzeitig allgemeine Entwicklergeräusche.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Persistenz des High-Fidelity-Anmeldeskripts (T1037)
- **ID:** `T1037.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung oder Änderung von Anmeldeskripten in der Registrierung (UserInitMprLogonScript).
Angreifer nutzen dies, um GPO-basierte Anmeldeskripte zu umgehen und bei jeder Anmeldung Schadcode auszuführen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity UserInitMprLogonScript-Persistenz
- **ID:** `T1037_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Erstellung oder Änderung des Registrierungsschlüssels UserInitMprLogonScript.
Dies ist eine High-Fidelity-Regel, da sie Standard-GPO-Updates herausfiltert und sich darauf konzentriert
Vom Benutzer beschreibbare Pfade und verdächtige Ausführungsmuster.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Netsh-Helper-DLL-Persistenz
- **ID:** `T1037_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Registrierung einer neuen Netsh Helper DLL.
Angreifer nutzen dies, um die Persistenz aufrechtzuerhalten, indem sie eine schädliche DLL laden
wann immer netsh.exe oder ein verwandter Netzwerkdienst gestartet wird.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Netzwerk-Anmeldeskript/Verknüpfungsänderung (T1037.003)
- **ID:** `T1037_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)
- **Beschreibung:** Erkennt unbefugte Änderungen an Skripten (.bat, .ps1, .vbs) oder Verknüpfungen (.lnk)
innerhalb sensibler Netzwerkfreigaben wie NETLOGON oder SYSVOL.
Es filtert insbesondere legitime DFS-Replikation und Aktualisierungen auf Systemebene heraus.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro RC-Skript und Init.d-Persistenz (T1037.004)
- **ID:** `T1037_004.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt unbefugte Änderungen an RC-Skripten, init.d- oder systemd-Generatoren durch Prozesse, die nicht zum Paketmanager gehören.
Angreifer nutzen diese, um Root-Persistenz auf Linux-/macOS-Systemen zu erlangen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Persistenz von Ultra-Pro macOS-Startelementen (T1037.005)
- **ID:** `T1037_005.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)
- **Beschreibung:** Erkennt die unbefugte Erstellung von Dateien in älteren StartupItems-Verzeichnissen.
Es minimiert Fehlalarme, indem es das offizielle macOS-Installationsprogramm auf die Whitelist setzt
Subsystem und konzentriert sich auf nicht signierte oder skriptgenerierte Persistenz.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Network Share Discovery (T1039)
- **ID:** `T1039.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Entdeckung und Sammlung sensibler Daten aus Netzwerkfreigaben
durch Identifizieren der rekursiven Dateiaufzählung mithilfe von UNC-Pfaden, kombiniert mit
Ausgabeumleitung oder Massenarchivierung aus nicht standardmäßigen Prozesskontexten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Netzwerk-Sniffing-Erkennung (T1040)
- **ID:** `T1040.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [PKTMON.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes Netzwerk-Sniffing durch Überwachung auf Verwaltungstools
Verwendung im Capture-Modus, Treiberinstallation zum Abfangen von Paketen,
und anstößige Sniffing-Frameworks, die von nicht vertrauenswürdigen Pfaden ausgehen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Exfiltration über C2-Kanal (T1041)
- **ID:** `T1041.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Datenexfiltration über einen etablierten C2-Kanal durch Korrelation
systematische Dateilesevorgänge, Memory-Stream-Codierung und langjährige Erfahrung
ausgehende Netzwerkverbindungen von Nicht-Browser-Prozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Netzwerkdiensterkennung (T1046)
- **ID:** `T1046.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung von Netzwerkdiensten und das Scannen interner Ports.
Konzentriert sich auf schleifenbasierte Scanmuster in PowerShell, CMD und spezialisiert
Binärdateien, die aus Nicht-IT-Administratorkontexten stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Remote-Prozesserstellung über WMIC
- **ID:** `T1047.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Verwendung von wmic.exe zum Erstellen von Prozessen auf Remote-Hosts mithilfe der Methode „Prozessaufruf erstellen“.Diese Technik wird häufig von Angreifern zur seitlichen Bewegung nach der Kompromittierung von Anmeldeinformationen verwendet.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Alternative Protocol Exfiltration (T1048)
- **ID:** `T1048.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Datenexfiltration über nicht standardmäßige Protokolle durch Identifizierung
ungewöhnliche ICMP-Puffergrößen, SSH-/Tunneling-Flags in Nicht-Administratorkontexten,
und netzwerkfähige LoLBins, die über verdächtige Pfade ausgeführt werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Symmetric Encrypted Exfiltration (T1048.001)
- **ID:** `T1048_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [FTP.EXE](https://lolbas-project.github.io/lolbas/), [SFTP.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Exfiltration verschlüsselter Daten durch Identifizierung von SCP/SFTP/Rclone
Nutzung von nicht standardmäßigen Pfaden, mit Schwerpunkt auf automatisierten (nicht interaktiven)
Flags und verdächtige übergeordnete Prozesslinien.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Asymmetrische verschlüsselte Exfiltration (T1048.002)
- **ID:** `T1048_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Datenexfiltration über asymmetrische verschlüsselte Protokolle (HTTPS)
durch die Identifizierung von Befehlszeilentools (Curl, Powershell) mithilfe von Upload-spezifischen
Flags von nicht vertrauenswürdigen Pfaden oder von verdächtigen übergeordneten Prozessen gestartet.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity unverschlüsseltes Protokoll Exfil (T1048.003)
- **ID:** `T1048_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt heimliche Datenexfiltration über DNS und ICMP durch Korrelation
Anomale Nutzlastgrößen und nicht standardmäßige Abfragetypen mit verdächtigen
Prozesslinien und nicht vertrauenswürdige Ausführungspfade.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-System-Netzwerkverbindungserkennung (T1049)
- **ID:** `T1049.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Erkennung aktiver Netzwerkverbindungen und bestehender Sitzungen.
Konzentriert sich auf nicht standardmäßige Prozesslinien (Office, Browser, Webserver) und
Erkennt bestimmte Befehlszeilen-Schalterkombinationen, die von Angreifern zur Zuordnung verwendet werden
der Netzwerklandschaft.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Physical-Medium-Exfiltration (T1052)
- **ID:** `T1052.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische Datenexfiltration auf physische Medien durch Überwachung
nicht interaktive Kopier-/Archivierungsbefehle, die auf Wechseldatenträger-Volumes abzielen,
Herausfiltern legitimer Windows Explorer-GUI-Vorgänge.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity USB-Exfiltration (T1052.001)
- **ID:** `T1052_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische Datenexfiltration auf USB-Geräte durch Überwachung
nicht interaktive Befehle zum Kopieren/Verschieben/Archivieren, die auf Wechseldatenträger abzielen,
Der Schwerpunkt liegt auf verdächtigen Prozessabläufen und versteckten CLI-Argumenten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige geplante Aufgaben- oder Joberstellung aufgrund von Persistenz (T1053).
- **ID:** `T1053.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Erstellung geplanter Aufgaben oder Aufgaben, die zur Datenaufbewahrung über mehrere Betriebssysteme hinweg verwendet werden.Konzentriert sich auf offensive Ausführungsmuster.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochpräzise At.exe-Aktivitätserkennung
- **ID:** `T1053_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung von at.exe zur Aufgabenplanung.Da „at“ veraltet ist,
Jegliche interaktive Nutzung oder Remote-Maschinen-Targeting (\\) gilt als äußerst verdächtig
und weist auf Persistenz oder seitliche Bewegung hin.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Cron-Persistenz und In-Place-Änderung
- **ID:** `T1053_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt durch Überwachung die unbefugte Erstellung oder Änderung von Cron-Jobs
Direktes Schreiben in Cron-Verzeichnisse und verdächtige Shell-Einzeiler.
Filtert legitime Paketmanager und Konfigurationsverwaltungstools.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige geplante Aufgabenerstellung beim Ausführen von PowerShell
- **ID:** `T1053_005.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die verdächtige Erstellung geplanter Aufgaben mithilfe von schtasks.exe, die PowerShell ausführen und häufig von Angreifern missbraucht werden, um eine Persistenz oder verzögerte Ausführung bösartiger Payloads herzustellen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erstellung oder Änderung eines High-Fidelity-Systemd-Dienstes
- **ID:** `T1053_006.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die Erstellung oder Änderung von systemd-Diensteinheiten mit Schwerpunkt auf
anormale Ausführungspfade (z. B. /tmp, /dev/shm) und verdächtige übergeordnete Prozesse
(z. B. Shells, Webserver).Filtert legitime Paketverwaltungs- und CM-Tools heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Systemd-Timer-Persistenzerkennung
- **ID:** `T1053_007.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die Erstellung oder Aktivierung von Systemd-Timern, die für die Persistenz verwendet werden.
Konzentriert sich auf nicht standardmäßige Verzeichnisspeicherorte (Einheiten auf Benutzerebene) und interaktive Shell
Auslöser und verdächtige Ausführungsnutzlasten (Verschleierung, Netzwerk-Tools).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Stealthy-Prozessinjektionserkennung (T1055)
- **ID:** `T1055.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt erweiterte Prozessinjektionen (z. B. DLL-Injection, Thread-Hijacking) durch
Überwachung auf bestimmte GrantedAccess-Masken mit hohem Risiko in Kombination mit
verdächtige Quelle-Ziel-Beziehungen und nicht gesicherte Speicherbereiche.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy DLL-Injektion (T1055.001)
- **ID:** `T1055_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die High-Fidelity-DLL-Injektion durch Identifizierung der Remote-Thread-Erstellung
Dabei ist die Startadresse eine bekannte Bibliotheksladefunktion oder die Quelle
Der Speicherbereich wird nicht durch eine Datei auf der Festplatte gesichert (nicht gesicherter Speicher).

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy PE-Injektion (T1055.002)
- **ID:** `T1055_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt High-Fidelity-PE-Injection durch Identifizierung des prozessübergreifenden Speichers
Manipulation, bei der die Quelle des Aufrufs ein nicht gesicherter Speicherbereich ist
(Shellcode) und das Ziel ist ein kritischer Systemprozess.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy Thread Hijacking (T1055.003)
- **ID:** `T1055_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Thread-Ausführungs-Hijacking durch Identifizierung prozessübergreifender Zugriffe
Anfragen mit Thread-Manipulationsrechten (SET_CONTEXT), bei denen die
Der aufrufende Stack stammt aus dem nicht gesicherten Speicher (Shellcode).

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy APC-Injektion (T1055.004)
- **ID:** `T1055_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Hi-Fi-APC-Injektionsversuche (einschließlich Early Bird) durch Überwachung
spezifische Thread-Zugriffsmasken (THREAD_SET_CONTEXT), aus denen der aufrufende Code stammt
aus nicht gesicherten oder nicht vertrauenswürdigen Speicherbereichen (CallTrace-Analyse).

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy TLS-Injektion (T1055.005)
- **ID:** `T1055_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt High-Fidelity-TLS-Injection durch Überwachung des prozessübergreifenden Speichers
Manipulation, die auf PE-Header abzielt, von denen der Ausführungsfluss stammt
aus ungesichertem Speicher (Shellcode).

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy Ptrace-Injektion (T1055.008)
- **ID:** `T1055_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochpräzise Ptrace-basierte Prozessinjektionen durch Identifizierung
PTRACE_POKETEXT/DATA-Vorgänge aus verdächtigen Quellen oder
Benutzerübergreifende Ptrace-Anhänge, die legitime Debugger herausfiltern.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Überschreiben des Ultra-Pro-Stealthy-Moduls (T1055.009)
- **ID:** `T1055_009.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das Überschreiben von Prozessen oder Modulen durch Identifizierung prozessübergreifender Zugriffe
Anfragen mit VM_WRITE-Berechtigungen, von denen der aufrufende Stack stammt
nicht gesicherter Speicher (Shellcode) statt eines signierten On-Disk-Moduls.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy EWM-Injektion (T1055.011)
- **ID:** `T1055_011.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Einschleusung von Extra Window Memory (EWM) durch Überwachung auf verdächtige Daten
Prozessübergreifender Zugriff mit Speichermanipulationsrechten bei CallTrace
Zeigt die Ausführung aus nicht gesichertem Speicher (Shellcode) an, die auf GUI-Prozesse abzielt.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy Process Hollowing (T1055.012)
- **ID:** `T1055_012.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt High-Fidelity Process Hollowing durch Identifizierung prozessübergreifender Zugriffe
Anfragen mit VM_WRITE/VM_OPERATION-Berechtigungen an den aufrufenden Stack
stammt aus ungesichertem Speicher (Shellcode) und zielt auf häufige Opferprozesse ab.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy Process Hollowing (T1055.013)
- **ID:** `T1055_013.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt High-Fidelity Process Hollowing durch Identifizierung prozessübergreifender Zugriffe
Anfragen mit VM_WRITE/VM_OPERATION-Berechtigungen an den aufrufenden Stack
stammt aus ungesichertem Speicher (Shellcode) und zielt auf häufige Opferprozesse ab.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy Process Ghosting (T1055.014)
- **ID:** `T1055_014.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Prozess-Ghosting durch Identifizierung von Prozesserstellungsereignissen, bei denen dies der Fall ist
Die zugrunde liegende Datei befindet sich im Status „Löschen steht aus“, was durch fehlende Hashes belegt wird
zur Ausführungszeit und stammen aus nicht standardmäßigen Verzeichnissen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy ListPlanting-Injektion (T1055.015)
- **ID:** `T1055_015.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die ListPlanting-Injection durch Identifizierung verdächtiger prozessübergreifender Zugriffe
Anfragen an ListView-fähige Prozesse, von denen der Ausführungsfluss stammt
aus nicht gesicherten Speicherbereichen (Shellcode) und nicht aus signierten Modulen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Eingangserfassungserkennung (T1056)
- **ID:** `T1056.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt anspruchsvolle Eingabeerfassung (Keylogging) durch Identifizierung verdächtiger Eingaben
API-bezogene Befehlszeilen, nicht autorisierte Shell-basierte Keylogging-Snippets,
und anomales Prozessverhalten, das auf Benutzereingaben abzielt.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelles High-Fidelity-Keylogging und Input-Hooking (T1056.001)
- **ID:** `T1056_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt erweitertes Keylogging, indem verdächtige API-Aufrufe von unprivilegierten Personen identifiziert werden
oder kurzlebige Prozesse, die auf die Verwendung von SetWindowsHookEx und GetAsyncKeyState abzielen
innerhalb nicht standardmäßiger Ausführungskontexte (z. B. PowerShell, Rundll32).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-GUI-Eingabeerfassung (T1056.002)
- **ID:** `T1056_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, Anmeldeinformationen durch irreführende GUI-Eingabeaufforderungen oder Overlays zu erfassen.
Konzentriert sich auf PowerShell/C#-Snippets, die modale Dialoge aus verdächtigen übergeordneten Elementen erstellen
Prozesse (Browser, Office-Apps) und nicht gesicherte Skripte.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Digitalzertifikat-Diebstahl (T1056.003)
- **ID:** `T1056_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Entnahme privater Schlüssel und digitaler Zertifikate.
Überwacht die Extraktion „nicht exportierbarer“ Schlüssel über Speicher-Patching,
verdächtige Verwendung von certutil/PowerShell zur PFX-Erstellung und direkt
Zugriff auf den kryptografischen Schlüsselspeicher von Windows.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtiges Einbinden der Anmeldeinformations-API über Win32-Bibliotheken
- **ID:** `T1056_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Prozesse, die Kombinationen von Win32-Bibliotheken laden, die häufig zum Abfangen von Anmeldeinformationen oder zum API-Hooking missbraucht werden, z. B. user32.dll, advapi32.dll und win32u.dll.Die Regel konzentriert sich auf systemfremde, vom Benutzer beschreibbare Ausführungspfade und schließt gängige legitime Software aus, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Prozesserkennung (T1057)
- **ID:** `T1057.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Prozesserkennung mit Schwerpunkt auf der Identifizierung von Sicherheitsprodukten
und Erinnerungszielaufklärung.Filtert hochfrequente Geräusche aus
Browser und legitime Update-Orchestratoren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Kontextuelle Anomalie des High-Fidelity-Scripting-Interpreters
- **ID:** `T1059.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige PowerShell- oder CMD-Ausführungen durch korrelierende Shell-Interpreter
mit hochriskanten übergeordneten Prozessen (Office, Browser, Webserver) und Verschleierungstechniken.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige verschlüsselte PowerShell-Befehlsausführung
- **ID:** `T1059_001.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Ausführungen von PowerShell mithilfe codierter Befehle in Kombination mit Ausführungsumgehungs- oder Verschleierungsflags.Diese Technik wird häufig von Angreifern verwendet, um der Erkennung zu entgehen und bösartige Nutzlasten im Speicher auszuführen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-AppleScript-Missbrauchserkennung (Osascript).
- **ID:** `T1059_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt verdächtige Osascript-Ausführungen durch Überwachung auf „Do Shell Script“-Escapes,
Base64-codierte Nutzlasten und Ausführung, die von nicht vertrauenswürdigen übergeordneten Prozessen stammt
wie Browser oder E-Mail-Clients.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte Kontextanomalie der Windows-Befehlsshell
- **ID:** `T1059_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige cmd.exe-Ausführungen durch Korrelation riskanter übergeordneter Prozesse
(Webserver, Office, SQL) mit anomalen Befehlszeilenmustern wie
Befehlsverkettung und -erkennung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Unix-Shell-Missbrauch und Reverse-Shell-Erkennung
- **ID:** `T1059_004.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt verdächtige Unix-Shell-Ausführungen durch Überwachung auf Befehlsinjektion
von Webprozessen, umgekehrter Shell-Socket-Umleitung und dateilosen Pipe-to-Shell-Mustern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochpräzise kontextbezogene Anomalieerkennung mit VBScript
- **ID:** `T1059_005.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [PUBPRN.VBS](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige VBScript-Ausführungen durch Filterung legitimer Betriebssystemverwaltungsskripts
und Konzentration auf riskante übergeordnete Prozesse, ungewöhnliche Dateispeicherorte usw
gängige Verschleierungs-/Downloadmuster, die bei der Verbreitung von Malware verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Python-Interpreter-Missbrauchserkennung
- **ID:** `T1059_006.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt verdächtige Python-Ausführungsmuster und konzentriert sich dabei auf einzeilige Reverse-Shells.
interaktive Shell-Upgrades und Ausführung, die von einer risikoreichen Netzwerkverbindung ausgehen
übergeordnete Prozesse (Webserver, SQL).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Kontextuelle Anomalie des High-Fidelity-JScript-Interpreters
- **ID:** `T1059_007.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige JScript-Ausführungen durch Korrelation von wscript/cscript mit
riskante übergeordnete Prozesse, nicht vertrauenswürdige Dateispeicherorte und Befehlszeilenargumente
Wird normalerweise zur Verschleierung oder zum Remote-Abruf von Nutzdaten verwendet.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## CLI-Manipulation von High-Fidelity-Netzwerkgeräten
- **ID:** `T1059_008.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Kritisch hoch (SIEM-Killerkategorie!)
- **Beschreibung:** Erkennt kritische, nicht autorisierte Konfigurationsänderungen auf Netzwerkgeräten.
Schwerpunkt auf Anti-Forensik (Deaktivieren von Protokollen), Offenlegung von Anmeldeinformationen,
und unbefugte Datenexfiltration (Konfigurationsexport).

#### 🚨 Reaktions-Playbook
1. **IP-Reputation: Überprüfen Sie die Remote-IP-Adresse in Reputationsdatenbanken.**
2. **Verkehrsanalyse: Untersuchen Sie die Menge der gesendeten Daten.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Cloud-Shell-Ausnutzung und Datenexfiltration
- **ID:** `T1059_009.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt nicht autorisierte oder böswillige Aktivitäten in Cloud Shell-Umgebungen.
Der Schwerpunkt liegt auf Identitätsdiebstahl, Protokollunterdrückung und der Umwandlung privater Daten
Cloud-Ressourcen öffentlich zugänglich machen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtiger SYSTEM-Prozess, der aus dem Benutzerkontext hervorgegangen ist
- **ID:** `T1068.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Prozesse, die als SYSTEM ausgeführt werden und von benutzerinitiierten übergeordneten Prozessen wie Explorer, Browsern oder Office-Anwendungen erzeugt werden.Dieses Verhalten kann auf eine Rechteausweitung, eine Token-Manipulation oder eine Ausnutzung der UAC-Umgehung hinweisen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Berechtigungsgruppenerkennung (T1069)
- **ID:** `T1069.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung lokaler oder domänenbezogener Berechtigungsgruppen.
Konzentriert sich auf Aufklärungsmuster zur Identifizierung privilegierter Konten
Gleichzeitig werden legitime System-/Inventarstörungen durch Integritäts- und übergeordnete Analyse herausgefiltert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Local Group Discovery (T1069.001)
- **ID:** `T1069_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte lokale Gruppenaufklärung mit Schwerpunkt auf privilegierten Konten
(Administratoren, RDP).Filtert legitimes System-/Inventarrauschen heraus
durch Integrity Level Gating und Parent-Process-Korrelation.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Domänengruppenerkennung (T1069.002)
- **ID:** `T1069_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung von AD-Domänengruppen mit Schwerpunkt auf Aufklärungstools
(BloodHound, AdFind) und verdächtige PowerShell-Muster.Verwendet die Integritätsstufe
und Prozessherkunft, um Fehlalarme von Administrator-Workstations zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Cloud Groups Discovery (T1069.003)
- **ID:** `T1069_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die systematische Entdeckung von Wolkengruppen durch die Identifizierung von Massenaufklärungsmustern.
atypische Benutzeragenten und Erweiterung sensibler Gruppeneigenschaften.
Entwickelt, um CSPM- und IaC-Dienstprinzipale mit hohem Volumen herauszufiltern.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Entfernung des Ultra-Pro High-Fidelity-Indikators auf dem Host (T1070)
- **ID:** `T1070.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [FSUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Versuche, Windows-Ereignisprotokolle und hochwertige forensische Artefakte zu löschen
(USN Journal, Prefetch).Konzentriert sich auf nicht standardmäßige und spezifische Ausführungsketten
Clearing sicherheitsrelevanter Anbieter.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Sicherheitsereignisprotokoll mit wevtutil.exe gelöscht
- **ID:** `T1070_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, das Windows-Sicherheitsereignisprotokoll mithilfe von wevtutil.exe zu löschen, einer häufigen Angreifertechnik, die zum Verwischen von Spuren nach Anmeldeinformationszugriff, lateraler Bewegung oder Persistenz verwendet wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Linux-Protokolllöschung und Journalsabotage (T1070.002)
- **ID:** `T1070_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt gezielte Versuche, Linux-Systemprotokolle und Journalpuffer zu löschen oder zu kürzen.
Konzentriert sich auf manuelle Befehlszeilenmuster, Shell-Umleitung auf Protokolldateien usw
Staubsaugen von Systemd-Journalen außerhalb automatisierter Wartungsfenster.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Mailbox-Datenlöschung und Regelsabotage (T1070.003)
- **ID:** `T1070_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das systematische Entfernen von Postfachdaten und die Erstellung schädlicher Posteingangsregeln.
Der Schwerpunkt liegt auf Massenlösch-Cmdlets und automatisierten Regelsätzen zur Unterdrückung
Sicherheitsbenachrichtigungen oder die Angreiferkommunikation verbergen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity forensische Artefakt- und Dateilöschung (T1070.004)
- **ID:** `T1070_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CIPHER.EXE](https://lolbas-project.github.io/lolbas/), [FSUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Zerstörung hochwertiger forensischer Artefakte (USN Journal, Prefetch, Amcache)
und die Verwendung von Secure Wipe-Dienstprogrammen.Konzentriert sich auf nicht standardmäßige Prozessursprünge und
Umgehungstechniken, die eingesetzt werden, um eine Wiederherstellung nach einem Vorfall zu verhindern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Netzwerkfreigabe und Entfernung von Anmeldeinformationen (T1070.005)
- **ID:** `T1070_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CMDKEY.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das systematische Entfernen von Netzwerkfreigaben und gespeicherten Anmeldeinformationen mithilfe von Platzhaltern
Lösch- und Force-Flags.Unterscheidet zwischen manueller Benutzeraktivität und
automatisierte anti-forensische Bereinigung nach seitlicher Bewegung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Timestomp und MACE-Attributmanipulation (T1070.006)
- **ID:** `T1070_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, Dateizeitstempel (MACE-Attribute) zu ändern, um einer forensischen Analyse zu entgehen.
Konzentriert sich auf die direkte Manipulation von Objekteigenschaften in PowerShell und ist spezialisiert
Anti-Forensik-Dienstprogramme, während legitimes Installationsverhalten herausgefiltert wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Netzwerkverlauf und RDP-Trace-Entfernung (T1070.007)
- **ID:** `T1070_007.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Versuche, den Netzwerkverbindungsverlauf zu löschen, wobei der Schwerpunkt auf RDP liegt
MRU-Listen des Terminalserver-Clients und Entfernung von Netzwerkfreigabe-Metadaten.
Filtert gängige Helpdesk-Fehlerbehebungen (DNS-Flush) heraus, sofern sie nicht Teil eines umfassenderen Angriffs sind.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-E-Mail-Speicherung und Datenbankvernichtung (T1070.008)
- **ID:** `T1070_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Zerstörung von E-Mail-Speicher (PST/OST) und Exchange-Datenbanken (EDB).
Der Schwerpunkt liegt auf der programmgesteuerten Löschung, dem Aufheben der Bereitstellung von Datenbanken und der forensischen Löschung
Muster aus nicht vertrauenswürdigen Prozessen oder verdächtigen Eltern-Kind-Ketten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Entfernung von Persistenzartefakten (T1070.009)
- **ID:** `T1070_009.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Entfernung von Persistenzmechanismen (geplante Aufgaben, Dienste, WMI)
Der Schwerpunkt liegt auf erzwungenen Löschmustern und verdächtigen Prozessabläufen.
Filtert gängige Software-Update-Zyklen und MSI-Installationsgeräusche heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Anwendungsschicht-C2-Anomalie (T1071)
- **ID:** `T1071.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Kritisch hoch (SIEM-Killerkategorie!)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielle C2-Kommunikation durch Identifizierung anomaler Netzwerkverbindungen
Initiiert durch Nicht-Browser-Prozesse, Schwerpunkt auf Bibliotheksladungen (WinInet/WinHTTP)
und verdächtige Eltern-Kind-Beziehungen.

#### 🚨 Reaktions-Playbook
1. **IP-Reputation: Überprüfen Sie die Remote-IP-Adresse in Reputationsdatenbanken.**
2. **Verkehrsanalyse: Untersuchen Sie die Menge der gesendeten Daten.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity HTTP/S C2-Anomalie (T1071.001)
- **ID:** `T1071_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Kritisch hoch (SIEM-Killerkategorie!)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielle C2-Kommunikation über HTTP/S durch Identifizierung von Anomalien
Netzwerkverbindungen von Prozessen, denen es typischerweise an Netzwerklogik mangelt,
oder Anzeichen von Prozessaushöhlung und verdächtiger Eltern-Kind-Abstammung aufweisen.

#### 🚨 Reaktions-Playbook
1. **IP-Reputation: Überprüfen Sie die Remote-IP-Adresse in Reputationsdatenbanken.**
2. **Verkehrsanalyse: Untersuchen Sie die Menge der gesendeten Daten.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity FTP/SFTP-Protokollanomalie (T1071.002)
- **ID:** `T1071_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Kritisch hoch (SIEM-Killerkategorie!)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Nutzung von Dateiübertragungsprotokollen durch Überwachung
nicht interaktive FTP/SFTP-Sitzungen, verdächtige skriptbasierte Übertragungen,
und anomale Eltern-Kind-Prozessbeziehungen (z. B. Office zu FTP).

#### 🚨 Reaktions-Playbook
1. **IP-Reputation: Überprüfen Sie die Remote-IP-Adresse in Reputationsdatenbanken.**
2. **Verkehrsanalyse: Untersuchen Sie die Menge der gesendeten Daten.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomalie des Ultra-Pro High-Fidelity-Mail-Protokolls (T1071.003)
- **ID:** `T1071_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Kritisch hoch (SIEM-Killerkategorie!)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGEWEBVIEW2.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte E-Mail-basierte C2- oder Exfiltrationsvorgänge durch direkte Identifizierung
Mail-Protokoll-Verbindungen (SMTP, IMAP, POP3) von Nicht-Mail-Prozessen,
Schwerpunkt auf .NET/PowerShell-Automatisierung und verdächtigen Prozesslinien.

#### 🚨 Reaktions-Playbook
1. **IP-Reputation: Überprüfen Sie die Remote-IP-Adresse in Reputationsdatenbanken.**
2. **Verkehrsanalyse: Untersuchen Sie die Menge der gesendeten Daten.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelles High-Fidelity-DNS-Tunneling und -Beaconing (T1071.004)
- **ID:** `T1071_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt DNS-Tunneling und C2 durch Überwachung auf Subdomänen mit hoher Entropie.
ungewöhnliche Abfragetypen (TXT, NULL) und DNS-Aktivität von Nicht-Netzwerk
native Prozesse mit besonderem Fokus auf Länge und Häufigkeit.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erkennung von Missbrauch durch High-Fidelity-Softwarebereitstellungstools
- **ID:** `T1072.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch von Softwarebereitstellungsagenten zur Ausführung bösartiger Payloads.
Konzentriert sich auf anomale untergeordnete Prozesse (PowerShell, BitsAdmin, CertUtil), die erzeugt wurden
durch Bereitstellungsdienste, Herausfiltern von Standardwartungsmustern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Daten-Staging-Anomalie (T1074)
- **ID:** `T1074.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MAKECAB.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das Staging von Daten durch die Identifizierung anomaler Dateiaggregationsmuster.
Archivwechsel mit geringer Komprimierung und Massenkopiervorgänge
versteckte oder temporäre Systemverzeichnisse von nicht vertrauenswürdigen Shells.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Local Data Staging-Anomalie (T1074.001)
- **ID:** `T1074_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MAKECAB.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematisches lokales Daten-Staging durch die Identifizierung einer anomalen Dateiaggregation
Muster, bestimmte Archivierungsschalter mit geringer Komprimierung oder Passwortschutz,
und Massenkopiervorgänge aus nicht vertrauenswürdigen Kontexten in versteckte Systemverzeichnisse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Remote Data Staging (T1074.002)
- **ID:** `T1074_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Remote-Datenbereitstellung durch die Identifizierung anomaler Massendateibewegungen
interne UNC-Pfade, gefolgt von Archivierungsbefehlen mit geringer Komprimierung/Verschlüsselung
Flags, die aus nicht vertrauenswürdigen Prozesslinien stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomale High-Fidelity-Anmeldung über ein gültiges Konto
- **ID:** `T1078.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt erfolgreiche Anmeldungen mit gültigen Konten, die anomale Merkmale aufweisen.
B. ungewöhnliche Anmeldetypen für Dienstkonten oder Anmeldungen mit anschließender sofortiger Anmeldung
sensible Befehlsausführung.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Standard-Kontomissbrauchserkennung
- **ID:** `T1078_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt erfolgreiche Anmeldungen mit bekannten Standardkontonamen (Administrator, Gast, Root)
von nicht standardmäßigen Netzwerkstandorten oder über interaktive Remote-Sitzungen (RDP) stammen.
Filtert allgemeines lokales Systemrauschen und interne Automatisierung heraus.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomalie der seitlichen Bewegung des High-Fidelity-Domänenkontos
- **ID:** `T1078_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt anomale RDP- oder Netzwerkanmeldungen bei kritischer Infrastruktur (DCs, SQL, Dateiserver)
stammen aus nicht autorisierten Quellsubnetzen oder Benutzerkonten ohne Administratorrechte.
Implementiert eine strenge Filterung für Maschinenkonten und bekannte Jump-Server.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Fernzugriffserkennung für lokale Konten
- **ID:** `T1078_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt erfolgreiche Remote-Anmeldungen (RDP, SMB, WinRM) über lokale Konten.
In einer Domänenumgebung sollten lokale Konten nur für die lokale Konsole verwendet werden
Zugang.Die Remote-Nutzung ist ein starker Indikator für Lateral Movement oder Zugangsdatendiebstahl.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Kompromittierung eines High-Fidelity-Cloud-Kontos (Entra-ID)
- **ID:** `T1078_004.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt erfolgreiche Cloud-Anmeldungen, die Hochrisikoindikatoren aufweisen:
MFA-Umgehung bei privilegierten Konten, unmögliche Reisemuster,
oder die Verwendung nicht standardmäßiger Automatisierungs-Benutzeragenten durch menschliche Konten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Taint Shared Content (T1080)
- **ID:** `T1080.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, freigegebene Inhalte zu manipulieren, indem es auf verdächtige Inhalte überwacht
Prozess-zu-Dateifreigabe-Interaktionen mit Schwerpunkt auf makrofähigen Vorlagen,
Shortcut-Hijacking und Binärersetzung auf UNC-Pfaden.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Systeminformationserkennung (T1082)
- **ID:** `T1082.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung von Systeminformationen (Betriebssystem, Patches, Architektur)
Der Schwerpunkt liegt auf der Aufklärung zur Exploit-Auswahl.Filtert laute Geräusche
von Inventaragenten und Browsern mithilfe von Integritätsstufen und übergeordnetem Prozess-Gating.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Datei- und Verzeichniserkennung (T1083)
- **ID:** `T1083.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Datei- und Verzeichniserkennung mit Schwerpunkt auf der Erfassung sensibler Daten.
Filtert durch Analyse legitime Systemindizierungen, AV-Scans und Entwickleraktivitäten heraus
Prozessintegrität, Eltern-Kind-Beziehungen und spezifische Schlüsselwortmuster.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Verwendung von Net User oder Net Localgroup über cmd.exe
- **ID:** `T1087.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die verdächtige Verwendung von cmd.exe zur Ausführung von Net User- oder Net Localgroup-Befehlen, die häufig von Angreifern zur Kontoerkennung oder zur Rechteausweitung verwendet werden.Die Regel konzentriert sich auf einen angreiferähnlichen Ausführungskontext, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Local Account Discovery (T1087.001)
- **ID:** `T1087_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Aufzählung lokaler Konten und Gruppen.
Konzentriert sich auf anomale Prozessabläufe (z. B. von Webservern gestartete Erkennungstools oder
Remote-Shells) und die Verwendung moderner Aufzählungsmethoden wie WMI/CIM.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Domänenkontoerkennung (T1087.002)
- **ID:** `T1087_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt eine systematische Active Directory-Aufzählung mit Schwerpunkt auf anstößigen LDAP-Filtern
und nicht standardmäßige Prozesslinien.Filtert legitimes Verwaltungsverhalten
durch den Ausschluss bekannter Dienstkonten und Verwaltungstools.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-E-Mail-Kontoerkennung (T1087.003)
- **ID:** `T1087_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung von E-Mail-Konten und globalen Adresslisten (GAL).
Konzentriert sich auf nicht interaktive PowerShell-Sitzungen, den Massenexport von Empfängern,
und anormaler Zugriff auf lokale E-Mail-Profilkonfigurationen durch nicht vertrauenswürdige Prozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Cloud-Kontoerkennung (T1087.004)
- **ID:** `T1087_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung von Cloud-Konten (AWS, Azure, GCP) mit Schwerpunkt auf
interaktive Shell-Sitzungen und anomale Befehlsverkettung.Filter legitim
CI/CD- und Automatisierungs-Workloads basierend auf Prozessherkunft und Benutzerkontext.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessioneller High-Fidelity-Proxy und Pivot-Punkt-Erkennung (T1090)
- **ID:** `T1090.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung von Netzwerk-Proxys und Port-Weiterleitungsregeln durch Korrelation
Hochriskante native Binärdateien (Netsh) mit Pivot-spezifischen Argumenten, die zugeordnet werden können
externe Überwachungsports zu internen Netzwerkressourcen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Interner Proxy und Pivot-Erkennung (T1090.001)
- **ID:** `T1090_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt interne Netzwerk-Pivotisierung durch Identifizieren der Konfiguration von
Portweiterleitung an private RFC 1918-IP-Adressen von Nicht-Systemadressen
Prozesse, ausgenommen legitime lokale Virtualisierung und Containerverkehr.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Profi-externer High-Fidelity-Proxy und Tunneling (T1090.002)
- **ID:** `T1090_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Verwendung nicht standardmäßiger externer Proxys durch Identifizierung hartcodierter Proxys
Anmeldeinformationen, benutzerdefinierte PAC-Dateien oder Proxy-Überschreibungen in Binärdateien mit hohem Risiko
von interaktiven oder Skript-Interpretern gestartet.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Multi-Hop-Proxy- und Tor-Erkennung (T1090.003)
- **ID:** `T1090_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Multi-Hop-Proxy- und Tor-Schaltkreise durch Identifizierung von Unbefugten
Proxy-Verkettungstools oder versteckte Tor-Clients, die von nicht standardmäßigen Geräten ausgeführt werden
Verzeichnisse, wobei der Schwerpunkt auf der Manipulation von Steuerports und der SOCKS5-Verkettung liegt.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Domain Fronting Detection (T1090.004)
- **ID:** `T1090_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Domänen-Fronting durch Identifizierung manueller HTTP-Host-Header-Überschreibungen
innerhalb der Befehlszeilenargumente gängiger webfähiger LoLBins,
zielt speziell auf die CDN-gestützte Infrastrukturumleitung ab.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Prozessausführung von Wechselmedien
- **ID:** `T1091.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SHELL32.DLL](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung von Skriptinterpretern und LOLBins von Nicht-Systemlaufwerken.
Konzentriert sich auf Muster, die von Würmern (wie Raspberry Robin) und manuellen USB-basierten Mustern verwendet werden
Angriffe, während gängige tragbare Anwendungen herausgefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Wechselmedien C2-Anomalie (T1071.002 / T1092)
- **ID:** `T1092.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes C2 oder Daten-Staging über Wechselmedien durch Identifizierung
nicht interaktive Prozesse, die auf versteckte/Systemdateien auf USB-Volumes zugreifen,
Der Schwerpunkt liegt auf der automatisierten Skriptausführung und dem Missbrauch von Alternate Data Stream (ADS).

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Non-Application Layer C2 (T1095)
- **ID:** `T1095.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt benutzerdefinierte C2-Kommunikation über unformatierte TCP/UDP-Sockets durch Identifizierung
die Instanziierung von Low-Level-NetworkStreams und manuellem Byte-Array
Puffermanipulation, gefolgt von Socket-Schreibvorgängen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Kontomanipulation – auf Persistenz ausgerichtet
- **ID:** `T1098.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt verdächtige und seltene Änderungen an Benutzerkontoattributen
stark mit Beharrlichkeit und Privilegieneskalation verbunden, wie z
SID-Verlaufsinjektion, Änderungen der eingeschränkten Kerberos-Delegierung und
Deaktivieren des Kennwortablaufs für vertrauliche Konten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Entra-ID-Anwendungszugangsberechtigungszusatz
- **ID:** `T1098_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt, wenn einer Entra ID-Anwendung ein neues Geheimnis oder Zertifikat hinzugefügt wird.
Angreifer nutzen dies, um über Service Principals eine Hintertür einzurichten.
Diese Regel filtert gängige Erstanbieter-Apps von Microsoft und bekannte CI/CD-Dienstprinzipale heraus.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Berechtigungsgewährung für High-Fidelity-Exchange-Postfächer (T1098.002)
- **ID:** `T1098_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die Erteilung kritischer Postfachberechtigungen (FullAccess, SendAs).
Filtert allgemeine Dienstkonten heraus und konzentriert sich auf mandantenübergreifende oder
unbefugte Verwaltungsmaßnahmen, insbesondere bei hochwertigen Zielen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Zusätzliches High-Fidelity-Entra-ID-App-Zertifikat
- **ID:** `T1098_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt das Hinzufügen eines neuen Zertifikats (öffentlicher Schlüssel) zu einer Entra ID-Anwendung.
Angreifer nutzen dies für eine langfristige Persistenz, um als Dienstprinzipal der Anwendung zu fungieren.
Diese Regel ist optimiert, um automatisierte interne Microsoft-Rotationen und bekannte CI/CD-Anbieter herauszufiltern.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochpräzise Eskalation der Azure-Rollenzuweisung
- **ID:** `T1098_004.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die direkte Zuweisung hochprivilegierter Azure-Rollen (Besitzer, Mitwirkender, Benutzerzugriffsadministrator).
Filtert PIM-Aktivierungen (Privileged Identity Management) und bekannte Automatisierungsprinzipale heraus
um Lärm zu reduzieren und sich auf die manuelle Rechteausweitung zu konzentrieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Persistenz der High-Fidelity-Geräteregistrierung (T1098.005)
- **ID:** `T1098_005.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt verdächtige Geräteregistrierungen in Entra ID.Angreifer registrieren ihre eigenen Geräte
um Richtlinien für bedingten Zugriff zu umgehen, die einen „registrierten“ Gerätestatus erfordern.
Diese Regel filtert verwaltete Registrierungen heraus und konzentriert sich auf nicht verwaltete oder skriptgesteuerte Registrierungen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ergänzung der High-Fidelity-MFA-Methode
- **ID:** `T1098_006.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt, wenn eine neue MFA-Methode von einem nicht vertrauenswürdigen Speicherort zu einem Benutzerkonto hinzugefügt wird
oder ohne eine neue MFA-Herausforderung.Dies ist eine primäre Persistenztechnik für Angreifer
um den Zugriff nach einer anfänglichen Kontokompromittierung aufrechtzuerhalten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Web Service C2 (T1102)
- **ID:** `T1102.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt C2-Kommunikation über legitime Cloud-Dienste durch Identifizierung
Roh-API oder Rohinhalts-Subdomains, auf die von Nicht-Browser-LoLBins zugegriffen wird,
Skriptinterpreter oder Binärdateien, die von verdächtigen Pfaden ausgeführt werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Dead Drop Resolver (T1102.001)
- **ID:** `T1102_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Verwendung von Dead-Drop-Resolvern durch Identifizierung des Rohinhaltsabrufs
von sozialen/Code-Plattformen, insbesondere Filterung nach verdächtigem Eltern-Kind
Beziehungen und nicht standardmäßige Download-Methoden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Bidirektional Cloud C2 (T1102.002)
- **ID:** `T1102_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt interaktive C2-Kommunikation über Cloud-APIs durch Identifizierung
spezifische Schreib-/Lesemethoden (POST/GET), die von Nicht-Browser-LoLBins ausgegeben werden
oder Binärdateien, die von verdächtigen Pfaden laufen, mit Ausnahme offizieller Clients.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity One-Way Web Service C2 (T1102.003)
- **ID:** `T1102_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unidirektionale C2- oder Datenexfiltration über Cloud-Dienste durch Korrelation
Spezifische API-Upload-/Download-Methoden mit nicht standardmäßigen Prozessspeicherorten
und verdächtige übergeordnete Prozesslinien.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Multi-Stage C2 (T1104)
- **ID:** `T1104.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt mehrstufige C2-Kommunikation durch Identifizierung dateiloser Ausführungsmuster
Dabei wird das Ergebnis einer Netzwerkanforderung direkt an die Speicherlast weitergeleitet
Funktionen oder Skriptauswertungen ohne Zwischenschreibvorgänge auf der Festplatte.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Verwendung integrierter Windows-Tools zum Herunterladen von Dateien und zur Codeausführung
- **ID:** `T1105.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Verwendung integrierter Windows-Dienstprogramme wie PowerShell, Bitsadmin und Certutil zum Herunterladen von Dateien und Ausführen von Code, einer häufigen Angreifertechnik für die Bereitstellung und Ausführung von Nutzlasten.Die Regel konzentriert sich auf angreifertypische Muster und Ausführungskontexte, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Missbrauch von nativen High-Fidelity-APIs über LOLBins
- **ID:** `T1106.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die verdächtige Verwendung der nativen API-Ausführung durch vertrauenswürdiges Windows
Binärdateien (LOLBins).Konzentriert sich auf Szenarien, in denen Compiler oder Systemtools verwendet werden
werden von nicht vertrauenswürdigen übergeordneten Prozessen missbraucht, um eine Speicherinjektion durchzuführen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Brute Force & Tooling (T1110)
- **ID:** `T1110.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung von Brute-Force-Tools und das Erraten von Anmeldeinformationen per Skript durch Identifizierung
verdächtige Befehlszeilenargumente (Passwortlisten, Benutzerdateien) und nicht autorisierte
Prozessabstammungen von nicht vertrauenswürdigen Standorten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Mehrere fehlgeschlagene Anmeldeversuche für einen einzelnen Benutzer (mögliches Erraten des Passworts)
- **ID:** `T1110_001.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟡 (medium)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt mehrere fehlgeschlagene Authentifizierungsversuche für dasselbe Benutzerkonto innerhalb eines kurzen Zeitfensters, was auf das Erraten von Passwörtern oder Brute-Force-Aktivitäten hinweisen kann.Die Regel schließt häufige Quellen für Authentifizierungsrauschen aus, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**


---
## Ultra-Pro High-Fidelity-Zugangsdatenexport und -knacken (T1110.002)
- **ID:** `T1110_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, Anmeldeinformationsdatenbanken (SAM, SYSTEM, NTDS.dit) offline zu extrahieren
Cracking und identifiziert die Ausführung von Passwort-Wiederherstellungstools mit hoher Präzision
durch Herausfiltern legitimer Backup- und Systemwartungsprozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Passwort-Sprühen (T1110.003)
- **ID:** `T1110_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt Passwort-Spraying-Angriffe durch Identifizierung verdächtiger automatisierter Authentifizierungen
Logik, bei der ein einzelner Prozess eine Liste von Konten durchläuft.Es filtert nach
nicht vertrauenswürdige Prozessstandorte und bekannte Angriffsmodulsignaturen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Credential Stuffing und Combo-List-Missbrauch (T1110.004)
- **ID:** `T1110_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Credential Stuffing durch die Identifizierung automatisierter Tools und Interpreter
(Python, .NET) Verarbeitung großer Anmeldeinformations-Kombinationslisten oder Verwendung bekannter
Stuffing von Framework-Argumenten von nicht vertrauenswürdigen Orten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity MFA Evasion & Session Hijacking (T1111)
- **ID:** `T1111.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt MFA-Umgehung durch Identifizierung unbefugter Zugriffe auf Browser-Hauptschlüssel (Lokaler Status)
und Sitzungsdatenbanken (Cookies) durch nicht vertrauenswürdige Prozesse.Es überwacht auch
Reverse-Proxy-Phishing-Frameworks (Evilginx, Muraena) und Token-Manipulationstools.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Registrierungsmanipulation zur Umgehung (T1112)
- **ID:** `T1112.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt risikoreiche Änderungen an der Windows-Registrierung, die auf eine Deaktivierung abzielen
Sicherheitskontrollen (Defender, UAC, LSA) oder die Ermöglichung unbefugten Fernzugriffs.
Optimiert, um Standardsystemaktualisierungen zu ignorieren und sich auf nicht standardmäßiges Prozessverhalten zu konzentrieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomalie bei der Ultra-Pro-High-Fidelity-Bildschirmaufnahme (T1113)
- **ID:** `T1113.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [PSR.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte Bildschirmaufnahmen durch Identifizierung verdächtiger .NET/GDI+-APIs
Aufrufe innerhalb von PowerShell, versteckte PSR.exe-Sitzungen und automatisiertes Image
Serialisierung in temporäre/öffentliche Verzeichnisse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-High-Fidelity-E-Mail-Ernte-Anomalie (T1114)
- **ID:** `T1114.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte automatisierte E-Mail-Sammlung durch Identifizierung verdächtiger E-Mails
COM-Objektinstanziierung (Outlook.Application), Postfachexportanforderungen,
und programmgesteuerter Zugriff auf Posteingangs-/Gesendet-Ordner über nicht standardmäßige Shells.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Local Email Harvesting-Anomalie (T1114.001)
- **ID:** `T1114_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte automatisierte lokale E-Mail-Sammlung durch Identifizierung verdächtiger E-Mails
COM-Objektinstanziierung (Outlook.Application), Ordnerindex-Targeting (Posteingang/Gesendet),
und programmatische Umgehung (Visible=$false) von nicht vertrauenswürdigen Shells.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomalie beim Remote-E-Mail-Export von Ultra-Pro High-Fidelity (T1114.002)
- **ID:** `T1114_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Remote-E-Mail-Sammlung durch Identifizierung systematischer
Postfachexportanfragen, die sensible Schlüsselwortfilter und Weiterleitungen verwenden
Ausgabe auf nicht standardmäßige interne UNC-Pfade oder administrative Freigaben.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-E-Mail-Weiterleitungsregelanomalie (T1114.003)
- **ID:** `T1114_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte E-Mail-Weiterleitungsregeln durch programmgesteuerte Identifizierung
Umleitung zu externen/nicht vertrauenswürdigen Domänen in Kombination mit sensiblen Schlüsselwörtern
Filterung, die aus verdächtigen Prozesslinien stammt.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Zwischenablage-Datenspionage (T1115)
- **ID:** `T1115.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatische Überwachung und den Diebstahl der Zwischenablage durch Identifizierung persistenter Daten
Abfrageschleifen, nicht verwaltete Assembly-Ladevorgänge für den Zugriff auf die Zwischenablage und
verdächtige Prozesslinien (Webshells, Office-Makros), die auf die API zugreifen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Automatisierte Sammlung (T1119)
- **ID:** `T1119.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt hochverdächtige, automatisierte Datenerfassung durch Überwachung
Wildcard-basierte rekursive Dateiübertragungen sensibler Erweiterungen in
Gemeinsame Bereitstellungsbereiche, die aus interaktiven oder Web-Shells stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Peripheriegeräteerkennung (T1120)
- **ID:** `T1120.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [PNPUTIL.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Aufzählung von Peripheriegeräten mit Schwerpunkt auf USB- und Speichergeräten.
Filtert durch Analyse legitime System-PnP-Aktivitäten und Treiberverwaltung heraus
Prozessintegrität, Eltern-Kind-Beziehungen und spezifische Metadatenabfragen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Audioaufnahme und -Spionage (T1123)
- **ID:** `T1123.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte Audioaufnahmen durch Korrelation der Low-Level-Multimedia-API
Aufrufe (winmm, dsound) mit verdächtigen Prozesslinien (Shells, Office, W3WP)
und anomale Befehlszeilenargumente, die von anstößigen Toolsets verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Systemzeiterkennung (T1124)
- **ID:** `T1124.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Zielsystemzeit oder die Zeitzonenerkennung.Konzentriert sich auf anomale Prozesse
Abstammungslinien (z. B. Office-Apps, Webserver) und spezifische Automatisierungsmuster
Wird für Sandbox-Umgehungs- oder Geofencing-Prüfungen verwendet.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Videoaufnahmeanomalie (T1125)
- **ID:** `T1125.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Videoaufnahmen durch Identifizierung des programmgesteuerten Zugriffs auf
Multimedia-Frameworks (DirectShow, Media Foundation) über verdächtige Interpreter,
eigenständige Medienbinärdateien (FFmpeg) mit Umleitung oder Headless-Shell-Sitzungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Trusted Developer Utility Proxy (T1127)
- **ID:** `T1127.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [JSC.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch vertrauenswürdiger Entwicklerdienstprogramme (MSBuild, CSC, JSC) als Proxy
Ausführung von Schadcode.Filtert legitime CI/CD- und IDE-Aktivitäten heraus
indem wir uns auf verdächtige Abstammungs- und Befehlszeilenanomalien konzentrieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity MSBuild Proxy Execution (T1127.001)
- **ID:** `T1127_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die böswillige Ausführung von MSBuild.exe durch Identifizierung anomaler übergeordneter Prozesse.
nicht vertrauenswürdige Befehlszeilenargumente (wie Inline-XML-Aufgaben) und ausschließen
Standardentwicklung und CI/CD-Umgebungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Gemeinsames Laden von High-Fidelity-Modulen aus einem nicht vertrauenswürdigen Pfad
- **ID:** `T1129.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt vertrauenswürdige Systembinärdateien oder Produktivitäts-Apps, von denen DLLs geladen werden
nicht vertrauenswürdige, weltweit beschreibbare Verzeichnisse.Dies ist ein primärer Indikator dafür
DLL-Side-Loading oder Search Order Hijacking.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Datenkodierung und -Verschleierung (T1132)
- **ID:** `T1132.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Datenkodierungs-/Dekodierungssequenzen, die für C2-Stealth verwendet werden.
Konzentriert sich auf die programmatische Base64/Hex-Konvertierung innerhalb eines nicht standardmäßigen Prozesses
Abstammungslinien und der Missbrauch von Certutil für die Nutzlastbereitstellung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Standardkodierung und Nutzlastinjektion (T1132.001)
- **ID:** `T1132_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Standard-Codierungsnutzung durch Identifizierung eingebetteter Codes
Ausführbare Header (MZ/PE) innerhalb von Base64-Strings, anomal
programmatische Dekodierung und Befehlszeilen mit hoher Entropie von
nicht-administrative Prozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle, nicht standardmäßige High-Fidelity-Kodierung und XOR-Verschleierung (T1132.002)
- **ID:** `T1132_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [COLORCPL.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt benutzerdefinierte Codierung und Verschleierung durch Identifizierung der programmatischen Byteebene
Manipulation (XOR), Backtick-basierte String-Fragmentierung und Zeichencode
Rekonstruktion in nicht-interaktiven Prozesskontexten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomaler externer Remote-Service-Zugriffskontext
- **ID:** `T1133.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt verdächtige erfolgreiche Anmeldungen über externe Remote-Dienste (RDP/VPN).
Es filtert nach nicht standardmäßigen Quell-IPs und konzentriert sich auf Kontotypen mit hohem Risiko
oder technische Anomalien im Anmeldevorgang, die für automatisierte Anwendungen typisch sind
Credential Stuffing oder seitliche Bewegung von externen Sprungboxen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Access-Token-Manipulation und -Imitation (T1134)
- **ID:** `T1134.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt hochriskante Zugriffstoken-Manipulationen durch Überwachung auf verdächtige Daten
Übergänge auf Integritätsebene und die Verwendung spezialisierter Tools, die interagieren
mit LSASS, um Sicherheitstoken zu duplizieren oder zu stehlen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Token-Imitation über LSASS-Handle-Duplizierung (T1134.001)
- **ID:** `T1134_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Token-Diebstahl durch Überwachung auf verdächtige Handle-Duplizierungsanfragen
Ziel ist LSASS.exe.Es filtert nach bekannten legitimen Systemprozessen und
Sicherheitsagenten, um hochpräzise Warnungen zu gewährleisten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Erstellungsprozess mit Token (T1134.002)
- **ID:** `T1134_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Prozesserstellung mithilfe duplizierter Token.
Überwacht verdächtige Übergänge der Integritätsebene von „Medium“ zu „System“.
ohne standardmäßige UAC-Erhöhung (Consent.exe) oder legitimen Dienststart.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Make-and-Imitate-Token (T1134.003)
- **ID:** `T1134_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Erstellung von Sicherheitstokens mithilfe expliziter Anmeldeinformationen.
Überwacht verdächtige Befehlszeilenargumente von anstößigen Tools und
korreliert mit Anomalien des Anmeldetyps 9 (NewCredentials) von nicht vertrauenswürdigen Eltern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Parent-PID-Spoofing und Prozessbaumverletzung (T1134.004)
- **ID:** `T1134_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BASH.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Parent-PID-Spoofing durch Identifizierung von Verstößen gegen den Windows-Prozess
hierarchisches Modell.Konzentriert sich speziell auf kritische Systemprozesse (LSASS,
Spooler, CSRSS), die Shells oder Skriptinterpreter erzeugen, was architektonisch sinnvoll ist
in einer gesunden Umgebung unmöglich.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro SID-History-Injektion und DS-Manipulation (T1134.005)
- **ID:** `T1134_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die sIDHistory-Injection durch Überwachung von Änderungen an Verzeichnisdienstobjekten (Ereignis 5136).
und sie mit verdächtigen RPC-Aufrufen oder unbefugtem LSASS-Zugriff auf Domänencontrollern in Zusammenhang zu bringen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Network Share Discovery (T1135)
- **ID:** `T1135.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung von Netzwerkfreigaben und das Crawlen von Inhalten.
Konzentriert sich auf automatisierte Aufzählungsmuster (Schleifen, UNC-Sweeps)
stammen aus nicht standardmäßigen übergeordneten Prozessen und spezialisierten Tools wie Snaffler.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Unbefugte Ultra-Pro-Kontoerstellung (T1136)
- **ID:** `T1136.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung lokaler oder Domänenkonten durch Identifizierung verdächtiger Prozesslinien
und Befehlszeilenmuster, während autorisierte System- und Bereitstellungstools herausgefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Unbefugte Erstellung eines lokalen Ultra-Pro-Kontos (T1136.001)
- **ID:** `T1136_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung lokaler Benutzerkonten durch Analyse verdächtiger Prozessabläufe
und Befehlszeilenargumente.Filtert automatisiertes MDM, GPO und bekannte Installationsprogramme heraus
Aktivitäten zur Aufrechterhaltung einer niedrigen Falsch-Positiv-Rate.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Erstellung eines nicht autorisierten Domänenkontos (T1136.002)
- **ID:** `T1136_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung von Domänenkonten durch die Identifizierung verdächtiger Prozesslinien und
Nicht standardmäßige Ausführungsumgebungen.Filtert autorisierte IAM- und HR-Synchronisierungstools heraus.
und offizielle AD-Verwaltungskonsolen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Unbefugte Erstellung eines Ultra-Pro-Cloud-Kontos (T1136.003)
- **ID:** `T1136_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die manuelle Erstellung eines Cloud-Kontos durch Korrelation des Akteurtyps,
die Reputation der Quell-IP und das Fehlen autorisierter Bereitstellungsdienstprinzipale.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Office-Anwendungsstartpersistenz (T1137)
- **ID:** `T1137.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte Office-Persistenz durch Überwachung von Registrierungsänderungen
von nicht standardmäßigen Prozessen stammen oder auf verdächtige Dateispeicherorte verweisen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Änderung der globalen Office-Vorlage (Normal.dotm)
- **ID:** `T1137_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt risikoreiche Änderungen oder Erstellung globaler Microsoft Office-Vorlagen (Normal.dotm / NormalEmail.dotm) durch Nicht-Office-Prozesse oder aus verdächtigen Ausführungspfaden.Dies kann auf makrobasierte Persistenz hinweisen (MITRE ATT&CK T1137.001).

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Office Test-DLL-Persistenz (T1137.002)
- **ID:** `T1137_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung oder Änderung des Registrierungsschlüssels „Office Test“, der für verwendet wird
DLL-Sideloading-Persistenz.High-Fidelity-Erkennungsfilter für Nicht-Standard
Pfade und nicht autorisierte übergeordnete Prozesse.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Persistenz benutzerdefinierter Outlook-Formulare von Ultra-Pro (T1137.003)
- **ID:** `T1137_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die nicht autorisierte Persistenz benutzerdefinierter Outlook-Formulare durch Überwachung
nicht standardmäßige Registrierungsänderungen und das Spawnen verdächtiger Prozesse
aus Outlook im Zusammenhang mit der Ausführung von Formularskripten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Outlook Home Page Hijacking & Bypass (T1137.004)
- **ID:** `T1137_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen an den Startseiten von Outlook-Ordnern und den
Aktivieren von WebView-Bypass-Schlüsseln.Diese Technik wird zur Ausführung verwendet
willkürlicher Code, wenn ein Benutzer auf einen Outlook-Ordner klickt.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Manipulation von Ultra-Pro Office-Sicherheitsrichtlinien (T1137.005)
- **ID:** `T1137_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Schwächungen der Microsoft Office-Sicherheitsrichtlinien.
Konzentriert sich auf die globale Makroaktivierung, das Hinzufügen nicht vertrauenswürdiger Netzwerkstandorte,
und Richtlinienänderungen, die aus nicht standardmäßigen Prozessen resultieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Office Add-in Binäre Persistenz (T1137.006)
- **ID:** `T1137_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Persistenz nicht autorisierter Office-Add-Ins (.wll, .xll) durch Filtern
nicht vertrauenswürdige Dateispeicherorte, nicht signierte Binärdateien und verdächtige Schreibprozesse.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy Deobfuscation/Dekodierung (T1140)
- **ID:** `T1140.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPAND.EXE](https://lolbas-project.github.io/lolbas/), [EXTRAC32.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt High-Fidelity-Deobfuscation durch Überwachung nativer Tools (certutil, expand)
Die Dekodierung von Binärdateien aus nicht ausführbaren Erweiterungen (txt, jpg, xml) wurde eingeleitet
durch misstrauische Eltern oder gezielte Angriffe auf sensible temporäre Verzeichnisse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Browsererweiterung Force-Install Persistence (T1176)
- **ID:** `T1176.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung der Registrierungsschlüssel „ExtensionInstallForcelist“ oder „ExtensionInstallSources“.
Angreifer nutzen diese, um die Installation bösartiger Erweiterungen zu erzwingen, die vom Benutzer nicht entfernt werden können
und um die Installation von nicht offiziellen Webstores zu ermöglichen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Browser-Sitzungs-Hijacking (T1185)
- **ID:** `T1185.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt fortgeschrittenes Browser-Session-Hijacking durch Überwachung unbefugter Zugriffe
an Cookie-Datenbanken von nicht vertrauenswürdigen/nicht signierten Prozessen oder verdächtigen Standorten
wie \Temp oder \AppData.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Zwangsauthentifizierung (T1187)
- **ID:** `T1187.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt erzwungene Authentifizierungsversuche (NTLM Relay/Coercion) durch Überwachung
verdächtige UNC-Pfadmuster, WebDAV-Umleitung und spezifisches RPC
Schnittstellenausnutzung zum Auslösen der ausgehenden Authentifizierung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Vom Browser stammende Shell- oder Systemtool-Ausführung
- **ID:** `T1189.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von Webbrowsern erzeugt werden.Dieses Muster ist hoch
Hinweis auf eine erfolgreiche Ausnutzung durch einen Drive-by-Kompromiss (T1189),
Dabei löst ein Exploit-Kit eine Nutzlast oder eine Shell direkt aus dem Speicher des Browsers aus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Auf dem Webserver wurde ein verdächtiger Cross-Site-Scripting-Versuch (XSS) erkannt
- **ID:** `T1190.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟡 (medium)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt potenzielle Cross-Site-Scripting-Versuche (XSS), indem es häufig reflektierte und codierte XSS-Nutzlasten in HTTP-Anfragen identifiziert, sich auf Parameter-basierte Injektionsmuster konzentriert und typische automatisierte Scanner ausschließt, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**


---
## High-Fidelity-Erkennung von Kompromittierungen in der Lieferkette (Anomalie nach der Aktualisierung)
- **ID:** `T1195.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WINGET.EXE](https://lolbas-project.github.io/lolbas/), [PROCDUMP.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von legitimen Software-Updatern erzeugt oder signiert wurden
Installateure.Konzentriert sich auf Erkennungs- und Zugangstools für Anmeldeinformationen, die es niemals geben sollte
Teil eines standardmäßigen Softwarewartungs- oder Aktualisierungszyklus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Erkennung von Abhängigkeitsvergiftungen
- **ID:** `T1195_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von Paketmanagern oder Build-Tools erzeugt werden.
Konzentriert sich auf Aufklärungs- und Exfiltrationsaktivitäten, die während der Bibliothek ausgelöst werden
Installation oder Kompilierung (Skripte vor/nach der Installation).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Kompromittierte binäre High-Fidelity-Aktivität (nach dem Update)
- **ID:** `T1195_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von vertrauenswürdigen Geschäftsanwendungen erzeugt werden
wurden auf binärer Ebene kompromittiert.Es konzentriert sich auf den Übergang von
Von der legitimen App-Ausführung bis zur unbefugten Entdeckung oder Skriptausführung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochpräzise Hardware-/Firmware-Manipulationserkennung
- **ID:** `T1195_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung von Firmware-Flashing-Tools oder Hardwarezugriff auf niedriger Ebene
Versorgungsunternehmen in verdächtigen Kontexten.Dies zielt auf eine potenzielle Nachnutzung ab
von kompromittierter Hardware oder Versuchen, UEFI-Rootkits zu installieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Download verdächtiger Dateien über Bitsadmin (High Fidelity)
- **ID:** `T1197.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Dateidownloads, die mit bitsadmin.exe durchgeführt werden, einem veralteten, aber immer noch missbrauchten Windows LOLBAS-Dienstprogramm.Die Regel konzentriert sich auf angreifertypische Nutzungsmuster, Ausführungskontext und Download-Ziele, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Missbrauchserkennung in vertrauenswürdigen Beziehungen
- **ID:** `T1199.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Entdeckungs- und Aufklärungsaktivitäten, die von stammen
Vertrauenswürdige Eingangspunkte (RDP, Citrix, VPN).Es filtert Standardadministrationen heraus
Verhalten durch Fokussierung auf bestimmte Eltern-Kind-Prozessketten und ungewöhnliche Argumente.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Schädliche hardwareinduzierte Befehlsausführung (HID-Injection)
- **ID:** `T1200.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Befehlsausführungsmuster, die für bösartige HID-Geräte (Rubber Ducky, Bash Bunny) typisch sind.
Konzentriert sich auf schnelles Shell-Spawnen mit „Stealth“-Flags, die aus dem Benutzersitzungskontext stammen
ohne Standard-GUI-Interaktion.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Kennwortrichtlinienerkennung (T1201)
- **ID:** `T1201.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Aufzählung von Domänen-/lokalen Passwortrichtlinien.
Konzentriert sich auf Aufklärungsmuster, die zur Kalibrierung von Brute-Force verwendet werden
Angriffe und filtert gleichzeitig legitime System-/Administratorgeräusche heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Indirekte Befehlsausführung (T1202)
- **ID:** `T1202.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FORFILES.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [PCALUA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung von Binärdateien, die als Proxy für die Befehlsausführung verwendet werden können.
Konzentriert sich auf nicht standardmäßige übergeordnete Prozesse und spezifische Befehlszeilenargumente
für pcalua.exe, conhost.exe und forfiles.exe, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Client-seitige Ausbeutung und Shell-Spawning
- **ID:** `T1203.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von Clientanwendungen (Office, Browser,
PDF-Reader).Der Schwerpunkt liegt auf der Shell-Ausführung, Erkennungstools und der Erstellung von LOLBins
aus Sandbox- oder Anwendungskontexten mit geringer Integrität.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtiger untergeordneter Prozess, der von einer Microsoft Office-Anwendung erzeugt wurde (High Fidelity)
- **ID:** `T1204.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [MSACCESS.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von Microsoft Office-Anwendungen erzeugt werden und auf Makromissbrauch, DDE-Ausnutzung oder dokumentbasierte Malware-Ausführung hinweisen.Die Regel konzentriert sich auf angreifertypische untergeordnete Prozesse, Befehlszeilenmuster und vom Benutzer beschreibbaren Ausführungskontext, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Benutzerausführung eines schädlichen Links (T1204.001)
- **ID:** `T1204_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von Webbrowsern, E-Mail-Clients usw. erzeugt werden
Instant Messenger.Konzentriert sich auf LOLBins und Skriptinterpreter, die mit gestartet werden
Netzwerkbezogene oder verschleierte Argumente, die auf die Ausführung eines böswilligen Links hinweisen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Benutzerausführung einer schädlichen Datei
- **ID:** `T1204_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von Office-Produktivitäts-Apps erzeugt werden.
PDF-Reader oder Archivierungstools.Zielt speziell auf makroinitiierte Personen ab
oder Exploit-gesteuerte Ausführung von Systemtools (LOLBins).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Ausführung von gemounteter virtueller Festplatte (T1204.003)
- **ID:** `T1204_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Binärdateien oder Skripte, die von einem virtuellen Laufwerk (ISO, VHD, VHDX) ausgeführt werden.
Konzentriert sich auf LOLBins und Skriptinterpreter, die über explorer.exe von Nicht-C:-Laufwerken gestartet werden.
ein häufiges Muster für Malware, die Mark-of-the-Web umgeht.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Phishing über einen bösartigen Link mit Domänen- und Absenderanomalien
- **ID:** `T1204_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Niedrig (Es lässt sich gut überwachen)
- **Beschreibung:** Erkennt Phishing-E-Mails mit bösartigen Links anhand von URL-Verkürzern, neu registrierten Domänen und Absender-Spoofing.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle Verkehrssignalisierung und Port-Knocking (T1205)
- **ID:** `T1205.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, Port Knocking/Traffic Signaling zu implementieren oder auszulösen.
Konzentriert sich auf die Registrierung von Rohpaket-Erfassungstreibern (Npcap/WinPcap).
und verdächtige Änderungen an Firewall-Regeln, die von nicht vertrauenswürdigen Shells aus initiiert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Port Knocking & Raw Socket Listener (T1205.001)
- **ID:** `T1205_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Implementierung von Port Knocking durch Überwachung
Registrierung von Rohpaket-Erfassungstreibern und verdächtiger Firewall
Änderungen (UDP/ICMP/LocalPort Any), die von nicht vertrauenswürdigen Shells initiiert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Steckdosenfilter und WFP-Verkehrssignalisierung (T1205.002)
- **ID:** `T1205_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FLTMC.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Registrierung von Netzwerk-Socket-Filtern oder WFP-Callouts.
Überwacht das Laden von Treibern auf niedriger Ebene und die Manipulation der WFP-Datenbank von
nicht vertrauenswürdige Prozesslinien, eine gängige Technik für heimliches Port-Klopfen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Rogue-DC-Topologiemanipulation (T1207)
- **ID:** `T1207.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die Erstellung eines neuen nTDSDSA-Objekts oder die Registrierung eines kritischen Objekts
Domänencontroller-SPNs durch ein Nicht-DC-Konto.Dies weist auf einen Rogue DC hin
oder DCShadow-Angriff.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Nutzung von Remote-Diensten (T1210)
- **ID:** `T1210.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt erfolgreiche Post-Exploitation-Muster, bei denen ein Netzwerkdienst eine generiert
interaktive Shell oder eine Proxy-Binärdatei.Speziell darauf abgestimmt, RCE über SMB zu empfangen,
RPC, Spooler und WMI, während die Standard-IT-Orchestrierung ignoriert wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Berechtigungseskalationsausnutzung (T1211)
- **ID:** `T1211.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielle Ausnutzung zur Rechteausweitung durch Identifizierung
anomale Kinderprozesse von gefährdeten Eltern mit besonderem Fokus auf
Ausbrechen aus Anwendungs-Sandboxen (Browser, Office, PDF).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Credential Service Exploitation (T1212)
- **ID:** `T1212.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielle Ausnutzung von Authentifizierungsdiensten (LSASS, LogonUI, Spooler)
durch Identifizierung illegaler untergeordneter Prozesse, nicht gesicherter Speicherausführung und bekannter
Ausnutzungsmuster erkennen und gleichzeitig legitime Sicherheitstool-Interferenzen filtern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Repository-Dump (T1213)
- **ID:** `T1213.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Massendatenerfassung aus internen Wissensdatenbanken (Confluence, Jira, SharePoint)
durch die Identifizierung verdächtiger API-gesteuerter Exportbefehle, die von nicht vertrauenswürdigen Unternehmen stammen
Prozesskontexte oder temporäre Verzeichnisse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Confluence Scraping (T1213.001)
- **ID:** `T1213_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Massenextraktion von Inhalten aus Atlassian Confluence durch
Identifizieren verdächtiger API-gesteuerter Lese-/Exportmuster, die ihren Ursprung haben
nicht vertrauenswürdige Shell-Kontexte oder temporäre Verzeichnisse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-SharePoint-Massendaten-Exfiltration (T1213.002)
- **ID:** `T1213_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Massendatenerfassung aus SharePoint durch Identifizierung
verdächtige PnP-PowerShell-Nutzung, Massen-REST-API-Abfragen und nicht autorisierte Angriffe
Aktivitäten der SharePoint Online-Verwaltungsshell aus nicht standardmäßigen Kontexten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Knowledge Base Scraping (T1213.003)
- **ID:** `T1213_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische Wissensdatenbank-Exfiltration (Wiki, Stack Overflow for Teams)
durch die Identifizierung rekursiver Spiegelungsflags, Massenarchivierungslogik usw
Nicht-Browser-Skript-Engines, die auf interne Dokumentations-URLs abzielen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-System-Skript-Proxy-Ausführung (T1216)
- **ID:** `T1216.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [MANAGE-BDE.WSF](https://lolbas-project.github.io/lolbas/), [PUBPRN.VBS](https://lolbas-project.github.io/lolbas/), [SYNCAPPVPUBLISHINGSERVER.VBS](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch vertrauenswürdiger, von Windows signierter Skripts, um schädlichen Code weiterzuleiten.
Konzentriert sich auf netzwerkbasierte Ausführungsauslöser und anomale Eltern-Kind-Verbindungen
Prozessbeziehungen, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Pubprn-Skript-Proxy-Ausführung (T1216.001)
- **ID:** `T1216_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [PUBPRN.VBS](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch des signierten Windows-Skripts „pubprn.vbs“ als Proxy für die Ausführung
von Remote-Skriptlets (.sct).Konzentriert sich auf die Argumentinjektion mit dem „script:“
Protokoll und anomale Prozesslinie.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Browser Information Discovery (T1217)
- **ID:** `T1217.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Entdeckung von Browser-Metadaten und -Verlauf.
Konzentriert sich auf Nicht-Browser-Prozesse, die auf vertrauliche Profildateien zugreifen (SQLite/JSON).
Verwendung von Befehlszeilentools oder anomalen Umleitungsmustern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-System-Binär-Proxy-Ausführung (T1218)
- **ID:** `T1218.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMSTP.EXE](https://lolbas-project.github.io/lolbas/), [CONTROL.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [ODBCCONF.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die anomale Ausführung vertrauenswürdiger Windows-Binärdateien, die als Proxy für bösartigen Code verwendet werden.
Konzentriert sich auf prozessübergreifende Aufrufe (z. B. Office an Rundll32) und ist verdächtig
Befehlszeilenargumente wie URLs oder Nicht-DLL-Erweiterungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity HH.exe Proxy-Ausführung (T1218.001)
- **ID:** `T1218_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch von hh.exe zur Ausführung von Schadcode über CHM-Dateien oder Remote-ITS-Protokolle.
Konzentriert sich auf nicht standardmäßige übergeordnete Prozesse und Befehlszeilenflags, die zur Dekompilierung verwendet werden
oder das Abrufen von Remote-Payloads, während die legitime Verwendung von Hilfedateien herausgefiltert wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Control.exe Proxy-Ausführung (T1218.002)
- **ID:** `T1218_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONTROL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch von control.exe, um schädliche .CPL- oder DLL-Dateien von nicht vertrauenswürdigen Pfaden zu laden.
Nutzt OriginalFileName, um umbenannte Binärdateien abzufangen, und konzentriert sich auf grenzüberschreitende Dateien
Prozessausführung (z. B. Office- oder Scripting-Hosts starten die Systemsteuerung).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity MsiExec Proxy Execution (T1218.003)
- **ID:** `T1218_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch von msiexec.exe zur Ausführung bösartiger Payloads.
Konzentriert sich auf nicht standardmäßige Eltern-Kind-Beziehungen (z. B. Office zu MsiExec)
und Remote-Ressourcenabruf, während legitime Unternehmensinstallationsprogramme herausgefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity InstallUtil Proxy-Ausführung (T1218.004)
- **ID:** `T1218_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung von InstallUtil.exe als Proxy für bösartigen Code.
Konzentriert sich auf das /u-Flag, nicht standardmäßige übergeordnete Prozesse und die Ausführung
aus beschreibbaren Verzeichnissen, während legitime .NET-Installationen herausgefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Mshta-Ausführung von Remote-Skript (High Fidelity)
- **ID:** `T1218_005.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die verdächtige Ausführung von mshta.exe, das zum direkten Ausführen von Skripts von Remote-URLs verwendet wird. Dies ist eine gängige LOLBAS-Technik, die von Angreifern für die Erstausführung und das Staging der Nutzlast verwendet wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Msiexec-Installation von einer Remote-URL (High Fidelity)
- **ID:** `T1218_007.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die verdächtige Verwendung von msiexec.exe zur direkten Installation von MSI-Paketen von Remote-URLs, eine Technik, die von Angreifern häufig als LOLBAS-Methode missbraucht wird.Die Regel konzentriert sich auf angreifertypische Befehlszeilenmuster und Ausführungskontext, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Odbcconf Proxy Execution (T1218.008)
- **ID:** `T1218_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [ODBCCONF.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch von odbcconf.exe zum Laden schädlicher DLLs über die REGSVR-Aktion.
Konzentriert sich auf Befehlszeilenanomalien, verdächtige übergeordnete Prozesse usw
Nicht standardmäßige Dateipfade, um Fehlalarme von legitimen Installationsprogrammen zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Regsvcs/Regasm Proxy Execution (T1218.009)
- **ID:** `T1218_009.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch von regsvcs.exe oder regasm.exe zur Ausführung schädlicher .NET-Assemblys.
Konzentriert sich auf das /U-Flag für die Proxy-Ausführung, nicht standardmäßige übergeordnete Prozesse,
und Ausführung über beschreibbare/nicht vertrauenswürdige Pfade.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Regsvr32-Ausführung, die auf LOLBAS-Missbrauch hinweist (High Fidelity)
- **ID:** `T1218_010.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Verwendung von regsvr32.exe, die häufig mit LOLBAS-Missbrauch (Squiablydoo-Technik) verbunden ist, einschließlich der Ausführung von Scriptlets, Remote-Payloads oder DLLs von benutzerbeschreibbaren Speicherorten unter Verwendung angreifertypischer Befehlszeilenargumente.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Rundll32-Ausführung mit Skript oder Remote-Payload (High Fidelity)
- **ID:** `T1218_011.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [SHELL32.DLL](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Verwendung von rundll32.exe, die häufig mit LOLBAS-Missbrauch in Zusammenhang steht, einschließlich der Ausführung von JavaScript, HTML-Anwendungen und dem Laden von Nutzlasten von entfernten oder vom Benutzer beschreibbaren Speicherorten.Die Regel minimiert Fehlalarme, indem sie sich auf angreifertypische Befehlszeilenmuster und Ausführungskontext konzentriert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Verclsid Proxy Execution (T1218.012)
- **ID:** `T1218_012.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [VERCLSID.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch von verclsid.exe als Proxy für die Ausführung schädlicher COM-Objekte (DLLs).
Filtert legitime, vom System initiierte Überprüfungen heraus und konzentriert sich dabei auf verdächtige
Eltern-Kind-Beziehungen und anomale Befehlszeilenauslöser.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Rundll32 Proxy-Ausführung (T1218.013)
- **ID:** `T1218_013.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [PCWUTL.DLL](https://lolbas-project.github.io/lolbas/), [SHELL32.DLL](https://lolbas-project.github.io/lolbas/), [URL.DLL](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt eine anomale Ausführung von rundll32.exe, indem es sich auf verdächtige Befehlszeilen konzentriert
Argumente, nicht standardmäßige Dateierweiterungen und nicht vertrauenswürdige Ausführungspfade.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity MMC Proxy Execution (T1218.014)
- **ID:** `T1218_014.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch von mmc.exe zur Ausführung von Schadcode über Component Object Model (COM)
Entführung oder nicht vertrauenswürdige Konsolendateien (.msc).Filtert legitime Verwaltungsmaßnahmen heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Verwendung legitimer Remote-Verwaltungstools außerhalb des Unternehmensmusters
- **ID:** `T1219.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt verdächtige Erstellung von Diensten im Zusammenhang mit legitimen Remote-Verwaltungstools (z. B. PsExec), wenn diese außerhalb genehmigter Unternehmensverwaltungsmuster verwendet werden.Dieses Verhalten wird häufig bei lateraler Bewegung durch Angreifer beobachtet, die Admin-Tools missbrauchen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-XSL-Skriptverarbeitung (T1220)
- **ID:** `T1220.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [WMIC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige WMIC-Ausführungen mit XSL-Stylesheets, die sich in nicht standardmäßigen Formaten befinden
Verzeichnisse oder Remote-URLs, was eine gängige Technik zur Umgehung von Anwendungen ist
Whitelisting und die Ausführung beliebiger Skripte.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Office-Vorlageninjektion (T1221)
- **ID:** `T1221.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Kritisch hoch (SIEM-Killerkategorie!)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Microsoft Office-Anwendungen, die Remote-Vorlagen von Nicht-Microsoft abrufen
Infrastruktur, gefolgt von der Erstellung temporärer Vorlagendateien.

#### 🚨 Reaktions-Playbook
1. **IP-Reputation: Überprüfen Sie die Remote-IP-Adresse in Reputationsdatenbanken.**
2. **Verkehrsanalyse: Untersuchen Sie die Menge der gesendeten Daten.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Änderung der Ultra-Pro High-Fidelity-Berechtigungen (T1222)
- **ID:** `T1222.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Dateiberechtigungsänderungen durch Identifizierung nativer Tools
(icacls, takeown) wird mit breiten Zugriffsflags (Vollzugriff, Jeder) verwendet
initiiert durch nicht standardmäßige übergeordnete Prozesse oder über verdächtige Pfade.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Änderung der Dateiberechtigungen für Ultra-Pro High-Fidelity Windows (T1222.001)
- **ID:** `T1222_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Dateiberechtigungsänderungen durch Identifizierung des breiten Zugriffs
Zuschüsse (Vollzugriff, Jeder) oder Vererbungsblockierung, initiiert von
verdächtige/nicht vertrauenswürdige Prozesse oder gezielte Angriffe auf sensible Verzeichnisse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Änderung der Dateiberechtigungen für Ultra-Pro High-Fidelity Linux (T1222.002)
- **ID:** `T1222_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt gezielte Manipulationen von Linux-Berechtigungen durch Identifizierung hoher Risiken
Attributänderungen (SUID, Unveränderlichkeit) oder Massenänderungen in sensiblen Bereichen
Systempfade, die von nicht privilegierten oder weborientierten Dienstkonten initiiert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Execution Guardrails Discovery (T1480)
- **ID:** `T1480.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Ausführungsleitlinien durch Identifizierung einer anomalen Umgebung
Entdeckungsmuster, die von nicht privilegierten Benutzern oder misstrauischen Eltern initiiert wurden,
Herausfiltern allgemeiner Verwaltungs- und Systemgeräusche.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Environmental Keying Discovery (T1480.001)
- **ID:** `T1480_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezieltes Umgebungs-Keying durch Identifizierung von Hardware-Fingerprinting
und maschinenspezifische Registrierungssuchen, die von verdächtigen, nicht gesicherten,
oder nicht standardmäßige übergeordnete Prozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Domain Trust Discovery (T1482)
- **ID:** `T1482.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Aufzählung von Domänen- und Gesamtstrukturvertrauensstellungen.
Konzentriert sich auf anomale Prozessherkunft (z. B. interaktive Shells auf Workstations)
und spezifische Aufklärungsmuster, die von Tools wie BloodHound/SharpHound verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Manipulation von Ultra-Pro-Domänenrichtlinien und GPO-Missbrauch (T1484)
- **ID:** `T1484.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen an kritischen Domänenrichtlinien durch Überwachung
Das Dateisystem schreibt in den SYSVOL-Ordner und die GPO-Linkänderungen werden herausgefiltert
Standard-Verwaltungstools (GPMC).

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Änderung und Missbrauch der Ultra-Pro-Gruppenrichtlinien (T1484.001)
- **ID:** `T1484_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte GPO-Änderungen durch Korrelation von Dateisystemschreibvorgängen mit kritischen Änderungen
Richtlinienvorlagen in SYSVOL mit Anomalien auf Prozessebene.Filtert DFSR heraus
Replikation und Standard-GPMC-Verwaltungskonsolen, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Domain Trust Tampering & SID Filtering Bypass (T1484.002)
- **ID:** `T1484_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt risikoreiche Änderungen an Domain Trust-Beziehungen und konzentriert sich dabei auf
die Deaktivierung der SID-Filterung (Quarantäne) und der unbefugten Vertrauenserstellung.
Korreliert AD-Objektänderungen mit dem bekannten Verwaltungskontext.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Datenvernichtung (T1485)
- **ID:** `T1485.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CIPHER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WBADMIN.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische Datenvernichtung durch Überwachung auf VSS-Löschung,
Sichere Dateivernichtung (sdelete, cipher) und rekursive Massenlöschung
initiiert von verdächtigen übergeordneten Prozessen oder zielt auf nicht temporäre Verzeichnisse ab.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ransomware-Vorbereitungsaktivität auf Windows-Host erkannt (High Fidelity)
- **ID:** `T1486.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Ransomware-Vorbereitungsaktivitäten durch die Identifizierung mehrerer Wiederherstellungs-Hemmungs- und Abwehr-Umgehungsaktionen, die innerhalb eines kurzen Zeitfensters ausgeführt werden.Dazu gehört das Deaktivieren von Wiederherstellungsoptionen, das Löschen von Schattenkopien und das Stoppen sicherheitsrelevanter Dienste.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Service Stop (T1489)
- **ID:** `T1489.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes Stoppen kritischer System- und Sicherheitsdienste
durch Überwachung von Dienstkontrolltools, die aus verdächtigen Prozessen stammen
Abstammungslinien oder die gezielte Bekämpfung hochwertiger Abwehrmechanismen (EDR, VSS, AV).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtiges Löschen von Volume-Schattenkopien über VSSAdmin (High Fidelity)
- **ID:** `T1490.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtiges Löschen von Volume-Schattenkopien mithilfe von vssadmin.exe, das häufig bei Ransomware- und zerstörerischen Angriffen beobachtet wird.Die Regel konzentriert sich auf angreifertypische Befehlszeilenargumente und Nicht-Dienstausführungskontexte und schließt bekannte Backup-Lösungen aus, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Verunstaltung (T1491)
- **ID:** `T1491.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Website-Verunstaltungen durch Überwachung auf verdächtige Dateien
Manipulationen (Verschieben, Kopieren, Echo) innerhalb von Web-Root-Verzeichnissen
von nicht standardmäßigen oder kompromittierten Dienstprozessen (z. B. w3wp.exe, httpd.exe).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity interne Verunstaltung (T1491.001)
- **ID:** `T1491_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt interne Systemverunstaltungen durch Überwachung auf nicht autorisierte Änderungen
zu Desktop-Hintergründen, rechtlichen Hinweisen und Anmeldebannern über die Registrierung oder CLI,
Insbesondere werden GPO-gesteuerte und vom System initiierte Änderungen herausgefiltert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity externe Verunstaltung (T1491.002)
- **ID:** `T1491_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Verunstaltungen externer Websites durch Identifizierung verdächtiger Dateien
Manipulationsbefehle (Verschieben, Kopieren, Echo), die von Webserver-Arbeitsprozessen ausgeführt werden
innerhalb sensibler Webroot-Verzeichnisse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Firmware-Beschädigung (T1495)
- **ID:** `T1495.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WBEMTEST.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt durch Überwachung potenzielle Firmware-Beschädigungen oder unbefugtes Flashen
Low-Level-Hardware-Zugriffstools und Firmware-Update-Dienstprogramme entstehen
aus nicht vertrauenswürdigen Prozessherkunftsbereichen (z. B. Browsern, Office-Apps oder temporären Ordnern).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Ressourcen-Hijacking (T1496)
- **ID:** `T1496.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes Ressourcen-Hijacking (Kryptomining) durch Überwachung
spezifische Miner-Protokolle (Stratum), Algorithmus-Flags und Hardware
Optimierungsargumente, die aus nicht vertrauenswürdigen Prozesslinien stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Virtualisierung/Sandbox-Umgehung (T1497)
- **ID:** `T1497.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt raffinierte Sandbox-Umgehung durch Überwachung auf schnelle Multivektoren
Virtualisierungsprüfungen (BIOS, MAC, CPU, Festplatte), die von nicht vertrauenswürdigen Prozessen initiiert werden
in verdächtigen Verzeichnissen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity VM Artifact Discovery (T1497.001)
- **ID:** `T1497_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Entdeckung von Virtualisierungsartefakten durch Nicht-System-,
nicht vertrauenswürdige Prozesse.Filtert legitime Installationsprogramme und Systemdienste heraus
sich auf Techniken zur Malware-Umgehung zu konzentrieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity User Interaction Evasion (T1497.002)
- **ID:** `T1497_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt raffinierte Umgehungen von Benutzerinteraktionen durch Identifizierung nicht signierter oder nicht signierter Benutzer
verdächtig lokalisierte Prozesse, die menschenzentrierte APIs abfragen (Maus, Tastatur, aktuelle Dateien)
ohne einen legitimen UI-Kontext zu haben.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Time-based Evasion (T1497.003)
- **ID:** `T1497_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt raffinierte zeitbasierte Umgehung durch Überwachung auf nicht standardmäßige Verzögerungen
Mechanismen (Ping, Auswahl, Zeitüberschreitung), die insbesondere von nicht vertrauenswürdigen Binärdateien initiiert werden
Ziel sind langfristige Verzögerungen, die dazu dienen, die Grenzen der Sandbox-Analyse auszuschöpfen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Netzwerk-DoS (T1498)
- **ID:** `T1498.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [PKTMON.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Netzwerk-Denial-of-Service-Versuche (Flooding, Amplification)
durch Überwachung auf Low-Level-Paketmanipulationstools und hohe Bandbreite
Stresstests, die aus nicht vertrauenswürdigen Prozesslinien stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Direct Flow Flood (T1498.001)
- **ID:** `T1498_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [PKTMON.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezieltes direktes Netzwerk-Flooding (SYN, UDP, ICMP) durch Überwachung
für aggressive Paketgenerierungsparameter (Mikrointervalle, unbegrenzte Bandbreite)
aus nicht vertrauenswürdigen Prozesslinien stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Endpunkt-DoS (T1499)
- **ID:** `T1499.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Denial-of-Service-Angriffe auf Endpunkten durch Überwachung auf erzwungene Beendigung
von kritischen Systemprozessen (LSASS, CSRSS) und Ressourcenerschöpfungsschleifen
aus nicht vertrauenswürdigen Prozesslinien stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-OS-Selbstzerstörung (T1499.001)
- **ID:** `T1499_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [NTSD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Selbstzerstörung des Betriebssystems durch Überwachung auf erzwungene Beendigung von
kritische Kernelprozesse (csrss.exe, wininit.exe) und böswillige Verwendung von
System-Debugger, um sofortiges BSOD auszulösen, insbesondere das Herausfiltern
vertrauenswürdige Verwaltungs- und Aktualisierungsprozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Service-Erschöpfung (T1499.002)
- **ID:** `T1499_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Denial-of-Service am Endpunkt aufgrund der Erschöpfung des Dienstes durch Überwachung
Unbefugte Dienstbeendigung und dauerhafte Konfigurationsänderungen (Deaktivierung)
Angriffe auf Sicherheits- und Infrastrukturdienste, die aus verdächtigen Abstammungslinien stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity OS-Selbstzerstörung (T1499.003)
- **ID:** `T1499_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [NTSD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Selbstzerstörung des Betriebssystems durch Überwachung auf erzwungene Beendigung von
kritische Kernelprozesse (csrss.exe, wininit.exe) und böswillige Verwendung von
System-Debugger, um sofortiges BSOD auszulösen, insbesondere das Herausfiltern
vertrauenswürdige Verwaltungs- und Aktualisierungsprozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Ressourcenerschöpfung (T1499.004)
- **ID:** `T1499_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Versuche zur Ressourcenauslastung (CPU/RAM/IO) durch Identifizierung
Endlosschleifenmuster und massive Speicherzuweisungsversuche
aus verdächtigen Prozesslinien stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Web-Shell-Ausführungsmuster (T1505.003)
- **ID:** `T1505.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [BASH.EXE](https://lolbas-project.github.io/lolbas/), [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt hochzuverlässige Indikatoren der Web-Shell-Aktivität durch Überwachung von Webserverprozessen
interaktive Granaten oder Systemaufklärungswerkzeuge hervorbringen.Beinhaltet eine strenge Filterung
für legitime .NET-Kompilierung und IIS-Verwaltung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro SQL Server-Befehls-Shell-Ausführung (T1505.001)
- **ID:** `T1505_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die nicht autorisierte Ausführung von Betriebssystembefehlen über erweiterte gespeicherte Prozeduren von SQL Server
und CLR-Baugruppen.Filtert legitime SQL-Agent-Wartung beim Markieren
verdächtige Erkennungsbefehle und Konfigurationsänderungen (xp_cmdshell, sp_configure).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro IIS Native Module Injection (T1505.002)
- **ID:** `T1505_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [NGEN.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Registrierung oder manuelle Injektion von IIS-Modulen durch Überwachung
Verwendung von appcmd.exe, direkte Bearbeitung von applicationHost.config und Laden von DLLs
aus nicht standardmäßigen oder vom Benutzer beschreibbaren Pfaden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Webshell-Upload oder Interaktion auf dem Webserver erkannt (High Fidelity)
- **ID:** `T1505_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt potenzielle Webshell-Aktivitäten, indem verdächtige Skript-Uploads in über das Internet zugängliche Verzeichnisse und nachfolgende Interaktionen mithilfe von Parametern im Befehlsausführungsstil identifiziert werden.Die Regel minimiert Fehlalarme, indem sie sich auf angreifertypische Pfade, Parameter und Zugriffsmuster konzentriert.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Mainboard-Boot-Image und SPI-Flash-Manipulation (T1542.004)
- **ID:** `T1505_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Firmware-Manipulationen durch Überwachung des Hardwarezugriffs auf niedriger Ebene
Tools und Fahrerregistrierungen, die aus nicht standardmäßigen Prozessketten initiiert werden.
Konzentriert sich auf SPI-Flash-Schreib- und Image-Injection-Versuche.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Terminal Services DLL-Hijacking (T1505.005)
- **ID:** `T1505_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen an Terminal Services (RDP)-Dienst-DLLs
und Anbieter.Überwacht ServiceDll- und ProviderPath-Manipulationen durch
nicht vertrauenswürdige Prozesse und nicht standardmäßige Dateipfade.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Software Discovery (T1518)
- **ID:** `T1518.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Softwareerkennung mit Schwerpunkt auf der Identifizierung von Sicherheitsprodukten.
Verwendet Gating auf Integritätsebene, Korrelation zwischen übergeordneten Prozessen und ein bestimmtes Schlüsselwort
Analyse, um Fehlalarme durch Systeminventarisierungstools zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Sicherheitssoftware-Erkennung (T1518.001)
- **ID:** `T1518_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Erkennung von Sicherheitsprodukten (AV/EDR/HIPS) und Sandboxes.
Konzentriert sich auf schlüsselwortspezifische Filterung (findstr/grep) und anomale Prozesse
Abstammungslinien (Office-Apps, Webserver oder nicht erhöhte Shells).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Unautorisierte Container-Image-Ausführung mit Exploit-Grad (Implant-Container-Image)
- **ID:** `T1525.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die Ausführung von Container-Images, die nicht aus genehmigten Registern stammen und außerhalb von CI/CD- oder System-Namespaces ausgeführt werden, was auf eine mögliche Verwendung implantierter Container-Images für Persistenz oder Erstzugriff hinweist.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Cloud Service Discovery (T1526)
- **ID:** `T1526.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische Cloud-Service-Aufzählung (Lambda, Secrets, KeyVault)
Fokussierung auf anomale Ausführungsumgebungen (interaktive Shells auf Nicht-Entwickler-Hosts)
und Ausgabeumleitungsmuster, die für die automatisierte Ernte verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Anwendungstoken und Session-Hijacking (T1528)
- **ID:** `T1528.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Extraktion von Anwendungszugriffstokens und Sitzungscookies.
Überwacht verdächtigen Zugriff auf Cloud-CLI-Konfigurationen (Azure, AWS, GCP)
und browserbasierte Anmeldeinformationsspeicher durch nicht vertrauenswürdige Prozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Herunterfahren/Neustarten des Ultra-Pro High-Fidelity-Systems (T1529)
- **ID:** `T1529.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte oder verdächtige Befehle zum Herunterfahren/Neustarten des Systems
durch Überwachung auf erzwungene Operationen (-f), die von nicht vertrauenswürdigen Personen stammen
Prozesslinien (Browser, Office-Apps, temporäre Ordner).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Cloud-Speicher-Datendiebstahl (T1530)
- **ID:** `T1530.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Datenexfiltration von Cloud-Speicheranbietern (AWS, Azure, GCP)
durch Identifizierung verdächtiger CLI-Argumente, Inline-Anmeldeinformationsinjektion und
Anomale Prozesslinien, die aus Nicht-Admin-Kontexten stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Entfernen des Ultra-Pro High-Fidelity-Kontozugriffs (T1531)
- **ID:** `T1531.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes Entfernen oder Sperren von Konten durch Identifizierung von Massenlöschungen.
Angriff auf Administratorkonten über die Befehlszeilenschnittstelle oder destruktive Kontoaktionen
die aus nicht standardmäßigen Prozesslinien stammen (z. B. Office-Apps, Webserver).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity interne Spearphishing-Erkennung (T1534)
- **ID:** `T1534.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt fortgeschrittene interne Spearphishing-Versuche durch Identifizierung von Anomalien
Programmgesteuerter Zugriff auf die Outlook-MAPI-Schnittstelle, verdächtige untergeordnete Prozesse,
und Befehlszeilen-Flags, die für den Massenversand oder die Einfügung von Anhängen verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Manipulation ungenutzter Dienste (T1535)
- **ID:** `T1535.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Änderung vorhandener Windows-Dienstpfade (ImagePath) in „nicht vertrauenswürdig“.
Standorte oder Binärdateien.Filtert legitime Betriebssystemwartungen und häufige Drittanbieter heraus
Updater, um Warnungen mit hoher Wiedergabetreue zu gewährleisten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Cloud-Konto-Exfil (T1537)
- **ID:** `T1537.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Datenexfiltration über native Cloud-CLI-Tools durch Überwachung
Kontoübergreifende Synchronisierung, manuelle Anmeldeinformationsinjektion in CLI,
und Übertragungen, die von nicht-administrativen Prozesslinien initiiert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Cloud-Service-Dashboard-Erkennung (T1538)
- **ID:** `T1538.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die anomale Generierung föderierter Anmeldetokens und der automatisierten Cloud
Dashboard-Zugriff.Konzentriert sich auf CLI-Befehle, die zur Umgehung von Standard-MFA verwendet werden
über Konsolen-Anmeldetokens und verdächtige Browserstarts von nicht interaktiven Shells.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Websitzungs-Cookie-Diebstahl (T1539)
- **ID:** `T1539.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugten Zugriff auf Browser-Sitzungscookies.Überwacht Nicht-Browser
Prozesse, die sowohl auf „Cookies“- als auch auf „Lokalstatus“-Dateien (Verschlüsselungsschlüssel) zugreifen,
Identifizierung von Exfiltrationsversuchen über LOLBins und verdächtige Skripte.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Pre-OS-Boot-Manipulation (T1542)
- **ID:** `T1542.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte Firmware- oder Bootloader-Änderungen.Monitore für
verdächtiges Mounten der EFI-Partition, unbefugte Nutzung der Firmware
Flash-Tools und UEFI-Variablenmanipulation von nicht standardmäßigen übergeordneten Prozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro ROM-Kit und UEFI-Firmware-Manipulation (T1542.001)
- **ID:** `T1542_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Firmware-Manipulationen durch Überwachung hochriskanter Treiber
Registrierungen und Firmware-Update-Dienstprogramme, die von verdächtigen Unternehmen initiiert wurden
Prozessbäume, die speziell auf den BYOVD- und SPI-Flash-Zugriff abzielen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Manipulation der Ultra-Pro-Komponenten-Firmware (T1542.002)
- **ID:** `T1542_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Modifikationen der Peripherie-Firmware (NIC, SSD, GPU) durch
Identifizieren eigenständiger Flash-Tools, die von einem nicht vertrauenswürdigen Prozess initiiert wurden
Ketten oder nicht standardmäßige Dateispeicherorte.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Bootkit-Persistenz und EFI-Manipulation (T1542.003)
- **ID:** `T1542_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Bootloader-Änderungen durch Überwachung auf BCD-Integritätsumgehungen,
manuelle EFI-Partitionsmontage und verdächtige Boot-Pfad-Umleitung.
Filtert legitime Betriebssystemreparaturen und BitLocker-Vorgänge heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Mainboard-Boot-Image und SPI-Flash-Manipulation (T1542.004)
- **ID:** `T1542_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Firmware-Manipulationen durch Überwachung des Hardwarezugriffs auf niedriger Ebene
Tools und Fahrerregistrierungen, die aus nicht standardmäßigen Prozessketten initiiert werden.
Konzentriert sich auf SPI-Flash-Schreib- und Image-Injection-Versuche.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro DHCP/PXE-Boot-Hijacking (T1542.005)
- **ID:** `T1542_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen der DHCP-Optionen 66 (Boot-Server) und 67 (Bootdateiname).
Angreifer nutzen dies, um Netzwerk-Boot-Anfragen an einen bösartigen TFTP-Server umzuleiten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Benutzer ohne Administratorrechte versuchen, mehrere sensible Windows-Dienste zu stoppen oder zu ändern
- **ID:** `T1543.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt verdächtiges Verhalten, wenn ein Benutzer ohne Administratorrechte versucht, innerhalb eines kurzen Zeitfensters mehrere vertrauliche Windows-Dienste zu stoppen oder zu ändern.Dieses Verhalten wird häufig mit Abwehrmaßnahmen oder Persistenzvorbereitungsaktivitäten in Verbindung gebracht.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro macOS Launch Agent-Persistenzerkennung (T1543.001)
- **ID:** `T1543_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)
- **Beschreibung:** Erkennt die unbefugte Erstellung von Launch Agents durch Überwachung verdächtiger Prozesslinien
und Identifizieren nicht signierter oder skriptbasierter Ausführungsziele innerhalb der .plist.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Systemd-Dienstpersistenz (T1543.002)
- **ID:** `T1543_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)
- **Beschreibung:** Erkennt unbefugte Erstellung oder Änderung von Systemd-Einheiten durch Überwachung
verdächtige Prozessabläufe und ungewöhnliche ausführbare Pfade innerhalb der Dienstdatei.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Nicht autorisierte Installation des Ultra-Pro-Windows-Dienstes (T1543.003)
- **ID:** `T1543_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Erstellung von Windows-Diensten durch Überwachung der Ereignis-ID 7045 und der Prozesserstellung.
Konzentriert sich auf verdächtige Binärpfade, von der Shell erzeugte Dienste und nicht standardmäßige ausführbare Dienstdateien.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Unautorisierter macOS-Startdaemon (T1543.004)
- **ID:** `T1543_004.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)
- **Beschreibung:** Erkennt die unbefugte Erstellung von Systemstart-Daemons durch Überwachung von Dateiereignissen
und Überprüfen der Integrität des Schreibprozesses und der binären Zielsignatur.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Persistenz des Ultra-Pro WMI-Ereignisabonnements (T1546.003)
- **ID:** `T1546.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte WMI-Ereignisabonnements durch Korrelation der Verbrauchertypen mit
verdächtige Befehlszeilenmuster und der Ausschluss vertrauenswürdiger System-Orchestratoren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro File Association-Hijacking (T1546.001)
- **ID:** `T1546_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt durch Überwachung nicht autorisierte Änderungen an Dateizuordnungen in der Registrierung
verdächtige Akteurprozesse und nicht standardmäßige ausführbare Pfade in „Shell\open\command“.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Bildschirmschoner-Persistenzerkennung (T1546.002)
- **ID:** `T1546_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CONTROL.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Bildschirmschoner-Hijacking durch Überwachung der Registrierungsschreibvorgänge in „SCRNSAVE.EXE“.
Filtert GPO-gesteuerte Änderungen heraus und validiert binäre Erweiterungen und vertrauenswürdige Pfade.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Persistenz des WMI-Ereignisabonnements über WMIC oder PowerShell (High Fidelity)
- **ID:** `T1546_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [WMIC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung permanenter WMI-Ereignisabonnements, die für die Persistenz verwendet werden.Die Regel konzentriert sich auf angreifertypische Kombinationen von EventFilter, CommandLineEventConsumer und FilterToConsumerBinding, die über WMIC oder PowerShell im Root\Subscription-Namespace erstellt wurden, schließt jedoch bekannte Unternehmensüberwachungsagenten aus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro AppCert DLL-Persistenzerkennung (T1546.004)
- **ID:** `T1546_004.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [REGEDIT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Registrierung von AppCert-DLLs durch Überwachung des Sitzungsmanagers
Registrierungsschlüssel.Es filtert vertrauenswürdige Systeminstallationsprogramme heraus und erfordert nicht standardmäßige Installationsprogramme
Pfade oder verdächtige Prozesslinien auszulösen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Persistenzerkennung für Granatenfallen (T1546.005)
- **ID:** `T1546_005.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt nicht autorisierte Shell-Trap-Persistenz durch Überwachung von Schreibvorgängen in Shell-Profildateien
Dazu gehören „Trap“-Befehle in Kombination mit verdächtigen Netzwerknutzlasten oder Ausführungsmustern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Mach-O LC_LOAD_DYLIB-Injektion (T1546.006)
- **ID:** `T1546_006.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt unbefugte Änderungen an Mach-O-Binärdateien, um bösartige Dylibs einzuschleusen.
Konzentriert sich auf Nicht-Entwickler-Tools, die Anwendungsbinärdateien ändern, und prüft darauf
verdächtige Dylib-Suchpfade oder nicht signierte Bibliotheksladevorgänge.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Netsh Helper DLL-Persistenz (T1546.007)
- **ID:** `T1546_007.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte Netsh Helper DLL-Registrierungen durch Überwachung von Registrierungsschreibvorgängen
und Befehlszeilenargumente.Filtert bekanntermaßen funktionierende Installationsprogramme und signierte Microsoft-Binärdateien heraus.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro WER SilentProcessExit Persistenz (T1546.008)
- **ID:** `T1546_008.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WINDBG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Persistenz über Windows Error Reporting (WER) SilentProcessExit.
Konzentriert sich auf die Registrierung von „MonitorProcess“-Befehlen, die bei einem Prozess ausgeführt werden
stürzt ab oder wird beendet, mit Ausnahme bekannter Debugging-Umgebungen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro AppInit_DLLs Persistenzerkennung (T1546.009)
- **ID:** `T1546_009.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Persistenz über AppInit_DLLs durch Überwachung von Registrierungsschreibvorgängen
zu den Werten „AppInit_DLLs“ und „LoadAppInit_DLLs“.
Filtert signierte Microsoft-Binärdateien und vertrauenswürdige Systeminstallationsprogramme heraus.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro AppCert DLL-Persistenzerkennung (T1546.010)
- **ID:** `T1546_010.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [REGEDIT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Registrierung von AppCert-DLLs durch Überwachung des Sitzungsmanagers
Registrierungsschlüssel.Es filtert vertrauenswürdige Systeminstallationsprogramme heraus und erfordert nicht standardmäßige Installationsprogramme
Pfade oder verdächtige Prozesslinien auszulösen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Anwendungs-Shimming-Persistenzerkennung (T1546.011)
- **ID:** `T1546_011.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte Shim-Datenbankinstallationen durch Überwachung von sdbinst.exe
Ausführung mit verdächtigen Quellpfaden und direkten Registrierungsschreibvorgängen in InstalledSDB.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro IFEO Debugger Hijacking-Erkennung (T1546.012)
- **ID:** `T1546_012.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [ATBROKER.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Debugger-Injection über Image File Execution Options (IFEO).
Filtert legitime Entwicklertools heraus und konzentriert sich auf Systembinärdateien mit hohem Risiko
und Eingabehilfen (Sticky Keys, Utility Manager).

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro PowerShell-Profilinjektionserkennung (T1546.013)
- **ID:** `T1546_013.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte automatisierte Änderungen an PowerShell-Profilen.
Filtert legitime manuelle Bearbeitung über Texteditoren heraus und konzentriert sich auf
Programmatische Injektion von Shells oder nicht standardmäßigen übergeordneten Prozessen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Persistenz des Ultra-Pro WMI-Ereignisabonnements (T1546.014)
- **ID:** `T1546_014.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte WMI-Ereignisabonnements durch Überwachung der Erstellung
EventFilter und Befehls-/Skriptkonsumenten.Filtert bekannte administrative Informationen heraus
Tools und konzentriert sich auf die nicht standardmäßige Skriptausführung.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtiges COM-Hijacking zur Persistenz auf Benutzerebene (High Fidelity)
- **ID:** `T1546_015.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige COM-Hijacking-Versuche, die für die Persistenz auf Benutzerebene verwendet werden, indem Registrierungsänderungen von CLSID InprocServer32- und LocalServer32-Einträgen überwacht werden, die auf nicht standardmäßige Ausführungspfade verweisen.Die Regel konzentriert sich auf HKCU-Änderungen in Kombination mit Skripting oder LOLBin-Ausführung, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Benutzerdefinierte Aktionspersistenz des Ultra-Pro MSI-Installationsprogramms (T1546.016)
- **ID:** `T1546_016.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von msiexec.exe erzeugt werden und von nicht standardmäßigen Prozessen stammen
Verzeichnisse.Dies zielt auf böswillige benutzerdefinierte MSI-Aktionen ab, die zur Persistenz oder zur Rechteausweitung verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Es wird ein verdächtiger Start- oder Anmelde-Autorun durchgeführt
- **ID:** `T1547.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Änderungen an verdächtigen Registrierungs- oder Startordnern, die zum Speichern von Daten verwendet werden, und konzentriert sich dabei auf nicht standardmäßige Pfade und verdächtige ausführbare Dateien.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Änderung des Registrierungsschlüssels für Benutzerpersistenz (High Fidelity)
- **ID:** `T1547_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Registrierungsänderungen, die zum Einrichten einer Persistenz auf Benutzerebene über die Windows-Schlüssel „Run“ und „RunOnce“ verwendet werden.Die Regel konzentriert sich auf nicht standardmäßige ausführbare Speicherorte in Kombination mit Skript-Engines, um Fehlalarme bei legitimen Softwareinstallationen zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Persistenz des High-Fidelity-LSA-Authentifizierungspakets
- **ID:** `T1547_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das Hinzufügen nicht autorisierter Authentifizierungspakete im LSA-Registrierungsschlüssel.
Angreifer nutzen dies für die Persistenz auf SYSTEM-Ebene und das Sammeln von Anmeldeinformationen.
Diese Regel filtert Standard-Windows-Pakete und überwacht DLLs außerhalb von System32.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Persistenz des High-Fidelity-Zeitanbieters (T1547.003)
- **ID:** `T1547_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die Registrierung eines neuen Windows-Zeitanbieters.
Angreifer nutzen dies für die Persistenz auf SYSTEM-Ebene, indem sie eine schädliche DLL in svchost.exe laden.
Diese Regel filtert Standard-Windows-DLLs und zielt auf Nicht-System32-Pfade ab.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Winlogon-Hilfsprogramm-DLL-Persistenz (T1547.004)
- **ID:** `T1547_004.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte Änderungen an Winlogon-Hilfsschlüsseln (Userinit, Shell).
Konzentriert sich auf das „Anhängen“ mehrerer ausführbarer Dateien oder die Verwendung nicht standardmäßiger Systempfade.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-SSP-DLL-Persistenz (T1547.005)
- **ID:** `T1547_005.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das Hinzufügen nicht autorisierter DLLs zum Registrierungsschlüssel der LSA-Sicherheitspakete.
Angreifer nutzen dies zur Persistenz und zum Diebstahl von Klartext-Anmeldeinformationen.
Filtert Standard-Windows-SSPs und warnt bei nicht verwalteten Änderungen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Registrierung des High-Fidelity-Kernel-Treibers (T1547.006)
- **ID:** `T1547_006.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Registrierung eines neuen Kernelmodus-Treiberdienstes.
Angreifer nutzen dies zur Persistenz auf Rootkit-Ebene und zur Deaktivierung von Sicherheitstools.
Optimiert, um Treiber in nicht standardmäßigen Pfaden und verdächtige manuelle Diensterstellung zu kennzeichnen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Browser-Sitzungspersistenz (T1547.007)
- **ID:** `T1547_007.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen an Browser-Sitzungs- oder Einstellungsdateien durch Nicht-Browser-Prozesse.
Angreifer nutzen dies, um Browser zu zwingen, beim Start bösartige URLs zu öffnen, um deren Persistenz zu gewährleisten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-LSASS-Treiber/Paketpersistenz (T1547.008)
- **ID:** `T1547_008.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Registrierung neuer LSA-Plugins, Benachrichtigungspakete oder Treiber.
Angreifer nutzen dies, um Schadcode in den Prozess lsass.exe zu laden
Persistenz und Echtzeit-Erfassung von Anmeldeinformationen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Erkennung von Verknüpfungsänderungen
- **ID:** `T1547_009.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung oder Änderung von LNK-Dateien durch verdächtige Prozesse (PowerShell, CMD usw.)
in Startordnern oder Taskleistenpfaden.Dies ist eine gängige Technik zur Persistenz.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity AppCert DLL-Persistenz (T1547.010)
- **ID:** `T1547_010.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Registrierung von AppCert-DLLs.Diese DLLs werden geladen
Jeder Prozess, der CreateProcess aufruft, macht ihn zu einem leistungsstarken Persistenz- und Injektionsvektor.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Shimming-Persistenz für High-Fidelity-Anwendungen (T1547.011)
- **ID:** `T1547_011.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Installation einer neuen Shim-Datenbank (.sdb) mithilfe von sdbinst.exe.
Angreifer verwenden Shims, um DLLs einzuschleusen, Sicherheitskontrollen zu umgehen oder die Persistenz aufrechtzuerhalten.
Diese Regel filtert seriöse Installationsprogramme und markiert verdächtige Eltern-Kind-Beziehungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-COM-Hijacking-Persistenz (T1547.012)
- **ID:** `T1547_012.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung von COM-Objekthandlern in HKCU, die auf verdächtige Speicherorte verweisen.
Konzentriert sich auf InprocServer32- und LocalServer32-Schlüssel, die primäre Ziele für Hijacking sind.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-E-Mail-Client-Helper-Persistenz (T1547.013)
- **ID:** `T1547_013.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Registrierung nicht autorisierter E-Mail-Client-Helper oder COM-Add-Ins.
Konzentriert sich auf DLLs, die über vom Benutzer beschreibbare Pfade und verdächtige Registrierungsautoren registriert wurden.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity Active Setup Persistence (T1547.014)
- **ID:** `T1547_014.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung oder Änderung von Active Setup „StubPath“-Registrierungsschlüsseln durch Nicht-Systemprozesse.
Angreifer nutzen dies, um eine Persistenz zu erreichen, die einmal pro Benutzer bei der Anmeldung ausgeführt wird.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-COM-Hijacking-Persistenz (T1547.015)
- **ID:** `T1547_015.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SCROBJ.DLL](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung von COM-Objekthandlern in HKCU, die auf verdächtige,
Vom Benutzer beschreibbare Speicherorte.Angreifer kapern CLSIDs, um eine heimliche Persistenz zu erreichen
innerhalb legitimer Systemprozesse wie explorer.exe.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Berechtigungsausweitung durch Registry-Hijacking (T1548.002)
- **ID:** `T1548.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [COMPUTERDEFAULTS.EXE](https://lolbas-project.github.io/lolbas/), [EVENTVWR.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt UAC-Umgehungsversuche durch Überwachung nicht autorisierter Registrierungsänderungen
zum Öffnen von Shell-Befehlen.Filtert speziell nach vertrauenswürdigen Installateuren und
systeminitiierte Änderungen, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Setuid/Setgid-Bit-Manipulation (T1548.001)
- **ID:** `T1548_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt eine unbefugte SUID/SGID-Bit-Eskalation durch Überwachung von chmod/chown
Ausführung in weltweit beschreibbaren Verzeichnissen und verdächtige Aufklärung
Muster, während legitime Paketmanager herausgefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## UAC-Umgehung über Fodhelper Registry Hijack (High Fidelity)
- **ID:** `T1548_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt UAC-Umgehungsversuche, bei denen fodhelper.exe missbraucht wird, indem die Registrierungsentführung des ms-settings-Protokolls in Kombination mit der Ausführung verdächtiger untergeordneter Prozesse überwacht wird.Diese Regel konzentriert sich auf die automatische Erhöhung des Benutzerkontexts, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Sudo-Manipulation und Sudo-Missbrauch (T1548.003)
- **ID:** `T1548_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt nicht autorisierte Sudoers-Dateiänderungen und Sudo-Caching-Missbrauch.
Konzentriert sich auf NOPASSWD-Ergänzungen, die Manipulation von timestamp_timeout und
gefährliche Umgebungsvariableninjektionen wie LD_PRELOAD.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-AppleScript-Berechtigungseskalation (T1548.004)
- **ID:** `T1548_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt nicht autorisierte AppleScript-Erhöhungsversuche.Konkret überwacht
Osascript-Ausführung mit „Administratorrechten“ von einem nicht vertrauenswürdigen übergeordneten Element
Prozesse wie Browser, Office-Suiten oder temporäre Verzeichnisse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro SUID-Desktop-Eintrag und Missbrauch von Verknüpfungen (T1548.005)
- **ID:** `T1548_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)
- **Beschreibung:** Erkennt unbefugte Änderungen an XDG-Desktopeinträgen oder versuchten Verknüpfungen
um SUID-Binärdateien auszuführen oder pkexec zur Rechteausweitung zu nutzen.
Konzentriert sich auf Änderungen in vom Benutzer beschreibbaren Verzeichnissen durch nicht vertrauenswürdige Prozesse.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Alternatives Authentifizierungsmaterial (T1550)
- **ID:** `T1550.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die Verwendung gestohlener Hashes oder Tickets für Lateral Movement durch Identifizierung
NTLM/Kerberos-Protokollanomalien, wie RC4-Downgrades und eingeschränkter Administrator
Anmeldetypen.Filtert legitime Systemverwaltungstools heraus.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Missbrauch von Ultra-Pro High-Fidelity-Anwendungszugriffstoken (T1550.001)
- **ID:** `T1550_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Diebstahl von Anwendungszugriffstokens durch Identifizierung unbefugter Zugriffe
IdentityCRL- und TokenBroker-Speicher sowie die Verwendung von Inhabertokens in Befehlszeilendienstprogrammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Pass-the-Hash-Erkennung (T1550.002)
- **ID:** `T1550_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt Pass-the-Hash (PtH) durch Identifizierung einer anomalen NTLM-Loopback-Authentifizierung.
eingeschränkte Administrator-Anmeldetypen (LogonType 9 über seclogo) und bekannte Anmeldeinformationsinjektion
Tool-Muster, während legitime Dienstkonten ausgeschlossen werden.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Pass-the-Ticket-Erkennung (T1550.003)
- **ID:** `T1550_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt Pass-the-Ticket (PtH) durch Identifizierung von Kerberos-Verschlüsselungs-Downgrades (RC4),
anomale Ticket-Flags (Rubeus/Mimikatz-Standards) und nicht autorisierte Ticket-Injektion
in den LSA-Prozessspeicher.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Pass-the-Session-Erkennung (T1550.004)
- **ID:** `T1550_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugten Websitzungsdiebstahl durch Überwachung auf Nicht-Browser-Prozesse
Zugriff sowohl auf den verschlüsselten AES-Schlüssel (Local State) als auch auf die Cookie-Datenbank (Cookies/Netzwerk).
Schließt legitime Browser-Update- und Synchronisierungsmechanismen aus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Erkennung ungesicherter Anmeldeinformationen (T1552)
- **ID:** `T1552.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Erkennung von Anmeldeinformationen in Dateien, der Registrierung und dem Shell-Verlauf.
Verwendet erweiterte Korrelation zwischen Suchtools (findstr, grep, PowerShell),
sensible Dateierweiterungen und Schlüsselwörter mit hoher Entropie.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Anmeldeinformationen bei der Dateierkennung (T1552.001)
- **ID:** `T1552_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt gezielte, rekursive Suchen nach Anmeldeinformationen in Konfigurationsdateien und Skripten.
Korreliert Suchtools (findstr, grep, PowerShell) mit Dateierweiterungen mit hohem Risiko
und anomale übergeordnete Prozesse, um Fehlalarme durch Entwickler-/Administratoraktivitäten zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Anmeldeinformationen bei der Registrierungserkennung (T1552.002)
- **ID:** `T1552_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte, rekursive oder Massenextraktion vertraulicher Registrierungsschlüssel
Enthält Anmeldeinformationen (PuTTY-, WinSCP-, RDP-, LSA-Geheimnisse).Korreliert die Suche
Befehle mit verdächtigen übergeordneten Prozessen, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Shell-Verlauf und Konsolenerkennung (T1552.003)
- **ID:** `T1552_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BASH.EXE](https://lolbas-project.github.io/lolbas/), [CONHOST.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes Extrahieren von Shell-Verlaufsdateien (.bash_history, ConsoleHost_history.txt).
Konzentriert sich auf Nicht-Shell-Prozesse, die auf diese Dateien zugreifen, und die Verwendung von Exfiltrationsfunktionen
Befehle (Base64, Curl, Umleitung) kombiniert mit Verlaufsdateipfaden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Private Key Discovery (T1552.004)
- **ID:** `T1552_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [SSH.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Entdeckung privater kryptografischer Schlüssel (SSH, PGP, Zertifikate).
Konzentriert sich auf die Suche nach Inhalten in der Befehlszeile nach privaten Schlüsselheadern und rekursiv
Verzeichnisdurchquerung durch nicht vertrauenswürdige Prozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Cloud Credential Discovery (T1552.005)
- **ID:** `T1552_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die unbefugte Extraktion von Cloud-Anmeldeinformationen (AWS, Azure, GCP) aus der lokalen Umgebung
Konfigurationsdateien.Filtert legitime CLI-Nutzung und konzentriert sich auf anormales Prozessverhalten
wie Umleitung, Verschlüsselung oder Zugriff von Webservern und Remote-Shells.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-GPP-Passworterkennung (T1552.006)
- **ID:** `T1552_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte manuelle oder skriptgesteuerte Erkennung von Passwörtern in den Gruppenrichtlinieneinstellungen.
Konzentriert sich auf systemfremde Prozesse, die darin Zeichenfolgensuchen nach „cpassword“ durchführen
die SYSVOL-Freigabe, die Tools wie PowerSploit, Empire oder die manuelle LOLBin-Nutzung identifiziert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Container Secret Discovery (T1552.007)
- **ID:** `T1552_007.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die gezielte Entdeckung von Geheimnissen (K8s-Token, Cloud-Schlüssel, Env-Variablen) in Containern.
Filtert legitime Einstiegspunktskripte und Überwachungsagenten und konzentriert sich dabei auf
interaktive Shell-Sitzungen und anomale Befehlsverkettung (z. B. env | grep).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-GPP-Passworterkennung (T1552.008)
- **ID:** `T1552_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Erkennung verschlüsselter Passwörter (cpassword) in XML-Dateien mit Gruppenrichtlinieneinstellungen.
Filtert legitime GPO-Engine-Aktivitäten, indem der Schwerpunkt auf der Suche nach Befehlszeilenzeichenfolgen liegt
stammen aus interaktiven oder Remote-Shells.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Subvert Trust Controls (T1553)
- **ID:** `T1553.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, Vertrauenskontrollen durch die erzwungene Installation von Stammzertifikaten zu untergraben
oder Ändern von Sicherheitszonen/MotW-Einstellungen aus nicht standardmäßigen Prozessen und Pfaden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity macOS Gatekeeper und Quarantäne-Bypass (T1553.001)
- **ID:** `T1553_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt Versuche, macOS Gatekeeper zu deaktivieren oder programmgesteuert zu entfernen
Quarantäneattribut aus Dateien.Konzentriert sich auf nicht interaktive Shells und
verdächtige Pfade, um Fehlalarme von Entwicklern zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelles High-Fidelity-SIP-Hijacking und Trust-Subversion (T1553.002)
- **ID:** `T1553_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen an Subject Interface Packages (SIP) und Trust Providern.
Konzentriert sich auf DLL-Registrierungen von nicht standardmäßigen oder vom Benutzer beschreibbaren Pfaden
gängige Technik, um bösartige Binärdateien als gültig signiert erscheinen zu lassen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Windows Catalog Database Subversion (T1553.003)
- **ID:** `T1553_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte Ergänzungen zur Windows-Katalogdatenbank.
Konzentriert sich auf Nicht-Systemkonten und verdächtige Quellpfade, die verhindert werden sollen
verhindert, dass nicht signierte Malware als vom Betriebssystem gültig signiert angezeigt wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Root-Zertifikat-Injektion (T1553.004)
- **ID:** `T1553_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die programmgesteuerte Installation eines Stammzertifikats im
Vertrauenswürdiger Root-Store.Konzentriert sich auf Befehlszeilenargumente mit hohem Risiko und
verdächtige Prozesslinien, um häufige Fehlalarme zu eliminieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity MotW Bypass & Zone Subversion (T1553.005)
- **ID:** `T1553_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die programmatische Entfernung oder Subversion des Mark of the Web (MotW).
Konzentriert sich auf nicht-interaktive ADS-Manipulation und verdächtige Registrierung
Änderungen, die die Sicherheitszoneneinstellungen herabsetzen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Codeintegrität und DSE-Subversion (T1553.006)
- **ID:** `T1553_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, die Windows-Codeintegrität und Driver Signature Enforcement (DSE) zu untergraben.
Konzentriert sich auf BCDEDIT-Flags und Registrierungsänderungen, die nicht signierte Kernel-Treiber zulassen
zu laden, während legitime Betriebssystemwartungs- und Installationsprogramme herausgefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Kompromittierung der Binärintegrität des Ultra-Pro-Clients (T1554)
- **ID:** `T1554.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Änderung oder Ersetzung vertrauenswürdiger Client-Binärdateien durch nicht autorisierte Prozesse.
Konzentriert sich auf Fälle, in denen der Schreibvorgang ein LOLBin ist oder der Datei eine gültige Herstellersignatur fehlt.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Nicht-Browser-Prozesszugriff auf Browser-Anmeldeinformationsspeicher (High Fidelity)
- **ID:** `T1555.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Zugriffe auf Browser-Anmeldeinformationsspeicherdateien durch Nicht-Browser-Prozesse.Die Regel konzentriert sich auf den Lesezugriff auf bekannte Anmeldeinformationsdatenbanken und verdächtigen Ausführungskontext, um Fehlalarme durch Backup-Agenten, Antivirensoftware und Browser-Updates zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Vault-Zugangsdatenerfassung (T1555.001)
- **ID:** `T1555_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die unbefugte Extraktion von Anmeldeinformationen aus Windows Vault durch Überwachung
Befehlszeilen-Datenumleitung, verdächtige API-Zeichenfolgen und Nicht-Standard
Prozesslinien und filtert gleichzeitig legitime Browser- und Systemupdate-Rauschen heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Sicherheitsspeicher-Dumping (T1555.002)
- **ID:** `T1555_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt unbefugte Versuche, den Speicher des „gesicherten“ Prozesses zu sichern oder zu lesen.
Der Schwerpunkt liegt auf der Verwendung von nicht standardmäßigen Debuggern und der Ausrichtung auf Speicherzuordnungstools
securityd, während von Apple signierte Diagnoseprogramme strikt gefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Browser-Anmeldedatenerfassung (T1555.003)
- **ID:** `T1555_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [ESENTUTL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugten Zugriff und Extraktion von Browser-Anmeldeinformationsdatenbanken.
Es zielt auf Befehlszeilenmissbrauch (Kopieren/Archivieren) und verdächtige Interpreter ab
Verhalten, das auf sensible Profildateien wie „Anmeldedaten“ oder „Cookies“ abzielt.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Windows Credential Manager Harvesting (T1555.004)
- **ID:** `T1555_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CMDKEY.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das unbefugte Sammeln von Anmeldeinformationen über cmdkey.exe durch Identifizierung
verdächtige Befehlszeilenumleitung, nicht interaktive übergeordnete Prozesse,
und bekannte Signaturen des Credential-Dumping-Tools.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Passwort-Manager-Extraktion (T1555.005)
- **ID:** `T1555_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugten Zugriff oder Exfiltration von Passwort-Manager-Datenbanken
durch die Identifizierung verdächtiger Dateivorgänge (Kopieren, Archivieren) und
Nicht vertrauenswürdige Prozesslinien, die auf .kdbx-, .opvault- und andere Tresordateien abzielen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Cloud Secret Harvesting (T1555.006)
- **ID:** `T1555_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugten Zugriff oder die Ausschleusung von Anmeldeinformationen von Cloud-Anbietern (AWS, Azure, GCP).
Es zielt speziell auf den Zugriff auf Befehlszeilentools (Archiver, Interpreter) ab
sensible Konfigurationspfade unter Ausschluss offizieller Cloud-CLI-Binärdateien und bekannter DevOps-Agenten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Exploit-Authentifizierungsprozess-Hijacking über verdächtige DLL-Registrierung
- **ID:** `T1556.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt eine ausnutzbare Änderung des Windows-Authentifizierungsprozesses, bei der ein Nicht-Systemprozess eine neue authentifizierungsbezogene DLL aus einem vom Benutzer beschreibbaren Verzeichnis in LSA-, SSP- oder Anmeldeinformationsanbieter-Registrierungsspeicherorten registriert, was ein starkes Anzeichen für das Abfangen von Anmeldeinformationen ist.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Exploit-Grade-Hijacking von Sicherheits-Support-Anbietern (LSA SSP)
- **ID:** `T1556_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt SSP-Hijacking (Security Support Provider) mit Ausnutzungsgrad, indem eine unbefugte Änderung des Registrierungswerts der LSA-Sicherheitspakete identifiziert wird, um eine neue, nicht zum System gehörende DLL aus einem vom Benutzer beschreibbaren Verzeichnis durch einen nicht vertrauenswürdigen Prozess oder ein nicht vertrauenswürdiges Konto zu registrieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Exploit-Grade-Passwortfilter-DLL-Hijacking über LSA-Benachrichtigungspakete
- **ID:** `T1556_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Installation einer schädlichen Passwortfilter-DLL mit Ausnutzungsgrad, indem eine unbefugte Änderung des Registrierungswerts der LSA-Benachrichtigungspakete identifiziert wird, um eine neue DLL hinzuzufügen, die sich in einem vom Benutzer beschreibbaren Verzeichnis durch einen nicht vertrauenswürdigen Prozess oder ein nicht vertrauenswürdiges Konto befindet.Dieses Verhalten weist stark auf das Abfangen von Anmeldeinformationen auf Domänencontrollern hin.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003)
- **ID:** `T1556_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt unbefugte Änderungen an der PAM-Konfiguration oder an Binärmodulen
durch die Identifizierung von Nicht-Paketmanager-Schreibvorgängen in /etc/pam.d/ und /lib/security/.
Filtert speziell nach automatisierten Konfigurationstools, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Hijacking der Netzwerkgeräteauthentifizierung (T1556.004)
- **ID:** `T1556_004.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Kritisch hoch (SIEM-Killerkategorie!)
- **Beschreibung:** Erkennt nicht autorisierte Änderungen an AAA (Authentifizierung, Autorisierung und Buchhaltung)
Einstellungen oder lokale Benutzerdatenbanken auf Netzwerkgeräten.Konzentriert sich auf manuelle Bypässe
Wird außerhalb autorisierter Verwaltungssubnetze durchgeführt.

#### 🚨 Reaktions-Playbook
1. **IP-Reputation: Überprüfen Sie die Remote-IP-Adresse in Reputationsdatenbanken.**
2. **Verkehrsanalyse: Untersuchen Sie die Menge der gesendeten Daten.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro SID-Verlaufsinjektionskorrelation (T1556.005)
- **ID:** `T1556_005.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die Injektion hochprivilegierter SIDs in das sIDHistory-Attribut eines Benutzers.
Dies zielt auf das Szenario „Ghost Admin“ ab, bei dem ein Benutzer Domänenadministratorrechte erhält
ohne Mitglied der Gruppe zu sein.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Entra ID MFA-Methoden-Hijacking (T1556.006)
- **ID:** `T1556_006.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt risikoreiche Änderungen an MFA-Methoden in Entra ID durch Korrelation
erfolgreiche Methodenänderungen mit verdächtigen Einstiegspunkten oder administrativen Anomalien.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Hybrid-Identitätssynchronisierungsmanipulation (T1556.007)
- **ID:** `T1556_007.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Manipulation des Entra ID (ehemals Azure AD) Connect-Synchronisierungsprozesses.
Konzentriert sich auf den Missbrauch von MSOL-Konten durch nicht synchronisierte Server und die unbefugte Verwendung von ADSync PowerShell.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Netzwerk-zu-Cloud-Auth-Hijacking (T1556.008)
- **ID:** `T1556_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt risikoreiche Änderungen an Unternehmensanwendungen und bedingtem Zugriff
Richtlinien, die von Netzwerkgeräten (VPNs, Firewalls) verwendet werden.Konzentriert sich auf MFA-Umgehungen
und unbefugte Hinzufügung von Anmeldeinformationen zu Dienstprinzipalen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Adversary-in-the-Middle (T1557)
- **ID:** `T1557.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte Systemkonfigurationsänderungen, die für AiTM-Angriffe erforderlich sind.
einschließlich der Aktivierung der IP-Weiterleitung und der Ausführung des LLMNR/NetBIOS-Poisoning-Tools,
Gleichzeitig werden legitime VPN- und Virtualisierungsgeräusche herausgefiltert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity LLMNR/NBT-NS-Vergiftung (T1557.001)
- **ID:** `T1557_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt LLMNR/NBT-NS-Vergiftung und SMB-Relay-Tools (Responder, Inveigh) durch Identifizierung
Nicht autorisierte Prozesse versuchen, eine Verbindung zu Netzwerkauflösungsports herzustellen, kombiniert mit
spezifische Befehlszeilensignaturen des Angreifers.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity ARP-Vergiftungserkennung (T1557.002)
- **ID:** `T1557_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt nicht autorisierte ARP-Poisoning-Versuche durch Überwachung der IP-Weiterleitung
Aktivierung und Ausführung von Paketmanipulationstools von Unvertrauenswürdigen
Standorte, insbesondere das Herausfiltern von Virtualisierungs- und VPN-Rauschen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity DHCP-Spoofing-Erkennung (T1557.003)
- **ID:** `T1557_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt nicht autorisierte DHCP-Spoofing-Versuche, indem Prozesse identifiziert werden, die versuchen, einzugreifen
als betrügerischer DHCP-Server.Es sucht speziell nach Gateway-/DNS-Hijack-Argumenten
kombiniert mit nicht vertrauenswürdigen Prozessstandorten und Nicht-Systembenutzern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Kerberos-Angriffserkennung (T1558)
- **ID:** `T1558.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt raffiniertes Fälschen und Sammeln von Kerberos-Tickets.
Konzentriert sich auf das Downgrade der Verschlüsselung (RC4/0x17), gezielte Service-Ticket-Anfragen (Kerberoasting),
und anstößige Tool-Artefakte, während gleichzeitig legitimes LSASS und Systemverhalten gefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Profi-High-Fidelity-Golden-Ticket-Fälschung und -Injektion (T1558.001)
- **ID:** `T1558_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung und Injektion gefälschter Kerberos-TGTs (Golden Tickets).
Konzentriert sich auf das obligatorische Vorhandensein des KRBTGT-Hash- oder AES-Schlüssels in Befehlszeilen.
kombiniert mit Ticket-Injection-Mustern (Pass-the-Ticket).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Silber-Ticketfälschung und -Injektion (T1558.002)
- **ID:** `T1558_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung und Einschleusung gefälschter Kerberos-Service-Tickets (Silver-Tickets).
Konzentriert sich auf das obligatorische Vorhandensein dienstspezifischer SPNs (cifs, mssql, http)
und die Bereitstellung von Dienstkonto-Hashes in der Befehlszeile.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Kerberos TGS-Ticketanfrage (Kerberoasting)
- **ID:** `T1558_003.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt verdächtige Kerberos Service Ticket (TGS)-Anfragen, die auf einen Kerberoasting-Angriff hinweisen können.Die Regel konzentriert sich auf schwache Verschlüsselungstypen (RC4) und filtert allgemeine rechtliche Störungen heraus.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity AS-REP-Röstung und LDAP-Enumeration (T1558.004)
- **ID:** `T1558_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt AS-REP-Roasting-Angriffe durch Überwachung auf bestimmte gezielte LDAP-Abfragen
das DONT_REQ_PREAUTH-Bit (4194304) und anstößige Tool-Parameter, die für verwendet werden
Hash-Extraktion (Rubeus, Impacket, PowerView).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Indirekte IPC- und COM-Ausführung mit hoher Wiedergabetreue
- **ID:** `T1559.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige indirekte Prozesserstellung über COM/DDE/WMI.
Konzentriert sich auf „verwaiste“ Prozesse, die von einer Office-App oder einem Browser ausgelöst werden
ein System-Proxy zum Ausführen von Code, der die standardmäßige Eltern-Kind-Überwachung umgeht.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Pipeline-Erstellung im Zusammenhang mit Post-Exploitation-Tools (High Fidelity)
- **ID:** `T1559_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Hochpräzise Erkennung der Entstehung verdächtiger benannter Pipelines, die häufig mit lateralen Bewegungen und Post-Exploitation-Frameworks verbunden sind.Die Regel kombiniert bekannte bösartige Pipeline-Namen, zufällige Pipeline-Muster, LOLBin-Ausführungskontext und strenge Whitelists, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Office-DDE-Kontextanomalie
- **ID:** `T1559_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das Spawnen verdächtiger Prozesse über Microsoft Office Dynamic Data Exchange (DDE).
Filtert legitime Finanzdaten-Links (Excel) und konzentriert sich auf den Start von Office-Apps
Interpreter oder LOLBins mit DDE-spezifischen Befehlszeilenmarkierungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Hypervisor-API und VM-Escape-Forschung
- **ID:** `T1559_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Interaktionen mit Hypervisor-APIs und Diagnosetools.
Konzentriert sich auf die manuelle Ausführung über interaktive Shells und verdächtige Befehlszeilen
Parameter im Zusammenhang mit VM-Escape oder Sandbox-Umgehung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Archivierung von Daten zu Exfiltrationszwecken
- **ID:** `T1560.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Komprimierung und Archivierung von Dateien (7z, rar, tar, PowerShell), insbesondere wenn ein Passwortschutz verwendet wird oder verdächtige temporäre Verzeichnisse als Ziele verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Datenarchivierung für Exfiltration (T1560.001)
- **ID:** `T1560_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt erweiterte Datenbereitstellung zur Exfiltration durch Überwachung auf hohe Entropie
Archiverstellung, ungewöhnliche Volume-Aufteilung und Passwortschutz
Komprimierung, die aus nicht-administrativen oder interaktiven Shell-Kontexten stammt.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Datenarchivierung über die Bibliothek (T1560.002)
- **ID:** `T1560_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt erweitertes Daten-Staging zur Exfiltration mithilfe von .NET/PowerShell
Komprimierungsbibliotheken.Filtert die Unternehmensautomatisierung durch Analyse
Abstammung des übergeordneten Prozesses, Befehlszeilen-Entropie und Integritätsebenen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Archiv über benutzerdefinierte Methode (T1560.003)
- **ID:** `T1560_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die benutzerdefinierte Datenerfassung durch Überwachung des Dateizugriffs auf Byte-Ebene
kombiniert mit manueller Kodierung (XOR, Base64) aus
interaktive Shells oder verdächtige übergeordnete Prozesse wie Webserver.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Disk Wipe (T1561)
- **ID:** `T1561.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche zur Festplattenzerstörung auf niedriger Ebene (MBR-Überschreibung, Partitionslöschung)
durch Überwachung auf unformatierte Festplattenzugriffskennungen und destruktive CLI-Argumente
die aus nicht standardmäßigen übergeordneten Prozessen stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Datenträgerinhaltslöschung (T1561.001)
- **ID:** `T1561_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das Löschen von Festplatteninhalten auf niedriger Ebene durch Überwachung auf direkte physische Geräte
Zugriffskennungen und destruktive Überschreibparameter, insbesondere Filterung
Bereitstellung bekanntermaßen guter Verwaltungs-, Sicherheits- und Imaging-Tools.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Disk Structure Wipe (T1561.002)
- **ID:** `T1561_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Zerstörung der Festplattenstruktur auf niedriger Ebene (Löschen der Partitionstabelle, Überschreiben des MBR).
durch Überwachung auf destruktive CLI-Argumente und unverfälschte Gerätezugriffszeichenfolgen
von nicht standardmäßigen übergeordneten Prozessen oder nicht vertrauenswürdigen Speicherorten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Beendigung von Sicherheitsdiensten
- **ID:** `T1562.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, kritische Sicherheitsdienste (Antivirus, EDR, Firewall) mithilfe von Tools wie net.exe, sc.exe oder PowerShell zu stoppen.Dies ist eine offensive Aktivität, die darauf abzielt, den Schutz zu beseitigen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Deaktivieren oder ändern Sie den Windows Defender-Schutz mit PowerShell
- **ID:** `T1562_001.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt, wenn Angreifer versuchen, PowerShell zu verwenden, um Windows Defender-Einstellungen zu ändern, z. B. den Echtzeitschutz zu deaktivieren oder Ausnahmen hinzuzufügen.Mit dieser Technik wird der Schutz umgangen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Deaktivieren Sie die Windows-Ereignisprotokollierung (T1562.002)
- **ID:** `T1562_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Versuche, den Windows-Ereignisprotokolldienst zu deaktivieren oder zu beeinträchtigen.
Konzentriert sich auf Dienstabhängigkeitssabotage, registrierungsbasierte Kanaldeaktivierung,
und heimliche Wevtutil-Nutzung durch Nicht-Systemprozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Beeinträchtigung der Ultra-Pro High-Fidelity-Befehlsverlaufsprotokollierung (T1562.003)
- **ID:** `T1562_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Versuche, die Protokollierung des Befehlsverlaufs zu unterdrücken oder umzuleiten.
Konzentriert sich auf den Missbrauch von Set-PSReadLineOption (SaveNothing, $null-Umleitung)
und Konsolenpufferunterdrückung, um eine forensische Wiederherstellung von Befehlen zu verhindern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Firewall-Änderung über Netsh.exe
- **ID:** `T1562_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt, wenn Angreifer das Tool „netsh.exe“ verwenden, um Windows-Firewallregeln zu ändern oder neue zulässige Regeln hinzuzufügen.Dies bezieht sich häufig auf Impair Defenses.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Indikatorblockierung und Telemetrie-Stummschaltung (T1562.006)
- **ID:** `T1562_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Versuche, die Sicherheitsüberwachung durch die Deaktivierung von ETW-Anbietern zum Schweigen zu bringen.
Manipulation der Ereignisweiterleitung (WEF) oder Verwendung von Host-Firewalls zur Blockierung von EDR/AV
Cloud-Reputation- und Telemetrie-Endpunkte.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Beeinträchtigung der Ultra-Pro High-Fidelity Cloud Firewall (T1562.007)
- **ID:** `T1562_007.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt nicht autorisierte oder gefährliche Änderungen an Cloud-Sicherheitsgruppen und Firewalls.
Konzentriert sich auf „Any-Any“-Regeln (0.0.0.0/0), Root-Benutzeraktivität und Änderungen
von nicht standardmäßigen Verwaltungstools oder IPs stammen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Beeinträchtigung der Ultra-Pro High-Fidelity-Cloud-Protokollierung (T1562.008)
- **ID:** `T1562_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt kritische Änderungen an der Cloud-Protokollierung (CloudTrail, Azure Activity).
Sichtbarkeitslücken schaffen.Der Schwerpunkt liegt auf der Löschung von Spuren und der Verschlüsselung von Protokolldateien
Deaktivierung und Manipulation auf Speicherebene durch nicht automatisierte Identitäten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Safe Mode Defense Evasion (T1562.009)
- **ID:** `T1562_009.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RESET.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, das System in den abgesicherten Modus zu zwingen, um Sicherheitskontrollen zu umgehen.
Konzentriert sich auf die Bcdedit-Manipulation in Kombination mit sofortigen erzwungenen Neustarts und
Registrierungsbasierter Dienstausschluss innerhalb des SafeBoot-Schlüssels.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Verteidigungs-Downgrade-Angriff (T1562.010)
- **ID:** `T1562_010.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, die Systemverteidigung herunterzustufen, um moderne Sicherheitskontrollen zu umgehen.
Zielt auf die Erzwingung der PowerShell v2.0-Engine (AMSI-Umgehung) und auf Registrierungsbasis ab
Schwächung der Authentifizierungs- und Verschlüsselungsprotokolle.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Virtualisierung und Sandbox-Umgehung (T1564.011)
- **ID:** `T1562_011.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezieltes Umgebungs-Fingerprinting, das von Malware zur Erkennung von Virtualisierung verwendet wird.
Sandboxes oder Analyseumgebungen.Konzentriert sich auf WMI-Hardwareabfragen und MAC-Adressen-OUI
Überprüfungen und VM-spezifische Treibersuchen aus nicht vertrauenswürdigen Prozessketten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Beeinträchtigung der Ultra-Pro High-Fidelity Cloud-Sicherheitsinfrastruktur (T1562.012)
- **ID:** `T1562_012.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt gezielte Versuche, Cloud-native Sicherheitsdienste auszublenden.
Konzentriert sich auf die Erstellung von Unterdrückungsfiltern, das Löschen von Detektoren usw
Sabotage von Bedrohungsinformationen durch nicht automatisierte oder Root-Identitäten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Remote Service Session Hijacking (T1563)
- **ID:** `T1563.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Entführung von RDP-/Terminal-Sitzungen durch Überwachung der Ausführung von tscon.exe
Muster.Konzentriert sich auf anomale übergeordnete Prozesse und bestimmte Befehlszeilen
Schalter, mit denen Benutzersitzungen zum Terminal des Angreifers umgeleitet werden
ohne Authentifizierung der Anmeldedaten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Local Session Hijacking (T1563.001)
- **ID:** `T1563_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt erweitertes lokales Sitzungs-Hijacking, bei dem tscon.exe zum Herstellen einer Verbindung verwendet wird
eine bestehende Benutzersitzung.Filtert legitimes RDS/VDI-Management heraus
Analyse der Integrität des übergeordneten Prozesses und der Befehlszeilenentropie.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity RDP Session Hijacking (T1563.002)
- **ID:** `T1563_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes RDP-Sitzungs-Hijacking und Shadowing.Konzentriert sich auf
die spezifische Kombination aus Ausführung auf SYSTEM-Ebene und anomalem übergeordnetem Element
Prozesse (Shells, laterale Bewegungswerkzeuge) und „No-Consent“-Parameter.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Erkennung versteckter Artefakte (T1564)
- **ID:** `T1564.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Techniken zum Verstecken von Artefakten, einschließlich NTFS Alternative Data Streams (ADS),
Registrierungsbasiertes Ausblenden von Benutzerkonten und verdächtige Manipulation von Dateiattributen
initiiert von nicht vertrauenswürdigen Eltern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Manipulation versteckter Dateiattribute (T1564.001)
- **ID:** `T1564_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das gezielte Verstecken von Dateien und Verzeichnissen durch die Identifizierung der kombinierten Verwendung von
Systemattribute (+s) und versteckte Attribute (+h), die von nicht vertrauenswürdigen übergeordneten Prozessen initiiert werden
oder auf sensible, vom Benutzer beschreibbare Verzeichnisse abzielen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Erstellung versteckter Benutzerkonten (T1564.002)
- **ID:** `T1564_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BASH.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt durch Targeting das Verstecken von Benutzerkonten auf dem Windows-Anmeldebildschirm
den Registrierungsschlüssel „SpecialAccounts\UserList“.Filtert legitime Systeme heraus
Installer und konzentriert sich auf verdächtige übergeordnete Prozesse und Nicht-Systembenutzer.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Hidden Window Execution (T1564.003)
- **ID:** `T1564_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Prozessausführungen mit ausgeblendeten Fenstern durch Korrelation
abgekürzte Stealth-Flags mit nicht vertrauenswürdigen übergeordneten Prozessen und
Verschleierungstechniken.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity NTFS Alternative Data Stream (ADS) Missbrauch (T1564.004)
- **ID:** `T1564_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CONTROL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung oder Ausführung bösartiger NTFS Alternative Data Streams (ADS).
Korreliert Umleitungsoperatoren und LOLBins mit streamspezifischer Befehlszeile
Syntax, um Fehlalarme aus Laufwerksbuchstaben und MOTW zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Manipulation versteckter Dateisysteme (T1564.005)
- **ID:** `T1564_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtiges Mounten oder Erstellen von virtuellen Festplatten-Images (VHD, VHDX, ISO)
initiiert durch nicht vertrauenswürdige übergeordnete Prozesse oder auf nicht standardmäßige Pfade abzielend,
Wird häufig verwendet, um MOTW zu umgehen oder bösartige Payloads zu verbergen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Missbrauch der Ausführung virtueller Ultra-Pro-High-Fidelity-Instanzen (T1564.006)
- **ID:** `T1564_006.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Ausführung virtueller Instanzen (Docker, VirtualBox, VMware)
durch Identifizierung von Anti-Forensik-Flags (--rm), privilegierten Eskalationsversuchen,
und nicht vertrauenswürdige übergeordnete Prozesse wie Webserver oder Office-Apps.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity VBA Macro Security Evasion (T1564.007)
- **ID:** `T1564_007.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, die Office-Makrosicherheit zu umgehen oder VBA-Projekte auszublenden
durch Identifizierung verdächtiger Registrierungsänderungen und auf Prozessebene
Manipulation des Office-Objektmodells.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Erkennung von E-Mail-Versteckregeln (T1564.008)
- **ID:** `T1564_008.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt gezielte Regeln zum Verstecken von E-Mails, indem verdächtige Posteingangsregeln identifiziert werden
Modifikationen, die das Löschen oder Ausblenden von Sicherheitswarnungen automatisieren,
initiiert durch nicht vertrauenswürdige übergeordnete Prozesse oder Nicht-Administrator-Shells.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Ressourcenextraktion und -missbrauch (T1564.009)
- **ID:** `T1564_009.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Missbrauch von binären Ressourcenabschnitten und Hilfedatei-Interpretern
(hh.exe, winhlp32.exe), um versteckte Payloads zu extrahieren oder auszuführen.
Konzentriert sich auf Protokollschmuggel (its:, ms-its:) und verdächtige Dekompilierung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Prozessargument-Spoofing-Erkennung (T1564.010)
- **ID:** `T1564_010.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt mögliches Spoofing von Prozessargumenten durch Identifizierung der Ausführung
Nichtübereinstimmungen, bei denen sensible Interpreter (PowerShell, CMD) erzeugt werden
mit leeren oder allgemeinen Argumenten nicht vertrauenswürdiger Eltern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Missbrauch virtueller Ultra-Pro-High-Fidelity-Instanzen (T1564.011)
- **ID:** `T1564_011.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/), [WSL.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Verwendung von Windows Sandbox und WSL, um der EDR-Überwachung zu entgehen.
Konzentriert sich auf nicht vertrauenswürdige übergeordnete Prozesse, das Laden nicht standardmäßiger Konfigurationen,
und direkte Befehlsausführung innerhalb virtueller Instanzen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Datenmanipulation (T1565)
- **ID:** `T1565.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Datenmanipulation durch Überwachung der Stream-Bearbeitung,
Protokolllöschung über CLI und unbefugte Änderungen an kritischen Systemen
Dateien (Hosts, Ereignisprotokolle) von nicht standardmäßigen übergeordneten Prozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Manipulation gespeicherter Daten (T1565.001)
- **ID:** `T1565_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen gespeicherter Daten (Konfigurationen, Protokolle, Datenbanken)
durch Identifizierung verdächtiger Stream-Bearbeitungen (sed, powershell-replace)
Sie stammen von nicht standardmäßigen übergeordneten Prozessen oder zielen auf kritische Systempfade ab.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Manipulation übertragener Daten (T1565.002)
- **ID:** `T1565_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Netzwerkumleitung und Auflösungsmanipulation (DNS, Proxy, Hosts)
durch die Identifizierung von CLI-basierten Konfigurationsänderungen, die von verdächtigem Ursprung stammen
übergeordnete Prozesse oder das Angreifen kritischer Registrierungsschlüssel.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Laufzeitprozessmanipulation (T1565.003)
- **ID:** `T1565_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Manipulationen von Laufzeitprozessen durch Überwachung auf verdächtige Speicherzugriffe
Masken (z. B. PROCESS_ALL_ACCESS) und Remote-Thread-Injection zwischen unabhängigen
Prozesse, insbesondere das Herausfiltern bekanntermaßen guter Verwaltungs- und Sicherheitstools.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Phishing-Payload-Ausführung aus Kommunikations-Apps
- **ID:** `T1566.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von E-Mail-Clients, Browsern oder Chat-Apps erzeugt werden
wobei die Nutzlast aus einem vom Benutzer beschreibbaren Verzeichnis stammt.Dieses Muster ist
sehr charakteristisch für Spearphishing (T1566.001/.002).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Ausführung von Spearphishing-Anhängen
- **ID:** `T1566_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [HH.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [MSPUB.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [VISIO.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt äußerst verdächtige untergeordnete Prozesse, die von E-Mail-Clients oder Office-Anwendungen erzeugt werden.
Es zielt speziell auf Skriptinterpreter und Dual-Use-Binärdateien (LOLBins) ab
stammen aus vom Benutzer beschreibbaren Verzeichnissen, wodurch Fehlalarme deutlich reduziert werden
vor legitimen Systemaktualisierungen und Standard-GUI-Verhalten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Browser-basierte Nutzlastausführung
- **ID:** `T1566_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige untergeordnete Prozesse, die von Webbrowsern in der Befehlszeile erzeugt werden
verweist auf vom Benutzer beschreibbare oder temporäre Verzeichnisse.Dieses Muster ist hoch
Dies weist auf einen erfolgreichen Spearphishing-Link-Angriff hin, der zur sofortigen Ausführung führt.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Prozess-Spawn vom Business Communication Service
- **ID:** `T1566_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt äußerst verdächtige untergeordnete Prozesse, die von Unternehmenskommunikationstools erzeugt werden
(Teams, Slack, Discord, LinkedIn).Es richtet sich speziell an Skriptinterpreter
und Dual-Use-Binärdateien (LOLBins), die aus vom Benutzer beschreibbaren Verzeichnissen ausgeführt werden,
Es filtert effektiv legitime Anwendungsaktualisierungen und Browserstarts heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochpräzise Erkennung der Remote-Tool-Ausführung nach dem Vishing
- **ID:** `T1566_004.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die Ausführung nicht autorisierter Fernzugriffstools (AnyDesk, TeamViewer usw.)
insbesondere, wenn es aus vom Benutzer beschreibbaren Verzeichnissen (Downloads, Temp) ausgeführt wird.
Dieses Muster ist ein hochzuverlässiger Indikator für einen erfolgreichen Vishing-Angriff
Das Opfer wird angewiesen, „Support“-Software auszuführen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Web Service Exfiltration (T1567)
- **ID:** `T1567.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische Datenexfiltration in Cloud-Dienste durch Identifizierung
Headless-Transfer-Tools (rclone, megatools) mit benutzerdefinierten Konfigurationsdateien
von nicht vertrauenswürdigen Pfaden oder ausgelöst durch übergeordnete Prozesse, die keine Administratoren sind.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Code Repo Exfil (T1567.001)
- **ID:** `T1567_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische Datenexfiltration in öffentliche Code-Repositorys durch Identifizierung
Headless-Git-Operationen, Inline-PAT-Tokens und Remote-Repository-Pivots
initiiert von übergeordneten Prozessen, die nicht zur Entwicklung gehören, oder verdächtigen Verzeichnissen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Cloud Storage Exfil (T1567.002)
- **ID:** `T1567_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische Datenexfiltration in den Cloud-Speicher durch Identifizierung von CLI-Tools
(rclone, megatools) mithilfe eingebetteter Anmeldeinformationen oder benutzerdefinierter Konfigurationsdateien
ausgelöst durch übergeordnete Prozesse ohne Administratorrechte (z. B. Office-Apps, Beacon-Hosts).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelles High-Fidelity-Video-Hosting Exfil (T1567.003)
- **ID:** `T1567_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdeckte Datenexfiltration über Video-Hosting-Plattformen durch Identifizierung
Steganografische Einbettung (Metadatenmissbrauch, Stream-Anhang) und CLI-basiert
Uploads aus nicht-kreativen Abteilungsressourcen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Textspeicher Exfil (T1567.004)
- **ID:** `T1567_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt durch Überwachung die programmgesteuerte Datenexfiltration auf Textspeicherseiten
CLI-basierte POST-Anfragen, die API-Schlüssel oder Befehle zum Abrufen der Zwischenablage enthalten
aus nicht-administrativen oder verdächtigen übergeordneten Prozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle, dynamische Auflösung und DGA (T1568)
- **ID:** `T1568.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt dynamische Auflösung und DGA-Aktivität durch Identifizierung programmatischer Aktivitäten
DNS-Abfragen innerhalb von Schleifen, Low-Level-DNS-API-Aufrufe von Skript-Engines,
und anomale Domänenmuster von Nicht-Browser-Prozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Fast Flux & DNS Cache Evasion (T1568.001)
- **ID:** `T1568_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Nutzung der Fast Flux DNS-Infrastruktur durch Identifizierung des erzwungenen DNS-Cache
Flushing kombiniert mit programmatischer Namensauflösung und schleifenbasiert
Konnektivitätsprüfungen von Nicht-Systemprozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Domain Generation Algorithmus (DGA) (T1568.002)
- **ID:** `T1568_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt DGA-Aktivität durch Überwachung auf schnelle, programmgesteuerte DNS-Auflösungsversuche.
Domänenmuster mit hoher Entropie in Befehlszeilen und die Unterdrückung von DNS-Fehlern
aus nicht standardmäßigen Prozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-DNS-Berechnung und -Extraktion (T1568.003)
- **ID:** `T1568_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die C2-Adressberechnung durch Identifizierung programmgesteuerter DNS-TXT/SRV-Einträge
Abruf mit anschließender expliziter Datentypkonvertierung oder Manipulation auf Byte-Ebene
innerhalb von Skriptinterpretern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Erkennung der Ausführung von Systemdiensten
- **ID:** `T1569.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung oder Ausführung von Systemdiensten mit verdächtigen Merkmalen,
B. Binärdateien, die sich in weltweit beschreibbaren Verzeichnissen befinden, oder Dienste, die als verwendet werden
Wrapper für Shell-Befehle.Optimiert, um legitime Software-Installer herauszufiltern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Launch-Daemon-Persistenzerkennung
- **ID:** `T1569_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die Erstellung oder Änderung von Launch Daemons durch Überwachung
nicht vertrauenswürdige übergeordnete Prozesse und verdächtige Befehlszeilenzeichenfolgen.
Optimiert, um Apple- und gängige Installationsprogramme von Drittanbietern herauszufiltern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Systemdienstausführungserkennung (T1569.002)
- **ID:** `T1569_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Dienstausführungen oder -änderungen durch Überwachung von Anomalien
übergeordnete Prozesse, weltweit beschreibbare Binärpfade und Shell-Befehls-Wrapper.
Optimiert für niedrige Falsch-Positiv-Raten in Unternehmensumgebungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-lateraler Werkzeugtransfer (T1570)
- **ID:** `T1570.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte seitliche Werkzeugübertragungen durch Überwachung der Befehlszeilenaktivität
Ausrichtung auf administrative Freigaben (C$, ADMIN$).Konzentriert sich auf nicht standardmäßige Prozesse
Abstammungslinien (Office, Browser, nicht erhöhte Shells) und bewaffnete Tools wie
bitsadmin oder robocopy.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Nicht-Standard-Port C2 (T1571)
- **ID:** `T1571.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Kritisch hoch (SIEM-Killerkategorie!)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt C2-Kommunikation über nicht standardmäßige Ports durch Korrelation mit hohem Risiko
native Binärdateien (LoLBins) mit ausgehenden öffentlichen Netzwerkverbindungen
an Ports außerhalb der Standardbereiche von Web-/Mail-/Verzeichnisdiensten.

#### 🚨 Reaktions-Playbook
1. **IP-Reputation: Überprüfen Sie die Remote-IP-Adresse in Reputationsdatenbanken.**
2. **Verkehrsanalyse: Untersuchen Sie die Menge der gesendeten Daten.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Protokoll-Tunneling-Erkennung (T1571)
- **ID:** `T1572.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Protokoll-Tunneling durch Identifizierung nicht standardmäßiger Kapselungslogik.
Low-Level-Socket-Proxying (SOCKS5) und spezifische CLI-Signaturen von
gegnerische Tunneling-Tools und filtert gleichzeitig legitimen administrativen SSH/VPN-Verkehr.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-verschlüsselter C2-Kanal (T1573)
- **ID:** `T1573.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung benutzerdefinierter verschlüsselter C2-Kanäle durch Überwachung
Instanziierung kryptografischer Klassen auf niedriger Ebene (AES, Rijndael, CryptoStream)
in Verbindung mit der manuellen Netzwerk-Socket-Erstellung durch Skriptinterpreter.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Symmetric Encryption C2-Kanal (T1573.001)
- **ID:** `T1573_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die in C2-Kanälen verwendete benutzerdefinierte symmetrische Verschlüsselung (AES/Rijndael) durch Identifizierung
die programmatische Einrichtung von CipherMode, PaddingMode und CryptoStreams darin
Skript-Engines, die speziell auf die manuelle IV/Tastenzuweisung und Stream-Piping abzielen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Asymmetric Encryption C2 (T1573.002)
- **ID:** `T1573_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [REGSVR32.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt benutzerdefinierte asymmetrische Verschlüsselung (RSA/ECC) durch Identifizierung programmatischer
Vertrauenskettenüberschreibungen (ServerCertificateValidationCallback) und roher öffentlicher Schlüssel
Importe (FromXmlString/ImportSubjectPublicKeyInfo) aus nicht standardmäßigen Prozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro DLL-Hijacking und Sideloading-Erkennung (T1574)
- **ID:** `T1574.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielles DLL-Hijacking oder Sideloading durch Überwachung vertrauenswürdiger Systeme
Binärdateien laden DLLs aus nicht standardmäßigen, vom Benutzer beschreibbaren Verzeichnissen, während
Herausfiltern legitimer signierter Module und bekannter Anwendungsverhalten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro DLL-Suchreihenfolge-Hijacking-Erkennung (T1574.001)
- **ID:** `T1574_001.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt vertrauenswürdige Windows-Systembinärdateien, die DLLs von nicht standardmäßigen,
potenziell vom Benutzer beschreibbare Verzeichnisse.Es filtert gültig signierte Dateien heraus
Module von Drittanbietern, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro DLL Side-Loading Integrity Gap Detection (T1574.002)
- **ID:** `T1574_002.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielles DLL-Sideloading durch Identifizierung von Fällen, in denen eine signierte,
Die vertrauenswürdige ausführbare Datei lädt eine nicht signierte oder verdächtig lokalisierte DLL von
Vom Benutzer beschreibbare Verzeichnisse.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro-Shell-Konfiguration und Pfadabfang (T1574.003)
- **ID:** `T1574_003.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen an PATH-Umgebungsvariablen oder Shell-Autorun
Registrierungsschlüssel.Konzentriert sich auf „Path Prepending“ (Platzierung bösartiger Pfade am
Anfang) und nicht standardmäßige Shell-Startbefehle.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Entführung von Ultra-Pro-Bibliothekssuchaufträgen und Integritätslücke (T1574.004)
- **ID:** `T1574_004.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielle Bibliotheksdiebstahl durch Überwachung vertrauenswürdiger Systembinärdateien
Laden nicht signierter oder verdächtig lokalisierter DLLs aus vom Benutzer beschreibbaren Verzeichnissen,
Insbesondere wird nach Vertrauenskonflikten zwischen der EXE-Datei und der DLL gesucht.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Schwäche bei Dateiberechtigungen des Ultra-Pro-Installationsprogramms (T1574.005)
- **ID:** `T1574_005.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausführung von Binärdateien mit hohen Berechtigungen von Speicherorten, die vom Benutzer beschreibbar sind.
Dies zielt auf Szenarien ab, in denen ein Angreifer ein legitimes Installationsprogramm ersetzt
mit einem böswilligen aufgrund unsicherer Verzeichnisberechtigungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Dynamic Linker-Hijacking gegen privilegierte Binärdateien
- **ID:** `T1574_006.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt Dynamic Linker Hijacking, indem es die Ausführung privilegierter oder SetUID-Linux-Binärdateien mit manipulierten dynamischen Linker-Umgebungsvariablen identifiziert, die auf vom Benutzer beschreibbare gemeinsam genutzte Bibliotheken verweisen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## PATH-Hijacking führt zur privilegierten Binärausführung
- **ID:** `T1574_007.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt das Hijacking von PATH-Umgebungsvariablen, wenn eine privilegierte Linux-Binärdatei mit einem vom Benutzer beschreibbaren Verzeichnis am Anfang von PATH ausgeführt wird und ein nicht absoluter Befehl aufgelöst wird, was auf eine realisierbare Path-Interception-Angriffskette hinweist.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Entführung der .NET-Assembly-Suchreihenfolge über ein vom Benutzer beschreibbares Verzeichnis
- **ID:** `T1574_008.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielles Hijacking der .NET-Assembly-Suchreihenfolge, bei dem ein legitimer .NET-Laufzeithost eine verwaltete Assembly aus einem vom Benutzer beschreibbaren Verzeichnis außerhalb des GAC, der Microsoft.NET-Framework-Pfade oder des Anwendungsinstallationsverzeichnisses lädt.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## .NET AppDomainManager-Hijacking über Nicht-GAC-Assembly
- **ID:** `T1574_009.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt .NET AppDomainManager-Hijacking durch die Identifizierung von .NET-Laufzeithosts, die bei der Prozessinitialisierung eine verwaltete Assembly aus einem vom Benutzer beschreibbaren Verzeichnis außerhalb der GAC- und Microsoft .NET Framework-Pfade laden.Dieses Verhalten weist stark auf einen böswilligen AppDomainManager-Missbrauch hin.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ausführbare Datei des privilegierten Dienstes vom vom Benutzer beschreibbaren Speicherort überschrieben
- **ID:** `T1574_010.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die Ausnutzung schwacher Dienstdateiberechtigungen, wenn eine registrierte ausführbare Windows-Dienstdatei, die mit hohen Berechtigungen ausgeführt wird, von einem Nicht-Systemprozess aus einem vom Benutzer beschreibbaren Verzeichnis überschrieben oder geändert wird.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Privilegierter Dienst ImagePath oder ServiceDll über die Registrierung gekapert
- **ID:** `T1574_011.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausnutzung schwacher Windows-Dienstregistrierungsberechtigungen, wenn ein systemfremder Prozess kritische Dienstregistrierungswerte so ändert, dass sie auf eine ausführbare Datei oder DLL verweisen, die sich in einem vom Benutzer beschreibbaren Verzeichnis befindet, und ermöglicht so eine Rechteausweitung beim Start oder Neustart des Dienstes.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## COR_PROFILER-Hijacking der Exploit-Klasse über eine vom Benutzer beschreibbare Profiler-DLL
- **ID:** `T1574_012.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [INSTALLUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [REGASM.EXE](https://lolbas-project.github.io/lolbas/), [REGSVCS.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/), [VSJITDEBUGGER.EXE](https://lolbas-project.github.io/lolbas/), [VSTEST.CONSOLE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Ausnutzung von COR_PROFILER-Hijacking, bei dem ein .NET-Laufzeithost mit aktivierter Profilerstellung und einer benutzerdefinierten Profiler-DLL ausgeführt wird, die aus einem vom Benutzer beschreibbaren Verzeichnis angegeben wird, ausgenommen legitime Microsoft-, Visual Studio- und APM-Profilerstellungsanwendungsfälle.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Exploit-Grade-KernelCallbackTable-Manipulation über Remote-Speicher-Schreiben
- **ID:** `T1574_013.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Remote-Speicherschreibvorgänge in GUI-Prozesse, die Voraussetzung sind
für KernelCallbackTable-Hijacking.Diese Technik wird häufig für Prozesse verwendet
Injektion, die der standardmäßigen Hook-basierten Überwachung entgeht.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Manipulation der Ultra-Pro-High-Fidelity-Cloud-Infrastruktur (T1578)
- **ID:** `T1578.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt risikoreiche Änderungen an der Cloud-Infrastruktur, die die Sicherheitslage schwächen
Oder bereiten Sie sich auf die Datenexfiltration vor, gefiltert nach Identitätsverhalten und Quellenvertrauen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Erstellung verdächtiger Cloud-Instanzen (T1578.001)
- **ID:** `T1578_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die Erstellung ressourcenintensiver oder teurer Cloud-Instanzen aus nicht vertrauenswürdigen Quellen
Identitäten oder außerhalb genehmigter Regionen.Optimiert für die Erkennung von Cryptojacking
mit minimalen Fehlalarmen aus CI/CD-Pipelines.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Cloud Snapshot Exfiltration (T1578.002)
- **ID:** `T1578_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die unbefugte Weitergabe oder öffentliche Offenlegung von Cloud-Computing-Snapshots.
Konzentriert sich auf Berechtigungsänderungen und kontoübergreifenden Zugriff und nicht auf einfache Erstellung.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Cloud-Instanzzerstörung (T1578.003)
- **ID:** `T1578_003.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt unbefugtes oder massenhaftes Löschen von Cloud-Instanzen.Filtert heraus
automatisierte Skalierungsereignisse und konzentriert sich auf manuelle, nicht-MFA- oder skriptbasierte
Zerstörungsversuche, die auf Sabotage oder Umgehung der Verteidigung schließen lassen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Cloud Image Manipulation (T1578.004)
- **ID:** `T1578_004.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt nicht autorisierte Änderungen an Cloud-Maschinen-Images (AMI, VHD).
Konzentriert sich auf Berechtigungsänderungen, die Bilder für externe Konten oder verfügbar machen
das öffentliche Internet und filtert bekannte CI/CD-Build-Pipelines heraus.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Cloud-Netzwerk-Sicherheitsregression (T1578.005)
- **ID:** `T1578_005.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt risikoreiche Änderungen an Netzwerk-ACLs oder Sicherheitsgruppen, die dies zulassen
Breiter Eingangsverkehr (0.0.0.0/0) auf sensiblen Verwaltungsports (RDP, SSH, DB).
Filtert automatisiertes Infrastructure-as-Code (IaC)-Rauschen heraus.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessionelle High-Fidelity-Cloud-Infrastrukturerkennung (T1580)
- **ID:** `T1580.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung von Cloud-Ressourcen (VMs, VPCs, S3) mit Schwerpunkt auf
anormale Ausführungsumgebungen und Datenextraktionsmuster.
Ausgenommen sind legitime Infrastructure-as-Code (IaC)- und CI/CD-Tools.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Bereitstellung einer High-Fidelity-Offensiv-Infrastruktur – T1583
- **ID:** `T1583.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatisierte Erfassung von Infrastruktur (VPS, Domänen, serverlos) durch Überwachung auf CLI-basierte Bereitstellungstools und API-Aufrufe zur Domänenregistrierung.Filter konzentrieren sich auf die Isolierung autorisierter DevOps-Pipelines und Entwicklerumgebungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Bereitstellung einer High-Fidelity-VPS-Infrastruktur – T1583.001
- **ID:** `T1583_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatisierte Erfassung der VPS-Infrastruktur (DigitalOcean, AWS, Azure, GCP).Konzentriert sich auf die Bereitstellungsphase (VM-Erstellung) und isoliert gleichzeitig autorisierte DevOps-Pipelines und interaktive Entwickler-Workflows.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Automatisierte High-Fidelity-Domainregistrierung und -Akquise – T1583.002
- **ID:** `T1583_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatisierte Domänenregistrierung über Registrar-APIs und spezielle Bereitstellungstools.Konzentriert sich auf die programmatische Erfassung über Curl/Python und filtert gleichzeitig autorisiertes IT-Infrastrukturmanagement (Certbot, Terraform) heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Bereitstellung von High-Fidelity-Cloud-Netzwerken (VPC) – T1583.003
- **ID:** `T1583_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erfassung und Konfiguration von Cloud-Netzwerken (VPC).Konzentriert sich auf die Identifizierung der Entstehung von Internet-Ausgangspunkten und netzwerkübergreifenden Brücken von nicht autorisierten Endpunkten und isoliert automatisierte CI/CD-Pipelines vor manuellem oder skriptgesteuertem lokalem Missbrauch.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Serverlose Infrastrukturbereitstellung mit hoher Wiedergabetreue – T1583.004
- **ID:** `T1583_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatisierte Erfassung und Bereitstellung serverloser Infrastruktur (AWS Lambda, Azure Functions, GCP Functions).Konzentriert sich auf die CLI-basierte Erstellung und wichtige Konfigurationsänderungen und isoliert gleichzeitig autorisierte CI/CD-Pipelines und interaktive Entwickler-IDE-Kontexte.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erwerb einer High-Fidelity-Botnet-Infrastruktur – T1583.005
- **ID:** `T1583_005.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erfassung und Vorbereitung der Botnet-Infrastruktur.Der Schwerpunkt liegt auf der Identifizierung von Multi-Architektur-Agent-Downloads, automatisierten Verbreitungsversuchen (Brute-Force) und der Nutzung von Botnet-C2-Clients.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erwerb und Bereitstellung von High-Fidelity-Webdiensten – T1583.006
- **ID:** `T1583_006.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Erwerb und die Einrichtung von Webdiensten (SaaS, Speicher, Messaging) für anstößige Infrastruktur.Konzentriert sich auf die befehlszeilenbasierte Speicherbereitstellung (Rclone, AzCopy) und die Messaging-API-Initialisierung (Slack/Discord/Telegram-Bots) von Endpunkten, die keine Administratoren oder Entwickler sind.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Serverlose Infrastrukturbereitstellung mit hoher Wiedergabetreue – T1583.007
- **ID:** `T1583_007.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatisierte Erfassung und Bereitstellung serverloser Infrastruktur (AWS Lambda, Azure Functions, GCP Functions).Konzentriert sich auf die CLI-basierte Erstellung und wichtige Konfigurationsänderungen und isoliert gleichzeitig autorisierte CI/CD-Pipelines und interaktive Entwickler-IDE-Kontexte.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Cloud-Kontoerwerb und Bootstrap – T1583.008
- **ID:** `T1583_008.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Erwerb und die Erstkonfiguration von Cloud-Konten.Zielt auf Bootstrapping auf Kontoebene (Einrichtung von Anmeldeinformationen, IAM-Benutzererstellung) und die automatisierte Identitätserfassung aus nicht standardmäßigen Prozessen ab und filtert gleichzeitig autorisierte DevOps-Pipelines heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Kompromittierte High-Fidelity-Infrastruktur und Ressourcenmissbrauch – T1584
- **ID:** `T1584.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Anzeichen einer kompromittierten Infrastruktur und konzentriert sich dabei insbesondere auf die Subversion von Webserverprozessen (Web Shells), nicht autorisierte Reverse-Proxys und Tunneling-Tools, die aus nicht standardmäßigen Verwaltungskontexten ausgeführt werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hijacking der High-Fidelity-Domain-Infrastruktur – T1584.001
- **ID:** `T1584_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes Domänen- oder Subdomänen-Hijacking durch Überwachung auf kritische DNS-Eintragstypen (NS, SOA) und Masseneintragserstellung über Cloud-Provider-CLIs, während gleichzeitig nach autorisierter DevOps-Automatisierung gefiltert wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Subversion der High-Fidelity-DNS-Serverkonfiguration – T1584.002
- **ID:** `T1584_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [DNSCMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Manipulationen der DNS-Infrastruktur durch Überwachung auf kritische Konfigurationsänderungen (Zonen-Resets, Master-Updates) und verdächtige untergeordnete Prozesse, die direkt von DNS-Diensten erzeugt werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Cloud-Identitätssubversion und -Persistenz – T1584.003
- **ID:** `T1584_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Cloud-Kontomanipulationen durch Überwachung auf risikoreiche Identitätsänderungen (MFA-Entfernung, neue Zugriffsschlüssel), die außerhalb autorisierter CI/CD-Pipelines oder bekannter administrativer Jump-Hosts ausgeführt werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Serverlose High-Fidelity-Funktionssubversion – T1584.004
- **ID:** `T1584_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen an serverlosen Funktionen (Lambda, Azure Functions, GCP), indem der Schwerpunkt auf risikoreiche Parameter wie Layer-Injection und Umgebungsvariablenmanipulation gelegt wird, während gleichzeitig streng nach autorisierten CI/CD-Pipeline-Dienstkonten gefiltert wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Botnet-Agent-Persistenz und -Kontrolle – T1584.005
- **ID:** `T1584_005.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Aktivität von Botnet-Agenten durch die Identifizierung verdächtiger Prozesslinien (z. B. LOLBins, die aus WMI entstehen), P2P-Bootstrap-Argumenten und bekannten DDoS-Tool-Mustern und filtert gleichzeitig autorisierte IT-Management- und P2P-Software.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Webdienst und Cloud-Speicher-Subversion – T1584.006
- **ID:** `T1584_006.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Manipulationen an Webdiensten und Cloud-Speichern durch Überwachung auf ACL-Änderungen (Öffentlichkeit von Buckets), gehostete verdächtige Dateitypen (Skripts/Exes) und die Verwendung von Datenübertragungstools von Drittanbietern (rclone) außerhalb autorisierter Kontexte.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-VPS-Steuerung und Tunneling – T1584.007
- **ID:** `T1584_007.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte VPS-Manipulationen durch die Identifizierung kritischer Lebenszyklusänderungen (SSH-Schlüsselinjektion, Firewall-Öffnung) und die Ausführung von Reverse-Tunneling-Tools aus nicht autorisierten Verwaltungskontexten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Benutzerkontoerstellung über CLI/Scripting
- **ID:** `T1585.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung neuer Benutzerkonten (T1585), wenn sie von initiiert wird
verdächtige Prozesse wie CMD, PowerShell oder net.exe, anstatt
Standard-Verwaltungskonsolen (ADUC, Windows Admin Center).

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Mögliche automatisierte Einrichtung eines Social-Media-Kontos
- **ID:** `T1585_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Kritisch hoch (SIEM-Killerkategorie!)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Muster bei der Registrierung von Social-Media-Konten durch Überwachung
Zugriff auf mehrere Anmeldeendpunkte von einem einzelnen Host oder einer Identifizierung aus
Nicht-Browser-Prozesse, die Anfragen an diese Domänen stellen.

#### 🚨 Reaktions-Playbook
1. **IP-Reputation: Überprüfen Sie die Remote-IP-Adresse in Reputationsdatenbanken.**
2. **Verkehrsanalyse: Untersuchen Sie die Menge der gesendeten Daten.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Heimliche Einrichtung und Manipulation von E-Mail-Konten
- **ID:** `T1585_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die Erstellung von E-Mail-Konten mit anschließender sofortiger Vertraulichkeit
Berechtigungsänderungen oder Weiterleitungsregeln.Konzentriert sich auf die CLI-basierte Ausführung
um Störungen durch standardmäßige HR-gesteuerte GUI-Prozesse zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomale Erstellung eines Cloud-Benutzerkontos
- **ID:** `T1585_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt die Erstellung von Cloud-Konten über Befehlszeilentools oder Dienstprinzipale.
ausgenommen autorisierte Synchronisierungskonten und automatisierte HR-Bereitstellungssysteme.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Kompromittierung von High-Fidelity-Konten und Identitätsmanipulation – T1586
- **ID:** `T1586.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Aktionen, die auf eine Kontokompromittierung und -übernahme (ATO) hinweisen, wie z. B. unbefugte MFA-Änderungen, verdächtige Anmeldeprofilaktualisierungen und automatisierte Anmeldeinformationstests durch nicht standardmäßige Verwaltungsprozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Automatisierte Social-Media-Manipulation mit hoher Wiedergabetreue – T1586.001
- **ID:** `T1586_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt automatisierte Interaktionen mit Social-Media-Plattformen über Headless-Browser-Frameworks (Selenium, Puppeteer, Playwright).Angreifer nutzen diese, um Account Takeover (ATO) zu skalieren und Sicherheitskontrollen zu umgehen, indem sie gestohlene Cookies einschleusen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Manipulation von High-Fidelity-E-Mail-Weiterleitungsregeln – T1586.002
- **ID:** `T1586_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung oder Änderung von E-Mail-Weiterleitungs-/Umleitungsregeln über Befehlszeilentools (PowerShell, Microsoft Graph CLI).Dies ist ein hochzuverlässiger Indikator für Account Takeover (ATO), bei dem ein Angreifer versucht, vertrauliche E-Mails (Rechnungen, Passwort-Resets) ohne Benutzerinteraktion zu exfiltrieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Übernahme und Persistenz von High-Fidelity-Cloud-Konten – T1586.003
- **ID:** `T1586_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Manipulationen von Cloud-Konten mit Schwerpunkt auf Identitätsübernahme und Persistenz.Zielt auf die Erstellung neuer Cloud-Anmeldeinformationen, MFA-Entfernung und Aktualisierungen von Anmeldeprofilen aus nicht autorisierten Prozessen ab und filtert insbesondere bekannte Verwaltungs- und Entwickler-Workflows heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Entwicklung und Zusammenstellung von High-Fidelity-Offensivfähigkeiten – T1587
- **ID:** `T1587.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [JSC.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Entwicklung und Kompilierung anstößiger Tools durch Überwachung auf bestimmte C2-Framework-Build-Argumente, unbefugte Verwendung von Code-Packern und Zertifikatsmanipulation außerhalb verifizierter CI/CD-Pipelines.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Malware-Entwicklungs- und Umgehungsmuster – T1587.001
- **ID:** `T1587_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Entwicklung benutzerdefinierter Malware durch die Identifizierung verdächtiger Compilerausführungen in Kombination mit umgehungsbezogenen API-Zeichenfolgen, Anti-Analysetechniken und nicht autorisierten Build-Speicherorten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Entwicklung von High-Fidelity-Funktionen für nicht autorisierte Code-Signierung – T1587.002
- **ID:** `T1587_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Erstellung von Codesignaturzertifikaten und die manuelle Signatur von Binärdateien durch Überwachung auf bestimmte OIDs (1.3.6.1.5.5.7.3.3) und Signierungstools, die außerhalb verifizierter CI/CD-Pipelines oder Windows SDK-Pfade verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Unbefugte Entwicklung digitaler High-Fidelity-Zertifikate – T1587.003
- **ID:** `T1587_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die nicht autorisierte Generierung digitaler Zertifikate und privater Schlüssel durch Überwachung auf risikoreiche Befehlszeilenargumente (Selbstsignierung, Schlüsselexfiltration), die in nicht standardmäßigen Verzeichnissen oder von nicht autorisierten Benutzern auftreten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Exploit-Entwicklung und Kompilierungserkennung – T1587.004
- **ID:** `T1587_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CSC.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [VBC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Indikatoren für die Exploit-Entwicklung durch Überwachung der Kompilierung von Quellcode, der Speicherinjektionsprimitive und Shellcode-bezogene Argumente enthält, insbesondere wenn er aus nicht standardmäßigen oder temporären Verzeichnissen ausgeführt wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomale Beschaffung von Angriffsfähigkeiten
- **ID:** `T1588.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/), [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CSC.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Erwerb anstößiger Tools durch Überwachung verdächtiger Kombinationen
von herunterladbaren Prozessen und bekannten Hacktool-Signaturen oder Dateierweiterungen,
Herausfiltern legitimer IT-Software-Bereitstellungstools.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomale Beschaffung von Malware-Fähigkeiten
- **ID:** `T1588_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Erwerb von Malware durch Überwachung verdächtiger Downloader (LotL)
Interaktion mit komprimierten Formaten/Containerformaten oder bekannten Malware-Namensmustern
in nicht standardmäßigen Verzeichnissen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomale Offensiv-Tool-Erfassung über CLI
- **ID:** `T1588_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Erwerb anstößiger Tools (Hacktools) durch Überwachung der Befehlszeile
Downloads, die auf nicht standardmäßige Verzeichnisse abzielen.Filtert legitime IT heraus
Verwaltung über Browser und autorisierte Management-Agenten.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomaler Export oder Erwerb von Code Signing-Zertifikaten
- **ID:** `T1588_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Zertifikatsvorgänge (Export privater Schlüssel oder erzwungene Speichererweiterungen)
initiiert durch ungewöhnliche übergeordnete Prozesse oder durch die Verwendung von Klartext-Passwörtern in der Befehlszeile.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Strategische Manipulation des Speichers vertrauenswürdiger Stammzertifikate
- **ID:** `T1588_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Versuche, die vertrauenswürdigen Stammzertifizierungsstellen zu ändern
speichern.Angreifer tun dies, um MitM-Angriffe zu erleichtern oder Sicherheitswarnungen zu umgehen.
Filtert legitime Installationsprogramme auf Systemebene und bekannte Sicherheitsagenten heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomale Beschaffung von Exploit- oder PoC-Code
- **ID:** `T1588_005.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [BITSADMIN.EXE](https://lolbas-project.github.io/lolbas/), [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Erwerb von Exploits oder Proof-of-Concept-Code (PoC) durch Überwachung
verdächtige Downloadmuster, CLI-basierte Übertragungen und bekannte Exploit-Namen
Konventionen einhalten und gleichzeitig autorisierte Sicherheitsscanner und Entwickleraktivitäten herausfiltern.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Gezielte Ernte von Artefakten der Schwachstellenforschung
- **ID:** `T1588_006.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erfassung von Schwachstellenrecherchen, Prüfberichten usw
Zero-Day-PoC-Dokumentation.Konzentriert sich auf CLI-basiertes Harvesting in nicht-technischen Bereichen
Benutzerkontexte und filtern gleichzeitig autorisierte Sicherheitsrecherchen heraus.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Identitätsaufzählung über Authentifizierungsendpunkte
- **ID:** `T1589.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochsichere Identitätsaufklärungsaktivitäten, bei denen ein externer Akteur gültige Benutzeridentitäten über Authentifizierung oder kontobezogene Endpunkte auflistet.Die Erkennung basiert auf Aufzählungsverhalten, Automatisierungsindikatoren und Authentifizierungsantwortmustern, ausgenommen Browser, SSO-Flows und Überwachungstools.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Aufzählung der Anmeldeinformationen über die Authentifizierungs-API (hohes Vertrauen)
- **ID:** `T1589_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt Aktivitäten zur Aufzählung von Anmeldeinformationen mit hoher Zuverlässigkeit anhand von Authentifizierungs-APIs.Die Regel konzentriert sich auf automatisiertes, nicht interaktives Prüfverhalten, bei dem versucht wird, die Existenz oder Richtigkeit von Anmeldeinformationen zu überprüfen.Browserbasierte Anmeldungen, SSO-Flows, Überwachungssysteme und legitime Benutzerauthentifizierung sind ausgeschlossen, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochzuverlässige OSINT-Identitätsaufzählung über öffentliche APIs
- **ID:** `T1589_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochzuverlässige Open-Source-Identitätsaufzählungsversuche über öffentlich zugängliche APIs oder Verzeichnisendpunkte.Diese Regel konzentriert sich auf skriptgesteuertes, automatisiertes Aufklärungsverhalten, das darauf abzielt, Benutzer- oder Mitarbeiteridentitätsdaten zu sammeln, während normales Surfen, Suchmaschinen und legitime Crawler ausgeschlossen werden, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Gezielte OSINT-Enumeration offener Websites und Domains
- **ID:** `T1589_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochzuverlässige Aufklärungsaktivitäten, die auf offene Websites und Domänen abzielen, um Informationen zur Opferidentität zu sammeln.Die Regel konzentriert sich auf das skriptgesteuerte Aufzählungsverhalten gegenüber Endpunkten im Such- oder Verzeichnisstil und schließt Browser, Crawler und legitimen Überwachungsverkehr aus, um sehr niedrige Falsch-Positiv-Raten sicherzustellen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Netzwerkaufklärung mit hoher Portvielfalt
- **ID:** `T1590.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Kritisch hoch (SIEM-Killerkategorie!)
- **Beschreibung:** Erkennt Netzwerkaufklärungsaktivitäten.Optimiert für SIEM-übergreifende Kompatibilität durch Verwendung von Standardfeldnamen und Vermeidung komplexer CIDR-Logik in der Kernregel.

#### 🚨 Reaktions-Playbook
1. **IP-Reputation: Überprüfen Sie die Remote-IP-Adresse in Reputationsdatenbanken.**
2. **Verkehrsanalyse: Untersuchen Sie die Menge der gesendeten Daten.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Professionelle Aufklärung der IP-Infrastruktur – T1590.001
- **ID:** `T1590_001.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟡 (medium)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [NETSH.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt professionelle IP-Erkennungstechniken, indem es sich auf auskundungsspezifische Befehlsargumente und externe IP-Suchdienste konzentriert und gleichzeitig Standard-Windows-Netzwerkgeräusche herausfiltert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**


---
## Erweiterte Aufklärung der DNS-Infrastruktur – T1590.002
- **ID:** `T1590_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [DNSCMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt systematische DNS-Aufklärung.Es reduziert Fehlalarme, indem es legitime Einzelhost-Suchen filtert und sich auf infrastrukturweite Aufzählungsversuche wie Zonenübertragungen oder spezifisches Datensatz-Harvesting konzentriert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte Aufklärung von Netzwerkvertrauensabhängigkeiten – T1590.003
- **ID:** `T1590_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung von Vertrauensbeziehungen im Netzwerk und gemeinsam genutzten Ressourcen.Es minimiert das Rauschen, indem es standardmäßige GPO-gesteuerte Laufwerkszuordnungen filtert und sich auf Enumerationsbefehle mit hoher Absicht wie nltest-Domänenvertrauensstellungen und Remote-Sitzungslisten konzentriert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte Informationsaufklärung für Zertifikate – T1590.004
- **ID:** `T1590_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt professionelle Aufklärung digitaler Zertifikate.Der Schwerpunkt liegt auf interaktiven Befehlszeilentools, mit denen Metadaten aus lokalen Speichern oder Remoteservern extrahiert und gleichzeitig die automatische Signaturüberprüfung herausgefiltert wird.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte Aufklärung der Cloud-Infrastruktur – T1590.005
- **ID:** `T1590_005.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt manuelle oder verdächtige Cloud-Infrastrukturaufzählung.Es filtert legitime CI/CD-Pipelines und automatisierte Dienstkonten heraus, um sich auf die interaktive Erkennung zu konzentrieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte Aufklärung über Opfer-Webseiteninformationen – T1590.006
- **ID:** `T1590_006.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt automatisierte Webaufklärung und Versuche zur Erkennung sensibler Dateien.Es minimiert Fehlalarme, indem es Entwicklungsumgebungen filtert und sich auf Aufklärungsmuster mit hoher Absicht in allen CLI-Tools konzentriert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte Aufzählung der organisatorischen Infrastruktur – T1591
- **ID:** `T1591.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [LDIFDE.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erfassung organisatorischer Metadaten (Organisationseinheiten, Gruppen, Benutzer).Es minimiert Fehlalarme, indem es bekannte Verwaltungskonsolen und Dienstkontosynchronisierungen filtert und sich auf nicht standardmäßige Ausführungskontexte konzentriert.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte Aufzählung der physischen Standortinfrastruktur – T1591.001
- **ID:** `T1591_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [VISIO.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Entdeckung physischer Infrastrukturdaten (Grundrisse, Ausweissysteme).Es filtert die übliche Büronutzung (Intranet, Visio) heraus und konzentriert sich auf CLI-basierte Massensuchvorgänge, die für die Aufklärung vor physischem Eindringen oder Social Engineering charakteristisch sind.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte Erkennung von Geschäftsbeziehungsinformationen – T1591.002
- **ID:** `T1591_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische und automatisierte Entdeckung von Geschäftsbeziehungen.Es filtert allgemeine Produktivitätsstörungen im Büro heraus und konzentriert sich auf Massensuchvorgänge, die aus nicht standardmäßigen übergeordneten Prozessen stammen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Advanced Knowledge Management Discovery – T1591.003
- **ID:** `T1591_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische und automatisierte Erkennung interner Wissensmanagementsysteme.Es zielt auf Massendatenextraktionsmuster und Befehlszeilenaufklärung ab und filtert gleichzeitig die Standard-Webbrowser-Nutzung und IT-Automatisierung heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Ermittlung von Personalinformationen – T1591.004
- **ID:** `T1591_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MMC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Massenextraktionen von Mitarbeiterdaten aus Active Directory.Konzentriert sich auf nicht standardmäßige LDAP-Abfragen und umfassende PowerShell-Filter, die vom routinemäßigen Verwaltungsverhalten abweichen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Host-Informationsaufklärungsaktivität
- **ID:** `T1592.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt hochzuverlässige Host-Informationsaufklärungsaktivitäten durch die Identifizierung mehrerer Systemerkennungsbefehle, die in einem kurzen Zeitrahmen aus einem Benutzerkontext ausgeführt werden.Optimiert, um Fehlalarme zu minimieren, indem SYSTEM-Aktivitäten, Unternehmenstools und einzelne harmlose Befehlsausführungen ausgeschlossen werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochzuverlässige Hardware-Enumeration über Verwaltungsschnittstellen
- **ID:** `T1592_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochzuverlässige Aufklärungsaktivitäten, bei denen eine externe Quelle versucht, Hardwaremerkmale wie CPU, Architektur, Speicher oder Gerätemodell über Management- oder eingebettete Systemschnittstellen aufzuzählen.Die Regel ist optimiert, um Fehlalarme zu minimieren, indem der Schwerpunkt auf automatisiertem Prüfverhalten liegt.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte Software-Enumerationsaufklärung über Web-Endpunkte
- **ID:** `T1592_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt fortgeschrittene Aufklärungsaktivitäten, bei denen ein externer Akteur innerhalb eines kurzen Zeitfensters systematisch installierte Software, Anwendungsnamen oder Versionsinformationen über mehrere über das Internet zugängliche Endpunkte auflistet.Optimiert, um Fehlalarme zu minimieren, indem automatisierungsähnliches Verhalten und wiederholte Prüfmuster erforderlich sind.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochzuverlässige Firmware-Enumeration für Netzwerkgeräte
- **ID:** `T1592_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochzuverlässige Aufklärungsaktivitäten, die auf Firmware- und Versionsinformationen von Netzwerk- oder eingebetteten Geräten abzielen.Die Regel konzentriert sich auf den automatisierten, browserfreien Zugriff auf gerätespezifische Verwaltungsendpunkte und ist darauf optimiert, Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochzuverlässiges Client-Konfigurations-Fingerprinting (Aufklärung)
- **ID:** `T1592_004.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟡 (medium)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochzuverlässige Aufklärungsaktivitäten, bei denen eine externe Quelle wiederholte Nicht-Browser-HTTP-Anfragen mithilfe von Sondierungsmethoden und Header-fokussierten Techniken ausführt, um Client- oder Infrastrukturkonfigurationen aufzuzählen.Optimiert, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**


---
## Automatisierte Webaufklärung mit hoher Wiedergabetreue – T1593
- **ID:** `T1593.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt automatisiertes Web-Scraping und OSINT-Erfassungsmuster, die auf soziale Medien und öffentliche Websites abzielen.Konzentriert sich auf Headless-Browser-Automatisierung und spezielle CLI-Tools und filtert gleichzeitig legitime HR- und Marketingaktivitäten heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity Social Media Entity Harvesting – T1593.001
- **ID:** `T1593_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatisierte Auskundung von Social-Media-Profilen.Es zielt auf die Headless-Browser-Automatisierung (Selenium/Puppeteer) und spezielle OSINT-Tools ab und filtert gleichzeitig routinemäßige Personalbeschaffung und interaktive Browsernutzung heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Automatisierte Suchmaschinenaufklärung mit hoher Wiedergabetreue – T1593.002
- **ID:** `T1593_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt automatisierte Aufklärung mithilfe von Suchmaschinen durch Überwachung auf Headless-Browser-Flags und systematische Dorking-Muster.Filtert gezielt legitime Entwickleraktivitäten und interaktive Browsernutzung heraus, um Fehlalarme zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity Social Media Entity Harvesting – T1593.003
- **ID:** `T1593_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatisierte Social-Media-Erkundung mithilfe von Headless-Browsern oder speziellen OSINT-Tools.Konzentriert sich darauf, systematisches Daten-Scraping zu identifizieren und gleichzeitig legitime browserbasierte Benutzeraktivitäten auszuschließen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity Information Repository Reconnaissance – T1594
- **ID:** `T1594.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatisierte Erkundung öffentlicher Informationsspeicher (GitHub, GitLab).Konzentriert sich auf spezielle geheime Scanner und Massen-API-Ernte und filtert gleichzeitig Standard-Entwickler-Workflows (Git Clone/Pull) und autorisierte Sicherheitstools heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity Active Scanning-Erkennung (verhaltensbasiert)
- **ID:** `T1595.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochzuverlässiges aktives Scanverhalten, indem automatisierte Clients identifiziert werden, die innerhalb kurzer Zeit systematisch mehrere sensible Web-Endpunkte von einer externen Quelle aus prüfen.Entwickelt, um Fehlalarme zu minimieren, indem Browser, Überwachung, Gesundheitsprüfungen und bekanntermaßen harmlose Scanner ausgeschlossen werden.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Erkennung externer IP-Block-Scans
- **ID:** `T1595_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochzuverlässiges aktives Scanverhalten, bei dem eine einzelne externe Quell-IP schnell mehrere Ziel-IP-Adressen innerhalb eines kurzen Zeitfensters prüft.Optimiert, um Fehlalarme zu reduzieren, indem bekannte Scanner, Crawler und Cloud-Infrastruktur ausgeschlossen werden.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochzuverlässige externe Schwachstellen-Scan-Aktivität
- **ID:** `T1595_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochzuverlässige Schwachstellen-Scan-Aktivitäten durch Korrelation aggressiven Anforderungsverhaltens, Exploit-Erkennungspfaden, Payload-Indikatoren und bekannter Scanner-Tools.Optimiert, um Fehlalarme in Unternehmensumgebungen zu minimieren.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Aktives Scannen von Wortlisten anhand von Authentifizierungsendpunkten
- **ID:** `T1595_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt hochzuverlässige Wortlisten-Scanaktivitäten, bei denen eine externe Quelle schnell Authentifizierungs- oder Verwaltungsendpunkte mithilfe unterschiedlicher Benutzernamenparameter überprüft, im Einklang mit der automatisierten Aufklärung.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Offene technische Datenbankaufklärung mit hoher Wiedergabetreue – T1596
- **ID:** `T1596.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Verwendung von CLI-Tools und skriptbasierten API-Abfragen, die an technische Datenbanken wie Shodan, Censys und VirusTotal gerichtet sind.Konzentriert sich auf Nicht-Browser-Prozessketten und automatisierte Datenextraktionsmuster.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Hochpräzise WHOIS-Datenbankaufklärung – T1596.001
- **ID:** `T1596_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt automatisierte WHOIS-Aufklärungsmuster.Konzentriert sich auf Massenabfragen zur Domainregistrierung über CLI-Tools und API-basierte Skripte (RDAP) und filtert gleichzeitig standardmäßige browserbasierte Recherchen, Softwarelizenzen und routinemäßige IT-Diagnosen heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Automatisierte High-Fidelity-Suchmaschine Dorking – T1596.002
- **ID:** `T1596_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den automatisierten Einsatz von Suchmaschinen-Idioten und speziellen CLI-Tools, die für die Massenerfassung technischer Daten entwickelt wurden.Filtert interaktive Browsersuchen und legitime, von der IDE ausgelöste Fehlersuchen heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Passive High-Fidelity-DNS-Aufklärung – T1597.003
- **ID:** `T1596_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt automatisierte Aufklärung mithilfe von Passive-DNS-Datenbanken (pDNS).Konzentriert sich auf nicht standardmäßige Prozessketten und CLI-basierte API-Interaktionen, die auf technische OSINT-Repositorys abzielen, während routinemäßige Netzwerk-Fehlerbehebung und browserbasierte Forschung herausgefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Aufklärung digitaler Zertifikate – T1596.004
- **ID:** `T1596_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt automatische Aufklärung, die auf digitale Zertifikate und CT-Protokolle abzielt.Konzentriert sich auf programmatische CLI-Muster (API-basiertes Scraping) und filtert gleichzeitig legitime Zertifikatsvalidierung auf Systemebene und Browserverkehr heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-IP-Infrastrukturaufklärung – T1596.005
- **ID:** `T1596_005.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatische Erkennung von IP-Adressmetadaten.Konzentriert sich auf spezielle OSINT-Tools (Shodan, GreyNoise, Censys) und CLI-basiertes API-Harvesting und filtert gleichzeitig routinemäßige Netzwerkfehlerbehebung, Browserverkehr und EDR-Rauschen heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Website-Erkundung im Besitz von Opfern – T1597
- **ID:** `T1597.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatisierte und systematische Erkundung der organisationseigenen Web-Infrastruktur.Der Schwerpunkt liegt auf der Massendatenextraktion, rekursivem Verzeichnis-Brute-Forcing und der Erkennung sensibler Konfigurationsdateien.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Domäneninfrastrukturaufzählung – T1597.001
- **ID:** `T1597_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt erweiterte und automatisierte Domänen-/DNS-Aufklärung.Konzentriert sich auf ungewöhnliche DNS-Abfragetypen (AXFR, ANY) und professionelle Tools zur Subdomain-Erkennung und filtert gleichzeitig routinemäßige Netzwerkfehlerbehebung heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Geheimnisjagd in Code-Repositories – T1597.002
- **ID:** `T1597_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt professionelle Tools zur Geheimnissuche und manuelle Aufklärungsmuster in Code-Repositories.Konzentriert sich auf eine detaillierte Verlaufsanalyse (Diff-Suche) und die automatisierte Extraktion von Anmeldeinformationen, während Standard-Entwicklungszyklen herausgefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweitertes Phishing zum Sammeln von Informationen und Anmeldeinformationen – T1598
- **ID:** `T1598.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TE.EXE](https://lolbas-project.github.io/lolbas/), [UPDATE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das Sammeln von Anmeldeinformationen nach Phishing und den Diebstahl von Sitzungstoken.Konzentriert sich auf Nicht-Browser-Prozesse, die auf Browserprofildaten zugreifen, und auf verdächtige interaktive Eingabeaufforderungen für Anmeldeinformationen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte Spearphishing-Linkumleitung – T1598.001
- **ID:** `T1598_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige URL-Ausführungsmuster, die von Produktivitäts-Apps stammen.Konzentriert sich auf indirekte Browserstarts (über cmd/powershell) und OAuth-spezifische Parameter zum Sammeln von Anmeldeinformationen, während bekannte SSO-Anbieter herausgefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erweiterte BEC-Mail- und Finanzdaten-Exfiltration – T1598.002
- **ID:** `T1598_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [FINDSTR.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Befehlszeilenzugriffe auf E-Mail-Archive und Finanzdokumente, auf die typischerweise BEC-Kampagnen abzielen.Es filtert legitime Outlook-Indizierung, OneDrive-Synchronisierung und Sicherungen auf Systemebene heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-MFA/OTP-Spoofing und -Ernte – T1598.003
- **ID:** `T1598_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die Erstellung betrügerischer MFA/OTP-Eingabeaufforderungen durch Überwachung ungewöhnlicher PowerShell-UI-Klassenladungen und spezifischer CLI-Schlüsselwörter.Filtert allgemeine IT-Automatisierungs- und Softwarebereitstellungsgeräusche heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Interaktion mit Spearphishing-Anhängen – T1598.004
- **ID:** `T1598_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Ausführungsmuster aus E-Mail-Anhängen.Konzentriert sich auf den HTML-Schmuggel und Office-zu-Skript-Übergänge und filtert gleichzeitig legitime SharePoint-, OneDrive- und Unternehmenssoftware-Update-Rauschen heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Netzwerk-Boundary-Bridging (T1599)
- **ID:** `T1599.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt nicht autorisierte Netzwerkgrenzenüberbrückung.Speziell auf das Handbuch ausgerichtet
Erstellung von „Any-to-Internal“-NAT-Regeln, Portweiterleitung sensibler Ports,
und Überbrückung isolierter Schnittstellen auf Hardwareebene.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Logical Isolation Bypass (T1599.001)
- **ID:** `T1599_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt nicht autorisierte Umgehungen der logischen Netzwerkisolation, z. B. VRF-Routenlecks,
unbefugtes VLAN-Trunking und die Erstellung von L2-Brücken zwischen sicheren Zonen.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Verschlüsselungsversuch schwächen (T1600)
- **ID:** `T1600.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Medium (Mäßiger Geräuschpegel)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt eine unbefugte Schwächung der Systemverschlüsselung (TLS-Downgrade) oder
Umgehung der PowerShell-Zertifikatsvalidierung, initiiert von Nicht-System- oder
verdächtig lokalisierte Prozesse.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-System-Image-Patching (T1600.001)
- **ID:** `T1600_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Versuche, die System-Image-Integrität durch Deaktivierung der Driver Signature Enforcement (DSE) zu schwächen.
Ändern der Boot-Konfigurationsdaten (BCD) oder Patchen kritischer Systembinärdateien (CI.dll, NTOSKRNL.exe)
Verwendung von Nicht-System-Prozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Entitätsüberprüfung deaktivieren (T1600.002)
- **ID:** `T1600_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [GPSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen der Systemvertrauenseinstellungen und der Zertifikatsüberprüfung
durch Überwachung auf verdächtige Certutil-Nutzung und registrierungsbasiertes Authenticode/WinTrust
Umgehungen, die von nicht vertrauenswürdigen Prozessen initiiert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Netzwerk-OS-Image-Modifikation (T1601)
- **ID:** `T1601.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt unbefugte Änderungen an Betriebssystem-Images von Netzwerkgeräten.
Konzentriert sich auf Binär-Uploads über unsichere Protokolle und Boot-System-Überschreibungen
Wird außerhalb vertrauenswürdiger Verwaltungsfenster oder Hosts durchgeführt.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Netzwerk-Binär-Patching (T1601.001)
- **ID:** `T1601_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt unbefugtes Low-Level-Patching von Netzwerk-Betriebssystem-Binärdateien.
Konzentriert sich auf das erneute Einhängen des Dateisystems (Lesen/Schreiben), binäre Manipulation (dd, xxd),
und das Laden von Kernelmodulen (insmod) außerhalb der autorisierten Wartung.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Upgrade für bösartige Netzwerk-Betriebssysteme (T1601.002)
- **ID:** `T1601_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt nicht autorisierte oder böswillige Netzwerk-Betriebssystem-Upgrades durch Korrelation
Upgrade-Befehle mit unsicheren Protokollen, nicht vertrauenswürdigen Quellen oder
kryptografische Signaturfehler.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Automatisierte Ultra-Pro-High-Fidelity-Netzwerkfreigabeerfassung (T1602)
- **ID:** `T1602.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt hochverdächtige, automatisierte Datenerfassung aus Netzwerkfreigaben durch
Identifizieren der Kombination aus UNC-Pfaddurchquerung, sensiblen Dateierweiterungen,
und rekursive Kopierlogik, die aus nicht vertrauenswürdigen Prozesslinien stammt.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Admin-Share-Datenexfiltration (T1602.001)
- **ID:** `T1602_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Datenerfassung oder Bereitstellung über administrative Freigaben (C$, ADMIN$)
durch Korrelation anomaler Prozesslinien, nicht standardmäßiger Quellpfade,
und die Verwendung rekursiver Erkennungsbefehle innerhalb derselben Sitzung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Cloud Share Exfiltration (T1602.002)
- **ID:** `T1602_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [TAR.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt äußerst verdächtige Massendatensammlungen aus Cloud-Synchronisierungswurzeln (OneDrive,
SharePoint, Google Drive) durch Überwachung auf rekursive Lese-/Kopiermuster
kombiniert mit Archivierungstools oder verdächtigen Staging-Zielen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Web-Token-Fälschung (T1606)
- **ID:** `T1606.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [TEAMS.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugtes Fälschen oder Diebstahl von Web-Anmeldeinformationen (SAML, Cookies, OAuth-Tokens).
Konzentriert sich auf Nicht-Browser-Prozesse, die auf DPAPI-Hauptschlüssel zugreifen, verdächtiges SQLite
Abfragen in Token-Datenbanken und Generierung von Golden SAML-Artefakten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity-Web-Cookie-Ernte (T1606.001)
- **ID:** `T1606_001.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das unbefugte Extrahieren von Browser-Cookies und den entsprechenden Cookies
AES-Verschlüsselungsschlüssel aus „Local State“-Dateien.Es zielt gezielt ab
Nicht vertrauenswürdige Prozesse (Interpreter, nicht signierte Binärdateien) beim Filtern
legitimes Browser- und Electron-Anwendungsverhalten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro High-Fidelity Web Token Forgery & Golden SAML (T1606.002)
- **ID:** `T1606_002.yaml`
- **Qualitätsindikator:** `60/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt unbefugte Fälschungen von Web-Tokens (SAML, OAuth) durch Überwachung
verdächtiger Zugriff auf IDP-Signaturschlüssel, AD FS-Datenbankextraktion und
die Verwendung spezialisierter Cloud-nativer Fälschungs-Frameworks wie Roadtools und AADInternals.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomale Infrastrukturbereitstellung und Ressourcenbereitstellung
- **ID:** `T1608.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die Verwendung von Cloud-CLI-Tools und IaC-Binärdateien zur Bereitstellung gegnerischer Ressourcen.
Es konzentriert sich auf Nicht-Standard-Benutzer, die Uploads oder Infrastrukturänderungen durchführen
Aktionen, Herausfiltern autorisierter CI/CD-Pipelines und IT-Administration.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomale Malware-Bereitstellung in der externen Infrastruktur
- **ID:** `T1608_001.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt durch Überwachung die Einschleusung von Malware in die externe Infrastruktur
Nicht-browserbasierte Uploads auf Cloud-Speicher-, Dateifreigabe- und Code-Hosting-Plattformen
Verwendung von Befehlszeilentools oder ungewöhnlichen Prozessen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomales offensives Tool-Staging und externer Upload
- **ID:** `T1608_002.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt durch Überwachung die Bereitstellung anstößiger Tools für die externe Infrastruktur
CLI-basierte Uploads aus nicht standardmäßigen Verzeichnissen.Konzentriert sich auf das „Inszenierung-dann-Versand“
Muster, bei dem Hacktools in externe Drop-Zones verschoben werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Strategisches Staging digitaler Zertifikate im vertrauenswürdigen Stammspeicher
- **ID:** `T1608_003.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [MMC.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Befehlszeileninstallation von Zertifikaten im Trusted Root-Speicher.
Angreifer tun dies, um Vertrauen in die C2-Infrastruktur aufzubauen oder zu ermöglichen
transparentes SSL/TLS-Abfangen (MitM).

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomale Webinhaltsmodifikation für Drive-by-Staging
- **ID:** `T1608_004.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Speicherintensiv)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Änderungen an Webserver-Inhaltsverzeichnissen (Web-Root)
initiiert durch nicht standardmäßige Prozesse oder interaktive Shells.Dieses Verhalten ist
Dies ist typischerweise dann der Fall, wenn ein Angreifer eine Drive-by-Download-Site inszeniert oder bösartige Skripte einschleust.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Strategische Inszenierung bösartiger Link-Ziele
- **ID:** `T1608_005.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die automatisierte Vorbereitung bösartiger Linkziele durch Überwachung
CLI-basierte Interaktionen mit URL-Shortener-APIs oder cloudbasiertem Redirector-Staging
initiiert durch nicht autorisierte Benutzer oder ungewöhnliche übergeordnete Prozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Anomale SEO-Vergiftung und Metadaten-Staging
- **ID:** `T1608_006.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die Vorbereitung einer SEO-Poisoning-Infrastruktur durch Überwachung
unbefugte CMS-Manipulation, automatisiertes Content-Spinnen und die Verwendung von
bekannte Black-Hat-SEO-Tools auf Webservern oder Staging-Umgebungen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Interaktive Shell-Ausführung für High-Fidelity-Container
- **ID:** `T1609.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt unbefugten interaktiven Shell-Zugriff auf laufende Container mit
kubectl oder docker exec.Filtert legitime Gesundheitsprüfungen und CI/CD-Automatisierung
sich auf manuelle, risikoreiche Eingriffe zu konzentrieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Erkennung der Bereitstellung bösartiger Container
- **ID:** `T1610.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt die Bereitstellung von Containern mit Hochrisikokonfigurationen
Erleichterung des Entweichens oder Fortbestehens des Containers.Konzentriert sich auf den privilegierten Modus,
Ressourcenfreigabe auf Hostebene und nicht standardmäßige Bildquellen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Container-Flucht und Host-Zugriff (T1611)
- **ID:** `T1611.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt unbefugte Container-Escape-Versuche und Host-Zugriffe.Konzentriert sich auf
nicht standardmäßige privilegierte Ausführungen, gefährliche Mounts und uneingeschränkte Sicherheit
Kontexte, während legitime Cluster-Infrastrukturkomponenten herausgefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultra-Pro Stealthy Local Image Build (T1612)
- **ID:** `T1612.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt lokale Container-Image-Builds mit hoher Wiedergabetreue, die von verdächtigen Personen initiiert wurden
Benutzer oder Prozesse, wobei der Schwerpunkt auf der Erstellung von Bildern nach der Nutzung liegt
Umgehung des Registry-Scans.Filtert vertrauenswürdige CI/CD-Pipelines heraus und
bekannte Build-Systeme.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Ultraprofessioneller High-Fidelity-Container und Kubernetes Discovery
- **ID:** `T1613.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt eine hochpräzise Aufzählung von Containern, Kubernetes-Ressourcen und Geheimnissen.
Konzentriert sich auf die Selbstabfrage der Identität (auth can-i), die Entdeckung von Geheimnissen und Konfigurationen,
und anomale Prozesslinie.Filtert Hochfrequenzüberwachung heraus und
Systemsonden, um Fehlalarme zu reduzieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Systemstandort und regionale Kill-Switch-Erkennung
- **ID:** `T1614.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [POWERPNT.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt den Zielsystemstandort und die regionale Erkennung, die häufig von Ransomware und Malware zur geografischen Ausrichtung oder Ausgrenzung verwendet werden (Kill-Switch-Logik).Konzentriert sich auf die registrierungsbasierte Tastatur-/Gebietsschema-Aufzählung in Kombination mit externen IP-zu-Geo-API-Aufrufen aus verdächtigen Ausführungskontexten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Erkennung von High-Fidelity-Systemsprache und Tastaturlayout
- **ID:** `T1614_001.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [REG.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die gezielte Erkennung von Systemsprache und Tastaturlayout und konzentriert sich dabei auf Malware-Kill-Switch-Prüfungen und Umgebungsschlüsselung.Kombiniert Registrierungsabfragen, CLI/PowerShell-Cmdlets und die Umleitung verdächtiger Ausgaben.Minimiert Fehlalarme durch übergeordneten Prozess, Integritätsstufe und Filterung vertrauenswürdiger Pfade.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Erkennung von Gruppenrichtlinien
- **ID:** `T1615.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erfassung von Gruppenrichtlinien, einschließlich der Erfassung von GPO-Berichten und der Richtlinienaufzählung aus ungewöhnlichen Ausführungskontexten.Filtert legitime Verwaltungs- und Helpdesk-Aktivitäten mithilfe von Befehlszeilen-, übergeordneten Prozess- und Integritätsstufenprüfungen heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Erkennung von Cloud-Speicherobjekten
- **ID:** `T1619.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt die systematische Erkennung von Cloud-Speicherobjekten in AWS S3, Azure Blobs und Google Cloud Storage durch Überwachung rekursiver Auflistungen, metadatenintensiver API-Aufrufe und anomaler Ausgabeumleitung.Filtert hochvertrauenswürdige Backup-, ETL- und DevOps-Automatisierungskonten.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Reflective-Code-Laden und In-Memory-Assembly-Ausführung
- **ID:** `T1620.yaml`
- **Qualitätsindikator:** `80/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSBUILD.EXE](https://lolbas-project.github.io/lolbas/), [DOTNET.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt das Laden von reflektierendem Code und die Ausführung von Assemblys im Arbeitsspeicher durch Überwachung der Speicherzuweisung mit Ausführungsflags, Schreibvorgängen im Prozessspeicher und Lademustern für .NET-Reflection-Assemblys in Kombination.Filtert legitime Entwicklungs- und CI/CD-Prozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige MFA-Prompt-Bombing- oder Authentifizierungs-Flood-Automatisierung
- **ID:** `T1621.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [SCHTASKS.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielles MFA-Prompt-Bombing oder automatisierte Authentifizierungsfluten mithilfe von PowerShell-Identitätsmodulen, Azure/Okta-Tools oder Headless-Browser-Frameworks, die in nicht interaktiven oder versteckten Kontexten ausgeführt werden.Der Schwerpunkt liegt auf Schleifenlogik in Kombination mit Tools zur Identitätsauthentifizierung.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtiger Anti-Debug-API-Zugriff aus nicht gesichertem oder User-Space-Speicher
- **ID:** `T1622.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [VSJITDEBUGGER.EXE](https://lolbas-project.github.io/lolbas/), [WINDBG.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielle Debugger-Umgehungstechniken durch die Identifizierung verdächtiger Zugriffe auf Prozesse in Kombination mit Anti-Debug-API-Mustern in CallTrace, insbesondere wenn sie aus nicht gesicherten Speicherbereichen oder nicht standardmäßigen Ausführungspfaden stammen.Filtert bekannte Entwicklungstools und Windows-Fehlerberichte.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige macOS LaunchAgent- oder LaunchDaemon Plist-Änderung
- **ID:** `T1647.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt verdächtige Änderungen oder Erstellungen von macOS LaunchAgent- oder LaunchDaemon-Eigenschaftenlistendateien mithilfe von Befehlszeilendienstprogrammen.Konzentriert sich auf persistenzbezogene Schlüssel und abnormale Ausführungskontexte und filtert legitime Apple-Systemprozesse.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Persistenz oder Missbrauch von serverlosen High-Fidelity-Funktionen
- **ID:** `T1648.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)
- **Beschreibung:** Erkennt verdächtige Erstellungen oder Aktualisierungen von AWS Lambda-Funktionen durch Überwachung
nicht automatisierte Aktivitäten, ungewöhnliche Quell-IPs und riskante Konfigurationen.
Konzentriert sich auf die Umgehung von CI/CD-Pipelines.

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Aktivität beim Exportieren oder Diebstahl von Zertifikaten und privaten Schlüsseln
- **ID:** `T1649.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CERTUTIL.EXE](https://lolbas-project.github.io/lolbas/), [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSIEXEC.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenziellen Diebstahl digitaler Zertifikate und privater Schlüssel durch Certutil-Missbrauch, PowerShell-basierten Schlüsselexport oder anstößige Tools (z. B. Mimikatz crypto::export, Certify).Konzentriert sich auf Exportvorgänge, Zugriff auf private Schlüssel und verdächtige Ausgabe-Staging-Pfade.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## High-Fidelity-Cloud-Kontoerwerb und -Initialisierung – T1650
- **ID:** `T1650.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))
- **Beschreibung:** Erkennt den Erwerb oder die unbefugte Einrichtung von Cloud-Konten.Konzentriert sich auf die Konfiguration von Anmeldeinformationen, die Profilerstellung und die automatisierte SDK-basierte Identitätserfassung und filtert gleichzeitig autorisierte DevOps-Automatisierung heraus.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Missbrauch von High-Fidelity-Cloud-Verwaltungsagenten
- **ID:** `T1651.yaml`
- **Qualitätsindikator:** `70/100` ⭐⭐⭐⭐ (Gut)
- **Kritikalität:** 🔴 (critical)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [AT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt eine anomale Prozessausführung, die von Cloud-Management-Agents (AWS SSM, Azure Guest Agent) initiiert wird.
Angreifer nutzen diese vertrauenswürdigen Pfade, um Aufklärungs- oder Credential-Dumping-Befehle auszuführen
die herkömmliche Netzwerk-Perimeter-Verteidigungsmaßnahmen umgehen.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Aufzählung verdächtiger Gerätetreiber aus anomalem Kontext (BYOVD Recon)
- **ID:** `T1652.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [EXPLORER.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [PNPUTIL.EXE](https://lolbas-project.github.io/lolbas/), [QUERY.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [SC.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Gerätetreiber-Erkennungsaktivitäten mithilfe nativer Windows-Dienstprogramme, WMI oder PowerShell in anormalen Ausführungskontexten.Konzentriert sich auf Aufklärungsmuster, die häufig vor dem Missbrauch von Bring Your Own Vulnerable Driver (BYOVD) beobachtet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Manipulation der Ultra-Pro-Energieeinstellungen (T1137.001)
- **ID:** `T1653.yaml`
- **Qualitätsindikator:** `50/100` ⭐⭐⭐ (Medium)
- **Kritikalität:** 🟡 (medium)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt unbefugte Änderungen der Energieeinstellungen, die darauf abzielen, den Ruhezustand zu verhindern oder
Winterschlaf.Konzentriert sich auf die Befehlszeilenautomatisierung (powercfg) über verdächtige
übergeordnete Prozesse wie PowerShell oder CMD, während legitime UI-basierte Änderungen gefiltert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**


---
## Aufzählung verdächtiger Ereignisprotokolle aufgrund eines anomalen Ausführungskontexts
- **ID:** `T1654.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Aufzählungen von Windows-Ereignisprotokollen mithilfe nativer Dienstprogramme (wevtutil) oder PowerShell-Cmdlets (Get-WinEvent, Get-EventLog) aus anomalen Ausführungskontexten.Der Schwerpunkt liegt auf der Erkennung von Protokollkanälen und der Erfassung von Metadaten, die möglicherweise zur Identifizierung von Sicherheitstools oder zur Umgehung der Erkennung verwendet werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtiger Identitätswechsel durch RunAs-Missbrauch oder irreführende lokale Kontoerstellung
- **ID:** `T1656.yaml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt technische Nachahmungsversuche, einschließlich verdächtiger RunAs-Nutzung für laterale Bewegungen und die Erstellung irreführender lokaler Konten, die Führungs- oder Administratoridentitäten außerhalb standardmäßiger IT-Bereitstellungsprozesse imitieren.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtige Manipulation der Zwischenablage und Zugriff auf Finanzdokumente über einen nicht vertrauenswürdigen übergeordneten Prozess
- **ID:** `T1657.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [CMD.EXE](https://lolbas-project.github.io/lolbas/), [CSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/), [MSHTA.EXE](https://lolbas-project.github.io/lolbas/), [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WSCRIPT.EXE](https://lolbas-project.github.io/lolbas/), [EXCEL.EXE](https://lolbas-project.github.io/lolbas/), [WINWORD.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt potenzielle Finanzdiebstahl- oder Betrugsaktivitäten im Zusammenhang mit der Manipulation der Zwischenablage (z. B. Adressvertauschung) in Kombination mit dem Zugriff auf Finanzdokumente, die von verdächtigen übergeordneten Prozessen wie Browsern, Office-Anwendungen oder webbasierten Diensten initiiert werden.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Professionelle Content-Impersonation und Infrastrukturspiegelung
- **ID:** `T1659.yaml`
- **Qualitätsindikator:** `90/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Hoch (Starke Filterung empfohlen (viele Protokolle))

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [MSEDGE.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt Tools und CLI-Muster, die zum Klonen oder Nachahmen legitimer Webinhalte verwendet werden.
Der Schwerpunkt liegt auf der rekursiven Spiegelung interner Portale und dem Einsatz von Phishing
Frameworks, die legitime Entwicklung und browserbasierte Aktivitäten herausfiltern.

#### 🚨 Reaktions-Playbook
1. **Prozessprüfung: Überprüfen Sie den übergeordneten Prozess und die Befehlszeile.**
2. **Binärprüfung: Führen Sie den Hash der Datei auf VirusTotal aus.**
3. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**


---
## Verdächtiger Zugriff auf den LSASS-Prozessspeicher (Credential Dumping-Versuch)
- **ID:** `credential_dumping_lsass.yml`
- **Qualitätsindikator:** `100/100` ⭐⭐⭐⭐⭐ (Exzellent)
- **Kritikalität:** 🟠 (high)
- **Geschätzter Geräuschpegel:** Unbekannt (Keine Daten)

> ⚠️ **LOLBAS-Auswirkungen: Diese Regel betrifft eine Factory-Binärdatei, die missbraucht werden kann:** [RUNDLL32.EXE](https://lolbas-project.github.io/lolbas/), [WMIC.EXE](https://lolbas-project.github.io/lolbas/), [COMSVCS.DLL](https://lolbas-project.github.io/lolbas/), [DUMP64.EXE](https://lolbas-project.github.io/lolbas/), [PROCDUMP.EXE](https://lolbas-project.github.io/lolbas/)
- **Beschreibung:** Erkennt verdächtige Zugriffe auf den LSASS-Prozessspeicher, die auf Anmeldeinformations-Dump-Aktivitäten hinweisen können (z. B. Mimikatz, ProcDump, Task-Manager-Dump, comsvcs.dll MiniDump oder andere Speicher-Dump-Techniken).

#### 🚨 Reaktions-Playbook
1. **Triage: Untersuchen Sie Rohereignisse in SIEM.**
2. **Dringend: Sollte sich der Verdacht bestätigen, den betroffenen Wirt isolieren!**

