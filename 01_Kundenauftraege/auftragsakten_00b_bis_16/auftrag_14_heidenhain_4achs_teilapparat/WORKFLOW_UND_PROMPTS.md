# 📋 Standard-Workflow & Fertige KI-Prompts: Auftrag 14: Heidenhain TNC 640 Klartext-Postprozessor (4-Achs-Indexierung A-Achse)

> **Auftragsordner:** `01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/`  
> **Kunde:** **Alps Precision AG (Schweiz)** (Urs Hodel (Produktionsleiter))  
> **Maschine & Steuerung:** **Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse)** — Heidenhain TNC 640 (Klartext-Dialogprogrammierung .H mit M126 & CYCL DEF 200)  
> **Honorar-Budget:** **850,00 € netto** (1.011,50 € brutto nach § 18 EStG *(Einkommensteuergesetz)*)

---

## 1. Übersicht der 6 Pflicht-Artefakte & Abschlussdokumentation (Speicherorte & KI-Agenten)

| Nr. | Pflicht-Artefakt *(Dateiname & Klick-Link)* | Zuständiger KI-Agent | Technischer & Kaufmännischer Zweck |
| :---: | :--- | :--- | :--- |
| **Eingang** | [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/KUNDENAUFTRAG.md) | 🔍 **Agent 1: Lead-Scout-Agent** | Unverfälschtes Original-Kundenbriefing mit Geometrie-, Maschinen- und Budgetvorgaben |
| **1** | [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) | 💰 **Agent 4: Backoffice-Ingenieur-Agent** | Verbindliches B2B-Festpreisangebot *(Business-to-Business)* nach § 18 EStG inkl. Single-Block-Haftungsklausel |
| **2** | [`uebung_14_heidenhain_klartext_4achse.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse.nc) und Postprozessor [`uebung_14_heidenhain_klartext_4achse.cps`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse.cps) | 💻 **Agent 2: Postprocessor-Coder-Agent** | Fertig generierter, absturzsicherer CNC-Maschinencode *(Computerized Numerical Control)* inkl. Z-MIN-Header |
| **3** | [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | 🛡️ **Agent 3: NC-Safety- & Setup-Agent** | 5-Stufen-Sicherheits-Audit mit mathematischem Kollisionsnachweis ($Z_{\text{min}} = -12.000\,\text{mm}$ vs. Backe $-18.000\,\text{mm}$) |
| **4** | [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/06_EINRICHTEBLATT_SETUP_SHEET.md) | 🛡️ **Agent 3: NC-Safety- & Setup-Agent** | Druckfertiges Rüstdatenblatt für den Maschinenbediener mit Nullpunkt (`Preset 1 (Drehachsen-Mittelpunkt A-Achse, X0 Planfläche links)`) und Auskraglängen |
| **5** | [`uebung_14_heidenhain_klartext_4achse_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse_simulation_video.mp4) | 🛡️ **Agent 3: NC-Safety- & Setup-Agent** | Gerendertes 3D-Simulationsvideo (MP4) zur visuellen Vorabkontrolle aller Werkzeugbahnen |
| **6** | [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | 💰 **Agent 4: Backoffice-Ingenieur-Agent** | Steuerkonforme Ingenieur-Honorarrechnung nach § 14 UStG *(Umsatzsteuergesetz)* & § 18 EStG für das Finanzamt Hanau |
| **Abschluss** | [`08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md) | 🤖 **Gesamtsystem (Agent 1–4)** | Lückenlose Abschlussdokumentation aller Phasen, Berechnungen und Freigaben |

---

## 2. Das 4-Stufen-Workflow-Diagramm

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ EINGANG: KUNDENAUFTRAG.md (Alps Precision AG (Schweiz))                        │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ SCHRITT 1 (Agent 4 - Backoffice):                                            │
│ Erstellt 02_ANGEBOT_DIPL_ING_BUJANOVSKI.md (850,00 € netto, § 18 EStG)       │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ SCHRITT 2 (Agent 2 - Postprocessor-Coder):                                   │
│ Entwickelt Postprozessor & generiert uebung_14_heidenhain_klartext_4achse.nc (Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse)) │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ SCHRITT 3 (Agent 3 - NC-Safety & Setup):                                     │
│ • Prüft Z-MIN (-12.000 mm) -> 05_SICHERHEITS_CRASH_PRUEFBERICHT.md          │
│ • Erstellt Rüstblatt        -> 06_EINRICHTEBLATT_SETUP_SHEET.md              │
│ • Rendert 3D-Video          -> uebung_14_heidenhain_klartext_4achse_simulation_video.mp4      │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ SCHRITT 4 (Agent 4 - Backoffice):                                            │
│ Stellt 07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md & 08_DOKUMENTATION...md         │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Fertige, maßgeschneiderte Prompts zum direkten Kopieren

### 💰 Schritt 1: Prompt für das Ingenieur-Angebot *(Agent 4)*

```text
Starte Agent 4 (Backoffice-Ingenieur-Agent):
Lies die Datei c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/KUNDENAUFTRAG.md.
Erstelle für den Kunden Alps Precision AG (Schweiz) (Ansprechpartner: Urs Hodel (Produktionsleiter), Adresse: Industriestrasse 18, CH-9015 St. Gallen (Schweiz)) ein rechtssicheres Ingenieur-Festpreisangebot nach § 18 EStG über exakt 850,00 € netto (1.011,50 € brutto) für das Bauteil "4-Seiten-Steuerwelle auf Teilapparat (Indexierung A+0 / A+90 / A+180 / A+270)" auf der Maschine "Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse)" (Heidenhain TNC 640 (Klartext-Dialogprogrammierung .H mit M126 & CYCL DEF 200)).
Integriere zwingend den Haftungsausschluss zum Einfahren im Einzelsatzbetrieb (Single Block) und speichere das Dokument unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Honorar- und Adressabgleich:** Stimmen `850,00 € netto` (`1.011,50 € brutto`), Firmenname `Alps Precision AG (Schweiz)` und Maschine `Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse)` exakt mit `KUNDENAUFTRAG.md` überein?
2. **Steuer-Check (§ 18 EStG):** Wird die Leistung als *„Ingenieurtechnische Entwicklung und mathematische Verifikation"* deklariert (keine gewerblichen Begriffe)?
3. **Haftungsklausel:** Ist die Verpflichtung zum Einfahren im Einzelsatzbetrieb *(Single Block)* enthalten?

---

### 💻 Schritt 2: Prompt für Postprozessor & NC-Maschinencode *(Agent 2)*

```text
Starte Agent 2 (Postprocessor-Coder-Agent):
Entwickle und verifiziere auf Basis von c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/KUNDENAUFTRAG.md den CNC-Maschinencode für den Kunden Alps Precision AG (Schweiz):
- Bauteil: 4-Seiten-Steuerwelle auf Teilapparat (Indexierung A+0 / A+90 / A+180 / A+270) (Edelstahl 1.4404 (X2CrNiMo17-12-2 / V4A))
- Maschine & Steuerung: Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse) (Heidenhain TNC 640 (Klartext-Dialogprogrammierung .H mit M126 & CYCL DEF 200))
- Werkstücknullpunkt: Preset 1 (Drehachsen-Mittelpunkt A-Achse, X0 Planfläche links)
- Werkzeuge & Schnittdaten: T1 (VHM-Schaftfräser Ø 10,0 mm (Schlüsselflächen auf A+0° / A+90°), S=8000 U/min, F=1200 mm/min, Z_min=-5.000 mm); T2 (VHM-Spiralbohrer Ø 6,0 mm (CYCL DEF 200 Querbohrungen bis Z-12.0), S=3500 U/min, F=300 mm/min, Z_min=-12.000 mm)
- Tiefste Zustellung: Z_min = -12.000 mm (Spannbacken-Oberkante bei Z = -18.000 mm)
Speichere den fertigen, fehlerfreien Maschinencode unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse.nc
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Textprüfung Header & Sicherheitszeile:** Enthält `uebung_14_heidenhain_klartext_4achse.nc` den Z-MIN-Sicherheitsheader sowie den Safe-Start-Block (`G90 G21 G17 G40 G49 G80` bzw. Steuerungs-Äquivalent)?
2. **Web-Backplot-Test:** Lade `uebung_14_heidenhain_klartext_4achse.nc` in [NCViewer.com](https://ncviewer.com/) oder den lokalen 3D-Simulator [`index.html`](file:///c:/Projekte/CNC/02_Software_und_Tools/web_tools/index.html) und prüfe die Werkzeugbahnen.
3. **Lokaler Simulator-Lauf:** Prüfe den Postprozessor mit `node 02_Software_und_Tools/simuliere_post.js`.

---

### 🛡️ Schritt 3: Prompt für Sicherheitsbericht, Einrichteblatt & 3D-Simulationsvideo *(Agent 3)*

```text
Starte Agent 3 (NC-Safety- & Setup-Agent):
Führe für die Datei c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse.nc des Kunden Alps Precision AG (Schweiz) (Hermle C400 (Heidenhain TNC 640 Steuerung mit 4. Achse / A-Achse)) das vollständige 5-Stufen-Sicherheitsaudit durch:
1. Berechne die Kollisionsreserve zwischen Z_min = -12.000 mm und den Schraubstockbacken bei Z = -18.000 mm und speichere den Prüfbericht unter:
   c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/05_SICHERHEITS_CRASH_PRUEFBERICHT.md
2. Erstelle das druckfertige Werkstatteinrichteblatt (Setup Sheet) mit allen Werkzeugen (T1 (VHM-Schaftfräser Ø 10,0 mm (Schlüsselflächen auf A+0° / A+90°), S=8000 U/min, F=1200 mm/min, Z_min=-5.000 mm); T2 (VHM-Spiralbohrer Ø 6,0 mm (CYCL DEF 200 Querbohrungen bis Z-12.0), S=3500 U/min, F=300 mm/min, Z_min=-12.000 mm)) und Mindest-Auskraglängen unter:
   c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/06_EINRICHTEBLATT_SETUP_SHEET.md
3. Rendere das 3D-Maschinensimulationsvideo über render_simulation_video.py:
   python 02_Software_und_Tools/scripts/render_simulation_video.py --gcode c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse.nc --output c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse_simulation_video.mp4
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Prüfbericht-Status:** Bescheinigt `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` den Status **BESTANDEN (GRÜN)** und die exakte Reserve von `6.000 mm`?
2. **Einrichteblatt-Check:** Stimmen alle Drehzahlen ($S$), Vorschübe ($F$) und Auskraglängen ($L_{\text{min}}$) in `06_EINRICHTEBLATT_SETUP_SHEET.md` zu 100 % mit `uebung_14_heidenhain_klartext_4achse.nc` überein?
3. **🎬 3D-Simulationsvideo-Check:** Öffne `uebung_14_heidenhain_klartext_4achse_simulation_video.mp4` und kontrolliere visuell die sichere Anfahrhöhe, das Eintauchen im Vorschub und den Sicherheitsabstand zu den Schraubstockbacken.

---

### 💰 Schritt 4: Prompt für Honorarrechnung & Abschlussdokumentation *(Agent 4)*

```text
Starte Agent 4 (Backoffice-Ingenieur-Agent):
Erstelle nach erfolgreicher technischer Freigabe für den Kunden Alps Precision AG (Schweiz) (Industriestrasse 18, CH-9015 St. Gallen (Schweiz)) die steuerkonforme Honorarrechnung nach § 14 UStG und § 18 EStG über 850,00 € netto (zzgl. 19 % USt. = 1.011,50 € brutto) für das Finanzamt Hanau unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md
Erstelle zudem die vollständige Abschlussdokumentation aller Projektartefakte unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Rechnungsprüfung (§ 14 UStG):** Sind Rechnungsnummer `RE-2026-14`, Leistungszeitraum, Nettobetrag (`850,00 €`), 19 % USt. und Bruttobetrag (`1.011,50 €`) korrekt ausgewiesen?
2. **Finanzamt-Konformität (§ 18 EStG):** Ist die Position eindeutig als freiberufliche Ingenieurleistung formuliert?

---

## 4. Abnahme-Kriterien (Checkliste für 100 % Erledigung)

- [x] **Artefakt 1:** [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) existiert und wurde geprüft.
- [x] **Artefakt 2:** [`uebung_14_heidenhain_klartext_4achse.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse.nc) existiert mit Z-MIN-Header und lief fehlerfrei im Simulator.
- [x] **Artefakt 3:** [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) bescheinigt Status **BESTANDEN (GRÜN)**.
- [x] **Artefakt 4:** [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/06_EINRICHTEBLATT_SETUP_SHEET.md) liegt druckfertig für die Werkstatt vor.
- [x] **Artefakt 5:** [`uebung_14_heidenhain_klartext_4achse_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/uebung_14_heidenhain_klartext_4achse_simulation_video.mp4) wurde gerendert und zeigt kollisionsfreie Fräsbahnen.
- [x] **Artefakt 6:** [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) ist für das Finanzamt Hanau abgelegt.
- [x] **Abschluss-Doku:** [`08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_14_heidenhain_4achs_teilapparat/08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md) dokumentiert alle 5 Phasen lückenlos.
