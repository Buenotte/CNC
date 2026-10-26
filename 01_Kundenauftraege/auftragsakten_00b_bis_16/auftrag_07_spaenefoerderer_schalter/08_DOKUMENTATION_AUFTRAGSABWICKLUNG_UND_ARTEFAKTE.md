# 📘 Abschluss-Dokumentation der Auftragsabwicklung & Artefakte: Auftrag 07: Konfigurierbare Postprozessor-Properties (Späneförderer M31/M33)

> **Zertifizierte Projektdokumentation gemäß Abschnitt 4 der CNC-Projektregel (`cnc_kundenauftrag_standard.md`)**

---

## 1. Auftrags-Stammdaten & Metadaten

| Parameter | Verbindlicher Projektwert |
| :--- | :--- |
| **Auftrags-ID & Ordner** | `auftrag_07_spaenefoerderer_schalter` (Auftrag 07) |
| **Kunde (Unternehmen)** | **Vogtland Zerspanungstechnik GmbH** |
| **Ansprechpartner & Kontakt** | Karsten Wolf (Technischer Leiter) (k.wolf@vogtland-zerspanung.de) |
| **Kundenanschrift** | Plauener Straße 22, 08523 Plauen |
| **Bauteil & Werkstoff** | Hochvolumen-Aluminiumgehäuse (90 % Zerspanungsvolumen) — Aluminium EN AW-6060 (AlMgSi0,5) |
| **Zielmaschine & CNC-Steuerung** | **Alzmetall CS 1200 (ISO G-Code-Modus)** — ISO G-Code (mit M31/M33 Späneförderer-Ansteuerung) |
| **Werkstücknullpunkt *(WCS)*** | `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` |
| **Vereinbartes Ingenieur-Honorar** | **390,00 € netto** *(zzgl. 19 % USt. = **464,10 € brutto**)* |
| **Steuerlicher Status** | Freiberufliche Ingenieurdienstleistung gemäß **§ 18 Abs. 1 Nr. 1 EStG *(Einkommensteuergesetz)*** |

---

## 2. Vollständige Artefakt-Matrix *(Alle generierten Dateien im Auftragsordner)*

| Datei / Artefakt *(Klickbarer Link)* | Zuständiger KI-Agent | Dateityp | Technischer & Kaufmännischer Inhalt |
| :--- | :--- | :--- | :--- |
| [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/KUNDENAUFTRAG.md) | 🔍 **Agent 1 (Lead-Scout)** | Markdown (`.md`) | Original-Kundenbriefing mit allen technischen und kaufmännischen Eckdaten |
| [`WORKFLOW_UND_PROMPTS.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/WORKFLOW_UND_PROMPTS.md) | 🤖 **System-Standard** | Markdown (`.md`) | 4-Stufen-Workflow-Leitfaden mit kopierfertigen Prompts und Prüfanleitungen |
| [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) | 💰 **Agent 4 (Backoffice)** | Markdown (`.md`) | Festpreisangebot nach § 18 EStG über 390,00 € netto inkl. Single-Block-Klausel |
| [`uebung_07_spaenefoerderer_schalter.cps`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/uebung_07_spaenefoerderer_schalter.cps) | 💻 **Agent 2 (Coder)** | JavaScript Postprozessor (`.cps`) | Maßgeschneiderte Übersetzungslogik für ISO G-Code (mit M31/M33 Späneförderer-Ansteuerung) |
| [`uebung_07_spaenefoerderer_schalter.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/uebung_07_spaenefoerderer_schalter.nc) | 💻 **Agent 2 (Coder)** | CNC-Programm (`.nc`) | Verifizierter Maschinencode mit Sicherheits-Startblock und Z-MIN-Header |
| [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | 🛡️ **Agent 3 (Safety)** | Markdown (`.md`) | 5-Stufen-Sicherheitsprüfung mit Status **BESTANDEN (GRÜN)** |
| [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/06_EINRICHTEBLATT_SETUP_SHEET.md) | 🛡️ **Agent 3 (Safety)** | Markdown (`.md`) | Werkstatteinrichteblatt mit Werkzeugtabelle, Drehzahlen, Vorschüben und Auskraglängen |
| [`uebung_07_spaenefoerderer_schalter_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/uebung_07_spaenefoerderer_schalter_simulation_video.mp4) | 🛡️ **Agent 3 (Safety)** | 3D-Video (`.mp4`) | Visuelle 3D-Werkzeugwegsimulation zur Kollisions- und Bewegungsprüfung |
| [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | 💰 **Agent 4 (Backoffice)** | Markdown (`.md`) | GoBD-konforme Honorarrechnung nach § 14 UStG & § 18 EStG (464,10 € brutto) |

---

## 3. Detaillierte Chronologie der Agenten-Arbeiten *(5-Phasen-Prozessprotokoll)*

1. **Phase 1 — 🔍 Agent 1 (Kundenbriefing & Anforderungsanalyse):**
   Aufnahme der Kundenanforderungen von **Vogtland Zerspanungstechnik GmbH**, Identifikation der Zielsteuerung **ISO G-Code (mit M31/M33 Späneförderer-Ansteuerung)** auf der **Alzmetall CS 1200 (ISO G-Code-Modus)** sowie Festlegung der Spann- und Nullpunktsituation (`G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)`).
2. **Phase 2 — 💰 Agent 4 (Vertragsgestaltung & B2B-Angebot):**
   Kalkulation des Ingenieurhonorars (3.9 Std. à 100.00 € = **390,00 € netto**) und Ausfertigung von [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) unter Einbindung der Mitwirkungspflicht zum Einfahren im Einzelsatzbetrieb *(Single Block)*.
3. **Phase 3 — 💻 Agent 2 (CAM-Engineering & Postprozessor-Entwicklung):**
   Programmierung und Ausführung der Postprozessor-Logik (`onOpen()`, `onSection()`, `onRapid()`, `onLinear()`, `onCircular()`, `onCyclePoint()`, `onClose()`) und Generierung des fehlerfreien Maschinencodes [`uebung_07_spaenefoerderer_schalter.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/uebung_07_spaenefoerderer_schalter.nc).
