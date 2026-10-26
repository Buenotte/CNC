# 📋 Standard-Workflow & Fertige KI-Prompts: Auftrag 05: Einrichtedokumentation, G-Code-Verifikation & 3D-Simulation

> **Auftragsordner:** `01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/`  
> **Kunde:** **Kuhn Medizintechnik & CNC-Fräszentrum** (Thomas Kuhn (Inhaber & Werkstattleiter))  
> **Maschine & Steuerung:** **Haas VF-2 (Haas NGC Steuerung)** — Haas NGC (Next Generation Control / ISO G-Code)  
> **Honorar-Budget:** **280,00 € netto** (333,20 € brutto nach § 18 EStG *(Einkommensteuergesetz)*)

---

## 1. Übersicht der 6 Pflicht-Artefakte & Abschlussdokumentation (Speicherorte & KI-Agenten)

| Nr. | Pflicht-Artefakt *(Dateiname & Klick-Link)* | Zuständiger KI-Agent | Technischer & Kaufmännischer Zweck |
| :---: | :--- | :--- | :--- |
| **Eingang** | [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/KUNDENAUFTRAG.md) | 🔍 **Agent 1: Lead-Scout-Agent** | Unverfälschtes Original-Kundenbriefing mit Geometrie-, Maschinen- und Budgetvorgaben |
| **1** | [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) | 💰 **Agent 4: Backoffice-Ingenieur-Agent** | Verbindliches B2B-Festpreisangebot *(Business-to-Business)* nach § 18 EStG inkl. Single-Block-Haftungsklausel |
| **2** | [`output_expected.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/output_expected.nc) (Direktverifikation) | 💻 **Agent 2: Postprocessor-Coder-Agent** | Fertig generierter, absturzsicherer CNC-Maschinencode *(Computerized Numerical Control)* inkl. Z-MIN-Header |
| **3** | [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | 🛡️ **Agent 3: NC-Safety- & Setup-Agent** | 5-Stufen-Sicherheits-Audit mit mathematischem Kollisionsnachweis ($Z_{\text{min}} = -12.000\,\text{mm}$ vs. Backe $-15.000\,\text{mm}$) |
| **4** | [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/06_EINRICHTEBLATT_SETUP_SHEET.md) | 🛡️ **Agent 3: NC-Safety- & Setup-Agent** | Druckfertiges Rüstdatenblatt für den Maschinenbediener mit Nullpunkt (`G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)`) und Auskraglängen |
| **5** | [`output_expected_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/output_expected_simulation_video.mp4) | 🛡️ **Agent 3: NC-Safety- & Setup-Agent** | Gerendertes 3D-Simulationsvideo (MP4) zur visuellen Vorabkontrolle aller Werkzeugbahnen |
| **6** | [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | 💰 **Agent 4: Backoffice-Ingenieur-Agent** | Steuerkonforme Ingenieur-Honorarrechnung nach § 14 UStG *(Umsatzsteuergesetz)* & § 18 EStG für das Finanzamt Hanau |
| **Abschluss** | [`08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md) | 🤖 **Gesamtsystem (Agent 1–4)** | Lückenlose Abschlussdokumentation aller Phasen, Berechnungen und Freigaben |

---

## 2. Das 4-Stufen-Workflow-Diagramm

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ EINGANG: KUNDENAUFTRAG.md (Kuhn Medizintechnik & CNC-Fräszentrum)                        │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ SCHRITT 1 (Agent 4 - Backoffice):                                            │
│ Erstellt 02_ANGEBOT_DIPL_ING_BUJANOVSKI.md (280,00 € netto, § 18 EStG)       │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ SCHRITT 2 (Agent 2 - Postprocessor-Coder):                                   │
│ Entwickelt Postprozessor & generiert output_expected.nc (Haas VF-2 (Haas NGC Steuerung)) │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ SCHRITT 3 (Agent 3 - NC-Safety & Setup):                                     │
│ • Prüft Z-MIN (-12.000 mm) -> 05_SICHERHEITS_CRASH_PRUEFBERICHT.md          │
│ • Erstellt Rüstblatt        -> 06_EINRICHTEBLATT_SETUP_SHEET.md              │
│ • Rendert 3D-Video          -> output_expected_simulation_video.mp4      │
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
Lies die Datei c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/KUNDENAUFTRAG.md.
Erstelle für den Kunden Kuhn Medizintechnik & CNC-Fräszentrum (Ansprechpartner: Thomas Kuhn (Inhaber & Werkstattleiter), Adresse: Medizinalring 11, 78532 Tuttlingen) ein rechtssicheres Ingenieur-Festpreisangebot nach § 18 EStG über exakt 280,00 € netto (333,20 € brutto) für das Bauteil "Referenz-Trägerplatte O1001 (80 x 50 x 12 mm)" auf der Maschine "Haas VF-2 (Haas NGC Steuerung)" (Haas NGC (Next Generation Control / ISO G-Code)).
Integriere zwingend den Haftungsausschluss zum Einfahren im Einzelsatzbetrieb (Single Block) und speichere das Dokument unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Honorar- und Adressabgleich:** Stimmen `280,00 € netto` (`333,20 € brutto`), Firmenname `Kuhn Medizintechnik & CNC-Fräszentrum` und Maschine `Haas VF-2 (Haas NGC Steuerung)` exakt mit `KUNDENAUFTRAG.md` überein?
2. **Steuer-Check (§ 18 EStG):** Wird die Leistung als *„Ingenieurtechnische Entwicklung und mathematische Verifikation"* deklariert (keine gewerblichen Begriffe)?
3. **Haftungsklausel:** Ist die Verpflichtung zum Einfahren im Einzelsatzbetrieb *(Single Block)* enthalten?

---

### 💻 Schritt 2: Prompt für Postprozessor & NC-Maschinencode *(Agent 2)*

```text
Starte Agent 2 (Postprocessor-Coder-Agent):
Entwickle und verifiziere auf Basis von c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/KUNDENAUFTRAG.md den CNC-Maschinencode für den Kunden Kuhn Medizintechnik & CNC-Fräszentrum:
- Bauteil: Referenz-Trägerplatte O1001 (80 x 50 x 12 mm) (Aluminium EN AW-6082 T6)
- Maschine & Steuerung: Haas VF-2 (Haas NGC Steuerung) (Haas NGC (Next Generation Control / ISO G-Code))
- Werkstücknullpunkt: G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)
- Werkzeuge & Schnittdaten: T01 (VHM-Schaftfräser Ø 10,0 mm (Außenkontur Z-5.0 & Kreistasche Z-3.0), S=8000 U/min, F=1200 mm/min, Z_min=-5.000 mm); T02 (VHM-Spiralbohrer Ø 6,0 mm (4x Tiefbohrzyklus G83 Z-12.0), S=3500 U/min, F=300 mm/min, Z_min=-12.000 mm)
- Tiefste Zustellung: Z_min = -12.000 mm (Spannbacken-Oberkante bei Z = -15.000 mm)
Speichere den fertigen, fehlerfreien Maschinencode unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/output_expected.nc
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Textprüfung Header & Sicherheitszeile:** Enthält `output_expected.nc` den Z-MIN-Sicherheitsheader sowie den Safe-Start-Block (`G90 G21 G17 G40 G49 G80` bzw. Steuerungs-Äquivalent)?
2. **Web-Backplot-Test:** Lade `output_expected.nc` in [NCViewer.com](https://ncviewer.com/) oder den lokalen 3D-Simulator [`index.html`](file:///c:/Projekte/CNC/02_Software_und_Tools/web_tools/index.html) und prüfe die Werkzeugbahnen.
3. **Lokaler Simulator-Lauf:** Prüfe den Postprozessor mit `node 02_Software_und_Tools/simuliere_post.js`.

---

### 🛡️ Schritt 3: Prompt für Sicherheitsbericht, Einrichteblatt & 3D-Simulationsvideo *(Agent 3)*

```text
Starte Agent 3 (NC-Safety- & Setup-Agent):
Führe für die Datei c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/output_expected.nc des Kunden Kuhn Medizintechnik & CNC-Fräszentrum (Haas VF-2 (Haas NGC Steuerung)) das vollständige 5-Stufen-Sicherheitsaudit durch:
1. Berechne die Kollisionsreserve zwischen Z_min = -12.000 mm und den Schraubstockbacken bei Z = -15.000 mm und speichere den Prüfbericht unter:
   c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/05_SICHERHEITS_CRASH_PRUEFBERICHT.md
2. Erstelle das druckfertige Werkstatteinrichteblatt (Setup Sheet) mit allen Werkzeugen (T01 (VHM-Schaftfräser Ø 10,0 mm (Außenkontur Z-5.0 & Kreistasche Z-3.0), S=8000 U/min, F=1200 mm/min, Z_min=-5.000 mm); T02 (VHM-Spiralbohrer Ø 6,0 mm (4x Tiefbohrzyklus G83 Z-12.0), S=3500 U/min, F=300 mm/min, Z_min=-12.000 mm)) und Mindest-Auskraglängen unter:
   c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/06_EINRICHTEBLATT_SETUP_SHEET.md
3. Rendere das 3D-Maschinensimulationsvideo über render_simulation_video.py:
   python 02_Software_und_Tools/scripts/render_simulation_video.py --gcode c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/output_expected.nc --output c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/output_expected_simulation_video.mp4
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Prüfbericht-Status:** Bescheinigt `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` den Status **BESTANDEN (GRÜN)** und die exakte Reserve von `3.000 mm`?
2. **Einrichteblatt-Check:** Stimmen alle Drehzahlen ($S$), Vorschübe ($F$) und Auskraglängen ($L_{\text{min}}$) in `06_EINRICHTEBLATT_SETUP_SHEET.md` zu 100 % mit `output_expected.nc` überein?
3. **🎬 3D-Simulationsvideo-Check:** Öffne `output_expected_simulation_video.mp4` und kontrolliere visuell die sichere Anfahrhöhe, das Eintauchen im Vorschub und den Sicherheitsabstand zu den Schraubstockbacken.

---

### 💰 Schritt 4: Prompt für Honorarrechnung & Abschlussdokumentation *(Agent 4)*

```text
Starte Agent 4 (Backoffice-Ingenieur-Agent):
Erstelle nach erfolgreicher technischer Freigabe für den Kunden Kuhn Medizintechnik & CNC-Fräszentrum (Medizinalring 11, 78532 Tuttlingen) die steuerkonforme Honorarrechnung nach § 14 UStG und § 18 EStG über 280,00 € netto (zzgl. 19 % USt. = 333,20 € brutto) für das Finanzamt Hanau unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md
Erstelle zudem die vollständige Abschlussdokumentation aller Projektartefakte unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Rechnungsprüfung (§ 14 UStG):** Sind Rechnungsnummer `RE-2026-05`, Leistungszeitraum, Nettobetrag (`280,00 €`), 19 % USt. und Bruttobetrag (`333,20 €`) korrekt ausgewiesen?
2. **Finanzamt-Konformität (§ 18 EStG):** Ist die Position eindeutig als freiberufliche Ingenieurleistung formuliert?

---

## 4. Abnahme-Kriterien (Checkliste für 100 % Erledigung)

- [x] **Artefakt 1:** [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) existiert und wurde geprüft.
- [x] **Artefakt 2:** [`output_expected.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/output_expected.nc) existiert mit Z-MIN-Header und lief fehlerfrei im Simulator.
- [x] **Artefakt 3:** [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) bescheinigt Status **BESTANDEN (GRÜN)**.
- [x] **Artefakt 4:** [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/06_EINRICHTEBLATT_SETUP_SHEET.md) liegt druckfertig für die Werkstatt vor.
- [x] **Artefakt 5:** [`output_expected_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/output_expected_simulation_video.mp4) wurde gerendert und zeigt kollisionsfreie Fräsbahnen.
- [x] **Artefakt 6:** [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) ist für das Finanzamt Hanau abgelegt.
- [x] **Abschluss-Doku:** [`08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_05_einrichtedoku_simulation/08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md) dokumentiert alle 5 Phasen lückenlos.
