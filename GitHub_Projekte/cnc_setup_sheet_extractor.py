#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CNC Setup Sheet & Tool List Extractor (Heidenhain Klartext .H & Siemens Sinumerik .MPF)
=======================================================================================
Dieses Skript analysiert bestehende NC-Programme (Heidenhain Klartext oder Siemens Sinumerik),
extrahiert automatisch:
  1. Programmname und Steuerungstyp
  2. Rohteilabmessungen (aus BLK FORM oder WORKPIECE)
  3. Alle aufgerufenen Werkzeuge (TOOL CALL / T="...") inkl. Drehzahl (S), Vorschub (F) und Kühlung (M7/M8)
  4. Die tiefste Z-Zustellung (Z_min) pro Werkzeug sowie die empfohlene Mindest-Auskraglänge (L_min)
und generiert daraus ein übersichtliches Einrichteblatt (Setup Sheet) als Markdown-Datei.
"""

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Tuple


@dataclass
class ToolOperation:
    """Repräsentiert einen einzelnen Werkzeugaufruf innerhalb des NC-Programms."""
    tool_id: str
    comment: str = "-"
    spindle_rpm: int = 0
    feedrate: int = 0
    min_z: float = 0.0
    coolant: str = "Trocken / Luft"


@dataclass
class NCProgramSummary:
    """Zusammenfassung aller extrahierten Daten eines NC-Programms."""
    program_name: str
    control_type: str
    stock_min: Optional[Tuple[float, float, float]] = None
    stock_max: Optional[Tuple[float, float, float]] = None
    preset_number: str = "Standard (G54 / Preset 1)"
    operations: List[ToolOperation] = field(default_factory=list)


def parse_nc_program(content: str, filename: str) -> NCProgramSummary:
    """Analysiert den Textinhalt eines Heidenhain- oder Siemens-NC-Programms."""
    lines = [line.strip() for line in content.splitlines() if line.strip()]

    # Steuerungstyp erkennen (Heidenhain BEGIN PGM vs. Siemens DIN/ISO)
    is_heidenhain = any("BEGIN PGM" in line or "TOOL CALL" in line for line in lines)
    control_type = "Heidenhain Klartext (TNC)" if is_heidenhain else "Siemens Sinumerik (DIN/ISO)"
    program_name = filename

    summary = NCProgramSummary(program_name=program_name, control_type=control_type)

    # Heidenhain Programmname aus 'BEGIN PGM <NAME> MM'
    for line in lines:
        m_pgm = re.search(r"BEGIN\s+PGM\s+([^\s]+)", line)
        if m_pgm:
            summary.program_name = m_pgm.group(1)
            break

    # Rohteil (BLK FORM 0.1 / 0.2 bei Heidenhain)
    blk_min, blk_max = None, None
    for line in lines:
        m_b1 = re.search(
            r"BLK\s+FORM\s+0\.1\s+[XYZ]\s+X([+-]?\d+(?:\.\d+)?)\s+Y([+-]?\d+(?:\.\d+)?)\s+Z([+-]?\d+(?:\.\d+)?)",
            line,
        )
        if m_b1:
            blk_min = (float(m_b1.group(1)), float(m_b1.group(2)), float(m_b1.group(3)))
        m_b2 = re.search(
            r"BLK\s+FORM\s+0\.2\s+X([+-]?\d+(?:\.\d+)?)\s+Y([+-]?\d+(?:\.\d+)?)\s+Z([+-]?\d+(?:\.\d+)?)",
            line,
        )
        if m_b2:
            blk_max = (float(m_b2.group(1)), float(m_b2.group(2)), float(m_b2.group(3)))

    if blk_min and blk_max:
        summary.stock_min = blk_min
        summary.stock_max = blk_max

    # Werkzeuge, Schnittdaten und minimale Z-Höhen extrahieren
    current_op: Optional[ToolOperation] = None

    for line in lines:
        # 1. Heidenhain TOOL CALL erkennen
        m_tc = re.search(r"TOOL\s+CALL\s+([^\s]+)\s+[XYZ]\s+S(\d+)(?:\s+F(\d+))?(?:\s*;\s*(.*))?", line)
        if m_tc:
            if current_op:
                summary.operations.append(current_op)
            t_id = f"T{m_tc.group(1)}"
            rpm = int(m_tc.group(2))
            feed = int(m_tc.group(3)) if m_tc.group(3) else 0
            comment = m_tc.group(4).strip() if m_tc.group(4) else "Standardwerkzeug"
            current_op = ToolOperation(tool_id=t_id, comment=comment, spindle_rpm=rpm, feedrate=feed)
            continue

        # 2. Siemens T="..." erkennen
        m_siemens_t = re.search(r'T="([^"]+)"', line)
        if m_siemens_t:
            if current_op:
                summary.operations.append(current_op)
            current_op = ToolOperation(
                tool_id=m_siemens_t.group(1),
                comment="Siemens Schwesterwerkzeug / Katalogname",
            )
            continue

        # Falls ein Werkzeug aktiv ist: Drehzahl, Vorschub, Kühlmittel und Z-Tiefe verfolgen
        if current_op:
            # Siemens Drehzahl S... M3
            m_s = re.search(r"\bS(\d+)\b", line)
            if m_s and current_op.spindle_rpm == 0:
                current_op.spindle_rpm = int(m_s.group(1))

            # Vorschub F... (ohne FMAX)
            m_f = re.search(r"\bF(\d+(?:\.\d+)?)\b", line)
            if m_f and current_op.feedrate == 0:
                current_op.feedrate = int(float(m_f.group(1)))

            # Kühlmittel M7 (IKZ) oder M8 (Außenkühlung)
            if re.search(r"\bM7\b", line):
                current_op.coolant = "Innenkühlung (IKZ / M7)"
            elif re.search(r"\bM8\b", line) and "IKZ" not in current_op.coolant:
                current_op.coolant = "Außenkühlung (M8)"

            # Tiefste Z-Koordinate oder Bohrtiefe Q201
            m_z = re.search(r"\bZ([+-]?\d+(?:\.\d+)?)\b", line)
            if m_z and "M91" not in line and "SUPA" not in line:
                z_val = float(m_z.group(1))
                if z_val < current_op.min_z:
                    current_op.min_z = z_val

            m_q201 = re.search(r"Q201=([+-]?\d+(?:\.\d+)?)", line)
            if m_q201:
                q_depth = float(m_q201.group(1))
                if q_depth < current_op.min_z:
                    current_op.min_z = q_depth

    if current_op:
        summary.operations.append(current_op)

    return summary


def generate_markdown_setup_sheet(summary: NCProgramSummary) -> str:
    """Erzeugt aus der Programmanalyse ein formatiertes Markdown-Einrichteblatt."""
    out = [
        f"# Automatisch generiertes CNC-Einrichteblatt: `{summary.program_name}`",
        "",
        f"* **Steuerungssystem:** {summary.control_type}",
        f"* **Bezugspunkt / Nullpunkt:** {summary.preset_number}",
    ]

    if summary.stock_min and summary.stock_max:
        dx = abs(summary.stock_max[0] - summary.stock_min[0])
        dy = abs(summary.stock_max[1] - summary.stock_min[1])
        dz = abs(summary.stock_max[2] - summary.stock_min[2])
        out.append(
            f"* **Rohteilabmessungen (aus BLK FORM):** `{dx:.1f} x {dy:.1f} x {dz:.1f} mm` "
            f"(X: {summary.stock_min[0]} bis {summary.stock_max[0]}, "
            f"Y: {summary.stock_min[1]} bis {summary.stock_max[1]}, "
            f"Z: {summary.stock_min[2]} bis {summary.stock_max[2]})"
        )

    out.extend([
        "",
        "## Extrahierte Werkzeug- und Operationsliste",
        "",
        "| Schritt | Werkzeug | Beschreibung / Kommentar | Drehzahl $n$ [U/min] | Vorschub $v_f$ [mm/min] | Tiefste Zustellung $Z_{\\text{min}}$ [mm] | Empf. Auskraglänge $L_{\\text{min}}$ (+5 mm Sicherheit) | Kühlung |",
        "| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :--- |",
    ])

    for idx, op in enumerate(summary.operations, start=1):
        rec_overhang = abs(op.min_z) + 5.0 if op.min_z < 0 else 25.0
        out.append(
            f"| **{idx * 10}** | `{op.tool_id}` | {op.comment} | {op.spindle_rpm} | "
            f"{op.feedrate} | {op.min_z:.2f} | **{rec_overhang:.1f} mm** | {op.coolant} |"
        )

    out.extend([
        "",
        "> **Sicherheitshinweis:** Automatisch durch `cnc_setup_sheet_extractor.py` erzeugte Dokumentation. "
        "Alle Mindest-Auskraglängen ($L_{\\text{min}}$) vor dem Programmstart am Voreinstellgerät prüfen!",
        "",
    ])
    return "\n".join(out)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extrahiert automatisch ein CNC-Einrichteblatt aus Heidenhain (.H) oder Siemens (.MPF) Programmen."
    )
    parser.add_argument("input_file", type=Path, help="Pfad zur NC-Programmdatei (.H oder .MPF)")
    parser.add_argument(
        "-o", "--output", type=Path, default=None, help="Optionaler Ausgabepfad für die Markdown-Datei (.md)"
    )
    args = parser.parse_args()

    content = args.input_file.read_text(encoding="utf-8", errors="ignore")
    summary = parse_nc_program(content, args.input_file.name)
    md_report = generate_markdown_setup_sheet(summary)

    if args.output:
        args.output.write_text(md_report, encoding="utf-8")
        print(f"Einrichteblatt erfolgreich gespeichert unter: {args.output}")
    else:
        print(md_report)


if __name__ == "__main__":
    main()
