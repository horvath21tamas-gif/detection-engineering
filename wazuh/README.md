# Sigma → Wazuh

A `dectools-wazuh` a `rules/sigma/` szabályokból Wazuh-szabály XML-t gyárt, teszteli, becsomagolja, és egy
korlátozott SSH-kulccsal, automatikus visszagörgetéssel telepíti a Wazuh managerre.

```
rules/sigma ─► dectools-wazuh build ─► build/wazuh/rules/sigma_*.xml + testvectors.jsonl + report.md
                                    └► dectools-wazuh bundle ─► wazuh-bundle.tar.gz ─ssh─► wazuh-deploy-gate
```

## Mit tud, mit nem

A 628 szabályból **546** fordítható (2427 Wazuh-szabály), **78** nem – ezek okát a `build/wazuh/report.md` sorolja fel:
Linux/macOS process_creation, felhő (Azure/AWS/M365), hálózati eszközök és néhány webszerver-mező nincs leképezve
a `src/dectools/wazuh/mapping.yml`-ben. **Semmi sem esik ki csendben**: ami nem fordítható, az jelentésbe kerül.

Támogatott naplóforrás: Windows Sysmon (EID 1–26), Windows Security/System/Application/PowerShell/Defender/…
csatornák, webszerver access log, Linux auditd (korlátozottan). Új forrás felvétele: `mapping.yml` szerkesztése,
kódot nem kell módosítani.

## A fordítás szabályai

* Egy Wazuh-szabály ÉS-kapcsolatú feltételek halmaza, a VAGY mezők között nem fejezhető ki egyben. Ezért minden
  Sigma feltétel diszjunktív normálformára kerül, **klózonként egy Wazuh-szabály** jön létre (átl. 4,4 / szabály).
  Ugyanazon mező érték-listája (`Image|endswith: [a, b, c]`) egyetlen regex-alternációvá olvad, nem külön szabályokká.
* Minden érték `pcre2` típusú `<field>`, `(?is)` kapcsolóval (a Sigma kis/nagybetű-független, `|cased` esetén nem).
  `contains` → szabad illesztés, `startswith` → `^`, `endswith` → `$`, pontos egyezés → `^…$`. A szóköz `\x20`,
  mert az XML-feldolgozás a szélső szóközöket levágná.
* `not` / szűrők: De Morgan szerint feloldva; ha egy mezőn csak tiltás van, `negate="yes"`, ha pozitív és tiltó is,
  lookahead egyetlen `<field>`-ben (egy szabályban egy mezőnév csak egyszer szerepel).
* Nem támogatott (jelentésbe kerül): `Field: null`, `|exists: false`, numerikus összehasonlítás, `fieldref`,
  nem oktett-határos CIDR, 64-nél több klózra bomló feltétel.
* A szint: informational 3 · low 5 · medium 8 · high 11 · critical 13. MITRE-azonosító csak akkor kerül a
  `<mitre>` blokkba, ha az adott Wazuh MITRE-adatbázisa ismeri (`mitre_ids.json`), különben `mitre_T…` csoport lesz.

### Fontos Wazuh-sajátosság: az első találat nyer

Azonos szülő alatt (itt a Sysmon EID 1: 61603) egy eseményre **csak az első illeszkedő testvérszabály** riaszt.
Ezért a kimenet súlyosság szerint rendezett fájlokra van bontva (`sigma_1_critical.xml`, `sigma_2_high.xml`, …; a
Wazuh ábécé-sorrendben tölti be őket), a fájlokon belül a specifikusabb (több feltételes) szabály előbb jön. Ha egy
esemény több Sigma-szabályra is illik, a legsúlyosabb jelzi. A Wazuh saját, már betöltött gyerekszabályai megelőzhetik
a miénket.

### Stabil szabály-ID-k

A Wazuh-szabályazonosító nem változhat (riasztási előzmények, dashboardok, hangolás). A `wazuh/id_registry.json`
`<sigma-uuid>:<klóz-hash>` → szám leképezést tárol (100000–119999), az ID-t soha nem használja újra. A CI
(`--check-registry`) megbukik, ha a regiszter nincs commitolva – futtasd lokálisan
`dectools-wazuh build --update-registry`, és commitold a fájlt.

## Minőségkapuk

| Kapu | Hol |
|---|---|
| XML jól formált, minden regex lefordul, azonosítók egyediek | `build` |
| minden szabálynak van bizonyítottan kiváltó teszt-eseménye (>90%) · mutációs ellenpróba | `pytest` |
| 546 szabály × 60 véletlen esemény: a fordított Wazuh ugyanazt adja, mint a Sigma-szemantika | `tests/wazuh/test_equivalence.py` |
| `wazuh/benign_events.jsonl` egyetlen eseményére sem riaszthat szabály | `build` |
| szerveroldal: `wazuh-analysisd -t`, újraindítás, logtest-visszajátszás, automatikus rollback | `wazuh-deploy-gate` |

