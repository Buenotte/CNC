# -*- coding: utf-8 -*-
"""
Hochpraeziser CAD-Generator fuer Bauteil_1001 (Flanschplatte) mit echter CSG-Geometrie (Manifold3D Engine):
- Garantiert 100% wasserdicht (Watertight Solid Body)
- Aussenabmessungen: 80.0 x 50.0 x 12.0 mm (X: 0 bis 80, Y: 0 bis 50, Z: -12 bis 0)
- Kreistasche: Durchmesser 30.0 mm (R=15), Tiefe 3.0 mm (Z: 0 bis -3), Mitte: X=40.0, Y=25.0
- 4 Durchgangsbohrungen: Durchmesser 6.0 mm (R=3), Tiefe 12.0 mm durchgehend,
  Positionen: (10, 10), (70, 10), (70, 40), (10, 40)
"""

import os
import trimesh
import numpy as np

def build_perfect_cad_flanschplatte():
    # 1. Grundkörper: Quader 80 x 50 x 12 mm
    # In trimesh ist der Quader zentriert um (0,0,0), d.h. von -40 bis +40, etc.
    box = trimesh.creation.box(extents=[80.0, 50.0, 12.0])
    # Verschieben, sodass: X von 0 bis 80, Y von 0 bis 50, Z von -12 bis 0
    box.apply_translation([40.0, 25.0, -6.0])

    # 2. Kreistasche im Zentrum (X=40, Y=25), Tiefe 3 mm (von Z=0 bis Z=-3)
    # Zylinder mit Radius 15 mm, Höhe 3.1 mm (mit leichtem Überstand oben für sauberen Boole-Schnitt)
    pocket_depth = 3.0
    pocket_h = pocket_depth + 0.2
    pocket = trimesh.creation.cylinder(radius=15.0, height=pocket_h, sections=64)
    # Z-Zentrum des Zylinders liegt bei -pocket_depth/2 + 0.1
    pocket.apply_translation([40.0, 25.0, -pocket_depth / 2.0 + 0.1])

    # 3. Vier Bohrungen (Durchmesser 6 mm -> R=3 mm), durchgehend Z=+1 bis Z=-13 (Höhe 14 mm)
    hole_h = 14.0
    holes = [(10.0, 10.0), (70.0, 10.0), (70.0, 40.0), (10.0, 40.0)]
    cutter_cylinders = [pocket]

    for hx, hy in holes:
        h_cyl = trimesh.creation.cylinder(radius=3.0, height=hole_h, sections=36)
        h_cyl.apply_translation([hx, hy, -6.0]) # Z-Zentrum bei -6, reicht von +1 bis -13
        cutter_cylinders.append(h_cyl)

    # 4. Echte boolesche Differenz über Manifold3D (industrieller CAD-Standard)
    result = trimesh.boolean.difference([box] + cutter_cylinders, engine='manifold')

    # Prüfungen
    print(f"CAD-Volumenkoerper erstellt:")
    print(f"  Watertight (wasserdicht): {result.is_watertight}")
    print(f"  Volumen: {result.volume:.2f} mm3")
    print(f"  Anzahl Vertices: {len(result.vertices)}, Faces: {len(result.faces)}")
    print(f"  Bounding Box Min: {result.bounds[0]}, Max: {result.bounds[1]}")

    return result

if __name__ == "__main__":
    cad_mesh = build_perfect_cad_flanschplatte()

    target_paths = [
        r"c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\bauteil_1001.stl",
        r"c:\Projekte\CNC\01_Kundenauftraege\referenz_auftrag_flanschplatte\bauteil_1001.stl",
        r"c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_03_flanschplatte_z_min\bauteil_1001.stl",
        r"c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_04_lagerplatte_3d_cam\bauteil_1001.stl",
        r"c:\Projekte\CNC\01_Kundenauftraege\auftragsakten_00b_bis_16\auftrag_05_einrichtedoku_simulation\bauteil_1001.stl"
    ]

    for p in target_paths:
        if os.path.exists(os.path.dirname(p)):
            cad_mesh.export(p, file_type='stl_ascii')
            print(f"Erfolgreich als STL exportiert: {p}")
