# Komplette Anleitung zum Berufseinstieg als CNC-Postprozessor-Entwickler (Entwickler für Übersetzungsprogramme von Konstruktionsdaten in Maschinensprache) & Technischer Implementierungsplan (Umsetzungsplan)

Dieses Dokument basiert auf Ihrer Datei [doc.txt](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/doc.txt) und erweitert diese zu einem vollständigen Karriere-Fahrplan (Berufseinstiegs-Leitfaden), einer konkreten Handlungsanweisung („Was soll ich jetzt tun?“) sowie einem detaillierten Software- und Implementierungsplan (Plan zur technischen Einrichtung und Umsetzung).

---

## Teil 1: Was steht in der `doc.txt` und was ist Ihre Rolle?

In Ihrer Datei [doc.txt](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/doc.txt) wird beschrieben, wie Sie als Softwareentwickler mit Kenntnissen in **JavaScript (skriptbasierte Programmiersprache)** und **KI (Künstlicher Intelligenz)** in eine extrem gefragte und hochbezahlte Nische der Fertigungsindustrie einsteigen: die Entwicklung von **CNC-Postprozessoren (Übersetzungsprogrammen für computergesteuerte Werkzeugmaschinen)**.

### Das Grundprinzip des Berufs einfach erklärt:

1. **CAD (Computer-Aided Design / Computergestützte Konstruktion):** Ein Ingenieur zeichnet ein 3D-Bauteil (dreidimensionales Werkstückmodell) am Computer.
2. **CAM (Computer-Aided Manufacturing / Computergestützte Fertigung):** Eine Software wie **Autodesk Fusion 360 (integrierte Cloud-Software für Konstruktion und Fertigung)** berechnet die Werkzeugwege (Fräsbahnen oder Bohrwege) als neutrale mathematische Koordinaten (**CL-Data / Cutter Location Data – neutrale Werkzeugpositionsdaten im Raum mit X-, Y- und Z-Vektoren**).
3. **Postprozessor (Nachbearbeitungs- bzw. Übersetzungsprogramm / Compiler für Werkzeugmaschinen):** Hier kommen Sie ins Spiel! Jede **CNC-Maschine (Computerized Numerical Control – computergesteuerte Werkzeugmaschine wie Fräse oder Drehmaschine)** spricht einen eigenen Dialekt. Ihr **Postprozessor (in JavaScript geschriebene `.cps`-Datei)** liest die neutralen Daten aus der **CAM-Software (Fertigungssoftware)** und übersetzt sie exakt in den spezifischen **G-Code (standardisierte Steuerungs- und Maschinensprache nach ISO/DIN-Norm)** oder Herstellercode für Steuerungen wie:
   - **Haas NGC (Next Generation Control – moderne Maschinensteuerung des US-Herstellers Haas Automation)**
   - **Fanuc (weltweit verbreitete japanische CNC-Maschinensteuerung)**
   - **Siemens Sinumerik (industrielle CNC-Steuerung der Firma Siemens)**
   - **Heidenhain Klartext (dialogorientierte Steuerungssprache des Herstellers Heidenhain)**
   - **Mazak Mazatrol (Steuerungssystem des japanischen Maschinenbauers Yamazaki Mazak)**

---

## Teil 2: Welche Software muss installiert werden? (Komplette Checkliste)

Um professionell als **CNC-Postprozessor-Entwickler (Entwickler für Maschinen-Übersetzungsskripte)** auf Ihrem **ThinkPad (Laptop-Modellreihe von Lenovo)** zu arbeiten, benötigen Sie folgende Software-Komponenten (Programme und Erweiterungen):

### 1. Pflicht-Software für den sofortigen Start (Kostenlos)

| Software / Tool (Werkzeug)                                                                                                                                         | Zweck & Erklärung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Installations-Quelle / Befehl                                                                                                                                                                                       |
|:------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Antigravity IDE (Integrated Development Environment / Integrierte Entwicklungsumgebung)** oder **VS Code (Visual Studio Code – Quelltext-Editor von Microsoft)** | Ihre Haupt-Arbeitsumgebung zum Schreiben, Analysieren und Testen des **JavaScript-Codes (Programmcode in der Sprache JavaScript)**. Antigravity IDE nutzen Sie bereits aktiv!                                                                                                                                                                                                                                                                                                                                                               | Bereits auf Ihrem System installiert.                                                                                                                                                                               |
| **Autodesk Fusion Post Processor Utility (Offizielle Erweiterung / Extension für die Entwicklungsumgebung)**                                                       | Das wichtigste **Plugin (Zusatzmodul)** überhaupt. Es bietet **IntelliSense (automatische Code-Vervollständigung und Parameter-Hilfe)** für die **Autodesk Post-API (Application Programming Interface – Programmierschnittstelle für Postprozessoren)**, **Inline-Debugging (Fehlersuche direkt im Code)** und eine eingebaute **Post-Engine (`post.exe` – lokales Ausführungsprogramm)**, mit der Sie `.cps`-Dateien (JavaScript-Postprozessordateien) direkt ohne echte CNC-Maschine und sogar ohne geöffnetes Fusion 360 testen können! | Im **Extensions-Marktplatz (Erweiterungs-Verzeichnis)** Ihrer IDE nach `Autodesk Fusion Post Processor Utility` suchen (Interne Kennung: `Autodesk.hsm-post-processor`) und auf **Install (Installieren)** klicken. |
| **Node.js (JavaScript-Laufzeitumgebung außerhalb des Browsers)**                                                                                                   | Hilfreich für lokale Hilfsskripte, **Linter (Programme zur automatischen Code-Qualitätsprüfung)** und Paketverwaltung über **npm (Node Package Manager – Paketverwaltung für JavaScript)**.                                                                                                                                                                                                                                                                                                                                                 | Über `winget install OpenJS.NodeJS.LTS` in der **PowerShell (Befehlszeilen-Konsole von Windows)** oder über `nodejs.org`.                                                                                           |
| **Git (Versionsverwaltungssystem für Quellcode)**                                                                                                                  | Unverzichtbar, um jede Änderung am **Postprozessor (Übersetzungsskript)** revisionssicher zu speichern (da ein falscher Befehl an einer echten Maschine zu einem **Maschinencrash / Kollision des Werkzeugs mit dem Werkstück** führen kann).                                                                                                                                                                                                                                                                                               | Über `winget install Git.Git` oder `git-scm.com`.                                                                                                                                                                   |
| **NCViewer (Webbasierter G-Code-Simulator)** oder **CIMCO Edit (Professioneller G-Code-Editor und Backplotter)**                                                   | Ein **Backplotter (Werkzeugweg-Visualisierer)** liest den von Ihrem JavaScript erzeugten **G-Code (Maschinencode)** und zeichnet die Fahrwege des Fräsers in 3D auf den Bildschirm. So sehen Sie sofort visuell, ob Ihre Programmierung funktioniert.                                                                                                                                                                                                                                                                                       | Kostenlos im Browser unter `ncviewer.com` nutzbar. Für Desktop-Simulation alternativ **CAMotics (Open-Source-3D-CNC-Simulator)**.                                                                                   |

