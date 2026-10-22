# -*- coding: utf-8 -*-
"""
Repariert alle gefundenen Pfade und Platzhalter:
1. Ersetzt [Ihr Name] / [Ihre Unterschrift] mit Dipl.-Ing. Buenotte
2. Korrigiert alle verschobenen Dateipfade (web_tools, Vorlagen, referenz_auftrag, etc.)
"""

import os
import glob
import re

BASE_DIR = r"c:\Projekte\CNC"

# Mapping von alten Pfaden/Fragmenten auf neue Pfade
path_fixes = [
    # Web tools
    ("kunden_cps_generator_web.html", "02_Software_und_Tools/web_tools/kunden_cps_generator_web.html"),
    ("cnc_video_generator_web.html", "02_Software_und_Tools/web_tools/cnc_video_generator_web.html"),
    ("ANLEITUNG_CPS_GENERATOR_UND_WEB_INTERFACE.md", "02_Software_und_Tools/ANLEITUNG_CPS_GENERATOR_UND_WEB_INTERFACE.md"),
    
    # Vorlagen & Verträge
    ("Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md", "04_Recht_Steuern_und_Backoffice/Vorlagen_Vertraege_Rechnungen/Vorlage_Angebot_und_Rechnung_Ingenieurbuero.md"),
    ("Vorlagen_Vertraege_Rechnungen/Vorlage_Geheimhaltungserklaerung_NDA.md", "04_Recht_Steuern_und_Backoffice/Vorlagen_Vertraege_Rechnungen/Vorlage_Geheimhaltungserklaerung_NDA.md"),
    ("Vorlagen_Vertraege_Rechnungen", "04_Recht_Steuern_und_Backoffice/Vorlagen_Vertraege_Rechnungen"),
    
    # Referenz Flanschplatte
    ("kundenauftrag_01_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md", "01_Kundenauftraege/referenz_auftrag_flanschplatte/KUNDEN_AUFTRAG_UND_KLICK_ANLEITUNG.md"),
    ("kundenauftrag_01_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md", "01_Kundenauftraege/referenz_auftrag_flanschplatte/EINRICHTEBLATT_SETUP_SHEET.md"),
    ("kundenauftrag_01_flanschplatte/3d_auftrag_simulator.html", "01_Kundenauftraege/referenz_auftrag_flanschplatte/3d_auftrag_simulator.html"),
    ("kundenauftrag_01_flanschplatte/bauteil_1001.stl", "01_Kundenauftraege/referenz_auftrag_flanschplatte/bauteil_1001.stl"),
    ("kundenauftrag_01_flanschplatte/cnc_frasmaschine_realitaet.jpg", "01_Kundenauftraege/referenz_auftrag_flanschplatte/cnc_frasmaschine_realitaet.jpg"),
    ("kundenauftrag_01_flanschplatte/cnc_g54_nullpunkt_ecke.jpg", "01_Kundenauftraege/referenz_auftrag_flanschplatte/cnc_g54_nullpunkt_ecke.jpg"),
    ("kundenauftrag_01_flanschplatte/cnc_g54_spindel_setup.jpg", "01_Kundenauftraege/referenz_auftrag_flanschplatte/cnc_g54_spindel_setup.jpg"),
    ("kundenauftrag_01_flanschplatte", "01_Kundenauftraege/referenz_auftrag_flanschplatte"),
    
    # Handbücher
    ("ALLE_UEBUNGEN_HANDBUCH.md", "03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md"),
    ("SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md", "03_Fachdokumentation_und_Wissen/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md"),
    ("FRAESER_UND_BOHRER_PRAXISGUIDE.md", "03_Fachdokumentation_und_Wissen/FRAESER_UND_BOHRER_PRAXISGUIDE.md"),
    ("BAUINGENIEUR_WISSEN_FUER_CNC_GUIDE.md", "03_Fachdokumentation_und_Wissen/BAUINGENIEUR_WISSEN_FUER_CNC_GUIDE.md"),
    ("ANLEITUNG_BERUFSEINSTIEG_UND_IMPLEMENTATION_PLAN.md", "03_Fachdokumentation_und_Wissen/ANLEITUNG_BERUFSEINSTIEG_UND_IMPLEMENTATION_PLAN.md"),
    
    # Portfolio
    ("Portfolio/Ingenieurbuero_CAD_CAM_Portfolio_Mappe.md", "04_Recht_Steuern_und_Backoffice/Portfolio/Ingenieurbuero_CAD_CAM_Portfolio_Mappe.md"),
    ("Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md", "04_Recht_Steuern_und_Backoffice/Portfolio/Vorlage_Einrichteblatt_und_Werkzeugliste.md"),
    ("Portfolio/Projekt_01_25D_Praezisionsfraesteil", "04_Recht_Steuern_und_Backoffice/Portfolio/Projekt_01_25D_Praezisionsfraesteil"),
    ("Portfolio/Projekt_02_3plus2_Mehrseiten_Ventilblock", "04_Recht_Steuern_und_Backoffice/Portfolio/Projekt_02_3plus2_Mehrseiten_Ventilblock"),
    ("Portfolio/Projekt_03_3D_Freiform_und_5Achs", "04_Recht_Steuern_und_Backoffice/Portfolio/Projekt_03_3D_Freiform_und_5Achs"),
    ("Portfolio/Projekt_04_Postprozessor_und_CAM_Automatisierung", "04_Recht_Steuern_und_Backoffice/Portfolio/Projekt_04_Postprozessor_und_CAM_Automatisierung"),
    
    # Backoffice
    ("CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md", "04_Recht_Steuern_und_Backoffice/CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md"),
    ("KI_Agenten_System_und_Bauplan.md", "04_Recht_Steuern_und_Backoffice/KI_Agenten_System_und_Bauplan.md")
]

