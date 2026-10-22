# -*- coding: utf-8 -*-
"""
Automatisches 3D-Mess- und Analysewerkzeug fuer STL- und CAD-Modelle:
Ermittelt vollautomatisch alle kritischen Fertigungsmasse, Bounding Box,
Volumen, Oberflaeche und das Bauteilgewicht fuer verschiedene Werkstoffe.
"""

import sys
import os
import trimesh
import numpy as np

def measure_cad_model(stl_path, density_al=2.70, density_steel=7.85):
    """
    Misst ein 3D-STL-Modell geometrisch aus.
    Dichten in g/cm3: Aluminium ca. 2.70, Stahl ca. 7.85.
    """
    if not os.path.exists(stl_path):
        print(f"Fehler: Datei nicht gefunden: {stl_path}")
        return None

    mesh = trimesh.load(stl_path)
    bounds = mesh.bounds # [[xmin, ymin, zmin], [xmax, ymax, zmax]]
    extents = mesh.extents # [dx, dy, dz]

    volume_mm3 = mesh.volume if mesh.is_watertight else 0.0
    volume_cm3 = volume_mm3 / 1000.0
    area_mm2 = mesh.area
    area_cm2 = area_mm2 / 100.0

    mass_al_g = volume_cm3 * density_al
    mass_steel_g = volume_cm3 * density_steel

    report = {
        "file": os.path.basename(stl_path),
        "is_watertight": mesh.is_watertight,
        "length_x_mm": extents[0],
        "width_y_mm": extents[1],
        "height_z_mm": extents[2],
        "bounds_min": bounds[0].tolist(),
        "bounds_max": bounds[1].tolist(),
        "area_cm2": area_cm2,
        "volume_cm3": volume_cm3,
        "mass_al_g": mass_al_g,
        "mass_steel_g": mass_steel_g,
        "triangles": len(mesh.faces),
        "vertices": len(mesh.vertices)
    }

    print("=" * 65)
    print(f"  3D-CAD MASS- UND GEOMETRIEPROTOKOLL: {os.path.basename(stl_path)}")
    print("=" * 65)
    print(f"  Volumenkoerper wasserdicht (Watertight): {'JA (Gueltiges Solid)' if report['is_watertight'] else 'NEIN (Loecher vorhanden!)'}")
    print(f"  Dreiecke (Facets): {report['triangles']} | Eckpunkte (Vertices): {report['vertices']}")
    print("-" * 65)
    print(f"  AUSSENMASSE (Bounding Box):")
    print(f"    - Laenge X:  {report['length_x_mm']:8.2f} mm  (von X={report['bounds_min'][0]:.1f} bis X={report['bounds_max'][0]:.1f})")
    print(f"    - Breite Y:  {report['width_y_mm']:8.2f} mm  (von Y={report['bounds_min'][1]:.1f} bis Y={report['bounds_max'][1]:.1f})")
    print(f"    - Dicke Z:   {report['height_z_mm']:8.2f} mm  (von Z={report['bounds_min'][2]:.1f} bis Z={report['bounds_max'][2]:.1f})")
    print("-" * 65)
    print(f"  OBERFLAECHE & VOLUMEN:")
    print(f"    - Gesamte Oberflaeche: {report['area_cm2']:8.2f} cm2  ({area_mm2:.1f} mm2)")
    print(f"    - Reines Bauteilvolumen:{report['volume_cm3']:8.2f} cm3  ({volume_mm3:.1f} mm3)")
    print("-" * 65)
    print(f"  BERECHNETE BAUTEILMASSE (GEWICHT):")
    print(f"    - Aluminium EN AW-6082 (Dichte 2,70 g/cm3): {report['mass_al_g']:7.2f} g  ({report['mass_al_g']/1000.0:.3f} kg)")
    print(f"    - Baustahl S235JR       (Dichte 7,85 g/cm3): {report['mass_steel_g']:7.2f} g  ({report['mass_steel_g']/1000.0:.3f} kg)")
    print("=" * 65)

    return report

if __name__ == "__main__":
    default_stl = r"c:\Projekte\CNC\01_Kundenauftraege\test_auftrag_ubung_03\bauteil_1001.stl"
    path = sys.argv[1] if len(sys.argv) > 1 else default_stl
    measure_cad_model(path)
