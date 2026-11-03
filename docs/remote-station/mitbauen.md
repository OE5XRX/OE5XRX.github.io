---
title: Mitbauen
nav_order: 3
parent: Technik
---

# Mitbauen

Alles an der Remote-Station ist offen: Schaltpläne, Layouts, Firmware und Software liegen auf GitHub unter [github.com/OE5XRX](https://github.com/OE5XRX). Du kannst reinschauen, nachbauen und mitarbeiten. Stand: November 2026.

## Die Repos

| Repo | Inhalt | Lizenz |
|------|--------|--------|
| [station-manager](https://github.com/OE5XRX/station-manager) | Server, Web-UI und Station-Agent | GPL-3.0 |
| [linux-image](https://github.com/OE5XRX/linux-image) | Yocto-Linux für den CM4 der Station | GPL-3.0 |
| [FW-RemoteStation](https://github.com/OE5XRX/FW-RemoteStation) | Zephyr-Firmware für den STM32 im FM-Modul | LGPL-3.0 |
| [FW-HIL](https://github.com/OE5XRX/FW-HIL) | Hardware-in-the-Loop-Teststand für die Firmware | GPL-3.0 |
| [HW-Module-BusBoard](https://github.com/OE5XRX/HW-Module-BusBoard) | Bus-Platine mit USB-Hub | CERN-OHL-S-2.0 |
| [HW-Module-CM4Carrier](https://github.com/OE5XRX/HW-Module-CM4Carrier) | Träger für das Raspberry Pi CM4 | CERN-OHL-S-2.0 |
| [HW-Module-PowerBoard](https://github.com/OE5XRX/HW-Module-PowerBoard) | Stromversorgung | CERN-OHL-S-2.0 |
| [HW-Module-FMTransceiver](https://github.com/OE5XRX/HW-Module-FMTransceiver) | FM-Funkmodul mit SA818 und STM32U575 | CERN-OHL-S-2.0 |
| [HW-Module-DeviceTester](https://github.com/OE5XRX/HW-Module-DeviceTester) | Testmodul | CERN-OHL-S-2.0 |
| [HW-DebugBoard](https://github.com/OE5XRX/HW-DebugBoard) | Universelles Debug-Board für Entwicklung und Tests (Schaltplanphase) | CERN-OHL-S-2.0 |
| [HW-Module-Template](https://github.com/OE5XRX/HW-Module-Template) | Vorlage für neue Hardware-Module | CERN-OHL-S-2.0 |
| [HW-Module-CI](https://github.com/OE5XRX/HW-Module-CI) | Gemeinsame CI für alle Hardware-Repos: KiBot, Auto-Release, Doku für diese Website | CERN-OHL-S-2.0 |

## Arbeitsweise

- Wir arbeiten auf GitHub: Änderungen kommen als Pull Request, die CI prüft sie.
- Die Station lässt sich simulieren: Das Linux-Image läuft in QEMU, die Firmware läuft als `native_sim` ohne Hardware.
- Für die Firmware gibt es einen Hardware-in-the-Loop-Teststand mit echter Platine. Er läuft nur auf Freigabe eines Maintainers.
- Die Hardware-Repos erzeugen bei Änderungen automatisch Releases mit Schaltplan, Stückliste und Fertigungsdaten. Wie wir Hardware versionieren, steht unter [Versioning & Releases]({% link docs/remote-station/hardware/versioning.md %}).

## Einsteigen

- Schreib uns an [info@oe5xrx.org](mailto:info@oe5xrx.org).
- Als [Mitglied]({% link docs/mitglieder.md %}) kommst du an die Station und kannst mit ihr funken.
- Den Bauverlauf dokumentieren wir auf [Hackaday.io](https://hackaday.io/project/205911-oe5xrx-open-source-modular-remote-ham-station).
