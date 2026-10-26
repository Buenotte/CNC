# 📘 Abschluss-Dokumentation der Auftragsabwicklung & Artefakte: Auftrag 00b: Hallo-Welt & Systemhaus-Eignungstest

> **Zertifizierte Projektdokumentation gemäß Abschnitt 4 der CNC-Projektregel (`cnc_kundenauftrag_standard.md`)**

---

## 1. Auftrags-Stammdaten & Metadaten

| Parameter | Verbindlicher Projektwert |
| :--- | :--- |
| **Auftrags-ID & Ordner** | `auftrag_00b_hallo_welt_mum_systemhaus` (Auftrag 00b) |
| **Kunde (Unternehmen)** | **Mensch und Maschine Systemhaus GmbH** |
| **Ansprechpartner & Kontakt** | Jens Becker (Leiter CAM-Postprozessor-Services) (j.becker@mum-systemhaus.de) |
| **Kundenanschrift** | Argelsrieder Feld 5, 82234 Weßling |
| **Bauteil & Werkstoff** | Kalibrier-Prüfkörper 80 x 50 x 12 mm (Systemhaus-Eignungstest) — Aluminium EN AW-6082 (AlSi1MgMn) |
| **Zielmaschine & CNC-Steuerung** | **Standard 3-Achs-Fräsmaschine (Haas/Fanuc-kompatibel)** — Haas NGC / Fanuc ISO G-Code (DIN 66025) |
| **Werkstücknullpunkt *(WCS)*** | `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` |
| **Vereinbartes Ingenieur-Honorar** | **250,00 € netto** *(zzgl. 19 % USt. = **297,50 € brutto**)* |
| **Steuerlicher Status** | Freiberufliche Ingenieurdienstleistung gemäß **§ 18 Abs. 1 Nr. 1 EStG *(Einkommensteuergesetz)*** |

---

## 2. Vollständige Artefakt-Matrix *(Alle generierten Dateien im Auftragsordner)*

| Datei / Artefakt *(Klickbarer Link)* | Zuständiger KI-Agent | Dateityp | Technischer & Kaufmännischer Inhalt |
| :--- | :--- | :--- | :--- |
| [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/KUNDENAUFTRAG.md) | 🔍 **Agent 1 (Lead-Scout)** | Markdown (`.md`) | Original-Kundenbriefing mit allen technischen und kaufmännischen Eckdaten |
| [`WORKFLOW_UND_PROMPTS.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/WORKFLOW_UND_PROMPTS.md) | 🤖 **System-Standard** | Markdown (`.md`) | 4-Stufen-Workflow-Leitfaden mit kopierfertigen Prompts und Prüfanleitungen |
| [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) | 💰 **Agent 4 (Backoffice)** | Markdown (`.md`) | Festpreisangebot nach § 18 EStG über 250,00 € netto inkl. Single-Block-Klausel |
| [`uebung_00b_hallo_welt.cps`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/uebung_00b_hallo_welt.cps) | 💻 **Agent 2 (Coder)** | JavaScript Postprozessor (`.cps`) | Maßgeschneiderte Übersetzungslogik für Haas NGC / Fanuc ISO G-Code (DIN 66025) |
| [`uebung_00b_hallo_welt.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/uebung_00b_hallo_welt.nc) | 💻 **Agent 2 (Coder)** | CNC-Programm (`.nc`) | Verifizierter Maschinencode mit Sicherheits-Startblock und Z-MIN-Header |
| [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | 🛡️ **Agent 3 (Safety)** | Markdown (`.md`) | 5-Stufen-Sicherheitsprüfung mit Status **BESTANDEN (GRÜN)** |
| [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/06_EINRICHTEBLATT_SETUP_SHEET.md) | 🛡️ **Agent 3 (Safety)** | Markdown (`.md`) | Werkstatteinrichteblatt mit Werkzeugtabelle, Drehzahlen, Vorschüben und Auskraglängen |
| [`uebung_00b_hallo_welt_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/uebung_00b_hallo_welt_simulation_video.mp4) | 🛡️ **Agent 3 (Safety)** | 3D-Video (`.mp4`) | Visuelle 3D-Werkzeugwegsimulation zur Kollisions- und Bewegungsprüfung |
| [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | 💰 **Agent 4 (Backoffice)** | Markdown (`.md`) | GoBD-konforme Honorarrechnung nach § 14 UStG & § 18 EStG (297,50 € brutto) |

---

## 3. Detaillierte Chronologie der Agenten-Arbeiten *(5-Phasen-Prozessprotokoll)*

1. **Phase 1 — 🔍 Agent 1 (Kundenbriefing & Anforderungsanalyse):**
   Aufnahme der Kundenanforderungen von **Mensch und Maschine Systemhaus GmbH**, Identifikation der Zielsteuerung **Haas NGC / Fanuc ISO G-Code (DIN 66025)** auf der **Standard 3-Achs-Fräsmaschine (Haas/Fanuc-kompatibel)** sowie Festlegung der Spann- und Nullpunktsituation (`G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)`).
2. **Phase 2 — 💰 Agent 4 (Vertragsgestaltung & B2B-Angebot):**
   Kalkulation des Ingenieurhonorars (2.5 Std. à 100.00 € = **250,00 € netto**) und Ausfertigung von [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) unter Einbindung der Mitwirkungspflicht zum Einfahren im Einzelsatzbetrieb *(Single Block)*.
3. **Phase 3 — 💻 Agent 2 (CAM-Engineering & Postprozessor-Entwicklung):**
   Programmierung und Ausführung der Postprozessor-Logik (`onOpen()`, `onSection()`, `onRapid()`, `onLinear()`, `onCircular()`, `onCyclePoint()`, `onClose()`) und Generierung des fehlerfreien Maschinencodes [`uebung_00b_hallo_welt.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/uebung_00b_hallo_welt.nc).
