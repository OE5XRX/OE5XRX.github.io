---
title: Einfache Remote Station 2025
nav_order: 3
parent: Projekte
---

# Einfache Remote Station 2025

> **Abgeschlossen.** Diese Seite war ursprünglich der Plan für 2025 und zeigt jetzt Plan und Ergebnis. Die Platinen sind entworfen, gefertigt und vermessen. Die Station in ihrer heutigen Form beschreibt die [Technik](../remote-station/).

Unser erstes Projekt als Verein sollte eine einfache Remote Station werden. Folgende Punkte sollte das Projekt enthalten:

- Keine eigene PSU. Eine externe Stromversorgung wird verwendet, die sich im Notfall über einen einfachen WLAN-Zwischenstecker ausschalten lässt. Die Stromverteilung übernimmt die Bus-Platine. Im Ergebnis erzeugt das PowerBoard die 5 V aus externen 12 V; die Bus-Platine verteilt sie.
- Die Bus-Platine nimmt nur eine minimale Anzahl an Modulen auf.

## Module und Platinen

Geplant waren eine Bus-Platine, ein CM4-Modul und zwei Funkmodule (2 m und 70 cm). Als Ergebnis gibt es diese Platinen:

- **BusBoard:** die Bus-Platine
- **PowerBoard:** Stromversorgung
- **CM4Carrier:** Träger für das Raspberry Pi CM4
- **FMTransceiver:** FM-Funkmodul
- **DeviceTester:** Test- und Bring-up-Board

### CM4Carrier

Der CM4Carrier trägt ein Raspberry Pi CM4, auf dem ein Linux-Betriebssystem läuft. Das USB-Interface wird an die Bus-Platine weitergeleitet.

### BusBoard

Die Bus-Platine verbindet die Module über PCN10-Steckverbinder. Sie ist ca. 117×100 mm groß und enthält einen USB-2.0-Hub, der die USB-Schnittstelle des CM4 an die Module weiterleitet.

### PowerBoard

Das PowerBoard wird mit 12 V über einen XT60-Stecker versorgt und ist mit 3 A abgesichert. Ein 5-V-Buck-Wandler erzeugt die 5 V für die Module, zwei INA226 messen den Strom.

### FMTransceiver

Das Funkmodul enthält einen SA818 (SA818V für 2 m oder SA818U für 70 cm). Der Ausgang des HF-Moduls führt über einen Tiefpassfilter zu einer SMA-Buchse. Ein STM32U575 stellt alle benötigten Schnittstellen bereit:

- Audio Ein- und Ausgang
- UART
- GPIOs
- USB (Steuerung, Audio, Firmware-Update)

Ursprünglich war ein STM32F3 vorgesehen. Wir haben ihn wegen USB-Problemen durch den STM32U575 ersetzt.

### DeviceTester

Der DeviceTester ist ein Board zum Testen und für die Inbetriebnahme (Bring-up) der anderen Module.

## Design-Entscheidungen

### Module

Die Module haben eine Größe von 100×100 mm.

In allen 4 Ecken sind 3,3-mm-Löcher vorgesehen, mit denen die Module auf einem Träger befestigt werden.

### Größe der Bus-Platine

Die Bus-Platine ist ca. 117×100 mm groß.

## Mechanischer Aufbau

Die Module und die Bus-Platine sitzen in einem 3D-gedruckten Gehäuse. Einschubhilfen sorgen dafür, dass die Module richtig mit der Bus-Platine verbunden werden.
