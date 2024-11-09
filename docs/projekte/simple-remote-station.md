---
title: Simple-Remote-Station
nav_order: 1
parent: Projekte
---

# Simple Remote Station

Unser erstes Projekt als Verein soll eine einfache Remote Station werden. Folgende Punkte sollte das Projekt enthalten:

- keine PSU! Eine externe Stromversorgung soll verwendet werden. Um diese im Notfall auszuschalten soll ein einfacher WLan-Zwischenstecker verwendet werden. Die Stromverteilung passiert über die Bus-Platine.
- Bus und alle Modul-Platinen sind nur für einen TRX auszuführen. Somit werden keine Multiplexer oder sonstige komplizierte Bus Schaltungen benötigt.
- Die Bus Platine nimmt nur eine Mindestanzahl an Platinen auf.

Somit werden diese Modul von Nöten sein:

- Bus Platine
- CPU Modul
- TRX Modul
- Interface Modul
- Raspberry Pi / Host Computer

## Bus Platine

Die Bus Platine braucht zusätzlich zu den Bus Verbindungen Eingänge für eine Spannungsversorgung: 12V
Auf der Bus Platine sollen dann diese Spannungen erzeugt werden:

- 5V
- 3,3V

Insgesamt soll die Bus Platine Platz für 3 Modul aufnehmen können.

## CPU Modul

Das CPU Modul enthält einen STM32 als Mikroprozessor. Folgende Interfaces werden benötigt:
- 2x ADC: Für das Mikrophone und der Tastatur des Mikrophone vom Interface Modul,
- 1x DAC: Für den Lautsprecher im Interface Modul,
- 2x I2C: Für die Tasten des Mikrophone und ein OLED Display im Interface Modul,
- 1x ADC: Für den Ausgang des TRX Modul,
- 1x DAC: Für den Eingang vom TRX Modul,
- 1x UART: Für das TRX Modul,
- 1x I1C: Für GPIOs im TRX Modul,

## TRX Modul

Das TRX Modul beinhaltet einen SA818U. Der Ausgang des HF Modul wird durch einen Tiefpass-Filter zu einer SMA-Buchse weiter geleitet.
Das HF Modul besitzt mehrere Ein und Ausgänge welche über einen I2C GPIO Expander angesteuert werden soll.
Der Lautsprecher Ausgang wird an die Bus Platine weiter gereicht. Der Audio Eingang wird direkt von der Bus Platine verwendet.
Zusätzlich braucht das HF Modul auch noch einen UART welcher vom BUS kommt.

## Interface Modul

Das Interface Modul stellt folgende Komponenten zur Verfügung:
- OLED Display (I2C),
- 6 Pin RJ45 Buchse für ein Handfunkmikrophon welches auch einen Lautsprecher enthält.

Um die DTMF Tasten Abzufragen wird ein ADC im CPU Modul benützt. Möglicherweise wäre ein günstiger ADC auch eine alternative um ADCs im CPU Modul einzusparen da hier keine großen Auflösungen und Geschwindigkeiten benötigt werden.
Die restlichen Tasten und LEDs werden über einen I2C GPIO Expander abgefragt bzw. angesteuert.

Das Mikrophone und der Lautsprecher sind über einen DAC bzw. ADC zu verarbeiten. Dieses befindet sich auf der CPU Platine.

## Raspberry Pi / Host Computer

Der Host Computer kann ein Raspberry Pi oder eine sonstige Linux Box sein. Die Anforderungen sind minimal. Es lauft lediglich ein einfaches Python Script.
