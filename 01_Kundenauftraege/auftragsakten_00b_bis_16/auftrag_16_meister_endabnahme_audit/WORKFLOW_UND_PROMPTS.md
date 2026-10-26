# 📋 Standard-Workflow & Fertige KI-Prompts: Auftrag 16: Meister-Endabnahme & Komplett-Postprozessor-Zertifizierung

> **Auftragsordner:** `01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/`  
> **Kunde:** **Hessen Automotive GmbH** (Dipl.-Ing. Bernd Schäfer (Leiter Qualitätssicherung))  
> **Maschine & Steuerung:** **Haas VF-2 / Grob G550 (Komplett-Zertifizierung ISO G-Code)** — Haas NGC / ISO (Vollständiger Kunden-Postprozessor inkl. Tool-Table, Z-MIN-Sperre & G53 Y0)  
> **Honorar-Budget:** **490,00 € netto** (583,10 € brutto nach § 18 EStG *(Einkommensteuergesetz)*)

---

## 1. Übersicht der 6 Pflicht-Artefakte & Abschlussdokumentation (Speicherorte & KI-Agenten)

| Nr. | Pflicht-Artefakt *(Dateiname & Klick-Link)* | Zuständiger KI-Agent | Technischer & Kaufmännischer Zweck |
| :---: | :--- | :--- | :--- |
| **Eingang** | [`KUNDENAUFTRAG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/KUNDENAUFTRAG.md) | 🔍 **Agent 1: Lead-Scout-Agent** | Unverfälschtes Original-Kundenbriefing mit Geometrie-, Maschinen- und Budgetvorgaben |
| **1** | [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) | 💰 **Agent 4: Backoffice-Ingenieur-Agent** | Verbindliches B2B-Festpreisangebot *(Business-to-Business)* nach § 18 EStG inkl. Single-Block-Haftungsklausel |
| **2** | [`kunden_post_generiert.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/kunden_post_generiert.nc) und Postprozessor [`kunden_post_generiert.cps`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/kunden_post_generiert.cps) | 💻 **Agent 2: Postprocessor-Coder-Agent** | Fertig generierter, absturzsicherer CNC-Maschinencode *(Computerized Numerical Control)* inkl. Z-MIN-Header |
| **3** | [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | 🛡️ **Agent 3: NC-Safety- & Setup-Agent** | 5-Stufen-Sicherheits-Audit mit mathematischem Kollisionsnachweis ($Z_{\text{min}} = -12.000\,\text{mm}$ vs. Backe $-15.000\,\text{mm}$) |
| **4** | [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/06_EINRICHTEBLATT_SETUP_SHEET.md) | 🛡️ **Agent 3: NC-Safety- & Setup-Agent** | Druckfertiges Rüstdatenblatt für den Maschinenbediener mit Nullpunkt (`G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)`) und Auskraglängen |
| **5** | [`kunden_post_generiert_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/kunden_post_generiert_simulation_video.mp4) | 🛡️ **Agent 3: NC-Safety- & Setup-Agent** | Gerendertes 3D-Simulationsvideo (MP4) zur visuellen Vorabkontrolle aller Werkzeugbahnen |
| **6** | [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | 💰 **Agent 4: Backoffice-Ingenieur-Agent** | Steuerkonforme Ingenieur-Honorarrechnung nach § 14 UStG *(Umsatzsteuergesetz)* & § 18 EStG für das Finanzamt Hanau |
| **Abschluss** | [`08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md) | 🤖 **Gesamtsystem (Agent 1–4)** | Lückenlose Abschlussdokumentation aller Phasen, Berechnungen und Freigaben |

---

## 2. Das 4-Stufen-Workflow-Diagramm

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│ EINGANG: KUNDENAUFTRAG.md (Hessen Automotive GmbH)                        │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ SCHRITT 1 (Agent 4 - Backoffice):                                            │
│ Erstellt 02_ANGEBOT_DIPL_ING_BUJANOVSKI.md (490,00 € netto, § 18 EStG)       │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ SCHRITT 2 (Agent 2 - Postprocessor-Coder):                                   │
│ Entwickelt Postprozessor & generiert kunden_post_generiert.nc (Haas VF-2 / Grob G550 (Komplett-Zertifizierung ISO G-Code)) │
└──────────────────────────────────────┬───────────────────────────────────────┘
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│ SCHRITT 3 (Agent 3 - NC-Safety & Setup):                                     │
│ • Prüft Z-MIN (-12.000 mm) -> 05_SICHERHEITS_CRASH_PRUEFBERICHT.md          │
│ • Erstellt Rüstblatt        -> 06_EINRICHTEBLATT_SETUP_SHEET.md              │
│ • Rendert 3D-Video          -> kunden_post_generiert_simulation_video.mp4      │
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
Lies die Datei c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/KUNDENAUFTRAG.md.
Erstelle für den Kunden Hessen Automotive GmbH (Ansprechpartner: Dipl.-Ing. Bernd Schäfer (Leiter Qualitätssicherung), Adresse: Automobilring 10, 34225 Baunatal) ein rechtssicheres Ingenieur-Festpreisangebot nach § 18 EStG über exakt 490,00 € netto (583,10 € brutto) für das Bauteil "Zertifizierungs-Referenzbauteil O1001 (Komplett-Audit aller Sicherheitsmodule)" auf der Maschine "Haas VF-2 / Grob G550 (Komplett-Zertifizierung ISO G-Code)" (Haas NGC / ISO (Vollständiger Kunden-Postprozessor inkl. Tool-Table, Z-MIN-Sperre & G53 Y0)).
Integriere zwingend den Haftungsausschluss zum Einfahren im Einzelsatzbetrieb (Single Block) und speichere das Dokument unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Honorar- und Adressabgleich:** Stimmen `490,00 € netto` (`583,10 € brutto`), Firmenname `Hessen Automotive GmbH` und Maschine `Haas VF-2 / Grob G550 (Komplett-Zertifizierung ISO G-Code)` exakt mit `KUNDENAUFTRAG.md` überein?
2. **Steuer-Check (§ 18 EStG):** Wird die Leistung als *„Ingenieurtechnische Entwicklung und mathematische Verifikation"* deklariert (keine gewerblichen Begriffe)?
3. **Haftungsklausel:** Ist die Verpflichtung zum Einfahren im Einzelsatzbetrieb *(Single Block)* enthalten?

---

### 💻 Schritt 2: Prompt für Postprozessor & NC-Maschinencode *(Agent 2)*

```text
Starte Agent 2 (Postprocessor-Coder-Agent):
Entwickle und verifiziere auf Basis von c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/KUNDENAUFTRAG.md den CNC-Maschinencode für den Kunden Hessen Automotive GmbH:
- Bauteil: Zertifizierungs-Referenzbauteil O1001 (Komplett-Audit aller Sicherheitsmodule) (Aluminium EN AW-6082 T6 (80 x 50 x 12 mm))
- Maschine & Steuerung: Haas VF-2 / Grob G550 (Komplett-Zertifizierung ISO G-Code) (Haas NGC / ISO (Vollständiger Kunden-Postprozessor inkl. Tool-Table, Z-MIN-Sperre & G53 Y0))
- Werkstücknullpunkt: G54 (Werkstücknullpunkt: Vorne links oben, Z = 0,0 mm)
- Werkzeuge & Schnittdaten: T01 (VHM-Schaftfräser Ø 10,0 mm (Außenkontur Z-5.0 & Vollkreistasche Ø30 G03 I-15.0 J0.0 Z-3.0), S=8000 U/min, F=1200 mm/min, Z_min=-5.000 mm); T02 (VHM-Spiralbohrer Ø 6,0 mm (4x Tiefbohrzyklus G83 bis Z-12.0 mit G80-Abwahl), S=3500 U/min, F=300 mm/min, Z_min=-12.000 mm)
- Tiefste Zustellung: Z_min = -12.000 mm (Spannbacken-Oberkante bei Z = -15.000 mm)
Speichere den fertigen, fehlerfreien Maschinencode unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/kunden_post_generiert.nc
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Textprüfung Header & Sicherheitszeile:** Enthält `kunden_post_generiert.nc` den Z-MIN-Sicherheitsheader sowie den Safe-Start-Block (`G90 G21 G17 G40 G49 G80` bzw. Steuerungs-Äquivalent)?
2. **Web-Backplot-Test:** Lade `kunden_post_generiert.nc` in [NCViewer.com](https://ncviewer.com/) oder den lokalen 3D-Simulator [`index.html`](file:///c:/Projekte/CNC/02_Software_und_Tools/web_tools/index.html) und prüfe die Werkzeugbahnen.
3. **Lokaler Simulator-Lauf:** Prüfe den Postprozessor mit `node 02_Software_und_Tools/simuliere_post.js`.

---

### 🛡️ Schritt 3: Prompt für Sicherheitsbericht, Einrichteblatt & 3D-Simulationsvideo *(Agent 3)*

```text
Starte Agent 3 (NC-Safety- & Setup-Agent):
Führe für die Datei c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/kunden_post_generiert.nc des Kunden Hessen Automotive GmbH (Haas VF-2 / Grob G550 (Komplett-Zertifizierung ISO G-Code)) das vollständige 5-Stufen-Sicherheitsaudit durch:
1. Berechne die Kollisionsreserve zwischen Z_min = -12.000 mm und den Schraubstockbacken bei Z = -15.000 mm und speichere den Prüfbericht unter:
   c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/05_SICHERHEITS_CRASH_PRUEFBERICHT.md
2. Erstelle das druckfertige Werkstatteinrichteblatt (Setup Sheet) mit allen Werkzeugen (T01 (VHM-Schaftfräser Ø 10,0 mm (Außenkontur Z-5.0 & Vollkreistasche Ø30 G03 I-15.0 J0.0 Z-3.0), S=8000 U/min, F=1200 mm/min, Z_min=-5.000 mm); T02 (VHM-Spiralbohrer Ø 6,0 mm (4x Tiefbohrzyklus G83 bis Z-12.0 mit G80-Abwahl), S=3500 U/min, F=300 mm/min, Z_min=-12.000 mm)) und Mindest-Auskraglängen unter:
   c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/06_EINRICHTEBLATT_SETUP_SHEET.md
3. Rendere das 3D-Maschinensimulationsvideo über render_simulation_video.py:
   python 02_Software_und_Tools/scripts/render_simulation_video.py --gcode c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/kunden_post_generiert.nc --output c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/kunden_post_generiert_simulation_video.mp4
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Prüfbericht-Status:** Bescheinigt `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` den Status **BESTANDEN (GRÜN)** und die exakte Reserve von `3.000 mm`?
2. **Einrichteblatt-Check:** Stimmen alle Drehzahlen ($S$), Vorschübe ($F$) und Auskraglängen ($L_{\text{min}}$) in `06_EINRICHTEBLATT_SETUP_SHEET.md` zu 100 % mit `kunden_post_generiert.nc` überein?
3. **🎬 3D-Simulationsvideo-Check:** Öffne `kunden_post_generiert_simulation_video.mp4` und kontrolliere visuell die sichere Anfahrhöhe, das Eintauchen im Vorschub und den Sicherheitsabstand zu den Schraubstockbacken.

---

### 💰 Schritt 4: Prompt für Honorarrechnung & Abschlussdokumentation *(Agent 4)*

```text
Starte Agent 4 (Backoffice-Ingenieur-Agent):
Erstelle nach erfolgreicher technischer Freigabe für den Kunden Hessen Automotive GmbH (Automobilring 10, 34225 Baunatal) die steuerkonforme Honorarrechnung nach § 14 UStG und § 18 EStG über 490,00 € netto (zzgl. 19 % USt. = 583,10 € brutto) für das Finanzamt Hanau unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md
Erstelle zudem die vollständige Abschlussdokumentation aller Projektartefakte unter:
c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md
```

#### 🔍 Wie wird dieses Artefakt getestet und geprüft?
1. **Rechnungsprüfung (§ 14 UStG):** Sind Rechnungsnummer `RE-2026-16`, Leistungszeitraum, Nettobetrag (`490,00 €`), 19 % USt. und Bruttobetrag (`583,10 €`) korrekt ausgewiesen?
2. **Finanzamt-Konformität (§ 18 EStG):** Ist die Position eindeutig als freiberufliche Ingenieurleistung formuliert?

---

## 4. Abnahme-Kriterien (Checkliste für 100 % Erledigung)

- [x] **Artefakt 1:** [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) existiert und wurde geprüft.
- [x] **Artefakt 2:** [`kunden_post_generiert.nc`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/kunden_post_generiert.nc) existiert mit Z-MIN-Header und lief fehlerfrei im Simulator.
- [x] **Artefakt 3:** [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) bescheinigt Status **BESTANDEN (GRÜN)**.
- [x] **Artefakt 4:** [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/06_EINRICHTEBLATT_SETUP_SHEET.md) liegt druckfertig für die Werkstatt vor.
- [x] **Artefakt 5:** [`kunden_post_generiert_simulation_video.mp4`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/kunden_post_generiert_simulation_video.mp4) wurde gerendert und zeigt kollisionsfreie Fräsbahnen.
- [x] **Artefakt 6:** [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) ist für das Finanzamt Hanau abgelegt.
- [x] **Abschluss-Doku:** [`08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md`](file:///c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16/auftrag_16_meister_endabnahme_audit/08_DOKUMENTATION_AUFTRAGSABWICKLUNG_UND_ARTEFAKTE.md) dokumentiert alle 5 Phasen lückenlos.
