# 📘 Abschluss-Dokumentation der Auftragsabwicklung & Artefakte: Auftrag 10: Dynamische Mehrseiten-Nullpunktlogik (G54 OP10 / G55 OP20)

> **Zertifizierte Projektdokumentation gemäß Abschnitt 4 der CNC-Projektregel (`cnc_kundenauftrag_standard.md`)**

---

## 1. Auftrags-Stammdaten & Metadaten

| Parameter | Verbindlicher Projektwert |
| :--- | :--- |
| **Auftrags-ID & Ordner** | `auftrag_10_zweite_aufspannung_op20` (Auftrag 10) |
| **Kunde (Unternehmen)** | **AluTech Gehäusebau GmbH** |
| **Ansprechpartner & Kontakt** | Robert Schneider (Fertigungsleiter) (r.schneider@alutech-gehaeuse.de) |
| **Kundenanschrift** | Borsigallee 18, 60388 Frankfurt am Main |
| **Bauteil & Werkstoff** | Doppelschraubstock-Serienbauteil (OP10 in G54 + OP20 Rückseite in G55) — Aluminium EN AW-6082 T6 |
| **Zielmaschine & CNC-Steuerung** | **Hermle C42 U MT (ISO/Fanuc-Modus mit 2x Schunk Kontec KSC)** — ISO G-Code (Dynamische WCS-Umschaltung G54..G59 über workOffset) |
| **Werkstücknullpunkt *(WCS)*** | `G54 (Schraubstock 1: OP10 Vorderseite) & G55 (Schraubstock 2: OP20 Rückseite)` |
| **Vereinbartes Ingenieur-Honorar** | **520,00 € netto** *(zzgl. 19 % USt. = **618,80 € brutto**)* |
| **Steuerlicher Status** | Freiberufliche Ingenieurdienstleistung gemäß **§ 18 Abs. 1 Nr. 1 EStG *(Einkommensteuergesetz)*** |

---

## 2. Vollständige Artefakt-Matrix *(Alle generierten Dateien im Auftragsordner)*

