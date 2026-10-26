# 📐 CNC-Projektregel: Verbindlicher Standard für Kundenaufträge & Workflow-Dateien

## Geltungsbereich:
Gilt für alle CNC-Kundenaufträge, Übungen und Anfragen im Projekt `c:\Projekte\CNC`.

---

## 1. Grundregel: Isolierter Auftragsordner
Für **JEDEN** neuen Kundenauftrag *(egal ob reale Anfrage oder Übung)* muss zwingend ein **eigener, isolierter Auftragsordner** unter `01_Kundenauftraege/` angelegt werden.

Vor Beginn der Bearbeitung dürfen in diesem Ordner **NUR** liegen:
1. `KUNDENAUFTRAG.md` *(Das Original-Briefing)*
2. `WORKFLOW_UND_PROMPTS.md` *(Der auftragsspezifische Leitfaden)*
3. Etwaige 3D-Modelle des Kunden *(`.stl` / `.step`)*

Es dürfen vorab **KEINE unbestellten Dateien *(wie unaufgeforderte `.cps`-Dateien)* oder fertige Teillösungen** hineingelegt werden.

---

## 2. Pflichtaufbau der Datei `WORKFLOW_UND_PROMPTS.md`
Jede `WORKFLOW_UND_PROMPTS.md` muss exakt dem Standard aus `test_auftrag_ubung_03` folgen und folgende 5 Abschnitte lückenlos enthalten:

### Abschnitt 1: Tabelle der zu erzeugenden Artefakte & deren exakte Speicherorte
Eine übersichtliche Markdown-Tabelle aller **6 Pflicht-Artefakte**:
1. `02_ANGEBOT_DIPL_ING_BUJANOVSKI.md` *(B2B-Angebot nach § 18 EStG)*
2. `[auftragsname].nc` *(Fertig generierter Maschinencode)*
3. `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` *(5-Stufen-Prüfbericht mit Freigabestatus)*
4. `06_EINRICHTEBLATT_SETUP_SHEET.md` *(Rüstdatenblatt für den Maschinenbediener)*
5. **`[auftragsname]_simulation_video.mp4` *(3D-Maschinensimulationsvideo zur Kundenfreigabe)***
6. `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md` *(Steuersichere Honorarrechnung nach § 14 UStG)*

Zu jedem Artefakt muss der genaue Klick-Speicherort mit `file:///`-Link im jeweiligen Auftragsordner und der zuständige KI-Agent *(Agent 4, Agent 2 oder Agent 3)* angegeben sein.

### Abschnitt 2: Das 4-Stufen-Workflow-Diagramm
Klares ASCII-Diagramm der 4 Bearbeitungsphasen:
* Schritt 1: Angebot erstellen *(Agent 4: Backoffice-Agent)*
* Schritt 2: NC-Maschinencode generieren *(Agent 2: Postprocessor-Coder-Agent)*
* Schritt 3: **Sicherheit, Einrichteblatt & 3D-Video-Generierung *(Agent 3: NC-Safety-Agent)***
* Schritt 4: Honorarrechnung stellen *(Agent 4: Backoffice-Agent)*

### Abschnitt 3: Fertige, maßgeschneiderte Prompts zum Kopieren
Für jeden der 4 Schritte muss ein **vollständig ausgefüllter Prompt** im Codeblock bereitgestellt werden.
* **STRENG VERBOTEN:** Generische Platzhalter wie `[Kunde]`, `[Betrag]`, `[Datei]`.
* **VERPFLICHTEND:** Jeder Prompt muss die **echten Kundendaten** enthalten:
  - Exakter Firmenname und Ansprechpartner
  - Exakter Maschinentyp *(z. B. Haas VF-2, Hermle C42, DMG MORI)*
  - Exakte Werkzeugdaten *(z. B. T01 Fräser Ø 10 mm)*
  - Exakte Frästiefen *(z. B. Z = -5,0 mm Schulter, Z = -3,0 mm Tasche)*
  - Exakter Nullpunkt *(z. B. G54 vorne links oben)*
  - Exaktes Budget *(z. B. 480,00 € netto)*
  - **In Schritt 3 zwingend der Befehl zur Video-Generierung:** Auftrag an Agent 3 zum Rendern des 3D-Simulationsvideos `[auftragsname]_simulation_video.mp4` via `render_simulation_video.py`
  - Vollständiger Zielpfad für alle Artefakte

### Abschnitt 4: Prüf- und Testanleitung für jedes einzelne Artefakt
Unter jedem Prompt muss eine eigene Anleitung **„🔍 Wie wird dieses Artefakt getestet und geprüft?“** stehen:
1. **Angebot prüfen:** Honorarbetrag, freiberufliche Formulierung nach § 18 EStG, Haftungsausschluss-Klausel *(Einzelsatzbetrieb beim Einfahren)*.
2. **NC-Code prüfen:**
   - Textprüfung auf Z-MIN Header und Sicherheitszeile `G90 G17 G21 G94 G40 G49 G80`.
   - Web-Backplot-Test *(z. B. mit NCViewer.com)*.
   - 3D-Browsersimulator-Test.
