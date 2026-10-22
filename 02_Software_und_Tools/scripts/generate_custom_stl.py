# -*- coding: utf-8 -*-
"""
Parametrischer CAD-Generator fuer beliebige Test-Bauteile (STL-Format):
Erstellt einen praezisen, wasserdichten CAD-Volumenkoerper mit benutzerdefinierten Massen:
- Quader-Grundkoerper (Laenge X, Breite Y, Dicke Z)
- Optionale Kreistasche im Zentrum (Durchmesser, Tiefe)
- Optionale Durchgangsbohrungen in den Ecken
"""

import os
import sys
import argparse
import trimesh

def create_parametric_stl(length=80.0, width=50.0, height=12.0, 
                          pocket_dia=30.0, pocket_depth=3.0, 
                          hole_dia=6.0, hole_margin=10.0, 
                          output_path="custom_part.stl"):
    print(f"-> Generiere CAD-Bauteil: {length}x{width}x{height} mm...")
    
    # 1. Grundquader
    box = trimesh.creation.box(extents=[length, width, height])
    box.apply_translation([length / 2.0, width / 2.0, -height / 2.0])
    
    cutters = []
    
    # 2. Optionale Kreistasche
    if pocket_dia > 0 and pocket_depth > 0:
        pocket_r = pocket_dia / 2.0
        p_cyl = trimesh.creation.cylinder(radius=pocket_r, height=pocket_depth + 0.2, sections=64)
        p_cyl.apply_translation([length / 2.0, width / 2.0, -pocket_depth / 2.0 + 0.1])
        cutters.append(p_cyl)
        print(f"   + Kreistasche: D={pocket_dia} mm, Tiefe={pocket_depth} mm im Zentrum")
        
    # 3. Optionale 4 Durchgangsbohrungen
    if hole_dia > 0 and hole_margin > 0:
        hr = hole_dia / 2.0
        holes = [
            (hole_margin, hole_margin),
            (length - hole_margin, hole_margin),
            (length - hole_margin, width - hole_margin),
            (hole_margin, width - hole_margin)
        ]
        for hx, hy in holes:
            h_cyl = trimesh.creation.cylinder(radius=hr, height=height + 4.0, sections=36)
            h_cyl.apply_translation([hx, hy, -height / 2.0])
            cutters.append(h_cyl)
        print(f"   + 4 Bohrungen: D={hole_dia} mm bei Randabstand={hole_margin} mm")
        
    # 4. Boolescher Schnitt mit Manifold3D
    if cutters:
        result = trimesh.boolean.difference([box] + cutters, engine='manifold')
    else:
        result = box
        
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    result.export(output_path, file_type='stl_ascii')
    
    vol_cm3 = result.volume / 1000.0
    mass_al = vol_cm3 * 2.70
    
    print(f"-> Fertig! Gespeichert unter: {output_path}")
    print(f"   Watertight: {result.is_watertight} | Volumen: {vol_cm3:.2f} cm3 | Masse (Alu): {mass_al:.2f} g")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parametrischer STL-Generator")
    parser.add_argument("--length", type=float, default=80.0, help="Laenge X in mm (Standard: 80)")
    parser.add_argument("--width", type=float, default=50.0, help="Breite Y in mm (Standard: 50)")
    parser.add_argument("--height", type=float, default=12.0, help="Dicke Z in mm (Standard: 12)")
    parser.add_argument("--pocket", nargs=2, type=float, default=[30.0, 3.0], metavar=('DIA', 'DEPTH'), help="Kreistasche Durchmesser und Tiefe in mm")
    parser.add_argument("--hole-dia", type=float, default=6.0, help="Bohrungsdurchmesser in mm")
    parser.add_argument("--hole-margin", type=float, default=10.0, help="Randabstand der Bohrungen in mm")
    parser.add_argument("--output", type=str, default=r"c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\custom_test_part.stl", help="Zielpfad der STL-Datei")
    
    args = parser.parse_args()
    create_parametric_stl(
        length=args.length,
        width=args.width,
        height=args.height,
        pocket_dia=args.pocket[0],
        pocket_depth=args.pocket[1],
        hole_dia=args.hole_dia,
        hole_margin=args.hole_margin,
        output_path=args.output
    )
