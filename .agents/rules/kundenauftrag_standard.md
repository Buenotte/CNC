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
1. `02_ANGEBOT_DIPL_ING_BUENOTTE.md` *(B2B-Angebot nach § 18 EStG)*
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
