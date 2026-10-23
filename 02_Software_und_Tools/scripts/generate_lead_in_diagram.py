"""
Generiert die hochauflösende technische CAD-Grafik zur Erklärung der Anfahrbewegung (Lead-In / G01 vs G00).
Erklärt visuell und millimetergenau:
- Warum die Linie außerhalb des Fertigteils BLAU (G01) statt GELB GESTRICHELT (G00) ist
- Rohteilaufmaß (+2.5 mm) vs. Fertigteil (80x50 mm)
- Crash-Gefahr bei Eilgang G00
"""

import os
import math
from PIL import Image, ImageDraw, ImageFont

def create_lead_in_diagram():
    width = 1920
    height = 1080
    
    # Farbschema (Modern Dark CAD Blueprint / Engineering Studio)
    bg_color = (20, 24, 33)           # Tiefes CAD-Dunkelblau/Grau
    panel_bg = (28, 33, 46)          # Panel-Hintergrund
    panel_border = (45, 55, 75)      # Panel-Rahmen
    text_white = (245, 248, 255)
    text_muted = (150, 165, 185)
    
    # Feature-Farben
    stock_color = (220, 140, 40)     # Rohteil Orange/Bernstein
    stock_fill = (45, 35, 25, 100)
    part_color = (56, 189, 248)      # Fertigteil Cyan/Hellblau
    part_fill = (20, 50, 80)
    
    g00_yellow = (250, 204, 21)      # Eilgang G00 Gelb
    g01_blue = (14, 165, 233)        # Vorschub G01 Leuchtendes Cyan-Blau
    danger_red = (239, 68, 68)       # Kollision / Crash Rot
    tool_carbide = (160, 175, 195)   # VHM Fräser
    tool_cutting = (245, 158, 11)    # TiN / Beschichtung
    
    img = Image.new("RGBA", (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Schriftarten laden
    try:
        font_title = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 34)
        font_subtitle = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 19)
        font_h2 = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 23)
        font_body = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 16)
        font_bold = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 17)
        font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 16)
        font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 19)
        font_badge = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 14)
    except:
        font_title = font_subtitle = font_h2 = font_body = font_bold = font_mono = font_mono_bold = font_badge = ImageFont.load_default()
        
    # ==================== HEADER BEREICH ====================
    draw.rectangle([(0, 0), (width, 85)], fill=(15, 18, 25))
    draw.line([(0, 85), (width, 85)], fill=(50, 65, 90), width=2)
    
    # Header Badge
    draw.rounded_rectangle([(30, 22), (200, 62)], radius=6, fill=(14, 165, 233, 50), outline=g01_blue, width=2)
    draw.text((45, 31), "CNC PRAXIS-WISSEN", font=font_badge, fill=part_color)
    
    draw.text((220, 16), "Warum ist die Anfahrbewegung BLAU (G01) und nicht GELB (G00)?", font=font_title, fill=text_white)
    draw.text((220, 56), "Physikalische Erklärung des Lead-In (Schnittanfahrt) & Kollisionsschutz bei Rohteil-Übermaß", font=font_subtitle, fill=text_muted)
    
    # ==================== LINKES PANEL: 2D DRAUFSICHT (XY-EBENE) ====================
    p1_x, p1_y, p1_w, p1_h = 30, 105, 960, 945
    draw.rounded_rectangle([(p1_x, p1_y), (p1_x + p1_w, p1_y + p1_h)], radius=12, fill=panel_bg, outline=panel_border, width=2)
    
    # Panel 1 Header
    draw.text((p1_x + 25, p1_y + 20), "1. DRAUFSICHT (XY-Ebene von oben betrachtet)", font=font_h2, fill=text_white)
    draw.text((p1_x + 25, p1_y + 52), "Maßstabgetreue Darstellung: Nullpunkt G54 (X0 Y0), Rohteilaufmaß (+2.5 mm) & Fräser Ø10 mm", font=font_subtitle, fill=text_muted)
    
    # 2D Koordinatensystem Ursprung für Zeichnung
    scale = 12.0
    ox = p1_x + 380  # Pixel-Position von X=0 mm
    oy = p1_y + 480  # Pixel-Position von Y=0 mm
    
    def to_screen(x, y):
        return (ox + x * scale, oy - y * scale)
    
    # Subtiles CAD-Raster (unterhalb des Subtitles)
    for gx in range(-25, 48, 5):
        sx = ox + gx * scale
        color = (38, 46, 65) if gx % 10 != 0 else (48, 58, 82)
        draw.line([(sx, oy - 28 * scale), (sx, oy + 20 * scale)], fill=color, width=1)
        if gx % 10 == 0:
            draw.text((sx - 10, oy + 21 * scale), f"{gx}", font=font_mono, fill=(100, 115, 140))
            
    for gy in range(-18, 28, 5):
        sy = oy - gy * scale
        color = (38, 46, 65) if gy % 10 != 0 else (48, 58, 82)
        draw.line([(ox - 25 * scale, sy), (ox + 45 * scale, sy)], fill=color, width=1)
        if gy % 10 == 0:
            draw.text((ox - 35 * scale, sy - 8), f"{gy}", font=font_mono, fill=(100, 115, 140))
            
    # Rohteil (85 x 55 mm, von X -2.5 bis X +82.5, Y -2.5 bis Y +52.5)
    rt_x0, rt_y0 = to_screen(-2.5, -2.5)
    rt_x1, rt_y1 = to_screen(45, 27)
    draw.rectangle([(rt_x0, rt_y1), (rt_x1, rt_y0)], fill=(60, 45, 30), outline=stock_color, width=3)
    
    # Fertigteil (80 x 50 mm, von X 0.0 bis X 80.0, Y 0.0 bis Y 50.0)
    ft_x0, ft_y0 = to_screen(0, 0)
    ft_x1, ft_y1 = to_screen(45, 27)
    draw.rectangle([(ft_x0, ft_y1), (ft_x1, ft_y0)], fill=(30, 60, 95), outline=part_color, width=3)
    
    draw.text((ox + 15, oy - 18 * scale), "FERTIGTEIL (Soll-Kontur)", font=font_bold, fill=part_color)
    draw.text((ox + 15, oy - 15 * scale), "80 mm x 50 mm Fertigmaß", font=font_body, fill=text_muted)
    
    # Bemaßung Rohteil-Aufmaß 2.5 mm an der X-Kante
    bm_y = oy + 9 * scale
    draw.line([(ox - 2.5 * scale, bm_y), (ox, bm_y)], fill=stock_color, width=2)
    draw.line([(ox - 2.5 * scale, bm_y - 6), (ox - 2.5 * scale, bm_y + 6)], fill=stock_color, width=2)
    draw.line([(ox, bm_y - 6), (ox, bm_y + 6)], fill=stock_color, width=2)
    draw.text((ox - 3.8 * scale, bm_y + 10), "Aufmaß 2.5 mm", font=font_badge, fill=stock_color)
    
    # Bemaßung Rohteil-Aufmaß 2.5 mm an der Y-Kante
    bm_x = ox - 9 * scale
    draw.line([(bm_x, oy), (bm_x, oy + 2.5 * scale)], fill=stock_color, width=2)
    draw.line([(bm_x - 6, oy), (bm_x + 6, oy)], fill=stock_color, width=2)
    draw.line([(bm_x - 6, oy + 2.5 * scale), (bm_x + 6, oy + 2.5 * scale)], fill=stock_color, width=2)
    draw.text((bm_x - 15, oy + 0.2 * scale), "Aufmaß\n2.5 mm", font=font_badge, fill=stock_color, anchor="rm")
    
    # Nullpunkt G54 Markierung an (0, 0)
    draw.ellipse([(ox - 8, oy - 8), (ox + 8, oy + 8)], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    draw.line([(ox - 14, oy), (ox + 14, oy)], fill=(255, 255, 255), width=2)
    draw.line([(ox, oy - 14), (ox, oy + 14)], fill=(255, 255, 255), width=2)
    # Pfeile für X+ und Y+
    draw.line([(ox, oy), (ox + 70, oy)], fill=(239, 68, 68), width=3)
    draw.polygon([(ox + 75, oy), (ox + 65, oy - 5), (ox + 65, oy + 5)], fill=(239, 68, 68))
    draw.text((ox + 80, oy - 10), "+X", font=font_bold, fill=(239, 68, 68))
    
    draw.line([(ox, oy), (ox, oy - 65)], fill=(34, 197, 94), width=3)
    draw.polygon([(ox, oy - 65), (ox - 5, oy - 55), (ox + 5, oy - 55)], fill=(34, 197, 94))
    draw.text((ox + 8, oy - 65), "+Y", font=font_bold, fill=(34, 197, 94))
    
    # G54 Label außerhalb des Fräserkreises platziert
    draw.text((ox + 90, oy + 25), "G54 Nullpunkt (X0, Y0)", font=font_bold, fill=text_white)
    
    # ================= ANFAHRWEG & WERKZEUGBEWEGUNG =================
    sp_x, sp_y = to_screen(-10.0, -10.0)
    r_px = 5.0 * scale
    draw.ellipse([(sp_x - r_px, sp_y - r_px), (sp_x + r_px, sp_y + r_px)], 
                 fill=(80, 100, 130, 180), outline=(180, 200, 220), width=2)
    draw.ellipse([(sp_x - 4, sp_y - 4), (sp_x + 4, sp_y + 4)], fill=g01_blue)
    draw.text((sp_x - 120, sp_y + 35), "Startposition im Freien:\nX = -10.0 mm | Y = -10.0 mm\n(Fräser Ø10 mm berührt hier nichts)", font=font_badge, fill=text_white)
    
    # 1. G00 Eilgang-Linie (Gelb gestrichelt)
    draw.line([(sp_x - 70, sp_y - 70), (sp_x, sp_y)], fill=g00_yellow, width=3)
    draw.rounded_rectangle([(sp_x - 290, sp_y - 145), (sp_x - 120, sp_y - 95)], radius=6, fill=(35, 30, 15), outline=g00_yellow, width=1)
    draw.text((sp_x - 280, sp_y - 140), "G00 Eilgang (30 m/min)\nIn der Luft bis Z +2.0", font=font_bold, fill=g00_yellow)
    
    # 2. Die BLAUE ANFAHRLINIE G01 von (-10, -10) nach (0, 0)
    draw.line([(sp_x, sp_y), (ox, oy)], fill=g01_blue, width=5)
    
    dx = 5.0 * scale * math.cos(math.radians(135))
    dy = -5.0 * scale * math.sin(math.radians(135))
    draw.line([(sp_x + dx, sp_y + dy), (ox + dx, oy + dy)], fill=(14, 165, 233, 100), width=2)
    draw.line([(sp_x - dx, sp_y - dy), (ox - dx, oy - dy)], fill=(14, 165, 233, 100), width=2)
    
    # Fräser an Position (0, 0) halbtransparent zeichnen
    draw.ellipse([(ox - r_px, oy - r_px), (ox + r_px, oy + r_px)], 
                 fill=(14, 165, 233, 70), outline=g01_blue, width=2)
    
    # Wo schneidet der Fräser ins Material ein?
    eintritt_x, eintritt_y = to_screen(-2.5, -2.5)
    draw.ellipse([(eintritt_x - 6, eintritt_y - 6), (eintritt_x + 6, eintritt_y + 6)], fill=(245, 158, 11), outline=(255, 255, 255), width=2)
    
    # Beschriftung der blauen Linie (Lead-In)
    draw.rounded_rectangle([(sp_x + 10, sp_y - 70), (sp_x + 240, sp_y - 15)], radius=6, fill=(10, 40, 70), outline=g01_blue, width=2)
    draw.text((sp_x + 20, sp_y - 65), "BLAUE LINIE = G01 VORSCHUB!", font=font_bold, fill=(255, 255, 255))
    draw.text((sp_x + 20, sp_y - 42), "F1200 mm/min (Spanabnahme)", font=font_badge, fill=part_color)
    
    draw.line([(sp_x + 100, sp_y - 15), (eintritt_x - 10, eintritt_y - 10)], fill=g01_blue, width=2)
    
    # ================= ROTE CRASH-WARNUNG =================
    draw.rounded_rectangle([(p1_x + 30, p1_y + 700), (p1_x + p1_w - 30, p1_y + 915)], radius=10, fill=(50, 15, 20), outline=danger_red, width=2)
    
    draw.rounded_rectangle([(p1_x + 50, p1_y + 715), (p1_x + 160, p1_y + 740)], radius=4, fill=danger_red)
    draw.text((p1_x + 105, p1_y + 727), "CRASH-GEFAHR", font=font_badge, fill=text_white, anchor="mm")
    draw.text((p1_x + 175, p1_y + 718), "WARUM DARF HIER KEINE GESTRICHELTE GELBE LINIE (G00) SEIN?", font=font_bold, fill=(254, 202, 202))
    
    crash_text = [
        "• Das Rohteil hat +2.5 mm Aufmaß! Die Ecke X0 Y0 ist noch KEIN Freiraum, sondern ROHEISEN!",
        "• Bei einem Eilgang G00 (30 Meter/Minute = 1.800 km/h im Zerspanungsmaßstab) würde der Fräser",
        "  mit ungebremster Wucht in das 2.5 mm Rohteil-Fleisch rammen!",
        "• FOLGE: Sofortiger Fräserbruch, Spindellagerschaden (5.000 € Reparatur) und Werkstückschrott!",
        "• DESHALB: Der Postprozessor MUSS ab Z-5 mit kontrolliertem Schnittvorschub (G01 = BLAU) anfahren!"
    ]
    
    cy = p1_y + 755
    for line in crash_text:
        draw.text((p1_x + 50, cy), line, font=font_body, fill=(254, 226, 226))
        cy += 30
        
    # ==================== RECHTES PANEL: CODE & LOGIK ====================
    p2_x, p2_y, p2_w, p2_h = 1020, 105, 870, 945
    draw.rounded_rectangle([(p2_x, p2_y), (p2_x + p2_w, p2_y + p2_h)], radius=12, fill=panel_bg, outline=panel_border, width=2)
    
    draw.text((p2_x + 25, p2_y + 20), "2. SCHRITT-FÜR-SCHRITT PHASEN & G-CODE", font=font_h2, fill=text_white)
    draw.text((p2_x + 25, p2_y + 52), "Vergleich des echten NC-Codes mit der physikalischen Fräsbewegung", font=font_subtitle, fill=text_muted)
    
    steps = [
        {
            "tag": "G00 Eilgang in sichere Luft (GELBE GESTRICHELTE LINIE)",
            "tag_color": g00_yellow,
            "code": "N45 G00 X-10.0 Y-10.0 Z2.0",
            "desc": "Der Fräser fährt mit Maximalgeschwindigkeit (30 m/min) im sicheren Abstand von 10 mm neben das Rohteil und bleibt 2 mm über dem Material stehen."
        },
        {
            "tag": "G01 Senkrechtes Eintauchen auf Frästiefe (BLAUE LINIE)",
            "tag_color": g01_blue,
            "code": "N50 G01 Z-5.0 F500",
            "desc": "Der Fräser taucht im sanften Tauchvorschub (F500 mm/min) auf die Solltiefe Z = -5.0 mm ab. Weil er bei X-10 Y-10 steht, taucht er komplett in freier Luft ein!"
        },
        {
            "tag": "G01 Lead-In: Horizontales Einschneiden ins Rohteil (BLAUE LINIE)",
            "tag_color": g01_blue,
            "code": "N55 G01 X0.0 Y0.0 F1200",
            "desc": "DAS IST DEINE BLAUE LINIE! Der Fräser fährt auf Tiefe Z-5 mm von X-10 Y-10 nach X0 Y0. Dabei schneidet er mit Vorschub F1200 sanft durch das 2.5 mm Aufmaß!"
        },
        {
            "tag": "G01 Konturfräsen der eigentlichen Bauteilkante (BLAUE LINIE)",
            "tag_color": g01_blue,
            "code": "N60 G01 X80.0 Y0.0 F1200",
            "desc": "Jetzt fräst das Werkzeug die 80 mm lange Kante des Fertigteils sauber ab. Alle Kanten werden maßhaltig fertiggestellt."
        }
    ]
    
    sy = p2_y + 90
    for s in steps:
        draw.rounded_rectangle([(p2_x + 25, sy), (p2_x + p2_w - 25, sy + 140)], radius=8, fill=(20, 25, 35), outline=(40, 50, 70), width=1)
        
        draw.rounded_rectangle([(p2_x + 40, sy + 15), (p2_x + 95, sy + 38)], radius=4, fill=s["tag_color"])
        draw.text((p2_x + 105, sy + 16), s["tag"], font=font_bold, fill=text_white)
        
        draw.rounded_rectangle([(p2_x + 40, sy + 45), (p2_x + p2_w - 40, sy + 80)], radius=4, fill=(10, 14, 20))
        draw.text((p2_x + 55, sy + 52), s["code"], font=font_mono_bold, fill=part_color)
        
        draw.text((p2_x + 40, sy + 92), s["desc"], font=font_body, fill=text_muted)
        
        sy += 155
        
    # Merkkasten unten rechts
    draw.rounded_rectangle([(p2_x + 25, sy + 15), (p2_x + p2_w - 25, sy + 215)], radius=10, fill=(15, 35, 55), outline=g01_blue, width=2)
    draw.rounded_rectangle([(p2_x + 40, sy + 30), (p2_x + 180, sy + 55)], radius=4, fill=g01_blue)
    draw.text((p2_x + 110, sy + 42), "CNC-PRAXISREGEL", font=font_badge, fill=text_white, anchor="mm")
    draw.text((p2_x + 195, sy + 32), "DIE MERKREGEL FÜR JEDEN CNC-ENTWICKLER:", font=font_bold, fill=text_white)
    
    rules = [
        "• GELB GESTRICHELT (G00) darf die CNC-Maschine NUR DANN fahren,",
        "  wenn sie 100 % sicher weiß, dass KEIN Span abgetragen wird",
        "  (über dem Werkstück in Z > 0 oder mit 10 mm Sicherheitsabstand).",
        "",
        "• Sobald der Fräser auf Frästiefe Z = -5.0 mm abgesenkt ist,",
        "  befindet er sich auf Kollisionshöhe mit dem Rohteil!",
        "  Jede Bewegung auf dieser Höhe MUSS zwingend BLAU (G01 mit F...)",
        "  sein – selbst wenn sie scheinbar 'außerhalb' des Fertigteils beginnt!"
    ]
    
    ry = sy + 68
    for r in rules:
        draw.text((p2_x + 40, ry), r, font=font_body, fill=(210, 230, 255))
        ry += 18
        
    out_dir = "c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/bilder"
    out_file = os.path.join(out_dir, "cnc_anfahrbewegung_lead_in_erklaerung.jpg")
    img.convert("RGB").save(out_file, quality=95)
    print("Gespeichert:", out_file)

if __name__ == "__main__":
    create_lead_in_diagram()
