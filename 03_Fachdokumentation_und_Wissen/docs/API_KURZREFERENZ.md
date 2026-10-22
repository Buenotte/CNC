# Autodesk Post Processor API (Application Programming Interface / Programmierschnittstelle) – Kurzreferenz & Spickzettel

Dieses Dokument im Ordner `docs/` dient als schnelles Nachschlagewerk für Sie und die **KI (Künstliche Intelligenz)** bei der Programmierung von `.cps`-Dateien (**CAM Post Scripts – JavaScript-Postprozessoren**).

---

## 1. Lebenszyklus-Funktionen (Entry Functions / Automatisch aufgerufene Ereignisfunktionen)

Wenn **Autodesk Fusion (CAD/CAM-Software)** oder das **Post Processor Utility (Entwickler-Plugin)** eine `.cps`-Datei ausführt, werden diese Funktionen in folgender Reihenfolge aufgerufen:

| JavaScript-Funktion | Wann wird sie aufgerufen? | Typische G-Code-Ausgabe (Maschinenbefehle) |
| :--- | :--- | :--- |
| `onOpen()` | Einmalig ganz zu Beginn des Programmexports. | `%`, Programmnummer `O1001`, Entwickler-Header (Kopfkommentar), Werkzeugliste, Sicherheitszeile (`G90 G17 G40 G49 G80 G21`). |
| `onSection()` | Zu Beginn jeder neuen **CAM-Operation (Bearbeitungsstrategie wie Planfräsen, Konturfräsen, Bohren)**. | Sicherer Rückzug (`G53 G00 Z0`), Werkzeugwechsel (`T01 M06`), Spindelstart (`S8000 M03`), Nullpunkt (`G54`), Längenkorrektur (`G43 H01`), Kühlmittel (`M08`). |
| `onRapid(x, y, z)` | Bei jeder schnellen Positionierbewegung in der Luft (**Eilgang / Rapid Move**). | `G00 X... Y... Z...` |
| `onLinear(x, y, z, feed)` | Bei jeder geradlinigen Fräsbewegung im Material (**Linear Interpolation**). | `G01 X... Y... Z... F...` (mit **Vorschub / Feedrate `F`**). |
| `onCircular(clockwise, cx, cy, cz, x, y, z, feed)` | Bei jeder Kreisbogen-Bewegung (**Circular Interpolation**). | `G02` (im Uhrzeigersinn / CW) oder `G03` (gegen den Uhrzeigersinn / CCW) mit Kreismittelpunkt-Abständen `I`, `J`, `K`. |
| `onCycle()` / `onCyclePoint(x, y, z)` / `onCycleEnd()` | Bei Bohrzyklen, Reibzyklen oder Gewindebohrzyklen (**Canned Cycles / Festzyklen**). | `G81` (Standardbohren), `G83` (Tiefbohren mit Entspanen), `G84` (Gewindebohren), beendet durch `G80` (Zyklus aufheben). |
| `onSectionEnd()` | Am Ende jeder einzelnen CAM-Operation. | Rücksetzen von modalen Zuständen (Speicherzuständen). |
| `onClose()` | Einmalig ganz am Ende des gesamten Programms. | Kühlmittel aus (`M09`), Z-Achse hochfahren (`G53 G00 Z0`), Spindel aus (`M05`), Tisch vorfahren (`G53 G00 Y0`), Programmende (`M30`), `%`. |

---

## 2. Wichtige Globale Objekte & Funktionen der Autodesk Post-API (Programmierschnittstelle)

### Text- und Blockausgabe
* `writeln("Text")`: Schreibt einen String (Textkette) exakt so in die Ausgabedatei, gefolgt von einem Zeilenumbruch.
* `writeWords("G00", "X10.0")`: Verbindet alle übergebenen Argumente mit einem Leerzeichen und gibt sie als Zeile aus.
* `writeWords2("N10", arguments)`: Wie `writeWords`, stellt aber eine **Satznummer (Zeilennummer wie `N10`)** voran.
* `getProperty("propertyName")`: Liest den aktuellen Wert einer **Benutzereigenschaft (`properties` – vom Anwender einstellbare Option)** aus.

### Formatierung & Modale Variablen (Zustandsbehaftete Variablen)
* `createFormat({prefix: "G", width: 2, zeropad: true, decimals: 0})`: Erzeugt einen Zahlenformatierer (macht z. B. aus der Zahl `1` den String `"G01"`).
* `createVariable({prefix: "X"}, xyzFormat)`: Erzeugt eine **modale Variable (Ausgabevariable, die ihren Wert speichert)**.
  * `xOutput.format(100)`: Gibt beim ersten Aufruf `"X100.000"` zurück. Wird direkt in der nächsten Zeile wieder `xOutput.format(100)` aufgerufen, gibt sie `""` (leerer Text) zurück, weil sich die X-Position nicht geändert hat!
  * `xOutput.reset()`: Zwingt die Variable dazu, beim nächsten Aufruf den Wert auf jeden Fall wieder auszugeben (extrem wichtig nach einem **Werkzeugwechsel `M06`**!).
* `createModal({}, gFormat)`: Speichert den aktiven **G-Code einer Gruppe** (z. B. Bewegungsgruppe `G00`/`G01`/`G02`/`G03`), damit er nicht unnötig in jeder Zeile wiederholt wird.

### Werkzeug- und Operationsdaten auslesen
* `tool.number`: Die Magazin-Nummer des aktuellen Werkzeugs (z. B. `1` für `T01`).
* `tool.diameter`: Der Durchmesser des Fräsers oder Bohrers (z. B. `10.0` mm).
* `tool.cornerRadius`: Der Eckenradius bei Torusfräsern (Schaftfräser mit abgerundeten Ecken).
* `tool.lengthOffset`: Die Registernummer für die **Werkzeuglängenkorrektur (`H`-Nummer)**.
* `tool.diameterOffset`: Die Registernummer für die **Werkzeugradiuskorrektur (`D`-Nummer)**.
* `tool.description` / `tool.comment`: Beschreibungstext des Werkzeugs aus der **CAM-Werkzeugbibliothek (Tool Library)**.
* `spindleSpeed`: Die aktuelle **Spindeldrehzahl (`S` in Umdrehungen pro Minute)**.
* `currentSection.workOffset`: Der gewählte **Werkstück-Nullpunkt (`1` = `G54`, `2` = `G55`, usw.)**.
* `getToolTable()`: Gibt eine Liste aller im gesamten Programm verwendeten Werkzeuge zurück (ideal für die Werkzeugübersicht in `onOpen()`).

---

## 3. Wichtiger Hinweis für offizielle Handbücher im Ordner `docs/`
Legen Sie in diesem Ordner (`C:\Projekte\CNC\docs\`) folgende **PDF-Dateien (Portable Document Format)** ab, sobald Sie sie heruntergeladen haben:
1. **`autodesk_post_guide.pdf`**: Das offizielle *Autodesk Fusion Post Processor Training Guide* (`https://cam.autodesk.com/posts/posts/guides/Post%20Processor%20Training%20Guide.pdf`).
2. **`maschinen_handbuch.pdf`**: Bei Kundenaufträgen das jeweilige Programmierhandbuch der Zielmaschine (z. B. *Haas Mill Operator's Manual*, *Siemens Sinumerik Programmierhandbuch* oder *Heidenhain TNC Klartext-Handbuch*).
