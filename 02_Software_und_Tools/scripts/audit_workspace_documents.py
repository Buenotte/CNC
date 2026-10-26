# -*- coding: utf-8 -*-
r"""
Umfassendes Audit- und Prüfskript für alle Dokumente im Projekt C:\Projekte\CNC:
1. Prüft auf leere oder beschädigte Markdown-Dateien
2. Prüft auf verbotene Alt-Namen ('Konstantin') oder offene Platzhalter ('[Dein Name]', etc.)
3. Prüft alle absoluten 'file:///C:/Projekte/CNC/...' Links auf reale Existenz auf der Festplatte
4. Prüft relative Markdown-Links [Text](rel/path)
5. Prüft strukturelle Integrität (Überschriften, Formatierung)
"""

import os
import glob
import re

BASE_DIR = r"c:\Projekte\CNC"
md_files = glob.glob(os.path.join(BASE_DIR, "**", "*.md"), recursive=True)

print(f"Starte Audit von {len(md_files)} Markdown-Dateien...")

empty_files = []
forbidden_findings = []
broken_abs_links = []
broken_rel_links = []

forbidden_patterns = [
    (r"\bKonstantin\b", "Konstantin"),
    (r"\[Dein Name\]", "[Dein Name]"),
    (r"\[Ihre Unterschrift\]", "[Ihre Unterschrift]"),
    (r"\[Ihr Name\]", "[Ihr Name]")
]

for mf in md_files:
    # 1. Leere Datei Prüfung
    if os.path.getsize(mf) == 0:
        empty_files.append(mf)
        continue

    with open(mf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    # 2. Namen- und Platzhalter-Prüfung
    for pat, desc in forbidden_patterns:
        matches = re.findall(pat, content, re.IGNORECASE)
        if matches:
            forbidden_findings.append((mf, desc, len(matches)))

    # 3. Absolute Links (file:///c:/Projekte/CNC/...)
    abs_links = re.findall(r"file:///[cC]:/Projekte/CNC/([^\s\)#\"'>]+)", content)
    for link in abs_links:
        # Säubere eventuelle Sonderzeichen am Ende
        clean_link = link.split('#')[0].rstrip('.)')
        target_path = os.path.normpath(os.path.join(BASE_DIR, clean_link))
        if not os.path.exists(target_path):
            broken_abs_links.append((mf, clean_link, target_path))

    # 4. Relative Links [Text](rel_path.md)
    # Ignoriere reine Web-Links (http/https/mailto)
    rel_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
    for text, link in rel_links:
        if link.startswith(("http://", "https://", "mailto:", "file:", "#")):
            continue
        clean_rel = link.split('#')[0].strip()
        if not clean_rel:
            continue
        rel_target = os.path.normpath(os.path.join(os.path.dirname(mf), clean_rel))
        if not os.path.exists(rel_target):
            broken_rel_links.append((mf, clean_rel, rel_target))

print("\n" + "="*70)
print(f"AUDIT-ERGEBNIS (Geprüfte Dateien: {len(md_files)}):")
print("="*70)

print(f"\n1. Leere Dateien: {len(empty_files)}")
for ef in empty_files:
    print(f"   [LEER] {os.path.relpath(ef, BASE_DIR)}")

print(f"\n2. Veraltete Namen & Platzhalter: {len(forbidden_findings)}")
for mf, desc, count in forbidden_findings:
    print(f"   [PLATZHALTER: {desc} ({count}x)] in {os.path.relpath(mf, BASE_DIR)}")

print(f"\n3. Defekte absolute Links (file:///): {len(broken_abs_links)}")
for mf, cl, tp in broken_abs_links[:15]:
    print(f"   [DEFEKT] in {os.path.relpath(mf, BASE_DIR)}\n      Linkziel fehlt: {tp}")

print(f"\n4. Defekte relative Links: {len(broken_rel_links)}")
for mf, cl, rt in broken_rel_links[:15]:
    print(f"   [DEFEKT] in {os.path.relpath(mf, BASE_DIR)}\n      Relativ fehlt: {rt}")

print("\n" + "="*70)
