# -*- coding: utf-8 -*-
"""
Erstellt für ALLE 17 Kundenauftrags-Ordner in 01_Kundenauftraege/auftragsakten_00b_bis_16/
die standardisierte 'WORKFLOW_UND_PROMPTS.md' und 'KUNDENAUFTRAG.md' gemäß der neuen Projektregel!
"""

import os
import re

BASE_DIR = r"c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16"

order_configs = {
    "auftrag_00b_hallo_welt_mum_systemhaus": {
        "title": "Auftrag 00b: Hallo Welt Postprozessor",
        "kunde": "Jens Becker (Leiter CAM-Postprozessor-Services)",
        "firma": "Mensch und Maschine Systemhaus GmbH",
        "budget": "250,00 € netto",
        "brutto": "297,50 € brutto",
        "machine": "Standard 3-Achs-Fräsmaschine (Haas/Fanuc-kompatibel)",
        "nc_file": "uebung_00b_hallo_welt.nc",
        "cps_file": "uebung_00b_hallo_welt.cps",
        "tech_req": "Basis-Postprozessor in JavaScript (.cps) mit ISO-Sicherheitszeile (G90 G17 G21 G94 G40 G80), writeComment() Begrüßung im Header und M30-Ende.",
        "test_step2": "Textprüfung auf ISO-Sicherheitszeile N10 G90 G17 G21 G94 G40 G80 und Spindelstopp M05, M09, M30 am Ende.",
        "test_step3": "Überprüfung, dass keine undefinierten Zeichen im Kommentar stehen und die Datei in NCViewer geladen werden kann."
    },
    "auftrag_01_header_werkzeugbau": {
        "title": "Auftrag 01: Qualitäts-Rückverfolgbarkeit & Entwickler-Header",
        "kunde": "Stefan Klausner (Geschäftsführer)",
        "firma": "Klausner Formenbau & Zerspanung",
        "budget": "350,00 € netto",
        "brutto": "416,50 € brutto",
        "machine": "3-Achs-Bearbeitungszentrum Hermle C400",
        "nc_file": "uebung_01_entwickler_header.nc",
        "cps_file": "uebung_01_entwickler_header.cps",
        "tech_req": "ISO-zertifizierter Entwickler-Infoblock in onOpen() mit Bauteilname, Kunde, Programmierer (Dipl.-Ing. Bujanovski), Datum/Uhrzeit, WCS G54 und Hermle-Sicherheitszeile.",
        "test_step2": "Textprüfung des Programmkopfs: Steht 'ENTWICKLER: DIPL.-ING. BUJANOVSKI' und 'KUNDE: KLAUSNER FORMENBAU' in den Klammern (...) drin?",
        "test_step3": "Verifikation gegen ISO-9001 Dokumentationsstandards: Lückenlose Rückverfolgbarkeit für die Qualitätssicherung."
    },
    "auftrag_02_werkzeugliste_feinmechanik": {
        "title": "Auftrag 02: Automatische Werkzeugliste (Tool Table)",
        "kunde": "Dr.-Ing. Sabine Hofmann (Produktionsleiterin)",
        "firma": "Bavaria Feinmechanik GmbH",
        "budget": "450,00 € netto",
        "brutto": "535,50 € brutto",
        "machine": "Chiron FZ 15W High-Speed Fräszentrum (Fanuc 31i)",
        "nc_file": "uebung_02_werkzeugliste.nc",
        "cps_file": "uebung_02_werkzeugliste.cps",
        "tech_req": "Automatische Iteration über getNumberOfSections() und Ausgabe einer formatierten Werkzeugtabelle (T-Nummer, Durchmesser D, Eckenradius CR, Typ) im Programmkopf.",
        "test_step2": "Header-Prüfung: Werden alle verwendeten Werkzeuge (T01 D=10, T02 D=6) im Tabellenkopf gelistet, bevor die erste Bewegung startet?",
        "test_step3": "Rüstzeit-Vergleich: Stimmen die T-Nummern der Werkzeugliste exakt mit den Magazinplätzen der Chiron überein?"
    },
    "auftrag_03_flanschplatte_z_min": {
        "title": "Auftrag 03: Z-MIN Tiefenberechnung & Schraubstock-Crashschutz",
        "kunde": "Markus Weber (Fertigungsleiter)",
        "firma": "Schmidt Präzisionstechnik GmbH",
        "budget": "480,00 € netto",
        "brutto": "571,20 € brutto",
        "machine": "Haas VF-2 (Haas NGC Steuerung)",
        "nc_file": "uebung_03_z_min_berechnung.nc",
        "cps_file": "uebung_03_z_min_berechnung.cps",
        "tech_req": "Automatische Z-MIN Tiefenberechnung für Werkzeug T01 (Außenkontur Z -5.0 mm, Kreistasche Z -3.0 mm) und Kollisionsabstand zu Schraubstockbacken bei Z = -12.0 mm (Spannrand 3.0 mm).",
        "test_step2": "Header-Prüfung auf Z-MIN: -5.000 MM und Simulation der Fräsbahnen in NCViewer.com / 3D-Simulator.",
        "test_step3": "Mathematische Kollisionskontrolle: Reserve = (-12.0 mm) - (-5.0 mm) = +7.0 mm Puffer zu den Stahlbacken!"
    },
    "auftrag_04_lagerplatte_3d_cam": {
        "title": "Auftrag 04: 3D-CAD-Modellbearbeitung (Lagerplatte)",
        "kunde": "Michael Brandner (Fertigungsleiter)",
        "firma": "Franken Präzisionsteile GmbH",
        "budget": "380,00 € netto",
        "brutto": "452,20 € brutto",
        "machine": "DMG MORI CMX 600 V",
        "nc_file": "uebung_04_3d_modell_cam.nc",
        "cps_file": "uebung_04_3d_modell_cam.cps",
        "tech_req": "Komplette 2,5D-Auslegung der Lagerplatte aus 3D-Modell (Planfräsen, 2D-Kontur Z -5 mm, Kreistasche Z -3 mm, 4 Bohrungen D=6 mm Z -12 mm).",
        "test_step2": "Simulation in NCViewer: Prüfung, dass Bohrer T02 die Bohrungen vollständig durchbohrt (Z -12.0 mm), aber nicht in den Schraubstock sticht.",
        "test_step3": "Prüfung der Tiefenstaffelung im Einrichteblatt mit Mindest-Auskraglängen L_min >= 25 mm."
    },
    "auftrag_05_einrichtedoku_simulation": {
        "title": "Auftrag 05: Einrichteblatt-Extraktion & Simulationsprüfung",
        "kunde": "Thomas Kuhn (Inhaber & Werkstattleiter)",
        "firma": "Kuhn Medizintechnik & CNC-Fräszentrum",
        "budget": "280,00 € netto",
        "brutto": "333,20 € brutto",
        "machine": "Hermle C22 5-Achs (Heidenhain TNC 640)",
        "nc_file": "uebung_03_z_min_berechnung.nc",
        "cps_file": "uebung_03_z_min_berechnung.cps",
        "tech_req": "Automatisierte Generierung normgerechter Rüstunterlagen via cnc_setup_sheet_extractor.py und visuelle Prüfung im 3D-Simulator.",
        "test_step2": "Ausführung des Python-Extractors und Prüfung, ob alle Spindeldrehzahlen und Schnitttiefen fehlerfrei erkannt werden.",
        "test_step3": "Prüfung des generierten Einrichteblatts auf Werkstück-Nullpunktlage G54 und Drehmoment-Angaben."
    },
    "auftrag_06_sicherer_rueckzug_arbeitsschutz": {
        "title": "Auftrag 06: Sicherer Rückzug (Safe Retract) & Tisch zur Tür",
        "kunde": "Andreas Eder (Betriebsleiter)",
        "firma": "Süd-Zerspanung GmbH",
        "budget": "420,00 € netto",
        "brutto": "499,80 € brutto",
        "machine": "Mazak VTC-800/30SR (Mazatrol Matrix 2)",
        "nc_file": "uebung_06_sicherer_rueckzug.nc",
        "cps_file": "uebung_06_sicherer_rueckzug.cps",
        "tech_req": "Zwingende sequentielle Trennung in onClose(): Zuerst Z-Achse absolut sicher auf Maschinenhöhe (G53 G0 Z0 / M91), erst danach Tisch Y nach vorne zur Bedienertür.",
        "test_step2": "Satz-für-Satz Kontrolle am Programmende: G53 Z0 muss zwingend vor G53 Y0 stehen (keine Diagonalbewegung!).",
        "test_step3": "Ergonomie-Check: Steht der Maschinentisch am Programmende ergonomisch optimal zur Tür für schnellen Werkstückwechsel?"
    },
    "auftrag_07_spaenefoerderer_schalter": {
        "title": "Auftrag 07: Konfigurierbare Schalter (Properties)",
        "kunde": "Karsten Wolf (Technischer Leiter)",
        "firma": "Vogtland Zerspanungstechnik GmbH",
        "budget": "390,00 € netto",
        "brutto": "464,10 € brutto",
        "machine": "Alzmetall CS 1200",
        "nc_file": "uebung_07_spaenefoerderer_schalter.nc",
        "cps_file": "uebung_07_spaenefoerderer_schalter.cps",
        "tech_req": "Erstellung konfigurierbarer Postprozessor-Schalter (properties.useChipConveyor) für M31/M33 Steuerung des Späneförderers je nach Material.",
        "test_step2": "Testlauf mit property 'useChipConveyor: true' -> Ausgabe von M31 prüfen; Testlauf mit 'false' -> M31 darf nicht im Code stehen.",
        "test_step3": "Code-Audit: Sicherstellen, dass der Späneförderer in onClose() mit M33 automatisch abgeschaltet wird."
    },
    "auftrag_08_migration_siemens_ventilblock": {
        "title": "Auftrag 08: Migration auf Siemens Sinumerik Dialekt",
        "kunde": "Jürgen Meier (Fertigungsleiter)",
        "firma": "Franken Zerspanung GmbH",
        "budget": "650,00 € netto",
        "brutto": "773,50 € brutto",
        "machine": "DMG MORI DMU 50 (Siemens Sinumerik 840D sl)",
        "nc_file": "siemens_ventilblock_post.nc",
        "cps_file": "siemens_ventilblock_post.cps",
        "tech_req": "Übersetzung eines Fanuc-Postprozessors auf echten Siemens Sinumerik 840D Dialekt (WORKPIECE Rohteil, D1 Schneidenkorrektur, SUPA G0 Z0 D0 Sicherheitsrückzug).",
        "test_step2": "Sinumerik-Syntax-Check: Enthält der Code 'WORKPIECE(...)' und 'SUPA G0 Z0 D0' statt Fanuc G53?",
        "test_step3": "Simulationsprüfung des Ventilblocks im Sinumerik-Modus mit CYCLE800 Schwenkebenen."
    },
    "auftrag_09_schnittdaten_edelstahl": {
        "title": "Auftrag 09: Schnittdaten-Validierung bei Edelstahl",
        "kunde": "Frank Lehmann (Produktionsleiter)",
        "firma": "Krupp & Partner Maschinenteile",
        "budget": "85,00 € / Std. (ca. 340 € netto)",
        "brutto": "404,60 € brutto",
        "machine": "Gildemeister CTX beta 800",
        "nc_file": "uebung_09_schnittdaten_check.nc",
        "cps_file": "uebung_09_schnittdaten_check.cps",
        "tech_req": "Automatisierte Schnittdatenüberwachung (vc, S, F) im Postprozessor zur Verhütung von Werkzeugbruch bei Edelstahl (1.4301 / V2A).",
        "test_step2": "Plausibilitätsprüfung: Gibt der Postprozessor eine Warnung aus, wenn vc > 120 m/min bei VHM-Fräsern in Edelstahl überschritten wird?",
        "test_step3": "Tabellenbuch-Abgleich: Drehzahl S und Vorschub F gegen Zerspanungsrichtwerte für V2A gegenprüfen."
    },
    "auftrag_10_zweite_aufspannung_op20": {
        "title": "Auftrag 10: 2. Aufspannung (OP20) & WCS G55",
        "kunde": "Robert Schneider (Fertigungsleiter)",
        "firma": "AluTech Gehäusebau GmbH",
        "budget": "520,00 € netto",
        "brutto": "618,80 € brutto",
        "machine": "Hermle C42 U MT",
        "nc_file": "uebung_10_zweite_aufspannung_g55.nc",
        "cps_file": "uebung_10_zweite_aufspannung_g55.cps",
        "tech_req": "Umdrehen des Bauteils um 180°, Spannen auf fertig bearbeiteten Konturen in weichen Backen, WCS G55 und Planfräsen des 3 mm Spannrands auf Fertigdicke 12.0 mm.",
        "test_step2": "Nullpunkt-Prüfung: Ist für OP20 exakt G55 programmiert? Fährt der Planfräser auf Endmaß Z = 0.0 mm bezogen auf G55?",
        "test_step3": "Prüfung des 2-Stufen-Einrichteblatts (OP10 G54 Schraubstock, OP20 G55 weiche Backen) mit Fotos/CAD-Schemata."
    },
    "auftrag_11_gewindebohren_g84_m8": {
        "title": "Auftrag 11: Starres Gewindebohren (G84 Rigid Tapping)",
        "kunde": "Christian Meyer (Fertigungsleiter)",
        "firma": "Meyer Hydraulikkomponenten GmbH",
        "budget": "460,00 € netto",
        "brutto": "547,40 € brutto",
        "machine": "Haas VF-4SS (Haas NGC)",
        "nc_file": "uebung_11_gewindebohren_g84.nc",
        "cps_file": "uebung_11_gewindebohren_g84.cps",
        "tech_req": "Synchronisiertes Gewindeschneiden G84 ohne Längenausgleichsfutter mit exakter Vorschubberechnung (F = S * Steigung; M8 Steigung 1.25 mm -> S=500, F=625 mm/min).",
        "test_step2": "Rechnerische Formelprüfung im G-Code: Ist F exakt gleich S * 1.25 mm? Ist Kernlochbohrung T02 (Ø 6.8 mm) vorab programmiert?",
        "test_step3": "Prüfung des Gewindebohrer-Rückzugs: Schaltet die Spindel am Bohrungsgrund synchron um (M04 Linkslauf beim Rückzug)?"
    },
    "auftrag_12_radiuskorrektur_g41_h7": {
        "title": "Auftrag 12: Werkzeugradiuskorrektur (G41 / G40) für H7-Passungen",
        "kunde": "Alexander Wagner (Werkstattleiter)",
        "firma": "Wagner Getriebebau GmbH",
        "budget": "580,00 € netto",
        "brutto": "690,20 € brutto",
        "machine": "DMG MORI NVX 5080",
        "nc_file": "uebung_12_radiuskorrektur_g41.nc",
        "cps_file": "uebung_12_radiuskorrektur_g41.cps",
        "tech_req": "Ausgabe von G41 (Gleichlauffräsen links der Kontur) mit tangentialen An-/Abfahrwegen zur Feinjustage von H7-Lagerpassungen direkt an der Steuerung.",
        "test_step2": "Prüfung der Anfahrbewegung: Wird G41 mit einer geraden Anfahrstrecke >= Fräserradius aktiviert? Wird vor Eilgang G00 lückenlos G40 abgewählt?",
        "test_step3": "Maßkontrolle im Einrichteblatt: Hinweis für den Bediener zur Korrekturtabelle D (Verschleißoffset für +0.015 mm Passungstoleranz)."
    },
    "auftrag_13_3d_freiformflaeche_alu": {
        "title": "Auftrag 13: 3D-Freiformflächen & Kugelfräser-Schlichten",
        "kunde": "Dr. Elena Rost (Leiterin Prototypenbau)",
        "firma": "AeroTech Prototypenbau Bremen",
        "budget": "750,00 € netto",
        "brutto": "892,50 € brutto",
        "machine": "Hermle C32 U 5-Achs (Heidenhain TNC 640)",
        "nc_file": "uebung_13_3d_freiformflaechen.nc",
        "cps_file": "uebung_13_3d_freiformflaechen.cps",
        "tech_req": "3D-Adaptive Clearing (Wirbelfräsen mit konstanter Spandicke) & 3D-Schlichten mit Vollkugelfräser unter Einhaltung minimaler Rautiefe (Scallop Height).",
        "test_step2": "Punktdichte- & Toleranzcheck: Sind Sehnenfehler-Toleranzen (Linearization Tolerance) fehlerfrei interpoliert (keine Facettierung)?",
        "test_step3": "Kollisionsprüfung des Fräserschafts und Spannfutters gegen steile 3D-Wandungen im Heidenhain-Prüfprotokoll."
    },
    "auftrag_14_heidenhain_4achs_teilapparat": {
        "title": "Auftrag 14: Heidenhain Klartext & 4. Achse (A-Achse)",
        "kunde": "Urs Hodel (Produktionsleiter)",
        "firma": "Alps Precision AG (Schweiz)",
        "budget": "850,00 € netto",
        "brutto": "1.011,50 € brutto",
        "machine": "Mikron HPM 600 HD (Heidenhain TNC 640)",
        "nc_file": "uebung_14_heidenhain_klartext_4achse.nc",
        "cps_file": "uebung_14_heidenhain_klartext_4achse.cps",
        "tech_req": "Heidenhain Klartext-Ausgabe (TOOL CALL, L ... FMAX, M91) kombiniert mit Teilapparat-Positionierung (A-Achse) und Achsklemmung M10/M11.",
        "test_step2": "Klartext-Syntax-Check: Steht vor jeder A-Achs-Drehung 'L Z+0 R0 FMAX M91' zur sicheren Freifahr-Höhe?",
        "test_step3": "Prüfung der M-Funktionen: Wird die A-Achse vor Bearbeitungsbeginn mit M10 hydraulisch geklemmt und nach Schnitt mit M11 gelöst?"
    },
    "auftrag_15_fasenfraesen_entgraten": {
        "title": "Auftrag 15: Automatisiertes Kantenentgraten & Spitzenversatz",
        "kunde": "Matthias Kunz (Geschäftsführer)",
        "firma": "Kunz Feinwerktechnik",
        "budget": "380,00 € netto",
        "brutto": "452,20 € brutto",
        "machine": "Hedelius Tiltenta 7",
        "nc_file": "uebung_15_fasenfraesen_entgraten.nc",
        "cps_file": "uebung_15_fasenfraesen_entgraten.cps",
        "tech_req": "Fasenfräsen 45° mit Spitzenversatz (Tip Offset 1.5 - 2.0 mm), damit der Schnitt im optimalen vc-Bereich liegt und nicht mit der stehenden Fräserspitze reibt.",
        "test_step2": "Tiefenkontrolle: Liegt die Fräserspitze bei 0.5 mm Fase exakt um den Spitzenversatz (Z = -2.0 mm) tiefer als die Bauteilkante?",
        "test_step3": "Freiraumprüfung: Reicht der Freiraum unter der Fase aus, ohne in darunterliegende Absätze oder Backen zu schneiden?"
    },
    "auftrag_16_meister_endabnahme_audit": {
        "title": "Auftrag 16: Meisterprüfung – 5-Punkte-Endabnahme & Zertifikat",
        "kunde": "Dipl.-Ing. Bernd Schäfer (Leiter Qualitätssicherung)",
        "firma": "Hessen Automotive GmbH",
        "budget": "490,00 € netto",
        "brutto": "583,10 € brutto",
        "machine": "GroB G550 5-Achs-Bearbeitungszentrum (Siemens Sinumerik ONE)",
        "nc_file": "kunden_post_generiert.nc",
        "cps_file": "uebung_16_endabnahme_meister_post.cps",
        "tech_req": "Vollständiges 5-Stufen-Meisteraudit des Maschinencodes, 100 % Null-Kollisions-Zertifizierung und Ausstellung des Prüfberichts vor Auslieferung.",
        "test_step2": "Prüflauf aller 5 Phasen der Sicherheitsprüfliste: Sicherheitszeile, Drehzahl, Z-MIN, Freifahren vor Schwenken, Programmende.",
        "test_step3": "Erstellung des signierten Abnahmezertifikats zur Übergabe an die Automobil-Qualitätssicherung."
    }
}

