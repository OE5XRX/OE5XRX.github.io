---
title: CM4 Carrier
nav_order: 4
parent: Hardware
---

# CM4 Carrier PCB

<table>
  <tr><th>Top</th><th>Bottom</th></tr>
  <tr>
    <td><img src="main-3D_top.png?dummy={{ site.data['hash'] }}" alt="top" /></td>
    <td><img src="main-3D_bottom.png?dummy={{ site.data['hash'] }}" alt="bottom" /></td>
  </tr>
</table>

Das `CM4` Modul beherbergt das Gehirn der Remote Station: ein Computer Module 4 (CM4) von Raspberry Pi.
Das CM4 ist eine einfache Platine welche CPU, Speicher, Wifi und andere Komponenten direkt aufgelötet hat. Somit können über die zwei 100pin Stecker alle Schnittstellen direkt angesprochen werden.

**Verwendete Schnittstellen:**

| CM4 Schnittstelle | Anwendung                                                                          |
| ----------------- | ---------------------------------------------------------------------------------- |
| I<sup>2</sup>C    | Messen der Versorgungsspannungen und Ströme                                        |
| Ethernet          | für die Verbindung zum Internet oder andere Netzwerke (Lan, externes Modem, etc.)  |
| SD-Card           | für die Software (im Produktiven Betrieb soll das interne eMMC verwendet werden)   |
| USB               | zum aufspielen eines neuen Images in den eMMC oder zum ansprechen der Bus-Devices  |

Der benötigter Strom für das CM4 ist immer stark Abhängig welche Schnittstellen aktiv sind. Bei einem Raspberry Pi 4 kann dies bis zu 3A betragen. Nachdem jedoch kein HDMI vorgesehen ist wird sich der benötigter Strom auf unter 1A beschränken.

| Spannung | benötigter Strom |
| -------- | ---------------- |
|      +5V |          max. 1A |
|     +12V |                - |

## Daten

- [Schaltplan](main-schematic.pdf)
- [BOM](main-bom.html)
- [iBOM](main-ibom.html)
- [JLCPCB fabrication & stencil](JLCPCB/main-_JLCPCB_compress.zip)
- [JLCPCB Bom](JLCPCB/main_bom_jlc.csv)
- [JLCPCB Pick&Place](JLCPCB/main_cpl_jlc.csv)