### 2. Empfohlene Zusatz-Software für Fortgeschrittene & Kundenprojekte

| Software / Tool (Werkzeug)                                                   | Zweck & Erklärung                                                                                                                                                                                                                                                                       | Lizenzmodell                                                                                              |
|:---------------------------------------------------------------------------- |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |:--------------------------------------------------------------------------------------------------------- |
| **Autodesk Fusion (ehemals Fusion 360 – CAD/CAM-Komplettsoftware)**          | Damit können Sie eigene **3D-Modelle (dreidimensionale Bauteile)** erstellen, **CAM-Werkzeugwege (Frässtrategien)** anlegen und eigene `.cnc`-Zwischendateien (**Intermediate Files – neutrale Testdaten für das Debugging**) exportieren.                                              | Kostenlose **Personal Use License (Lizenz für nicht-kommerzielle/private Nutzung zum Lernen)** verfügbar. |
| **WinMerge (Programm zum Dateivergleich / Diff-Tool)** oder IDE-Diff-Ansicht | Vergleicht den alten **G-Code (Maschinenprogramm)** mit dem neu generierten G-Code Zeile für Zeile, um sicherzustellen, dass Änderungen am **Postprozessor (Übersetzungsskript)** keine unbeabsichtigten Nebeneffekte haben (**Regressionstest – Prüfung auf eingeschlichene Fehler**). | Kostenlos (**Open Source – quelloffene Software**).                                                       |
| **Hersteller-Simulatoren (Virtuelle CNC-Steuerungen)**                       | Später für hochbezahlte Aufträge: **Heidenhain Programmierplatz (virtuelle Steuerung für Heidenhain TNC)** oder **Siemens SinuTrain (Simulationssoftware für Sinumerik-Steuerungen)**.                                                                                                  | Kostenlose Demo-/Trainingsversionen bei den Maschinenherstellern verfügbar.                               |

---

## Teil 3: Was sollen Sie JETZT konkret machen? (Schritt-für-Schritt-Aktionsplan)

Sie befinden sich bereits im richtigen Arbeitsverzeichnis `C:\Projekte\CNC`. So setzen wir die Anweisungen aus der [doc.txt](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/doc.txt) jetzt sauber in die Tat um:

### Schritt 1: Projektstruktur in `C:\Projekte\CNC` anlegen

Wir erstellen direkt hier in `C:\Projekte\CNC` die professionelle Ordnerstruktur aus Ihrer Vorlage:

```text
C:\Projekte\CNC\
├── doc.txt                                              # Ihre ursprüngliche Notizdatei (bleibt unverändert!)
├── ANLEITUNG_BERUFSEINSTIEG_UND_IMPLEMENTATION_PLAN.md  # Dieser vollständige Leitfaden & Plan
├── docs/                                                # Wissensdatenbank & Handbücher für die KI (Künstliche Intelligenz)
│   └── autodesk_post_guide.pdf                          # Offizielles Autodesk Post Processor Training Guide (Handbuch)
├── src/                                                 # Quellcode-Ordner (Source Code) für Ihre Postprozessoren
│   ├── mein_erster_post.cps                             # Ihr erster Übungs-Postprozessor (z. B. Haas NGC oder Fanuc)
│   └── config.json                                      # Konfigurationsdatei für benutzerdefinierte Einstellungen
├── tests/                                               # Testumgebung für Simulation und Qualitätssicherung
│   ├── sample_cam_data.cnc                              # Neutrale CAM-Zwischendatei (Intermediate File) zum Testen
│   └── output_expected.nc                               # Erwarteter G-Code-Output (Soll-Ergebnis)
└── README.md                                            # Projektdokumentation für Sie und zukünftige Kunden
```

### Schritt 2: Das offizielle Plugin (Zusatzmodul) installieren

1. Klicken Sie links in der Seitenleiste Ihrer **Antigravity IDE (Entwicklungsumgebung)** auf das Symbol für **Extensions (Erweiterungen / Vier-Quadrate-Icon)** oder drücken Sie die Tastenkombination `Strg + Umschalt + X`.
2. Geben Sie in das Suchfeld ein: `Autodesk Fusion Post Processor Utility`.
3. Klicken Sie auf **Install (Installieren)**.
4. **Wichtiger Bonus dieses Plugins:** Sobald Sie dieses Plugin installiert haben, bringt es automatisch **Beispiel-CAM-Dateien (`.cnc` Benchmark-Dateien)** mit! Sie brauchen also am Anfang noch nicht einmal zwingend Autodesk Fusion 360 installiert zu haben, um echten **G-Code (Maschinencode)** zu generieren.

