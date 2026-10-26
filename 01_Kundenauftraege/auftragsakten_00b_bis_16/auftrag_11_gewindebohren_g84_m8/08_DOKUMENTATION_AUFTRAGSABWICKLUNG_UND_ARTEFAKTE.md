# 📘 Abschluss-Dokumentation der Auftragsabwicklung & Artefakte: Auftrag 11: Synchron-Gewindebohren (Rigid Tapping M29 + G84 für M8x1,25)

> **Zertifizierte Projektdokumentation gemäß Abschnitt 4 der CNC-Projektregel (`cnc_kundenauftrag_standard.md`)**

---

## 1. Auftrags-Stammdaten & Metadaten

| Parameter | Verbindlicher Projektwert |
| :--- | :--- |
| **Auftrags-ID & Ordner** | `auftrag_11_gewindebohren_g84_m8` (Auftrag 11) |
| **Kunde (Unternehmen)** | **Meyer Hydraulikkomponenten GmbH** |
| **Ansprechpartner & Kontakt** | Christian Meyer (Fertigungsleiter) (c.meyer@meyer-hydraulik.de) |
| **Kundenanschrift** | Dieselstraße 9, 86154 Augsburg |
| **Bauteil & Werkstoff** | Getriebeflanschplatte mit 4x Befestigungsgewinde M8 (Steigung P = 1,25 mm) — Baustahl S235JR / C45 (1.0503) |
| **Zielmaschine & CNC-Steuerung** | **Haas VF-4SS (Haas NGC Steuerung)** — Haas NGC / Fanuc ISO (Synchron-Gewindebohren M29 S500 + G84 F625) |
| **Werkstücknullpunkt *(WCS)*** | `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` |
| **Vereinbartes Ingenieur-Honorar** | **460,00 € netto** *(zzgl. 19 % USt. = **547,40 € brutto**)* |
| **Steuerlicher Status** | Freiberufliche Ingenieurdienstleistung gemäß **§ 18 Abs. 1 Nr. 1 EStG *(Einkommensteuergesetz)*** |

---

## 2. Vollständige Artefakt-Matrix *(Alle generierten Dateien im Auftragsordner)*

