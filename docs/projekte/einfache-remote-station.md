---
title: Einfache-Remote-Station
nav_order: 1
parent: Projekte
---

# Einfache Remote Station

Unser erstes Projekt als Verein soll eine einfache Remote Station werden. Folgende Punkte sollte das Projekt enthalten:

- keine PSU! Eine externe Stromversorgung soll verwendet werden. Um diese im Notfall auszuschalten soll ein einfacher WLan-Zwischenstecker verwendet werden. Die Stromverteilung wird über die Bus-Platine erfolgen.
- Die Bus Platine nimmt nur eine minimale Anzahl an Modulen auf.

Somit werden diese Modul von Nöten sein:

- Bus Platine
- CM4 (Raspberry Pi) Modul
- TRX Modul (2m)
- TRX Modul (70cm)
- Interface Modul

## Module und Platinen

### CM4 (Raspberry Pi) Modul

Das CM4 Modul enthält ein CM4 Modul (Raspberry Pi) auf welchem ein Linux Betriebssystem läuft. Das USB Interface wird an die Bus Platine weiter geleitet.

### Bus Platine

Die Stromversorgung wird über die Bus Platine bewerkstelligt. Als Eingangsspannung sind 12V vorgesehen.

Insgesamt soll die Bus Platine Platz für 4 Sub-Modul aufnehmen können. Zusätzlich kommt das CM4 Modul hinzu.
Auf der Bus Platine ist weiter ein USB Hub vorgesehen welcher die USB Schnittstelle vom CM4 weiter leitet an die verschiedenen Module.

### TRX Modul

Das TRX Modul beinhaltet einen SA818. Der Ausgang des HF Modul wird durch einen Tiefpass-Filter zu einer SMA-Buchse weiter geleitet.
Ein STM32 erzeugt alle benötigten Interfaces:
- Audio Ein und Ausgang,
- UART,
- GPIOs.

### Interface Modul

Todo


## Design Entscheidungen

### Module

Die Module sollen eine Größe von 86,36x55,88 mm aufweisen. Diese ist ähnlich zu einem Raspberry Pi.

Der Abstand zwischen einem Modul zum nächsten beträgt 40 mm.

In allen 4 Ecken sollen 3,3 mm Löcher vorgesehen werden um die Module auf einen Träger zu befestigen.

### Bus Platinen Größe

Die Bus Platine kann 4 Sub-Module aufnehmen so wie ein CM4 Modul. Somit ist seine Größe nur für die Module 160x86,36 mm.

Hinzu kommt ein Abstand nach oben und unten, so wie den USB Hub.
Die Stromversorgung 12V wird über eine einfache Buchse gelöst.

In allen 4 Ecken sollen 3,3 mm Löcher vorgesehen werden um die Bus Platine auf dem Träger zu befestigen.
Zusätzlich ist unter und über jedem Steckbereich für ein Modul ein 3,3 mm Loch um dieses auf dem Träger zu befestigen.

## Mechanischer Aufbaue

Die Module werden auf einen 3D Gedruckten Rahmen befestigt. Diese werden in einen Einschubhilfe eingeführt damit das Modul richtig mit der Bus Platine verbunden wird.

Die Bus Platine wird auf einen 20x20 mm Aluminium Rahmen befestigt. Auf diesen Aluminium Rahmen sind auch die Einschubhilfen befestigt um einem Modul einen besseren halt zu geben.