# Relative link fixes in GitHub_Projekte/README.md:
github_readme = os.path.join(BASE_DIR, "02_Software_und_Tools", "GitHub_Projekte", "README.md")
if os.path.exists(github_readme):
    with open(github_readme, "r", encoding="utf-8") as f:
        gh_c = f.read()
    gh_c = gh_c.replace("../../Portfolio/", "../../04_Recht_Steuern_und_Backoffice/Portfolio/")
    gh_c = gh_c.replace("../Portfolio/", "../../04_Recht_Steuern_und_Backoffice/Portfolio/")
    with open(github_readme, "w", encoding="utf-8") as f:
        f.write(gh_c)

# Fix KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md
az_file = os.path.join(BASE_DIR, "01_Kundenauftraege", "KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md")
if os.path.exists(az_file):
    with open(az_file, "r", encoding="utf-8") as f:
        az_c = f.read()
    az_c = az_c.replace("[Ihr Name]", "Dipl.-Ing. Buenotte")
    az_c = az_c.replace("[Ihre Unterschrift]", "Dipl.-Ing. Buenotte")
    with open(az_file, "w", encoding="utf-8") as f:
        f.write(az_c)

# Now fix all markdown files
md_files = glob.glob(os.path.join(BASE_DIR, "**", "*.md"), recursive=True)
count = 0

for mf in md_files:
    with open(mf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    new_content = content

    # Replace absolute file:/// paths
    for old_sub, new_sub in path_fixes:
        # Check both forward slashes and backward slashes
        old_pattern_fwd = f"file:///c:/Projekte/CNC/{old_sub}"
        new_pattern_fwd = f"file:///c:/Projekte/CNC/{new_sub}"
        new_content = new_content.replace(old_pattern_fwd, new_pattern_fwd)

        old_pattern_fwd_cap = f"file:///C:/Projekte/CNC/{old_sub}"
        new_pattern_fwd_cap = f"file:///C:/Projekte/CNC/{new_sub}"
        new_content = new_content.replace(old_pattern_fwd_cap, new_pattern_fwd_cap)

        old_pattern_back = f"c:\\Projekte\\CNC\\{old_sub.replace('/', chr(92))}"
        new_pattern_back = f"c:\\Projekte\\CNC\\{new_sub.replace('/', chr(92))}"
        new_content = new_content.replace(old_pattern_back, new_pattern_back)

    # Avoid duplicate 01_Kundenauftraege/01_Kundenauftraege
    for prefix in ["01_Kundenauftraege", "02_Software_und_Tools", "03_Fachdokumentation_und_Wissen", "04_Recht_Steuern_und_Backoffice"]:
        dup = f"{prefix}/{prefix}"
        new_content = new_content.replace(dup, prefix)
        dup_back = f"{prefix}\\{prefix}"
        new_content = new_content.replace(dup_back, prefix)

    if new_content != content:
        with open(mf, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1

print(f"Reparatur abgeschlossen: {count} Markdown-Dateien aktualisiert.")
