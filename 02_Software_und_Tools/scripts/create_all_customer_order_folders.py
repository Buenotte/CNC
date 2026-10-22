# -*- coding: utf-8 -*-
"""
Erstellt für jeden der 17 Kundenaufträge einen eigenen, perfekt organisierten Ordner
unter c:\\Projekte\\CNC\\kundenauftraege\\ mit:
1. KUNDENAUFTRAG_BRIEFING.md (Original-Anfrage des Kunden)
2. ANGEBOT_DIPL_ING_BUENOTTE.md (Von Agent 4 erstelltes, rechtssicheres Angebot nach § 18 EStG)
3. Vorhandene Quellcode-Dateien (.cps / .nc) aus uebungen/ kopiert
4. STATUS_UND_CHECKLISTE.md (Übersicht der Dateien & Bearbeitungsstatus)
"""

import os
import re
import shutil

BASE_DIR = r"c:\Projekte\CNC"
HANDBUCH_PATH = os.path.join(BASE_DIR, "ALLE_UEBUNGEN_HANDBUCH.md")
TARGET_DIR = os.path.join(BASE_DIR, "kundenauftraege")
UEBUNGEN_DIR = os.path.join(BASE_DIR, "uebungen")

os.makedirs(TARGET_DIR, exist_ok=True)