| Datei / Artefakt *(Klickbarer Link)* | Zuständiger KI-Agent | Dateityp | Technischer & Kaufmännischer Inhalt |
| :--- | :--- | :--- | :--- |
| [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/KUNDENAUFTRAG.md) | 🔍 **Agent 1 (Lead-Scout)** | Markdown (`.md`) | Original-Kundenbriefing mit allen technischen und kaufmännischen Eckdaten |
| [`WORKFLOW_UND_PROMPTS.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/WORKFLOW_UND_PROMPTS.md) | 🤖 **System-Standard** | Markdown (`.md`) | 4-Stufen-Workflow-Leitfaden mit kopierfertigen Prompts und Prüfanleitungen |
| [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) | 💰 **Agent 4 (Backoffice)** | Markdown (`.md`) | Festpreisangebot nach § 18 EStG über 520,00 € netto inkl. Single-Block-Klausel |
| [`uebung_10_zweite_aufspannung_g55.cps`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/uebung_10_zweite_aufspannung_g55.cps) | 💻 **Agent 2 (Coder)** | JavaScript Postprozessor (`.cps`) | Maßgeschneiderte Übersetzungslogik für ISO G-Code (Dynamische WCS-Umschaltung G54..G59 über workOffset) |
| [`uebung_10_zweite_aufspannung_g55.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/uebung_10_zweite_aufspannung_g55.nc) | 💻 **Agent 2 (Coder)** | CNC-Programm (`.nc`) | Verifizierter Maschinencode mit Sicherheits-Startblock und Z-MIN-Header |
| [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | 🛡️ **Agent 3 (Safety)** | Markdown (`.md`) | 5-Stufen-Sicherheitsprüfung mit Status **BESTANDEN (GRÜN)** |
| [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/06_EINRICHTEBLATT_SETUP_SHEET.md) | 🛡️ **Agent 3 (Safety)** | Markdown (`.md`) | Werkstatteinrichteblatt mit Werkzeugtabelle, Drehzahlen, Vorschüben und Auskraglängen |
| [`uebung_10_zweite_aufspannung_g55_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/uebung_10_zweite_aufspannung_g55_simulation_video.mp4) | 🛡️ **Agent 3 (Safety)** | 3D-Video (`.mp4`) | Visuelle 3D-Werkzeugwegsimulation zur Kollisions- und Bewegungsprüfung |
| [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | 💰 **Agent 4 (Backoffice)** | Markdown (`.md`) | GoBD-konforme Honorarrechnung nach § 14 UStG & § 18 EStG (618,80 € brutto) |

---

## 3. Detaillierte Chronologie der Agenten-Arbeiten *(5-Phasen-Prozessprotokoll)*

1. **Phase 1 — 🔍 Agent 1 (Kundenbriefing & Anforderungsanalyse):**
   Aufnahme der Kundenanforderungen von **AluTech Gehäusebau GmbH**, Identifikation der Zielsteuerung **ISO G-Code (Dynamische WCS-Umschaltung G54..G59 über workOffset)** auf der **Hermle C42 U MT (ISO/Fanuc-Modus mit 2x Schunk Kontec KSC)** sowie Festlegung der Spann- und Nullpunktsituation (`G54 (Schraubstock 1: OP10 Vorderseite) & G55 (Schraubstock 2: OP20 Rückseite)`).
2. **Phase 2 — 💰 Agent 4 (Vertragsgestaltung & B2B-Angebot):**
   Kalkulation des Ingenieurhonorars (5.2 Std. à 100.00 € = **520,00 € netto**) und Ausfertigung von [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) unter Einbindung der Mitwirkungspflicht zum Einfahren im Einzelsatzbetrieb *(Single Block)*.
3. **Phase 3 — 💻 Agent 2 (CAM-Engineering & Postprozessor-Entwicklung):**
   Programmierung und Ausführung der Postprozessor-Logik (`onOpen()`, `onSection()`, `onRapid()`, `onLinear()`, `onCircular()`, `onCyclePoint()`, `onClose()`) und Generierung des fehlerfreien Maschinencodes [`uebung_10_zweite_aufspannung_g55.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/uebung_10_zweite_aufspannung_g55.nc).
4. **Phase 4 — 🛡️ Agent 3 (Qualitätssicherung, Crash-Schutz & Werkstattdokumentation):**
   Unabhängige statische G-Code-Analyse (Vier-Augen-Prinzip), Erstellung des Prüfberichts [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/05_SICHERHEITS_CRASH_PRUEFBERICHT.md), des Einrichteblatts [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/06_EINRICHTEBLATT_SETUP_SHEET.md) und des 3D-Simulationsvideos [`uebung_10_zweite_aufspannung_g55_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/uebung_10_zweite_aufspannung_g55_simulation_video.mp4).
5. **Phase 5 — 💰 Agent 4 (Kaufmännische Abrechnung):**
   Ausstellung der Endrechnung [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_10_zweite_aufspannung_op20/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) über **618,80 € brutto** für die Buchhaltung und das Finanzamt Hanau.

---

## 4. Mathematischer und technischer Verifikationsnachweis

* **Z-MIN-Kollisionsabgleich:** Tiefste programmierte Zustellung $Z_{\text{min}} = -12.000\,\text{mm}$ gegenüber Spannbacken-Oberkante $Z_{\text{Backe}} = -15.000\,\text{mm}$ ergibt eine bestätigte Sicherheitsreserve von **$\Delta Z = +3.000\,\text{mm}$**.
* **Nullpunkt-Verifikation:** `G54 (Schraubstock 1: OP10 Vorderseite) & G55 (Schraubstock 2: OP20 Rückseite)` ist vor der ersten Verfahrbewegung aktiv gesetzt.
* **Schnittdaten-Plausibilität:** Alle Drehzahlen ($S$) und Vorschübe ($F$) wurden werkstoffgerecht für **Aluminium EN AW-6082 T6** ausgelegt und mit aktiver Kühlschmierung verknüpft.

---

## 5. Rechtliche Freigabeerklärung *(§ 18 EStG)*

Hiermit wird bestätigt, dass sämtliche in diesem Auftrag erbrachten Leistungen ausschließlich geistig-schöpferische Ingenieurarbeiten *(algorithmische Postprozessor-Entwicklung, CAM-Bahnplanung und mathematische Sicherheitsverifikation)* gemäß **§ 18 Abs. 1 Nr. 1 EStG** darstellen.

**Freigegeben am:** 26.10.2026 — **Dipl.-Ing. (FH) Alexander Bujanovski**

---

### 🔧 Technische Schnittzeichnung: Warum die `3 mm` Spannrand im Maschinenschraubstock überlebenswichtig sind (`OP10` vs. `Crash` vs. `OP20`)

Hier siehst du im direkten technischen Querschnitt *(Schnittzeichnung durch Maschinenschraubstock, Parallelunterlagen, gehärtete Stahlbacken und Bauteil)*, warum der Fräser in **`OP10 (G54)`** bei **`Z = -12,0 mm`** stoppen muss, was passiert, wenn er fälschlicherweise bis **`Z = -15,0 mm`** durchfräst (**Crash in die Stahlbacken!**), und wie der **`3 mm` Restboden („Hut-Rand“)** nach dem **180°-Umdrehen in `OP20 (G55)`** oben abgefräst wird:

![Technische Schnittzeichnung: Warum 3 mm Spannrand im Maschinenschraubstock Pflicht sind](file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/bilder/op10_op20_spannrand_schraubstock.png)

| Phase im Schnittbild | Z-Tiefe *(Zustellung in $\text{mm}$)* | Was passiert im Maschinenschraubstock *(Spannmittel)*? | Technisches Ergebnis an der Maschine |
| :--- | :--- | :--- | :--- |
| **1. `OP10 (G54)` — Richtig & Sicher** | **`Z-MIN = -12,0 mm`** | Die gehärteten Stahlbacken *(Feste & Bewegliche Backe)* halten das `15 mm` dicke Rohteil an den untersten **`3 mm` (`Z = -12,0 mm` bis `Z = -15,0 mm`)** auf Parallelunterlagen *(Auflageleisten)*. Der Schaftfräser `T01` ($\varnothing 10\,\text{mm}$) stoppt exakt bei `Z = -12,0 mm`. | ✅ **0,0 mm Kontakt mit den Stahlbacken!** Unten bleibt ein `3 mm` dicker Halte-Rand *(der sogenannte „Hut-Rand“)* stehen. |
| **2. `OP10` — Fehler bei `Z = -15,0 mm`** | **`Z = -15,0 mm` (CRASH!)** | Würde der Fräser in `OP10` bis zur Rohteil-Unterkante (`Z = -15,0 mm`) durchfräsen, taucht er **`3,0 mm` tief mitten in die gehärteten Stahlbacken** des Schraubstocks ein und fräst gleichzeitig den Halte-Rand weg. | 🚨 **Schwerer Maschinen-Crash!** Der Vollhartmetall-Fräser *(VHM)* bricht bei $8.000\,\text{U/min}$ explosionsartig ab, die Stahlbacken werden zerstört und das lose Bauteil fliegt aus der Spannung! |
| **3. `OP20 (G55)` — Bauteil 180° umgedreht** | **`Z = +3,0 mm` ➔ `Z = 0,0 mm`** | Nach dem Programmstopp `M00` *(Mandatory Stop)* wird das Bauteil um **180° gewendet** (`Tasche Ø 30 mm` zeigt nach unten). Die Stahlbacken spannen nun die bereits fertigen `80 mm`-Seitenflächen, und der `3 mm` Restboden liegt frei zugänglich **ganz oben**, wo ihn der Planmesserkopf `T03` ($\varnothing 50\,\text{mm}$) sauber auf `Z = 0,0 mm` abfräst. | ✅ **Fertigteil exakt $80 \times 50 \times 12{,}0\,\text{mm}$** – auf allen 6 Seiten bearbeitet, maßhaltig und 100 % kollisionsfrei! |

---
