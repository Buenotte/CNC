# 🛠️ Vollständige Anleitung: Der Kunden-Postprozessor-Generator (Web-Interface & Terminal)

Dieses Dokument erklärt Ihnen Schritt für Schritt und in einfacher, bildhafter Sprache, wie Sie mit unserem neuen **Kunden-Postprozessor-Generator *(CPS-Generator / Konfigurator)*** aus beliebigen Kundenwünschen in wenigen Sekunden eine fertige, fehlerfreie **`.cps`-Datei *(Postprozessor / Übersetzer für Autodesk Fusion 360)*** erzeugen.

---

## 💡 1. Worum geht es in einfacher Sprache? (Das Grundprinzip)

### Was ist eine `.cps`-Datei wirklich?
Viele Einsteiger glauben, eine `.cps`-Datei sei ein kompliziertes, kompiliertes Maschinenprogramm. Das ist falsch!
* **CPS** steht für: **C**AM **P**ostprocessor **S**cript *(CAM-Postprozessor-Skript)*.
* Eine `.cps`-Datei ist in Wahrheit eine **ganz normale Textdatei mit JavaScript-Code**!
* **Der Büro-Drucker-Vergleich:**
  * Das 3D-Modell des Kunden (`.step` oder `.stl`) ist wie ein **Word-Dokument** *(Textinhalt)*.
  * Die Fräsmaschine in der Werkshalle ist wie der **Drucker** *(Hardware)*.
  * Die `.cps`-Datei ist der **Druckertreiber** *(Übersetzer)*!
  * Die `.nc`-Datei *(G-Code)* ist das **ausgedruckte Blatt Papier**.

Bisher musste man diesen JavaScript-Code mühsam mit der Hand Zeile für Zeile tippen oder anpassen.  
Unser neues Programm nimmt Ihnen diese Arbeit zu **100 % ab**!

---

## 🖥️ 2. Weg A: Das grafische Web-Interface (`kunden_cps_generator_web.html`)

Das Web-Interface ist der **bequemste Weg**. Sie bedienen das Programm wie einen modernen Online-Konfigurator mit der Maus im Webbrowser.