### Schritt 3: Den ersten echten Postprozessor (`haas next generation.cps` oder `fanuc.cps`) und das Handbuch herunterladen

1. **Postprozessor-Vorlage holen:**
   - Öffnen Sie im Webbrowser die offizielle **Autodesk Post Library (Bibliothek für Postprozessoren)**: `https://cam.autodesk.com/hsmposts`
   - Suchen Sie nach `Haas Next Generation` (oder `Fanuc`).
   - Laden Sie die Datei `.cps` (**CAM Post Script – JavaScript-basierte Postprozessordatei**) herunter und speichern Sie sie unter `C:\Projekte\CNC\02_Software_und_Tools\src\mein_erster_post.cps`.
2. **Offizielles API-Handbuch (Dokumentation der Programmierschnittstelle) holen:**
   - Laden Sie das offizielle **Autodesk Post Processor Training Guide (PDF-Handbuch)** herunter (direkt bei Autodesk verfügbar unter `https://cam.autodesk.com/posts/posts/guides/Post%20Processor%20Training%20Guide.pdf`).
   - Speichern Sie die **PDF-Datei (Portable Document Format – plattformübergreifendes Dokumentenformat)** im Ordner `C:\Projekte\CNC\03_Fachdokumentation_und_Wissen\docs\autodesk_post_guide.pdf`.

### Schritt 4: Die erste Code-Änderung (`onOpen()`-Funktion) durchführen und testen

In jedem **Autodesk-Postprozessor (`.cps`-Skript)** gibt es feste **Einstiegspunkte (Callback-Funktionen / Ereignisfunktionen)**, die während der Übersetzung automatisch aufgerufen werden:

- `onOpen()`: Wird ganz am Anfang aufgerufen, wenn die **G-Code-Datei (Ausgabedatei)** geöffnet wird. Hier schreibt man den **Programm-Header (Kopfbereich mit Metadaten, Datum, Entwicklername, Sicherheitsbefehlen wie `G90` für Absolutmaß und `G21` für metrische Einheiten in Millimetern)**.
- `onSection()`: Wird für jeden einzelnen Bearbeitungsschritt (z. B. Planfräsen, Taschenfräsen, Bohren) aufgerufen. Hier passieren der **Werkzeugwechsel (`M06`)**, das Einschalten der **Spindeldrehzahl (`S... M03`)** und die **Kühlmittelsteuerung (`M08`)**.
- `onLinear(x, y, z, feed)` / `onRapid(x, y, z)`: Wird für jede geradlinige Fräsbewegung (`G01` mit **Vorschubgeschwindigkeit / Feedrate `F`**) oder Eilgangbewegung (`G00` – maximale Verfahrgeschwindigkeit im Freiraum) aufgerufen.
- `onCircular(clockwise, cx, cy, cz, x, y, z, feed)`: Wird für Kreisbögen (`G02` im Uhrzeigersinn / `G03` gegen den Uhrzeigersinn) aufgerufen.
- `onCycle()` / `onCyclePoint(x, y, z)`: Wird für **Festzyklen (Canned Cycles – vordefinierte Maschinenroutinen wie Tiefbohren `G83` oder Gewindebohren `G84`)** aufgerufen.
- `onClose()`: Wird ganz am Ende des Programms aufgerufen (schaltet Spindel mit `M05` und Kühlmittel mit `M09` aus, fährt in die sichere Parkposition mit `G28` oder `G53` und beendet das Programm mit `M30`).

---

## Teil 4: Anleitung für den Berufseinstieg (Vom JavaScript-Entwickler zum gefragten CNC-Postprozessor-Experten)

### Warum ist dieser Beruf für Sie als JavaScript-Entwickler mit KI-Kenntnissen (Künstliche Intelligenz) eine Goldgrube?

In der Industrie gibt es ein massives Problem (**Fachkräftemangel an der Schnittstelle IT / Maschinenbau**):

- Klassische **CNC-Zerspanungsmechaniker (Maschinenbediener an Fräs- und Drehmaschinen)** kennen zwar **G-Code (Maschinensprache)**, können aber meistens kein komplexes **JavaScript (Programmiersprache)** programmieren.
- Klassische **Web-Entwickler (Programmierer für Internetanwendungen)** beherrschen zwar **JavaScript (Programmiersprache)**, haben aber Angst vor Begriffen wie **Spindeldrehzahl (Umdrehungen pro Minute des Werkzeugs)**, **Werkzeuglängenkorrektur (`G43 H...` – Anpassung an die reale Länge des Fräsers)** oder **5-Achs-Kinematik (gleichzeitige Bewegung in 3 Raumachsen X/Y/Z und 2 Drehachsen A/B oder B/C)**.
- **Ihre Chance:** Mit **Gemini (KI-Sprachmodell von Google)** in **Antigravity IDE (Entwicklungsumgebung)** überbrücken Sie das fehlende Maschinenbau-Wissen in Sekunden, während Sie Ihre **Software-Engineering-Fähigkeiten (systematische Softwareentwicklung)** nutzen, um sauberen, wartbaren und fehlerfreien JavaScript-Code zu liefern!

### Die 4 Stufen zum Berufseinstieg (Karriere-Roadmap / Entwicklungsplan)

#### Stufe 1: Grundlagen & Architektur verstehen (Woche 1–2)

1. **Verstehen der `.cps`-Struktur (Aufbau einer Postprozessor-Datei):**
   - Kopfzeilen-Metadaten (`description`, `vendor`, `certificationLevel`, `extension`).
   - **Properties (Benutzereigenschaften):** Das Objekt `properties` definiert einstellbare Optionen, die der **CAM-Programmierer (Anwender in Fusion 360)** beim Exportieren per Häkchen oder Dropdown-Menü auswählen kann (z. B. `showSequenceNumbers` für Zeilennummern `N10, N20...` oder `useG28` für Referenzpunktfahrt).
   - **Format-Definitionen (`createFormat`, `createVariable`):** Wie Zahlen gerundet werden (z. B. 3 Nachkommastellen für Millimeter `0.001`), damit die Steuerung keinen **Syntaxfehler (Formatierungsfehler)** meldet.
