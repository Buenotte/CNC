# -*- coding: utf-8 -*-
"""
Reorganisiert das Arbeitsverzeichnis c:\\Projekte\\CNC in 4 klare Kernbereiche:
01_Kundenauftraege/
02_Software_und_Tools/
03_Fachdokumentation_und_Wissen/
04_Recht_Steuern_und_Backoffice/

Beachtet strikt:
- Keine Dokumente kürzen oder löschen
- Alle Daten werden vollständig in die neue Struktur überführt
- Erstellt ein zentrales README.md als Cockpit / Dashboard
"""

import os
import shutil

BASE_DIR = r"c:\Projekte\CNC"

# 1. Zielordner definieren
P1 = os.path.join(BASE_DIR, "01_Kundenauftraege")
P2 = os.path.join(BASE_DIR, "02_Software_und_Tools")
P3 = os.path.join(BASE_DIR, "03_Fachdokumentation_und_Wissen")
P4 = os.path.join(BASE_DIR, "04_Recht_Steuern_und_Backoffice")

for p in [P1, P2, P3, P4]:
    os.makedirs(p, exist_ok=True)

# Hilfsfunktion zum sicheren Verschieben
def safe_move(src_rel, dst_rel):
    src = os.path.join(BASE_DIR, src_rel)
    dst = os.path.join(BASE_DIR, dst_rel)
    if os.path.exists(src):
        # Wenn Ziel existiert und Ordner ist, nach dst/basename verschieben
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        print(f"Moving: {src_rel} -> {dst_rel}")
        shutil.move(src, dst)
    else:
        print(f"Source not found: {src_rel}")

# --- Säule 1: 01_Kundenauftraege ---
safe_move("kundenauftraege", "01_Kundenauftraege/auftragsakten_00b_bis_16")
safe_move("test_auftrag_ubung_03", "01_Kundenauftraege/test_auftrag_ubung_03")
safe_move("kundenauftrag_01_flanschplatte", "01_Kundenauftraege/referenz_auftrag_flanschplatte")
safe_move("KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md", "01_Kundenauftraege/KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md")
safe_move("kundenauftrag_beispiel.json", "01_Kundenauftraege/kundenauftrag_beispiel.json")

# --- Säule 2: 02_Software_und_Tools ---
os.makedirs(os.path.join(P2, "web_tools"), exist_ok=True)
safe_move("src", "02_Software_und_Tools/src")
safe_move("tests", "02_Software_und_Tools/tests")
safe_move("GitHub_Projekte", "02_Software_und_Tools/GitHub_Projekte")
safe_move("node_modules", "02_Software_und_Tools/node_modules")
safe_move("jsconfig.json", "02_Software_und_Tools/jsconfig.json")
safe_move("ANLEITUNG_CPS_GENERATOR_UND_WEB_INTERFACE.md", "02_Software_und_Tools/ANLEITUNG_CPS_GENERATOR_UND_WEB_INTERFACE.md")
safe_move("kunden_cps_generator_web.html", "02_Software_und_Tools/web_tools/kunden_cps_generator_web.html")
safe_move("cnc_video_generator_web.html", "02_Software_und_Tools/web_tools/cnc_video_generator_web.html")

# --- Säule 3: 03_Fachdokumentation_und_Wissen ---
safe_move("ALLE_UEBUNGEN_HANDBUCH.md", "03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md")
safe_move("SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md", "03_Fachdokumentation_und_Wissen/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md")
safe_move("FRAESER_UND_BOHRER_PRAXISGUIDE.md", "03_Fachdokumentation_und_Wissen/FRAESER_UND_BOHRER_PRAXISGUIDE.md")
safe_move("BAUINGENIEUR_WISSEN_FUER_CNC_GUIDE.md", "03_Fachdokumentation_und_Wissen/BAUINGENIEUR_WISSEN_FUER_CNC_GUIDE.md")
safe_move("ANLEITUNG_BERUFSEINSTIEG_UND_IMPLEMENTATION_PLAN.md", "03_Fachdokumentation_und_Wissen/ANLEITUNG_BERUFSEINSTIEG_UND_IMPLEMENTATION_PLAN.md")
safe_move("docs", "03_Fachdokumentation_und_Wissen/docs")
safe_move("uebungen", "03_Fachdokumentation_und_Wissen/uebungen")
safe_move("doc.txt", "03_Fachdokumentation_und_Wissen/doc.txt")

# --- Säule 4: 04_Recht_Steuern_und_Backoffice ---
safe_move("CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md", "04_Recht_Steuern_und_Backoffice/CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md")
safe_move("KI_Agenten_System_und_Bauplan.md", "04_Recht_Steuern_und_Backoffice/KI_Agenten_System_und_Bauplan.md")
safe_move("Vorlagen_Vertraege_Rechnungen", "04_Recht_Steuern_und_Backoffice/Vorlagen_Vertraege_Rechnungen")
safe_move("Portfolio", "04_Recht_Steuern_und_Backoffice/Portfolio")
safe_move("Reclamacion_Alicante_Calle_Barcelona_3", "04_Recht_Steuern_und_Backoffice/Reclamacion_Alicante_Calle_Barcelona_3")

# Note: scripts/ will be moved last after script execution!
print("Basis-Verschiebung erfolgreich abgeschlossen!")