### 🚀 So starten Sie das Web-Interface:
* Öffnen Sie per Doppelklick die Datei:  
  👉 [`kunden_cps_generator_web.html`](file:///C:/Projekte/CNC/kunden_cps_generator_web.html)  
  *(funktioniert offline in jedem Browser: Google Chrome, Microsoft Edge, Mozilla Firefox)*.

---

### 🖱️ Die 4 Eingabebereiche Schritt für Schritt erklärt:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ DIE 4 FORMULAR-BEREICHE IM WEB-INTERFACE                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
  1. KUNDEN- & ENTWICKLERDATEN   --> Wer gibt den Auftrag? Wer programmiert?
  2. MASCHINEN-STEUERUNG         --> Haas, Siemens, Fanuc oder Heidenhain?
  3. SICHERHEITS-FEATURES        --> Z-MIN Crash-Schutz, Tool Table, Tisch zur Tür?
  4. KÜHLMITTEL-STEUERUNG        --> Standard M08 oder Hochdruck-Innenkühlung M88?
```

#### 1. Kunden- & Entwicklerdaten:
* **Kundenname / Firma:** Tragen Sie den Namen Ihres Kunden ein *(z. B. `Zerspanungstechnik Schmidt GmbH`)*. Dieser Name erscheint automatisch in allen Kopfzeilen des fertigen G-Codes!
* **Ihr Entwickler-Name:** Ihr Name oder der Name Ihres Ingenieurbüros *(z. B. `Dipl.-Ing. CNC-Büro`)*. Das beweist Ihre Urheberschaft und schützt Sie rechtlich.
* **Programmnummer & Kommentar:** z. B. `1001` und `KUNDENAUFTRAG FLANSCHPLATTE OP10`.

#### 2. Maschinen-Steuerung *(Die 4 großen Industriestandards auf Knopfdruck)*:
Jede CNC-Maschine „spricht“ einen etwas anderen Dialekt. Wählen Sie einfach die passende Kachel an:

| Kachel | Steuerung | Was der Generator automatisch in die `.cps` einbaut: |
|:---|:---|:---|
| 🟡 **Haas NGC** | Haas Automation *(USA-Standard)* | Sicherheitszeile `G90 G21 G17 G40 G49 G80`, Werkzeugwechsel `T01 M06`, Werkzeuglängenkorrektur `G43 H01`, Tisch freifahren mit `G53 Z0 Y0`. |
| 🔵 **Siemens 840D** | Sinumerik 840D / 828D *(Deutscher Standard)* | Sicherheitszeile `G90 G71 G17 G40 G64` *(metrischer Modus mit Glättung)*, Werkzeugaufruf `T="NAME" M06 D1`, Absolutes Maschinenfreifahren mit `SUPA G00 Z0 D0`. |
| 🔴 **Fanuc 0i-MF** | Fanuc *(Weltweiter ISO-Standard)* | Klassischer DIN/ISO-Code, extrem kompatibel mit fast allen asiatischen und europäischen Fräsmaschinen. |
| 🟢 **Heidenhain** | TNC 640 / iTNC 530 *(Klartext-Dialog)* | Klartext-Syntax: `TOOL CALL 1 Z S8000`, Verfahrbefehle mit `L X... Y... R0 FMAX`, Freifahren mit Maschinen-Bezug `M91`. |

#### 3. Die 4 Sicherheits- & Komfortfunktionen *(Schalter / Checkboxen)*:
* ☑️ **Automatische Z-MIN Tiefenprüfung *(Schraubstock-Kollisionsschutz)***:  
  Aktiviert unsere mathematische Z-MIN-Schleife aus Übung 3. Der Postprozessor ermittelt die tiefste Koordinate und druckt sie in den Programmkopf, damit der Fräser an der Maschine niemals in den Schraubstock kracht!
* ☑️ **Werkzeugtabelle *(Tool Table)***:  
  Listet im Programmkopf alle Werkzeuge mit Nummer, Durchmesser, Z-MIN und Typ auf. Der Maschinenbediener sieht morgens in 10 Sekunden, welche Fräser er ins Magazin stecken muss.
* ☑️ **Operations-Info vor jedem Einzelschnitt**:  
  Druckt vor jeder Kontur `(SICHERHEITS-INFO: OP Z-MIN=... | OP Z-MAX=...)` in den G-Code.
* ☑️ **Tisch am Programmende zur Tür fahren (`G53 Y0` / `SUPA Y0`)**:  
  Der Maschinentisch fährt nach getaner Arbeit automatisch nach ganz vorne an die geöffnete Glasscheibe. Der Arbeiter muss sich nicht in die nasse Maschine beugen, um das schwere Werkstück herauszuheben.

#### 4. Kühlmittel-Steuerung:
* **`M08` *(Standard Flutkühlung)***: Normale Schmiermitteldusche von außen über flexible Gelenkschläuche.
* **`M88` *(IKZ – Innenkühlmittelzufuhr mit 70 bar)***: Spritzt das Wasser unter Hochdruck direkt durch den Kern des Bohrers *(wichtig für tiefe Bohrungen und hitzeempfindliche Legierungen)*.
* **`M07` *(MMS – Minimalmengenschmierung)***: Bläst einen feinen Öl-Luft-Nebel *(Aerosol)* auf die Fräserschneide.

---

### 👁️ Die Live-Vorschau & der 1-Klick-Download:

Auf der rechten Bildschirmseite sehen Sie zwei Reiter:
1. **Reiter 1: `📄 Generierte .cps Datei`**:  
   Hier sehen Sie in Echtzeit den vollständigen, sauberen JavaScript-Code der `.cps`-Datei. Jedes Mal, wenn Sie links einen Haken setzen oder die Maschine wechseln, passt sich der Code in einer Millisekunde an!
2. **Reiter 2: `🤖 G-Code Simulation`**:  
   Hier sehen Sie eine Vorschau des Maschinencodes, den dieser Postprozessor erzeugen wird *(inklusive Sicherheitszeile, Werkzeugliste und Lead-In-Anfahrschnitt)*!

#### 📥 Der Download:
Klicken Sie oben rechts auf den blauen Button **„📥 .cps-Datei herunterladen“**.  
Ihr Browser speichert die fertige Datei *(z. B. `schmidt_haas.cps`)* sofort ab – fertig zum Einsatz in Autodesk Fusion 360!

---

## ⚡ 3. Weg B: Das Terminal-Programm (`scripts/kunden_cps_generator.js`)

Wenn Sie lieber in der Konsole *(Terminal)* arbeiten oder die Erstellung vollautomatisch über Skripte steuern möchten, nutzen Sie unser Node.js-Skript:

* **Datei:** [`scripts/kunden_cps_generator.js`](file:///c:/Projekte/CNC/scripts/kunden_cps_generator.js)

### Die 2 Befehle im Terminal:

#### Befehl 1: Schneller Demo-Lauf (1 Sekunde)
```powershell
node scripts/kunden_cps_generator.js --demo
```
* Erzeugt sofort eine Muster-`.cps`-Datei für eine Haas-Maschine.
* Startet im Hintergrund automatisch unser Prüfskript [`tests/simuliere_post.js`](file:///C:/Projekte/CNC/tests/simuliere_post.js) und testet, ob der G-Code 100 % fehlerfrei kompiliert!

#### Befehl 2: Aus einer JSON-Auftragsdatei erzeugen
Sie können die Kundenwünsche in einer kleinen Textdatei speichern, z. B. [`kundenauftrag_beispiel.json`](file:///c:/Projekte/CNC/kundenauftrag_beispiel.json):

```json
{
  "kundenName": "Mueller Praezisionsteile GmbH",
  "entwicklerName": "Dipl.-Ing. CNC-Büro",
  "steuerungsTyp": "siemens",
  "programmNummer": 2002,
  "programmKommentar": "VENTILBLOCK OP10",
  "features": {
    "zMinBerechnung": true,
    "opZMinInfo": true,
    "werkzeugTabelle": true,
    "tischZurTuer": true,
    "kuehlmittelTyp": "M88"
  },
  "ausgabeDatei": "siemens_ventilblock_post.cps"
}
```

Befehl zum Erzeugen:
```powershell
node scripts/kunden_cps_generator.js kundenauftrag_beispiel.json
```
Das Programm liest die JSON-Datei ein, generiert [`uebungen/siemens_ventilblock_post.cps`](file:///C:/Projekte/CNC/uebungen/siemens_ventilblock_post.cps) und führt sofort die automatische Simulation aus!

---

## 📥 4. Wie binden Sie die generierte `.cps`-Datei in Autodesk Fusion 360 ein?

Sobald Sie die `.cps`-Datei heruntergeladen oder erzeugt haben, binden Sie sie in **3 einfachen Schritten** in Fusion 360 ein:

1. **In den Fräsmodus wechseln:**  
   Öffnen Sie Ihr 3D-Modell in Fusion 360 und schalten Sie oben links auf **`Fertigen (Manufacture)`**.
2. **Postprozessor-Fenster öffnen:**  
   Klicken Sie oben auf das Symbol **`NC-Programm / Postprozess`** *(Tastaturkürzel: `Strg + P`)*.
3. **Eigene `.cps`-Datei auswählen:**  
   * Klicken Sie bei **„Post-Konfiguration *(Post)*“** auf das kleine **Ordner-Symbol 📁** *(„Bibliothek öffnen / Open Library“)*.
   * Wählen Sie links den Reiter **„Lokal / Persönliche Posts *(Personal Posts)“***.
   * Wählen Sie Ihre heruntergeladene `.cps`-Datei aus *(z. B. `schmidt_haas.cps`)*.
4. **Auf „Postprozessieren (Post)“ klicken:**  
   Fertig! Fusion 360 erzeugt in einer Sekunde die fertige Maschinendatei (`.nc` oder `.mpf`) für die Werkstatt!

---

## 💼 5. Wie verdienen Sie damit als CAM-Ingenieurbüro Geld?

Dieses Tool ist Ihr persönlicher **Produktivitäts-Turbo**:

1. **Standard-Lohnprogrammierung (80 € bis 350 € pro Teil):**  
   Ein Kunde schickt Ihnen ein 3D-Modell und sagt: *„Ich habe eine Siemens 840D Maschine.“*  
   Sie öffnen [`kunden_cps_generator_web.html`](file:///c:/Projekte/CNC/kunden_cps_generator_web.html), klicken auf „Siemens“, laden die `.cps` herunter, lassen sie in Fusion über das 3D-Teil laufen und schicken dem Kunden in 15 Minuten das fertige CNC-Programm samt Einrichteblatt.
2. **Verkauf maßgeschneiderter Postprozessoren (1.500 € bis 4.000 € einmalig):**  
   Ein metallverarbeitender Betrieb kauft sich eine neue CNC-Fräsmaschine und findet bei Autodesk keinen Postprozessor, der den Maschinentisch zur Tür fährt und die Werkzeugtabelle sauber darstellt.  
   Sie konfigurieren ihm über unser Tool die perfekte `.cps`-Datei, fügen seinen Firmennamen ein, testen sie – und stellen ihm die fertige Postprozessor-Datei in Rechnung!

---

## 📚 6. Glossar der wichtigsten Fachbegriffe

* **`.cps` *(CAM Postprocessor Script)*:** Eine JavaScript-Textdatei, die als Übersetzer zwischen dem 3D-CAM-System *(Autodesk Fusion 360)* und der echten Fräsmaschine dient.
* **G-Code *(Maschinencode / .nc / .mpf / .h)***: Die vom Postprozessor erzeugte Textdatei mit Koordinaten (`X... Y... Z...`) und Schaltbefehlen (`M03`, `M08`), die der Computer der Fräsmaschine Satz für Satz abarbeitet.
* **`Z-MIN` *(Tiefste Frästiefe)***: Die tiefste Koordinate, die ein Werkzeug während der gesamten Bearbeitung erreicht. Lebenswichtig zur Vermeidung von Kollisionen mit dem Maschinenschraubstock!
* **Lead-In *(Schnittanfahrt)***: Das gezielte Einfahren des Fräsers mit geregeltem Arbeitsvorschub (`G01`) aus der freien Luft in das überstehende Rohteilmaterial zur Vermeidung von Eilgang-Crashes.
* **IKZ *(Innenkühlmittel-Zufuhr)***: Hochdruckkühlung, bei der das Kühlmittel mit bis zu 70 bar direkt durch Bohrungen im Inneren des Fräsers oder Bohrers an die Schneide gepumpt wird.
* **`G53` / `SUPA` *(Maschinen-Koordinatensystem)***: Befehle, die Achsen nicht relativ zum Werkstück, sondern bezogen auf den festen Maschinenrahmen verfahren *(z. B. Spindel nach ganz oben oder Tisch nach ganz vorne zur Tür)*.
