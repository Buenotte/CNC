# -*- coding: utf-8 -*-
"""
Erstellt in JEDEM der 17 Kundenauftrags-Ordner die verbindliche Arbeitsanleitung:
'00_AUFTRAGS_LEITFADEN_UND_AGENTEN_ANLEITUNG.md'

Die Anleitung beschreibt:
1. Welche Artefakte in diesem Ordner generiert werden müssen
2. Wie man den Auftrag Schritt für Schritt mit den 4 KI-Agenten erledigt
3. Die genauen Befehle und Prompts für jeden Agenten
4. Die verbindlichen Abnahmekriterien für 100 % Erledigung
"""

import os
import re

BASE_DIR = r"c:\Projekte\CNC\kundenauftraege"

order_metadata = {
    "auftrag_00b_hallo_welt_mum_systemhaus": {
        "title": "Übung 00b: Hallo Welt Postprozessor",
        "kunde": "Jens Becker (Leiter CAM-Services, Mensch und Maschine Systemhaus GmbH)",
        "budget": "250,00 € netto",
        "tech_focus": "Basis-Postprozessor in JavaScript (.cps) mit ISO-Sicherheitszeile (G90 G17 G21 G94 G40 G80), writeComment() Begrüßung und sauberem M30-Ende.",
        "cps_file": "uebung_00b_hallo_welt.cps",
        "nc_file": "uebung_00b_hallo_welt.nc",
        "agent2_task": "Erstelle/optimiere die Datei uebung_00b_hallo_welt.cps so, dass im Programmkopf eine Sicherheitszeile und der Begrüßungs-Kommentar ausgegeben werden.",
        "agent3_task": "Prüfe den generierten Code uebung_00b_hallo_welt.nc auf das Vorhandensein der Sicherheitszeile und des korrekten M30-Endes."
    },
    "auftrag_01_header_werkzeugbau": {
        "title": "Übung 01: Qualitäts-Rückverfolgbarkeit & Entwickler-Header",
        "kunde": "Stefan Klausner (Geschäftsführer, Klausner Formenbau & Zerspanung)",
        "budget": "350,00 € netto",
        "tech_focus": "Erweiterter Infoblock in onOpen() mit Bauteilname, Kunde, Programmierer (Dipl.-Ing. Bujanovski), Datum, WCS G54 und Maschinentyp.",
        "cps_file": "uebung_01_entwickler_header.cps",
        "nc_file": "uebung_01_entwickler_header.nc",
        "agent2_task": "Passe onOpen() in uebung_01_entwickler_header.cps an, um alle ISO-zertifizierten Rückverfolgbarkeitsdaten im Header auszugeben.",
        "agent3_task": "Verifiziere den Programmkopf in uebung_01_entwickler_header.nc gegen die ISO-9001 Prüfkriterien."
    },
    "auftrag_02_werkzeugliste_feinmechanik": {
        "title": "Übung 02: Automatische Werkzeugliste (Tool Table)",
        "kunde": "Dr.-Ing. Sabine Hofmann (Produktionsleiterin, Bavaria Feinmechanik GmbH)",
        "budget": "450,00 € netto",
        "tech_focus": "Automatische Iteration über alle im CAM verwendeten Werkzeuge und Ausgabe einer formatierten Werkzeugtabelle im Programmkopf.",
        "cps_file": "uebung_02_werkzeugliste.cps",
        "nc_file": "uebung_02_werkzeugliste.nc",
        "agent2_task": "Implementiere in uebung_02_werkzeugliste.cps eine Schleife über getNumberOfSections() / toolTable, die Werkzeugnummer, Durchmesser und Typ sauber listet.",
        "agent3_task": "Prüfe, ob alle im G-Code aufgerufenen Werkzeuge (T-Nummern) lückenlos in der Kopf-Werkzeugliste deklariert sind."
    },
    "auftrag_03_flanschplatte_z_min": {
        "title": "Übung 03: Z-MIN Tiefenberechnung & Schraubstock-Kollisionsschutz",
        "kunde": "Markus Weber (Fertigungsleiter, Schmidt Präzisionstechnik GmbH)",
        "budget": "480,00 € netto",
        "tech_focus": "Automatische Berechnung der tiefsten Z-Koordinate (Z-MIN) jedes Werkzeugs und Warnmeldung bei Überschreiten des Spannrands.",
        "cps_file": "uebung_03_z_min_berechnung.cps",
        "nc_file": "uebung_03_z_min_berechnung.nc",
        "agent2_task": "Integriere die Z-MIN Überwachung in uebung_03_z_min_berechnung.cps und gebe den tiefsten Punkt im Programmkopf aus.",
        "agent3_task": "Führe den 5-Stufen-Sicherheitscheck durch und erstelle das Einrichteblatt mit Abstandsreserve zu den Schraubstockbacken."
    },
    "auftrag_04_lagerplatte_3d_cam": {
        "title": "Übung 04: 3D-CAD-Modellbearbeitung (Lagerplatte)",
        "kunde": "Michael Brandner (Fertigungsleiter, Franken Präzisionsteile GmbH)",
        "budget": "380,00 € netto",
        "tech_focus": "Komplette 2,5D- und 3D-Bearbeitung eines Bauteils (Planfräsen, 2D-Kontur, Kreistasche und Bohrbild) aus 3D-STEP/STL.",
        "cps_file": "uebung_04_3d_modell_cam.cps",
        "nc_file": "uebung_04_3d_modell_cam.nc",
        "agent2_task": "Generiere die optimierten Werkzeugbahnen für die Lagerplatte und passe die Schnittparameter an.",
        "agent3_task": "Prüfe die Bahnübergänge und stelle sicher, dass kein Werkzeug im Eilgang ins Rohteil eintaucht."
    },
    "auftrag_05_einrichtedoku_simulation": {
        "title": "Übung 05: Einrichteblatt-Extraktion & Simulationsprüfung",
        "kunde": "Thomas Kuhn (Inhaber, Kuhn Medizintechnik & CNC-Fräszentrum)",
        "budget": "280,00 € netto",
        "tech_focus": "Automatisierte Extraktion aller Rüstparameter aus NC-Code via cnc_setup_sheet_extractor.py und visuelle Prüfung im Simulator.",
        "cps_file": "uebung_03_z_min_berechnung.cps",
        "nc_file": "uebung_03_z_min_berechnung.nc",
        "agent2_task": "Stelle sicher, dass alle relevanten Kommentarfelder für den Python-Extractor im NC-Code hinterlegt sind.",
        "agent3_task": "Führe cnc_setup_sheet_extractor.py aus und erstelle das druckfertige Rüstdatenblatt für den Maschinenbediener."
    },
    "auftrag_06_sicherer_rueckzug_arbeitsschutz": {
        "title": "Übung 06: Sicherer Rückzug (Safe Retract) & Tisch zur Tür",
        "kunde": "Andreas Eder (Betriebsleiter, Süd-Zerspanung GmbH)",
        "budget": "420,00 € netto",
        "tech_focus": "Automatischer sicherer Rückzug der Z-Achse auf Maschinenkoordinaten (G53 G0 Z0 / M91) vor Tischbewegung zur Tür in onClose().",
        "cps_file": "uebung_06_sicherer_rueckzug.cps",
        "nc_file": "uebung_06_sicherer_rueckzug.nc",
        "agent2_task": "Programmiere in onClose() die zwingende Trennung: Zuerst Z ganz hoch, erst danach Y-Tisch nach vorne zur Tür.",
        "agent3_task": "Verifiziere im NC-Code, dass keine gleichzeitige Z/Y-Bewegung im Maschinen-Nullpunktsystem stattfindet."
    },
    "auftrag_07_spaenefoerderer_schalter": {
        "title": "Übung 07: Konfigurierbare Schalter (Properties)",
        "kunde": "Karsten Wolf (Technischer Leiter, Vogtland Zerspanungstechnik GmbH)",
        "budget": "390,00 € netto",
        "tech_focus": "Erstellung von benutzerdefinierten Schaltern (properties.useChipConveyor, properties.highPressureCooling) im Postprozessor.",
        "cps_file": "uebung_07_spaenefoerderer_schalter.cps",
        "nc_file": "uebung_07_spaenefoerderer_schalter.nc",
        "agent2_task": "Definiere in properties die Schalter und binde die M-Codes (M31/M33 für Späneförderer) bedingungsgesteuert ein.",
        "agent3_task": "Teste den Postprozessor mit Schalterstellung EIN und AUS und vergleiche die resultierenden NC-Dateien."
    },
    "auftrag_08_migration_siemens_ventilblock": {
        "title": "Übung 08: Migration auf Siemens Sinumerik Dialekt",
        "kunde": "Jürgen Meier (Fertigungsleiter, Franken Zerspanung GmbH)",
        "budget": "650,00 € netto",
        "tech_focus": "Übersetzung eines Haas/Fanuc-Postprozessors auf Siemens Sinumerik 840D (WORKPIECE, CYCLE800, SUPA G0 Z0 D0).",
        "cps_file": "uebung_08_fanuc_siemens_dialekt.cps",
        "nc_file": "siemens_ventilblock_post.nc",
        "agent2_task": "Passe die Ausgabe an den Siemens-Steuerungsstandard an (Rohteildefinition WORKPIECE, Zyklenaufrufe, Satznummern).",
        "agent3_task": "Prüfe den Sinumerik-Code auf korrekte D-Korrekturaufrufe (D1) und SUPA-Sicherheitsrückzüge."
    },
    "auftrag_09_schnittdaten_edelstahl": {
        "title": "Übung 09: Schnittdaten-Validierung bei Edelstahl",
        "kunde": "Frank Lehmann (Produktionsleiter, Krupp & Partner Maschinenteile)",
        "budget": "85,00 € / Std. (ca. 340 €)",
        "tech_focus": "Automatische Schnittdaten-Überprüfung (Schnittgeschwindigkeit vc, Drehzahl S, Vorschub F) zur Vermeidung von Werkzeugbruch bei V2A.",
        "cps_file": "uebung_09_schnittdaten_check.cps",
        "nc_file": "uebung_09_schnittdaten_check.nc",
        "agent2_task": "Erstelle eine Plausibilitätsprüfung im Postprozessor, die bei Überschreitung von vc > 120 m/min bei Edelstahl warnt.",
        "agent3_task": "Prüfe die programmierten Drehzahlen und Vorschübe gegen das Tabellenbuch Zerspanungstechnik."
    },
    "auftrag_10_zweite_aufspannung_op20": {
        "title": "Übung 10: 2. Aufspannung (OP20) & WCS G55",
        "kunde": "Robert Schneider (Fertigungsleiter, AluTech Gehäusebau GmbH)",
        "budget": "520,00 € netto",
        "tech_focus": "Umdrehen des Werkstücks (180°), Spannen auf weichen Backen, WCS G55 und Planfräsen des 3 mm Spannrands auf Fertigmaß 12.0 mm.",
        "cps_file": "uebung_10_zweite_aufspannung_g55.cps",
        "nc_file": "uebung_10_zweite_aufspannung_g55.nc",
        "agent2_task": "Konfiguriere das Setup 2 für G55 und programmiere die Planfräsoperation mit Messerkopf.",
        "agent3_task": "Erstelle das 2-Stufen-Einrichteblatt (OP10 auf G54, OP20 auf G55) und prüfe die Z-Endhöhe."
    },
    "auftrag_11_gewindebohren_g84_m8": {
        "title": "Übung 11: Starres Gewindebohren (G84 Rigid Tapping)",
        "kunde": "Christian Meyer (Fertigungsleiter, Meyer Hydraulikkomponenten GmbH)",
        "budget": "460,00 € netto",
        "tech_focus": "Synchronisiertes Gewindebohren ohne Ausgleichsfutter mit exakter Vorschubberechnung (F = S * Steigung, M8 Steigung 1.25 mm).",
        "cps_file": "uebung_11_gewindebohren_g84.cps",
        "nc_file": "uebung_11_gewindebohren_g84.nc",
        "agent2_task": "Programmiere den Zyklus G84 im Postprozessor so, dass F exakt aus Spindeldrehzahl und Gewindesteigung errechnet wird.",
        "agent3_task": "Überprüfe rechnerisch die Zeile G84: Ist F bei S=500 exakt 625 mm/min? Liegt Kernlochbohrung T02 (Ø 6.8 mm) vor?"
    },
    "auftrag_12_radiuskorrektur_g41_h7": {
        "title": "Übung 12: Werkzeugradiuskorrektur (G41 / G40) für H7-Passungen",
        "kunde": "Alexander Wagner (Werkstattleiter, Wagner Getriebebau GmbH)",
        "budget": "580,00 € netto",
        "tech_focus": "Programmierung auf Bauteil-Sollkontur mit G41 (Gleichlauf links) zur Feinjustage von Passungen direkt am Maschinen-Bedienpult.",
        "cps_file": "uebung_12_radiuskorrektur_g41.cps",
        "nc_file": "uebung_12_radiuskorrektur_g41.nc",
        "agent2_task": "Implementiere saubere tangentiale Anfahr- (G41) und Abfahrwege (G40), um Konturverletzungen zu verhindern.",
        "agent3_task": "Prüfe, ob G41 stets mit gerader Anfahrbewegung aktiviert und vor Eilgang G00 lückenlos mit G40 abgewählt wird."
    },
    "auftrag_13_3d_freiformflaeche_alu": {
        "title": "Übung 13: 3D-Freiformflächen & Kugelfräser-Schlichten",
        "kunde": "Dr. Elena Rost (Leiterin Prototypenbau, AeroTech Prototypenbau Bremen)",
        "budget": "750,00 € netto",
        "tech_focus": "3D-Adaptive Clearing (Wirbelfräsen) und paralleles Schlichten mit Vollkugelfräser unter Einhaltung minimaler Raufiefe (Scallop).",
        "cps_file": "uebung_13_3d_freiformflaechen.cps",
        "nc_file": "uebung_13_3d_freiformflaechen.nc",
        "agent2_task": "Optimiere die Punktdichte und die Toleranzeinstellungen (Linearization Tolerance) im Postprozessor für ruckfreie Bahnen.",
        "agent3_task": "Führe eine Kollisionsprüfung des Fräserschafts und Spannfutters gegen die geneigten Bauteilwände durch."
    },
    "auftrag_14_heidenhain_4achs_teilapparat": {
        "title": "Übung 14: Heidenhain Klartext & 4. Achse (A-Achse)",
        "kunde": "Urs Hodel (Produktionsleiter, Alps Precision AG, Schweiz)",
        "budget": "850,00 € netto",
        "tech_focus": "Ausgabe von Heidenhain Klartext (TOOL CALL, L ... FMAX, M91) kombiniert mit Teilapparat-Rotationen (A-Achse).",
        "cps_file": "uebung_14_heidenhain_klartext_4achse.cps",
        "nc_file": "uebung_14_heidenhain_klartext_4achse.nc",
        "agent2_task": "Erstelle die Klartext-Schnittstelle mit automatischer Klemmung/Entklemmung der Rundachse (M10/M11).",
        "agent3_task": "Prüfe die Freifahrhöhe vor Achsrotation: Steht die Spindel vor A-Achs-Drehung sicher auf M91 Z+0?"
    },
    "auftrag_15_fasenfraesen_entgraten": {
        "title": "Übung 15: Automatisiertes Kantenentgraten & Spitzenversatz",
        "kunde": "Matthias Kunz (Geschäftsführer, Kunz Feinwerktechnik)",
        "budget": "380,00 € netto",
        "tech_focus": "Fasenfräsen 45° mit Spitzenversatz (Tip Offset 1.5 - 2.0 mm), damit der Schnitt im optimalen Schnittgeschwindigkeitsbereich vc liegt.",
        "cps_file": "uebung_15_fasenfraesen_entgraten.cps",
        "nc_file": "uebung_15_fasenfraesen_entgraten.nc",
        "agent2_task": "Integriere die Spitzenversatz-Berechnung im CAM/Postprozessor, um Fräsen mit stehender Werkzeugspitze zu verhindern.",
        "agent3_task": "Prüfe die Eintauchtiefe: Reicht der Freiraum unter der Fase aus, ohne in Absätze oder Spannmittel zu schneiden?"
    },
    "auftrag_16_meister_endabnahme_audit": {
        "title": "Übung 16: Meisterprüfung – 5-Punkte-Endabnahme & Zertifikat",
        "kunde": "Dipl.-Ing. Bernd Schäfer (Leiter Qualitätssicherung, Hessen Automotive GmbH)",
        "budget": "490,00 € netto",
        "tech_focus": "Komplettes 5-Punkte-Qualitätsaudit des gesamten Postprozessor-Systems und Ausstellung des offiziellen Prüfzertifikats.",
        "cps_file": "uebung_16_endabnahme_meister_post.cps",
        "nc_file": "kunden_post_generiert.nc",
        "agent2_task": "Führe die finale Code-Synthese aller Module (Header, Werkzeugliste, Z-MIN, Rückzug, M30) durch.",
        "agent3_task": "Führe den vollständigen Audit-Lauf durch und erstelle das signierte Prüfzertifikat für den Kunden."
    }
}