| Datei / Artefakt *(Klickbarer Link)* | Zuständiger KI-Agent | Dateityp | Technischer & Kaufmännischer Inhalt |
| :--- | :--- | :--- | :--- |
| [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/KUNDENAUFTRAG.md) | 🔍 **Agent 1 (Lead-Scout)** | Markdown (`.md`) | Original-Kundenbriefing mit allen technischen und kaufmännischen Eckdaten |
| [`WORKFLOW_UND_PROMPTS.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/WORKFLOW_UND_PROMPTS.md) | 🤖 **System-Standard** | Markdown (`.md`) | 4-Stufen-Workflow-Leitfaden mit kopierfertigen Prompts und Prüfanleitungen |
| [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) | 💰 **Agent 4 (Backoffice)** | Markdown (`.md`) | Festpreisangebot nach § 18 EStG über 460,00 € netto inkl. Single-Block-Klausel |
| [`uebung_11_gewindebohren_g84.cps`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/uebung_11_gewindebohren_g84.cps) | 💻 **Agent 2 (Coder)** | JavaScript Postprozessor (`.cps`) | Maßgeschneiderte Übersetzungslogik für Haas NGC / Fanuc ISO (Synchron-Gewindebohren M29 S500 + G84 F625) |
| [`uebung_11_gewindebohren_g84.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/uebung_11_gewindebohren_g84.nc) | 💻 **Agent 2 (Coder)** | CNC-Programm (`.nc`) | Verifizierter Maschinencode mit Sicherheits-Startblock und Z-MIN-Header |
| [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | 🛡️ **Agent 3 (Safety)** | Markdown (`.md`) | 5-Stufen-Sicherheitsprüfung mit Status **BESTANDEN (GRÜN)** |
| [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/06_EINRICHTEBLATT_SETUP_SHEET.md) | 🛡️ **Agent 3 (Safety)** | Markdown (`.md`) | Werkstatteinrichteblatt mit Werkzeugtabelle, Drehzahlen, Vorschüben und Auskraglängen |
| [`uebung_11_gewindebohren_g84_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/uebung_11_gewindebohren_g84_simulation_video.mp4) | 🛡️ **Agent 3 (Safety)** | 3D-Video (`.mp4`) | Visuelle 3D-Werkzeugwegsimulation zur Kollisions- und Bewegungsprüfung |
| [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | 💰 **Agent 4 (Backoffice)** | Markdown (`.md`) | GoBD-konforme Honorarrechnung nach § 14 UStG & § 18 EStG (547,40 € brutto) |

---

## 3. Detaillierte Chronologie der Agenten-Arbeiten *(5-Phasen-Prozessprotokoll)*

1. **Phase 1 — 🔍 Agent 1 (Kundenbriefing & Anforderungsanalyse):**
   Aufnahme der Kundenanforderungen von **Meyer Hydraulikkomponenten GmbH**, Identifikation der Zielsteuerung **Haas NGC / Fanuc ISO (Synchron-Gewindebohren M29 S500 + G84 F625)** auf der **Haas VF-4SS (Haas NGC Steuerung)** sowie Festlegung der Spann- und Nullpunktsituation (`G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)`).
2. **Phase 2 — 💰 Agent 4 (Vertragsgestaltung & B2B-Angebot):**
   Kalkulation des Ingenieurhonorars (4.6 Std. à 100.00 € = **460,00 € netto**) und Ausfertigung von [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) unter Einbindung der Mitwirkungspflicht zum Einfahren im Einzelsatzbetrieb *(Single Block)*.
3. **Phase 3 — 💻 Agent 2 (CAM-Engineering & Postprozessor-Entwicklung):**
   Programmierung und Ausführung der Postprozessor-Logik (`onOpen()`, `onSection()`, `onRapid()`, `onLinear()`, `onCircular()`, `onCyclePoint()`, `onClose()`) und Generierung des fehlerfreien Maschinencodes [`uebung_11_gewindebohren_g84.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/uebung_11_gewindebohren_g84.nc).
4. **Phase 4 — 🛡️ Agent 3 (Qualitätssicherung, Crash-Schutz & Werkstattdokumentation):**
   Unabhängige statische G-Code-Analyse (Vier-Augen-Prinzip), Erstellung des Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/06_EINRICHTEBLATT_SETUP_SHEET.md) und des 3D-Simulationsvideos [`uebung_11_gewindebohren_g84_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/uebung_11_gewindebohren_g84_simulation_video.mp4).
5. **Phase 5 — 💰 Agent 4 (Kaufmännische Abrechnung):**
   Ausstellung der Endrechnung [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_11_gewindebohren_g84_m8/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) über **547,40 € brutto** für die Buchhaltung und das Finanzamt Hanau.

---

## 4. Mathematischer und technischer Verifikationsnachweis

* **Z-MIN-Kollisionsabgleich:** Tiefste programmierte Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber Spannbacken-Oberkante $Z_{\text{Backe}} = -16.000\,\text{mm}$ ergibt eine bestätigte Sicherheitsreserve von **$\Delta Z = +4.000\,\text{mm}$**.
* **Nullpunkt-Verifikation:** `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` ist vor der ersten Verfahrbewegung aktiv gesetzt.
* **Schnittdaten-Plausibilität:** Alle Drehzahlen ($S$) und Vorschübe ($F$) wurden werkstoffgerecht für **Baustahl S235JR / C45 (1.0503)** ausgelegt und mit aktiver Kühlschmierung verknüpft.

---

## 5. Rechtliche Freigabeerklärung *(§ 18 EStG)*

Hiermit wird bestätigt, dass sämtliche in diesem Auftrag erbrachten Leistungen ausschließlich geistig-schöpferische Ingenieurarbeiten *(algorithmische Postprozessor-Entwicklung, CAM-Bahnplanung und mathematische Sicherheitsverifikation)* gemäß **§ 18 Abs. 1 Nr. 1 EStG** darstellen.

**Freigegeben am:** 26.10.2026 — **Dipl.-Ing. (FH) Alexander Bujanovski**
