# 🛠️ CNC / CAD-CAM Engineering & Postprocessor Portfolio

**Dipl.-Ing. & Senior Software Engineer** | Location: Erlensee (Rhein-Main / Frankfurt / Hanau & Fürth / Nürnberg)  
**Focus:** 2.5D / 3+2 / 5-Axis Simultaneous CAM Programming • Custom Postprocessor Development (Heidenhain TNC / Siemens Sinumerik) • CAM API & Shopfloor Automation

---

## 🇩🇪 Überblick (Deutsch)

Dieses Repository dokumentiert praxisnahe Referenzprojekte aus der **CAD/CAM-Fertigungstechnik *(rechnerunterstützte Konstruktion und CNC-Programmierung)*** sowie **Software-Tools zur Automatisierung der Arbeitsvorbereitung *(Postprozessoren, NC-Code-Parser und automatische Einrichteblatt-Generatoren)***.

### 📂 Enthaltene Engineering-Pakete & Tools

1. **[Projekt 01 – 2,5D-Präzisionsfrästeil (42CrMo4)](../Portfolio/Projekt_01_25D_Praezisionsfraesteil/Fertigungspaket_Projekt_01.md)**
   * Komplettbearbeitung in 2 Aufspannungen (`OP10` / `OP20`), Passungsfräsen $\varnothing\,52\,\text{H7}$ mit Werkzeugradiuskorrektur (`RL` / `G41`) und prozesssicheres Gewindefräsen (`CYCL DEF 262`).
2. **[Projekt 02 – 3+2-Achsen-Mehrseitenbearbeitung (Hydraulik-Ventilblock EN AW-7075)](../Portfolio/Projekt_02_3plus2_Mehrseiten_Ventilblock/Fertigungspaket_Projekt_02.md)**
   * 5-Seiten-Komplettbearbeitung in einer Aufspannung auf 5-Achs-Bearbeitungszentrum mit Raumwinkel-Transformation über `PLANE SPATIAL` (Heidenhain TNC 640) und `CYCLE800` (Siemens Sinumerik).
3. **[Projekt 03 – 3D-Freiformflächen & 5-Achs-Simultanbearbeitung](../Portfolio/Projekt_03_3D_Freiform_und_5Achs/Fertigungspaket_Projekt_03.md)**
   * Mathematisch geglättete Vektorführung (`TX/TY/TZ` bzw. `A3/B3/C3`), Einsatz von Kreissegmentfräsern *(Tonnenfräsern)* und HSC-Toleranzzyklen (`FUNCTION TCPM` / `CYCL DEF 32` & `TRAORI` / `CYCLE832`).
4. **[Projekt 04 – Postprozessor-Engineering & Shopfloor-Automatisierung](../Portfolio/Projekt_04_Postprozessor_und_CAM_Automatisierung/Fertigungspaket_Projekt_04.md)**
   * Maßgeschneiderte Postprozessor-Erweiterungen (automatische Berechnung der Mindest-Auskraglänge $L_{\text{min}}$, automatische Laser-Werkzeugbruchkontrolle `TCH PROBE 586`).
5. **[Python-Tool: `cnc_setup_sheet_extractor.py`](./cnc_setup_sheet_extractor.py)**
   * Ein Kommandozeilen- und Automatisierungstool in Python, das fertige **Heidenhain Klartext (`.H`)** und **Siemens Sinumerik (`.MPF`)** NC-Programme statisch analysiert, Rohteilabmessungen (`BLK FORM` / `WORKPIECE`), Nullpunkte, maximale $Z$-Tiefen sowie alle Werkzeugaufrufe (`TOOL CALL` / `T="..."`) extrahiert und automatisch ein druckfertiges **Einrichteblatt (Setup Sheet)** im Markdown-Format erzeugt.

---

## 🚀 Schnellstart: Automatischer Einrichteblatt-Generator (`cnc_setup_sheet_extractor.py`)

Mit diesem Skript lassen sich bestehende NC-Programme in Sekundenschnelle dokumentieren und auf kritische Einstichtiefen ($Z_{\text{min}}$) prüfen:

```bash
python cnc_setup_sheet_extractor.py pfad/zum/programm.H --output einrichteblatt.md
```

### Funktionsumfang des Parsers:
* Automatische Steuerungserkennung (**Heidenhain Klartext** vs. **Siemens Sinumerik DIN/ISO**).
* Auslesen der Rohteil-Grenzwerte (`BLK FORM 0.1 / 0.2` bzw. `WORKPIECE(...)`) und Berechnung der Rohteilabmessungen ($\Delta X \times \Delta Y \times \Delta Z$).
* Extraktion aller Werkzeugaufrufe inklusive Spindeldrehzahl ($S$), Vorschub ($F$), Kühlmittelstatus (`M7` Innenkühlung / `M8` Außenkühlung) und tiefster $Z$-Koordinate pro Werkzeug zur Ermittlung der **erforderlichen Mindest-Auskraglänge ($L_{\text{min}}$)**.

---

## 🇬🇧 Overview (English)

This repository showcases industrial **CAD/CAM Manufacturing Engineering packages** alongside **custom software tools for CNC shopfloor automation** (combining classical Mechanical/Civil Engineering geometry & mechanics with modern Software Engineering).

* **Multi-Axis CAM Programming:** 2.5D prismatic milling, 3+2 indexed 5-axis machining (`PLANE SPATIAL` / `CYCLE800`), and 5-axis simultaneous surface finishing (`FUNCTION TCPM` / `TRAORI`).
* **Postprocessor Development:** Custom JavaScript, Python, and Tcl postprocessors with automated minimum tool overhang calculation ($L_{\text{min}}$) and automatic laser tool breakage probing (`TCH PROBE 586`).
* **NC Code Static Analysis & Setup Sheet Generation:** Automated Python parser (`cnc_setup_sheet_extractor.py`) turning raw Heidenhain `.H` and Siemens `.MPF` G-code into structured shopfloor setup sheets.