2. **Die wichtigsten 10 G-Codes (Wegbefehle) und M-Codes (Zusatzfunktionen / Miscellaneous Functions) kennenlernen:**
   - `G00`: **Eilgang (Rapid Move)** – schnelle Positionierung ohne Materialabtrag (niemals im Material!).
   - `G01`: **Geradeninterpolation (Linear Move)** – Fräsen in einer geraden Linie mit definiertem **Vorschub (`F` in Millimeter pro Minute)**.
   - `G02` / `G03`: **Kreisinterpolation (Circular Move)** – Fräsen im Uhrzeigersinn (`G02`) oder gegen den Uhrzeigersinn (`G03`).
   - `G17` / `G18` / `G19`: **Ebenenauswahl (Plane Selection)** – `G17` ist die Standard-XY-Ebene beim vertikalen Fräsen.
   - `G20` / `G21`: **Maßeinheit (Units)** – `G20` = Zoll (Inch), `G21` = Metrisch (Millimeter).
   - `G40` / `G41` / `G42`: **Werkzeugradiuskorrektur (Cutter Compensation)** – die Steuerung verrechnet den Radius des Fräsers automatisch nach links (`G41`), rechts (`G42`) oder schaltet sie aus (`G40`).
   - `G54` bis `G59`: **Nullpunktverschiebung (Work Coordinate System / WCS)** – legt fest, wo der Koordinaten-Ursprung `(X0, Y0, Z0)` auf dem realen Werkstück im Schraubstock liegt.
   - `G90` / `G91`: **Absolutmaß (`G90` – Koordinaten beziehen sich immer auf den Nullpunkt)** vs. **Kettenmaß / Inkrementalmaß (`G91` – Koordinaten beziehen sich auf die letzte Position)**.
   - `M03` / `M04` / `M05`: **Spindelsteuerung** – Rechtslauf (`M03`), Linkslauf (`M04`), Spindel Stopp (`M05`).
   - `M06`: **Werkzeugwechsel (Tool Change)** in Verbindung mit `T...` (Werkzeugnummer).
   - `M08` / `M09`: **Kühlmittel (Coolant)** ein (`M08`) und aus (`M09`).
   - `M30`: **Programmende mit Rücksprung zum Programmanfang (End of Program & Rewind)**.

#### Stufe 2: Typische Kundenaufträge im 3-Achs-Bereich meistern (Woche 3–4)

Die meisten Einstiegs-Aufträge (im Wert von ca. 200 € bis 800 € pro Anpassung) sind gar keine kompletten Neuentwicklungen, sondern **Customizing (gezielte Anpassungen bestehender Standard-Postprozessoren)**:

- **Praxis-Fall 1 (Header & Werkzeugliste):** Der Kunde möchte ganz oben im **G-Code (Maschinenprogramm)** eine automatisch generierte Liste aller verwendeten Werkzeuge (Fräserdurchmesser, Eckenradius, minimale und maximale Frästiefe `Z-Min`), damit der **Maschinenbediener (Zerspaner)** sofort sieht, welche Werkzeuge er in die Maschine einbauen muss.
- **Praxis-Fall 2 (Sicherer Rückzug / Safe Retract):** Vor jedem Werkzeugwechsel soll der Tisch an eine ganz bestimmte Position an der Kabinentür fahren (z. B. `G53 G00 Z0` und danach `G53 G00 X-200 Y0`), damit der Bediener das Bauteil messen oder Späne wegblasen kann.
- **Praxis-Fall 3 (Spezielle M-Codes nachrüsten):** Eine Kundenmaschine hat eine nachträglich angebaute **Minimalmengenschmierung (MMS / Luft-Öl-Sprühnebel)** auf `M51` statt `M08` oder eine **Späneförderer-Steuerung (Förderband für Metallspäne)** auf `M62`. Sie fügen dafür eine Auswahloption (**Property**) im JavaScript-Code hinzu.

#### Stufe 3: Drehfräsen (Mill-Turn) und 3+2 / 5-Achs-Bearbeitung (Monat 2–3)

Hier steigen die Honorare stark an (oft 1.000 € bis 3.500 €+ pro Postprozessor):

- **3+2-Achsen (Positioniertes 5-Achs-Fräsen):** Die Drehachsen (z. B. Schwenktisch A und Rundtisch C) stellen das Werkstück schräg an, klemmen die Achsen fest (**Achsklemmung per M-Code**), und dann wird mit geschwenkter Arbeitsebene (z. B. `G68.2` bei Fanuc, `CYCLE800` bei Siemens oder `PLANE SPATIAL` bei Heidenhain) gefräst.
- **5-Achs-Simultanbearbeitung (Simultaneous 5-Axis):** Alle 5 Achsen bewegen sich gleichzeitig, während der **TCPM-Modus (Tool Center Point Management – automatische Nachführung der Werkzeugspitze durch die Steuerung, z. B. `G43.4` bei Fanuc, `TRAORI` bei Siemens, `M128` / `FUNCTION TCPM` bei Heidenhain)** aktiv ist.

#### Stufe 4: Kunden gewinnen & Positionierung am Markt (Ab Monat 2)

