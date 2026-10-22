# -*- coding: utf-8 -*-
"""
Vollständiger Link-Fixer für alle 4 Säulen.
"""

import os
import glob
import re

BASE_DIR = r"c:\Projekte\CNC"

path_replacements = [
    # Absolute file:/// links
    ("file:///c:/Projekte/CNC/src/", "file:///c:/Projekte/CNC/02_Software_und_Tools/src/"),
    ("file:///C:/Projekte/CNC/src/", "file:///c:/Projekte/CNC/02_Software_und_Tools/src/"),
    ("file:///c:/Projekte/CNC/tests/", "file:///c:/Projekte/CNC/02_Software_und_Tools/tests/"),
    ("file:///C:/Projekte/CNC/tests/", "file:///c:/Projekte/CNC/02_Software_und_Tools/tests/"),
    ("file:///c:/Projekte/CNC/scripts/", "file:///c:/Projekte/CNC/02_Software_und_Tools/scripts/"),
    ("file:///C:/Projekte/CNC/scripts/", "file:///c:/Projekte/CNC/02_Software_und_Tools/scripts/"),
    ("file:///c:/Projekte/CNC/uebungen/", "file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/uebungen/"),
    ("file:///C:/Projekte/CNC/uebungen/", "file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/uebungen/"),
    ("file:///c:/Projekte/CNC/docs/", "file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/"),
    ("file:///C:/Projekte/CNC/docs/", "file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/"),
    ("file:///c:/Projekte/CNC/kundenauftrag_beispiel.json", "file:///c:/Projekte/CNC/01_Kundenauftraege/kundenauftrag_beispiel.json"),
    ("file:///c:/Projekte/CNC/KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md", "file:///c:/Projekte/CNC/01_Kundenauftraege/KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md"),
    
    # Backslash paths
    ("c:\\Projekte\\CNC\\src\\", "c:\\Projekte\\CNC\\02_Software_und_Tools\\src\\"),
    ("c:\\Projekte\\CNC\\tests\\", "c:\\Projekte\\CNC\\02_Software_und_Tools\\tests\\"),
    ("c:\\Projekte\\CNC\\scripts\\", "c:\\Projekte\\CNC\\02_Software_und_Tools\\scripts\\"),
    ("c:\\Projekte\\CNC\\uebungen\\", "c:\\Projekte\\CNC\\03_Fachdokumentation_und_Wissen\\uebungen\\"),
    ("c:\\Projekte\\CNC\\docs\\", "c:\\Projekte\\CNC\\03_Fachdokumentation_und_Wissen\\docs\\"),
    ("c:\\Projekte\\CNC\\kundenauftrag_beispiel.json", "c:\\Projekte\\CNC\\01_Kundenauftraege\\kundenauftrag_beispiel.json"),
    ("c:\\Projekte\\CNC\\KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md", "c:\\Projekte\\CNC\\01_Kundenauftraege\\KUNDENAUFTRAG_VOLLSTAENDIGER_PROZESSABLAUF_A_BIS_Z.md"),

    # Fix relative image in ALLE_UEBUNGEN_HANDBUCH.md
    ("kundenauftrag_01_flanschplatte/cnc_frasmaschine_realitaet.jpg", "../01_Kundenauftraege/referenz_auftrag_flanschplatte/cnc_frasmaschine_realitaet.jpg")
]

md_files = glob.glob(os.path.join(BASE_DIR, "**", "*.md"), recursive=True)
count = 0

for mf in md_files:
    with open(mf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    new_content = content
    for old, rep in path_replacements:
        new_content = new_content.replace(old, rep)

    # Avoid duplicate prefixes
    for prefix in ["01_Kundenauftraege", "02_Software_und_Tools", "03_Fachdokumentation_und_Wissen", "04_Recht_Steuern_und_Backoffice"]:
        dup = f"{prefix}/{prefix}"
        new_content = new_content.replace(dup, prefix)
        dup_b = f"{prefix}\\{prefix}"
        new_content = new_content.replace(dup_b, prefix)

    if new_content != content:
        with open(mf, "w", encoding="utf-8") as f:
            f.write(new_content)
        count += 1

print(f"Erfolgreich {count} Markdown-Dateien mit allen Pfad-Aktualisierungen versehen.")