for folder_name, meta in order_metadata.items():
    folder_path = os.path.join(BASE_DIR, folder_name)
    if not os.path.exists(folder_path):
        continue

    guide_path = os.path.join(folder_path, "00_AUFTRAGS_LEITFADEN_UND_AGENTEN_ANLEITUNG.md")

    content = f"""# 📘 Auftrags-Leitfaden & Agenten-Bedienungsanleitung
**Auftrags-Ordner:** `{folder_name}`  
**Projekt / Übung:** {meta['title']}  
**Auftraggeber:** {meta['kunde']}  
**Vereinbartes Budget:** **{meta['budget']}**  
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik (§ 18 EStG)  
**Status:** In Bearbeitung / Systematische Abwicklung

---

## 🎯 1. Technisches Ziel dieses Auftrags
{meta['tech_focus']}

---

## 📂 2. Verbindliche Liste aller Artefakte (Was muss in diesem Ordner stehen?)

Damit dieser Auftrag zu 100 % erledigt ist, müssen **alle folgenden Artefakte direkt in diesem Ordner `{folder_name}` liegen**:

| Artefakt-Name | Dateityp | Zuständiger KI-Agent | Zweck & Inhalt |
| :--- | :---: | :---: | :--- |
| **`00_AUFTRAGS_LEITFADEN_UND_AGENTEN_ANLEITUNG.md`** | Doku | *System* | Diese verbindliche Schritt-für-Schritt-Anleitung. |
| **`KUNDENAUFTRAG_BRIEFING.md`** | Briefing | `Agent 1` / Kunde | Original-Auftrag mit Maschinenpark, Werkzeugen und Vorgaben. |
| **`ANGEBOT_DIPL_ING_BUJANOVSKI.md`** | Vertrag | **`Agent 4`** | Rechtssicheres B2B-Angebot nach § 18 EStG inkl. Haftungsausschluss. |
| **`{meta['cps_file']}`** | JavaScript | **`Agent 2`** | Maschinenspezifischer Postprozessor-Quellcode. |
| **`{meta['nc_file']}`** | G-Code / Klartext | **`Agent 2`** | Fertig generiertes NC-Maschinenprogramm für die Kundenmaschine. |
| **`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`** | Prüfbericht | **`Agent 3`** | 5-Stufen-Sicherheitsbericht (Crash-Check & Z-MIN Verifikation). |
| **`06_EINRICHTEBLATT_SETUP_SHEET.md`** | Werkstatt-Doku | **`Agent 3`** | Rüst- und Werkzeugdatenblatt für den Maschinenbediener. |
| **`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`** | Abrechnung | **`Agent 4`** | Revisionssichere Honorarabrechnung für das Finanzamt Hanau. |

---

## 🤖 3. Schritt-für-Schritt-Anleitung: So wickelst du diesen Auftrag mit den 4 KI-Agenten ab

Du musst die Arbeit nicht selbst programmieren. Nutze einfach die 4 spezialisierten KI-Agenten:

### Schritt 1: Angebot erstellen & kalkulieren (Agent 4)
* **Aufgabe:** Prüft die Kundenanfrage in `KUNDENAUFTRAG_BRIEFING.md`, kalkuliert den Festpreis von **{meta['budget']}** und erstellt das B2B-Angebot.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 4**: Überprüfe das Briefing im Ordner `{folder_name}` und erstelle das formelle Angebot `ANGEBOT_DIPL_ING_BUJANOVSKI.md` inklusive der Klausel zum Einfahren des ersten Bauteils im Einzelsatz.“*

### Schritt 2: Code & Postprozessor umsetzen (Agent 2)
* **Aufgabe:** {meta['agent2_task']}
* **Befehl im Chat:**
  > *„Starte bitte **Agent 2**: Bearbeite den Postprozessor `{meta['cps_file']}` im Ordner `{folder_name}`. {meta['tech_focus']} Generiere im Anschluss das NC-Programm `{meta['nc_file']}`.“*

### Schritt 3: Crash-Prüfung & Einrichteblatt (Agent 3)
* **Aufgabe:** {meta['agent3_task']}
* **Befehl im Chat:**
  > *„Starte bitte **Agent 3**: Führe die 5-Stufen-Sicherheitsprüfung für `{meta['nc_file']}` im Ordner `{folder_name}` durch. Erstelle `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` und das druckfertige Rüstdatenblatt `06_EINRICHTEBLATT_SETUP_SHEET.md`.“*

### Schritt 4: Honorarrechnung stellen (Agent 4)
* **Aufgabe:** Nach erfolgreicher Simulation und Prüfung erstellt Agent 4 die steuersichere Rechnung über **{meta['budget']}** nach § 14 UStG und § 18 EStG.
* **Befehl im Chat:**
  > *„Starte bitte **Agent 4**: Der Auftrag `{folder_name}` ist abgeschlossen. Erstelle die steuerlich korrekte Honorarrechnung `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md` an {meta['kunde']}.“*

---

## 🛡️ 4. Abnahme-Kriterien (Wann ist der Auftrag zu 100 % fertig?)
Ein Auftrag gilt erst dann als vollständig abgeschlossen und lieferbereit, wenn:
1. [ ] Alle oben gelisteten Dateien physisch in diesem Ordner `{folder_name}` existieren.
2. [ ] Der Postprozessor `{meta['cps_file']}` im Simulator fehlerfrei durchläuft.
3. [ ] Im Sicherheitsbericht `05_SICHERHEITS_CRASH_PRUEFBERICHT.md` der Status **BESTANDEN (GRÜN)** dokumentiert ist.
4. [ ] Das Einrichteblatt `06_EINRICHTEBLATT_SETUP_SHEET.md` alle Werkzeuge, Nullpunkte und Drehmomente enthält.
5. [ ] Das Rechnungsdokument `07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md` für das Finanzamt Hanau abgelegt ist.
"""
    with open(guide_path, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Erfolgreich '00_AUFTRAGS_LEITFADEN_UND_AGENTEN_ANLEITUNG.md' in allen 17 Ordnern generiert!")
