---
title: Modul-Firmware
nav_order: 3
parent: Software
grand_parent: Technik
---

# Modul-Firmware

Repo: [OE5XRX/FW-RemoteStation](https://github.com/OE5XRX/FW-RemoteStation), Lizenz LGPL-3.0. Stand: November 2026.

## Was sie tut

Die Firmware läuft auf dem STM32U575 des FM-Moduls und macht aus dem SA818 ein USB-Gerät, das der CM4 steuern und hören kann.

## Wie es funktioniert

Die Firmware basiert auf Zephyr RTOS und ist in C++20 geschrieben. Das Modul meldet sich am USB als Verbund aus drei Funktionen:

- **Steuer-Shell (CDC-ACM):** Über sie wird das Modul bedient. Das Modul beschreibt dabei selbst, was es kann. Daraus erzeugt die Web-Oberfläche ihre Bedienelemente. Die Beschreibung enthält auch Chip-ID, Firmware-Version und Variante.
- **Audio (UAC2):** Vollduplex bei 8 kHz, für Empfang und Senden.
- **DFU:** Zugang für Firmware-Updates.

Die Firmware lässt sich auch ohne Hardware bauen und testen (`native_sim`). Für Tests an echter Hardware gibt es das Projekt [FW-HIL](https://github.com/OE5XRX/FW-HIL): einen Teststand, an dem eine Platine hängt. Er prüft unter anderem USB, Update und Audio. Der Test läuft nur, wenn ein Maintainer einen Pull Request dafür freigibt.

## Sicherheit und Robustheit

- **Signierte Images:** MCUboot prüft die Signatur (ECDSA P-256) und verhindert Downgrades. Updates laufen über A/B-Tausch.
- **Bestätigung nach dem Start:** Ein neues Image gilt erst als gut, wenn drei Prüfungen bestanden sind: USB ist da, die Shell läuft, das SA818 antwortet. Sonst kehrt das Modul zum alten Image zurück. Ein Watchdog fängt Hänger ab.
- **Verteilung:** Der Server verteilt neue Firmware automatisch, der Agent spielt sie ein.
