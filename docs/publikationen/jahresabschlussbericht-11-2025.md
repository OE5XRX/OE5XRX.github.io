---
title: Jahresabschlussbericht November 2025
nav_order: 3
parent: Publikationen
---

# Jahresabschlussbericht November 2025

## Allgemeines

Unser erstes Jahr als Verein war äußerst positiv – wir haben viel erreicht.
Die Zahl unserer offiziellen ÖVSV-Mitglieder konnte von 3 auf 4 erhöht werden.
Unser interner Mitgliederstand liegt derzeit bei 8 Personen. Wie bereits im letzten Jahr erwähnt, nehmen wir auch Mitglieder auf, die bereits bei anderen ADLs gemeldet sind.

In der **QSP** konnten wir zwei Artikel veröffentlichen:

- im April: *Neu gegründeter Amateurfunkclub für Remotestationen*
- im Oktober: *OE5XRX Remote-Station – Struktur, Aufbau und aktueller Entwicklungsstand*

Beide Artikel stießen auf reges Interesse in der Funkamateur-Community und brachten uns auch einige neue Mitglieder.

---

## Technischer Fortschritt

Dieses Jahr stand ganz im Zeichen der **Hardware-Entwicklung**.
Wir haben insgesamt **fünf Platinen** entworfen – manche davon bereits in der zweiten Version – sowie ein passendes **3D-gedrucktes Gehäuse** konstruiert und gefertigt.

Zu den entwickelten Platinen zählen:

- **BusBoard**
  Die zentrale Rückwandplatine bildet das Rückgrat der Station. Sie sorgt für mechanische Stabilität und elektrische Verbindung aller Module und erlaubt eine flexible Erweiterung.

- **CM4Carrier**
  Dieses Modul nimmt ein Raspberry Pi Compute Module 4 auf und dient als zentrale Steuer- und Netzwerkschnittstelle. Die angebundenen Module werden über LAN, USB und I²C verwaltet.

- **PowerBoard**
  Die Stromversorgungseinheit stellt alle benötigten Spannungen (z. B. 12 V, 5 V) bereit und überwacht Spannung und Stromaufnahme der gesamten Station.

- **DeviceTester**
  Ein flexibles Testmodul, mit dem sich Peripherie und Endgeräte vor ihrer festen Integration prüfen lassen.

- **FMTransceiver**
  Dieses Modul bindet ein SA818-Funkmodul ein und ermöglicht einfachen FM-Betrieb auf VHF oder UHF.

Mit dem 3D-Gehäuse konnte im Sommer die erste **Remote-Station** vollständig aufgebaut werden. Diese wurde im **August am DX-Camp** interessierten Kolleginnen und Kollegen vorgeführt.  
Das Feedback war äußerst positiv und hat uns in unserem Weg bestärkt.

Allerdings fehlte zu diesem Zeitpunkt noch der gesamte **Software-Teil**, sodass die vorhandene Hardware noch nicht funktionsfähig eingesetzt werden konnte.

---

## Software & Firmware

Im Herbst wurde eine umfassende **Firmware-Entwicklungsumgebung** aufgebaut – inklusive:

- Unit-Testing
- Cross-Kompilation für Host und Target
- Einbindung externer Git-Repositories zur Vermeidung von redundanter Codebasis

Dieser Aufbau war sehr zeitintensiv und wurde erst im **November** abgeschlossen, stellt nun aber eine stabile Grundlage für die weitere Entwicklung dar.

---

## Ausblick auf 2026

Im kommenden Jahr wollen wir kleinere Hardwareprobleme – insbesondere auf der FM-Platine – beheben.

Der Fokus wird dann auf der **Firmware- und Softwareentwicklung** liegen, mit dem Ziel, eine erste lauffähige Version für den **FM-Betrieb** der Remote-Station zu realisieren.

Ein weiterer wichtiger Punkt ist das **Remote-Update** von Software und Firmware – über **LTE** oder **HAMNET**.

Bis zum **Sommeranfang 2026** soll die Remote-Station **OE5XRX** in **Gunskirchen** in Betrieb gehen.
Für das nächste **DX-Camp** ist eine erste **Teststation** geplant. Sollte das erste Halbjahr erfolgreich verlaufen, ist eine Umstellung auf eine **Dauerstation** vorgesehen.

---

Weitere Informationen und aktuelle Entwicklungen findet ihr auf unserer Website:
👉 **[oe5xrx.org](https://oe5xrx.org)**
