"""
3D-CAD CNC-Simulations-Video-Generator
=============================================================================
Rendert die vollständige 3D-Simulation von Übung 3 (Flanschplatte OP10)
Frame für Frame und erzeugt per FFmpeg direkt ein hochauflösendes MP4-Video:
docs/videos/uebung_03_simulation_video.mp4
=============================================================================
"""

import sys
import os
import math
import subprocess
from PIL import Image, ImageDraw, ImageFont

def render_video():
    width = 1280
    height = 720
    fps = 30
    out_dir = "docs/videos"
    os.makedirs(out_dir, exist_ok=True)
    out_mp4 = os.path.join(out_dir, "uebung_03_simulation_video.mp4")

    # FFmpeg Subprozess starten (Piped raw RGB24)
    ffmpeg_cmd = [
        "ffmpeg", "-y",
        "-f", "rawvideo",
        "-vcodec", "rawvideo",
        "-s", f"{width}x{height}",
        "-pix_fmt", "rgb24",
        "-r", str(fps),
        "-i", "-",
        "-c:v", "libx264",
        "-preset", "fast",
        "-crf", "22",
        "-pix_fmt", "yuv420p",
        out_mp4
    ]

    try:
        proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Fehler beim Starten von FFmpeg: {e}")
        return

    # Schriftarten laden
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 22)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 14)
        font_hud = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 16)
        font_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
        font_badge = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 13)
    except:
        font_title = font_sub = font_hud = font_small = font_badge = ImageFont.load_default()

    # 3D Projektions-Parameter (Isometrische CAD-Kamera)
    # Bauteilzentrum ist bei X=40, Y=25, Z=0
    cam_rot_x = 0.85
    cam_rot_z = -0.65
    scale = 5.2
    center_screen_x = width // 2 - 40
    center_screen_y = height // 2 + 30

    def project_3d(x, y, z):
        # Verschiebung zum Modellzentrum
        dx = x - 40.0
        dy = y - 25.0
        dz = z - (-6.0)

        # Z-Rotation
        cos_z = math.cos(cam_rot_z)
        sin_z = math.sin(cam_rot_z)
        x1 = dx * cos_z - dy * sin_z
        y1 = dx * sin_z + dy * cos_z
        z1 = dz

        # X-Rotation (Kippung)
        cos_x = math.cos(cam_rot_x)
        sin_x = math.sin(cam_rot_x)
        y2 = y1 * cos_x - z1 * sin_x
        z2 = y1 * sin_x + z1 * cos_x

        # Bildschirm-Koordinaten
        sx = center_screen_x + x1 * scale
        sy = center_screen_y - z2 * scale
        return (sx, sy, y2)

    # Waypoints der Fräsbewegungen (Übung 3)
    # Jedes Waypoint hat: x, y, z, feed, type (rapid/linear/circle/peck), op, tool, comment
    waypoints = []
    
    # OP1: Außenkontur Schaftfräser 10mm
    waypoints.append({"x": -10.0, "y": -10.0, "z": 25.0, "f": 0, "type": "rapid", "op": "1. AUSSENKONTUR FRAESEN", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Eilgang Anfahrt"})
    waypoints.append({"x": -10.0, "y": -10.0, "z": 2.0, "f": 0, "type": "rapid", "op": "1. AUSSENKONTUR FRAESEN", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Sicherheitsebene Z+2"})
    waypoints.append({"x": -10.0, "y": -10.0, "z": -5.0, "f": 500, "type": "linear", "op": "1. AUSSENKONTUR FRAESEN", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Senkrecht abtauchen auf Z-5"})
    waypoints.append({"x": 0.0, "y": 0.0, "z": -5.0, "f": 1200, "type": "linear", "op": "1. AUSSENKONTUR FRAESEN", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Lead-In Schnittanfahrt ins Rohteil"})
    waypoints.append({"x": 80.0, "y": 0.0, "z": -5.0, "f": 1200, "type": "linear", "op": "1. AUSSENKONTUR FRAESEN", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Vorderkante X80 fräsen"})
    waypoints.append({"x": 80.0, "y": 50.0, "z": -5.0, "f": 1200, "type": "linear", "op": "1. AUSSENKONTUR FRAESEN", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Rechte Kante Y50 fräsen"})
    waypoints.append({"x": 0.0, "y": 50.0, "z": -5.0, "f": 1200, "type": "linear", "op": "1. AUSSENKONTUR FRAESEN", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Hinterkante X0 fräsen"})
    waypoints.append({"x": 0.0, "y": 0.0, "z": -5.0, "f": 1200, "type": "linear", "op": "1. AUSSENKONTUR FRAESEN", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Linke Kante Y0 schließen"})
    waypoints.append({"x": 0.0, "y": 0.0, "z": 15.0, "f": 0, "type": "rapid", "op": "1. AUSSENKONTUR FRAESEN", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Rückzug auf Z+15"})

    # OP2: Kreistasche Mitte
    waypoints.append({"x": 40.0, "y": 25.0, "z": 15.0, "f": 0, "type": "rapid", "op": "2. KREISTASCHE MITTE Ø30", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Positionierung Taschenzentrum"})
    waypoints.append({"x": 40.0, "y": 25.0, "z": 2.0, "f": 0, "type": "rapid", "op": "2. KREISTASCHE MITTE Ø30", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Eilgang Z+2"})
    waypoints.append({"x": 40.0, "y": 25.0, "z": -3.0, "f": 400, "type": "linear", "op": "2. KREISTASCHE MITTE Ø30", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Tauchvorschub auf Z-3"})
    waypoints.append({"x": 55.0, "y": 25.0, "z": -3.0, "f": 1000, "type": "linear", "op": "2. KREISTASCHE MITTE Ø30", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Auf Taschenradius R15 fahren"})
    # Kreis interpolieren (16 Schritte)
    for a in range(0, 361, 24):
        rad = math.radians(a)
        cx = 40.0 + 15.0 * math.cos(rad)
        cy = 25.0 + 15.0 * math.sin(rad)
        waypoints.append({"x": cx, "y": cy, "z": -3.0, "f": 1000, "type": "linear", "op": "2. KREISTASCHE MITTE Ø30", "tool": "T01 (Schaftfräser Ø10mm)", "desc": f"G03 Kreisbahn {a}°"})
    waypoints.append({"x": 40.0, "y": 25.0, "z": -3.0, "f": 1000, "type": "linear", "op": "2. KREISTASCHE MITTE Ø30", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Zurück zum Zentrum"})
    waypoints.append({"x": 40.0, "y": 25.0, "z": 15.0, "f": 0, "type": "rapid", "op": "2. KREISTASCHE MITTE Ø30", "tool": "T01 (Schaftfräser Ø10mm)", "desc": "Rückzug Z+15"})

    # OP3: 4 Befestigungsbohrungen Tiefbohren G83
    holes = [(10.0, 10.0), (70.0, 10.0), (70.0, 40.0), (10.0, 40.0)]
    for i, (hx, hy) in enumerate(holes, 1):
        waypoints.append({"x": hx, "y": hy, "z": 15.0, "f": 0, "type": "rapid", "op": f"3. BOHRUNGEN G83 (Loch {i}/4)", "tool": "T02 (Spiralbohrer Ø6mm)", "desc": f"Anfahrt Bohrung {i}"})
        waypoints.append({"x": hx, "y": hy, "z": 2.0, "f": 0, "type": "rapid", "op": f"3. BOHRUNGEN G83 (Loch {i}/4)", "tool": "T02 (Spiralbohrer Ø6mm)", "desc": "Rüstebene Z+2"})
        # 4 Stufen Tiefbohren (Pecks)
        for depth in [-3.0, -6.0, -9.0, -12.0]:
            waypoints.append({"x": hx, "y": hy, "z": depth, "f": 300, "type": "linear", "op": f"3. BOHRUNGEN G83 (Loch {i}/4)", "tool": "T02 (Spiralbohrer Ø6mm)", "desc": f"Spanbruch Z{depth} mm"})
            if depth > -12.0:
                waypoints.append({"x": hx, "y": hy, "z": 2.0, "f": 0, "type": "rapid", "op": f"3. BOHRUNGEN G83 (Loch {i}/4)", "tool": "T02 (Spiralbohrer Ø6mm)", "desc": "Spanabfuhr Entlastung"})
        waypoints.append({"x": hx, "y": hy, "z": 15.0, "f": 0, "type": "rapid", "op": f"3. BOHRUNGEN G83 (Loch {i}/4)", "tool": "T02 (Spiralbohrer Ø6mm)", "desc": "Rückzug nach Bohrzyklus"})

    # Programmende
    waypoints.append({"x": 10.0, "y": 40.0, "z": 30.0, "f": 0, "type": "rapid", "op": "PROGRAMMENDE", "tool": "T02 (Spiralbohrer Ø6mm)", "desc": "G53 Z0.0 Spindel Decke"})

    total_frames = 450 # ca. 15 Sekunden bei 30 fps
    pts_len = len(waypoints)

    print(f"Starte Video-Rendering: {total_frames} Frames bei 30 FPS...")

    # Vorberechnen der Spur-Linien
    history_lines = []

    for frame_idx in range(total_frames):
        # Aktueller Animationsschritt entlang der Waypoints
        progress = frame_idx / float(total_frames - 1)
        curr_pt_idx = int(progress * (pts_len - 1))
        curr_wp = waypoints[curr_pt_idx]

        # Interpolation zwischen curr_wp und nächstem Waypoint
        sub_progress = (progress * (pts_len - 1)) - curr_pt_idx
        if curr_pt_idx < pts_len - 1:
            next_wp = waypoints[curr_pt_idx + 1]
            cur_x = curr_wp["x"] + (next_wp["x"] - curr_wp["x"]) * sub_progress
            cur_y = curr_wp["y"] + (next_wp["y"] - curr_wp["y"]) * sub_progress
            cur_z = curr_wp["z"] + (next_wp["z"] - curr_wp["z"]) * sub_progress
        else:
            cur_x, cur_y, cur_z = curr_wp["x"], curr_wp["y"], curr_wp["z"]

        # Historie der gefahrenen Fräsbahnen
        if frame_idx > 0:
            last_x, last_y, last_z, l_type = history_lines[-1] if history_lines else (cur_x, cur_y, cur_z, curr_wp["type"])
            history_lines.append((cur_x, cur_y, cur_z, curr_wp["type"]))
        else:
            history_lines.append((cur_x, cur_y, cur_z, curr_wp["type"]))

        # Erstelle Frame Bild
        img = Image.new("RGB", (width, height), (15, 20, 28))
        draw = ImageDraw.Draw(img)

        # 1. Raster auf Maschinentisch (Z = -20 mm)
        for gx in range(-20, 101, 20):
            p1 = project_3d(gx, -20, -18)
            p2 = project_3d(gx, 70, -18)
            draw.line([(p1[0], p1[1]), (p2[0], p2[1])], fill=(28, 38, 52), width=1)
        for gy in range(-20, 71, 20):
            p1 = project_3d(-20, gy, -18)
            p2 = project_3d(100, gy, -18)
            draw.line([(p1[0], p1[1]), (p2[0], p2[1])], fill=(28, 38, 52), width=1)

        # 2. Schraubstock-Backen (Stahl gehärtet, Z = -15 bis -18 mm)
        # Vordere Backe
        b1_pts = [project_3d(-10, -15, -15), project_3d(90, -15, -15), project_3d(90, -2, -15), project_3d(-10, -2, -15)]
        draw.polygon([(p[0], p[1]) for p in b1_pts], fill=(45, 55, 70), outline=(80, 95, 115))
        # Hintere Backe
        b2_pts = [project_3d(-10, 52, -15), project_3d(90, 52, -15), project_3d(90, 65, -15), project_3d(-10, 65, -15)]
        draw.polygon([(p[0], p[1]) for p in b2_pts], fill=(45, 55, 70), outline=(80, 95, 115))

        # 3. Rohteil / Werkstück (80 x 50 mm, Z=0 bis Z=-12)
        # Unterseite Z = -12
        w_bot = [project_3d(0, 0, -12), project_3d(80, 0, -12), project_3d(80, 50, -12), project_3d(0, 50, -12)]
        draw.polygon([(p[0], p[1]) for p in w_bot], fill=(30, 42, 58), outline=(60, 80, 105), width=2)
        # Seitenwände
        for i in range(4):
            ni = (i + 1) % 4
            p_top1 = project_3d([0, 80, 80, 0][i], [0, 0, 50, 50][i], 0)
            p_top2 = project_3d([0, 80, 80, 0][ni], [0, 0, 50, 50][ni], 0)
            p_bot2 = project_3d([0, 80, 80, 0][ni], [0, 0, 50, 50][ni], -12)
            p_bot1 = project_3d([0, 80, 80, 0][i], [0, 0, 50, 50][i], -12)
            draw.polygon([(p_top1[0], p_top1[1]), (p_top2[0], p_top2[1]), (p_bot2[0], p_bot2[1]), (p_bot1[0], p_bot1[1])],
                         fill=(35, 52, 75), outline=(70, 95, 125))
        # Oberseite Z = 0
        w_top = [project_3d(0, 0, 0), project_3d(80, 0, 0), project_3d(80, 50, 0), project_3d(0, 50, 0)]
        draw.polygon([(p[0], p[1]) for p in w_top], fill=(45, 68, 98), outline=(100, 140, 185), width=2)

        # Kreistasche auf Oberseite
        circ_pts = []
        for a in range(0, 360, 15):
            rad = math.radians(a)
            circ_pts.append(project_3d(40.0 + 15.0 * math.cos(rad), 25.0 + 15.0 * math.sin(rad), 0))
        draw.polygon([(p[0], p[1]) for p in circ_pts], fill=(30, 48, 70), outline=(56, 189, 248), width=1)

        # 4 Bohrungen
        for hx, hy in [(10, 10), (70, 10), (70, 40), (10, 40)]:
            hp = project_3d(hx, hy, 0)
            draw.ellipse([(hp[0] - 6, hp[1] - 4), (hp[0] + 6, hp[1] + 4)], fill=(20, 25, 35), outline=(147, 197, 253))

        # 4. Koordinatenursprung G54 (Vorne links oben)
        g54_p = project_3d(0, 0, 0)
        draw.ellipse([(g54_p[0] - 5, g54_p[1] - 5), (g54_p[0] + 5, g54_p[1] + 5)], fill=(255, 255, 255))
        px = project_3d(20, 0, 0)
        draw.line([(g54_p[0], g54_p[1]), (px[0], px[1])], fill=(239, 68, 68), width=2) # X+ rot
        py = project_3d(0, 20, 0)
        draw.line([(g54_p[0], g54_p[1]), (py[0], py[1])], fill=(34, 197, 94), width=2) # Y+ grün
        pz = project_3d(0, 0, 20)
        draw.line([(g54_p[0], g54_p[1]), (pz[0], pz[1])], fill=(56, 189, 248), width=2) # Z+ blau
        draw.text((g54_p[0] - 55, g54_p[1] + 6), "G54 (0,0,0)", font=font_small, fill=(255, 255, 255))

        # 5. Gezeichnete Fräsbahnen (Trace / Werkzeugspur)
        for i in range(1, len(history_lines), 2):
            p_prev = project_3d(history_lines[i - 1][0], history_lines[i - 1][1], history_lines[i - 1][2])
            p_now = project_3d(history_lines[i][0], history_lines[i][1], history_lines[i][2])
            mtype = history_lines[i][3]
            line_color = (250, 204, 21) if mtype == "rapid" else (14, 165, 233)
            draw.line([(p_prev[0], p_prev[1]), (p_now[0], p_now[1])], fill=line_color, width=2 if mtype == "rapid" else 3)

        # 6. Werkzeug (Fräser / Bohrer) an aktueller Position
        tp_tip = project_3d(cur_x, cur_y, cur_z)
        tp_shaft = project_3d(cur_x, cur_y, cur_z + 25.0)
        tp_holder = project_3d(cur_x, cur_y, cur_z + 45.0)

        # Werkzeugschaft (Silber/Gold)
        tool_color = (234, 179, 8) if "T01" in curr_wp["tool"] else (168, 85, 247)
        draw.line([(tp_tip[0], tp_tip[1]), (tp_shaft[0], tp_shaft[1])], fill=tool_color, width=7)
        # Werkzeug-Spitze
        draw.ellipse([(tp_tip[0] - 5, tp_tip[1] - 5), (tp_tip[0] + 5, tp_tip[1] + 5)], fill=(255, 255, 255), outline=tool_color, width=2)
        # Werkzeugaufnahme / Spannfutter
        draw.line([(tp_shaft[0], tp_shaft[1]), (tp_holder[0], tp_holder[1])], fill=(148, 163, 184), width=15)

        # Kollisionswarnung / Z-Status Badge am Werkzeug
        if cur_z <= -15.0:
            draw.text((tp_tip[0] + 12, tp_tip[1] - 10), "🚨 CRASH!", font=font_badge, fill=(239, 68, 68))
        elif cur_z < -12.0:
            draw.text((tp_tip[0] + 12, tp_tip[1] - 10), "⚠️ DURCHBRUCH", font=font_badge, fill=(245, 158, 11))

        # ==================== HUD OVERLAYS ====================
        # Header Balken oben
        draw.rectangle([(0, 0), (width, 65)], fill=(11, 15, 23))
        draw.line([(0, 65), (width, 65)], fill=(30, 41, 59), width=1)
        draw.text((25, 12), "CNC 3D-FERTIGUNGS-SIMULATION & SICHERHEITS-PRÜFUNG", font=font_title, fill=(255, 255, 255))
        draw.text((25, 38), "Kundenbauteil: Flanschplatte 80 x 50 x 12 mm | Steuerung: Haas / ISO G-Code", font=font_sub, fill=(148, 163, 184))

        # Rechts oben: Z-MIN Schutz Status
        draw.rounded_rectangle([(width - 320, 12), (width - 20, 52)], radius=6, fill=(16, 42, 66), outline=(56, 189, 248), width=1)
        draw.text((width - 305, 18), "🛡️ CRASHSCHUTZ Z-MIN: -12.000 MM", font=font_badge, fill=(56, 189, 248))
        draw.text((width - 305, 33), "Spannbacken bei Z = -15.0 mm -> SICHER!", font=font_small, fill=(147, 197, 253))

        # Live Koordinaten-Panel (Links unten)
        draw.rounded_rectangle([(25, height - 170), (320, height - 25)], radius=10, fill=(11, 15, 23, 220), outline=(45, 55, 75), width=1)
        draw.text((40, height - 158), "LIVE-MASCHINENDATEN:", font=font_badge, fill=(148, 163, 184))
        draw.text((40, height - 135), f"X: {cur_x:+7.3f} mm", font=font_hud, fill=(255, 255, 255))
        draw.text((40, height - 115), f"Y: {cur_y:+7.3f} mm", font=font_hud, fill=(255, 255, 255))
        z_col = (239, 68, 68) if cur_z <= -15 else ((245, 158, 11) if cur_z < -12 else (56, 189, 248))
        draw.text((40, height - 95), f"Z: {cur_z:+7.3f} mm", font=font_hud, fill=z_col)
        draw.text((40, height - 70), f"Vorschub: F{curr_wp['f']:4d} mm/min", font=font_small, fill=(203, 213, 225))
        draw.text((40, height - 50), f"Werkzeug: {curr_wp['tool'][:20]}", font=font_small, fill=(203, 213, 225))

        # Operations-Panel (Mitte unten)
        draw.rounded_rectangle([(340, height - 100), (width - 25, height - 25)], radius=10, fill=(11, 15, 23, 220), outline=(45, 55, 75), width=1)
        draw.text((360, height - 90), f"AKTUELLE OPERATION: {curr_wp['op']}", font=font_title, fill=(56, 189, 248))
        draw.text((360, height - 62), f"Aktion: {curr_wp['desc']}", font=font_sub, fill=(241, 245, 249))

        # Fortschrittsbalken ganz unten
        bar_w = width - 50
        draw.rectangle([(25, height - 12), (25 + bar_w, height - 6)], fill=(30, 41, 59))
        draw.rectangle([(25, height - 12), (25 + int(bar_w * progress), height - 6)], fill=(56, 189, 248))

        # Frame in Pipe an FFmpeg schreiben
        try:
            proc.stdin.write(img.tobytes())
        except Exception as err:
            print(f"Fehler beim Schreiben von Frame {frame_idx}: {err}")
            break

    proc.stdin.close()
    proc.wait()
    print(f"[OK] Video erfolgreich fertiggestellt: {out_mp4}")

if __name__ == "__main__":
    render_video()