1. **Portfolio (Referenz-Sammlung) auf GitHub aufbauen:** Erstellen Sie ein öffentliches **GitHub-Repository (Online-Code-Archiv)** mit 3 bis 4 sauber dokumentierten Beispiel-Anpassungen (z. B. „Haas NGC Postprozessor mit erweiterter deutscher Werkzeugliste und automatischer Sicherheitsprüfung“).
2. **Zielgruppen ansprechen:**
   - Kleine und mittelständische **Lohnfertiger (Metallbearbeitungsbetriebe, die im Auftrag fräsen und drehen)** im deutschsprachigen Raum (**DACH-Region: Deutschland, Österreich, Schweiz**).
   - **Autodesk-Systemhäuser (Vertriebspartner für CAD/CAM-Software)** – diese suchen oft händeringend nach freien **Freelancern (selbstständigen Auftragnehmern)**, weil ihre eigenen Techniker mit Schulungen ausgelastet sind.
   - Plattformen wie **Upwork (internationale Freelancer-Plattform)**, **Freelancermap (deutsches IT- und Ingenieur-Projektportal)**, **LinkedIn (berufliches soziales Netzwerk)** und das offizielle **Autodesk Fusion HSM Post Processor Forum (Fachforum, in dem täglich Firmen nach Postprozessor-Anpassungen suchen)**.
3. **Sicherheits-Standard & Haftung (Wichtig für Profis):**
   - Liefern Sie jeden Postprozessor mit einem klaren **Abnahmeprotokoll (Test-Checkliste)** aus: Der erste Test an der echten Maschine muss immer im **Einzelsatz-Modus (Single Block – die Maschine führt jede G-Code-Zeile erst nach Knopfdruck einzeln aus)**, mit stark reduziertem **Vorschub-Override (Drehregler für die Geschwindigkeit auf 0 % bis 10 %)** und **in der Luft (Dry Run / Nullpunkt in Z um +100 mm nach oben verschoben, also weit über dem Schraubstock)** stattfinden!

---

## Teil 5: Technischer Implementierungsplan (Umsetzungsplan für Ihr Projekt in `C:\Projekte\CNC`)

Hier ist der konkrete, sofort ausführbare **Implementierungsplan (Phasenplan zur technischen Umsetzung)** für Ihr lokales Projekt:

### Phase 1: Projekt-Initialisierung & Verzeichnisaufbau (Heute – 10 Minuten)

