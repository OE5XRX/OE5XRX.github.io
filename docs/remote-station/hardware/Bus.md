---
title: Bus
parent: Hardware
nav_order: 1
---

# Bus

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
style Bus fill:#960,stroke:#000,stroke-width:2px
```

Die Bus-Platine ist die einfachste aber wichtigste Platine in dem System. Sie verbindet die einzelnen Module miteinander und sorgt so für einen Daten Austausch so wie die Spannungsversorgung der einzelnen Module.
Sie ist fix in das Gehäuse eingebaut, so das die anderen Module via Schienen in sie gesteckt werden können.
