---
title: Software
nav_order: 2
parent: Technik
has_children: true
---

# Software

Die Software der Remote-Station besteht aus drei Teilen, die ineinandergreifen: dem Server mit Weboberfläche, dem Linux-Image für die Station und der Firmware der Funkmodule. Alle drei sind Open Source. Stand: November 2026.

## Server & Web-UI

Der Server (`station-manager`, GPL-3.0) läuft unter remote.oe5xrx.org und ist die Zentrale: Er bietet Funken im Browser mit Steuerung, RX/TX-Audio und Sendesperre, Fernwartung mit Terminal, Telemetrie und Alarmen, Rollouts von Image- und Firmware-Updates sowie Single-Sign-On für Vereins-Apps. [Mehr dazu]({% link docs/remote-station/software/server.md %}).

## Stations-Image

Das Image (`linux-image`, GPL-3.0) ist das Yocto-Linux auf dem CM4 der Station. Es hat A/B-Partitionen mit automatischem Rollback, ein schreibgeschütztes Root-Dateisystem und signierte Releases. Der Station-Agent ist eingebaut. [Mehr dazu]({% link docs/remote-station/software/image.md %}).

## Modul-Firmware

Die Firmware (`FW-RemoteStation`, LGPL-3.0) läuft auf dem STM32U575 des FM-Moduls unter Zephyr RTOS. Das Modul zeigt sich am USB als Verbund aus Soundkarte (UAC2), Steuer-Shell (CDC) und DFU. Updates sind signiert, laufen über MCUboot mit Rollback, und der Server verteilt sie automatisch. [Mehr dazu]({% link docs/remote-station/software/firmware.md %}).
