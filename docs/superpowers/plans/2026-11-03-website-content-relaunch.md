# oe5xrx.org Content-Relaunch: Implementierungsplan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Ziel:** Die Inhalte von oe5xrx.org auf den Stand November 2026 bringen, mit neuer Navigation, ohne das Design zu verändern.

**Architektur:** Reine Markdown- und Front-Matter-Änderungen in einer just-the-docs-Jekyll-Seite. Umstrukturiert wird nur über `title`/`parent`/`grand_parent`/`nav_order`. Bestehende Dateien werden nicht verschoben. Verifiziert wird über einen lokalen Docker-Build und `site_check.py` (URLs, Links, Bilder, Navigation).

**Tech Stack:** Jekyll 4.4, just-the-docs, Mermaid 11.3, kramdown, Docker (`ruby:3.4`), Python 3 (Prüfskript).

**Spec:** `docs/superpowers/specs/2026-11-03-website-content-relaunch-design.md` (vor jedem Task lesen; die Inhaltsvorgaben pro Seite stehen dort im Abschnitt „Seiteninhalte").

## Global Constraints

- Design wird **nicht** verändert: kein CSS, keine Includes, kein Eingriff in den Brand-Layer (gitignorte Pfade in `.gitignore`), keine Theme-Optionen.
- **Nicht anfassen:** `docs/remote-station/hardware/HW-Module-*/**`, `docs/remote-station/hardware/versioning.md`, `docs/publikationen/*.md` außer `index.md`.
- Bestehende Dateien nicht verschieben oder umbenennen. Alle URLs aus `docs/superpowers/tools/baseline-urls.txt` müssen weiter existieren.
- Der Seitentitel `Hardware` bleibt exakt so und eindeutig (die Modulseiten hängen per `parent: Hardware` daran).
- Deutsch, Du-Form. Ehrlich, kein Hype. Technik-Seiten nur Ist-Stand im Präsens. Geplantes kommt nur unter Projekte.
- Zeitgebundenes trägt „Stand: November 2026".
- Öffentlicher Kontakt: `info@oe5xrx.org`. Das Impressum bleibt inhaltlich unverändert.
- Keine IPs, keine internen Hostnamen, keine Seriennummern. Öffentliche Hosts sind nur `remote.oe5xrx.org` und `oe5xrx.org`.
- Fakten nur aus den Quellen der Spec (Code `origin/main`, Publikationen, Project 3). Was nicht belegt ist, weglassen.
- Die Repos liegen lokal unter `<workspace>/<repo>`, gelesen wird von `origin/main` (`git -C <repo> show origin/main:<pfad>`).
- Commit-Footer: `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`

## Verifikation (in jedem Task)

```bash
docs/superpowers/tools/build-local.sh          # braucht /tmp/brand = OE5XRX/branding @ v0.2.5
python3 docs/superpowers/tools/site_check.py   # ab Task 6 zusätzlich: --nav
```
`/tmp/brand` fehlt? → `git clone -q --branch v0.2.5 https://github.com/OE5XRX/branding /tmp/brand`.
Erwartet: `OK`. Ausnahme bis Task 1 erledigt ist: die 4 bekannten Fehler (superpowers publiziert, 3 externe Logos).

## Review Focus

1. **Generierte HW-Modulseiten fallen aus der Navigation**, wenn „Hardware" umbenannt oder dupliziert wird → `site_check.py --nav` prüft „FM Transceiver" im Menü (Task 6).
2. **Light/Dark-Toggle mit dem Vereinsplaner-Widget:** Text muss in beiden Modi lesbar sein → manuelle Sichtprüfung beider Modi im Browser, Ergebnis im PR (Task 1).
3. **Kramdown frisst Raw-HTML** (Custom Element ohne Leerzeilen drumherum wird zu `<p>`-Text) → Test in Task 1 prüft, dass `<vp-event-widget` als Element im `_site/index.html` steht und nicht escaped ist.
4. **Relative Links brechen**, weil Seiten jetzt andere Eltern haben (z.B. `standorte.html` aus der Geschichte, `../mitglieder` von der Startseite) → `site_check.py` prüft alle internen Links nach jedem Task.
5. **Falsche Faktenbehauptungen** (DX-Camp „Audio lief", OE8XRX „in Betrieb") → Grep-Asserts in Task 3 und Task 5.

---

### Task 1: Build-Ausschluss, Startseite, Logos, Termine-Widget

**Files:**
- Modify: `_config.yml` (`exclude` ergänzen)
- Modify: `index.md`
- Create: `assets/img/github-logo.png`, `assets/img/osi-logo.svg`, `assets/img/oshw-logo.svg`

**Interfaces:**
- Produces: Pfad `docs/verein.html` (Link-Ziel, wird in Task 2 erstellt). Bis dahin meldet `site_check` den Link als kaputt, das ist erlaubt, bis Task 2 fertig ist. Ebenso `docs/stationen/funken.html` (Task 3) und `docs/remote-station/index.html` (gibt es schon).

- [ ] **Step 1: Fehler reproduzieren.** Build + `site_check.py`. Erwartet: genau die 4 bekannten Fehler.
- [ ] **Step 2: `_config.yml`:** `exclude:` mit `docs/superpowers` plus die Jekyll-4-Defaults explizit (`.sass-cache`, `.jekyll-cache`, `gemfiles`, `Gemfile`, `Gemfile.lock`, `node_modules`, `vendor/bundle/`, `vendor/cache/`, `vendor/gems/`, `vendor/ruby/`), zusätzlich `README.md`, `LICENSE`.
- [ ] **Step 3: Logos holen** (Quelle steht im Commit):
  - `https://github.githubassets.com/assets/GitHub-Logo-ee398b662d42.png` → `assets/img/github-logo.png`
  - `https://upload.wikimedia.org/wikipedia/commons/e/eb/Open_Source_Initiative.svg` → `assets/img/osi-logo.svg`
  - `https://upload.wikimedia.org/wikipedia/commons/f/fd/Open-source-hardware-logo.svg` → `assets/img/oshw-logo.svg`
  Mit `curl -fsSL -A "Mozilla/5.0"` laden. Prüfen, dass die Dateien ein gültiges PNG/SVG sind (`file`).
- [ ] **Step 4: `index.md` neu schreiben** (Spec → „Start"). Front Matter: `title: Start`, `nav_order: 1`. Inhalt in dieser Reihenfolge:
  1. Positionierung (ein Satz).
  2. „Was läuft gerade" mit „Stand: November 2026": OE5XRX Gunskirchen QRV auf 2 m; Funken im Browser über remote.oe5xrx.org (für Mitglieder); 70-cm-Modul in Arbeit und finanziert.
  3. „Nächste Termine" mit dem Widget (Snippet aus der Spec, exakt diese `widget-id`, `variant="styled"`). Leerzeilen vor und nach dem HTML-Block.
  4. Einstiege: Mitmachen → `docs/mitglieder`, Technik → `docs/remote-station/`, Neuigkeiten → `docs/publikationen/`.
  5. Unterstützen: Mitglied werden + der GoFundMe-Link `https://gofund.me/9dd9fa90` (unverändert).
  6. „Wir lieben Open Source!" mit den drei lokalen Logos über `{{ '/assets/img/…' | relative_url }}`. Breiten wie bisher: GitHub `width="50"`, OSI `width="183"`, OSHW `width="228"`.
  Widget-Styling: nur `--vp-*`-Tokens als Inline-`style`. Werte stammen aus Brand-Variablen, falls `/tmp/brand/jekyll/_sass/custom/custom.scss` CSS-Custom-Properties definiert. Sonst kein `style` und `theme="auto"`.
- [ ] **Step 5: Verifizieren.** Build + `site_check.py`. Erwartet: nur noch der fehlende Link `docs/verein.html` bzw. `docs/stationen/funken.html` (falls verlinkt). Zusätzlich:
  ```bash
  grep -c '<vp-event-widget widget-id="01a1a0d6-b4d1-7046-aa07-4ffa67ac21f0"' _site/index.html   # → 1
  grep -c '&lt;vp-event-widget' _site/index.html                                                     # → 0
  grep -c 'web-widgets.vereinsplaner.com/v1/vp-event-widget' _site/index.html                        # → 1
  ls _site/docs/superpowers 2>/dev/null | wc -l                                                      # → 0
  ```
- [ ] **Step 6: Sichtprüfung Light/Dark.** `cd _site && python3 -m http.server 8000`, dann im Browser oder per Screenshot-Tool beide Modi ansehen. Ist das Widget im Dark Mode unlesbar, ein Token-Set wählen, das in beiden Modi trägt, und das im Commit vermerken.
- [ ] **Step 7: Commit** `feat(home): rewrite start page, self-host logos, add Vereinsplaner events widget`

### Task 2: Verein, Geschichte, Mitglieder, Impressum

**Files:**
- Create: `docs/verein.md`
- Modify: `docs/geschichte.md`, `docs/mitglieder.md`, `docs/impressum.md` (nur Front Matter)

**Interfaces:**
- Produces: Elternseite mit `title: Verein`, `nav_order: 10`.

- [ ] **Step 1: Failing check.** `grep -l '^title: Verein$' docs/*.md`, erwartet: leer.
- [ ] **Step 2: `docs/verein.md`** (Spec → „Verein"): Gründung 23.09.2024, Sitz Gunskirchen, ADL525 im ÖVSV, Zweck, 9 Mitglieder (Stand November 2026), Kontakt info@oe5xrx.org, Links zu Geschichte/Mitglieder/Statuten (`Vereinsstatuten.pdf`). Front Matter: `title: Verein`, `nav_order: 10`, `has_children: true`.
- [ ] **Step 3: `docs/geschichte.md`:** `parent: Verein`, `nav_order: 1`. Bestehenden Text behalten. Absätze für 2025 und 2026 anhängen, nur aus den Publikationen (`docs/publikationen/*.md`): Platinen v0.1/v0.2 (2025), QSP-Artikel 04/2025 und 10/2025, Umstieg STM32F3 → STM32U575 wegen USB-Problemen, DX-Camp 2026 mit Web-Steuerung (noch ohne Audio), Gunskirchen QRV auf 2 m, Funken im Browser mit Audio ab Herbst 2026. Den Link `standorte.html` beibehalten.
- [ ] **Step 4: `docs/mitglieder.md`:** `parent: Verein`, `nav_order: 2`. Inhalt unverändert.
- [ ] **Step 5: `docs/impressum.md`:** bleibt top-level, `nav_order: 99`. Keine Inhaltsänderung.
- [ ] **Step 6: Verifizieren.** Build + `site_check.py`. Erwartet: kein Fehler mehr zu `verein.html`. `grep -c 'ADL525' _site/docs/verein.html` → ≥1.
- [ ] **Step 7: Commit** `feat(verein): add Verein section, extend history to 2026`

### Task 3: Stationen + „So funkst du über die Station"

**Files:**
- Modify: `docs/standorte.md`
- Create: `docs/stationen/funken.md`

**Interfaces:**
- Consumes: station-manager UI auf `origin/main`: `apps/control/templates/control/panel.html`, `_lock_banner.html`, `_audio_panel.html`, `widgets/_ptt.html`, `static/js/control-panel.js`, `static/js/audio-panel.js`.
- Produces: `title: Stationen` (`nav_order: 20`, `has_children: true`) und Kind `title: So funkst du über die Station` (`parent: Stationen`, `nav_order: 1`).

- [ ] **Step 1: Failing check.** `test -f docs/stationen/funken.md`, erwartet: Exit 1.
- [ ] **Step 2: `docs/standorte.md`:** Titel „Stationen", Pro-Standort-Status mit „Stand: November 2026".
  - **OE5XRX Gunskirchen:** QRV 2 m, Diamond X200.
  - **OE8XRX Döbriach:** neutral als Clubfunkstelle (seit 07.11.2024), DX-Camp-Einsatzort. Kein „in Betrieb".
  - **Berg:** unter „in Planung", Text beibehalten.
  - Abschnitt „Über die Station funken" mit Link auf die Anleitung.
- [ ] **Step 3: UI-Verhalten nachlesen** in den Consumes-Dateien. Festhalten: wie die Sendesperre heißt und übernommen wird, Timeout, PTT-Bedienung (Maus/Taste), TX-Anzeige, was ohne Sperre geht (Zuhören), welche Einstellungen das FM-Modul anbietet (Frequenz, CTCSS …).
- [ ] **Step 4: `docs/stationen/funken.md`** nach Spec → „So funkst du über die Station", Schritte 1–6. Die UI-Begriffe so verwenden, wie sie in den Templates stehen.
  - **Voraussetzungen:** Mitgliedschaft, erledigte Einführungs-Schulung, Konto legt ein Admin an (Anfrage an info@oe5xrx.org), keine Selbst-Registrierung.
  - **Rufzeichen:** vorerst **OE5XRX**.
  - **Screenshots:** keine.
- [ ] **Step 5: Verifizieren.** Build + `site_check.py`. Dazu:
  ```bash
  grep -c 'info@oe5xrx.org' _site/docs/stationen/funken.html     # ≥1
  grep -c 'OE5XRX' _site/docs/stationen/funken.html              # ≥1
  grep -ci 'in Betrieb' _site/docs/standorte.html                # nur im Gunskirchen-Kontext; OE8XRX-Abschnitt darf es nicht enthalten (manuell prüfen)
  ```
- [ ] **Step 6: Commit** `feat(stationen): station status page and public operating guide`

### Task 4: Technik: Übersicht, Hardware-Index, Software, Mitbauen

**Files:**
- Modify: `docs/remote-station/index.md`, `docs/remote-station/hardware/index.md`, `docs/remote-station/software/index.md`
- Create: `docs/remote-station/software/server.md`, `docs/remote-station/software/image.md`, `docs/remote-station/software/firmware.md`, `docs/remote-station/mitbauen.md`

**Interfaces:**
- Produces: `title: Technik` (`nav_order: 50`, `has_children: true`). Kinder: `Hardware` (1, bleibt Titel exakt), `Software` (2, `has_children: true`), `Mitbauen` (3). Software-Kinder: `Server & Web-UI` (1), `Stations-Image` (2), `Modul-Firmware` (3), jeweils `parent: Software`, `grand_parent: Technik`.

- [ ] **Step 1: Failing check.** `grep -c MQTT docs/remote-station/software/index.md` → ≥1 (soll am Ende 0 sein).
- [ ] **Step 2: Übersicht `docs/remote-station/index.md`** (Spec → „Technik"):
  - Mermaid-`flowchart`: Browser ↔ remote.oe5xrx.org ↔ Station (CM4/Linux) ↔ BusBoard/USB ↔ FM-Modul (SA818) ↔ Antenne.
  - Ablauf „Funken im Browser".
  - Designprinzipien.
  - Links zu den Unterseiten.
- [ ] **Step 3: Hardware-Index:** `parent: Technik`, Text im Präsens, Fakten aus der Spec. Das Mermaid-Bild unverändert lassen.
- [ ] **Step 4: Software-Index + 3 Unterseiten** (Spec → „Software"). Je Seite: Was es tut · Wie es funktioniert · Sicherheit/Robustheit · Repo-Link `https://github.com/OE5XRX/<repo>` mit Lizenz. Lizenzen so verwenden, wie die LICENSE-Dateien auf `origin/main` sie angeben (FW-RemoteStation: Datei prüfen). Fakten aus Code/PRs, nicht aus den veralteten READMEs.
- [ ] **Step 5: `mitbauen.md`** (Spec → „Mitbauen"):
  - Repo-Tabelle mit Einzeiler + Lizenz.
  - Arbeitsweise, abstrakter HIL-Teststand, Link auf `hardware/versioning`.
  - Kontakt info@oe5xrx.org, Mitglied werden, Hackaday-Link.
- [ ] **Step 6: Verifizieren.** Build + `site_check.py`. `grep -c MQTT _site/docs/remote-station/software/index.html` → 0. `grep -c 'parent: Hardware' docs/remote-station/hardware/HW-Module-FMTransceiver/index.md` → 1 (unverändert). `git diff --stat origin/main -- docs/remote-station/hardware/HW-Module-* docs/remote-station/hardware/versioning.md` → leer.
- [ ] **Step 7: Commit** `feat(technik): rewrite system overview, software and contributor pages`

### Task 5: Projekte + Publikationen

**Files:**
- Modify: `docs/projekte/index.md`, `docs/projekte/einfache-remote-station.md`, `docs/publikationen/index.md`
- Create: `docs/projekte/dx-camp-2026.md`, `docs/projekte/ausblick-2027.md`

**Interfaces:**
- Produces: Kinder von `Projekte` (Titel exakt): `Ausblick 2027` (1), `DX-Camp Döbriach 2026` (2), `Einfache Remote Station 2025` (3).

- [ ] **Step 1: Failing check.** `grep -c '86,36' docs/projekte/einfache-remote-station.md` → ≥1.
- [ ] **Step 2: Index:** nach Status gruppiert (geplant / abgeschlossen), je Projekt Zeitraum + Ein-Satz-Ergebnis.
- [ ] **Step 3: Einfache Remote Station 2025:** Titel ändern. Oben ein Kasten „Abgeschlossen" + Ergebnis mit Link auf Technik. Faktenfehler laut Spec korrigieren (100×100 mm, BusBoard ca. 117×100 mm, PowerBoard mit XT60/5-V-Buck, reale Modulliste inkl. DeviceTester, kein „Interface Modul Todo", 3D-gedrucktes Gehäuse statt Alu-Rahmen, falls im Text, „Aufbaue"-Tippfehler).
- [ ] **Step 4: DX-Camp Döbriach 2026** (17.–26. Juli 2026):
  - Ziel: MVP 1×2m-FM übers Web.
  - Ergebnis: Steuerung übers Web lief, **noch kein Audio**. Audio folgte im September/Oktober 2026.
  - Was es angestoßen hat: Modul-Plattform, virtuelle QEMU-Station.
- [ ] **Step 5: Ausblick 2027:** 70-cm-Modul (finanziert), 1–2 weitere Stationen, LTE-Modul, APRS. Darunter „Ideen" aus QSP 10/2025 (Antennenumschalter, HF-Verstärker, Sensor/SWR-Karten).
- [ ] **Step 6: Publikationen-Index:** ein Satz + Hackaday-Link `https://hackaday.io/project/205911-oe5xrx-open-source-modular-remote-ham-station`.
- [ ] **Step 7: Verifizieren.** Build + `site_check.py`. Dazu:
  ```bash
  grep -c '86,36' _site/docs/projekte/einfache-remote-station.html   # 0
  grep -ci 'kein.* audio\|ohne audio\|noch kein audio' _site/docs/projekte/dx-camp-2026.html   # ≥1
  ```
- [ ] **Step 8: Commit** `feat(projekte): mark 2025 project done, add DX-Camp 2026 and 2027 outlook`

### Task 6: Navigation abnehmen + PR

**Files:** keine neuen (nur Fixes, falls die Checks scheitern)

- [ ] **Step 1:** Build + `python3 docs/superpowers/tools/site_check.py --nav`. Erwartet: `OK`.
- [ ] **Step 2:** `git diff --stat origin/main -- _sass _includes assets/css assets/fonts .github` → leer (Design unangetastet).
- [ ] **Step 3:** Push + PR gegen `main` (Titel: `Website-Relaunch: Inhalte auf Stand November 2026`). Body:
  - Struktur-Übersicht.
  - Liste der Entscheidungen aus der Spec.
  - Datenschutz-Hinweis zum Vereinsplaner-Widget (Drittanbieter, IP-Übertragung, ggf. Datenschutzhinweis nötig).
  - Ergebnis der Light/Dark-Prüfung.
  - Hinweis auf das lokale Build-Skript.

  Ende mit `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
- [ ] **Step 4:** Warten, bis die Pages-Build-Checks des PRs grün sind (falls vorhanden). **Nicht selbst mergen.**