3. **Sicherheitsbericht, Einrichteblatt & 3D-Video prüfen:**
   - Status BESTANDEN (GRÜN).
   - Rechnerische Kollisionsreserve zu den Schraubstockbacken *(mathematische Formel: Abstand = Backenhöhe - Z_min)*.
   - Vollständigkeit der Werkzeugliste mit Mindest-Auskraglängen.
   - **🎬 3D-Simulationsvideo-Check:** Visuelle Kontrolle der MP4-Datei: Sichere Freifahrhöhe, sanftes Eintauchen im Vorschub, Fräsen aller Konturen und dauerhafter Sicherheitsabstand über den Schraubstockbacken.
4. **Rechnung prüfen:**
   - Pflichtangaben nach § 14 UStG, Bruttobetrag mit 19 % MwSt., freiberufliche Leistungsbeschreibung für das Finanzamt Hanau.

### Abschnitt 5: Abnahme-Kriterien (Checkliste für 100 % Erledigung)
Checkliste aller 6 erzeugten Dateien mit Prüfpunkten für den Projektabschluss:
* [ ] Angebot existiert und wurde geprüft.
* [ ] NC-Programm existiert mit Z-MIN Header und lief im Simulator.
* [ ] Sicherheitsprüfbericht bescheinigt Status BESTANDEN (GRÜN).
* [ ] Einrichteblatt liegt druckfertig vor.
* [ ] **3D-Simulationsvideo wurde gerendert und zeigt kollisionsfreie Fräsbahnen.**
* [ ] Rechnung ist für das Finanzamt Hanau abgelegt.

---

## 3. Strikte Konsistenz- und Synchronitätsprüfung vor Bearbeitungsstart (Zero-Tolerance-Konsistenzgebot)

Um Inkonsistenzen zwischen Kundenanfrage, Workflow-Prompts und Handbuchkapiteln systematisch zu unterbinden, gilt ab sofort folgende verbindliche Prüfregel vor jeder Auftragsbearbeitung:

1. **Maschinen- und Steuerungs-Synchronität:**
   * Die im Briefing genannte Fräsmaschine *(z. B. Haas VF-2 oder DMG MORI CMX 600 V)* und deren Steuerung *(z. B. Haas NGC, Siemens Sinumerik 840D oder Heidenhain TNC 640)* müssen im Metadatenkopf von `KUNDENAUFTRAG.md`, im Fließtext des Kundenbriefings, in allen 4 Prompts von `WORKFLOW_UND_PROMPTS.md` und im Postprozessor bzw. Handbuch **zu 100 % identisch** sein.
   * Es ist streng verboten, in Vorlagen oder Kopfzeilen andere Maschinenmodelle stehenzulassen *(Verbot von Template-Drift durch unvollständiges Copy-Paste)*.

2. **Kaufmännische Synchronität & Zahlungskonditionen:**
   * Zahlungsbedingungen aus dem Kundenbriefing *(z. B. 50 % Anzahlung sofort, 50 % nach Vorlage des Freigabevideos)* müssen exakt so in das Angebot `02_ANGEBOT_DIPL_ING_BUJANOVSKI.md` und in die spätere Abrechnung übernommen werden.

3. **Einheitliche Dateinamen-Konvention (Präfix-Standard):**
   * Alle Artefakte müssen ausnahmslos der definierten Nomenklatur folgen:
     - `02_ANGEBOT_DIPL_ING_BUJANOVSKI.md` *(immer mit führendem `02_`)*
     - `[auftragsname].nc`
     - `05_SICHERHEITS_CRASH_PRUEFBERICHT.md`
     - `06_EINRICHTEBLATT_SETUP_SHEET.md`
     - `[auftragsname]_simulation_video.mp4`
     - `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`
   * Veraltete Bezeichnungen ohne Präfix *(wie `ANGEBOT_DIPL_ING_BUJANOVSKI.md`)* sind sofort auf den Standard `02_...` zu vereinheitlichen.

4. **Bereinigung redundanter Alt-Dateien (No Duplicate Briefings):**
   * Es darf im Auftragsordner nur **eine einzige, maßgebliche `KUNDENAUFTRAG.md`** geben. Veraltete Dubletten wie `KUNDENAUFTRAG_BRIEFING.md`, `00_AUFTRAGS_LEITFADEN...` oder `STATUS_UND_DATEIEN.md` dürfen bei Neuaufträgen nicht mehr angelegt werden; in Bestandsordnern sind diese Dokumente auf den aktuellen Stand von `KUNDENAUFTRAG.md` zu synchronisieren.