count = 0

for folder_name, cfg in order_configs.items():
    folder_path = os.path.join(BASE_DIR, folder_name)
    if not os.path.exists(folder_path):
        continue

    wp_path = os.path.join(folder_path, "WORKFLOW_UND_PROMPTS.md")
    ka_path = os.path.join(folder_path, "KUNDENAUFTRAG.md")

    # Read original briefing if available
    briefing_file = os.path.join(folder_path, "KUNDENAUFTRAG_BRIEFING.md")
    briefing_text = ""
    if os.path.exists(briefing_file):
        with open(briefing_file, "r", encoding="utf-8") as bf:
            briefing_text = bf.read()
    else:
        briefing_text = f"Kundenanfrage von {cfg['kunde']} ({cfg['firma']}) für {cfg['title']}."

    # Write KUNDENAUFTRAG.md
    with open(ka_path, "w", encoding="utf-8") as kaf:
        kaf.write(f"""# 📩 Kundenauftrag: {cfg['firma']} ({cfg['title']})

**Auftraggeber:** {cfg['kunde']}  
**Unternehmen:** {cfg['firma']}  
**Empfänger:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
**Zielmaschine:** **{cfg['machine']}**  
**Vereinbartes Budget:** **{cfg['budget']}** ({cfg['brutto']})  

---

## Auftrags-Briefing des Kunden:

{briefing_text}
""")

    # Write WORKFLOW_UND_PROMPTS.md
    with open(wp_path, "w", encoding="utf-8") as wpf:
        wpf.write(f"""# 📋 Workflow-Beschreibung & Prompts: {cfg['title']}

Mit dieser Anleitung wickelst du den Kundenauftrag aus [`KUNDENAUFTRAG.md`](file:///{ka_path.replace(chr(92), '/')}) Schritt für Schritt mit deinen 4 KI-Agenten ab.

Kopiere nacheinander die folgenden **4 Prompts** in unseren Chat. Die Agenten erzeugen dann alle geforderten Artefakte direkt in diesem Ordner [`{folder_name}`](file:///{folder_path.replace(chr(92), '/')}).

---

## 🗂️ 1. Welche Artefakte werden erzeugt und wo genau stehen sie?

| Artefakt-Dateiname | Was ist das? | Wo steht die Datei? *(Speicherort)* | Wer erzeugt sie? |
| :--- | :--- | :--- | :---: |
| **`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`** | Rechtssicheres B2B-Angebot ({cfg['budget']}) | [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///{folder_path.replace(chr(92), '/')}/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) | **Agent 4** *(Backoffice)* |
| **`{cfg['nc_file']}`** | Fertiger Maschinencode für {cfg['machine']} | [`{cfg['nc_file']}`](file:///{folder_path.replace(chr(92), '/')}/{cfg['nc_file']}) | **Agent 2** *(Post-Coder)* |
| **`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`** | 5-Stufen-Sicherheitsprüfbericht *(Null-Kollisions-Garantie)* | [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///{folder_path.replace(chr(92), '/')}/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) | **Agent 3** *(NC-Safety)* |
| **`06_EINRICHTEBLATT_SETUP_SHEET.md`** | Rüstdatenblatt für den Maschinenbediener vor Ort | [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///{folder_path.replace(chr(92), '/')}/06_EINRICHTEBLATT_SETUP_SHEET.md) | **Agent 3** *(NC-Safety)* |
| **`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`** | Revisionssichere Honorarrechnung ({cfg['brutto']}) | [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///{folder_path.replace(chr(92), '/')}/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) | **Agent 4** *(Backoffice)* |

---

## 🧭 2. Der 4-Stufen-Workflow im Überblick:

```
                  1. KUNDENAUFTRAG.md (Liegt bereits im Ordner)
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 1: ANGEBOT ERSTELLEN (Agent 4: Backoffice-Agent)              │
 │ Prompt 1 ausführen ──► Erzeugt: 02_ANGEBOT_DIPL_ING_BUJANOVSKI.md        │
 └───────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 2: NC-MASCHINENCODE GENERIEREN (Agent 2: Postprocessor-Coder)  │
 │ Prompt 2 ausführen ──► Erzeugt: {cfg['nc_file']}
 └───────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 3: SICHERHEIT & EINRICHTEBLATT (Agent 3: NC-Safety-Agent)      │
 │ Prompt 3 ausführen ──► Erzeugt: 05_SICHERHEITS_CRASH_PRUEFBERICHT.md   │
 │                    ──► Erzeugt: 06_EINRICHTEBLATT_SETUP_SHEET.md       │
 └───────────────────────────┬────────────────────────────────────────────┘
                             │
                             ▼
 ┌────────────────────────────────────────────────────────────────────────┐
 │ SCHRITT 4: RECHNUNG STELLEN (Agent 4: Backoffice-Agent)                │
 │ Prompt 4 ausführen ──► Erzeugt: 07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md  │
 └────────────────────────────────────────────────────────────────────────┘
```

---

## 💬 3. Die 4 fertigen Prompts & wie du jedes Artefakt testest:

### 🟢 SCHRITT 1: Angebot erstellen (Agent 4)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 4 (Backoffice-Agent):
Lies die Kundenanfrage in {folder_path}\\KUNDENAUFTRAG.md.
Erstelle direkt im Ordner {folder_path}\\ das formelle B2B-Angebot "02_ANGEBOT_DIPL_ING_BUJANOVSKI.md" für {cfg['kunde']} ({cfg['firma']}) über {cfg['budget']}. Verwende ausschließlich ingenieurmäßige Leistungsbeschreibungen nach § 18 EStG und binde die verbindliche Haftungsausschluss-Klausel für das Einfahren des ersten Werkstücks im Einzelsatz ein.
```

#### 🔍 Wie wird das Angebot getestet und geprüft?
1. **Honorar:** Steht exakt der Festpreis von **{cfg['budget']}** drin?
2. **Freiberufler-Status:** Enthält die Leistungsbeschreibung ingenieurmäßige Begriffe nach § 18 EStG *(keine Einstufung als Gewerbe durch das Finanzamt Hanau)*?
3. **Haftungsausschluss:** Verpflichtung des Kunden zum Einfahren des ersten Werkstücks im Einzelsatz *(Single Block)* an der {cfg['machine']} enthalten?

---

### 🔵 SCHRITT 2: NC-Maschinencode generieren (Agent 2)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 2 (Postprocessor-Coder-Agent):
Generiere für die {cfg['machine']} im Ordner {folder_path}\\ das fertige NC-Programm "{cfg['nc_file']}".
Anforderung: {cfg['tech_req']}
Stelle sicher, dass alle Werkzeugaufrufe, Sicherheitszeilen und Programmabschlüsse fehlerfrei implementiert sind.
```

#### 🔍 Wie wird der generierte NC-Code getestet und geprüft?
1. **Syntax-Check:** {cfg['test_step2']}
2. **Simulation:** Lade den Code in [NCViewer.com](https://ncviewer.com) oder führe ihn lokal aus. Fahren alle Achsen kollisionsfrei ab?

---

### 🛡️ SCHRITT 3: Sicherheitsbericht & Einrichteblatt erstellen (Agent 3)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 3 (NC-Safety- & Setup-Agent):
Führe für die Datei "{cfg['nc_file']}" im Ordner {folder_path}\\ die 5-Stufen-Sicherheitsprüfung nach SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md durch.
Erstelle im selben Ordner:
1. "05_SICHERHEITS_CRASH_PRUEFBERICHT.md" mit Freigabestatus BESTANDEN.
2. "06_EINRICHTEBLATT_SETUP_SHEET.md" als druckfertiges Rüstblatt für den Bediener an der {cfg['machine']} inklusive Werkzeugliste.
```

#### 🔍 Wie werden Sicherheitsbericht und Einrichteblatt getestet und geprüft?
1. **Sicherheitsbericht:** {cfg['test_step3']} Status muss **BESTANDEN (GRÜN)** sein.
2. **Einrichteblatt:** Sind alle Werkzeuge mit Mindest-Auskraglängen $L_{{min}}$, Drehzahlen und Nullpunktlagen vollständig gelistet?

---

### 💰 SCHRITT 4: Rechnungsstellung nach § 18 EStG (Agent 4)
#### Prompt zum Kopieren in den Chat:
```text
Starte bitte Agent 4 (Backoffice-Agent):
Der Auftrag im Ordner {folder_path}\\ ist technisch erfolgreich abgeschlossen und freigegeben.
Erstelle jetzt im selben Ordner die steuersichere Honorarrechnung "07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md" über {cfg['budget']} ({cfg['brutto']}) an {cfg['firma']} mit allen Pflichtangaben nach § 14 UStG und freiberuflicher Leistungsabgrenzung für das Finanzamt Hanau.
```

#### 🔍 Wie wird die Rechnung getestet und geprüft?
1. **Betrag:** Netto-Honorar {cfg['budget']} zzgl. 19 % USt. = **{cfg['brutto']}**.
2. **Steuerliche Pflichtangaben:** Eindeutige Rechnungsnummer, Leistungszeitraum, USt-Ausweis nach § 14 UStG und § 18 EStG Vermerk.

---

## 🛡️ 4. Abnahme-Kriterien (Checkliste für 100 % Erledigung)
* [ ] [`02_ANGEBOT_DIPL_ING_BUJANOVSKI.md`](file:///{folder_path.replace(chr(92), '/')}/02_ANGEBOT_DIPL_ING_BUJANOVSKI.md) existiert und wurde geprüft.
* [ ] [`{cfg['nc_file']}`](file:///{folder_path.replace(chr(92), '/')}/{cfg['nc_file']}) existiert und lief fehlerfrei im Simulator.
* [ ] [`05_SICHERHEITS_CRASH_PRUEFBERICHT.md`](file:///{folder_path.replace(chr(92), '/')}/05_SICHERHEITS_CRASH_PRUEFBERICHT.md) bescheinigt Status **BESTANDEN (GRÜN)**.
* [ ] [`06_EINRICHTEBLATT_SETUP_SHEET.md`](file:///{folder_path.replace(chr(92), '/')}/06_EINRICHTEBLATT_SETUP_SHEET.md) liegt vor.
* [ ] [`07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md`](file:///{folder_path.replace(chr(92), '/')}/07_RECHNUNG_NACH_PARAGRAPH_18_ESTG.md) ist für das Finanzamt Hanau abgelegt.
""")
    count += 1

print(f"Erfolgreich für alle {count} Kundenaufträge KUNDENAUFTRAG.md und WORKFLOW_UND_PROMPTS.md erstellt!")
