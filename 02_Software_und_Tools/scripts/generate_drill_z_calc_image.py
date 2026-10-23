"""
Skript zur Erzeugung des hochpräzisen CAD-Diagramms:
'Berechnung der Durchgangsbohrung Z-MIN = -14.500 mm'
"""
import os
import shutil
from PIL import Image, ImageDraw, ImageFont

# Dimensionen
W = 1650
H = 1050

img = Image.new("RGB", (W, H), "#F8FAFC")
draw = ImageDraw.Draw(img)

# Schriftarten
font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 30)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 19)
font_h2 = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 22)
font_h3 = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 18)
font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 16)
font_body_b = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 16)
font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 15)
font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 13)
font_dim = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 15)

# Hintergrund-Gitter (Subtiles technisches CAD-Raster)
for x in range(0, W, 40):
    draw.line([(x, 0), (x, H)], fill="#EDF2F7", width=1)
for y in range(0, H, 40):
    draw.line([(0, y), (W, y)], fill="#EDF2F7", width=1)

# Header Banner
draw.rectangle([(0, 0), (W, 95)], fill="#0F172A")
draw.text((40, 18), "ÜBUNG 3: EXAKTE BERECHNUNG DER DURCHGANGSBOHRUNG (Z-MIN = -14.500 mm)", fill="#FFFFFF", font=font_title)
draw.text((40, 58), "Warum reicht Z = -12.0 mm nicht aus? Geometrie aus Bauteildicke, Bohrerspitze (118°) und Durchbruch-Zugabe", fill="#94A3B8", font=font_subtitle)
draw.line([(0, 95), (W, 95)], fill="#2563EB", width=4)

# ==============================================================================
# LINKER BEREICH: CAD-SCHNITTZEICHNUNG (SCHNITTANSICHT A-A)
# ==============================================================================
cad_x0 = 50
cad_y0 = 130
cad_w = 790
cad_h = 870

draw.rounded_rectangle([(cad_x0, cad_y0), (cad_x0 + cad_w, cad_y0 + cad_h)], radius=12, fill="#FFFFFF", outline="#CBD5E1", width=2)
draw.rectangle([(cad_x0, cad_y0), (cad_x0 + cad_w, cad_y0 + 46)], fill="#F1F5F9")
draw.text((cad_x0 + 20, cad_y0 + 12), "CAD-SCHNITTANSICHT: SPIRALBOHRER D=5.0 mm DURCH ALUMINIUMPLATTE", fill="#1E293B", font=font_h3)
draw.line([(cad_x0, cad_y0 + 46), (cad_x0 + cad_w, cad_y0 + 46)], fill="#E2E8F0", width=1)

# Maßstab für Z-Achse im Diagramm:
# 1 mm physikalisch = 28 Pixel im Bild
scale_z = 28.0

y_z0 = 360
y_z_plate_bottom = y_z0 + int(12.0 * scale_z)  # 696
y_z_cyl_end = y_z_plate_bottom + int(1.0 * scale_z)  # 724
y_z_tip = y_z_cyl_end + int(1.5 * scale_z)  # 766

# Werkstück Geometrie im Schnitt:
hole_center_x = 445
hole_w = 90
hole_left_x = hole_center_x - hole_w // 2   # 400
hole_right_x = hole_center_x + hole_w // 2  # 490

wp_left = 175
wp_right = 715

# Werkstück Material links & rechts der Bohrung
draw.rectangle([(wp_left, y_z0), (hole_left_x, y_z_plate_bottom)], fill="#E2E8F0", outline="#94A3B8", width=2)
draw.rectangle([(hole_right_x, y_z0), (wp_right, y_z_plate_bottom)], fill="#E2E8F0", outline="#94A3B8", width=2)

# Schraffur links
for d in range(wp_left, hole_left_x + 100, 24):
    x_start = d
    y_start = y_z0
    x_end = d - (y_z_plate_bottom - y_z0)
    y_end = y_z_plate_bottom
    draw.line([(max(wp_left, x_end), min(y_end, y_z0 + (x_start - max(wp_left, x_end)))),
               (min(hole_left_x, x_start), y_z0)], fill="#CBD5E1", width=1)

# Schraffur rechts
for d in range(hole_right_x, wp_right + 100, 24):
    draw.line([(max(hole_right_x, d - 100), min(y_z_plate_bottom, y_z0 + 100)),
               (min(wp_right, d), y_z0)], fill="#CBD5E1", width=1)