with open(HANDBUCH_PATH, "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"# (Übung [^\n]+)\n\n## 📩 Der reale Kundenauftrag zu Übung ([^\n]+)\n\n(.*?)\n---"
matches = list(re.finditer(pattern, content, re.DOTALL))

folder_mapping = [
    ("00b", "auftrag_00b_hallo_welt_mum_systemhaus", ["uebung_00b_hallo_welt.cps", "uebung_00b_hallo_welt.nc"]),
    ("01", "auftrag_01_header_werkzeugbau", ["uebung_01_entwickler_header.cps", "uebung_01_entwickler_header.nc"]),
    ("02", "auftrag_02_werkzeugliste_feinmechanik", ["uebung_02_werkzeugliste.cps", "uebung_02_werkzeugliste.nc"]),
    ("03", "auftrag_03_flanschplatte_z_min", ["uebung_03_z_min_berechnung.cps", "uebung_03_z_min_berechnung.nc"]),
    ("04", "auftrag_04_lagerplatte_3d_cam", ["uebung_04_3d_modell_cam.cps"]),
    ("05", "auftrag_05_einrichtedoku_simulation", []),
    ("06", "auftrag_06_sicherer_rueckzug_arbeitsschutz", ["uebung_06_sicherer_rueckzug.cps"]),
    ("07", "auftrag_07_spaenefoerderer_schalter", ["uebung_07_spaenefoerderer_schalter.cps"]),
    ("08", "auftrag_08_migration_siemens_ventilblock", ["uebung_08_fanuc_siemens_dialekt.cps", "siemens_ventilblock_post.cps", "siemens_ventilblock_post.nc"]),
    ("09", "auftrag_09_schnittdaten_edelstahl", ["uebung_09_schnittdaten_check.cps"]),
    ("10", "auftrag_10_zweite_aufspannung_op20", ["uebung_10_zweite_aufspannung_g55.cps"]),
    ("11", "auftrag_11_gewindebohren_g84_m8", ["uebung_11_gewindebohren_g84.cps"]),
    ("12", "auftrag_12_radiuskorrektur_g41_h7", ["uebung_12_radiuskorrektur_g41.cps"]),
    ("13", "auftrag_13_3d_freiformflaeche_alu", ["uebung_13_3d_freiformflaechen.cps"]),
    ("14", "auftrag_14_heidenhain_4achs_teilapparat", ["uebung_14_heidenhain_klartext_4achse.cps"]),
    ("15", "auftrag_15_fasenfraesen_entgraten", ["uebung_15_fasenfraesen_entgraten.cps"]),
    ("16", "auftrag_16_meister_endabnahme_audit", ["uebung_16_endabnahme_meister_post.cps", "kunden_post_generiert.cps", "kunden_post_generiert.nc"])
]

overview_rows = []

for idx, (ueb_id, folder_name, source_files) in enumerate(folder_mapping):
    match = matches[idx]
    uebung_title = match.group(1).strip()
    order_subtitle = match.group(2).strip()
    order_body = match.group(3).strip()
    
    order_dir = os.path.join(TARGET_DIR, folder_name)
    os.makedirs(order_dir, exist_ok=True)
    
    # 1. KUNDENAUFTRAG_BRIEFING.md
    briefing_path = os.path.join(order_dir, "KUNDENAUFTRAG_BRIEFING.md")
    briefing_content = f"""# 📩 Kundenauftrag: {uebung_title}
**Auftrags-Kategorie:** {order_subtitle}
**Auftragnehmer:** Dipl.-Ing. Buenotte – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

{order_body}

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUENOTTE.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.
"""
    with open(briefing_path, "w", encoding="utf-8") as f:
        f.write(briefing_content)
        
    # 2. Extract client info for ANGEBOT
    sender_match = re.search(r"\*\*Von:\*\*\s*([^\n]+)", order_body)
    sender = sender_match.group(1).strip() if sender_match else "Auftraggeber"
    
    subject_match = re.search(r"\*\*Betreff:\*\*\s*([^\n]+)", order_body)
    subject = subject_match.group(1).strip() if subject_match else uebung_title
    
    budget_match = re.search(r"(\d+[\d.,]*\s*€)", order_body)
    budget_str = budget_match.group(1) if budget_match else "Nach Aufwand (Stundensatz 85,00 €)"
    
    # Generate formal engineering proposal from Agent 4
    angebot_path = os.path.join(order_dir, "ANGEBOT_DIPL_ING_BUENOTTE.md")
    angebot_content = f"""# 📄 Freiberufliches Ingenieur-Angebot
**Ingenieurbüro Dipl.-Ing. Buenotte**  
Softwaretechnik & CAD/CAM-Fertigungsprozesse  
63526 Erlensee | E-Mail: kontakt@ingenieurbuero-buenotte.de  
Steuerliche Einordnung: Freiberufliche Tätigkeit nach § 18 Abs. 1 Nr. 1 EStG (Finanzamt Hanau)

---

**An:**  
{sender}  

**Datum:** 22. Oktober 2026  
**Angebots-Nummer:** ANG-2026-{ueb_id.upper()}-01  
**Projekt / Betreff:** {subject}  

Sehr geehrte Damen und Herren,

vielen Dank für Ihre Anfrage. Gerne biete ich Ihnen die ingenieurtechnische Bearbeitung Ihres Auftrags wie folgt an:

### 1. Leistungsumfang (Ingenieurtechnische Dienstleistung gem. § 18 EStG)
* **Ingenieurtechnische Prozessanalyse & Schnittstellenauslegung** bezüglich Ihrer Steuerung und Maschinenkinematik.
* **Entwicklung / Anpassung maschinenspezifischer Algorithmen** für den Postprozessor bzw. mathematisch optimierte 3D-Bahnplanung.
* **Statische Sicherheits- und Syntaxprüfung** des Maschinencodes nach mehrstufigem Industriestandard.
* **Erstellung der Dokumentation:** Bereitstellung des kommentierten Quellcodes (.cps / NC) sowie des Einrichtedatenblatts für das Fertigungspersonal.

### 2. Honorar & Abrechnung
* **Vergütung:** **{budget_str} netto** (zzgl. gesetzl. MwSt. gem. § 14 UStG).
* **Zahlungsbedingungen:** 14 Tage netto nach Abnahme und Datenübergabe.
* **Lieferform:** 100 % digital per verschlüsseltem Datentransfer (E-Mail / Cloud / GitHub).

### 3. Technischer Haftungsausschluss & Mitwirkungspflichten des Auftraggebers
Gemäß den ingenieurrechtlichen Sorgfaltspflichten obliegt die finale Prüfung der Werkzeugdaten, der Spannmittel sowie das überwachte Einfahren des ersten Bauteils im Einzelsatzbetrieb mit reduzierter Vorschubübersteuerung dem qualifizierten Bedienpersonal des Auftraggebers an der realen Maschine.

Mit freundlichen Grüßen  
**Dipl.-Ing. Buenotte**  
*(Freiberuflicher Ingenieur)*
"""
    with open(angebot_path, "w", encoding="utf-8") as f:
        f.write(angebot_content)

    # 3. Copy existing source files from uebungen/ into this order folder
    copied_files = []
    for s_file in source_files:
        src = os.path.join(UEBUNGEN_DIR, s_file)
        if os.path.exists(src):
            dst = os.path.join(order_dir, s_file)
            shutil.copy2(src, dst)
            copied_files.append(s_file)

    # For exercise 3 / 4, copy 3D model if available
    stl_src = os.path.join(BASE_DIR, "kundenauftrag_01_flanschplatte", "bauteil_1001.stl")
    if ueb_id in ["03", "04", "05"] and os.path.exists(stl_src):
        dst_stl = os.path.join(order_dir, "bauteil_1001.stl")
        shutil.copy2(stl_src, dst_stl)
        copied_files.append("bauteil_1001.stl")

    # 4. STATUS_UND_DATEIEN.md
    status_path = os.path.join(order_dir, "STATUS_UND_DATEIEN.md")
    status_content = f"""# 📁 Auftragsordner: {folder_name}
**Zugehörige Übung:** {uebung_title}  
**Kunde:** {sender}  
**Vereinbartes Budget:** {budget_str}

## In diesem Ordner enthaltene Dateien:
1. `KUNDENAUFTRAG_BRIEFING.md` – Vollständiger Kundenbriefing-Text mit Maschinen- und Bauteildaten.
2. `ANGEBOT_DIPL_ING_BUENOTTE.md` – Offizielles Angebot von Dipl.-Ing. Buenotte (Agent 4) nach § 18 EStG.
"""
    for cf in copied_files:
        status_content += f"* `{cf}` – Projektspezifische Quellcode-/Modelldatei.\n"

    status_content += f"""
## Nächste Schritte:
* Zum Prüfen des Codes: `Agent 3` aufrufen (*„Prüfe den Code im Ordner {folder_name}“*).
* Zur Postprozessor-Änderung: `Agent 2` aufrufen (*„Passe den Postprozessor in {folder_name} an...“*).
"""
    with open(status_path, "w", encoding="utf-8") as f:
        f.write(status_content)

    overview_rows.append((ueb_id, folder_name, sender, budget_str))

# Create Master Index: UEBERSICHT_ALLE_KUNDENAUFTRAEGE.md
master_index_path = os.path.join(TARGET_DIR, "UEBERSICHT_ALLE_KUNDENAUFTRAEGE.md")
master_content = """# 🗂️ Zentrale Übersicht: Alle 17 Kundenauftrags-Ordner

Hier findest du für **jeden einzelnen Kundenauftrag einen eigenständigen Ordner** mit allen zugehörigen Dokumenten:
* Das **Kundenbriefing** (`KUNDENAUFTRAG_BRIEFING.md`)
* Das offizielle **Angebot von Dipl.-Ing. Buenotte** (`ANGEBOT_DIPL_ING_BUENOTTE.md` nach § 18 EStG)
* Die zugehörigen **Quellcode-Dateien** (`.cps`, `.nc`, 3D-Modelle)
* Die **Statusübersicht** (`STATUS_UND_DATEIEN.md`)

---

## 📋 Tabelle aller Kundenauftrags-Ordner:

| Nr. | Auftragsordner | Kunde / Unternehmen | Vereinbartes Budget | Direktlink zum Ordner |
| :---: | :--- | :--- | :---: | :--- |
"""

for ueb_id, f_name, snd, bg in overview_rows:
    master_content += f"| **{ueb_id}** | `{f_name}` | {snd} | **{bg}** | [{f_name}](file:///{TARGET_DIR.replace(chr(92), '/')}/{f_name}) |\n"

master_content += """
---

## 💡 Wie du einen Auftrag mit deinen KI-Agenten bearbeitest:
* **Angebot anpassen:** *„Starte Agent 4: Passe das Angebot im Ordner `auftrag_03_flanschplatte_z_min` an.“*
* **Postprozessor schreiben:** *„Starte Agent 2: Bearbeite die .cps-Datei im Ordner `auftrag_01_header_werkzeugbau`.“*
* **Sicherheitscheck durchführen:** *„Starte Agent 3: Führe den Crash-Check für das NC-Programm im Ordner `auftrag_03_flanschplatte_z_min` durch.“*
"""

with open(master_index_path, "w", encoding="utf-8") as f:
    f.write(master_content)

print(f"Erfolgreich {len(folder_mapping)} Kundenauftrags-Ordner in {TARGET_DIR} erstellt!")
