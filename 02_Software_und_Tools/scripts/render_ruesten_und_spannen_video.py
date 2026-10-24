# -*- coding: utf-8 -*-
"""
Lehrvideo-Generator: Richtiges Rüsten, Spannen & G54-Nullpunktaufnahme
=============================================================================
Rendert ein didaktisches 3D-CAD-Lehrvideo für Zerspanungsmechaniker.
Zeigt Schritt für Schritt:
1. Schraubstock reinigen (Spänefalle verhindern)
2. Parallelleisten einlegen (h = 32 mm)
3. Rohteil einlegen (85x55x15 mm)
4. Festspannen (80 Nm) & Schonhammer-Setzschlag
5. Die Wackel-Probe (Fingerkontrolle der Parallelunterlagen)
6. 3D-Kantentaster Antasten & G54 Nullpunktaufnahme (+5 mm Radiusverrechnung)
7. Kollisionsprüfung & Freigabe für Luftschnitt / Einzelsatz
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
    
    out_dir = r"C:\Projekte\CNC\03_Fachdokumentation_und_Wissen\docs\videos"
    os.makedirs(out_dir, exist_ok=True)
    out_mp4 = os.path.join(out_dir, "zerspanungsmechaniker_ruest_und_spann_anleitung.mp4")

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
        "-crf", "20",
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
        font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 15)
        font_hud = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 16)
        font_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
        font_badge = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 14)
        font_big_step = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 28)
    except:
        font_title = font_sub = font_hud = font_small = font_badge = font_big_step = ImageFont.load_default()

    # 3D Projektions-Parameter (Isometrische CAD-Kamera)
    # Zentrum Bauteil: X=40, Y=25, Z=0
    cam_rot_x = 0.85
    cam_rot_z = -0.65
    scale = 5.2
    center_screen_x = width // 2 - 40
    center_screen_y = height // 2 + 35

    def project_3d(x, y, z):
        dx = x - 40.0
        dy = y - 25.0
        dz = z - (-6.0)

        cos_z = math.cos(cam_rot_z)
        sin_z = math.sin(cam_rot_z)
        x1 = dx * cos_z - dy * sin_z
        y1 = dx * sin_z + dy * cos_z
        z1 = dz

        cos_x = math.cos(cam_rot_x)
        sin_x = math.sin(cam_rot_x)
        y2 = y1 * cos_x - z1 * sin_x
        z2 = y1 * sin_x + z1 * cos_x

        sx = center_screen_x + x1 * scale
        sy = center_screen_y - z2 * scale
        return (sx, sy, y2)

    total_frames = 720  # 24 Sekunden bei 30 fps
    print(f"Starte Rendering von {total_frames} Frames...")

    # Phasen-Einteilung:
    # Phase 0: Intro & Schraubstock bereitstellen (0 - 80)
    # Phase 1: Reinigung & Ausblasen (81 - 170)
    # Phase 2: Parallelunterlagen einlegen (171 - 270)
    # Phase 3: Rohteil einlegen (271 - 380)
    # Phase 4: Schraubstock spannen & Schonhammer-Schlag (381 - 480)
    # Phase 5: Wackel-Probe der Parallelleisten (481 - 580)
    # Phase 6: 3D-Kantentaster & G54 Nullpunktaufnahme (581 - 680)
    # Phase 7: Finale Abnahme & Luftschnitt-Freigabe (681 - 720)

    for frame_idx in range(total_frames):
        img = Image.new("RGB", (width, height), (15, 20, 28))
        draw = ImageDraw.Draw(img)

        # 1. Raster Maschinentisch (Z = -22 mm)
        for gx in range(-30, 111, 20):
            p1 = project_3d(gx, -30, -22)
            p2 = project_3d(gx, 80, -22)
            draw.line([(p1[0], p1[1]), (p2[0], p2[1])], fill=(26, 36, 50), width=1)
        for gy in range(-30, 81, 20):
            p1 = project_3d(-30, gy, -22)
            p2 = project_3d(110, gy, -22)
            draw.line([(p1[0], p1[1]), (p2[0], p2[1])], fill=(26, 36, 50), width=1)

        # Schraubstock-Grundkörper (Boden auf Z = -22 bis -15 mm)
        base_pts = [project_3d(-15, -20, -22), project_3d(95, -20, -22), project_3d(95, 70, -22), project_3d(-15, 70, -22)]
        draw.polygon([(p[0], p[1]) for p in base_pts], fill=(30, 40, 52), outline=(60, 75, 95))

        # Dynamische Position der beweglichen Backe (in Y)
        # Wenn gespannt (ab Frame 381): clamp_offset = 0 (an Y = -2 mm)
        # Wenn offen (Frame 0 - 380): clamp_offset = -12 mm
        if frame_idx < 380:
            clamp_y = -14.0
        elif frame_idx < 420:
            prog = (frame_idx - 380) / 40.0
            clamp_y = -14.0 + 12.0 * prog
        else:
            clamp_y = -2.0

        # Feste Backe hinten (Y = 52 bis 68, Z = -22 bis -12 mm)
        back_top = [project_3d(-12, 52, -12), project_3d(92, 52, -12), project_3d(92, 68, -12), project_3d(-12, 68, -12)]
        draw.polygon([(p[0], p[1]) for p in back_top], fill=(50, 62, 78), outline=(90, 110, 135), width=2)
        back_front = [project_3d(-12, 52, -22), project_3d(92, 52, -22), project_3d(92, 52, -12), project_3d(-12, 52, -12)]
        draw.polygon([(p[0], p[1]) for p in back_front], fill=(65, 80, 100), outline=(90, 110, 135))

        # Bewegliche Backe vorne (Y = clamp_y - 14 bis clamp_y, Z = -22 bis -12 mm)
        front_top = [project_3d(-12, clamp_y - 14, -12), project_3d(92, clamp_y - 14, -12), project_3d(92, clamp_y, -12), project_3d(-12, clamp_y, -12)]
        draw.polygon([(p[0], p[1]) for p in front_top], fill=(50, 62, 78), outline=(90, 110, 135), width=2)
        front_back = [project_3d(-12, clamp_y, -22), project_3d(92, clamp_y, -22), project_3d(92, clamp_y, -12), project_3d(-12, clamp_y, -12)]
        draw.polygon([(p[0], p[1]) for p in front_back], fill=(65, 80, 100), outline=(90, 110, 135))

        # Phase 1: Reinigung & Späne ausblasen (81 - 170)
        if 80 <= frame_idx < 170:
            # Blasluft-Animation (Druckluftstöße)
            air_t = (frame_idx - 80) % 15
            for ox in [-5, 20, 45, 70, 85]:
                for oy in [10, 25, 40]:
                    pt = project_3d(ox + air_t * 0.8, oy, -21.0)
                    draw.ellipse([(pt[0]-2, pt[1]-2), (pt[0]+2, pt[1]+2)], fill=(125, 211, 252))
            draw.text((width//2 - 180, height//2 - 90), "💨 DRUCKLUFT: SCHRAUBSTOCK GRÜNDLICH AUSBLASEN!", font=font_title, fill=(56, 189, 248))
            draw.text((width//2 - 130, height//2 - 60), "Keine Späne auf Auflageflächen dulden!", font=font_sub, fill=(224, 242, 254))

        # Phase 2 bis Ende: Parallelunterlagen einlegen (ab Frame 171)
        if frame_idx >= 170:
            # Eintauchanimation der Parallelleisten (Z von +30 mm auf Z = -15 mm)
            if frame_idx < 240:
                prog = (frame_idx - 170) / 70.0
                par_z = 30.0 - 45.0 * prog
            else:
                par_z = -15.0  # Endlage auf Schraubstockboden

            # Parallelleiste 1 (hinten an fester Backe Y=45 bis Y=51, h=32 mm -> Oberkante bei Z=-15)
            # Parallelleiste 2 (vorne bei Y=-1 bis Y=5)
            par_color = (245, 158, 11) if (481 <= frame_idx < 580 and (frame_idx % 10 < 5)) else (180, 195, 215)
            
            # Hintere Leiste
            p_par1 = [project_3d(-5, 45, par_z), project_3d(85, 45, par_z), project_3d(85, 51, par_z), project_3d(-5, 51, par_z)]
            draw.polygon([(p[0], p[1]) for p in p_par1], fill=par_color, outline=(255, 255, 255), width=2)
            # Vordere Leiste
            p_par2 = [project_3d(-5, 0, par_z), project_3d(85, 0, par_z), project_3d(85, 6, par_z), project_3d(-5, 6, par_z)]
            draw.polygon([(p[0], p[1]) for p in p_par2], fill=par_color, outline=(255, 255, 255), width=2)

            if 170 <= frame_idx < 270:
                draw.text((width//2 - 200, height//2 - 90), "2. PARALLELUNTERLAGEN EINLEGEN (h = 32 mm)", font=font_title, fill=(251, 191, 36))
                draw.text((width//2 - 170, height//2 - 60), "Geschliffene Präzisionsleisten plan auflegen", font=font_sub, fill=(254, 243, 199))

        # Phase 3 bis Ende: Rohteil einlegen (ab Frame 271)
        if frame_idx >= 270:
            if frame_idx < 340:
                prog = (frame_idx - 270) / 70.0
                stock_z = 35.0 - 35.0 * prog  # Senkt sich ab bis Z=0 (Oberseite) und Z=-15 (Unterseite)
            else:
                stock_z = 0.0

            # Rohteilmaße: 85 x 55 x 15 mm. Oberkante Z = stock_z, Unterkante Z = stock_z - 15 mm
            r_top = stock_z
            r_bot = stock_z - 15.0
            
            # Rohteil-Box zeichnen
            w_bot = [project_3d(-2.5, -2.5, r_bot), project_3d(82.5, -2.5, r_bot), project_3d(82.5, 52.5, r_bot), project_3d(-2.5, 52.5, r_bot)]
            draw.polygon([(p[0], p[1]) for p in w_bot], fill=(35, 48, 65), outline=(75, 95, 120))
            
            # Seiten
            for i in range(4):
                ni = (i + 1) % 4
                xs = [-2.5, 82.5, 82.5, -2.5]
                ys = [-2.5, -2.5, 52.5, 52.5]
                pt1 = project_3d(xs[i], ys[i], r_top)
                pt2 = project_3d(xs[ni], ys[ni], r_top)
                pb2 = project_3d(xs[ni], ys[ni], r_bot)
                pb1 = project_3d(xs[i], ys[i], r_bot)
                draw.polygon([(pt1[0], pt1[1]), (pt2[0], pt2[1]), (pb2[0], pb2[1]), (pb1[0], pb1[1])],
                             fill=(45, 62, 85), outline=(85, 110, 140))
            
            # Oberseite
            w_top = [project_3d(-2.5, -2.5, r_top), project_3d(82.5, -2.5, r_top), project_3d(82.5, 52.5, r_top), project_3d(-2.5, 52.5, r_top)]
            draw.polygon([(p[0], p[1]) for p in w_top], fill=(55, 80, 110), outline=(147, 197, 253), width=2)

            if 270 <= frame_idx < 380:
                draw.text((width//2 - 200, height//2 - 90), "3. ROHTEIL EINLEGEN (85 x 55 x 15 mm)", font=font_title, fill=(96, 165, 250))
                draw.text((width//2 - 180, height//2 - 60), "Lange Seite in X, feste Backe hinten als Anschlag!", font=font_sub, fill=(219, 234, 254))

        # Phase 4: Schraubstock festspannen & Schonhammer-Schlag (381 - 480)
        if 381 <= frame_idx < 480:
            draw.text((width//2 - 220, height//2 - 90), "4. SPANNEN (80 Nm) & SCHONHAMMER-SETZSCHLAG", font=font_title, fill=(234, 179, 8))
            
            # Schonhammer-Animation
            hammer_prog = ((frame_idx - 380) % 25) / 25.0
            hammer_z = 25.0 - 22.0 * math.sin(hammer_prog * math.pi)
            hp_top = project_3d(40, 25, hammer_z + 20)
            hp_head = project_3d(40, 25, hammer_z)
            draw.line([(hp_top[0], hp_top[1]), (hp_head[0], hp_head[1])], fill=(180, 83, 9), width=8)
            draw.ellipse([(hp_head[0]-16, hp_head[1]-8), (hp_head[0]+16, hp_head[1]+8)], fill=(245, 158, 11), outline=(255, 255, 255), width=2)
            
            if hammer_prog > 0.4 and hammer_prog < 0.6:
                # Schlag-Funken
                draw.text((hp_head[0] + 20, hp_head[1] - 15), "💥 KLACK! (Satter Sitz)", font=font_badge, fill=(255, 255, 255))
            draw.text((width//2 - 170, height//2 - 60), "Kräftig von oben klopfen, damit Teil satt aufliegt!", font=font_sub, fill=(254, 240, 138))

        # Phase 5: Wackel-Probe der Parallelleisten (481 - 580)
        if 481 <= frame_idx < 580:
            draw.text((width//2 - 220, height//2 - 90), "5. DIE WACKEL-PROBE (FINGERTEST)", font=font_title, fill=(34, 197, 94))
            draw.text((width//2 - 210, height//2 - 60), "Versuch: Parallelleisten mit Fingern verschieben!", font=font_sub, fill=(187, 247, 208))

            # Pfeile & Bestätigungs-Badges an beiden Leisten
            par1_p = project_3d(40, 48, -15)
            par2_p = project_3d(40, 3, -15)
            draw.rectangle([(par1_p[0]-60, par1_p[1]-12), (par1_p[0]+60, par1_p[1]+12)], fill=(22, 101, 52), outline=(34, 197, 94), width=2)
            draw.text((par1_p[0]-50, par1_p[1]-8), "BOMBENFEST!", font=font_small, fill=(255, 255, 255))
            draw.rectangle([(par2_p[0]-60, par2_p[1]-12), (par2_p[0]+60, par2_p[1]+12)], fill=(22, 101, 52), outline=(34, 197, 94), width=2)
            draw.text((par2_p[0]-50, par2_p[1]-8), "BOMBENFEST!", font=font_small, fill=(255, 255, 255))

        # Phase 6: 3D-Kantentaster & G54 Nullpunktaufnahme (581 - 680)
        if 581 <= frame_idx < 680:
            draw.text((width//2 - 230, height//2 - 90), "6. WERKSTÜCKNULLPUNKT G54 ANTASTEN", font=font_title, fill=(168, 85, 247))
            
            # 3D-Kantentaster fährt an Ecke X0 / Y0 / Z0
            t_sub = (frame_idx - 581) / 99.0
            probe_x = -2.5 + 2.5 * math.cos(t_sub * 4.0)
            probe_y = -2.5 + 2.5 * math.sin(t_sub * 4.0)
            probe_z = 10.0 - 10.0 * t_sub

            pr_tip = project_3d(probe_x, probe_y, probe_z)
            pr_shaft = project_3d(probe_x, probe_y, probe_z + 25)
            draw.line([(pr_tip[0], pr_tip[1]), (pr_shaft[0], pr_shaft[1])], fill=(216, 180, 254), width=6)
            draw.ellipse([(pr_tip[0]-6, pr_tip[1]-6), (pr_tip[0]+6, pr_tip[1]+6)], fill=(239, 68, 68), outline=(255, 255, 255), width=2)

            draw.text((pr_tip[0] + 15, pr_tip[1] - 10), "🔴 3D-TASTER (Kugel Ø10 mm)", font=font_badge, fill=(244, 114, 182))
            draw.text((width//2 - 240, height//2 - 60), "Wichtig: Tastkugel-Radius (+5.0 mm) in Steuerung verrechnen!", font=font_sub, fill=(243, 232, 255))

        # Phase 7 & G54 Achsenkreuz (ab Frame 630 bis 720)
        if frame_idx >= 630:
            g54_p = project_3d(0, 0, 0)
            draw.ellipse([(g54_p[0] - 6, g54_p[1] - 6), (g54_p[0] + 6, g54_p[1] + 6)], fill=(255, 255, 255))
            px = project_3d(25, 0, 0)
            draw.line([(g54_p[0], g54_p[1]), (px[0], px[1])], fill=(239, 68, 68), width=3) # X+ rot
            py = project_3d(0, 25, 0)
            draw.line([(g54_p[0], g54_p[1]), (py[0], py[1])], fill=(34, 197, 94), width=3) # Y+ grün
            pz = project_3d(0, 0, 25)
            draw.line([(g54_p[0], g54_p[1]), (pz[0], pz[1])], fill=(56, 189, 248), width=3) # Z+ blau
            draw.text((g54_p[0] - 65, g54_p[1] + 8), "G54 (X0,Y0,Z0)", font=font_small, fill=(255, 255, 255))

            if frame_idx >= 680:
                draw.text((width//2 - 250, height//2 - 90), "7. RÜSTUNG 100% ABGENOMMEN & FREIGEGEBEN", font=font_title, fill=(34, 197, 94))
                draw.text((width//2 - 220, height//2 - 60), "Startklar für Luftschnitt in Z+50 mm & Einzelsatz!", font=font_sub, fill=(187, 247, 208))

        # --- HUD KOPFZEILE (Oben) ---
        draw.rectangle([(0, 0), (width, 55)], fill=(11, 15, 22))
        draw.line([(0, 55), (width, 55)], fill=(30, 41, 59), width=2)
        draw.text((25, 12), "🛠️ CNC-LEHRVIDEO: ROHTEIL SPANNEN & G54 NULLPUNKT EINSTELLEN", font=font_title, fill=(255, 255, 255))
        draw.text((width - 340, 18), "Dipl.-Ing. Bujanovski | Haas VF-2", font=font_hud, fill=(148, 163, 184))

        # --- HUD FUSSZEILE (Unten) ---
        draw.rectangle([(0, height - 70), (width, height)], fill=(11, 15, 22))
        draw.line([(0, height - 70), (width, height - 70)], fill=(30, 41, 59), width=2)

        # Aktueller Schritt-Balken
        curr_step_text = "Phase 0: Bereitstellung"
        if 80 <= frame_idx < 170:
            curr_step_text = "Schritt 1/6: Schraubstock & Backen reinigen (Spänefalle verhindern)"
        elif 170 <= frame_idx < 270:
            curr_step_text = "Schritt 2/6: Parallelleisten h = 32 mm einlegen (Kollisionsreserve +7 mm)"
        elif 270 <= frame_idx < 380:
            curr_step_text = "Schritt 3/6: Rohteil 85x55x15 mm einlegen (Spannrand 3.0 mm)"
        elif 381 <= frame_idx < 480:
            curr_step_text = "Schritt 4/6: Schraubstock mit 80 Nm spannen & Schonhammer-Setzschlag"
        elif 481 <= frame_idx < 580:
            curr_step_text = "Schritt 5/6: Die Wackel-Probe durchführen (beide Leisten spielfrei fest)"
        elif 581 <= frame_idx < 680:
            curr_step_text = "Schritt 6/6: G54 mit 3D-Taster aufnehmen (+5 mm Kugelradius verrechnen)"
        elif frame_idx >= 680:
            curr_step_text = "✅ 100% FREIGABE: Jetzt Luftschnitt in Z+50 mm & Einzelsatz starten!"

        draw.text((25, height - 55), curr_step_text, font=font_hud, fill=(250, 204, 21))
        draw.text((25, height - 30), "Vorgabe aus Einrichteblatt: 06_EINRICHTEBLATT_SETUP_SHEET.md | Haas NGC Steuerung", font=font_small, fill=(148, 163, 184))

        # Fortschrittsbalken
        bar_w = int((frame_idx / total_frames) * (width - 50))
        draw.rectangle([(25, height - 10), (width - 25, height - 6)], fill=(30, 41, 59))
        draw.rectangle([(25, height - 10), (25 + bar_w, height - 6)], fill=(34, 197, 94))

        # Frame an FFmpeg senden
        proc.stdin.write(img.tobytes())

        if frame_idx % 60 == 0:
            print(f"Frame {frame_idx}/{total_frames} gerendert...")

    proc.stdin.close()
    proc.wait()
    print(f"Video erfolgreich gerendert: {out_mp4}")

if __name__ == "__main__":
    render_video()
