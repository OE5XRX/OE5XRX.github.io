# oe5xrx.org: inhaltliche Überarbeitung (Design)

Stand: 2026-11-03 · Repo: `OE5XRX/OE5XRX.github.io`

## Warum

Die Website steht inhaltlich auf dem Stand Ende 2024 / Anfang 2025:
„ganz am Anfang, suchen Ideen", MQTT-Konzept, „2025 planen wir". Inzwischen
ist die erste Station (Gunskirchen, 2 m) QRV, und über remote.oe5xrx.org wird
im Browser gefunkt (Steuerung, RX/TX-Audio mit PTT). Die Seite verschenkt
damit ihren wichtigsten Zweck.

Die Seite hat zwei Zielgruppen, beide gleich wichtig:

- **Mitglieder:** brauchen die Seite als Doku (wo sind Stationen, wie funke ich darüber).
- **Mitbauer / technisch Interessierte:** die Seite ist technische Werbung für den
  Verein. Sie zeigt, was wir gebaut haben und wie es funktioniert, und wie man
  einsteigt.

## Ziele

1. Die Inhalte stimmen mit dem Ist-Stand auf `main` der Repos überein (Stand Nov 2026).
2. Neue Navigation, gegliedert nach den Fragen eines Besuchers (siehe Struktur).
3. Die kaputten Bilder auf der Startseite funktionieren wieder.
4. Neu: eine öffentliche Anleitung für Mitglieder, „So funkst du über die Station".
5. Die Seite veraltet langsamer (siehe Schreibregeln).

## Nicht-Ziele / Anti-Ziele

- **Design wird NICHT verändert.** Kein Eingriff in Theme, Farben, Fonts,
  Logo oder Layout. Der Brand-Layer (`OE5XRX/branding`, `apply-brand`-Action,
  gitignorte Dateien in `_sass/`, `_includes/`, `assets/`) wird nicht angefasst.
  Es gibt kein eigenes CSS und keine eigenen Includes. Erlaubt sind nur
  Markdown-Inhalte, Front Matter, Bilder und reine Konfig-Einträge in
  `_config.yml` (z.B. `exclude`).
- **Hardware-Modulseiten werden nicht angefasst.**
  `docs/remote-station/hardware/HW-Module-*/` sowie
  `docs/remote-station/hardware/versioning.md` werden aus den HW-Repos per
  `HW-Module-CI` deployt (`clean: true` auf den Modul-Ordner) und dort
  gepflegt. Lokale Änderungen würden überschrieben.
- **Publikationen** (`docs/publikationen/*`) bleiben inhaltlich unverändert.
  Das sind veröffentlichte Berichte. Sie sind aber eine wichtige Quelle.
- Keine Hilfe/Anleitung *in* der Web-UI (station-manager). Das wäre ein
  eigenes Software-Projekt.
- Anti-Ziel: Marketing-Sprech oder Übertreibung. Was nicht auf `main`
  gemergt bzw. belegt ist, wird nicht als „funktioniert" beschrieben.
- Anti-Ziel: kaputte Links. Bestehende URLs müssen weiter funktionieren.

## Harte Randbedingungen

- **URLs bleiben stabil.** Bestehende Dateien werden nicht verschoben oder
  umbenannt. Umstrukturiert wird nur über Front Matter (`title`, `parent`,
  `nav_order`). Das betrifft vor allem `docs/remote-station/hardware/` (Deploy-Ziel) und
  `docs/remote-station/hardware/versioning/` (extern verlinkt, u.a. in
  Artikeln). Neue Seiten dürfen neue Pfade bekommen.
- **Seitentitel `Hardware` bleibt exakt so und eindeutig.** Die generierten
  Modulseiten hängen per `parent: Hardware` (ohne `grand_parent`) daran.
  Keine andere Seite darf `title: Hardware` tragen.
- Theme ist `just-the-docs` (Navigation über `title`/`parent`/`grand_parent`/
  `nav_order`; Mermaid 11.3.0 ist aktiv). Build läuft per GitHub-Actions
  (`.github/workflows/jekyll.yml`), Plugins aus dem `Gemfile`.
