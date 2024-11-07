---
title: CPU
parent: Hardware
nav_order: 3
---

# CPU

```mermaid
block-beta
columns 8
Bus:8
blockArrowId1<["&nbsp;&nbsp;&nbsp;"]>(up)
blockArrowId2<["&nbsp;&nbsp;&nbsp;"]>(updown)
blockArrowId3<["&nbsp;&nbsp;&nbsp;"]>(down)
blockArrowId4<["&nbsp;&nbsp;&nbsp;"]>(updown)
blockArrowId5<["&nbsp;&nbsp;&nbsp;"]>(updown)
blockArrowId6<["&nbsp;&nbsp;&nbsp;"]>(down)
blockArrowId7<["&nbsp;&nbsp;&nbsp;"]>(down)
blockArrowId8<["&nbsp;&nbsp;&nbsp;"]>(updown)
PSU
CPU
PA1
TRX1
TRX2
PA2
Aux
Interface
blockArrowId9<["&nbsp;&nbsp;&nbsp;"]>(up)
blockArrowId10<["USB"]>(updown)
space:6
RaspberryPi:2
space:6
blockArrowId13<["&nbsp;&nbsp;&nbsp;"]>(updown)
space:7
Modem
style CPU fill:#960,stroke:#000,stroke-width:2px
```

Auf dem CPU Module befindet sich der "Kopf" des Funkgerätes. Als erste Idee wird hier ein STM32 verwendet da dieser viele Ein- und Ausgänge bereitstellt. Er besitzt mehrere sehr gute ADCs und DACs welche perfekt für Audio-Verarbeitungen verwendet werden können. Mehrere Hardware-UARTs können als Kommunikation zu den FM Modulen verwendet werden.

Als zusätzliches Interface nach außen hat er zwei Pins welches für einen USB-Port verwendet werden kann. Auf diesem Interface können mehrere HID-Devices (UART, Soundkarte) in Software "angehängt" werden.

## Interfaces

Welche Interfaces werden nun benötigt:

- USB: 1
  - Kommunikation mit dem PC
- UART: 2
  - für TRX1
  - für TRX2
- ADC: 3
  - von TRX1
  - von TRX2
  - von Interface PCB
- DAC: 3
  - zu TRX1
  - zu TRX2
  - zu Interface PCB
- I2C: 6 wobei mehrere Interface zusammengefasst werden können
  - TRX1
  - TRX2
  - PA1
  - PA2
  - AUX
  - Interface PCB
