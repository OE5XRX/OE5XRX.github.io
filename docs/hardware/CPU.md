---
title: CPU
parent: Hardware
nav_order: 3
---

# CPU

Auf dem CPU Module befindet sich der "Kopf" des Funkgerätes. Als erste Idee wird hier ein STM32 verwendet da dieser viele Ein- und Ausgänge bereit stellt. Er besitzt mehrere sehr gute ADCs und DACs welche perfekt für Audio-Verarbeitungen verwendet werden können. Mehrere Hardware-UARTs können als Kommunikation zu den FM Modulen verwendet werden.

Als zusätzliches Interface nach außen hat er zwei Pins welches für einen USB-Port verwendet werden kann. Auf diesem Interface können mehrere HID-Devices (UART, Soundkarte) in Software "angehängt" werden.
