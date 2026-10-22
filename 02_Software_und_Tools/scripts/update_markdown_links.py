# -*- coding: utf-8 -*-
"""
Aktualisiert Verweise in allen Markdown-Dateien auf die neuen 4 Säulen.
"""

import os
import glob

BASE_DIR = r"c:\Projekte\CNC"

replacements = [
    ("c:/Projekte/CNC/kundenauftraege", "c:/Projekte/CNC/01_Kundenauftraege/auftragsakten_00b_bis_16"),
    ("c:\\Projekte\\CNC\\kundenauftraege", "c:\\Projekte\\CNC\\01_Kundenauftraege\\auftragsakten_00b_bis_16"),
    ("c:/Projekte/CNC/test_auftrag_ubung_03", "c:/Projekte/CNC/01_Kundenauftraege/test_auftrag_ubung_03"),
    ("c:\\Projekte\\CNC\\test_auftrag_ubung_03", "c:\\Projekte\\CNC\\01_Kundenauftraege\\test_auftrag_ubung_03"),
    ("c:/Projekte/CNC/kundenauftrag_01_flanschplatte", "c:/Projekte/CNC/01_Kundenauftraege/referenz_auftrag_flanschplatte"),
    ("c:\\Projekte\\CNC\\kundenauftrag_01_flanschplatte", "c:\\Projekte\\CNC\\01_Kundenauftraege\\referenz_auftrag_flanschplatte"),
    ("c:/Projekte/CNC/ALLE_UEBUNGEN_HANDBUCH.md", "c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/ALLE_UEBUNGEN_HANDBUCH.md"),
    ("c:\\Projekte\\CNC\\ALLE_UEBUNGEN_HANDBUCH.md", "c:\\Projekte\\CNC\\03_Fachdokumentation_und_Wissen\\ALLE_UEBUNGEN_HANDBUCH.md"),
    ("c:/Projekte/CNC/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md", "c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md"),
    ("c:\\Projekte\\CNC\\SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md", "c:\\Projekte\\CNC\\03_Fachdokumentation_und_Wissen\\SICHERHEITS_UND_QUALITAETS_PRUEFLISTE_GCODE.md"),
    ("c:/Projekte/CNC/CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md", "c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md"),
    ("c:\\Projekte\\CNC\\CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md", "c:\\Projekte\\CNC\\04_Recht_Steuern_und_Backoffice\\CAM_Nebentaetigkeit_und_Gewerbe_Leitfaden.md"),
    ("c:/Projekte/CNC/KI_Agenten_System_und_Bauplan.md", "c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/KI_Agenten_System_und_Bauplan.md"),
    ("c:\\Projekte\\CNC\\KI_Agenten_System_und_Bauplan.md", "c:\\Projekte\\CNC\\04_Recht_Steuern_und_Backoffice\\KI_Agenten_System_und_Bauplan.md"),
    ("c:/Projekte/CNC/GitHub_Projekte", "c:/Projekte/CNC/02_Software_und_Tools/GitHub_Projekte"),
    ("c:\\Projekte\\CNC\\GitHub_Projekte", "c:\\Projekte\\CNC\\02_Software_und_Tools\\GitHub_Projekte"),
    ("c:/Projekte/CNC/Portfolio", "c:/Projekte/CNC/04_Recht_Steuern_und_Backoffice/Portfolio"),
    ("c:\\Projekte\\CNC\\Portfolio", "c:\\Projekte\\CNC\\04_Recht_Steuern_und_Backoffice\\Portfolio"),
    ("c:/Projekte/CNC/docs", "c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs"),
    ("c:\\Projekte\\CNC\\docs", "c:\\Projekte\\CNC\\03_Fachdokumentation_und_Wissen\\docs"),
    ("c:/Projekte/CNC/uebungen", "c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/uebungen"),
    ("c:\\Projekte\\CNC\\uebungen", "c:\\Projekte\\CNC\\03_Fachdokumentation_und_Wissen\\uebungen")
]

md_files = glob.glob(os.path.join(BASE_DIR, "**", "*.md"), recursive=True)
updated_count = 0

for file_path in md_files:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content
        for old_str, new_str in replacements:
            if old_str in new_content:
                new_content = new_content.replace(old_str, new_str)

        if new_content != content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated_count += 1
    except Exception as e:
        print(f"Fehler bei {file_path}: {e}")

print(f"Erfolgreich {updated_count} Markdown-Dateien mit den neuen Pfaden aktualisiert!")