5. **Geometrie- und Rohteil-Prüfung:**
   * Rohteilabmessungen *(z. B. $85 \times 55 \times 15\,\text{mm}$)*, Fertigmaße *(z. B. $80 \times 50 \times 12\,\text{mm}$)* und Werkzeuglisten *(z. B. T01 Fräser $\varnothing 10\,\text{mm}$, T02 Bohrer $\varnothing 6\,\text{mm}$)* müssen zwischen Kundenbriefing, `.cps`-Kommentaren und NC-Code zeichengenau übereinstimmen.

6. **Reines Kundenbriefing in `KUNDENAUFTRAG.md` (Keine internen Agenten-Hinweise):**
   * In der Datei `KUNDENAUFTRAG.md` darf **AUSSCHLIESSLICH der reale Kundenauftrag** *(die E-Mail bzw. das Original-Briefing des Kunden mit Absender, Empfänger, Bauteildaten, Maschinentyp, Spannsituation und Honorar)* stehen.
   * Interne Bearbeitungshinweise *(wie z. B. „Zuständiger Agent für Angebot: Agent 4“, „Agent 2 für Umsetzung“)*, Lösungstipps oder Lehrbuchtexte haben in `KUNDENAUFTRAG.md` **nichts verloren**. Alle agentenspezifischen Anweisungen und Arbeitsabläufe gehören ausnahmslos in die Datei `WORKFLOW_UND_PROMPTS.md`.


---

## 4. Pflicht zur strukturierten Abschluss-Dokumentation aller generierten Artefakte (`08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md`)

Sobald die KI-Agenten *(Agent 1, Agent 2, Agent 3 und Agent 4)* alle für einen Kundenauftrag erforderlichen Artefakte generiert haben, muss zwingend eine zentrale, detaillierte Abschluss-Dokumentation mit dem festen Dateinamen **`08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md`** direkt im jeweiligen Auftragsordner unter `01_Kundenauftraege/auftragsakten_.../` erstellt werden.

### Verbindlicher Aufbau und Pflichtinhalte dieser Dokumentation:

1. **Auftrags-Stammdaten & Metadaten:**
   * Kunde *(Unternehmen, Ansprechpartner, E-Mail)*
   * Bauteilbezeichnung und 3D-CAD-Dateiname *(`.step` / `.stl`)*
   * Maschinentyp und CNC-Steuerung *(z. B. Haas VF-2 mit NextGen Control)*
   * Kaufmännisches Budget und Zahlungskonditionen
   * Freiberuflicher Ingenieurstatus gemäß § 18 EStG *(Einkommensteuergesetz – reine Prozessauslegung und Software-Bahnplanung, keine gewerbliche Zerspanung)*.

2. **Vollständige Artefakt-Matrix (Tabelle aller generierten Dateien):**
   Eine lückenlose Übersichtstabelle aller erstellten Dateien mit:
   * Dateiname als klickbarer Link im Format `file:///...`
   * Zuständiger KI-Agent *(Agent 1, 2, 3 oder 4)*
   * Dateityp und Speicherort
   * Zweck und technischer Inhalt des Artefakts

3. **Detaillierte Chronologie der Agenten-Arbeiten (Wer hat was und wie gemacht?):**
   * **Phase 1: Agent 1 (Kundenbriefing & Anforderungsanalyse):**
     Erfassung der geometrischen Maße, Toleranzen, Rohteilaufmaße und Prüfung der Spannsituation im Maschinenschraubstock.
   * **Phase 2: Agent 4 (Vertragsgestaltung & B2B-Angebot):**
     Kalkulation des Festpreises, Formulierung der Leistungsbeschreibung für die Softwareentwicklung und Einbau der Haftungsausschluss-Klausel *(Verpflichtung des Kunden zum Einfahren des ersten Bauteils im Einzelsatz / Single Block)*.
   * **Phase 3: Agent 2 (CAM-Engineering & Postprozessor-Entwicklung):**
     Detaillierte Beschreibung der JavaScript-Programmierung in `.cps` *(Funktionen `onOpen()`, `onSection()`, `onLinear()`, `onCircular()`, `onCyclePoint()`, `onClose()`)*, Konsistenzprüfung der Werkzeugliste *(Tool Table)* und Generierung des NC-Maschinencodes (`.nc`).
   * **Phase 4: Agent 3 (Qualitätssicherung, Crash-Schutz & Werkstattdokumentation):**
     5-Stufen-Sicherheitsüberprüfung, rechnerischer Nachweis des Z-MIN-Kollisionsabstands zu den Schraubstockbacken *(Tunnel-Prinzip)*, Erstellung des Werkstatt-Einrichteblatts (`Setup Sheet`) und Rendering bzw. Bereitstellung des 3D-Simulationsvideos.
   * **Phase 5: Agent 4 (Kaufmännische Abrechnung):**
     Erstellung der steuerkonformen Honorarrechnung nach § 14 UStG *(Umsatzsteuergesetz)* und § 18 EStG ohne Gewerbesteuer.