- [ ] **Aufgabe 1.1:** Erstellen der Unterordner `docs/`, `src/` und `tests/` direkt in `C:\Projekte\CNC\`.
- [ ] **Aufgabe 1.2:** Anlegen einer `README.md` (Projektbeschreibung) und einer `src/config.json` (Konfigurationsdatei).
- [ ] **Aufgabe 1.3:** Anlegen einer funktionsfähigen Einsteiger-Postprozessor-Datei `src/mein_erster_post.cps` zum sofortigen Lernen (sowie Herunterladen des vollständigen `haas next generation.cps` und `fanuc.cps` aus der Autodesk Post Library).

### Phase 2: Tooling (Werkzeuge) & Dokumentation einbinden (Heute – 15 Minuten)

- [ ] **Aufgabe 2.1:** Installation der Erweiterung **Autodesk Fusion Post Processor Utility** in der **Antigravity IDE (Entwicklungsumgebung)**.
- [ ] **Aufgabe 2.2:** Ablegen des offiziellen **Autodesk Post Processor Training Guide (PDF-Handbuch)** unter `C:\Projekte\CNC\03_Fachdokumentation_und_Wissen\docs\autodesk_post_guide.pdf`.

### Phase 3: Erstes Entwicklungs-Feature – `onOpen()` modifizieren (Heute – 20 Minuten)

- [ ] **Aufgabe 3.1:** Analyse der Funktion `onOpen()` in `src/mein_erster_post.cps`.
- [ ] **Aufgabe 3.2:** Programmieren eines personalisierten **Entwickler-Infoblocks (Header-Kommentar im G-Code)** mittels der API-Funktion `writeComment(...)` (Schreibt einen für die CNC-Steuerung gültigen Kommentar in Klammern `(...)` oder mit Semikolon `;`), der automatisch:
  - Ihren Entwickler-Namen,
  - das aktuelle Generierungsdatum und die Uhrzeit (`new Date()`),
  - den Namen des Bauteils (`programName`),
  - und eine Übersicht der aktiven Sicherheitseinstellungen ausgibt.

### Phase 4: Simulation & Visuelle Prüfung (Heute – 15 Minuten)

- [ ] **Aufgabe 4.1:** Ausführen des Postprozessors über das **Autodesk Fusion Post Processor Utility (IDE-Erweiterung)** mit einer mitgelieferten **Benchmark-CAM-Datei (`.cnc` Testdatei)**.
- [ ] **Aufgabe 4.2:** Überprüfen der erzeugten **G-Code-Ausgabedatei (`.nc` oder `.tap` Datei)** im Editorfenster.
- [ ] **Aufgabe 4.3:** Kopieren des generierten **G-Codes (Maschinenprogramms)** in **NCViewer (`ncviewer.com` – 3D-Online-Simulator)** und visuelle Kontrolle der Fräsbahnen.

---

## Teil 6: Wichtige Unterscheidung – Wenn Sie ein 3D-Modell (dreidimensionales Bauteil) als Kundenauftrag bekommen!

Es gibt in der **CNC-Branche (computergesteuerte Fertigungsindustrie)** zwei eng verwandte, aber unterschiedliche Dienstleistungen. Es ist extrem wichtig, beide genau zu kennen – denn zusammen ergeben sie das lukrativste Geschäftsmodell:

### 1. Die zwei Auftrags-Arten im direkten Vergleich

| Merkmal                          | Auftrags-Typ A: Externer CAM-Programmierer (CNC-Programmierdienstleister)                                                                                                                                                                                          | Auftrags-Typ B: Postprozessor-Entwickler (JavaScript-Spezialist, wie in `doc.txt`)                                                                                                                                                      |
|:-------------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Was schickt Ihnen der Kunde?** | Ein **3D-Modell (dreidimensionale CAD-Datei im Format `.step`, `.stp`, `.iges` oder `.f3d`)** + eine **technische Zeichnung (`.pdf` mit Toleranzen und Gewindeangaben)** + eine Liste seiner vorhandenen Werkzeuge.                                                | Ein **Maschinen-Handbuch (Programmierhandbuch der Steuerung)** + ein **Muster-G-Code-Programm (Beispiel-Textdatei, die auf seiner Maschine läuft)**.                                                                                    |
| **Was ist Ihre Aufgabe?**        | Sie öffnen das **3D-Modell** in **Autodesk Fusion (CAD/CAM-Software)**, wählen Fräser und Bohrer aus, definieren die **Frässtrategien (z. B. Planfräsen, 2D-Tasche, 3D-Adaptiv-Schruppen)** und exportieren am Ende den fertigen **G-Code (`.nc`-Maschinencode)**. | Sie programmieren in **Antigravity IDE (Entwicklungsumgebung)** das **JavaScript-Übersetzungsprogramm (`.cps`-Datei)**, damit die CAM-Software überhaupt erst weiß, wie der G-Code für diese spezielle Maschine formatiert werden muss. |
| **Was liefern Sie dem Kunden?**  | 1. Den fertigen **G-Code (`.nc`-Datei)** für genau dieses eine Bauteil.<br>2. Ein **Einrichteblatt (Setup Sheet als PDF)**, auf dem steht, wo der Nullpunkt (`G54`) liegt und welche Fräser er einbauen muss.                                                      | Die fertige **`.cps`-Postprozessor-Datei (JavaScript-Compiler)**, mit der der Kunde ab sofort unendlich viele eigene Bauteile per Knopfdruck exportieren kann.                                                                          |
| **Wie oft zahlt der Kunde?**     | **Immer wieder (Wiederkehrend pro Bauteil):** Für jedes neue 3D-Bauteil, das der Kunde fertigen muss, bekommen Sie einen neuen Auftrag (oft **80 € bis 500 €+ pro Bauteil** je nach Komplexität).                                                                  | **Einmalig pro Maschine (Projektpreis):** Meist **300 € bis 2.500 €+** einmalig pro CNC-Maschine (plus spätere Änderungswünsche).                                                                                                       |

---

### 2. Der genaue Ablauf: Was Sie tun müssen, wenn Ihnen ein Kunde ein 3D-Modell schickt!

Wenn Ihr Ziel ist, **3D-Modelle (dreidimensionale Werkstück-Dateien)** als Auftrag anzunehmen und daraus fertigen **G-Code (Maschinenprogramme)** zu machen, sieht Ihr konkreter Arbeitsablauf (Workflow) in **6 Schritten** so aus:

#### Schritt 1: Auftragsdaten vom Kunden einsammeln (Checkliste)

Bevor Sie anfangen, brauchen Sie vom Kunden 4 Dinge:

1. **Das 3D-Modell:** Meist als **STEP-Datei (`.step` oder `.stp` – Standard for the Exchange of Product Model Data, das universelle Austauschformat für 3D-CAD-Modelle)**.
2. **Das Rohteil-Maß (Stock Size) & Material:** Woraus wird gefräst? (z. B. **Aluminium EN AW-6061**, **Baustahl S235** oder **Edelstahl V2A**) und wie groß ist der gesägte Metallblock (z. B. `100 x 60 x 25 mm`)?
   * *Warum wichtig?* In weichem Aluminium können Sie mit hoher **Spindeldrehzahl (`S` = z. B. 10.000 U/min)** und schnellem **Vorschub (`F` = z. B. 2000 mm/min)** fräsen. In hartem Edelstahl würde der Fräser bei diesen Werten sofort abbrechen (**Werkzeugbruch**)!
3. **Die Werkzeugliste des Kunden (Tool List):** Welche Fräser und Bohrer hat der Kunde in seiner Werkstatt? (z. B. Schaftfräser $\varnothing 10\text{ mm}$, Bohrer $\varnothing 6\text{ mm}$).
4. **Die genaue CNC-Maschine & Steuerung des Kunden:** Hat er eine **Haas VF-2**, eine **DMG MORI mit Siemens Sinumerik 840D** oder eine **Hermle mit Heidenhain TNC 640**?

#### Schritt 2: Das 3D-Modell in Autodesk Fusion (CAD/CAM-Software) öffnen

* Sie installieren **Autodesk Fusion (ehemals Fusion 360)** auf Ihrem Laptop.
* Sie importieren die **`.step`-Datei (das 3D-Modell des Kunden)** und wechseln oben links vom Arbeitsbereich **Konstruktion (Design / CAD)** in den Arbeitsbereich **Fertigen (Manufacture / CAM)**.

#### Schritt 3: Das Setup (Grund-Einrichtung & Nullpunkt) anlegen

* Sie erstellen im CAM-Bereich ein neues **Setup (Spann-Situation)**:
  * Sie legen die Größe des **Rohteils (Stock – der unbearbeitete Metallklotz)** fest (z. B. oben `1 mm` Aufmaß zum Planfräsen).
  * Sie setzen den **Werkstück-Nullpunkt (`WCS` / `G54` – Koordinatenursprung `X0, Y0, Z0`)**, z. B. auf die obere linke Ecke oder genau in die Mitte der Rohteil-Oberseite.

#### Schritt 4: Die Bearbeitungs-Operationen (Toolpaths / Werkzeugwege) programmieren

Jetzt weisen Sie dem 3D-Modell Schritt für Schritt die Bearbeitungen zu:

1. **Planfräsen (Face Milling):** Ein großer Fräser fährt einmal über die Oberseite, damit das Bauteil exakt eben und glatt ist (`Z0`).
2. **Schruppen (Adaptive Clearing / Grobbearbeitung):** Der Fräser trägt außen und in den Taschen schnell das meiste überschüssige Material ab, lässt aber z. B. `0.2 mm` **Aufmaß (Stock to Leave – Restmaterial für den Feinschliff)** stehen.
3. **Schlichten (2D Contour / Pocket – Feinbearbeitung):** Der Fräser fährt noch einmal langsam und hochpräzise an den Wänden entlang, um das exakte Endmaß laut Zeichnung herzustellen.
4. **Bohren & Gewindeschneiden (Drilling & Tapping):** Zentrierbohrer und Spiralbohrer bohren die Löcher (`G81` / `G83`).
5. **Kollisionsprüfung (3D-Simulation in Fusion):** Sie lassen die integrierte **Rohteil-Simulation (Stock Simulation)** laufen. Fusion zeigt Ihnen farbig an, ob irgendwo der **Werkzeughalter (Spannfutter)** das Bauteil berührt (**Kollision = Rot**) oder ob alles fehlerfrei abläuft (**Grün**).

#### Schritt 5: Der Export über Ihren Postprozessor (`.cps`-Datei)!

**Und genau HIER verbinden sich das 3D-Modell und das, was wir heute in `C:\Projekte\CNC` gebaut haben:**

* Wenn die Fräsbahnen am 3D-Modell fertig sind, klicken Sie in Autodesk Fusion auf **`NC-Programm erstellen (Post Process)`**.
* Jetzt wählt Fusion Ihren **Postprozessor (`mein_erster_post.cps` aus `C:\Projekte\CNC\02_Software_und_Tools\src\`)** aus!
* Ihr **JavaScript-Postprozessor** übersetzt die 3D-Fräsbahnen aus Fusion in den exakt passenden **G-Code (`.nc`-Datei)** für die Maschine des Kunden – inklusive Ihres **Entwickler-Headers** und der **Sicherheits-Info (`Z-MIN`)**, die wir vorhin programmiert haben!

#### Schritt 6: Auslieferung an den Kunden

Sie schicken dem Kunden per E-Mail oder Cloud-Ordner:

1. Die fertige **G-Code-Datei (`Bauteil_1001.nc`)**.
2. Das **Einrichteblatt (`Setup_Sheet.pdf`)**, damit der Mitarbeiter an der Maschine weiß: *„Nullpunkt G54 liegt oben links, Werkzeug T01 ist ein 10mm Fräser, Werkzeug T02 ist ein 6mm Bohrer“*.

---

### 3. Warum Sie mit BEIDEN Fähigkeiten (3D-CAM + JavaScript-Postprozessor) unschlagbar sind:

* Ein normaler **CAM-Programmierer** muss Aufträge oft ablehnen, wenn der Kunde eine exotische Maschine hat, für die er keinen passenden **Postprozessor (`.cps`)** besitzt.
* **Sie hingegen** können dank **Antigravity IDE + Gemini** innerhalb weniger Minuten den Postprozessor in JavaScript an jede Maschine des Kunden anpassen **UND** danach dauerhaft seine **3D-Modelle (`.step`-Dateien)** in fertigen **G-Code** verwandeln!

---

## Teil 7: Komplette Übersicht aller 16 Praxis-Übungen (+ 2 Einsteiger-Basis-Übungen) aus dem Übungshandbuch

Alle 16 Übungen (sowie die 2 Basis-Vorübungen A und B) sind vollständig mit Code, einfachen Erklärungen und **Simulator-Prüfanleitungen** in Ihrer zentralen Übungsdatei **[ALLE_UEBUNGEN_HANDBUCH.md](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md)** dokumentiert:

### 🟢 Block 1: Einsteiger & Grundlagen (Vom ersten Blick bis zur ersten Code-Zeile)

* **[Basis-Übung A](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L502-L547):** Die 5 wichtigsten **G-Code-Zeilen (Maschinenbefehle)** lesen lernen (`T01 M06`, `S8000 M03`, `M08`, `G00`, `G01`) und im Simulator anklicken.
* **[Basis-Übung B](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L551-L578):** Eine einzige eigene Textzeile (`writeComment("HALLO WELT...")`) in [`src/mein_erster_post.cps`](file:///c:/Projekte/CNC/02_Software_und_Tools/src/mein_erster_post.cps) einfügen und mit `node 02_Software_und_Tools/scripts/simuliere_post.js` testen.
* **[Übung 1](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L30-L88):** Der erste eigene Entwickler-Infoblock in `onOpen()` (Name, Betrieb und automatisches Datum im G-Code ausgeben).
* **[Übung 2](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L92-L144):** Automatische **Werkzeugliste (`Tool Table`)** mit einer `for`-Schleife ganz oben im G-Code ausgeben.
* **[Übung 3](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L148-L214):** Sicherheits-Schutz gegen **Maschinencrash (Kollision mit dem Schraubstock)** – Tiefste Frästiefe (`Z-MIN`) für jedes Werkzeug und jede Operation berechnen.

### 🔵 Block 2: 3D-Modelle als Kundenauftrag & Postprozessor-Anpassungen

* **[Übung 4](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L218-L254):** Ein **3D-Modell (`bauteil_1001.stl`)** als Kundenauftrag bearbeiten – Klick-für-Klick vom 3D-Bauteil zum fertigen G-Code.
* **[Übung 5](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L258-L284):** **3D-Simulation** im Browser ([`3d_auftrag_simulator.html`](file:///c:/Projekte/CNC/02_Software_und_Tools/web_tools/3d_auftrag_simulator.html)) durchführen & das **Einrichteblatt (`Setup Sheet`)** für den Kunden erstellen.
* **[Übung 6](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L288-L357):** **Sicherer Rückzug (`Safe Retract` mit `G53 Z0` vs. `G28`)** & Maschinentisch am Programmende (`onClose`) automatisch zur Kabinentür fahren (`G53 Y0`).
* **[Übung 7](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L361-L419):** Eigenen Schalter (`Property` – Auswahlfeld im Menü) für Zusatzfunktionen wie **Späneförderer (`M31` / `M33`)** oder **Blasluft (`M07`)** einbauen.
* **[Übung 8](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L423-L460):** Zwei Steuerungs-Sprachen vergleichen und umschalten (**Haas/Fanuc ISO-Dialekt** vs. **Siemens Sinumerik Dialekt**).

### 🟣 Block 3: Fortgeschrittene Profi-Übungen für echte Online-Aufträge (Upwork, Fiverr, Lohnfertiger)

* **[Übung 9](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L766-L818):** **Schnittdaten (`S` Drehzahl & `F` Vorschub)** berechnen – Warum Aluminium, Baustahl und Edelstahl völlig andere Werte brauchen.
* **[Übung 10](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L822-L864):** **Die 2. Aufspannung (`G55`)** – Wie das 3D-Bauteil umgedreht und der Restboden auf der Rückseite plangefräst wird.
* **[Übung 11](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L868-L930):** **Gewindebohren (`G84` Rigid Tapping)** – `M6`/`M8`-Schraubengewinde ohne Werkzeugbruch programmieren (`F = S × Steigung`).
* **[Übung 12](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L934-L967):** **Werkzeugradiuskorrektur (`G41` / `G42` / `G40`)** – Wie der Kunde an der Maschine `0,01 mm` Genauigkeit für Passungen einstellt.
* **[Übung 13](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L971-L1008):** **Echte 3D-Freiformflächen** – `3D Adaptive Clearing` (Wirbelfräsen) & `3D-Schlichten` mit **Kugelfräser (`Ball End Mill`)**.
* **[Übung 14](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L1012-L1044):** **Heidenhain Klartext-Steuerung (`TOOL CALL`, `L ... FMAX`) & 4. Drehachse (`A-Achse`)** für Aufträge im deutschsprachigen Raum.
* **[Übung 15](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L1048-L1091):** **Kanten entgraten am 3D-Modell (`2D-Fase / Chamfer Milling`)** mit einem 45°-Fasenfräser (`T04`).
* **[Übung 16](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L1095-L1127):** **Die komplette 5-Punkte-Endabnahme im Simulator** vor der Auslieferung an den Online-Kunden (Meister-Prüfung).

---

## Teil 8: Wo genau starte und teste ich die Programme? (In VSC / Antigravity IDE vs. Browser) & Fusion 360 FAQ

### 1. Antigravity IDE = VSC (Visual Studio Code)!

Das Programm, in dem Sie gerade arbeiten (**Antigravity IDE**), basiert technisch direkt auf **VSC (Visual Studio Code – dem weltbekannten Programmier-Editor von Microsoft)**.

* Alle Tasten, Menüs, das **Terminal (Befehlsfenster)** und die **Extensions (Erweiterungen)** sind hier **exakt gleich wie in VSC**!
* Sie müssen also kein separates Programm öffnen – Sie arbeiten direkt **hier in diesem Fenster (Ihrer VSC / Antigravity IDE)**.

### 2. Die 2 Orte, an denen Sie arbeiten und testen:

| Was möchten Sie tun?                                            | Wo machen Sie das?                                                     | Wie genau starten Sie es? (Klick-für-Klick)                                                                                                                                                                                                                                                                                                                                                                        |
|:--------------------------------------------------------------- |:---------------------------------------------------------------------- |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. JavaScript-Code ändern** (`mein_erster_post.cps`)          | **Direkt hier in VSC / Antigravity IDE** *(im oberen Editor-Fenster)*  | Links im Datei-Baum auf [`src/mein_erster_post.cps`](file:///c:/Projekte/CNC/02_Software_und_Tools/src/mein_erster_post.cps) klicken $\rightarrow$ Code ändern $\rightarrow$ mit **`Strg + S`** speichern.                                                                                                                                                                                                                               |
| **2. Programm starten & G-Code erzeugen** (`simuliere_post.js`) | **Direkt hier in VSC / Antigravity IDE** *(unten im Terminal-Fenster)* | 1. Oben im Menü auf **`Terminal` $\rightarrow$ `New Terminal`** klicken (oder Tastenkombination **`Strg + Ö`** drücken).<br>2. Unten im Terminal-Fenster eintippen:<br>`node 02_Software_und_Tools/scripts/simuliere_post.js`<br>3. **`Enter`-Taste** drücken $\rightarrow$ Sofort läuft Ihr Programm durch und schreibt den neuen G-Code in [`tests/mein_generierter_gcode.nc`](file:///c:/Projekte/CNC/02_Software_und_Tools/tests/mein_generierter_gcode.nc)! |
| **3. Den G-Code in 3D als bewegte Fräse sehen**                 | **Im Internet-Browser** *(Chrome, Edge oder Firefox)*                  | **Weg A:** Doppelklick im Windows-Explorer auf [`02_Software_und_Tools/web_tools/3d_auftrag_simulator.html`](file:///c:/Projekte/CNC/02_Software_und_Tools/web_tools/3d_auftrag_simulator.html).<br>**Weg B:** In VSC die Datei `tests/mein_generierter_gcode.nc` öffnen, alles kopieren (`Strg+A`, `Strg+C`), im Browser **`https://ncviewer.com`** öffnen, links einfügen (`Strg+V`) und auf **`Plot`** klicken!   |

### 3. Autodesk Fusion 360: Größe, Kosten & Gratis-Lizenz (`Personal Use License`)

* **Größe auf der Festplatte:** Ca. **4,5 GB bis 6 GB (Gigabyte)** (läuft flüssig auf jedem ThinkPad ab 8 GB RAM / Arbeitsspeicher).
* **Kosten zum Lernen & Üben:** **0,00 € (Dauerhaft kostenlos!)** über die Lizenz **„Autodesk Fusion für Privatanwender“ (`Autodesk Fusion for personal use`)**.
* **Wann installieren?** Für Stufe 1 bis 6 können Sie sofort ohne Download mit `node 02_Software_und_Tools/scripts/simuliere_post.js` und `3d_auftrag_simulator.html` starten; ab Stufe 7 ([Übung 4](file:///C:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md#L198-L258)) installieren Sie die kostenlose Privatanwender-Version von Fusion 360, um das 3D-Modell ([`bauteil_1001.stl`](file:///C:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte/bauteil_1001.stl)) selbst anzuklicken.