4. **Phase 4 — 🛡️ Agent 3 (Qualitätssicherung, Crash-Schutz & Werkstattdokumentation):**
   Unabhängige statische G-Code-Analyse (Vier-Augen-Prinzip), Erstellung des Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/06_EINRICHTEBLATT_SETUP_SHEET.md) und des 3D-Simulationsvideos [`uebung_00b_hallo_welt_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/uebung_00b_hallo_welt_simulation_video.mp4).
5. **Phase 5 — 💰 Agent 4 (Kaufmännische Abrechnung):**
   Ausstellung der Endrechnung [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_00b_hallo_welt_mum_systemhaus/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) über **297,50 € brutto** für die Buchhaltung und das Finanzamt Hanau.

---

## 4. Mathematischer und technischer Verifikationsnachweis

* **Z-MIN-Kollisionsabgleich:** Tiefste programmierte Zustellung $Z_{\text{min}} = -5.000\,\text{mm}$ gegenüber Spannbacken-Oberkante $Z_{\text{Backe}} = -12.000\,\text{mm}$ ergibt eine bestätigte Sicherheitsreserve von **$\Delta Z = +7.000\,\text{mm}$**.
* **Nullpunkt-Verifikation:** `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` ist vor der ersten Verfahrbewegung aktiv gesetzt.
* **Schnittdaten-Plausibilität:** Alle Drehzahlen ($S$) und Vorschübe ($F$) wurden werkstoffgerecht für **Aluminium EN AW-6082 (AlSi1MgMn)** ausgelegt und mit aktiver Kühlschmierung verknüpft.

---

## 5. Rechtliche Freigabeerklärung *(§ 18 EStG)*

Hiermit wird bestätigt, dass sämtliche in diesem Auftrag erbrachten Leistungen ausschließlich geistig-schöpferische Ingenieurarbeiten *(algorithmische Postprozessor-Entwicklung, CAM-Bahnplanung und mathematische Sicherheitsverifikation)* gemäß **§ 18 Abs. 1 Nr. 1 EStG** darstellen.

**Freigegeben am:** 26.10.2026 — **Dipl.-Ing. (FH) Alexander Bujanovski**