4. **Phase 4 — 🛡️ Agent 3 (Qualitätssicherung, Crash-Schutz & Werkstattdokumentation):**
   Unabhängige statische G-Code-Analyse (Vier-Augen-Prinzip), Erstellung des Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/06_EINRICHTEBLATT_SETUP_SHEET.md) und des 3D-Simulationsvideos [`uebung_07_spaenefoerderer_schalter_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/uebung_07_spaenefoerderer_schalter_simulation_video.mp4).
5. **Phase 5 — 💰 Agent 4 (Kaufmännische Abrechnung):**
   Ausstellung der Endrechnung [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_07_spaenefoerderer_schalter/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) über **464,10 € brutto** für die Buchhaltung und das Finanzamt Hanau.

---

## 4. Mathematischer und technischer Verifikationsnachweis

* **Z-MIN-Kollisionsabgleich:** Tiefste programmierte Zustellung $Z_{\text{min}} = -5.000\,\text{mm}$ gegenüber Spannbacken-Oberkante $Z_{\text{Backe}} = -15.000\,\text{mm}$ ergibt eine bestätigte Sicherheitsreserve von **$\Delta Z = +10.000\,\text{mm}$**.
* **Nullpunkt-Verifikation:** `G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)` ist vor der ersten Verfahrbewegung aktiv gesetzt.
* **Schnittdaten-Plausibilität:** Alle Drehzahlen ($S$) und Vorschübe ($F$) wurden werkstoffgerecht für **Aluminium EN AW-6060 (AlMgSi0,5)** ausgelegt und mit aktiver Kühlschmierung verknüpft.

---

## 5. Rechtliche Freigabeerklärung *(§ 18 EStG)*

Hiermit wird bestätigt, dass sämtliche in diesem Auftrag erbrachten Leistungen ausschließlich geistig-schöpferische Ingenieurarbeiten *(algorithmische Postprozessor-Entwicklung, CAM-Bahnplanung und mathematische Sicherheitsverifikation)* gemäß **§ 18 Abs. 1 Nr. 1 EStG** darstellen.

**Freigegeben am:** 26.10.2026 — **Dipl.-Ing. (FH) Alexander Bujanovski**
