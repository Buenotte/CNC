# -*- coding: utf-8 -*-
import os, glob

BASE_DIR = r"c:\Projekte\CNC"

fixes = [
    ("file:///c:/Projekte/CNC/doc.txt", "file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/doc.txt"),
    ("file:///C:/Projekte/CNC/doc.txt", "file:///c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/doc.txt"),
    ("file:///c:/Projekte/CNC/GitHub_Projekte/cnc_setup_sheet_extractor.py", "file:///c:/Projekte/CNC/02_Software_und_Tools/GitHub_Projekte/cnc_setup_sheet_extractor.py"),
    ("file:///C:/Projekte/CNC/GitHub_Projekte/cnc_setup_sheet_extractor.py", "file:///c:/Projekte/CNC/02_Software_und_Tools/GitHub_Projekte/cnc_setup_sheet_extractor.py"),
    ("c:\\Projekte\\CNC\\doc.txt", "c:\\Projekte\\CNC\\03_Fachdokumentation_und_Wissen\\doc.txt"),
    ("c:\\Projekte\\CNC\\GitHub_Projekte\\cnc_setup_sheet_extractor.py", "c:\\Projekte\\CNC\\02_Software_und_Tools\\GitHub_Projekte\\cnc_setup_sheet_extractor.py")
]

for mf in glob.glob(os.path.join(BASE_DIR, "**", "*.md"), recursive=True):
    with open(mf, "r", encoding="utf-8", errors="ignore") as f:
        c = f.read()
    nc = c
    for o, n in fixes:
        nc = nc.replace(o, n)
    if nc != c:
        with open(mf, "w", encoding="utf-8") as f:
            f.write(nc)
print("Letzte 5 Links erfolgreich korrigiert!")