- Sprache der Seite: Deutsch (österreichisch, Du-Form wie bisher).
- `index.md` hat aktuell kein Front Matter; das darf so bleiben oder minimal
  ergänzt werden.
- Diese Spec (und ein späterer Plan) liegen unter `docs/superpowers/` und
  dürfen **nicht** auf der Website erscheinen. Daher
  `docs/superpowers` in `_config.yml` `exclude` aufnehmen (Jekyll-4-Defaults
  bleiben dabei erhalten, prüfen!).

## Neue Struktur (Navigation)

Reihenfolge = `nav_order`. Pfade in Klammern; „neu" = neue Datei.

1. **Start** (`index.md`)
2. **Verein** (neu: `docs/verein.md`, Elternseite)
   - Über uns: Inhalt direkt auf der Verein-Seite (Zweck, ADL525/ÖVSV, Mitmachen-Hinweis)
   - Geschichte (`docs/geschichte.md`, `parent: Verein`)
   - Mitglieder & Mitgliedschaft (`docs/mitglieder.md`, `parent: Verein`)
3. **Stationen** (`docs/standorte.md`, Titel → „Stationen", bleibt Elternseite)
   - So funkst du über die Station (neu: `docs/stationen/funken.md`, `parent: Stationen`)
4. **Technik** (`docs/remote-station/index.md`, Titel „Remote-Station" → „Technik")
   - Hardware (`docs/remote-station/hardware/index.md`, `parent: Technik`; darunter
     unverändert die generierten Modulseiten + Versioning)
   - Software (`docs/remote-station/software/index.md`, `parent: Technik`)
     - Server & Web-UI (neu: `docs/remote-station/software/server.md`, `grand_parent: Technik`)
     - Stations-Image (neu: `docs/remote-station/software/image.md`)
     - Modul-Firmware (neu: `docs/remote-station/software/firmware.md`)
   - Mitbauen (neu: `docs/remote-station/mitbauen.md`, `parent: Technik`)
5. **Projekte** (`docs/projekte/index.md`)
   - Einfache Remote Station 2025 (`docs/projekte/einfache-remote-station.md`)
   - DX-Camp Döbriach 2026 (neu: `docs/projekte/dx-camp-2026.md`)
   - Ausblick 2027 (neu: `docs/projekte/ausblick-2027.md`)
6. **Publikationen** (unverändert, nur `index.md` um Hackaday-Link ergänzen)
7. **Impressum** (`docs/impressum.md`, bleibt **top-level**, `nav_order: 99`).
   *Entscheidung Claude:* nicht unter „Verein" einklappen, weil das Impressum nach
   ECG/MedienG leicht auffindbar und direkt erreichbar sein muss. Ein Footer-Link ist
   ohne Design-Änderung nicht möglich.

Hinweis zum Umbenennen: Wird „Remote-Station" zu „Technik", müssen alle
Kinder, die `parent: Remote-Station` tragen, auf `parent: Technik` umgestellt
werden. Das gilt auch für `grand_parent` bei Software-Unterseiten. Die generierten
HW-Modulseiten nutzen nur `parent: Hardware` und sind davon nicht betroffen.
Gleiches gilt für Projekte-Kinder (`parent: Projekte`, bleibt).

## Schreibregeln (gegen erneutes Veralten)

- **Technik-Seiten beschreiben nur, was existiert** (auf `main` gemergt,
  Präsens). Geplantes kommt ausschließlich nach *Projekte → Ausblick* bzw. in
  ein Projekt mit Datum.
- **Konzept statt Implementierung.** Erklären, *was* und *warum*. Für Details auf
  das Repo verlinken, statt sie zu kopieren (keine PR-Nummern-Listen,
  keine Config-Keys, keine Versionsnummern außer wo sinnvoll mit „Stand:").
- Zeitgebundene Aussagen (Status, Stationen, Projekte) tragen ein Datum
  („Stand: November 2026").
- Ehrlich und konkret, kein Hype. Engineering-Details, die für Funkamateure
  interessant sind, ruhig nennen (SA818, STM32U575, Opus, A/B-Updates).
- Keine sensiblen Interna: keine IPs, Hostnamen außer den öffentlichen
  (`remote.oe5xrx.org`, `oe5xrx.org`), keine Seriennummern, keine
  Heim-/Bench-Details (der HIL-Teststand wird nur abstrakt erwähnt).

## Seiteninhalte

### Start (`index.md`)
- Ein Satz Positionierung: Verein, der offene Remote-Stationen für den
  Amateurfunk entwickelt, baut und betreibt. Gefunkt wird im Browser.
- Kasten/Abschnitt „Was läuft gerade" (Stand-Datum): OE5XRX Gunskirchen
  QRV auf 2 m; Web-UI remote.oe5xrx.org (Mitglieder); 70-cm-Modul in Arbeit
  (finanziert laut Jahresabschlussbericht 11/2026).
- Abschnitt „Nächste Termine" mit dem Vereinsplaner-Widget (siehe unten).
- Drei Einstiege als Links: Mitmachen (→ Mitglieder), Technik, Neuigkeiten
  (→ Publikationen / neuester Bericht).
- Unterstützen-Abschnitt behalten (Mitglied werden, GoFundMe-Link wie bisher).
- „Wir lieben Open Source" behalten. **Bild-Fix:** GitHub-, OSI- und
  OSHW-Logo werden ins Repo gelegt (z.B. `docs/assets/img/` oder
  `assets/img/`, aber nicht in gitignorte Brand-Pfade) und relativ
  eingebunden. Grund: Wikimedia-Thumbnail-URLs liefern HTTP 400 (nicht
  erlaubte Thumb-Größen), und die GitHub-Asset-URL enthält einen Hash, der
  jederzeit wechseln kann. Lizenz/Herkunft der Logos prüfen (OSI- und
  OSHW-Logo stammen von Wikimedia Commons, die Nutzung als Kennzeichnung ist üblich;
  Quelle im Commit vermerken). Darstellung bleibt wie bisher (Größen
  beibehalten).

### Termine-Widget (Vereinsplaner)
Der Verein pflegt seine Termine im Vereinsplaner. Dessen Web-Widget zeigt die
nächsten Termine automatisch an, die Website muss dafür nicht gepflegt werden.
Einbau:

```html
<script type="module" src="https://web-widgets.vereinsplaner.com/v1/vp-event-widget"></script>
<vp-event-widget widget-id="01a1a0d6-b4d1-7046-aa07-4ffa67ac21f0" variant="styled"></vp-event-widget>
```

- **Platzierung:** Abschnitt „Nächste Termine" auf der Startseite (und
  optional auf der Verein-Seite). Den Script-Tag nur einmal pro Seite einbinden.
- **Design bleibt unverändert:** Das Widget rendert im Shadow DOM, es gibt
  kein Abfärben auf die Seite. An die Seite angepasst wird es nur über die öffentlichen
  `--vp-*`-Tokens (z.B. `--vp-font`, `--vp-accent`) als Inline-`style` am
  Element. Werte nach Möglichkeit von bestehenden Theme-Variablen ableiten,
  sonst Defaults lassen. Keine Änderung am Brand-Layer. Den „powered by"-Footer
  des Widgets kann man nicht entfernen, das ist so hinzunehmen.
- **Hell/Dunkel:** `theme="auto"` misst den Hintergrund nur beim Rendern.
  Prüfen, ob der Light/Dark-Toggle der Seite sauber mitspielt. Falls nicht,
  eine pragmatische Lösung wählen (z.B. neutrale Token-Werte, die in beiden
  Modi lesbar sind) und im PR beschreiben.
- `variant`: `styled` (Timeline) laut Vorgabe. Wenn das auf schmalen Bildschirmen
  schlecht aussieht, `minimal` als dokumentierte Abweichung.
- **Datenschutz:** Das Widget lädt Script und Daten von
  `web-widgets.vereinsplaner.com` (Drittanbieter, die IP des Besuchers geht dorthin).
  Die Doku sagt nichts zu Cookies. Im PR als Hinweis an den Vorstand vermerken
  (ggf. Datenschutzhinweis nötig). Kein Consent-Banner bauen.

### Verein (neu)
Kurz: Gründung 2024, Sitz Gunskirchen, ADL525 im ÖVSV, Zweck (Remote-
Stationen in ganz Österreich), Mitglieder (9, Stand 11/2026). Links zu den
Unterseiten. Bestehende Unterseiten bleiben inhaltlich, mit folgenden Ausnahmen:
- **Geschichte:** Zeitleiste fortsetzen für 2025 und 2026. Die Fakten kommen aus den
  Publikationen (QSP 04/2025, QSP 10/2025, JAB 11/2025, Jahresbericht
  04/2026, JAB 11/2026): erste Platinen v0.1/v0.2 2025, DX-Camp 2025,
  Umstieg STM32F3 → STM32U575 wegen USB-Problemen, Web-Steuerung (noch ohne Audio) beim DX-Camp
  2026, Gunskirchen QRV, Web-UI mit Audio.
  Nur belegte Ereignisse verwenden.
- **Mitglieder:** Inhalt bleibt. Den Vorstand nur ändern, wenn eine Quelle es belegt
  (sonst unverändert lassen).

### Stationen (`docs/standorte.md`)
Pro Standort: Rufzeichen, Ort, Status mit Datum (QRV / in Aufbau / geplant),
Bänder, Antenne, falls belegt. OE5XRX Gunskirchen: QRV auf 2 m, Diamond X200
(Quelle JAB 11/2026). OE8XRX Döbriach: Status aus den Quellen ableiten. Wenn
nicht belegt, neutral als Clubstation beschreiben, ohne Behauptung „in Betrieb".
„Berg" bleibt unter „in Planung". Hinweis: Zugang zum Funken über
remote.oe5xrx.org für Mitglieder, mit Link auf die Anleitung.

### So funkst du über die Station (neu)
Öffentlich lesbare Schritt-für-Schritt-Anleitung, gleichzeitig Werbung (zeigt
Nicht-Mitgliedern, wie Funken im Browser abläuft). Inhalt aus dem
tatsächlichen UI-Verhalten von station-manager `main` ableiten (Templates/
JS unter `apps/…/templates`, Control-/Audio-UI):
1. Voraussetzungen (Vorstand bestätigt): Mitgliedschaft und **erledigte
   Einführungs-Schulung**. Das Konto auf remote.oe5xrx.org legt ein **Admin** an,
   eine Selbst-Registrierung gibt es nicht. Wer ein Konto braucht, schreibt an
   **info@oe5xrx.org**. Der Admin weist danach die Station zu. Browser mit
   Mikrofon, Headset empfohlen.
2. Anmelden, Station auswählen, Bedienseite öffnen.
3. Zuhören (RX): ohne Sperre möglich, mehrere Hörer gleichzeitig.
4. Senden (TX): Sendesperre übernehmen (exklusiv, Timeout bei Inaktivität),
   PTT halten (Maus/Leertaste), Anzeige „TX ON" erst nach Bestätigung der
   Station; Abbruch der Verbindung lässt die Station automatisch entkeyen.
5. Frequenz/CTCSS etc. einstellen, soweit die UI das anbietet.
6. Betriebsregeln (Vorstand bestätigt): Senden dürfen Mitglieder, die die
   Einführungs-Schulung erledigt haben. Als Rufzeichen wird vorerst **OE5XRX**
   verwendet, wie bei der Clubstation. Keine weiteren Regeln erfinden.
Screenshots: nur wenn sie ohne Login-Daten und personenbezogene Daten
herstellbar sind. Sonst weglassen (kein Platzhalter-Bild).

### Technik (`docs/remote-station/index.md`)
Übersicht des Gesamtsystems:
- Mermaid-Diagramm: Browser ↔ Server (remote.oe5xrx.org) ↔ Station (CM4,
  Linux) ↔ Module (USB-Hub/BusBoard) ↔ Funkmodul (SA818) ↔ Antenne.
- Kurztext zum Ablauf „Funken im Browser": Steuerbefehl → Server → Station
  (Agent baut die Verbindung immer selbst nach außen auf, geht hinter NAT/LTE) → Modul-
  Shell über USB → SA818; Audio RX/TX als Opus über WebSocket, USB-Audio am
  Modul.
- Designprinzipien: modular (100×100-mm-Module am USB-Bus), selbstbeschreibende
  Module (UI wird aus Modul-Beschreibung generiert), sichere Updates auf allen
  Ebenen mit automatischem Rollback, Open Source.
- Links zu Hardware, Software, Mitbauen.

### Hardware (`docs/remote-station/hardware/index.md`)
Nur diese Index-Seite ändern: `parent: Technik`, Text vom Konjunktiv/Futur
(„wäre", „soll") auf den Ist-Stand umschreiben. Die Begründung (warum Selbstbau
statt teurer oder Billig-Funkgeräte) bleibt als kurze Herleitung. Das
bestehende Mermaid-Blockbild bleibt (stimmt mit der aktuellen HW überein). Fakten:
Module 100×100 mm, BusBoard ca. 117×100 mm mit USB-2.0-Hub und
PCN10-Steckverbindern, PowerBoard (XT60 12 V, 5-V-Buck, Strommessung),
CM4Carrier, FMTransceiver (SA818V/U + STM32U575), DeviceTester.

### Software (`docs/remote-station/software/index.md`)
Komplett neu (das alte MQTT-Konzept fällt weg). Überblick über drei Teile mit je
einem Absatz und Link auf die Unterseite + Repo:
- **Server & Web-UI** (`station-manager`, GPL-3.0): Django-basierter
  Server. Er bietet Funken im Browser (Steuerung, RX/TX-Audio, Sendesperre),
  Fernwartung (Terminal, Telemetrie, Alarme), Rollouts von Image- und
  Firmware-Updates und Single-Sign-On für Vereins-Apps.
- **Stations-Image** (`linux-image`, GPL-3.0): Yocto-Linux für den CM4,
  A/B-Partitionen mit automatischem Rollback, read-only Rootfs, signierte
  Releases (cosign), der Station-Agent ist eingebaut.
- **Modul-Firmware** (`FW-RemoteStation`, LGPL-3.0): Zephyr RTOS auf dem
  STM32U575. USB-Verbund aus Audio (UAC2), Steuer-Shell (CDC) und DFU,
  signierte Updates über MCUboot mit Rollback, Updates verteilt der Server
  automatisch.
Unterseiten jeweils: Was es tut · Wie es funktioniert (Konzept-Ebene) ·
Sicherheit/Robustheit · Repo-Link. Quelle: READMEs/Specs der Repos auf
`origin/main`. **Achtung:** Das station-manager-README und das linux-image-README sind teils
veraltet (fehlende Features bzw. Yocto-Version). Den Code bzw. die gemergten PRs als
Wahrheit nehmen.

### Mitbauen (neu)
Für technisch Interessierte: Liste der Repos mit Einzeiler und Lizenz
(HW-Module-*, HW-Module-CI, FW-RemoteStation, linux-image, station-manager,
FW-HIL). Arbeitsweise: GitHub, PRs, CI, Simulation (QEMU-Station, native_sim),
Hardware-in-the-Loop-Teststand für die Firmware (abstrakt), Versionierung der
Hardware (Link auf versioning). Einstieg: Mitglied werden / Kontakt / Hackaday-
Projekt.

### Projekte
- **Index:** Gliederung nach Status (laufend / abgeschlossen), jedes Projekt
  mit Zeitraum und Ein-Satz-Ergebnis.
- **Einfache Remote Station 2025:** Als *abgeschlossen* kennzeichnen. Am Anfang
  ein kurzes „Ergebnis" mit Verweis auf die heutige Technik. Faktenfehler
  korrigieren (Modulmaße 100×100 statt 86,36×55,88; PowerBoard statt „keine
  PSU"; tatsächliche Modulliste; kein Interface-Modul „Todo"; Tippfehler). Den
  historischen Charakter bewahren (die Seite war der Plan, jetzt Plan + Ergebnis).
- **DX-Camp Döbriach 2026** (17.–26. Juli 2026): Ziel (eine Station übers Web
  funkbar machen, MVP 1×2m-FM), was erreicht wurde (Vorstand bestätigt: einfache
  Steuerung der Station übers Web war beim Camp möglich, aber noch **kein
  Audio**; Audio im Browser kam erst danach, im September und Oktober 2026), was es
  ausgelöst hat (Modul-Plattform, virtuelle Station). Quellen: GitHub Project
  „DX Camp Döbriach 2026", Merge-Daten, Jahresabschlussbericht 11/2026.
- **Ausblick 2027:** Laut JAB 11/2026: 70-cm-Modul (finanziert), 1–2 weitere
  Stationen, LTE-Modul, APRS. Weitere Ideen aus QSP 10/2025 (Antennen-
  umschalter, HF-Verstärker, Sensor/SWR) als „Ideen" kennzeichnen.

### Publikationen
`index.md`: einen Satz ergänzen, mit Link auf das Hackaday-Projekt
(https://hackaday.io/project/205911-oe5xrx-open-source-modular-remote-ham-station)
als laufendes Build-Log.

## Quellen (in dieser Reihenfolge)

1. Code/merged PRs auf `origin/main` der Repos (station-manager, linux-image,
   FW-RemoteStation, FW-HIL, HW-Module-*).
2. Publikationen im Website-Repo (vor allem JAB 11/2026).
3. GitHub Project 3 „DX Camp Döbriach 2026".
4. READMEs (mit Vorsicht, teils veraltet).

## Fertig-Kriterien

- `bundle exec jekyll build` läuft ohne Fehler. Die Navigation entspricht der
  Struktur oben. Die generierten HW-Modulseiten hängen weiter unter Hardware.
- Alle alten URLs liefern weiterhin eine Seite (Liste der Pfade vor/nach
  vergleichen).
- Keine externen Bild-Hotlinks auf der Startseite. Alle Bilder laden.
- Interne Links geprüft (z.B. mit einem Link-Checker auf `_site`).
- `docs/superpowers/` taucht nicht in `_site` auf.
- Optisch unverändert bis auf Inhalte (Theme, Farben, Layout identisch).
- Alles auf einem Feature-Branch, **ein** PR (Spec + Plan + Inhalte).

## Geklärt mit dem Vorstand (2026-11-03)

- DX-Camp 2026: Steuerung übers Web lief, Audio noch nicht.
- Senden: geschulte Mitglieder, Rufzeichen vorerst OE5XRX.
- Konto: legt ein Admin an, Kontakt **info@oe5xrx.org**. Das ist auch der
  Kontakt auf „Mitbauen" und „Verein". Das Impressum bleibt unverändert.
- **Priorität: so schnell wie möglich online.** Daher als *ein* PR umsetzen,
  ohne Zwischen-Releases. Bei Unsicherheit lieber knapp und korrekt als
  ausführlich und geraten.
- OE8XRX Döbriach: Zum Betriebsstatus gibt es keine weitere Angabe. Neutral als
  Clubfunkstelle beschreiben, das DX-Camp 2026 als Einsatzort erwähnen.

## Dem Builder überlassen

- Genaue Formulierungen, Absatzlängen, Reihenfolge innerhalb einer Seite.
- Ob Mermaid-Diagramme als `flowchart` oder `block-beta`.
- Ablageort der Logo-Dateien (außer gitignorten Brand-Pfaden).
- Wie ausführlich die Software-Unterseiten werden (Konzept-Ebene halten).
