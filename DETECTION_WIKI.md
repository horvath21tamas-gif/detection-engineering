# 🛡️ Detection Rule Knowledge Base

## 📖 Tartalomjegyzék
- [Suspicious Access to LSASS Process Memory](#suspicious-access-to-lsass-process-memory)
- [Ultra-Pro Stealthy Direct Volume Access (T1006)](#ultra-pro-stealthy-direct-volume-access-(t1006))
- [Rapid Logons to Multiple Distant Hosts by Same User](#rapid-logons-to-multiple-distant-hosts-by-same-user)
- [Suspicious RDP Logon from Unusual Source](#suspicious-rdp-logon-from-unusual-source)
- [Suspicious Base64-Encoded PowerShell Command with Network Activity](#suspicious-base64-encoded-powershell-command-with-network-activity)
- [Legitimate Windows Binary Copied to User-Writable Location](#legitimate-windows-binary-copied-to-user-writable-location)
- [High-Fidelity Logon Script Persistence (T1037)](#high-fidelity-logon-script-persistence-(t1037))
- [High-Fidelity UserInitMprLogonScript Persistence](#high-fidelity-userinitmprlogonscript-persistence)
- [High-Fidelity Netsh Helper DLL Persistence](#high-fidelity-netsh-helper-dll-persistence)
- [Ultra-Pro Network Logon Script/Shortcut Modification (T1037.003)](#ultra-pro-network-logon-scriptshortcut-modification-(t1037003))
- [Ultra-Pro RC Script and Init.d Persistence (T1037.004)](#ultra-pro-rc-script-and-initd-persistence-(t1037004))
- [Ultra-Pro macOS Startup Items Persistence (T1037.005)](#ultra-pro-macos-startup-items-persistence-(t1037005))
- [Suspicious Remote Process Creation via WMIC](#suspicious-remote-process-creation-via-wmic)
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
- [Suspicious Credential API Hooking via Win32 Libraries](#suspicious-credential-api-hooking-via-win32-libraries)
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
- [Security Event Log Cleared Using wevtutil.exe](#security-event-log-cleared-using-wevtutilexe)
- [High-Fidelity Software Deployment Tool Abuse Detection](#high-fidelity-software-deployment-tool-abuse-detection)
- [High-Fidelity Anomalous Logon via Valid Account](#high-fidelity-anomalous-logon-via-valid-account)
- [High-Fidelity Default Account Abuse Detection](#high-fidelity-default-account-abuse-detection)
- [High-Fidelity Domain Account Lateral Movement Anomaly](#high-fidelity-domain-account-lateral-movement-anomaly)
- [High-Fidelity Local Account Remote Access Detection](#high-fidelity-local-account-remote-access-detection)
- [High-Fidelity Cloud Account Compromise (Entra ID)](#high-fidelity-cloud-account-compromise-(entra-id))
- [Suspicious Use of net user or net localgroup via cmd.exe](#suspicious-use-of-net-user-or-net-localgroup-via-cmdexe)
- [High-Fidelity Process Execution from Removable Media](#high-fidelity-process-execution-from-removable-media)
- [High-Fidelity Account Manipulation - Persistence Focused](#high-fidelity-account-manipulation---persistence-focused)
- [High-Fidelity Entra ID Application Credential Addition](#high-fidelity-entra-id-application-credential-addition)
- [High-Fidelity Exchange Mailbox Permission Grant (T1098.002)](#high-fidelity-exchange-mailbox-permission-grant-(t1098002))
- [High-Fidelity Entra ID App Certificate Addition](#high-fidelity-entra-id-app-certificate-addition)
- [High-Fidelity Azure Role Assignment Escalation](#high-fidelity-azure-role-assignment-escalation)
- [High-Fidelity Device Registration Persistence (T1098.005)](#high-fidelity-device-registration-persistence-(t1098005))
- [High-Fidelity MFA Method Addition](#high-fidelity-mfa-method-addition)
- [Suspicious Use of Built-in Windows Tools for File Download and Code Execution](#suspicious-use-of-built-in-windows-tools-for-file-download-and-code-execution)
- [High-Fidelity Native API Abuse via LOLBins](#high-fidelity-native-api-abuse-via-lolbins)
- [Multiple Failed Login Attempts for Single User (Possible Password Guessing)](#multiple-failed-login-attempts-for-single-user-(possible-password-guessing))
- [High-Fidelity Shared Module Load from Untrusted Path](#high-fidelity-shared-module-load-from-untrusted-path)
- [Anomalous External Remote Service Access Context](#anomalous-external-remote-service-access-context)
- [Ultra-Pro Access Token Manipulation & Impersonation (T1134)](#ultra-pro-access-token-manipulation-&-impersonation-(t1134))
- [Ultra-Pro Token Impersonation via LSASS Handle Duplication (T1134.001)](#ultra-pro-token-impersonation-via-lsass-handle-duplication-(t1134001))
- [Ultra-Pro Create Process with Token (T1134.002)](#ultra-pro-create-process-with-token-(t1134002))
- [Ultra-Pro Make and Impersonate Token (T1134.003)](#ultra-pro-make-and-impersonate-token-(t1134003))
- [Ultra-Pro Parent PID Spoofing & Process Tree Violation (T1134.004)](#ultra-pro-parent-pid-spoofing-&-process-tree-violation-(t1134004))
- [Ultra-Pro SID-History Injection & DS Manipulation (T1134.005)](#ultra-pro-sid-history-injection-&-ds-manipulation-(t1134005))
- [Ultra-Pro Unauthorized Account Creation (T1136)](#ultra-pro-unauthorized-account-creation-(t1136))
- [Ultra-Pro Unauthorized Local Account Creation (T1136.001)](#ultra-pro-unauthorized-local-account-creation-(t1136001))
- [Ultra-Pro Unauthorized Domain Account Creation (T1136.002)](#ultra-pro-unauthorized-domain-account-creation-(t1136002))
- [Ultra-Pro Unauthorized Cloud Account Creation (T1136.003)](#ultra-pro-unauthorized-cloud-account-creation-(t1136003))
- [Ultra-Pro Office Application Startup Persistence (T1137)](#ultra-pro-office-application-startup-persistence-(t1137))
- [Ultra-Pro Office Global Template Integrity (T1137.001)](#ultra-pro-office-global-template-integrity-(t1137001))
- [Ultra-Pro Office Test DLL Persistence (T1137.002)](#ultra-pro-office-test-dll-persistence-(t1137002))
- [Ultra-Pro Outlook Custom Forms Persistence (T1137.003)](#ultra-pro-outlook-custom-forms-persistence-(t1137003))
- [Ultra-Pro Outlook Home Page Hijacking & Bypass (T1137.004)](#ultra-pro-outlook-home-page-hijacking-&-bypass-(t1137004))
- [Ultra-Pro Office Security Policy Tampering (T1137.005)](#ultra-pro-office-security-policy-tampering-(t1137005))
- [Ultra-Pro Office Add-in Binary Persistence (T1137.006)](#ultra-pro-office-add-in-binary-persistence-(t1137006))
- [Ultra-Pro Stealthy Deobfuscation/Decoding (T1140)](#ultra-pro-stealthy-deobfuscationdecoding-(t1140))
- [Ultra-Pro Browser Extension Force-Install Persistence (T1176)](#ultra-pro-browser-extension-force-install-persistence-(t1176))
- [Browser-Originating Shell or System Tool Execution](#browser-originating-shell-or-system-tool-execution)
- [Suspicious Cross-Site Scripting (XSS) Attempt Detected on Web Server](#suspicious-cross-site-scripting-(xss)-attempt-detected-on-web-server)
- [High-Fidelity Supply Chain Compromise Detection (Post-Update Anomaly)](#high-fidelity-supply-chain-compromise-detection-(post-update-anomaly))
- [High-Fidelity Dependency Poisoning Detection](#high-fidelity-dependency-poisoning-detection)
- [High-Fidelity Compromised Binary Activity (Post-Update)](#high-fidelity-compromised-binary-activity-(post-update))
- [High-Fidelity Hardware/Firmware Manipulation Detection](#high-fidelity-hardwarefirmware-manipulation-detection)
- [Suspicious File Download via Bitsadmin (High Fidelity)](#suspicious-file-download-via-bitsadmin-(high-fidelity))
- [High-Fidelity Trusted Relationship Abuse Detection](#high-fidelity-trusted-relationship-abuse-detection)
- [Malicious Hardware-Induced Command Execution (HID Injection)](#malicious-hardware-induced-command-execution-(hid-injection))
- [High-Fidelity Client-Side Exploitation and Shell Spawning](#high-fidelity-client-side-exploitation-and-shell-spawning)
- [Suspicious Child Process Spawned by Microsoft Office Application (High Fidelity)](#suspicious-child-process-spawned-by-microsoft-office-application-(high-fidelity))
- [High-Fidelity User Execution of Malicious Link (T1204.001)](#high-fidelity-user-execution-of-malicious-link-(t1204001))
- [High-Fidelity User Execution of Malicious File](#high-fidelity-user-execution-of-malicious-file)
- [High-Fidelity Execution from Mounted Virtual Disk (T1204.003)](#high-fidelity-execution-from-mounted-virtual-disk-(t1204003))
- [Adathalászat rosszindulatú linken keresztül, domain és feladó rendellenességekkel](#adathalászat-rosszindulatú-linken-keresztül-domain-és-feladó-rendellenességekkel)
- [Ultra-Pro Traffic Signaling & Port Knocking (T1205)](#ultra-pro-traffic-signaling-&-port-knocking-(t1205))
- [Ultra-Pro Port Knocking & Raw Socket Listener (T1205.001)](#ultra-pro-port-knocking-&-raw-socket-listener-(t1205001))
- [Ultra-Pro Socket Filter & WFP Traffic Signaling (T1205.002)](#ultra-pro-socket-filter-&-wfp-traffic-signaling-(t1205002))
- [Ultra-Pro High-Fidelity Privilege Escalation Exploitation (T1211)](#ultra-pro-high-fidelity-privilege-escalation-exploitation-(t1211))
- [Suspicious Mshta Execution of Remote Script (High Fidelity)](#suspicious-mshta-execution-of-remote-script-(high-fidelity))
- [Suspicious Msiexec Installation from Remote URL (High Fidelity)](#suspicious-msiexec-installation-from-remote-url-(high-fidelity))
- [Suspicious Regsvr32 Execution Indicative of LOLBAS Abuse (High Fidelity)](#suspicious-regsvr32-execution-indicative-of-lolbas-abuse-(high-fidelity))
- [Suspicious Rundll32 Execution with Script or Remote Payload (High Fidelity)](#suspicious-rundll32-execution-with-script-or-remote-payload-(high-fidelity))
- [Suspicious Use of Legitimate Remote Administration Tools Outside Enterprise Pattern](#suspicious-use-of-legitimate-remote-administration-tools-outside-enterprise-pattern)
- [Ultra-Pro High-Fidelity Permissions Modification (T1222)](#ultra-pro-high-fidelity-permissions-modification-(t1222))
- [Ultra-Pro High-Fidelity Windows File Permissions Modification (T1222.001)](#ultra-pro-high-fidelity-windows-file-permissions-modification-(t1222001))
- [Ultra-Pro High-Fidelity Linux File Permissions Modification (T1222.002)](#ultra-pro-high-fidelity-linux-file-permissions-modification-(t1222002))
- [Ultra-Pro High-Fidelity Execution Guardrails Discovery (T1480)](#ultra-pro-high-fidelity-execution-guardrails-discovery-(t1480))
- [Ultra-Pro Environmental Keying Discovery (T1480.001)](#ultra-pro-environmental-keying-discovery-(t1480001))
- [Ultra-Pro Domain Policy Manipulation & GPO Abuse (T1484)](#ultra-pro-domain-policy-manipulation-&-gpo-abuse-(t1484))
- [Ultra-Pro Group Policy Modification & Abuse (T1484.001)](#ultra-pro-group-policy-modification-&-abuse-(t1484001))
- [Ultra-Pro Domain Trust Tampering & SID Filtering Bypass (T1484.002)](#ultra-pro-domain-trust-tampering-&-sid-filtering-bypass-(t1484002))
- [Ransomware Preparation Activity Detected on Windows Host (High Fidelity)](#ransomware-preparation-activity-detected-on-windows-host-(high-fidelity))
- [Suspicious Deletion of Volume Shadow Copies via VSSAdmin (High Fidelity)](#suspicious-deletion-of-volume-shadow-copies-via-vssadmin-(high-fidelity))
- [Ultra-Pro Web Shell Execution Patterns (T1505.003)](#ultra-pro-web-shell-execution-patterns-(t1505003))
- [Ultra-Pro SQL Server Command Shell Execution (T1505.001)](#ultra-pro-sql-server-command-shell-execution-(t1505001))
- [Ultra-Pro IIS Native Module Injection (T1505.002)](#ultra-pro-iis-native-module-injection-(t1505002))
- [Webshell Upload or Interaction Detected on Web Server (High Fidelity)](#webshell-upload-or-interaction-detected-on-web-server-(high-fidelity))
- [Ultra-Pro Mainboard Boot Image & SPI Flash Tampering (T1542.004)](#ultra-pro-mainboard-boot-image-&-spi-flash-tampering-(t1542004))
- [Ultra-Pro Terminal Services DLL Hijacking (T1505.005)](#ultra-pro-terminal-services-dll-hijacking-(t1505005))
- [Exploit-Grade Unauthorized Container Image Execution (Implant Container Image)](#exploit-grade-unauthorized-container-image-execution-(implant-container-image))
- [Ultra-Pro Pre-OS Boot Manipulation (T1542)](#ultra-pro-pre-os-boot-manipulation-(t1542))
- [Ultra-Pro ROM Kit & UEFI Firmware Tampering (T1542.001)](#ultra-pro-rom-kit-&-uefi-firmware-tampering-(t1542001))
- [Ultra-Pro Component Firmware Tampering (T1542.002)](#ultra-pro-component-firmware-tampering-(t1542002))
- [Ultra-Pro Bootkit Persistence & EFI Tampering (T1542.003)](#ultra-pro-bootkit-persistence-&-efi-tampering-(t1542003))
- [Ultra-Pro Mainboard Boot Image & SPI Flash Tampering (T1542.004)](#ultra-pro-mainboard-boot-image-&-spi-flash-tampering-(t1542004))
- [Ultra-Pro DHCP/PXE Boot Hijacking (T1542.005)](#ultra-pro-dhcppxe-boot-hijacking-(t1542005))
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
- [Ultra-Pro Privilege Escalation via Registry Hijacking (T1548.002)](#ultra-pro-privilege-escalation-via-registry-hijacking-(t1548002))
- [Ultra-Pro Setuid/Setgid Bit Manipulation (T1548.001)](#ultra-pro-setuidsetgid-bit-manipulation-(t1548001))
- [UAC Bypass via Fodhelper Registry Hijack (High Fidelity)](#uac-bypass-via-fodhelper-registry-hijack-(high-fidelity))
- [Ultra-Pro Sudoers Manipulation and Sudo Abuse (T1548.003)](#ultra-pro-sudoers-manipulation-and-sudo-abuse-(t1548003))
- [Ultra-Pro AppleScript Privilege Escalation (T1548.004)](#ultra-pro-applescript-privilege-escalation-(t1548004))
- [Ultra-Pro SUID Desktop Entry & Shortcut Abuse (T1548.005)](#ultra-pro-suid-desktop-entry-&-shortcut-abuse-(t1548005))
- [Ultra-Pro Client Binary Integrity Compromise (T1554)](#ultra-pro-client-binary-integrity-compromise-(t1554))
- [Nem böngészős folyamat hozzáférése a böngésző hitelesítőadat-tárolóihoz (High Fidelity)](#nem-böngészős-folyamat-hozzáférése-a-böngésző-hitelesítőadat-tárolóihoz-(high-fidelity))
- [Exploit-Grade Authentication Process Hijack via Suspicious DLL Registration](#exploit-grade-authentication-process-hijack-via-suspicious-dll-registration)
- [Exploit-Grade Security Support Provider Hijacking (LSA SSP)](#exploit-grade-security-support-provider-hijacking-(lsa-ssp))
- [Exploit-Grade Password Filter DLL Hijacking via LSA Notification Packages](#exploit-grade-password-filter-dll-hijacking-via-lsa-notification-packages)
- [Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003)](#ultra-pro-pam-integrity-hijacking-&-backdoor-(t1556003))
- [Ultra-Pro Network Device Authentication Hijacking (T1556.004)](#ultra-pro-network-device-authentication-hijacking-(t1556004))
- [Ultra-Pro SID History Injection Correlation (T1556.005)](#ultra-pro-sid-history-injection-correlation-(t1556005))
- [Ultra-Pro Entra ID MFA Method Hijacking (T1556.006)](#ultra-pro-entra-id-mfa-method-hijacking-(t1556006))
- [Ultra-Pro Hybrid Identity Sync Manipulation (T1556.007)](#ultra-pro-hybrid-identity-sync-manipulation-(t1556007))
- [Ultra-Pro Network-to-Cloud Auth Hijacking (T1556.008)](#ultra-pro-network-to-cloud-auth-hijacking-(t1556008))
- [Gyanús Kerberos TGS jegykérés (Kerberoasting)](#gyanús-kerberos-tgs-jegykérés-(kerberoasting))
- [High-Fidelity Indirect IPC and COM Execution](#high-fidelity-indirect-ipc-and-com-execution)
- [Gyanús elnevezett csővezeték-létrehozás, amely utólagos kihasználási eszközökhöz kapcsolódik (High Fidelity)](#gyanús-elnevezett-csővezeték-létrehozás-amely-utólagos-kihasználási-eszközökhöz-kapcsolódik-(high-fidelity))
- [High-Fidelity Office DDE Contextual Anomaly](#high-fidelity-office-dde-contextual-anomaly)
- [High-Fidelity Hypervisor API and VM Escape Research](#high-fidelity-hypervisor-api-and-vm-escape-research)
- [Adatok gyanús archiválása exfiltráció céljából](#adatok-gyanús-archiválása-exfiltráció-céljából)
- [Biztonsági szolgáltatások gyanús leállítása](#biztonsági-szolgáltatások-gyanús-leállítása)
- [Windows Defender védelem kikapcsolása vagy módosítása PowerShell segítségével](#windows-defender-védelem-kikapcsolása-vagy-módosítása-powershell-segítségével)
- [Suspicious Firewall Modification via Netsh.exe](#suspicious-firewall-modification-via-netshexe)
- [Ultra-Pro High-Fidelity Hide Artifacts Detection (T1564)](#ultra-pro-high-fidelity-hide-artifacts-detection-(t1564))
- [Ultra-Pro High-Fidelity Hidden File Attribute Manipulation (T1564.001)](#ultra-pro-high-fidelity-hidden-file-attribute-manipulation-(t1564001))
- [Ultra-Pro High-Fidelity Hidden User Account Creation (T1564.002)](#ultra-pro-high-fidelity-hidden-user-account-creation-(t1564002))
- [Ultra-Pro High-Fidelity Hidden Window Execution (T1564.003)](#ultra-pro-high-fidelity-hidden-window-execution-(t1564003))
- [Ultra-Pro High-Fidelity NTFS Alternative Data Stream (ADS) Abuse (T1564.004)](#ultra-pro-high-fidelity-ntfs-alternative-data-stream-(ads)-abuse-(t1564004))
- [Ultra-Pro High-Fidelity Hidden File System Manipulation (T1564.005)](#ultra-pro-high-fidelity-hidden-file-system-manipulation-(t1564005))
- [Ultra-Pro High-Fidelity Email Hiding Rules Detection (T1564.008)](#ultra-pro-high-fidelity-email-hiding-rules-detection-(t1564008))
- [Ultra-Pro High-Fidelity Virtual Instance Abuse (T1564.011)](#ultra-pro-high-fidelity-virtual-instance-abuse-(t1564011))
- [High-Fidelity Phishing Payload Execution from Communication Apps](#high-fidelity-phishing-payload-execution-from-communication-apps)
- [High-Fidelity Spearphishing Attachment Execution](#high-fidelity-spearphishing-attachment-execution)
- [High-Fidelity Browser-Originating Payload Execution](#high-fidelity-browser-originating-payload-execution)
- [High-Fidelity Process Spawn from Business Communication Service](#high-fidelity-process-spawn-from-business-communication-service)
- [High-Fidelity Detection of Post-Vishing Remote Tool Execution](#high-fidelity-detection-of-post-vishing-remote-tool-execution)
- [High-Fidelity System Service Execution Detection](#high-fidelity-system-service-execution-detection)
- [High-Fidelity Launch Daemon Persistence Detection](#high-fidelity-launch-daemon-persistence-detection)
- [High-Fidelity System Service Execution Detection (T1569.002)](#high-fidelity-system-service-execution-detection-(t1569002))
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
- [Exploit-Grade KernelCallbackTable Manipulation via Remote Memory Write](#exploit-grade-kernelcallbacktable-manipulation-via-remote-memory-write)
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
- [Ultra-Pro Stealthy Debugger Evasion (T1622)](#ultra-pro-stealthy-debugger-evasion-(t1622))
- [High-Fidelity Serverless Function Persistence or Abuse](#high-fidelity-serverless-function-persistence-or-abuse)
- [High-Fidelity Cloud Account Acquisition and Initialization - T1650](#high-fidelity-cloud-account-acquisition-and-initialization---t1650)
- [High-Fidelity Cloud Administration Agent Abuse](#high-fidelity-cloud-administration-agent-abuse)
- [Ultra-Pro Power Settings Manipulation (T1137.001)](#ultra-pro-power-settings-manipulation-(t1137001))
- [Professional Content Impersonation and Infrastructure Mirroring](#professional-content-impersonation-and-infrastructure-mirroring)
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

## Ultra-Pro Stealthy Direct Volume Access (T1006)
- **Azonosító:** `T1006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-fidelity direct volume access by monitoring for raw device paths 
initiated by non-system processes or suspicious parents, often used to bypass 
file system locks and EDR monitoring for credential dumping.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1006`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
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

## High-Fidelity Logon Script Persistence (T1037)
- **Azonosító:** `T1037.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the creation or modification of logon scripts in the registry (UserInitMprLogonScript).
Attackers use this to bypass GPO-based logon scripts and execute malicious code at every logon.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1037`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity UserInitMprLogonScript Persistence
- **Azonosító:** `T1037_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized creation or modification of the UserInitMprLogonScript registry key.
This is a high-fidelity rule because it filters out standard GPO updates and focuses on 
user-writable paths and suspicious execution patterns.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Netsh Helper DLL Persistence
- **Azonosító:** `T1037_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the registration of a new Netsh Helper DLL. 
Attackers use this to maintain persistence by loading a malicious DLL 
whenever netsh.exe or a related networking service starts.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Network Logon Script/Shortcut Modification (T1037.003)
- **Azonosító:** `T1037_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized modification of scripts (.bat, .ps1, .vbs) or shortcuts (.lnk) 
within sensitive network shares like NETLOGON or SYSVOL. 
It specifically filters out legitimate DFS replication and system-level updates.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro RC Script and Init.d Persistence (T1037.004)
- **Azonosító:** `T1037_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized modification of RC scripts, init.d, or systemd generators by non-package manager processes.
Attackers use these to gain root persistence on Linux/macOS systems.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro macOS Startup Items Persistence (T1037.005)
- **Azonosító:** `T1037_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized creation of files in legacy StartupItems directories.
It minimizes false positives by whitelisting the official macOS installer 
subsystem and focusing on unsigned or script-generated persistence.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
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

## High-Fidelity At.exe Activity Detection
- **Azonosító:** `T1053_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the execution of at.exe for task scheduling. Since 'at' is deprecated, 
any interactive use or remote machine targeting (\\) is considered highly suspicious 
and indicative of persistence or lateral movement.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Cron Persistence and In-Place Modification
- **Azonosító:** `T1053_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized creation or modification of cron jobs by monitoring 
direct writes to cron directories and suspicious shell one-liners. 
Filters legitimate package managers and configuration management tools.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

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

## High-Fidelity Systemd Service Creation or Modification
- **Azonosító:** `T1053_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation or modification of systemd service units with a focus on 
anomalous execution paths (e.g., /tmp, /dev/shm) and suspicious parent processes 
(e.g., shells, web servers). Filters out legitimate package management and CM tools.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Systemd Timer Persistence Detection
- **Azonosító:** `T1053_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation or activation of systemd timers used for persistence. 
Focuses on non-standard directory locations (user-level units), interactive shell 
triggers, and suspicious execution payloads (obfuscation, network tools).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002, 007`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy Process Injection Detection (T1055)
- **Azonosító:** `T1055.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects advanced process injection (e.g. DLL injection, Thread Hijacking) by 
monitoring for specific high-risk GrantedAccess masks combined with 
suspicious source-target relationships and unbacked memory regions.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1055`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy DLL Injection (T1055.001)
- **Azonosító:** `T1055_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-fidelity DLL injection by identifying remote thread creation 
where the start address is a known library-loading function or the source 
memory region is not backed by a file on disk (unbacked memory).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy PE Injection (T1055.002)
- **Azonosító:** `T1055_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-fidelity PE injection by identifying cross-process memory 
manipulation where the source of the call is an unbacked memory region 
(shellcode) and the target is a critical system process.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy Thread Hijacking (T1055.003)
- **Azonosító:** `T1055_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects thread execution hijacking by identifying cross-process access 
requests with thread manipulation rights (SET_CONTEXT) where the 
calling stack originates from unbacked memory (shellcode).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy APC Injection (T1055.004)
- **Azonosító:** `T1055_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-fidelity APC injection attempts (including Early Bird) by monitoring for 
specific thread access masks (THREAD_SET_CONTEXT) where the calling code originates 
from unbacked or untrusted memory regions (CallTrace analysis).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy TLS Injection (T1055.005)
- **Azonosító:** `T1055_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-fidelity TLS injection by monitoring for cross-process memory 
manipulation targeting PE headers where the execution flow originates 
from unbacked memory (shellcode).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy Ptrace Injection (T1055.008)
- **Azonosító:** `T1055_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-fidelity ptrace-based process injection by identifying 
PTRACE_POKETEXT/DATA operations from suspicious sources or 
cross-user ptrace attachments, filtering out legitimate debuggers.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `008`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy Module Overwriting (T1055.009)
- **Azonosító:** `T1055_009.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects process or module overwriting by identifying cross-process access 
requests with VM_WRITE permissions where the calling stack originates from 
unbacked memory (shellcode) rather than a signed on-disk module.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `009`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy EWM Injection (T1055.011)
- **Azonosító:** `T1055_011.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects Extra Window Memory (EWM) injection by monitoring for suspicious 
cross-process access with memory manipulation rights where the CallTrace 
indicates execution from unbacked memory (shellcode) targeting GUI processes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `011`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy Process Hollowing (T1055.012)
- **Azonosító:** `T1055_012.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-fidelity process hollowing by identifying cross-process access 
requests with VM_WRITE/VM_OPERATION permissions where the calling stack 
originates from unbacked memory (shellcode) and targets common sacrificial processes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `012`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy Process Hollowing (T1055.013)
- **Azonosító:** `T1055_013.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-fidelity process hollowing by identifying cross-process access 
requests with VM_WRITE/VM_OPERATION permissions where the calling stack 
originates from unbacked memory (shellcode) and targets common sacrificial processes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `013`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy Process Ghosting (T1055.014)
- **Azonosító:** `T1055_014.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects Process Ghosting by identifying process creation events where the 
underlying file is in a 'delete-pending' state, evidenced by missing hashes 
at execution time and originating from non-standard directories.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `014`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy ListPlanting Injection (T1055.015)
- **Azonosító:** `T1055_015.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects ListPlanting injection by identifying suspicious cross-process access 
requests to ListView-capable processes where the execution flow originates 
from unbacked memory regions (shellcode) rather than signed modules.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `015`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
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

## High-Fidelity Scripting Interpreter Contextual Anomaly
- **Azonosító:** `T1059.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious PowerShell or CMD execution by correlating shell interpreters 
with high-risk parent processes (Office, Browsers, Web Servers) and obfuscation techniques.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1059`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
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

## High-Fidelity AppleScript (osascript) Abuse Detection
- **Azonosító:** `T1059_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious osascript execution by monitoring for 'do shell script' escapes, 
base64 encoded payloads, and execution originating from untrusted parent processes 
like browsers or mail clients.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Advanced Windows Command Shell Contextual Anomaly
- **Azonosító:** `T1059_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious cmd.exe execution by correlating risky parent processes 
(Web Servers, Office, SQL) with anomalous command-line patterns like 
command chaining and discovery.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Unix Shell Abuse and Reverse Shell Detection
- **Azonosító:** `T1059_004.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious Unix shell execution by monitoring for command injection 
from web processes, reverse shell socket redirection, and fileless pipe-to-shell patterns.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity VBScript Contextual Anomaly Detection
- **Azonosító:** `T1059_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious VBScript execution by filtering legitimate OS management scripts 
and focusing on risky parent processes, unusual file locations, and 
common obfuscation/download patterns used in malware delivery.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Python Interpreter Abuse Detection
- **Azonosító:** `T1059_006.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious Python execution patterns, focusing on one-liner reverse shells, 
interactive shell upgrades, and execution originating from high-risk network-facing 
parent processes (Web Servers, SQL).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity JScript Interpreter Contextual Anomaly
- **Azonosító:** `T1059_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious JScript execution by correlating wscript/cscript with 
risky parent processes, untrusted file locations, and command-line arguments 
typically used for obfuscation or remote payload retrieval.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `007`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Network Device CLI Manipulation
- **Azonosító:** `T1059_008.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects critical unauthorized configuration changes on network devices, 
focusing on anti-forensics (disabling logs), credential exposure, 
and unauthorized data exfiltration (config export).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `008`

#### 🚨 Response Playbook
1. **IP hírnév:** Ellenőrizd a távoli IP címet hírnév-adatbázisokban.
2. **Forgalom elemzés:** Vizsgáld meg a küldött adatmennyiséget és a protokoll típusát.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Cloud Shell Exploitation and Data Exfiltration
- **Azonosító:** `T1059_009.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized or malicious activities within Cloud Shell environments, 
focusing on identity theft, log suppression, and the conversion of private 
cloud resources to public access.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `009`

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

## High-Fidelity Software Deployment Tool Abuse Detection
- **Azonosító:** `T1072.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the abuse of software deployment agents to execute malicious payloads. 
Focuses on anomalous child processes (PowerShell, BitsAdmin, CertUtil) spawned 
by deployment services, filtering out standard maintenance patterns.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1072`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Anomalous Logon via Valid Account
- **Azonosító:** `T1078.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects successful logons using valid accounts that exhibit anomalous characteristics, 
such as unusual logon types for service accounts or logons followed by immediate 
sensitive command execution.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1078`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Default Account Abuse Detection
- **Azonosító:** `T1078_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects successful logons using well-known default account names (Administrator, Guest, root) 
originating from non-standard network locations or via interactive remote sessions (RDP). 
Filters out common local system noise and internal automation.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Domain Account Lateral Movement Anomaly
- **Azonosító:** `T1078_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects anomalous RDP or Network logons to critical infrastructure (DCs, SQL, File Servers) 
originating from unauthorized source subnets or non-admin user accounts. 
Implements strict filtering for machine accounts and known jump servers.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Local Account Remote Access Detection
- **Azonosító:** `T1078_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects successful remote logons (RDP, SMB, WinRM) using local accounts. 
In a domain environment, local accounts should only be used for local console 
access. Remote usage is a strong indicator of lateral movement or credential theft.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Cloud Account Compromise (Entra ID)
- **Azonosító:** `T1078_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects successful cloud logons that exhibit high-risk indicators: 
MFA bypass on privileged accounts, impossible travel patterns, 
or the use of non-standard automation User-Agents by human accounts.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
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

## High-Fidelity Process Execution from Removable Media
- **Azonosító:** `T1091.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the execution of script interpreters and LOLBins from non-system drives. 
Focuses on patterns used by worms (like Raspberry Robin) and manual USB-based 
attacks while filtering out common portable applications.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1091`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Account Manipulation - Persistence Focused
- **Azonosító:** `T1098.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious and rare modifications to user account attributes that are 
strongly associated with persistence and privilege escalation, such as 
SID History injection, Kerberos Constrained Delegation changes, and 
disabling password expiration for sensitive accounts.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1098`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Entra ID Application Credential Addition
- **Azonosító:** `T1098_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects when a new secret or certificate is added to an Entra ID application.
Attackers use this to establish a backdoor via Service Principals.
This rule filters out common Microsoft first-party apps and known CI/CD service principals.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Exchange Mailbox Permission Grant (T1098.002)
- **Azonosító:** `T1098_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the granting of critical mailbox permissions (FullAccess, SendAs). 
Filters out common service accounts and focuses on cross-tenant or 
unauthorized administrative actions, especially on high-value targets.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Entra ID App Certificate Addition
- **Azonosító:** `T1098_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the addition of a new certificate (public key) to an Entra ID application.
Attackers use this for long-term persistence to act as the application's service principal.
This rule is optimized to filter out automated Microsoft internal rotations and known CI/CD providers.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Azure Role Assignment Escalation
- **Azonosító:** `T1098_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects direct assignment of highly privileged Azure roles (Owner, Contributor, User Access Admin). 
Filters out PIM (Privileged Identity Management) activations and known automation principals 
to reduce noise and focus on manual privilege escalation.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Device Registration Persistence (T1098.005)
- **Azonosító:** `T1098_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious device registrations in Entra ID. Attackers register their own devices 
to bypass Conditional Access policies that require a "registered" device state.
This rule filters out managed enrollments and focuses on unmanaged or scripted registrations.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity MFA Method Addition
- **Azonosító:** `T1098_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects when a new MFA method is added to a user account from a non-trusted location 
or without a fresh MFA challenge. This is a primary persistence technique for attackers 
to maintain access after an initial account compromise.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
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

## High-Fidelity Native API Abuse via LOLBins
- **Azonosító:** `T1106.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the suspicious use of Native API execution through trusted Windows 
binaries (LOLBins). Focuses on scenarios where compilers or system tools 
are abused by untrusted parent processes to perform memory injection.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1106`

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

## High-Fidelity Shared Module Load from Untrusted Path
- **Azonosító:** `T1129.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects trusted system binaries or productivity apps loading DLLs from 
untrusted, world-writable directories. This is a primary indicator of 
DLL Side-Loading or Search Order Hijacking.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1129`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous External Remote Service Access Context
- **Azonosító:** `T1133.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious successful logins via external remote services (RDP/VPN). 
It filters for non-standard source IPs and focuses on high-risk account types 
or technical anomalies in the logon event that are typical for automated 
credential stuffing or lateral movement from external jump boxes.
- **Hamis pozitívok:** Misconfigured internal load balancers showing their own IP or no IP., New VPN ranges not yet added to the 'filter_authorized_gateways' list.
- **MITRE ATT&CK:** `T1133`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Access Token Manipulation & Impersonation (T1134)
- **Azonosító:** `T1134.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-risk access token manipulation by monitoring for suspicious 
Integrity Level transitions and the use of specialized tools that interact 
with LSASS to duplicate or steal security tokens.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1134`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Token Impersonation via LSASS Handle Duplication (T1134.001)
- **Azonosító:** `T1134_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects token theft by monitoring for suspicious handle duplication requests 
targeting LSASS.exe. It filters for known legitimate system processes and 
security agents to ensure high-fidelity alerts.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Create Process with Token (T1134.002)
- **Azonosító:** `T1134_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized process creation using duplicated tokens. 
Monitors for suspicious integrity level transitions from Medium to System 
without standard UAC elevation (Consent.exe) or legitimate service startup.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Make and Impersonate Token (T1134.003)
- **Azonosító:** `T1134_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized creation of security tokens using explicit credentials. 
Monitors for suspicious command line arguments from offensive tools and 
correlates with Logon Type 9 (NewCredentials) anomalies from untrusted parents.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Parent PID Spoofing & Process Tree Violation (T1134.004)
- **Azonosító:** `T1134_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects Parent PID spoofing by identifying violations of the Windows process 
hierarchical model. Specifically targets critical system processes (LSASS, 
Spooler, CSRSS) spawning shells or script interpreters, which is architecturally 
impossible in a healthy environment.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro SID-History Injection & DS Manipulation (T1134.005)
- **Azonosító:** `T1134_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects sIDHistory injection by monitoring Directory Service object changes (Event 5136) 
and correlating them with suspicious RPC calls or unauthorized LSASS access on Domain Controllers.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Unauthorized Account Creation (T1136)
- **Azonosító:** `T1136.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects local or domain account creation by identifying suspicious process lineages 
and command-line patterns while filtering out authorized system and deployment tools.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1136`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Unauthorized Local Account Creation (T1136.001)
- **Azonosító:** `T1136_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects local user account creation by analyzing suspicious process lineages 
and command-line arguments. Filters out automated MDM, GPO, and known installer 
activities to maintain a low false-positive rate.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Unauthorized Domain Account Creation (T1136.002)
- **Azonosító:** `T1136_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects domain account creation by identifying suspicious process lineages and 
non-standard execution environments. Filters out authorized IAM, HR-sync tools, 
and official AD management consoles.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Unauthorized Cloud Account Creation (T1136.003)
- **Azonosító:** `T1136_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects manual cloud account creation by correlating the actor type, 
source IP reputation, and the absence of authorized provisioning service principals.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Office Application Startup Persistence (T1137)
- **Azonosító:** `T1137.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized Office persistence by monitoring Registry modifications
originating from non-standard processes or pointing to suspicious file locations.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1137`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Office Global Template Integrity (T1137.001)
- **Azonosító:** `T1137_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-risk modifications to the Office global template (Normal.dotm) by 
identifying non-Office processes or suspicious file creation patterns in the 
Templates directory.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Office Test DLL Persistence (T1137.002)
- **Azonosító:** `T1137_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the creation or modification of the 'Office Test' Registry key used for 
DLL sideloading persistence. High-fidelity detection filters for non-standard 
paths and unauthorized parent processes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Outlook Custom Forms Persistence (T1137.003)
- **Azonosító:** `T1137_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized Outlook Custom Forms persistence by monitoring 
non-standard Registry modifications and suspicious process spawning 
from Outlook related to form script execution.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Outlook Home Page Hijacking & Bypass (T1137.004)
- **Azonosító:** `T1137_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized modification of Outlook Folder Home Pages and the 
enabling of WebView bypass keys. This technique is used to execute 
arbitrary code when a user clicks on an Outlook folder.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Office Security Policy Tampering (T1137.005)
- **Azonosító:** `T1137_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized weakening of Microsoft Office security policies. 
Focuses on global macro enablement, addition of untrusted network locations, 
and policy modifications originating from non-standard processes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Office Add-in Binary Persistence (T1137.006)
- **Azonosító:** `T1137_006.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized Office Add-in (.wll, .xll) persistence by filtering for 
untrusted file locations, unsigned binaries, and suspicious writing processes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy Deobfuscation/Decoding (T1140)
- **Azonosító:** `T1140.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-fidelity deobfuscation by monitoring native tools (certutil, expand) 
decoding binaries from non-executable extensions (txt, jpg, xml) initiated 
by suspicious parents or targeting sensitive temp directories.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1140`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Browser Extension Force-Install Persistence (T1176)
- **Azonosító:** `T1176.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the creation of 'ExtensionInstallForcelist' or 'ExtensionInstallSources' registry keys.
Attackers use these to force-install malicious extensions that cannot be removed by the user 
and to allow installation from non-official webstores.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1176`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Browser-Originating Shell or System Tool Execution
- **Azonosító:** `T1189.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious child processes spawned by web browsers. This pattern is highly 
indicative of successful exploitation via a Drive-by Compromise (T1189), 
where an exploit kit triggers a payload or a shell directly from the browser's memory.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1189`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

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

## High-Fidelity Supply Chain Compromise Detection (Post-Update Anomaly)
- **Azonosító:** `T1195.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious child processes spawned by legitimate software updaters or signed 
installers. Focuses on discovery and credential access tools that should never be 
part of a standard software maintenance or update cycle.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1195`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Dependency Poisoning Detection
- **Azonosító:** `T1195_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious child processes spawned by package managers or build tools. 
Focuses on reconnaissance and exfiltration activities triggered during library 
installation or compilation (pre/post-install scripts).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Compromised Binary Activity (Post-Update)
- **Azonosító:** `T1195_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious child processes spawned by trusted business applications that 
have been compromised at the binary level. It focuses on the transition from 
legitimate app execution to unauthorized discovery or script execution.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Hardware/Firmware Manipulation Detection
- **Azonosító:** `T1195_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the execution of firmware-flashing tools or low-level hardware access 
utilities in suspicious contexts. This targets potential post-exploitation 
of compromised hardware or attempts to install UEFI rootkits.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

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

## High-Fidelity Trusted Relationship Abuse Detection
- **Azonosító:** `T1199.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious discovery and reconnaissance activities originating from 
trusted ingress points (RDP, Citrix, VPN). It filters out standard administrative 
behavior by focusing on specific parent-child process chains and unusual arguments.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1199`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Malicious Hardware-Induced Command Execution (HID Injection)
- **Azonosító:** `T1200.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious command execution patterns typical for malicious HID devices (Rubber Ducky, Bash Bunny). 
Focuses on rapid shell spawning with "stealth" flags originating from the user session context 
without standard GUI interaction.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1200`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Client-Side Exploitation and Shell Spawning
- **Azonosító:** `T1203.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious child processes spawned by client applications (Office, Browsers, 
PDF Readers). Focuses on shell execution, discovery tools, and LOLBins originating 
from sandboxed or low-integrity application contexts.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1203`

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

## High-Fidelity User Execution of Malicious Link (T1204.001)
- **Azonosító:** `T1204_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious child processes spawned by web browsers, email clients, or 
instant messengers. Focuses on LOLBins and script interpreters launched with 
network-related or obfuscated arguments, indicative of malicious link execution.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity User Execution of Malicious File
- **Azonosító:** `T1204_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious child processes spawned by office productivity apps, 
PDF readers, or archive tools. Specifically targets macro-initiated 
or exploit-driven execution of system tools (LOLBins).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Execution from Mounted Virtual Disk (T1204.003)
- **Azonosító:** `T1204_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious binaries or scripts executing from a virtual disk drive (ISO, VHD, VHDX).
Focuses on LOLBins and script interpreters launched via explorer.exe from non-C: drives,
a common pattern for malware bypassing Mark-of-the-Web.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

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

## Ultra-Pro Traffic Signaling & Port Knocking (T1205)
- **Azonosító:** `T1205.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects attempts to implement or trigger Port Knocking/Traffic Signaling. 
Focuses on the registration of raw packet capturing drivers (Npcap/WinPcap) 
and suspicious firewall rule modifications initiated from untrusted shells.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1205`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Port Knocking & Raw Socket Listener (T1205.001)
- **Azonosító:** `T1205_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized implementation of Port Knocking by monitoring the 
registration of raw packet capturing drivers and suspicious firewall 
modifications (UDP/ICMP/LocalPort Any) initiated from untrusted shells.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Socket Filter & WFP Traffic Signaling (T1205.002)
- **Azonosító:** `T1205_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized registration of network socket filters or WFP callouts. 
Monitors for low-level driver loading and WFP database manipulation from 
untrusted process lineages, a common technique for stealthy port knocking.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity Privilege Escalation Exploitation (T1211)
- **Azonosító:** `T1211.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects potential exploitation for privilege escalation by identifying 
anomalous child processes from vulnerable parents with specific focus on 
breaking out of application sandboxes (browsers, office, pdf).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1211`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
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

## Ultra-Pro High-Fidelity Permissions Modification (T1222)
- **Azonosító:** `T1222.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious file permission modifications by identifying native tools 
(icacls, takeown) used with broad access flags (Full Control, Everyone) 
initiated by non-standard parent processes or from suspicious paths.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001, T1222`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity Windows File Permissions Modification (T1222.001)
- **Azonosító:** `T1222_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects targeted file permission modifications by identifying broad access 
grants (Full Control, Everyone) or inheritance blocking, initiated by 
suspicious/untrusted processes or targeting sensitive directories.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity Linux File Permissions Modification (T1222.002)
- **Azonosító:** `T1222_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects targeted Linux permission tampering by identifying high-risk 
attribute changes (SUID, Immutability) or mass modifications in sensitive 
system paths initiated by non-privileged or web-facing service accounts.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity Execution Guardrails Discovery (T1480)
- **Azonosító:** `T1480.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects targeted execution guardrails by identifying anomalous environment 
discovery patterns initiated by non-privileged users or suspicious parents, 
filtering out common administrative and system noise.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1480`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Environmental Keying Discovery (T1480.001)
- **Azonosító:** `T1480_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects targeted environmental keying by identifying hardware fingerprinting 
and machine-specific registry lookups initiated by suspicious, unbacked, 
or non-standard parent processes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Domain Policy Manipulation & GPO Abuse (T1484)
- **Azonosító:** `T1484.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized modifications to critical Domain Policies by monitoring 
file system writes to the SYSVOL folder and GPO link changes, filtering out 
standard administrative tools (GPMC).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1484`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Group Policy Modification & Abuse (T1484.001)
- **Azonosító:** `T1484_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized GPO modifications by correlating file system writes to critical 
policy templates in SYSVOL with process-level anomalies. Filters out DFSR 
replication and standard GPMC management consoles to minimize false positives.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Domain Trust Tampering & SID Filtering Bypass (T1484.002)
- **Azonosító:** `T1484_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-risk modifications to Domain Trust relationships, focusing on 
the disabling of SID Filtering (Quarantine) and unauthorized trust creation. 
Correlates AD object changes with known administrative context.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

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

## Ultra-Pro Web Shell Execution Patterns (T1505.003)
- **Azonosító:** `T1505.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-confidence indicators of web shell activity by monitoring web server processes 
spawning interactive shells or system reconnaissance tools. Includes strict filtering 
for legitimate .NET compilation and IIS administration.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1505`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro SQL Server Command Shell Execution (T1505.001)
- **Azonosító:** `T1505_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized OS command execution through SQL Server extended stored procedures 
and CLR assemblies. Filters legitimate SQL Agent maintenance while flagging 
suspicious discovery commands and configuration changes (xp_cmdshell, sp_configure).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro IIS Native Module Injection (T1505.002)
- **Azonosító:** `T1505_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the registration or manual injection of IIS modules by monitoring 
appcmd.exe usage, direct applicationHost.config edits, and DLL loads 
from non-standard or user-writable paths.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

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

## Ultra-Pro Mainboard Boot Image & SPI Flash Tampering (T1542.004)
- **Azonosító:** `T1505_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized firmware manipulation by monitoring low-level hardware access 
tools and driver registrations initiated from non-standard process chains. 
Focuses on SPI flash writing and image injection attempts.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Terminal Services DLL Hijacking (T1505.005)
- **Azonosító:** `T1505_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized modification of Terminal Services (RDP) service DLLs 
and providers. Monitors for ServiceDll and ProviderPath tampering from 
untrusted processes and non-standard file paths.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Exploit-Grade Unauthorized Container Image Execution (Implant Container Image)
- **Azonosító:** `T1525.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects execution of container images that are not sourced from approved registries and are executed outside of CI/CD or system namespaces, indicating potential use of implanted container images for persistence or initial access.
- **Hamis pozitívok:** Explicitly approved manual container testing on isolated nodes, Emergency break-glass debugging with documented approval
- **MITRE ATT&CK:** `T1525`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Pre-OS Boot Manipulation (T1542)
- **Azonosító:** `T1542.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized firmware or bootloader modifications. Monitors for 
suspicious mounting of the EFI partition, unauthorized use of firmware 
flashing tools, and UEFI variable manipulation from non-standard parent processes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1542`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro ROM Kit & UEFI Firmware Tampering (T1542.001)
- **Azonosító:** `T1542_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized firmware manipulation by monitoring high-risk driver 
registrations and firmware update utilities initiated from suspicious 
process trees, specifically targeting BYOVD and SPI flash access.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Component Firmware Tampering (T1542.002)
- **Azonosító:** `T1542_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized peripheral firmware (NIC, SSD, GPU) modification by 
identifying stand-alone flashing tools initiated from untrusted process 
chains or non-standard file locations.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Bootkit Persistence & EFI Tampering (T1542.003)
- **Azonosító:** `T1542_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized bootloader modification by monitoring for BCD integrity bypasses, 
manual EFI partition mounting, and suspicious boot path redirection. 
Filters out legitimate OS repairs and BitLocker operations.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Mainboard Boot Image & SPI Flash Tampering (T1542.004)
- **Azonosító:** `T1542_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized firmware manipulation by monitoring low-level hardware access 
tools and driver registrations initiated from non-standard process chains. 
Focuses on SPI flash writing and image injection attempts.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro DHCP/PXE Boot Hijacking (T1542.005)
- **Azonosító:** `T1542_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized modification of DHCP Options 66 (Boot Server) and 67 (Bootfile Name).
Attackers use this to redirect network boot requests to a malicious TFTP server.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

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

## Ultra-Pro macOS Launch Agent Persistence Detection (T1543.001)
- **Azonosító:** `T1543_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized creation of Launch Agents by monitoring suspicious process lineages 
and identifying unsigned or script-based execution targets within the .plist.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Systemd Service Persistence (T1543.002)
- **Azonosító:** `T1543_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized creation or modification of systemd units by monitoring 
suspicious process lineages and unusual executable paths within the service file.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Unauthorized Windows Service Installation (T1543.003)
- **Azonosító:** `T1543_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized Windows service creation by monitoring Event ID 7045 and process creation. 
Focuses on suspicious binary paths, shell-spawned services, and non-standard service executables.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Unauthorized macOS Launch Daemon (T1543.004)
- **Azonosító:** `T1543_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized creation of System Launch Daemons by monitoring file events 
and verifying the integrity of the writing process and the target binary signature.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro WMI Event Subscription Persistence (T1546.003)
- **Azonosító:** `T1546.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized WMI event subscriptions by correlating consumer types with 
suspicious command-line patterns and excluding trusted system orchestrators.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1546, 003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro File Association Hijacking (T1546.001)
- **Azonosító:** `T1546_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized changes to file associations in the Registry by monitoring 
suspicious actor processes and non-standard executable paths in 'shell\open\command'.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Screensaver Persistence Detection (T1546.002)
- **Azonosító:** `T1546_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized screensaver hijacking by monitoring Registry writes to 'SCRNSAVE.EXE'. 
Filters out GPO-driven changes and validates binary extensions and trusted paths.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

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

## Ultra-Pro AppCert DLL Persistence Detection (T1546.004)
- **Azonosító:** `T1546_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized registration of AppCert DLLs by monitoring the Session Manager 
Registry key. It filters out trusted system installers and requires non-standard 
paths or suspicious process lineages to trigger.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Shell Trap Persistence Detection (T1546.005)
- **Azonosító:** `T1546_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized shell trap persistence by monitoring writes to shell profile files 
that include 'trap' commands combined with suspicious network payloads or execution patterns.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Mach-O LC_LOAD_DYLIB Injection (T1546.006)
- **Azonosító:** `T1546_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized modification of Mach-O binaries to inject malicious dylibs. 
Focuses on non-developer tools modifying Application binaries and checks for 
suspicious dylib search paths or unsigned library loads.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Netsh Helper DLL Persistence (T1546.007)
- **Azonosító:** `T1546_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized Netsh Helper DLL registration by monitoring Registry writes 
and command-line arguments. Filters out known-good installers and signed Microsoft binaries.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `007`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro WER SilentProcessExit Persistence (T1546.008)
- **Azonosító:** `T1546_008.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized persistence via Windows Error Reporting (WER) SilentProcessExit. 
Focuses on the registration of 'MonitorProcess' commands which execute when a process 
crashes or exits, excluding known debugging environments.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `008`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro AppInit_DLLs Persistence Detection (T1546.009)
- **Azonosító:** `T1546_009.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized persistence via AppInit_DLLs by monitoring Registry writes 
to the 'AppInit_DLLs' and 'LoadAppInit_DLLs' values. 
Filters out signed Microsoft binaries and trusted system installers.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `009`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro AppCert DLL Persistence Detection (T1546.010)
- **Azonosító:** `T1546_010.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized registration of AppCert DLLs by monitoring the Session Manager 
Registry key. It filters out trusted system installers and requires non-standard 
paths or suspicious process lineages to trigger.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `010`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Application Shimming Persistence Detection (T1546.011)
- **Azonosító:** `T1546_011.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized Shim database installation by monitoring sdbinst.exe 
execution with suspicious source paths and direct Registry writes to InstalledSDB.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `011`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro IFEO Debugger Hijacking Detection (T1546.012)
- **Azonosító:** `T1546_012.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized Debugger injection via Image File Execution Options (IFEO). 
Filters out legitimate developer tools and focuses on high-risk system binaries 
and accessibility features (Sticky Keys, Utility Manager).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `012`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro PowerShell Profile Injection Detection (T1546.013)
- **Azonosító:** `T1546_013.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized automated modification of PowerShell profiles. 
Filters out legitimate manual editing via text editors and focuses on 
programmatic injection from shells or non-standard parent processes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `013`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro WMI Event Subscription Persistence (T1546.014)
- **Azonosító:** `T1546_014.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized WMI event subscriptions by monitoring the creation of 
EventFilters and Command/Script Consumers. Filters out known administrative 
tools and focuses on non-standard scripted execution.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `014`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
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

## Ultra-Pro MSI Installer Custom Action Persistence (T1546.016)
- **Azonosító:** `T1546_016.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious child processes spawned by msiexec.exe originating from non-standard 
directories. This targets malicious MSI Custom Actions used for persistence or privilege escalation.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `016`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Gyanús rendszerindítási vagy bejelentkezési automatikus indítás végrehajtása
- **Azonosító:** `T1547.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Észleli a gyanús beállításjegyzékbeli vagy indítómappák módosításait, amelyeket az adatok megőrzése érdekében használnak, a nem szabványos elérési utakra és a gyanús végrehajtókra összpontosítva.
- **Hamis pozitívok:** Szoftverfrissítők, amelyek ideiglenes mappából futtatnak telepítőt a következő bejelentkezéskor., Egyedi vállalati scriptek a Startup mappában.
- **MITRE ATT&CK:** `T1547, 001`

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

## High-Fidelity LSA Authentication Package Persistence
- **Azonosító:** `T1547_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the addition of unauthorized Authentication Packages in the LSA registry key.
Attackers use this for SYSTEM-level persistence and credential harvesting.
This rule filters standard Windows packages and monitors for DLLs outside System32.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Time Provider Persistence (T1547.003)
- **Azonosító:** `T1547_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the registration of a new Windows Time Provider. 
Attackers use this for SYSTEM-level persistence by loading a malicious DLL into svchost.exe.
This rule filters standard Windows DLLs and targets non-System32 paths.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Winlogon Helper DLL Persistence (T1547.004)
- **Azonosító:** `T1547_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized modifications to Winlogon helper keys (Userinit, Shell). 
Focuses on 'appending' multiple executables or using non-standard system paths.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity SSP DLL Persistence (T1547.005)
- **Azonosító:** `T1547_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the addition of unauthorized DLLs to the LSA Security Packages registry key.
Attackers use this for persistence and cleartext credential theft.
Filters standard Windows SSPs and alerts on unmanaged modifications.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Kernel Driver Registration (T1547.006)
- **Azonosító:** `T1547_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the registration of a new kernel-mode driver service.
Attackers use this for rootkit-level persistence and to disable security tools.
Optimized to flag drivers in non-standard paths and suspicious manual service creation.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Browser Session Persistence (T1547.007)
- **Azonosító:** `T1547_007.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized modification of browser session or preference files by non-browser processes. 
Attackers use this to force browsers to open malicious URLs upon startup for persistence.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `007`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity LSASS Driver/Package Persistence (T1547.008)
- **Azonosító:** `T1547_008.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the registration of new LSA plugins, notification packages, or drivers. 
Attackers use this to load malicious code into the lsass.exe process for 
persistence and real-time credential harvesting.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `008`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Shortcut Modification Detection
- **Azonosító:** `T1547_009.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation or modification of LNK files by suspicious processes (PowerShell, CMD, etc.)
in startup folders or taskbar paths. This is a common technique for persistence.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `009`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity AppCert DLL Persistence (T1547.010)
- **Azonosító:** `T1547_010.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized registration of AppCert DLLs. These DLLs are loaded into 
every process that calls CreateProcess, making it a powerful persistence and injection vector.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `010`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Application Shimming Persistence (T1547.011)
- **Azonosító:** `T1547_011.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the installation of a new Shim database (.sdb) using sdbinst.exe.
Attackers use shims to inject DLLs, bypass security controls, or maintain persistence.
This rule filters legit installers and flags suspicious parent-child relationships.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `011`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity COM Hijacking Persistence (T1547.012)
- **Azonosító:** `T1547_012.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation of COM object handlers in HKCU that point to suspicious locations.
Focuses on InprocServer32 and LocalServer32 keys, which are primary targets for hijacking.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `012`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Email Client Helper Persistence (T1547.013)
- **Azonosító:** `T1547_013.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the registration of unauthorized email client helpers or COM add-ins.
Focuses on DLLs registered from user-writable paths and suspicious registry writers.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `013`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Active Setup Persistence (T1547.014)
- **Azonosító:** `T1547_014.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the creation or modification of Active Setup 'StubPath' registry keys by non-system processes.
Attackers use this to achieve persistence that executes once per user upon logon.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `014`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity COM Hijacking Persistence (T1547.015)
- **Azonosító:** `T1547_015.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation of COM object handlers in HKCU that point to suspicious, 
user-writable locations. Attackers hijack CLSIDs to achieve stealthy persistence 
within legitimate system processes like explorer.exe.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `015`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Privilege Escalation via Registry Hijacking (T1548.002)
- **Azonosító:** `T1548.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects UAC bypass attempts by monitoring unauthorized Registry modifications 
to shell open commands. Specifically filters for trusted installers and 
system-initiated changes to minimize false positives.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1548, 002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Setuid/Setgid Bit Manipulation (T1548.001)
- **Azonosító:** `T1548_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized SUID/SGID bit escalation by monitoring chmod/chown 
execution in world-writable directories and suspicious reconnaissance 
patterns, while filtering out legitimate package managers.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
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

## Ultra-Pro Sudoers Manipulation and Sudo Abuse (T1548.003)
- **Azonosító:** `T1548_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized sudoers file modifications and sudo caching abuse. 
Focuses on NOPASSWD additions, timestamp_timeout manipulation, and 
dangerous environment variable injections like LD_PRELOAD.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro AppleScript Privilege Escalation (T1548.004)
- **Azonosító:** `T1548_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized AppleScript elevation attempts. Specifically monitors 
osascript execution with "administrator privileges" from untrusted parent 
processes such as browsers, office suites, or temporary directories.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro SUID Desktop Entry & Shortcut Abuse (T1548.005)
- **Azonosító:** `T1548_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized modification of XDG desktop entries or shortcuts that attempt 
to execute SUID binaries or leverage pkexec for privilege escalation. 
Focuses on modifications in user-writable directories by untrusted processes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Client Binary Integrity Compromise (T1554)
- **Azonosító:** `T1554.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the modification or replacement of trusted client binaries by unauthorized processes. 
Focuses on cases where the writing process is a LOLBin or the file lacks a valid vendor signature.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1554`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
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

## Exploit-Grade Authentication Process Hijack via Suspicious DLL Registration
- **Azonosító:** `T1556.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects exploitation-grade modification of the Windows authentication process where a non-system process registers a new authentication-related DLL from a user-writable directory into LSA, SSP, or Credential Provider registry locations, strongly indicating credential interception.
- **Hamis pozitívok:** Extremely rare, explicitly approved third-party authentication extensions, Legacy SSO components with insecure installation practices (should be allowlisted)
- **MITRE ATT&CK:** `T1556`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Exploit-Grade Security Support Provider Hijacking (LSA SSP)
- **Azonosító:** `T1556_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects exploitation-grade Security Support Provider (SSP) hijacking by identifying unauthorized modification of the LSA Security Packages registry value to register a new, non-system DLL from a user-writable directory by a non-trusted process or account.
- **Hamis pozitívok:** Extremely rare, explicitly approved third-party SSP deployments, Legacy authentication extensions with insecure installers (should be allowlisted)
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Exploit-Grade Password Filter DLL Hijacking via LSA Notification Packages
- **Azonosító:** `T1556_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects exploitation-grade installation of a malicious Password Filter DLL by identifying unauthorized modification of the LSA Notification Packages registry value to add a new DLL located in a user-writable directory by a non-trusted process or account. This behavior strongly indicates credential interception on Domain Controllers.
- **Hamis pozitívok:** Explicitly approved custom password policy extensions (should be extremely rare and allowlisted), Controlled red team or malware research environments
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro PAM Integrity Hijacking & Backdoor (T1556.003)
- **Azonosító:** `T1556_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized modification of PAM configuration or binary modules 
by identifying non-package-manager writes to /etc/pam.d/ and /lib/security/.
Specifically filters for automated configuration tools to reduce false positives.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Network Device Authentication Hijacking (T1556.004)
- **Azonosító:** `T1556_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized modifications to AAA (Authentication, Authorization, and Accounting) 
settings or local user databases on network devices. Focuses on manual bypasses 
performed outside of authorized management subnets.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **IP hírnév:** Ellenőrizd a távoli IP címet hírnév-adatbázisokban.
2. **Forgalom elemzés:** Vizsgáld meg a küldött adatmennyiséget és a protokoll típusát.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro SID History Injection Correlation (T1556.005)
- **Azonosító:** `T1556_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the injection of highly privileged SIDs into the sIDHistory attribute of a user. 
This targets the "Ghost Admin" scenario where a user gains Domain Admin rights 
without being a member of the group.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Entra ID MFA Method Hijacking (T1556.006)
- **Azonosító:** `T1556_006.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-risk modifications to MFA methods in Entra ID by correlating 
successful method changes with suspicious entry points or administrative anomalies.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Hybrid Identity Sync Manipulation (T1556.007)
- **Azonosító:** `T1556_007.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized manipulation of the Entra ID (formerly Azure AD) Connect sync process.
Focuses on MSOL account abuse from non-sync servers and unauthorized ADSync PowerShell usage.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `007`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Network-to-Cloud Auth Hijacking (T1556.008)
- **Azonosító:** `T1556_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-risk modifications to Enterprise Applications and Conditional Access 
policies used by network devices (VPNs, Firewalls). Focuses on MFA bypasses 
and unauthorized credential additions to service principals.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `008`

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

## High-Fidelity Indirect IPC and COM Execution
- **Azonosító:** `T1559.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious indirect process creation via COM/DDE/WMI. 
Focuses on 'orphan' processes where an Office app or browser triggers 
a system proxy to execute code, bypassing standard parent-child monitoring.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1559, 001, 002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
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

## High-Fidelity Office DDE Contextual Anomaly
- **Azonosító:** `T1559_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious process spawning via Microsoft Office Dynamic Data Exchange (DDE). 
Filters legitimate financial data links (Excel) and focuses on Office apps launching 
interpreters or LOLBins with DDE-specific command-line markers.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Hypervisor API and VM Escape Research
- **Azonosító:** `T1559_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized interaction with hypervisor APIs and diagnostic tools. 
Focuses on manual execution from interactive shells and suspicious command-line 
parameters associated with VM escape or sandbox evasion.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
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

## Ultra-Pro High-Fidelity Hide Artifacts Detection (T1564)
- **Azonosító:** `T1564.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects targeted artifact hiding techniques including NTFS Alternative Data Streams (ADS), 
registry-based user account hiding, and suspicious file attribute manipulation 
initiated by untrusted parents.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1564, 001, 002, 004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity Hidden File Attribute Manipulation (T1564.001)
- **Azonosító:** `T1564_001.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects targeted file and directory hiding by identifying the combined use of 
System (+s) and Hidden (+h) attributes initiated by untrusted parent processes 
or targeting sensitive user-writable directories.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity Hidden User Account Creation (T1564.002)
- **Azonosító:** `T1564_002.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the hiding of user accounts from the Windows logon screen by targeting 
the 'SpecialAccounts\UserList' registry key. Filters out legitimate system 
installers and focuses on suspicious parent processes and non-system users.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity Hidden Window Execution (T1564.003)
- **Azonosító:** `T1564_003.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious process execution with hidden windows by correlating 
abbreviated stealth flags with untrusted parent processes and 
obfuscation techniques.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity NTFS Alternative Data Stream (ADS) Abuse (T1564.004)
- **Azonosító:** `T1564_004.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation or execution of malicious NTFS Alternative Data Streams (ADS). 
Correlates redirection operators and LOLBins with stream-specific command-line 
syntax to minimize false positives from drive letters and MOTW.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity Hidden File System Manipulation (T1564.005)
- **Azonosító:** `T1564_005.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious mounting or creation of virtual disk images (VHD, VHDX, ISO) 
initiated by untrusted parent processes or targeting non-standard paths, 
often used to bypass MOTW or hide malicious payloads.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity Email Hiding Rules Detection (T1564.008)
- **Azonosító:** `T1564_008.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects targeted email hiding rules by identifying suspicious inbox rule 
modifications that automate the deletion or hiding of security alerts, 
initiated by untrusted parent processes or non-admin shells.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `008`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro High-Fidelity Virtual Instance Abuse (T1564.011)
- **Azonosító:** `T1564_011.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious use of Windows Sandbox and WSL to evade EDR monitoring. 
Focuses on untrusted parent processes, non-standard configuration loading, 
and direct command execution within virtual instances.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `011`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Phishing Payload Execution from Communication Apps
- **Azonosító:** `T1566.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious child processes spawned by email clients, browsers, or chat apps 
where the payload originates from a user-writable directory. This pattern is 
highly characteristic of spearphishing (T1566.001/.002).
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1566`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Spearphishing Attachment Execution
- **Azonosító:** `T1566_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects highly suspicious child processes spawned from email clients or Office applications. 
It specifically targets script interpreters and dual-use binaries (LOLBins) that 
originate from user-writable directories, significantly reducing false positives 
from legitimate system updates and standard GUI behavior.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Browser-Originating Payload Execution
- **Azonosító:** `T1566_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects suspicious child processes spawned by web browsers where the command line 
references user-writable or temporary directories. This pattern is highly 
indicative of a successful spearphishing link attack leading to immediate execution.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Process Spawn from Business Communication Service
- **Azonosító:** `T1566_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects highly suspicious child processes spawned by business communication tools 
(Teams, Slack, Discord, LinkedIn). It specifically targets script interpreters 
and dual-use binaries (LOLBins) executing from user-writable directories, 
effectively filtering out legitimate application updates and browser launches.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Detection of Post-Vishing Remote Tool Execution
- **Azonosító:** `T1566_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the execution of unauthorized remote access tools (AnyDesk, TeamViewer, etc.) 
specifically when run from user-writable directories (Downloads, Temp). 
This pattern is a high-confidence indicator of a successful vishing attack where 
the victim is instructed to run "support" software.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity System Service Execution Detection
- **Azonosító:** `T1569.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation or execution of system services with suspicious characteristics, 
such as binaries located in world-writable directories or services used as 
wrappers for shell commands. Optimized to filter out legitimate software installers.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1569, 002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Launch Daemon Persistence Detection
- **Azonosító:** `T1569_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the creation or modification of Launch Daemons by monitoring 
untrusted parent processes and suspicious command-line strings. 
Optimized to filter out Apple and common third-party installers.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity System Service Execution Detection (T1569.002)
- **Azonosító:** `T1569_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious service execution or modification by monitoring anomalous 
parent processes, world-writable binary paths, and shell command wrappers. 
Optimized for low false positive rates in enterprise environments.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro DLL Hijacking & Side-Loading Detection (T1574)
- **Azonosító:** `T1574.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects potential DLL hijacking or side-loading by monitoring trusted system 
binaries loading DLLs from non-standard, user-writable directories, while 
filtering out legitimate signed modules and known application behaviors.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1574, 001, 002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro DLL Search Order Hijacking Detection (T1574.001)
- **Azonosító:** `T1574_001.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects trusted Windows system binaries loading DLLs from non-standard, 
potentially user-writable directories. It filters out validly signed 
third-party modules to reduce false positives.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro DLL Side-Loading Integrity Gap Detection (T1574.002)
- **Azonosító:** `T1574_002.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects potential DLL side-loading by identifying cases where a signed, 
trusted executable loads an unsigned or suspiciously-located DLL from 
user-writable directories.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Shell Configuration & Path Interception (T1574.003)
- **Azonosító:** `T1574_003.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized modification of PATH environment variables or shell autorun 
registry keys. Focuses on "Path Prepending" (placing malicious paths at the 
beginning) and non-standard shell startup commands.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Library Search Order Hijacking & Integrity Gap (T1574.004)
- **Azonosító:** `T1574_004.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects potential library hijacking by monitoring trusted system binaries 
loading unsigned or suspiciously-located DLLs from user-writable directories, 
specifically looking for trust mismatches between the EXE and the DLL.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Installer File Permissions Weakness (T1574.005)
- **Azonosító:** `T1574_005.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-privilege execution of binaries from user-writable locations. 
This targets scenarios where an attacker replaces a legitimate installer 
with a malicious one due to insecure directory permissions.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Dynamic Linker Hijacking Against Privileged Binary
- **Azonosító:** `T1574_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects Dynamic Linker Hijacking by identifying execution of privileged or SetUID Linux binaries with manipulated dynamic linker environment variables pointing to user-writable shared libraries.
- **Hamis pozitívok:** Extremely rare custom hardened environments, Manual exploitation labs or red team activity
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## PATH Hijacking Leading to Privileged Binary Execution
- **Azonosító:** `T1574_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects PATH environment variable hijacking where a privileged Linux binary is executed with a user-writable directory at the beginning of PATH, and a non-absolute command is resolved, indicating a viable path interception attack chain.
- **Hamis pozitívok:** Extremely rare misconfigured automation running privileged tools, Controlled red team or security testing activity
- **MITRE ATT&CK:** `007`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## .NET Assembly Search Order Hijacking via User-Writable Directory
- **Azonosító:** `T1574_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects potential .NET Assembly Search Order Hijacking where a legitimate .NET runtime host loads a managed assembly from a user-writable directory outside of the GAC, Microsoft.NET framework paths, or the application installation directory.
- **Hamis pozitívok:** Extremely rare legacy .NET applications with local assembly loading, Explicitly misconfigured enterprise applications
- **MITRE ATT&CK:** `008`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## .NET AppDomainManager Hijacking via Non-GAC Assembly
- **Azonosító:** `T1574_009.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects .NET AppDomainManager hijacking by identifying .NET runtime hosts that load a managed assembly from a user-writable directory at process initialization, outside of the GAC and Microsoft .NET framework paths. This behavior is highly indicative of malicious AppDomainManager abuse.
- **Hamis pozitívok:** Almost non-existent in production environments, Highly specialized .NET research or red team activity
- **MITRE ATT&CK:** `009`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Privileged Service Executable Overwritten from User-Writable Location
- **Azonosító:** `T1574_010.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects exploitation of weak service file permissions where a registered Windows service executable running with high privileges is overwritten or modified from a user-writable directory by a non-system process.
- **Hamis pozitívok:** Extremely rare legacy third-party services installed in unsafe paths, Misconfigured enterprise software with self-updating service binaries
- **MITRE ATT&CK:** `010`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Privileged Service ImagePath or ServiceDll Hijacked via Registry
- **Azonosító:** `T1574_011.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects exploitation of weak Windows service registry permissions where a non-system process modifies critical service registry values to point to an executable or DLL located in a user-writable directory, enabling privilege escalation upon service start or restart.
- **Hamis pozitívok:** Extremely rare legacy software with insecure service update mechanisms, Intentionally vulnerable lab or red team environments
- **MITRE ATT&CK:** `011`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Exploit-Grade COR_PROFILER Hijacking via User-Writable Profiler DLL
- **Azonosító:** `T1574_012.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects exploitation of COR_PROFILER hijacking where a .NET runtime host is executed with profiling enabled and a custom profiler DLL specified from a user-writable directory, excluding legitimate Microsoft, Visual Studio, and APM profiling use cases.
- **Hamis pozitívok:** Extremely rare, explicitly approved .NET profiling on production systems, Controlled red team or malware research environments
- **MITRE ATT&CK:** `012`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Exploit-Grade KernelCallbackTable Manipulation via Remote Memory Write
- **Azonosító:** `T1574_013.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects remote memory write operations into GUI processes which are prerequisites 
for KernelCallbackTable hijacking. This technique is often used for process 
injection that evades standard hook-based monitoring.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `013`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
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

## High-Fidelity VPS Infrastructure Provisioning - T1583.001
- **Azonosító:** `T1583_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the automated acquisition of VPS infrastructure (DigitalOcean, AWS, Azure, GCP).  Focuses on the provisioning phase (VM creation) while isolating authorized DevOps  pipelines and interactive developer workflows.
- **Hamis pozitívok:** Authorized cloud engineers performing manual infrastructure updates., Development teams testing IaC scripts in non-standard local environments., Automated cloud-monitoring tools that trigger resource updates.
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Automated Domain Registration & Acquisition - T1583.002
- **Azonosító:** `T1583_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated domain registration through registrar APIs and specialized  provisioning tools. Focuses on programmatic acquisition via curl/python  while filtering out authorized IT infrastructure management (Certbot, Terraform).
- **Hamis pozitívok:** Automated domain renewals by IT department., SEO teams using auditing tools for brand protection., Security team performing authorized domain-squatting research.
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Cloud Network (VPC) Provisioning - T1583.003
- **Azonosító:** `T1583_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the acquisition and configuration of cloud networking (VPC).  Focuses on identifying the creation of internet egress points and  cross-network bridges from unauthorized endpoints, isolating automated  CI/CD pipelines from manual or scripted local abuse.
- **Hamis pozitívok:** Authorized network architects deploying new staging VPCs., Automated disaster recovery scripts rebuilding network stacks.
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Serverless Infrastructure Provisioning - T1583.004
- **Azonosító:** `T1583_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the automated acquisition and provisioning of serverless infrastructure  (AWS Lambda, Azure Functions, GCP Functions). Focuses on CLI-based creation  and critical configuration changes while isolating authorized CI/CD pipelines  and interactive developer IDE contexts.
- **Hamis pozitívok:** Authorized developers performing manual serverless deployments for debugging., Automated maintenance scripts that rotate function secrets or update env vars.
- **MITRE ATT&CK:** `004`

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

## High-Fidelity Web Service Acquisition and Provisioning - T1583.006
- **Azonosító:** `T1583_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the acquisition and setup of web services (SaaS, Storage, Messaging)  for offensive infrastructure. Focuses on command-line based storage provisioning  (Rclone, AzCopy) and messaging API initialization (Slack/Discord/Telegram bots)  from non-administrative or non-developer endpoints.
- **Hamis pozitívok:** IT administrators performing one-time data migrations via Rclone., Developers testing messaging API integrations in local terminals., Marketing scripts uploading assets to cloud storage buckets.
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Serverless Infrastructure Provisioning - T1583.007
- **Azonosító:** `T1583_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the automated acquisition and provisioning of serverless infrastructure  (AWS Lambda, Azure Functions, GCP Functions). Focuses on CLI-based creation  and critical configuration changes while isolating authorized CI/CD pipelines  and interactive developer IDE contexts.
- **Hamis pozitívok:** Authorized developers performing manual serverless deployments for debugging., Automated maintenance scripts that rotate function secrets or update env vars.
- **MITRE ATT&CK:** `007`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Cloud Account Acquisition and Bootstrap - T1583.008
- **Azonosító:** `T1583_008.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the acquisition and initial configuration of cloud accounts.  Targets account-level bootstrapping (credential setup, IAM user creation)  and automated identity harvesting from non-standard processes,  while filtering out authorized DevOps pipelines.
- **Hamis pozitívok:** Cloud engineers configuring their local environment for the first time., Development teams debugging cloud integration locally in authorized IDEs., Legitimate automated billing or auditing scripts run outside of CI/CD.
- **MITRE ATT&CK:** `008`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Compromised Infrastructure and Resource Abuse - T1584
- **Azonosító:** `T1584.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects indicators of compromised infrastructure, specifically focusing on  web server process subversion (Web Shells), unauthorized reverse proxies,  and tunneling tools executed from non-standard administrative contexts.
- **Hamis pozitívok:** Penetration testing or Red Team exercises., Developers using Chisel/Ngrok for authorized remote debugging., Complex web applications that legitimately call system commands (rare, check app logic).
- **MITRE ATT&CK:** `T1584`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Domain Infrastructure Hijacking - T1584.001
- **Azonosító:** `T1584_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized domain or subdomain hijacking by monitoring for  critical DNS record types (NS, SOA) and mass record creation via  Cloud Provider CLIs, while filtering for authorized DevOps automation.
- **Hamis pozitívok:** Authorized network engineers performing bulk DNS migrations., Automated cloud-native services updating DNS (e.g., ExternalDNS in Kubernetes)., Marketing automation creating new subdomains via authorized CLI.
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity DNS Server Configuration Subversion - T1584.002
- **Azonosító:** `T1584_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized DNS infrastructure manipulation by monitoring for  critical configuration changes (zone resets, master updates) and  suspicious child processes spawned directly from DNS services.
- **Hamis pozitívok:** Authorized IPAM software performing DNS zone synchronization., Emergency manual DNS recovery by authorized senior administrators., Vulnerability scanners probing the DNS service (e.g., Nessus).
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Cloud Identity Subversion and Persistence - T1584.003
- **Azonosító:** `T1584_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized cloud account manipulation by monitoring for  high-risk identity changes (MFA removal, new access keys) executed  outside of authorized CI/CD pipelines or known administrative jump-hosts.
- **Hamis pozitívok:** Emergency manual MFA reset by a Cloud Architect from an authorized jump-host., Legitimate identity migration scripts during tenant consolidation., Security audits using authorized scanning accounts.
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Serverless Function Subversion - T1584.004
- **Azonosító:** `T1584_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized modification of serverless functions (Lambda, Azure Functions, GCP) by focusing on high-risk parameters like layer injection and environment variable manipulation, while strictly filtering for authorized CI/CD pipeline service accounts.
- **Hamis pozitívok:** Emergency manual hotfix by a senior Cloud Architect from a jump-server., Authorized security testing/red teaming focusing on FaaS., Initial setup of serverless infrastructure before CI/CD is established.
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Botnet Agent Persistence and Control - T1584.005
- **Azonosító:** `T1584_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects botnet agent activity by identifying suspicious process lineages  (e.g., LOLBins spawning from WMI), P2P bootstrap arguments, and known  DDoS tool patterns while filtering authorized IT management and P2P software.
- **Hamis pozitívok:** Legitimate P2P-based software distribution (e.g., BranchCache, Delivery Optimization)., IT admins using WMI for authorized mass-configuration changes., Performance monitoring tools using Stratum-like protocols.
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Web Service and Cloud Storage Subversion - T1584.006
- **Azonosító:** `T1584_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized manipulation of web services and cloud storage by  monitoring for ACL changes (making buckets public), suspicious file types  being hosted (scripts/exes), and the use of third-party data transfer  tools (rclone) outside of authorized contexts.
- **Hamis pozitívok:** Authorized developers updating static website assets (e.g., .js or .css files)., IT admins using rclone for one-time authorized data migration., Automated report generation uploading zip files to internal storage buckets.
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity VPS Control and Tunneling - T1584.007
- **Azonosító:** `T1584_007.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized VPS manipulation by identifying critical lifecycle changes  (SSH key injection, firewall opening) and the execution of reverse tunneling tools  from non-authorized administrative contexts.
- **Hamis pozitívok:** Cloud engineers performing emergency manual network troubleshooting., Legitimate automated scaling scripts not yet in the service account whitelist., Authorized Red Team exercises.
- **MITRE ATT&CK:** `007`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Suspicious User Account Creation via CLI/Scripting
- **Azonosító:** `T1585.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation of new user accounts (T1585) when initiated from 
suspicious processes like CMD, PowerShell, or net.exe, rather than 
standard Administrative consoles (ADUC, Windows Admin Center).
- **Hamis pozitívok:** Automated provisioning scripts (adjust filters for your specific SVC accounts), Legacy batch scripts used by sysadmins for bulk user creation
- **MITRE ATT&CK:** `T1585`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Potential Automated Social Media Account Establishment
- **Azonosító:** `T1585_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious patterns of social media account registration by monitoring 
access to multiple sign-up endpoints from a single host or identifying 
non-browser processes making requests to these domains.
- **Hamis pozitívok:** Marketing automatizációs szoftverek (pl. HubSpot, Buffer), ha helyileg futnak, Fejlesztők, akik API-kat tesztelnek (érdemes a forrás IP-t szűrni)
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **IP hírnév:** Ellenőrizd a távoli IP címet hírnév-adatbázisokban.
2. **Forgalom elemzés:** Vizsgáld meg a küldött adatmennyiséget és a protokoll típusát.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Stealthy Email Account Establishment and Manipulation
- **Azonosító:** `T1585_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation of email accounts followed by immediate sensitive 
permission changes or forwarding rules. Focuses on CLI-based execution 
to reduce noise from standard HR-driven GUI processes.
- **Hamis pozitívok:** IT migrations where mailbox forwarding is part of the decommissioning process., Security-approved automated backup or journaling accounts.
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous Cloud User Account Creation
- **Azonosító:** `T1585_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation of cloud accounts via command-line tools or service principals, 
excluding authorized synchronization accounts and automated HR provisioning systems.
- **Hamis pozitívok:** DevOps mérnökök, akik CLI-ből automatizálnak (őket érdemes fix IP vagy user alapján szűrni), Újonnan bevezetett felhő-menedzsment eszközök
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Account Compromise and Identity Manipulation - T1586
- **Azonosító:** `T1586.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects actions indicative of account compromise and takeover (ATO), such as  unauthorized MFA modification, suspicious login profile updates, and automated  credential testing from non-standard administrative processes.
- **Hamis pozitívok:** Authorized Red Team exercises or internal penetration testing., Emergency account recovery by senior IT staff via CLI., Automated identity lifecycle management scripts (if not using the service account).
- **MITRE ATT&CK:** `T1586`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Automated Social Media Manipulation - T1586.001
- **Azonosító:** `T1586_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects automated interaction with social media platforms via headless browser  frameworks (Selenium, Puppeteer, Playwright). Attackers use these to scale  account takeover (ATO) and bypass security controls by injecting stolen cookies.
- **Hamis pozitívok:** Frontend developers running automated UI tests for internal apps., Marketing automation tools used for scheduled posts on authorized machines.
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Email Forwarding Rule Manipulation - T1586.002
- **Azonosító:** `T1586_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation or modification of email forwarding/redirection rules via  command-line tools (PowerShell, Microsoft Graph CLI). This is a high-confidence  indicator of Account Takeover (ATO) where an attacker attempts to exfiltrate  sensitive emails (invoices, password resets) without user interaction.
- **Hamis pozitívok:** IT administrators using PowerShell for bulk mailbox migration or cleanup., Power users who prefer managing their mailbox via scripts rather than the GUI.
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Cloud Account Takeover and Persistence - T1586.003
- **Azonosító:** `T1586_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized cloud account manipulation focusing on identity takeover  and persistence. Targets the creation of new cloud credentials, MFA removal,  and login profile updates from non-authorized processes, specifically filtering  out known administrative and developer workflows.
- **Hamis pozitívok:** Authorized identity admins performing manual emergency recovery., Legitimate automated IAM cleanup or key rotation scripts., Developers debugging identity-related logic in authorized local environments.
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Offensive Capability Development and Compilation - T1587
- **Azonosító:** `T1587.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the development and compilation of offensive tools by monitoring  for specific C2 framework build arguments, unauthorized use of code packers,  and certificate manipulation outside of verified CI/CD pipelines.
- **Hamis pozitívok:** Legitimate developers working on obfuscated internal tools., Software installation processes that compile components on the fly (e.g., .NET optimization)., Security analysts performing authorized research in lab environments.
- **MITRE ATT&CK:** `T1587`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Malware Development and Evasion Patterns - T1587.001
- **Azonosító:** `T1587_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects custom malware development by identifying suspicious compiler execution  combined with evasion-related API strings, anti-analysis techniques,  and unauthorized build locations.
- **Hamis pozitívok:** Security analysts developing internal testing tools., Legitimate installers that compile code during setup (e.g., .NET ngen)., Software protection/DRM developers using obfuscation.
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Unauthorized Code Signing Capability Development - T1587.002
- **Azonosító:** `T1587_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the creation of code-signing certificates and the manual signing of binaries  by monitoring for specific OIDs (1.3.6.1.5.5.7.3.3) and signing tools used outside  of verified CI/CD pipelines or Windows SDK paths.
- **Hamis pozitívok:** Authorized developers signing internal drivers or legacy applications., Security tools (e.g., AV/EDR) generating local certificates for inspection., IT admins generating self-signed certs for internal lab testing.
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Unauthorized Digital Certificate Development - T1587.003
- **Azonosító:** `T1587_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized digital certificate and private key generation by monitoring  for high-risk command-line arguments (self-signing, key exfiltration) occurring  in non-standard directories or by unauthorized users.
- **Hamis pozitívok:** Developers testing SSL/TLS logic in local temp folders., Automated deployment scripts (Ansible/Puppet) creating local certs., Third-party software installers generating self-signed certs during setup.
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Exploit Development and Compilation Detection - T1587.004
- **Azonosító:** `T1587_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects indicators of exploit development by monitoring for the compilation of  source code containing memory injection primitives and shellcode-related  arguments, specifically when executed from non-standard or temporary directories.
- **Hamis pozitívok:** Security software (e.g., EDR/AV) components that compile filters on the fly., Legitimate custom .NET applications that use 'unsafe' code for performance., Authorized vulnerability scanning tools that deploy temporary agents.
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous Procurement of Offensive Capabilities
- **Azonosító:** `T1588.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the acquisition of offensive tools by monitoring suspicious combinations 
of download-capable processes and known hacktool signatures or file extensions, 
filtering out legitimate IT software deployment tools.
- **Hamis pozitívok:** Authorized penetration testing activities., Security administrators updating their local toolkits via CLI.
- **MITRE ATT&CK:** `T1588`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous Procurement of Malware Capabilities
- **Azonosító:** `T1588_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the acquisition of malware by monitoring suspicious downloaders (LotL) 
interacting with compressed/container formats or known malware naming patterns 
in non-standard directories.
- **Hamis pozitívok:** IT staff downloading OS images (.iso) via PowerShell scripts (add to exclusion by user)., Developers using CLI tools to download legitimate libraries or VM images.
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous Offensive Tool Acquisition via CLI
- **Azonosító:** `T1588_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the acquisition of offensive tools (hacktools) by monitoring command-line 
downloads targeting non-standard directories. Filters out legitimate IT 
administration from browsers and authorized management agents.
- **Hamis pozitívok:** DevOps mérnökök, akik scriptekkel konfigurálnak munkaállomásokat., IT automatizációs scriptek, amik nem szervizfiókkal futnak.
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous Code Signing Certificate Export or Acquisition
- **Azonosító:** `T1588_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious certificate operations (exporting private keys or forced store additions) 
initiated from unusual parent processes or using plaintext passwords in the command line.
- **Hamis pozitívok:** Automated CI/CD pipelines signing binaries (should be added to filters)., Backup scripts for PKI infrastructure.
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Strategic Trusted Root Certificate Store Manipulation
- **Azonosító:** `T1588_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects unauthorized attempts to modify the Trusted Root Certification Authorities 
store. Attackers do this to facilitate MitM attacks or bypass security warnings. 
Filters out legitimate system-level installers and known security agents.
- **Hamis pozitívok:** Corporate PKI updates via GPO or automated scripts (should be added to filters by thumbprint/user)., Security appliance agents (e.g., Zscaler, Netskope) injecting inspection certs.
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous Procurement of Exploit or PoC Code
- **Azonosító:** `T1588_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the acquisition of exploits or Proof-of-Concept (PoC) code by monitoring 
suspicious download patterns, CLI-based transfers, and known exploit naming 
conventions while filtering out authorized security scanners and developer activity.
- **Hamis pozitívok:** Security researchers or IT staff manually downloading PoCs for patching validation., Automated build systems downloading packages that contain "exploit" in their name as a dependency.
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Targeted Harvesting of Vulnerability Research Artifacts
- **Azonosító:** `T1588_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the systematic acquisition of vulnerability research, audit reports, or 
zero-day PoC documentation. Focuses on CLI-based harvesting in non-technical 
user contexts while filtering out authorized security research.
- **Hamis pozitívok:** IT managers downloading security compliance templates via PowerShell., Automated backup of security documentation shares (if not excluded).
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
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

## Anomalous Infrastructure Staging and Resource Deployment
- **Azonosító:** `T1608.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the use of cloud CLI tools and IaC binaries to stage adversary resources. 
It focuses on non-standard users performing upload or infrastructure modification 
actions, filtering out authorized CI/CD pipelines and IT administration.
- **Hamis pozitívok:** IT staff performing emergency cloud fixes outside of standard CI/CD., Developers using Cloud CLIs on their local machines (should be added to filters if permitted).
- **MITRE ATT&CK:** `T1608`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous Malware Staging to External Infrastructure
- **Azonosító:** `T1608_001.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the staging of malware to external infrastructure by monitoring 
non-browser based uploads to cloud storage, file-sharing, and code-hosting platforms 
using command-line tools or unusual processes.
- **Hamis pozitívok:** Developers manually pushing code to GitHub via CLI (add developer usernames to filters)., IT administrators using rclone for legitimate offsite backups.
- **MITRE ATT&CK:** `001`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous Offensive Tool Staging and External Upload
- **Azonosító:** `T1608_002.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the staging of offensive tools to external infrastructure by monitoring 
CLI-based uploads from non-standard directories. Focuses on the "staged-then-shipped" 
pattern where hacktools are moved to external drop zones.
- **Hamis pozitívok:** IT troubleshooting where an admin uploads a tool log or binary to a vendor., Security researchers testing tools from their own Desktop/Temp folders.
- **MITRE ATT&CK:** `002`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Strategic Digital Certificate Staging in Trusted Root Store
- **Azonosító:** `T1608_003.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the command-line installation of certificates into the Trusted Root store. 
Adversaries do this to establish trust for C2 infrastructure or to enable 
transparent SSL/TLS interception (MitM).
- **Hamis pozitívok:** Manual IT administration via CLI (should be avoided, but happens)., Internal PKI rollouts using custom scripts (filter by specific script path).
- **MITRE ATT&CK:** `003`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous Web Content Modification for Drive-by Staging
- **Azonosító:** `T1608_004.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious modifications to web server content directories (web root) 
initiated by non-standard processes or interactive shells. This behavior is 
typical when an adversary stages a drive-by download site or injects malicious scripts.
- **Hamis pozitívok:** Web developers performing emergency hotfixes via CLI (unrecommended practice)., Legitimate CMS auto-updates (e.g. WordPress, Joomla) - filter by service account.
- **MITRE ATT&CK:** `004`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Strategic Staging of Malicious Link Targets
- **Azonosító:** `T1608_005.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the automated preparation of malicious link targets by monitoring 
CLI-based interactions with URL shortener APIs or cloud-based redirector staging 
initiated by unauthorized users or unusual parent processes.
- **Hamis pozitívok:** Marketing automation scripts that haven't been whitelisted by username., Security teams testing URL shortening for internal phishing simulations.
- **MITRE ATT&CK:** `005`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Anomalous SEO Poisoning and Metadata Staging
- **Azonosító:** `T1608_006.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects the preparation of SEO poisoning infrastructure by monitoring for 
unauthorized CMS manipulation, automated content spinning, and the use of 
known black-hat SEO tools on web servers or staging environments.
- **Hamis pozitívok:** Marketing agencies performing bulk content migrations via CLI., Web developers testing sitemap plugins on dev environments.
- **MITRE ATT&CK:** `006`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Container Interactive Shell Execution
- **Azonosító:** `T1609.yaml`
- **Minőségi mutató:** `80/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized interactive shell access to running containers using 
kubectl or docker exec. Filters legitimate health checks and CI/CD automation 
to focus on manual, high-risk interventions.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1609`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Malicious Container Deployment Detection
- **Azonosító:** `T1610.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects the deployment of containers with high-risk configurations that 
facilitate container escape or persistence. Focuses on privileged mode, 
host-level resource sharing, and non-standard image sources.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1610`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Container Escape & Host Access (T1611)
- **Azonosító:** `T1611.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects unauthorized attempts to bypass container isolation and access the 
underlying host. Targets non-standard privileged executions and high-risk 
volume mounts, while filtering out known cluster infrastructure components.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1611`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy Local Image Build (T1612)
- **Azonosító:** `T1612.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects high-fidelity local container image builds by identifying builds 
initiated by non-CI/CD users or suspicious parent processes like web servers, 
indicating post-exploitation image creation to evade registry scans.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1612`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Stealthy Debugger Evasion (T1622)
- **Azonosító:** `T1622.yaml`
- **Minőségi mutató:** `60/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects high-fidelity debugger evasion by identifying anti-debug API access 
originating from unbacked memory (shellcode) or suspicious temporary paths, 
while filtering out legitimate IDEs and system error reporting.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1622`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## High-Fidelity Serverless Function Persistence or Abuse
- **Azonosító:** `T1648.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects suspicious creation or update of AWS Lambda functions by monitoring 
non-automated activity, unusual source IPs, and risky configurations. 
Focuses on bypassing CI/CD pipelines.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1648`

#### 🚨 Response Playbook
1. **Triage:** Vizsgáld meg a nyers eseményeket a SIEM-ben.
2. **Érintett gép:** Ellenőrizd a host státuszát és a legutóbbi bejelentkezéseket.
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

## High-Fidelity Cloud Administration Agent Abuse
- **Azonosító:** `T1651.yaml`
- **Minőségi mutató:** `70/100` ⭐⭐⭐⭐ (Jó)
- **Kritikusság:** 🔴 (critical)
- **Leírás:** Detects anomalous process execution initiated by cloud management agents (AWS SSM, Azure Guest Agent). 
Attackers use these trusted paths to execute reconnaissance or credential dumping commands 
that bypass traditional network perimeter defenses.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1651`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.
3. **Sürgős:** Ha a gyanú beigazolódik, izoláld az érintett fiókot vagy hostot!

---

## Ultra-Pro Power Settings Manipulation (T1137.001)
- **Azonosító:** `T1653.yaml`
- **Minőségi mutató:** `50/100` ⭐⭐⭐ (Közepes)
- **Kritikusság:** 🟡 (medium)
- **Leírás:** Detects unauthorized power setting modifications aimed at preventing sleep or 
hibernation. Focuses on command-line automation (powercfg) via suspicious 
parent processes like PowerShell or CMD, while filtering legitimate UI-based changes.
- **Hamis pozitívok:** Nincs megadva
- **MITRE ATT&CK:** `T1653`

#### 🚨 Response Playbook
1. **Folyamat vizsgálata:** Ellenőrizd a szülő folyamatot (ParentProcessName) és a parancssort.
2. **Bináris ellenőrzés:** Futtasd le a fájl hash-ét VirusTotal-on.

---

## Professional Content Impersonation and Infrastructure Mirroring
- **Azonosító:** `T1659.yaml`
- **Minőségi mutató:** `90/100` ⭐⭐⭐⭐⭐ (Kiváló)
- **Kritikusság:** 🟠 (high)
- **Leírás:** Detects tools and CLI patterns used to clone or impersonate legitimate web content. 
Focuses on recursive mirroring of internal portals and the use of phishing 
frameworks, filtering out legitimate development and browser-based activity.
- **Hamis pozitívok:** Web developers migrating internal sites using CLI tools., Security teams conducting authorized phishing simulations., Automated documentation generators (e.g., Doxygen, Sphinx) if misconfigured.
- **MITRE ATT&CK:** `T1659`

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