4. **Mathematischer und technischer Verifikationsnachweis:**
   * Exakter Z-MIN-Abgleich *(Schnitttiefe vs. Spannbackenhöhe)*
   * Nullpunkt-Verifikation (`G54` Lage)
   * Schnittdaten-Plausibilität *(Drehzahl $S$, Vorschub $F$, Schnittgeschwindigkeit $v_c$)*

5. **Rechtliche Freigabeerklärung:**
   * Verbindliche Bestätigung, dass die gelieferte Leistung eine reine geistig-schöpferische Ingenieurdienstleistung *(Prozessauslegung, CAM-Bahnplanung, Software-Postprozessor)* darstellt.

---

## 5. Verbindliche Pflicht: Transparente Nennung des aktiven KI-Agenten

Der Assistent muss bei **JEDER Antwort, Prüfung, Code-Generierung und jedem Arbeitsschritt stets explizit und unübersehbar zu Beginn deklarieren, welcher KI-Agent gerade agiert**:
* `🔍 [Aktivierter Agent: Agent 1 – Lead-Scout-Agent]` *(Kundenbriefing & Anforderungsanalyse)*
* `💻 [Aktivierter Agent: Agent 2 – Postprocessor-Coder-Agent]` *(JavaScript .cps Postprozessor-Programmierung)*
* `🛡️ [Aktivierter Agent: Agent 3 – NC-Safety- & Setup-Agent]` *(G-Code-Sicherheitsprüfung, Kollisions-Check & Einrichteblatt)*
* `💰 [Aktivierter Agent: Agent 4 – Backoffice-Ingenieur-Agent]` *(Angebote, Rechnungen nach § 18 EStG & kaufmännische Dokumente)*

Dies stellt sicher, dass der Benutzer jederzeit lückenlos nachvollziehen kann, welcher spezialisierte Agent welche Aufgabe ausführt.


---

## 6. Best-Practice-Ausführung mit `Argon 4` und dem `/goal`-Befehl *(Autonome Gesamt-Abwicklung)*

Um sicherzustellen, dass bei der Bearbeitung eines Kundenauftrags keines der **6+1 Pflicht-Artefakte *(Arbeitsergebnisse)*** vergessen wird und sämtliche Code-Dateien (`.cps` *(Custom Postprocessor Script)* und `.nc` *(Numerical Control G-Code)*) gegen echte **Compiler *(Übersetzer und Syntaxprüfer)*** getestet werden, gilt für die Ausführung in **Google Antigravity *(AGY — Agentenbasierte Entwicklungsumgebung)*** folgende Empfehlung:

1. **Bevorzugtes KI-Modell (`Argon 4`):**
   Für die Postprozessor-Programmierung (**Agent 2**), die statische G-Code-Kollisionsprüfung (**Agent 3**) und die steuerrechtlich präzise Abrechnung nach **§ 18 EStG *(Einkommensteuergesetz)*** (**Agent 4**) ist **`Argon 4`** zu wählen, da es komplexe logische Abhängigkeiten *(wie `xOutput.reset()` bei 360°-Vollkreisen und `G80`-Zyklusaufhebungen)* mittels echter Terminal-Prüfskripte verifiziert.
2. **Einsatz des `/goal`-Befehls *(Zielorientierter Ausdauer-Modus)*:**
   * **Komplett-Abwicklung (Modus A):** Soll ein Kundenauftrag von A bis Z in einem einzigen Durchgang abgearbeitet werden, wird der Prompt mit **`/goal`** eingeleitet. Dadurch arbeitet das System alle 4 Schritte (**Agent 4 ➔ Agent 2 ➔ Agent 3 ➔ Agent 4**) ohne vorzeitigen Abbruch ab und beendet den Lauf erst, wenn alle **6+1 Dateien** (`02_...`, `.cps`/`.nc`, `05_...`, `06_...`, `.mp4`, `07_...`, `08_...`) physisch im Auftragsordner verifiziert wurden.
   * **Zweistufiger Echtkunden-Betrieb (Modus B):** Im realen Tagesgeschäft wird bei Eingang einer Anfrage zunächst nur **Agent 4** für das Festpreis-Angebot (`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`) gestartet. Sobald die Auftragsbestätigung des Kunden vorliegt, wird mit **`/goal`** die gesamte technische Umsetzung und Abrechnung *(Stationen `03` bis `08`)* in einem Durchgang ausgeführt.