# Text im Werkstück - sauber zentriert in den Blöcken
draw.text(((wp_left + hole_left_x) // 2, y_z0 + 140), "ALUMINIUMPLATTE\n(Dicke h = 12.0 mm)", fill="#334155", font=font_h3, anchor="mm")
draw.text(((hole_right_x + wp_right) // 2, y_z0 + 140), "WERKSTOFF:\nAlMgSi0.5 (AW-6060)", fill="#334155", font=font_h3, anchor="mm")

# ------------------------------------------------------------------------------
# PARALLELUNTERLAGEN & TUNNEL UNTER DEM BAUTEIL
# ------------------------------------------------------------------------------
par_h = 160
# Linke Unterlage
draw.rectangle([(wp_left, y_z_plate_bottom), (wp_left + 75, y_z_plate_bottom + par_h)], fill="#64748B", outline="#334155", width=2)
draw.text((wp_left + 37, y_z_plate_bottom + 80), "PARALLEL-\nUNTERLAGE", fill="#FFFFFF", font=font_badge, anchor="mm")

# Rechte Unterlage
draw.rectangle([(wp_right - 75, y_z_plate_bottom), (wp_right, y_z_plate_bottom + par_h)], fill="#64748B", outline="#334155", width=2)
draw.text((wp_right - 37, y_z_plate_bottom + 80), "PARALLEL-\nUNTERLAGE", fill="#FFFFFF", font=font_badge, anchor="mm")

# Schraubstock-Basis ganz unten
draw.rectangle([(wp_left - 30, y_z_plate_bottom + par_h), (wp_right + 30, y_z_plate_bottom + par_h + 35)], fill="#334155", outline="#1E293B", width=2)
draw.text((hole_center_x, y_z_plate_bottom + par_h + 17), "MASCHINENSCHRAUBSTOCK-BODEN AUS GEHÄRTETEM STAHL", fill="#94A3B8", font=font_badge, anchor="mm")

# Luft-Tunnel Kennzeichnung
tunnel_x1 = wp_left + 75
tunnel_x2 = wp_right - 75
draw.rectangle([(tunnel_x1 + 2, y_z_plate_bottom + 2), (tunnel_x2 - 2, y_z_plate_bottom + par_h - 2)], fill="#F8FAFC")
draw.line([(tunnel_x1, y_z_plate_bottom), (tunnel_x1, y_z_plate_bottom + par_h)], fill="#3B82F6", width=2)
draw.line([(tunnel_x2, y_z_plate_bottom), (tunnel_x2, y_z_plate_bottom + par_h)], fill="#3B82F6", width=2)
draw.text((hole_center_x, y_z_plate_bottom + 115), "FREIER LUFT-TUNNEL (Unter dem Bauteil)\nBohrerspitze tritt gefahrlos ins Leere aus", fill="#2563EB", font=font_body_b, anchor="mm")

# ------------------------------------------------------------------------------
# DER SPIRALBOHRER (T02 - Ø 5.0 mm)
# ------------------------------------------------------------------------------
drill_top_y = 190
draw.rectangle([(hole_center_x - 42, drill_top_y), (hole_center_x + 42, y_z0 - 70)], fill="#475569", outline="#1E293B", width=2)
draw.text((hole_center_x, drill_top_y + 25), "WERKZEUGHALTER", fill="#E2E8F0", font=font_badge, anchor="mm")

drill_cyl_pts = [
    (hole_left_x + 6, y_z0 - 70),
    (hole_right_x - 6, y_z0 - 70),
    (hole_right_x - 6, y_z_cyl_end),
    (hole_left_x + 6, y_z_cyl_end)
]
draw.polygon(drill_cyl_pts, fill="#F59E0B", outline="#B45309", width=2)

for y_flute in range(y_z0 - 50, y_z_cyl_end, 36):
    draw.arc([(hole_left_x + 8, y_flute), (hole_right_x - 8, y_flute + 28)], 0, 180, fill="#78350F", width=3)

drill_tip_pts = [
    (hole_left_x + 6, y_z_cyl_end),
    (hole_right_x - 6, y_z_cyl_end),
    (hole_center_x, y_z_tip)
]
draw.polygon(drill_tip_pts, fill="#D97706", outline="#78350F", width=2)
draw.line([(hole_left_x + 6, y_z_cyl_end), (hole_center_x, y_z_tip)], fill="#FEF3C7", width=2)
draw.line([(hole_right_x - 6, y_z_cyl_end), (hole_center_x, y_z_tip)], fill="#FEF3C7", width=2)
draw.ellipse([(hole_center_x - 5, y_z_tip - 5), (hole_center_x + 5, y_z_tip + 5)], fill="#EF4444", outline="#991B1B", width=2)

# ------------------------------------------------------------------------------
# REFERENZ-EBENEN
# ------------------------------------------------------------------------------
def draw_ref_line(y, color, dash=True):
    if dash:
        for x in range(cad_x0 + 15, cad_x0 + cad_w - 15, 12):
            draw.line([(x, y), (x + 7, y)], fill=color, width=2)
    else:
        draw.line([(cad_x0 + 15, y), (cad_x0 + cad_w - 15, y)], fill=color, width=2)

# Z = 0 Ebene
draw_ref_line(y_z0, "#2563EB", dash=False)
draw.ellipse([(wp_left - 12, y_z0 - 12), (wp_left + 12, y_z0 + 12)], fill="#2563EB", outline="#1D4ED8", width=2)
draw.text((wp_left + 18, y_z0 - 24), "G54 NULLPUNKT (Z = 0.000 mm)", fill="#2563EB", font=font_h3)

draw_ref_line(y_z_plate_bottom, "#64748B", dash=True)
draw_ref_line(y_z_cyl_end, "#059669", dash=True)
draw_ref_line(y_z_tip, "#DC2626", dash=False)

# ------------------------------------------------------------------------------
# BEMASSUNGS-PFEILE LINKS (Im freien linken Rand x = 85)
# ------------------------------------------------------------------------------
# 1. Großer Pfeil für 12.0 mm Platte
draw.line([(85, y_z0), (85, y_z_plate_bottom)], fill="#1E293B", width=2)
draw.line([(77, y_z0), (93, y_z0)], fill="#1E293B", width=2)
draw.line([(77, y_z_plate_bottom), (93, y_z_plate_bottom)], fill="#1E293B", width=2)
draw.polygon([(85, y_z0), (81, y_z0 + 8), (89, y_z0 + 8)], fill="#1E293B")
draw.polygon([(85, y_z_plate_bottom), (81, y_z_plate_bottom - 8), (89, y_z_plate_bottom - 8)], fill="#1E293B")
draw.text((95, (y_z0 + y_z_plate_bottom) // 2), "12.0 mm\n(Platte)", fill="#1E293B", font=font_dim, anchor="lm")

# 2. Pfeil für 1.0 mm Überlauf
draw.line([(85, y_z_plate_bottom), (85, y_z_cyl_end)], fill="#059669", width=2)
draw.line([(77, y_z_cyl_end), (93, y_z_cyl_end)], fill="#059669", width=2)
draw.polygon([(85, y_z_cyl_end), (81, y_z_cyl_end - 6), (89, y_z_cyl_end - 6)], fill="#059669")
draw.text((95, y_z_cyl_end - 14), "+ 1.0 mm (Überlauf)", fill="#059669", font=font_badge, anchor="lm")

# 3. Pfeil für 1.5 mm Bohrerspitze
draw.line([(85, y_z_cyl_end), (85, y_z_tip)], fill="#D97706", width=2)
draw.line([(77, y_z_tip), (93, y_z_tip)], fill="#D97706", width=2)
draw.polygon([(85, y_z_tip), (81, y_z_tip - 6), (89, y_z_tip - 6)], fill="#D97706")
draw.text((95, y_z_tip - 14), "+ 1.5 mm (Bohrerspitze)", fill="#D97706", font=font_badge, anchor="lm")

# ------------------------------------------------------------------------------
# GESAMTMASS RECHTS (Im freien rechten Rand x = 775)
# ------------------------------------------------------------------------------
def draw_dim_arrow_right(x, y1, y2, label, color):
    draw.line([(x, y1), (x, y2)], fill=color, width=2)
    draw.line([(x - 8, y1), (x + 8, y1)], fill=color, width=2)
    draw.line([(x - 8, y2), (x + 8, y2)], fill=color, width=2)
    draw.polygon([(x, y1), (x - 4, y1 + 8), (x + 4, y1 + 8)], fill=color)
    draw.polygon([(x, y2), (x - 4, y2 - 8), (x + 4, y2 - 8)], fill=color)
    ymid = (y1 + y2) // 2
    draw.text((x - 12, ymid), label, fill=color, font=font_dim, anchor="rm")

draw_dim_arrow_right(775, y_z0, y_z_tip, "GESAMT = 14.500 mm\n-> Z-MIN = -14.500 mm", "#DC2626")

# Z-Koordinaten Badges im linken Rand
draw.rounded_rectangle([(cad_x0 + 8, y_z_plate_bottom - 24), (cad_x0 + 130, y_z_plate_bottom - 4)], radius=4, fill="#F1F5F9", outline="#CBD5E1")
draw.text((cad_x0 + 69, y_z_plate_bottom - 14), "Z = -12.0 mm (Boden)", fill="#475569", font=font_badge, anchor="mm")

draw.rounded_rectangle([(cad_x0 + 8, y_z_tip + 8), (cad_x0 + 145, y_z_tip + 30)], radius=4, fill="#FEF2F2", outline="#FCA5A5")
draw.text((cad_x0 + 76, y_z_tip + 19), "Z-MIN = -14.5 mm", fill="#DC2626", font=font_badge, anchor="mm")

# ==============================================================================
# RECHTER BEREICH: MATHEMATISCHE ERKLÄRUNGS-KARTE
# ==============================================================================
card_x0 = 870
card_y0 = 130
card_w = 720
card_h = 870

draw.rounded_rectangle([(card_x0, card_y0), (card_x0 + card_w, card_y0 + card_h)], radius=12, fill="#FFFFFF", outline="#CBD5E1", width=2)
draw.rectangle([(card_x0, card_y0), (card_x0 + card_w, card_y0 + 46)], fill="#0F172A")
draw.text((card_x0 + 20, card_y0 + 12), "INGENIEUR-FORMELN & LOGISCHE SCHRITTE", fill="#FFFFFF", font=font_h3)

# Block 1: Warum reicht Z = -12.0 mm nicht?
b1_y = card_y0 + 65
draw.rounded_rectangle([(card_x0 + 20, b1_y), (card_x0 + card_w - 20, b1_y + 130)], radius=8, fill="#FEF2F2", outline="#FCA5A5", width=1)
draw.rounded_rectangle([(card_x0 + 35, b1_y + 10), (card_x0 + 115, b1_y + 32)], radius=4, fill="#DC2626")
draw.text((card_x0 + 75, b1_y + 21), "ACHTUNG", fill="#FFFFFF", font=font_badge, anchor="mm")
draw.text((card_x0 + 125, b1_y + 12), "WARUM REICHT Z = -12.0 mm BEIM DURCHBOHREN NICHT?", fill="#991B1B", font=font_h3)
draw.text((card_x0 + 35, b1_y + 44), 
          "• Würde der Bohrer bei Z = -12.0 mm stoppen, hätte nur die Spitze das Bauteil berührt.\n"
          "• Das Bohrloch an der Unterseite wäre noch trichterförmig verschlossen!\n"
          "• Der zylindrische Schaft (D = 5.0 mm) muss VOLLSTÄNDIG aus der Unterseite austreten,\n"
          "  damit eine Schraube oder ein Bolzen hindurchpasst.", fill="#7F1D1D", font=font_body)

# Block 2: Die 3 Teil-Komponenten
b2_y = b1_y + 145
draw.rounded_rectangle([(card_x0 + 20, b2_y), (card_x0 + card_w - 20, b2_y + 180)], radius=8, fill="#F8FAFC", outline="#E2E8F0", width=1)
draw.rounded_rectangle([(card_x0 + 35, b2_y + 10), (card_x0 + 135, b2_y + 32)], radius=4, fill="#2563EB")
draw.text((card_x0 + 85, b2_y + 21), "GEOMETRIE", fill="#FFFFFF", font=font_badge, anchor="mm")
draw.text((card_x0 + 145, b2_y + 12), "DIE 3 TEIL-KOMPONENTEN DER Z-TIEFE:", fill="#1E293B", font=font_h3)

draw.text((card_x0 + 35, b2_y + 42), "1. Bauteildicke (h):               = 12.0 mm", fill="#1E293B", font=font_body_b)
draw.text((card_x0 + 55, b2_y + 64), "Vollmaterial der Aluminium-Flanschplatte von Z = 0 bis Z = -12.0 mm.", fill="#64748B", font=font_body)

draw.text((card_x0 + 35, b2_y + 90), "2. Durchbruch-Zugabe:         = 1.0 mm", fill="#059669", font=font_body_b)
draw.text((card_x0 + 55, b2_y + 112), "Zylindrischer Überlauf ins Freie, damit an der Austrittskante kein Grat bleibt.", fill="#64748B", font=font_body)

draw.text((card_x0 + 35, b2_y + 138), "3. Bohrerspitzen-Länge (l):  = 1.5 mm  (bei D = 5.0 mm & Spitzenwinkel 118°)", fill="#D97706", font=font_body_b)
draw.text((card_x0 + 55, b2_y + 158), "Exakte Formel: l = d / (2 * tan(118° / 2)) = 5.0 / (2 * 1.60) = 1.56 mm (≈ 1.5 mm)", fill="#64748B", font=font_code)

# Block 3: Die Gesamtrechnung
b3_y = b2_y + 195
draw.rounded_rectangle([(card_x0 + 20, b3_y), (card_x0 + card_w - 20, b3_y + 115)], radius=8, fill="#EFF6FF", outline="#BFDBFE", width=1)
draw.rounded_rectangle([(card_x0 + 35, b3_y + 10), (card_x0 + 145, b3_y + 32)], radius=4, fill="#1D4ED8")
draw.text((card_x0 + 90, b3_y + 21), "BERECHNUNG", fill="#FFFFFF", font=font_badge, anchor="mm")
draw.text((card_x0 + 155, b3_y + 12), "DIE GESAMTRECHNUNG FÜR DEN G-CODE:", fill="#1E40AF", font=font_h3)

draw.text((card_x0 + 35, b3_y + 44), "Gesamttiefe = Bauteildicke (12.0) + Durchbruch (1.0) + Spitze (1.5) = 14.5 mm", fill="#1E3A8A", font=font_body_b)
draw.text((card_x0 + 35, b3_y + 75), "Da Z = 0 oben liegt und es nach unten ins Material geht:", fill="#334155", font=font_body)
draw.text((card_x0 + 35, b3_y + 92), "--> Resultierende Koordinate: Z = -14.500 mm (Z-MIN)", fill="#DC2626", font=font_body_b)

# Block 4: Phasen
b4_y = b3_y + 130
draw.rounded_rectangle([(card_x0 + 20, b4_y), (card_x0 + card_w - 20, b4_y + 225)], radius=8, fill="#F8FAFC", outline="#E2E8F0", width=1)
draw.rounded_rectangle([(card_x0 + 35, b4_y + 10), (card_x0 + 115, b4_y + 32)], radius=4, fill="#0F172A")
draw.text((card_x0 + 75, b4_y + 21), "PROZESS", fill="#FFFFFF", font=font_badge, anchor="mm")
draw.text((card_x0 + 125, b4_y + 12), "WANN WIRD DIESER WERT ERMITTELT?", fill="#0F172A", font=font_h3)

draw.ellipse([(card_x0 + 35, b4_y + 48), (card_x0 + 47, b4_y + 60)], fill="#2563EB")
draw.text((card_x0 + 55, b4_y + 44), "Phase 1: Im CAM (Fusion 360)", fill="#1E293B", font=font_body_b)
draw.text((card_x0 + 55, b4_y + 64), "Beim Klick auf 'Generieren'. Fusion berechnet Bahnen\nund speichert Z-Min intern in section.getGlobalZRange().", fill="#475569", font=font_body)

draw.ellipse([(card_x0 + 35, b4_y + 112), (card_x0 + 47, b4_y + 124)], fill="#D97706")
draw.text((card_x0 + 55, b4_y + 108), "Phase 2: Im Postprozessor", fill="#1E293B", font=font_body_b)
draw.text((card_x0 + 55, b4_y + 128), "Beim Klick auf 'Posten'. getToolMinimumZ() liest -14.5 mm\naus und schreibt: (T02 | BOHRER | Z-MIN=-14.500mm).", fill="#475569", font=font_body)

draw.ellipse([(card_x0 + 35, b4_y + 176), (card_x0 + 47, b4_y + 188)], fill="#16A34A")
draw.text((card_x0 + 55, b4_y + 172), "Phase 3: An der Fräsmaschine", fill="#1E293B", font=font_body_b)
draw.text((card_x0 + 55, b4_y + 192), "Beim Rüsten VOR Start. Der Fräser wählt Parallelunterlagen\nmit Tunnel, damit der Bohrer ins Freie austritt.", fill="#475569", font=font_body)

# Speichern
out_dir = "c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/bilder"
out_path = os.path.join(out_dir, "cnc_bohrung_z_min_14_5mm_berechnung.jpg")
img.save(out_path, quality=95)
print("Gespeichert unter:", out_path)
