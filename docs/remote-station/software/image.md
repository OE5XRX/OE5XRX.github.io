---
title: Stations-Image
nav_order: 2
parent: Software
grand_parent: Technik
---

# Stations-Image

Repo: [OE5XRX/linux-image](https://github.com/OE5XRX/linux-image), Lizenz GPL-3.0. Stand: November 2026.

## Was es tut

Das Image ist das Betriebssystem auf dem CM4 der Station. Es startet den Station-Agenten, stellt Audio bereit und kann Modul-Firmware über USB einspielen.

## Wie es funktioniert

Das Image wird mit Yocto gebaut, für den CM4 und zusätzlich als x86-Variante für Tests in QEMU. Die wichtigsten Bausteine:

- **PipeWire und GStreamer** für das Audio zwischen Modul und Agent.
- **dfu-util** mit einer Zuordnung der USB-Anschlüsse, damit der Agent Module gezielt flashen kann.
- **Nur Ethernet:** Bluetooth und WLAN sind entfernt.
- **Fehlersuche im Feld:** Abstürze und das Journal bleiben über Neustarts erhalten.

Releases entstehen aus Tags und werden auf einem kurzzeitig gemieteten Cloud-Server gebaut. Vor jedem Release laufen ein Boot- und Update-Test sowie ein Audio-Test in QEMU. Veröffentlicht wird als GitHub-Release.

## Sicherheit und Robustheit

- **A/B-Partitionen:** Es gibt zwei komplette Root-Dateisysteme samt Kernel. Ein Update landet im inaktiven Slot, auch der Kernel wird so aktualisiert.
- **Automatischer Rollback:** Der Bootloader (U-Boot beim Raspberry Pi, GRUB auf x86) zählt Startversuche. Nach drei gescheiterten Starts fällt das System auf den alten Slot zurück.
- **Schreibgeschütztes Root-Dateisystem** und eine getrennte, persistente Datenpartition.
- **Signierte Releases:** Die Artefakte werden schlüssellos mit cosign (Sigstore) signiert.
