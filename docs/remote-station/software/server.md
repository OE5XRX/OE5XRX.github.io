---
title: Server & Web-UI
nav_order: 1
parent: Software
grand_parent: Technik
---

# Server & Web-UI

Repo: [OE5XRX/station-manager](https://github.com/OE5XRX/station-manager), Lizenz GPL-3.0. Stand: November 2026.

## Was er tut

Der Server läuft unter remote.oe5xrx.org und verwaltet alle Stationen des Vereins.

- **Funken im Browser:** Steuerung der Module, Empfangs- und Sendeaudio und eine exklusive Sendesperre, damit immer nur eine Person sendet.
- **Fernwartung:** Stationsübersicht, Heartbeats, Telemetrie mit Alarmen (per E-Mail, Telegram oder Web-Push), ein Terminal im Browser und ein Audit-Log.
- **Updates:** Rollouts von Linux-Images (mit Gruppen für Entwicklung und Release) und von Modul-Firmware.
- **Single-Sign-On:** Der Server ist der zentrale Login für Vereins-Apps wie unsere InvenTree-Instanz.
- **Schnittstelle für Automatisierung:** Eine API mit Token-Zugriff und einheitlichem Rechtesystem.

## Wie es funktioniert

Der Server ist eine Django-Anwendung mit PostgreSQL, Redis und Channels für die Echtzeitverbindungen. Die Oberfläche nutzt Bootstrap, HTMX und Alpine.js, das Terminal basiert auf xterm.js.

Auf jeder Station läuft ein Agent (Teil desselben Repos). Er hält eine Steuerverbindung zum Server und erzeugt das Audio. Der Server reicht Audio nur weiter und verarbeitet es nicht. Der Browser dekodiert den Opus-Strom und mischt ihn ab. Beim Senden kodiert der Browser das Mikrofon als Opus und schickt es über denselben Weg zur Station. Der Agent pegelt den Ton dort (Filter, Kompressor, Limiter), bevor er ans Modul geht.

Die Bedienoberfläche wird aus den Beschreibungen erzeugt, die die Module selbst liefern. Der Server führt außerdem ein Inventar der Module nach ihrer Chip-ID. Er weiß, welche Firmware ein Modul haben soll, und lässt den Agenten abweichende Module aktualisieren.

## Sicherheit und Robustheit

- Jede Station hat ein eigenes Schlüsselpaar (Ed25519) und signiert ihre Anfragen. Es gibt keine gemeinsamen Geheimnisse.
- Der Agent baut nur ausgehende Verbindungen auf. Die Station braucht keine offenen Ports.
- Ein einheitliches Rechtesystem steuert, wer was darf. Änderungen landen im Audit-Log.
- Das Linux-Update läuft als A/B-Update mit Gesundheitsprüfung und automatischem Rollback.
