---
title: PSU
parent: Hardware
nav_order: 2
---

# PSU - Power Supply Unit

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
style PSU fill:#960,stroke:#000,stroke-width:2px
```

Die PSU versorgt die einzelnen Module mit verschiedene Spannungen.

Es werden folgenden Spannungen an den Bus weiter gegeben:
- Spannung vom Eingang (max. ~13.7V),
- 12V und
- 5V.

Aktuelle Leistungen können noch nicht bekannt gegeben werden da der Verbrauch auch noch nicht berechnet worden ist.

Als Spannungsquelle wird gerade an 13.7V (typische Autobatterie) oder 12V gedacht welche auch direkt an den Bus weiter geleitet wird für die PA.

# PSU mit Solar und Battery

Zur PSU welche einen einfachen Eingang besitzt, wäre auch eine PSU mit Solar und Batterie Eingang möglich.
