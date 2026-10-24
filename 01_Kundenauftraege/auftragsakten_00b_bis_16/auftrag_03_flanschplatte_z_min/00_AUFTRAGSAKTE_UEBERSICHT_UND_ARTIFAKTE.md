# 📁 Vollständige Auftragsakte & Artefakt-Übersicht: Auftrag 03 (Flanschplatte)

Dieses Verzeichnis ist das **Muster-Beispiel für einen 100 % vollständigen Kundenauftrags-Ordner**. Es demonstriert, wie alle 4 KI-Agenten *(autonome Software-Assistenten)* ihre Arbeitsergebnisse lückenlos an einem einzigen Ort ablegen.

**Auftrag:** Auftrag 03 – Flanschplatte Z-MIN & Kollisionsschutz  
**Kunde:** Schmidt Präzisionstechnik GmbH (Markus Weber, Fertigungsleiter)  
**Auftragnehmer:** Dipl.-Ing. Bujanovski (Freiberufliches Ingenieurbüro nach § 18 EStG)  
**Gesamt-Budget:** 480,00 € netto (Festpreis)

---

## 🗂️ Übersicht aller in diesem Auftragsordner gespeicherten Artefakte

Alle Dateien in diesem Ordner sind durchnummeriert, damit der gesamte Lebenszyklus eines Kundenauftrags chronologisch und transparent nachvollziehbar ist:

```
c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_03_flanschplatte_z_min\
│
├── 📄 00_AUFTRAGSAKTE_UEBERSICHT_UND_ARTIFAKTE.md   (Diese Übersicht)
│
├── 📩 01_KUNDENAUFTRAG_BRIEFING.md                  (Phase 1: Original-Kundenanfrage)
│
├── 📄 02_ANGEBOT_DIPL_ING_BUJANOVSKI.md               (Phase 2: B2B-Angebot nach § 18 EStG von Agent 4)
│
├── 💻 03_POSTPROZESSOR_uebung_03.cps                (Phase 3: JavaScript-Postprozessor von Agent 2)
├── ⚙️ 04_MASCHINENPROGRAMM_HAAS.nc                  (Phase 3: Fertiger Maschinencode für Haas VF-2)
├── 🧊 bauteil_1001.stl                              (Phase 3: 3D-CAD-Modell des Kunden)
│
├── 🛡️ 05_SICHERHEITS_CRASH_PRUEFBERICHT.md          (Phase 4: 5-Stufen-Prüfbericht von Agent 3)
├── 📋 06_EINRICHTEBLATT_SETUP_SHEET.md              (Phase 4: Setup Sheet für Bediener von Agent 3)
├── 🖼️ flanschplatte_cnc_depth_levels.jpg            (Phase 4: 3D-Schema Frästiefen & Aufspannung)
├── 🖼️ cnc_op10_op20_setup.jpg                       (Phase 4: CAD-Schema 1. vs. 2. Aufspannung)
├── 🎬 uebung_03_simulation_video.mp4                (Phase 4: Render-Video der 3D-Spansimulation)
├── 🌐 3d_auftrag_simulator.html                     (Phase 4: Interaktiver 3D-Browser-Simulator)
│
└── 💰 07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md         (Phase 5: Finanzamtssichere Rechnung von Agent 4)
```

---

## 🤖 Welche Agenten welche Artefakte erzeugen und verwalten

### 1. Phase 1: Auftragseingang & Briefing
* **Artefakt:** `01_KUNDENAUFTRAG_BRIEFING.md`
* **Zuständiger Agent:** **`Agent 1 (Lead-Scout-Agent)`** oder direkte Kunden-E-Mail
* **Inhalt:** Das vollständige technische Briefing: Bauteilmaße ($80 \times 50 \times 12\,\text{mm}$), Rohteilmaße ($85 \times 55 \times 15\,\text{mm}$), Material (EN AW-6082), Maschinentyp (Haas VF-2), Werkzeuge (T01 D=10 mm, T02 D=6 mm) und Budget (480 €).

### 2. Phase 2: Kaufmännische Angebotslegung
* **Artefakt:** `02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`
* **Zuständiger Agent:** **`Agent 4 (Backoffice-Agent)`**
* **Inhalt:** Rechtssicheres B2B-Ingenieurangebot mit Leistungsbeschreibung nach § 18 EStG *(„Ingenieurtechnische CAD/CAM-Prozessauslegung“)*, Zahlungszielen und dem unabdingbaren Haftungsausschluss *(Verpflichtung des Auftraggebers zum Einfahren des ersten Bauteils im Einzelsatz)*.

### 3. Phase 3: Programmierung & Code-Generierung
* **Artefakte:** 
  - `uebung_03_z_min_berechnung.cps` (Postprozessor)
  - `uebung_03_z_min_berechnung.nc` (NC-Maschinenprogramm)
  - `bauteil_1001.stl` (3D-Bauteilgeometrie)
* **Zuständiger Agent:** **`Agent 2 (Postprocessor-Coder-Agent)`**
* **Inhalt:** Der JavaScript-Postprozessor mit integrierter $Z_{\text{min}}$-Sicherheitsabfrage sowie der fertig generierte DIN/ISO-Code für die Haas VF-2 Fräsmaschine.

### 4. Phase 4: Crash-Prüfung, Setup-Sheet & Visualisierung
* **Artefakte:**
  - `05_SICHERHEITS_CRASH_PRUEFBERICHT.md`: Der lückenlose Prüfbericht nach dem 5-Stufen-Sicherheitsprotokoll (Sicherheitszeile, Z-MIN $7{,}0\,\text{mm}$ über Backenoberkante, Spindelstart, Kühlung).
  - `06_EINRICHTEBLATT_SETUP_SHEET.md`: Das druckfertige Dokument für den Werkstattbediener mit Werkzeugliste, Nullpunktlage (G54 vorne links oben) und Drehmomentangaben.
  - `flanschplatte_cnc_depth_levels.jpg` & `cnc_op10_op20_setup.jpg`: Hochauflösende CAD-Grafiken für den Bediener.
  - `uebung_03_simulation_video.mp4` & `3d_auftrag_simulator.html`: Visuelle Frässimulation zur 100 % sicheren Vorab-Abnahme ohne Maschinenstillstand.
* **Zuständiger Agent:** **`Agent 3 (NC-Safety- & Setup-Agent)`**

### 5. Phase 5: Rechnungsstellung & Projektabschluss
* **Artefakt:** `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`
* **Zuständiger Agent:** **`Agent 4 (Backoffice-Agent)`**
* **Inhalt:** Die ordnungsgemäße Honorarabrechnung über 480,00 € netto (571,20 € brutto) mit allen Pflichtangaben nach § 14 UStG und freiberuflicher Leistungsabgrenzung für das Finanzamt Hanau.

---

## 🔒 Qualitätsgarantie & Arbeitsweise
Sobald ein neuer Kundenauftrag eingeht, wird dieser Ordner angelegt. Sämtliche Agenten greifen **nur auf diesen Ordner zu und speichern alle Zwischen- und Endergebnisse genau hier ab**. Dadurch entsteht eine in sich geschlossene, revisionssichere digitale Auftragsakte.
