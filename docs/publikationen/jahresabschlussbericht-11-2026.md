---
title: Jahresabschlussbericht November 2026
nav_order: 5
parent: Publikationen
---

# Jahresabschlussbericht November 2026

## Allgemeines

Das zweite Vereinsjahr war unser bisher arbeitsreichstes. Wir haben jetzt **9 Mitglieder**, im Vorjahr waren es 8. Unser Schwerpunkt hat sich von einzelnen Platinen auf das Gesamtsystem verlagert: Hardware, Firmware, Linux-Image, Server und Fernverwaltung. In unseren Repositories sind seit April über 600 Commits zusammengekommen.

## Remote-Station Gunskirchen – QRV!

Unser wichtigstes Ziel für 2026 ist erreicht. Die erste Remote-Station hängt in **Gunskirchen** an einer **Diamond X200** und steht ab sofort unseren Mitgliedern zum Testen zur Verfügung.

Derzeit arbeitet die Station **nur auf 2 m**. Für ein zweites FM-Modul für 70 cm fehlt aktuell das Budget, obwohl die Antenne beide Bänder abdeckt.

## Hardware

- **FM-Modul (SA818):** Wir haben vom STM32F3 auf den **STM32U575** gewechselt, Hardware und Firmware sind fertig. Damit sind die USB-Probleme behoben, und alles funktioniert. Das Modul meldet sich am CM4 als USB-Verbundgerät mit drei Funktionen an: CDC-ACM für die Steuerung, UAC2 für Audio und DFU für Updates.
- **Debug-Board und HIL-Testplatz:** Seit September wird jede Firmware vor der Freigabe automatisch auf echter Hardware getestet: Flashen, USB-Enumeration, DFU-Update und Audio-Loopback. Den Testplatz selbst richten wir per Ansible ein.
- **KiCad-CI:** Alle Module haben eine überarbeitete Doku und automatische, versionierte Releases. Schaltplan, Stückliste und Fertigungsdaten erzeugen wir direkt aus KiCad mit KiBot.

## Firmware FM-Modul (Zephyr)

- Audio läuft in beiden Richtungen (RX und TX) mit 8 kHz über USB, mit Hardware-Timing.
- Der **MCUboot-Bootloader mit signierten Images** erlaubt sichere Remote-Updates über USB-DFU.
- Das Modul beschreibt sich selbst: Es meldet Typ, Seriennummer (UID), Firmware-Version und Audio-Fähigkeiten an die Station.

## Linux-Image (Yocto)

- Umstellung auf **Yocto 6.0 LTS** mit Kernel 6.18 auf dem Raspberry Pi CM4
- Ausfallsichere **A/B-Updates** mit Healthcheck und automatischem Rollback
- Eine Audio-Pipeline (GStreamer/Opus) mit DSP-Kette für die TX-Pegelanpassung
- Firmware-Updates der Funkmodule direkt von der Station aus

## Weboberfläche: remote.oe5xrx.org

Die Weboberfläche war im April noch für 2026/2027 angekündigt. Sie ist schon unter [remote.oe5xrx.org](https://remote.oe5xrx.org) in Betrieb und bietet:

- **Funkbetrieb im Browser:** RX und TX mit PTT, Sendesperre (TX-Lock), Pegelanpassung und Audio-Diagnose
- Stationsverwaltung mit Live-Status, Telemetrie und Alarmierung per E-Mail, Telegram und Web-Push
- Updates mit stufenweisem Rollout (Dev- und Release-Kanal) für Image und Modul-Firmware
- Ein Remote-Terminal im Browser
- Rollenbasierte Benutzerverwaltung, ein zentrales Login (SSO) für alle Vereinsdienste und eine REST-API

## Vereinsinfrastruktur

- Der Server ist mit Terraform aufgebaut, Backups liegen offsite in Cloudflare R2, das Monitoring läuft über Grafana und Prometheus.
- Für die Bauteilverwaltung nutzen wir InvenTree, mit Abgleich der Stücklisten aus KiCad.
- Der Verein hat ein **neues Logo und ein einheitliches Erscheinungsbild** über alle Webseiten bekommen.

## Finanzen

Die finanzielle Lage ist weiterhin angespannt. Mit dem neuen Mitglied und der Hilfe unserer Sponsoren konnten wir die Arbeit weiterführen. Am dringendsten brauchen wir **ein 70-cm-FM-Modul**. Dafür und für weitere Stationen sind wir auf zusätzliche Sponsoren und Förderungen angewiesen.

## Vereinstreffen

Am **20. November 2026 ab 17:00 Uhr** gibt es ein **Vereinstreffen im Golden Pub in Linz-Urfahr**. Dort schulen wir die Mitglieder in der Bedienung der Remote-Station. **Alle Interessierten sind herzlich willkommen!**

## Ausblick 2027

- **Dauerbetrieb in Gunskirchen** und Erfahrungen im Betrieb sammeln
- **Ein 70-cm-Modul nachrüsten**, sobald die Finanzierung steht
- **1–2 weitere Remote-Stationen aufbauen**
- **Weitere Hardware-Module entwickeln**, zum Beispiel ein LTE-Modem für Standorte ohne Festnetz- oder HAMNET-Anbindung
- **Die Software weiter ausbauen:**
  - Eine Repeater-Liste in der Weboberfläche
  - Sekundäre, passive Dienste wie APRS, die die Stationen nebenbei betreiben
- **Remote-Funkbetrieb** für alle Mitglieder
- **Weitere Mitglieder und Sponsoren gewinnen**
