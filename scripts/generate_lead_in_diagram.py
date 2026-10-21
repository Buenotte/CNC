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
        font_subtitle = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
        font_h2 = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 24)
        font_body = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 17)
        font_bold = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 18)
        font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 17)
        font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 20)
        font_badge = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 15)
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
    draw.text((p1_x + 25, p1_y + 55), "Maßstabgetreue Darstellung: Nullpunkt G54 (X0 Y0), Rohteilaufmaß (+2.5 mm) & Fräser Ø10 mm", font=font_subtitle, fill=text_muted)
    
    # 2D Koordinatensystem Ursprung für Zeichnung
    # Skalierungsfaktor: 1 mm = 12 Pixel
    scale = 12.0
    ox = p1_x + 360  # Pixel-Position von X=0 mm
    oy = p1_y + 450  # Pixel-Position von Y=0 mm (Y wächst nach oben, Pixel nach unten => oy - Y*scale)
    
    def to_screen(x, y):
        return (ox + x * scale, oy - y * scale)
    
    # Subtiles CAD-Raster zeichnen (-30 mm bis +50 mm X, -30 mm bis +40 mm Y)
    for gx in range(-25, 50, 5):
        sx = ox + gx * scale
        color = (38, 46, 65) if gx % 10 != 0 else (48, 58, 82)
        draw.line([(sx, oy - 35 * scale), (sx, oy + 25 * scale)], fill=color, width=1)
        if gx % 10 == 0:
            draw.text((sx - 10, oy + 26 * scale), f"{gx}", font=font_mono, fill=(100, 115, 140))
            
    for gy in range(-20, 35, 5):
        sy = oy - gy * scale
        color = (38, 46, 65) if gy % 10 != 0 else (48, 58, 82)
        draw.line([(ox - 25 * scale, sy), (ox + 45 * scale, sy)], fill=color, width=1)
        if gy % 10 == 0:
            draw.text((ox - 35 * scale, sy - 8), f"{gy}", font=font_mono, fill=(100, 115, 140))
            
    # Rohteil (85 x 55 mm, von X -2.5 bis X +82.5, Y -2.5 bis Y +52.5)
    rt_x0, rt_y0 = to_screen(-2.5, -2.5)
    rt_x1, rt_y1 = to_screen(45, 32) # wir zeichnen die Ecke bis X+45, Y+32
    # Rohteil-Schraffur / Bereich
    draw.rectangle([(rt_x0, rt_y1), (rt_x1, rt_y0)], fill=(60, 45, 30), outline=stock_color, width=3)
    
    # Fertigteil (80 x 50 mm, von X 0.0 bis X 80.0, Y 0.0 bis Y 50.0)
    ft_x0, ft_y0 = to_screen(0, 0)
    ft_x1, ft_y1 = to_screen(45, 32)
    draw.rectangle([(ft_x0, ft_y1), (ft_x1, ft_y0)], fill=(30, 60, 95), outline=part_color, width=3)
    
    # Schraffur für das Rohteil-Übermaß (Aufmaß 2.5 mm)
    draw.text((ox + 5, oy - 20 * scale), "FERTIGTEIL (Soll-Kontur)", font=font_bold, fill=part_color)
    draw.text((ox + 5, oy - 17 * scale), "80 mm x 50 mm Fertigmaß", font=font_body, fill=text_muted)
    
    # Bemaßung Rohteil-Aufmaß 2.5 mm an der X-Kante
    bm_y = oy + 12 * scale
    draw.line([(ox - 2.5 * scale, bm_y), (ox, bm_y)], fill=stock_color, width=2)
    draw.line([(ox - 2.5 * scale, bm_y - 8), (ox - 2.5 * scale, bm_y + 8)], fill=stock_color, width=2)
    draw.line([(ox, bm_y - 8), (ox, bm_y + 8)], fill=stock_color, width=2)
    draw.text((ox - 3.8 * scale, bm_y + 12), "Aufmaß 2.5 mm", font=font_badge, fill=stock_color)
    
    # Bemaßung Rohteil-Aufmaß 2.5 mm an der Y-Kante
    bm_x = ox - 12 * scale
    draw.line([(bm_x, oy), (bm_x, oy + 2.5 * scale)], fill=stock_color, width=2)
    draw.line([(bm_x - 8, oy), (bm_x + 8, oy)], fill=stock_color, width=2)
    draw.line([(bm_x - 8, oy + 2.5 * scale), (bm_x + 8, oy + 2.5 * scale)], fill=stock_color, width=2)
    draw.text((bm_x - 110, oy + 0.3 * scale), "Aufmaß\n2.5 mm", font=font_badge, fill=stock_color)
    
    # Nullpunkt G54 Markierung an (0, 0)
    draw.ellipse([(ox - 8, oy - 8), (ox + 8, oy + 8)], fill=(255, 255, 255), outline=(0, 0, 0), width=2)
    # Fadenkreuz G54
    draw.line([(ox - 14, oy), (ox + 14, oy)], fill=(255, 255, 255), width=2)
    draw.line([(ox, oy - 14), (ox, oy + 14)], fill=(255, 255, 255), width=2)
    # Pfeile für X+ und Y+
    draw.line([(ox, oy), (ox + 60, oy)], fill=(239, 68, 68), width=3) # X+ rot
    draw.polygon([(ox + 65, oy), (ox + 55, oy - 5), (ox + 55, oy + 5)], fill=(239, 68, 68))
    draw.text((ox + 70, oy - 10), "+X", font=font_bold, fill=(239, 68, 68))
    
    draw.line([(ox, oy), (ox, oy - 60)], fill=(34, 197, 94), width=3) # Y+ grün
    draw.polygon([(ox, oy - 65), (ox - 5, oy - 55), (ox + 5, oy - 55)], fill=(34, 197, 94))
    draw.text((ox + 8, oy - 65), "+Y", font=font_bold, fill=(34, 197, 94))
    
    draw.text((ox + 12, oy + 12), "G54 Nullpunkt (X0, Y0)", font=font_bold, fill=text_white)
    
    # ================= ANFAHRWEG & WERKZEUGBEWEGUNG =================
    # Startpunkt außerhalb: X = -10.0, Y = -10.0
    sp_x, sp_y = to_screen(-10.0, -10.0)
    
    # Fräser an Startposition zeichnen (Radius = 5 mm -> 5 * scale Pixel)
    r_px = 5.0 * scale
    draw.ellipse([(sp_x - r_px, sp_y - r_px), (sp_x + r_px, sp_y + r_px)], 
                 fill=(80, 100, 130, 180), outline=(180, 200, 220), width=2)
    # Fräser-Zentrum
    draw.ellipse([(sp_x - 4, sp_y - 4), (sp_x + 4, sp_y + 4)], fill=g01_blue)
    draw.text((sp_x - 120, sp_y + 35), "Startposition im Freien:\nX = -10.0 mm | Y = -10.0 mm\n(Fräser Ø10 mm berührt hier nichts)", font=font_badge, fill=text_white)
    
    # 1. G00 Eilgang-Linie (Gelb gestrichelt) von oben nach X-10 Y-10 Z2
    # Gestrichelte Linie von Luft-Position
    draw.line([(sp_x - 90, sp_y - 90), (sp_x, sp_y)], fill=g00_yellow, width=3)
    draw.text((sp_x - 220, sp_y - 120), "G00 Eilgang (30 m/min)\nIn der Luft bis Z +2.0", font=font_bold, fill=g00_yellow)
    
    # 2. Die BLAUE ANFAHRLINIE G01 von (-10, -10) nach (0, 0)
    # Dies ist genau die Linie, die der Benutzer im Simulator gesehen hat!
    draw.line([(sp_x, sp_y), (ox, oy)], fill=g01_blue, width=5)
    
    # Fräserspur (Hüllkurve / Schnittbreite 10 mm) entlang dieser Linie
    # Versatz nach links und rechts um Fräserradius (5 mm senkrecht zur Diagonale)
    # Vektor (-10, -10) -> (0,0) ist (10, 10). Winkel 45 Grad. Senkrechte = (-sin 45, cos 45)
    dx = 5.0 * scale * math.cos(math.radians(135))
    dy = -5.0 * scale * math.sin(math.radians(135))
    draw.line([(sp_x + dx, sp_y + dy), (ox + dx, oy + dy)], fill=(14, 165, 233, 100), width=2)
    draw.line([(sp_x - dx, sp_y - dy), (ox - dx, oy - dy)], fill=(14, 165, 233, 100), width=2)
    
    # Fräser an Position (0, 0) halbtransparent zeichnen
    draw.ellipse([(ox - r_px, oy - r_px), (ox + r_px, oy + r_px)], 
                 fill=(14, 165, 233, 70), outline=g01_blue, width=2)
    
    # Wo schneidet der Fräser ins Material ein?
    # Rohteilkante ist bei X = -2.5 mm, Y = -2.5 mm
    eintritt_x, eintritt_y = to_screen(-2.5, -2.5)
    draw.ellipse([(eintritt_x - 6, eintritt_y - 6), (eintritt_x + 6, eintritt_y + 6)], fill=(245, 158, 11), outline=(255, 255, 255), width=2)
    
    # Beschriftung der blauen Linie (Lead-In)
    draw.rounded_rectangle([(sp_x + 10, sp_y - 70), (sp_x + 240, sp_y - 15)], radius=6, fill=(10, 40, 70), outline=g01_blue, width=2)
    draw.text((sp_x + 20, sp_y - 65), "BLAUE LINIE = G01 VORSCHUB!", font=font_bold, fill=(255, 255, 255))
    draw.text((sp_x + 20, sp_y - 42), "F1200 mm/min (Spanabnahme)", font=font_badge, fill=part_color)
    
    # Pfeil auf Schnittbereich
    draw.line([(sp_x + 100, sp_y - 15), (eintritt_x - 10, eintritt_y - 10)], fill=g01_blue, width=2)
    
    # ================= ROTE CRASH-WARNUNG =================
    # Was würde passieren, wenn man hier EILGANG (G00) fahren würde?
    draw.rounded_rectangle([(p1_x + 30, p1_y + 700), (p1_x + p1_w - 30, p1_y + 915)], radius=10, fill=(50, 15, 20), outline=danger_red, width=2)
    
    draw.text((p1_x + 50, p1_y + 715), "🚨 WARUM DARF HIER KEINE GESTRICHELTE GELBE LINIE (G00) SEIN?", font=font_h2, fill=danger_red)
    draw.text((p1_x + 50, p1_y + 755), 
              "• Das Rohteil hat +2.5 mm Aufmaß! Die Ecke X0 Y0 ist noch KEIN Freiraum, sondern ROHEISEN!\n"
              "• Bei einem Eilgang G00 (30 Meter/Minute = 1.800 km/h im Zerspanungsmaßstab) würde der Fräser\n"
              "  mit ungebremster Wucht in das 2.5 mm Rohteil-Fleisch rammen!\n"
              "• FOLGE: Sofortiger Fräserbruch, Spindellagerschaden (5.000 € Reparatur) und Werkstückschrott!\n"
              "• DESHALB: Der Postprozessor MUSS ab Z-5 mit kontrolliertem Schnittvorschub (G01 = BLAU) anfahren!",
              font=font_body, fill=(255, 220, 220), spacing=6)

    # ==================== RECHTES PANEL: 3D ABLAUF & G-CODE CODE ====================
    p2_x, p2_y, p2_w, p2_h = 1015, 105, 875, 945
    draw.rounded_rectangle([(p2_x, p2_y), (p2_x + p2_w, p2_y + p2_h)], radius=12, fill=panel_bg, outline=panel_border, width=2)
    
    draw.text((p2_x + 25, p2_y + 20), "2. SCHRITT-FÜR-SCHRITT PHASEN & G-CODE", font=font_h2, fill=text_white)
    draw.text((p2_x + 25, p2_y + 55), "Vergleich des echten NC-Codes mit der physikalischen Fräsbewegung", font=font_subtitle, fill=text_muted)
    
    # 4 Phasen-Karten
    steps = [
        {
            "num": "SCHRITT 1",
            "title": "G00 Eilgang in sichere Luft (GELBE GESTRICHELTE LINIE)",
            "gcode": "N45 G00 X-10.0 Y-10.0 Z2.0",
            "desc": "Der Fräser fährt mit Maximalgeschwindigkeit (30 m/min) im sicheren Abstand von 10 mm neben das Rohteil und bleibt 2 mm ÜBER der Werkstückoberkante stehen. Null Risiko!",
            "color": g00_yellow,
            "badge": "LUFTFAHRT"
        },
        {
            "num": "SCHRITT 2",
            "title": "G01 Senkrechtes Eintauchen auf Frästiefe (BLAUE LINIE)",
            "gcode": "N50 G01 Z-5.0 F500",
            "desc": "Der Fräser taucht im sanften Tauchvorschub (F500 mm/min) auf die Solltiefe Z = -5.0 mm ab. Weil er bei X-10 Y-10 steht, taucht er IN DER LUFT ab, ohne Materialberührung!",
            "color": g01_blue,
            "badge": "TAUCHEN"
        },
        {
            "num": "SCHRITT 3",
            "title": "G01 Lead-In: Horizontales Einschneiden ins Rohteil (BLAUE LINIE)",
            "gcode": "N55 G01 X0.0 Y0.0 F1200",
            "desc": "DAS IST DEINE BLAUE LINIE! Der Fräser fährt auf Tiefe Z-5 mm von X-10 Y-10 nach X0 Y0. Dabei schneidet er mit Vorschub F1200 durch das 2.5 mm Rohteilaufmaß!",
            "color": g01_blue,
            "badge": "LEAD-IN"
        },
        {
            "num": "SCHRITT 4",
            "title": "G01 Konturfräsen der eigentlichen Bauteilkante (BLAUE LINIE)",
            "gcode": "N60 G01 X80.0 Y0.0 F1200",
            "desc": "Jetzt fräst das Werkzeug die 80 mm lange Kante des Fertigteils sauber ab. Alle Kanten werden maßhaltig fertiggestellt.",
            "color": part_color,
            "badge": "KONTUR"
        }
    ]
    
    card_y = p2_y + 100
    for s in steps:
        draw.rounded_rectangle([(p2_x + 25, card_y), (p2_x + p2_w - 25, card_y + 145)], radius=8, fill=(20, 25, 36), outline=(45, 55, 75), width=1)
        
        # Nummer & Badge
        draw.rounded_rectangle([(p2_x + 40, card_y + 15), (p2_x + 130, card_y + 40)], radius=4, fill=(s["color"][0], s["color"][1], s["color"][2], 40), outline=s["color"], width=1)
        draw.text((p2_x + 48, card_y + 19), s["badge"], font=font_badge, fill=s["color"])
        
        draw.text((p2_x + 145, card_y + 16), s["title"], font=font_bold, fill=text_white)
        
        # G-Code Box
        draw.rounded_rectangle([(p2_x + 40, card_y + 48), (p2_x + p2_w - 40, card_y + 78)], radius=4, fill=(10, 14, 20), outline=(35, 45, 60), width=1)
        draw.text((p2_x + 55, card_y + 53), s["gcode"], font=font_mono_bold, fill=s["color"])
        
        # Beschreibung
        draw.text((p2_x + 40, card_y + 88), s["desc"], font=font_body, fill=text_muted)
        
        card_y += 160
        
    # Zusammenfassungs-Box unten rechts
    draw.rounded_rectangle([(p2_x + 25, card_y + 10), (p2_x + p2_w - 25, card_y + 265)], radius=10, fill=(16, 42, 66), outline=part_color, width=2)
    draw.text((p2_x + 45, card_y + 25), "💡 DIE MERKREGEL FÜR JEDEN CNC-ENTWICKLER:", font=font_h2, fill=(255, 255, 255))
    
    draw.text((p2_x + 45, card_y + 65),
              "• GELB GESTRICHELT (G00) darf die CNC-Maschine NUR DANN fahren,\n"
              "  wenn sie 100 % sicher weiß, dass KEIN Span abgetragen wird\n"
              "  (über dem Werkstück in Z > 0 oder mit 10 mm Sicherheitsabstand).\n\n"
              "• Sobald der Fräser auf Frästiefe Z = -5.0 mm abgesenkt ist,\n"
              "  befindet er sich auf Kollisionshöhe mit dem Rohteil!\n"
              "  Jede Bewegung auf dieser Höhe MUSS zwingend BLAU (G01 mit F...)\n"
              "  sein – selbst wenn sie scheinbar 'außerhalb' des Fertigteils beginnt!",
              font=font_body, fill=(225, 240, 255), spacing=5)

    # Zielordner sicherstellen
    os.makedirs("docs/bilder", exist_ok=True)
    out_path_png = "docs/bilder/cnc_anfahrbewegung_lead_in_erklaerung.png"
    out_path_jpg = "docs/bilder/cnc_anfahrbewegung_lead_in_erklaerung.jpg"
    
    # Als RGB konvertieren und speichern
    rgb_img = img.convert("RGB")
    rgb_img.save(out_path_jpg, quality=95)
    img.save(out_path_png)
    print(f"Diagramm erfolgreich gespeichert: {out_path_jpg} und {out_path_png}")

if __name__ == "__main__":
    create_lead_in_diagram()