Karantén: ha egy szabály jóindulatú eseményre riaszt, a `build` megbukik. `dectools-wazuh triage` kilistázza a
tetteseket, `--write` a `wazuh/quarantine.yml`-be teszi őket (okkal együtt) – a szabály addig nem kerül élesbe.
A `benign_events.jsonl`-t érdemes saját, valódi (anonimizált) Sysmon-eseményekkel bővíteni.

## Telepítés a Wazuh managerre (egyszeri)

Elv: a GitHub **nem** ér el semmit a labor felől. A deploy egy, a laborban futó *self-hosted runnerről* indul
(csak kifelé kapcsolódik a GitHubhoz, nem kell bejövő port), a kulcs a runneren van – nem GitHub-secret.

1. **Runner:** egy kis VM-en telepítsd a GitHub Actions runnert a `lab` címkével
   (`./config.sh --labels lab`). Külön, nem privilegizált felhasználóval fusson.
2. **Kulcs a runneren:** `ssh-keygen -t ed25519 -f ~/.ssh/wazuh_deploy -N ''` (a publikus rész kell a következő lépéshez,
   a privát SOHA nem hagyja el a runnert). A manager host-kulcsát tedd a `~/.ssh/known_hosts_wazuh` fájlba
   (`ssh-keyscan -t ed25519 <manager> > ~/.ssh/known_hosts_wazuh`, majd hasonlítsd össze az ujjlenyomatot).
3. **A manageren (root):** `sudo wazuh/server/install.sh "<publikus kulcs sor>" <runner-IP>`
   Létrehozza a `wazuh-deploy` felhasználót; a kulcs kizárólag a `wazuh-deploy-gate`-et futtathatja (forced command,
   `restrict`, forrás-IP korlát), sudo is csak erre az egy programra.
4. **API-felhasználó a logtesthez:** a Wazuh dashboardon hozz létre külön, minimális jogú API-felhasználót, és írd be
   az `/etc/wazuh-deploy/api.env` fájlba (0600).
5. **GitHub:** Settings → Environments → `wazuh-prod` → *Required reviewers* (te). Repository variables:
   `WAZUH_HOST` (a manager címe). Opcionális: `WAZUH_DEPLOY_USER`, `WAZUH_SSH_KEY_PATH`, `WAZUH_KNOWN_HOSTS_PATH`.
   Settings → Actions → *Require approval for all outside collaborators*.
6. **Első kör:** Actions → *Deploy rules to Wazuh* → Run workflow → `status`, majd `deploy`.

> A repó nyilvános. Self-hosted runnert **soha** ne köss `pull_request` eseményhez (idegen fork kódot futtathatna a
> laborban). A `deploy-wazuh.yml` csak `push` a `main`-re és kézi indítás, a `ci.yml` kizárólag GitHub-hosted runneren fut.

### Mit csinál a `deploy` a manageren

csomag-ellenőrzés (SHA-256, fájlnév-fehérlista, csak 100000–119999 ID, tiltott elemek: `<command>`, `<active-response>`,
`<include>`) → mentés a jelenlegi `sigma_*.xml`-ekről → telepítés → `wazuh-analysisd -t` → újraindítás → a
`testvectors.jsonl` visszajátszása a logtest API-n (≥90% el kell süljön a mi tartományunkból, a jóindulatú események
közül egy sem) → bármilyen hiba esetén **automatikus visszaállítás és újraindítás**. `rollback` és `status` kézzel is kérhető.

## Amit érdemes tudni, mielőtt élesben használod

* **Nem teszteltem élő Wazuh ellen.** A helyi környezetben nincs Wazuh; a fordítás szemantikáját saját illesztővel
  és a Sigma-referencia ellen bizonyítottam, a deploy-gate-et hamis Wazuh-val teszteltem. Az első kört ezért futtasd
  **teszt-Wazuh VM-en** (`wazuh-analysisd -t` és a logtest valódi eredménye dönt).
* Feltevés: ha egy kötelező mező hiányzik az eseményből, a szabály nem illeszkedik, `negate="yes"` mellett sem.
  Sysmon-eseményeknél a mezők rendre megvannak; a logtest-kapu ezt a gyakorlatban ellenőrzi.
* Az `ossec.conf`-ban a manager `<rule_dir>etc/rules</rule_dir>` alapértelmezésére számít (a stock telepítés ilyen).
* 2400+ egymás melletti szabály Sysmon EID 1 alatt mérhető CPU-többletet jelent; otthoni laborban belefér, de figyeld
  az `analysisd` terhelését.
