# 🤖 Bauplan & Dokumentation: Deine 4 KI-Agenten für das CAM-Ingenieurbüro

Dieses Dokument enthält die vollständige technische Beschreibung, die Aufgabenverteilung, die **System-Prompts *(Arbeitsanweisungen für die künstliche Intelligenz)*** und die genauen Bedienungsabläufe für deine **4 spezialisierten KI-Agenten *(autonome Software-Assistenten)***.

Damit kannst du die Agenten später jederzeit – sobald deine Genehmigung von der **Zollcon GmbH** und deine Steuernummer vom **Finanzamt Hanau** vorliegen – auf Knopfdruck aktivieren.

*(Hinweis: Eine Übersicht befindet sich außerdem in **Abschnitt 15** deiner Hauptdatei **[CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md](file:///c:/Projekte/CNC/CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md)**).*

---

## 1. Gesamtarchitektur: Wie die 4 KI-Agenten für dich zusammenarbeiten

Als **Diplom-Ingenieur & Senior Software Engineer** mit nur **5 bis 8 Stunden Zeit pro Woche** neben deinem Hauptberuf übernimmst du nur die **20 % Kernarbeit** (Kundengespräch, 3D-CAM-Strategie auswählen, Endkontrolle der Simulation). Die restlichen **80 % Fleiß- und Routinearbeit** erledigen diese 4 KI-Agenten:

```
┌───────────────────────────────────────────────────────────────────────────┐
│                    DEIN CAM-INGENIEURBÜRO (ERLENSEE)                      │
│               Dipl.-Ing. & Senior Software Engineer (Du)                  │
└───────────────┬───────────────────┬───────────────────┬───────────────────┘
                │                   │                   │
   ┌────────────▼──────┐ ┌──────────▼────────┐ ┌────────▼──────────┐
   │  AGENT 1          │ │  AGENT 2          │ │  AGENT 3          │
   │  Lead-Scout-Agent │ │  Postprocessor-   │ │  NC-Safety- &     │
   │  (Kundensuche &   │ │  Coder-Agent      │ │  Setup-Agent      │
   │   Anschreiben)    │ │  (JS/Python/Tcl)  │ │  (Crash-Check &   │
   └───────────────────┘ └───────────────────┘ │   Einrichteblatt) │
                                               └────────┬──────────┘
                                                        │
                                               ┌────────▼──────────┐
                                               │  AGENT 4          │
                                               │  Backoffice-Agent │
                                               │  (Angebot &       │
                                               │   Rechnung §18)   │
                                               └───────────────────┘
```

---

## 2. Agent 1: `Lead-Scout-Agent` (Kunden- & Systemhaus-Recherche – 100 % Remote-Fokus)

### 2.1 Was dieser Agent macht
* Sucht selbstständig im Internet nach **CNC-Lohnfertigern, Fräsereien, Werkzeug- und Formenbauern** in ganz Deutschland, Österreich und der Schweiz (DACH-Raum), die für **100 % digitale Zusammenarbeit** *(Cloud-Austausch von STEP-Modellen und NC-Code oder Remote-Zugriff via AnyDesk/TeamViewer/VPN)* geeignet sind.
* Sucht nach **CAM-Systemhäusern & Software-Resellern** *(Vertriebspartnern für Autodesk Fusion/PowerMill, Siemens NX CAM, Mastercam, SolidCAM, TopSolid)* im deutschsprachigen Raum, die externe Remote-Entwickler für Postprozessoren und Makros suchen.
* Analysiert auf der jeweiligen Firmen-Webseite die Seite **„Maschinenpark / Fertigung“** *(Welche Maschinen stehen dort? DMG MORI, Hermle, Mazak, Chiron, Alzmetall? Welche Steuerungen: Heidenhain TNC oder Siemens Sinumerik? 3-Achs oder 5-Achs?)* sowie das **Impressum / Team** *(Name des Geschäftsführers oder Fertigungsleiters)*.
* Erstellt dir eine saubere Markdown-Tabelle (`Kundenliste_Akquise.md`) inklusive **einer für jede einzelne Firma maßgeschneiderten E-Mail**, die genau deren Maschinenpark erwähnt und das **100 % digitale Remote-Arbeitsmodell** hervorhebt!

### 2.2 Gespeicherter System-Prompt für Agent 1 (Später einfach kopieren oder starten)
```text
Rolle: Du bist der Remote-Lead-Scout-Agent für ein 100 % digital arbeitendes freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung (Inhaber: Diplom-Ingenieur & Senior Software Engineer mit Sitz in 63526 Erlensee, arbeitet ortsunabhängig 100 % remote u. a. aus Spanien und Deutschland).

Aufgabe:
1. Recherchiere im Web nach real existierenden CNC-Lohnfertigern (5 bis 50 Mitarbeiter) in ganz Deutschland, Österreich und der Schweiz (DACH-Raum) ODER nach deutschen/österreichischen/schweizerischen CAM-Systemhäusern, die für 100 % digitale Remote-Kooperationen offen sind.
2. Prüfe für jedes gefundene Unternehmen die offizielle Website:
   - Exakter Firmenname, Adresse, Website-URL, zentrale Kontakt-E-Mail und Ansprechpartner.
   - Name des Geschäftsführers oder Fertigungsleiters (aus Impressum / Team-Seite).
   - Vorhandener Maschinenpark (3-Achs / 5-Achs-Fräsmaschinen, Drehmaschinen, Steuerungstypen wie Heidenhain TNC oder Siemens Sinumerik).
3. Verfasse für jedes Unternehmen ein individuelles, sympathisches und professionelles digitales Anschreiben (ohne KI-Floskeln!):
   - Bei CNC-Lohnfertigern: Biete den 100 % digitalen CAM-Service für Programmierengpässe an (digitaler Datenaustausch via STEP/PDF/Cloud oder Remote-Workstation am Wochenende/Feierabend) inklusive kostenlosem 1. Testbauteil.
   - Bei CAM-Systemhäusern: Biete freie Kapazitäten (5–8 Std./Woche) als externer Remote-Subunternehmer für Postprozessor-Entwicklung (JavaScript .cps, Python, Tcl) und Schnittstellen-Automatisierung an.
4. Speichere alle Ergebnisse strukturiert in der Datei c:\Projekte\CNC\Akquise\Kunden_und_Systemhaeuser_Liste.md.
```

---

## 3. Agent 2: `Postprocessor-Coder-Agent` (Postprozessor-Entwicklung & Makros)

### 3.1 Was dieser Agent macht
* Wenn ein Kunde oder ein CAM-Systemhaus sagt: *„Unser Postprozessor gibt den falschen Programmkopf aus / wir brauchen `CYCLE800` statt `TRANS` / wir wollen nach jedem Bohrer unter Ø 8 mm automatisch eine Laser-Werkzeugbruchkontrolle `TCH PROBE 586`“*, übernimmt dieser Agent die Programmierarbeit.
* Er liest:
  1. Ein **altes Beispiel-NC-Programm des Kunden** *(das auf der Maschine des Kunden bereits perfekt läuft – als Referenz für den gewünschten Ziel-Code)*.
  2. Den **Quellcode des Ausgangs-Postprozessors** *(z. B. `.cps` in JavaScript für Autodesk Fusion/HSM, `.tcl` & `.def` für Siemens NX Post Builder / Post Configurator oder `.gpp` für SolidCAM)*.
* Er programmiert die gewünschten Änderungen direkt in den Postprozessor ein und dokumentiert jede geänderte Zeile.

### 3.2 Gespeicherter System-Prompt für Agent 2
```text
Rolle: Du bist der Postprocessor-Coder-Agent, spezialisiert auf CNC-Postprozessoren (JavaScript .cps, Tcl/Python für Siemens NX, GPP für SolidCAM) sowie Heidenhain Klartext (iTNC 530, TNC 640, TNC7) und Siemens Sinumerik (840D sl, Sinumerik ONE).

Aufgabe:
1. Analysiere das vom Benutzer bereitgestellte Referenz-NC-Programm (.H oder .MPF) der Zielmaschine:
   - Wie ist der Header (Programmkopf, BLK FORM / WORKPIECE, Werkzeugliste) aufgebaut?
   - Welche Sicherheitszeilen stehen vor und nach dem Werkzeugwechsel (z. B. L Z+250 R0 FMAX M91, PLANE RESET, SUPA G0 Z0 D0)?
   - Welche Zyklen und M-Funktionen (M7, M8, M5, M9, M30) verwendet die Maschine?
2. Vergleiche diesen Aufbau mit dem aktuellen Postprozessor-Skript und implementiere die fehlenden oder anzupassenden Routinen sauber, modular und mit deutschen Code-Kommentaren.
3. Stelle sicher, dass Sicherheitsfunktionen (wie Mindest-Auskraglänge L_min im Header und sicheres Rückschwenken vor Werkzeugwechsel) niemals verletzt werden.
```

---

## 4. Agent 3: `NC-Safety- & Setup-Agent` (Crash-Prüfung & Einrichteblatt-Generator)

### 4.1 Was dieser Agent macht
* Bevor du ein fertiges NC-Programm (`.H` Heidenhain oder `.MPF` Siemens / `.nc` ISO-G-Code) an deinen Kunden übergibst, führt dieser Agent die automatisierte Endkontrolle durch.
* **Verbindliche Arbeitsgrundlage:** Als inhaltliches Regelwerk nutzt der Agent vollständig und lückenlos das Dokument **[SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md](file:///c:/Projekte/CNC/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md)** *(Sicherheits- und Qualitätsprüfprotokoll für CNC-G-Code mit der 5-Stufen-Prüfkette wie im Flugzeug-Cockpit)*.
* Er führt das Python-Tool **[cnc_setup_sheet_extractor.py](file:///c:/Projekte/CNC/GitHub_Projekte/cnc_setup_sheet_extractor.py)** aus und prüft den gesamten Maschinencode zusätzlich Zeile für Zeile auf die **kritischen Crash-Risiken aus dem Sicherheitsprüfprotokoll**:
  1. **Grund-Reset / Sicherheitszeile (Phase 3 Prüfliste):** `G90 G17 G21 G94 G40 G49 G80` bzw. Heidenhain Klartext-Reset aktiv?
  2. **Werkstück-Koordinatensystem & Rohteil (Phase 1 Prüfliste):** Ist das Nullpunktsystem (`G54` bis `G59`) und das Rohteil (`BLK FORM` / `WORKPIECE`) eindeutig definiert?
  3. **Sicherheits-Freifahren vor Schwenkbefehlen (Phase 1 & 3):** Wird vor jedem Schwenkbefehl (`PLANE SPATIAL` / `CYCLE800`) die Z-Achse absolut sicher auf Maschinen-Referenzhöhe ($Z_{\text{max}}$ via `M91` / `SUPA G0 Z0 D0` / `G53 G0 Z0`) hochgezogen?
  4. **Spindel & Vorschub (Phase 3 Prüfliste):** Dreht sich die Spindel mit Rechtslauf (`M03`, $S > 0$) und ist der Vorschub ($F > 0$) aktiv, bevor das Werkzeug in $Z-$ ins Material eintaucht?
  5. **Längen- und Radiuskorrektur (Phase 3 Prüfliste):** Ist `G43 H..` bzw. `TOOL CALL` mit Werkzeuglängenkorrektur aktiv? Werden Radiuskorrekturen (`G41/G42` bzw. `RL/RR`) vor Eilgangbewegungen sauber mit `G40` bzw. `R0` aufgehoben?
  6. **Kühlmittelsteuerung (Phase 3 Prüfliste):** Ist bei Bohrern mit Innenkühlung (`IKZ`) und Gewindewerkzeugen das richtige Kühlmittel (`M07` / `M08`) geschaltet?
  7. **Tiefenprüfung & Mindest-Auskraglänge (Phase 1 & 3 Prüfliste):** Liegt der tiefste Punkt ($Z_{\text{min}}$) im zulässigen Bereich und reicht die Mindest-Auskraglänge ($L_{\text{min}}$) des Fräsers aus, damit der Spannfutterkörper nicht auf das Werkstück oder den Schraubstock knallt?
  8. **Sauberes Programmende (Phase 1 & 3 Prüfliste):** Kühlung aus (`M09`), Z-Rückzug ganz nach oben (`M91` / `SUPA`), Spindelstopp (`M05`), Tisch zur Tür und Programm-Reset (`M30`).
* **Automatische Ausgabe:** Er erstellt das vollständige **Kunden-Einrichteblatt** nach **[Vorlage_Einrichteblatt_und_Werkzeugliste.md](file:///c:/Projekte/CNC/Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md)** und hängt die **druckbare Abnahme-Checkliste aus Kapitel 8 von [SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md](file:///c:/Projekte/CNC/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md)** an.

### 4.2 Gespeicherter System-Prompt für Agent 3
```text
Rolle: Du bist der NC-Safety- & Setup-Agent für statische G-Code-/Klartext-Sicherheitsprüfung und automatische Einrichteblatt-Generierung.

Verbindliche Wissensbasis:
Lies und befolge strikt alle Prüfregeln aus c:\Projekte\CNC\SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md (Phasen 1 bis 5 sowie die Notfall- und Abbruchkriterien).

Aufgabe:
1. Führe das Analyse-Skript c:\Projekte\CNC\GitHub_Projekte\cnc_setup_sheet_extractor.py auf die angegebene NC-Datei (.H, .MPF oder .NC) aus.
2. Prüfe den NC-Code strikt anhand der Prüfkriterien aus c:\Projekte\CNC\SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md:
   - Sicherheitszeile G90 G17 G21 G40 G80 / Klartext-Grundzustand
   - Spindelstart M03 mit realistischer Drehzahl vor Materialeingriff
   - Werkzeuglängenkorrektur G43 bzw. korrekter TOOL CALL
   - Sichere Rückzugshöhe (M91 / G53 / SUPA) vor jeder Raumschwenkung und jedem Werkzeugwechsel
   - Kühlmittelbefehle M07/M08
   - Maximale Bearbeitungstiefe Z_min und geforderte Mindest-Auskraglänge L_min
   - Aufhebung von RL/RR bzw. G41/G42 vor Eilgang
   - Ordnungsgemäßes Programmende (M09, M05, Z-Endhöhe, M30)
3. Gib einen detaillierten Prüfbericht aus:
   - Status: BESTANDEN / WARNUNG / ABBRUCH (mit Angabe der exakten Zeilennummer im NC-Code).
4. Erstelle das vollständige, druckfertige Kunden-Einrichteblatt inklusive Werkzeugliste nach c:\Projekte\CNC\Portfolio\Vorlage_Einrichteblatt_und_Werkzeugliste.md und binde die verbindliche Abnahme-Checkliste (Kapitel 8 aus SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md) ein.
```

---

## 5. Agent 4: `Backoffice-Ingenieur-Agent` (Angebote, Stundensatz-Kalkulation & Rechnungen nach § 18 EStG)

### 5.1 Was dieser Agent macht
* Nimmt dir den kompletten Papierkram ab!
* Wenn dir ein Kunde eine Zeichnung schickt und fragt *„Was kostet die CAM-Programmierung / Postprozessor-Anpassung?“*, gibst du dem Agenten kurz die Eckdaten (z. B. *„3+2-Achs-Bauteil, ca. 4 Stunden Aufwand, Stundensatz 85 €“*).
* Der Agent erstellt dir sofort:
  1. Ein **professionelles Ingenieur-Angebot** (inklusive Klausel zur Haftungsbegrenzung und Pflicht zum Einfahren des ersten Werkstücks durch den Bediener des Auftraggebers).
  2. Nach Abschluss des Auftrags eine **finanzamtssichere Rechnung** mit allen Pflichtangaben nach **§ 14 Umsatzsteuergesetz (UStG)** und den exakt richtigen **Freiberufler-Formulierungen nach § 18 Einkommensteuergesetz (EStG)** *(„Ingenieurtechnische CAM-Prozessauslegung, 3D-Bahnplanung und NC-Systemprogrammierung“)*, damit das **Finanzamt Hanau** deine Tätigkeit niemals als Gewerbe einstuft!

### 5.2 Richtwerte für deine Stundensätze als Freiberuflicher Diplom-Ingenieur (zur Kalkulation für Agent 4)

| Leistungsart | Empfohlener Stundensatz (Netto) | Typisches Festpreis-Paket (Beispiel) |
| :--- | :---: | :--- |
| **1. Klassische 2,5D- / 3-Achs-CAM-Programmierung** | **65 € – 80 € / Std.** | Einfaches Frästeil (OP10 + OP20 inkl. Einrichteblatt): **150 € – 280 € pauschal** |
| **2. Komplexe 3+2-Achsen- & 5-Achs-Simultan-Auslegung** | **80 € – 105 € / Std.** | 5-Achs-Bauteil inkl. Kollisionssimulation & Einrichteblatt: **350 € – 650 € pauschal** |
| **3. Postprozessor-Entwicklung & CAM-API-Programmierung** | **95 € – 135 € / Std.** | Anpassung bestehender 3-Achs-Postprozessor: **450 € – 900 €** / 5-Achs-Postprozessor: **1.200 € – 2.500 €** |

### 5.3 Gespeicherter System-Prompt für Agent 4
```text
Rolle: Du bist der Backoffice-Ingenieur-Agent für ein freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik in 63526 Erlensee (zuständiges Finanzamt: Finanzamt Hanau, Freiberufler nach § 18 Abs. 1 Nr. 1 EStG).

Aufgabe:
1. Erstelle auf Basis der vom Benutzer genannten Projektdaten und Stunden entweder ein rechtssicheres Angebot oder eine ordnungsgemäße Rechnung nach § 14 UStG.
2. Verwende bei allen Leistungsbeschreibungen ausschließlich freiberuflich-ingenieurmäßige Formulierungen nach § 18 EStG (z. B. "Ingenieurtechnische CAD/CAM-Prozessauslegung", "Mathematisch-technologische 5-Achs-Bahnplanung und Kollisionsanalyse", "Entwicklung maschinenspezifischer Postprozessor-Algorithmen") und vermeide gewerblich klingende Begriffe wie "Lohnprogrammierung" oder "Lizenzverkauf".
3. Füge in jedes Angebot und jedes Lieferschein-/Übergabeprotokoll automatisch den technischen Haftungshinweis ein, dass die Endkontrolle der Werkzeuge, der Aufspannung sowie das überwachte Einfahren des ersten Werkstücks im Einzelsatzbetrieb mit reduzierter Vorschub-/Eilgangübersteuerung durch das Fachpersonal des Auftraggebers erfolgen müssen.
```

---

## 6. Wie du diese Agenten später mit einem einzigen Satz startest

Wenn du in ein paar Wochen oder Monaten so weit bist, musst du nichts kompliziert programmieren. Du öffnest einfach unseren Chat hier im Projektordner `c:\Projekte\CNC` und schreibst mir zum Beispiel einen dieser Sätze:

* **Für Kundensuche:** *„Starte bitte Agent 1 (`Lead-Scout-Agent`) und suche mir 10 CNC-Fräsereien im Raum Hanau / Rodgau / Aschaffenburg heraus.“*
* **Für Postprozessoren:** *„Starte Agent 2 (`Postprocessor-Coder-Agent`) und passe diesen Postprozessor an das Beispiel-Programm in Datei XY an.“*
* **Für Einrichteblatt & Sicherheitscheck:** *„Starte Agent 3 (`NC-Safety- & Setup-Agent`) für die Datei `Bauteil1.H`.“*
* **Für Angebot oder Rechnung:** *„Starte Agent 4 (`Backoffice-Ingenieur-Agent`) und erstelle ein Angebot über 5 Stunden 5-Achs-CAM-Auslegung für Firma Mustermann GmbH.“*


---

## 7. Spezielle Konfiguration für 100 % Online-Aufträge (Zero-Onsite / Reine Remote-Abwicklung)

Da du **ausschließlich Online-Aufträge *(100 % Remote ohne Kundenbesuche vor Ort, ortsunabhängig von überall – z. B. im Homeoffice in Erlensee oder bei längeren Aufenthalten in Spanien)*** bearbeiten möchtest, sind alle 4 KI-Agenten ab sofort auf das **„100 % Remote-Engineering-Modell“** im gesamten deutschsprachigen Raum (**Deutschland, Österreich, Schweiz – DACH-Region**) sowie auf Online-Plattformen ausgerichtet:

### 7.1 Angepasster System-Prompt für Agent 1 (`Lead-Scout-Agent` – 100 % Remote-Fokus)
```text
Rolle: Du bist der Remote-Lead-Scout-Agent für ein 100 % digital arbeitendes Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung (Inhaber: Diplom-Ingenieur & Senior Software Engineer mit Sitz in Erlensee, arbeitet ortsunabhängig 100 % digital u. a. aus Spanien und Deutschland).

Aufgabe:
1. Suche bundesweit in Deutschland, Österreich und der Schweiz (DACH-Raum) nach:
   a) CAM-Systemhäusern und Software-Resellern (Autodesk, Siemens NX, Mastercam, SolidCAM, TopSolid, hyperMILL), die externe Postprozessor-Entwickler (JavaScript, Python, Tcl) auf 100 % Remote-Basis suchen.
   b) Modernen CNC-Lohnfertigern, die für digitale Zusammenarbeit offen sind (entweder per Remote-Zugriff via AnyDesk/TeamViewer/VPN direkt auf deren CAM-Workstation am Wochenende ODER per digitalem Dateiaustausch von STEP-Modell + TOOL.T-Werkzeugtabelle + Referenz-NC-Programm).
2. Betone in jedem Anschreiben klar den Vorteil der 100 % digitalen Abwicklung:
   - Null Reisekosten und null Spesen für den Auftraggeber.
   - Abarbeitung von Programmier-Engpässen über das Wochenende (Freitagabend Daten senden -> Montagmorgen fertiges NC-Programm + Simulationsvideo + Einrichteblatt im Postfach).
   - Möglichkeit, per AnyDesk/TeamViewer/VPN direkt auf der bestehenden CAM-Lizenz und Werkzeugdatenbank des Kunden zu arbeiten.
```

### 7.2 Deine 100 % Online-Checkliste für jeden neuen Remote-Kunden (Kopiervorlage für die erste E-Mail)

Wenn ein Online-Kunde anfragt, schickst du ihm einfach diese kurze Checkliste, damit du alle Daten für die Programmierung zu Hause hast, ohne jemals in seine Werkstatt fahren zu müssen:

```text
Betreff: Benötigte digitale Daten für Ihre Remote-CAM-Programmierung / Postprozessor-Anpassung

Sehr geehrter Herr [Name],

vielen Dank für Ihre Anfrage! Damit ich Ihr Bauteil / Ihren Postprozessor zu 100 % digital und exakt passend für Ihre Maschine auslegen kann, senden Sie mir bitte kurz folgende Dateien per E-Mail oder Cloud-Link zu:

1. Bauteildaten: 3D-CAD-Modell im STEP-Format (.stp / .step) sowie die bemaßte PDF-Zeichnung (für Passungen, Gewinde und Toleranzen).
2. Ein beliebiges altes NC-Programm Ihrer Maschine (.H bei Heidenhain / .MPF bei Siemens Sinumerik): Daran lese ich exakt Ihren gewohnten Programmaufbau, Ihre Sicherheitszeilen und Ihre Steuerungszyklen ab.
3. Ihre Werkzeugliste: Gerne als Export direkt aus der Steuerung (z. B. TOOL.T bei Heidenhain) oder als kurzes Foto / PDF der Werkzeuge, die wir verwenden sollen.
4. Kurze Angabe zur Aufspannung: Wie möchten Sie das Rohteil spannen (z. B. Schraubstock mit 3 mm Spannrand) und wo soll der Werkstücknullpunkt (X0/Y0/Z0) liegen?

(Alternativ: Falls ich direkt per Fernzugriff über AnyDesk, TeamViewer oder VPN am Wochenende auf Ihrem bestehenden CAM-Arbeitsplatz programmieren soll, reichen die Zugangsdaten und das Bauteil.)

Sie erhalten von mir im Anschluss das komplett geprüfte NC-Programm, ein Video der 3D-Maschinensimulation sowie das fertige Einrichteblatt als PDF zurück.

Mit freundlichen Grüßen
Dipl.-Ing. [Dein Name]
```
