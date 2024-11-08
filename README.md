# OE5XRX.github.io

Dieses Repository beinhaltet den Source Code für die Webseite [oe5xrx.org](https://oe5xrx.org/).

Der Inhalt der Webseite wird mit [Markdown](https://docs.github.com/de/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) in den Textfiles mit der Endung `.md` geschrieben.
Über Jekyll werden die Markdown Daten übersetzt in HTML Dateien welche dann von Github angezeigt werden.

## Webseite lokal bauen und sehen

Um die Webseite auf deinem PC zu testen führe folgenden Befehl auf der Konsole aus:

```
bundle install --path .bundle
```

Um nun die Webseite zu sehen, führe diesen Befehl aus:

```
bundle exec jekyll serve
```

Jetzt kannst du einen Browser deiner Wahl aufmachen und rufst diese URL auf: `http://127.0.0.1:4000`
Dort solltest du nun die Webseite sehen. Die Webseite wird nun automatisch neu generiert wenn du eine Datei im Projekt speicherst.
