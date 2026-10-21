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
font_code = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 16)
font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 14)
font_dim = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 17)

# Hintergrund-Gitter (Subtiles technisches CAD-Raster)
for x in range(0, W, 40):
    draw.line([(x, 0), (x, H)], fill="#EDF2F7", width=1)
for y in range(0, H, 40):
    draw.line([(0, y), (W, y)], fill="#EDF2F7", width=1)

# Header Banner
draw.rectangle([(0, 0), (W, 95)], fill="#0F172A")
draw.text((40, 18), "ÜBUNG 3: EXAKTE BERECHNUNG DER DURCHGANGSBOHRUNG (Z-MIN = -14.500 mm)", fill="#FFFFFF", font=font_title)
draw.text((40, 58), "Warum reicht Z = -12.0 mm nicht aus? Geometrie aus Bauteildicke, Bohrerspitze (118°) und Durchbruch-Zugabe", fill="#94A3B8", font=font_subtitle)

# Trennlinie unter Header
draw.line([(0, 95), (W, 95)], fill="#2563EB", width=4)

# ==============================================================================
# LINKER BEREICH: CAD-SCHNITTZEICHNUNG (SCHNITTANSICHT A-A)
# ==============================================================================
cad_x0 = 60
cad_y0 = 130
cad_w = 780
cad_h = 870

draw.rounded_rectangle([(cad_x0, cad_y0), (cad_x0 + cad_w, cad_y0 + cad_h)], radius=12, fill="#FFFFFF", outline="#CBD5E1", width=2)
draw.rectangle([(cad_x0, cad_y0), (cad_x0 + cad_w, cad_y0 + 46)], fill="#F1F5F9")
draw.text((cad_x0 + 20, cad_y0 + 12), "CAD-SCHNITTANSICHT: SPIRALBOHRER D=5.0 mm DURCH ALUMINIUMPLATTE", fill="#1E293B", font=font_h3)
draw.line([(cad_x0, cad_y0 + 46), (cad_x0 + cad_w, cad_y0 + 46)], fill="#E2E8F0", width=1)

# Maßstab für Z-Achse im Diagramm:
# 1 mm physikalisch = 28 Pixel im Bild
scale_z = 28.0

# Horizontale Ebenen:
# Z = 0 (Oberkante): Y = 360
y_z0 = 360
y_z_plate_bottom = y_z0 + int(12.0 * scale_z)  # Z = -12 mm -> Y = 360 + 336 = 696
y_z_cyl_end = y_z_plate_bottom + int(1.0 * scale_z)  # Z = -13 mm -> Y = 696 + 28 = 724
y_z_tip = y_z_cyl_end + int(1.5 * scale_z)  # Z = -14.5 mm -> Y = 724 + 42 = 766

# Werkstück Geometrie im Schnitt:
# Werkstück reicht von X = 130 bis X = 770
wp_left = 140
wp_right = 760
hole_center_x = 420
hole_dia_px = int(5.0 * 22.0)  # optisch etwas breiter dargestellt für beste Lesbarkeit: 110 px
hole_left_x = hole_center_x - hole_dia_px // 2   # 420 - 55 = 365
hole_right_x = hole_center_x + hole_dia_px // 2  # 420 + 55 = 475

# Werkstück Material links & rechts der Bohrung
# Linker Materialblock
draw.rectangle([(wp_left, y_z0), (hole_left_x, y_z_plate_bottom)], fill="#E2E8F0", outline="#94A3B8", width=2)
# Rechter Materialblock
draw.rectangle([(hole_right_x, y_z0), (wp_right, y_z_plate_bottom)], fill="#E2E8F0", outline="#94A3B8", width=2)

# Schraffur (Hatching) für Metallwerkstück links
for d in range(wp_left, hole_left_x + 100, 24):
    x_start = d
    y_start = y_z0
    x_end = d - (y_z_plate_bottom - y_z0)
    y_end = y_z_plate_bottom
    # Schnittpunkte klemmen
    pts = []
    # Zeichne Schraffurlinie
    draw.line([(max(wp_left, x_end), min(y_end, y_z0 + (x_start - max(wp_left, x_end)))),
               (min(hole_left_x, x_start), y_z0)], fill="#CBD5E1", width=1)

# Schraffur rechts
for d in range(hole_right_x, wp_right + 100, 24):
    draw.line([(max(hole_right_x, d - 100), min(y_z_plate_bottom, y_z0 + 100)),
               (min(wp_right, d), y_z0)], fill="#CBD5E1", width=1)

# Text im Werkstück
draw.text((wp_left + 25, y_z0 + 140), "ALUMINIUMPLATTE\n(Dicke = 12.0 mm)", fill="#475569", font=font_h3)
draw.text((hole_right_x + 40, y_z0 + 140), "WERKSTOFF: ALMGSI0.5\n(Kunde: Flanschplatte)", fill="#475569", font=font_h3)

# ------------------------------------------------------------------------------
# PARALLELUNTERLAGEN & TUNNEL UNTER DEM BAUTEIL
# ------------------------------------------------------------------------------
# Linke Unterlage
par_h = 160
draw.rectangle([(wp_left, y_z_plate_bottom), (wp_left + 110, y_z_plate_bottom + par_h)], fill="#64748B", outline="#334155", width=2)
draw.text((wp_left + 12, y_z_plate_bottom + 65), "PARALLEL-\nUNTERLAGE", fill="#FFFFFF", font=font_badge)

# Rechte Unterlage
draw.rectangle([(wp_right - 110, y_z_plate_bottom), (wp_right, y_z_plate_bottom + par_h)], fill="#64748B", outline="#334155", width=2)
draw.text((wp_right - 102, y_z_plate_bottom + 65), "PARALLEL-\nUNTERLAGE", fill="#FFFFFF", font=font_badge)

# Schraubstock-Basis ganz unten
draw.rectangle([(wp_left - 30, y_z_plate_bottom + par_h), (wp_right + 30, y_z_plate_bottom + par_h + 35)], fill="#334155", outline="#1E293B", width=2)
draw.text((wp_left + 180, y_z_plate_bottom + par_h + 8), "MASCHINENSCHRAUBSTOCK-BODEN AUS GEHÄRTETEM STAHL", fill="#94A3B8", font=font_badge)

# Luft-Tunnel Kennzeichnung
tunnel_x1 = wp_left + 110
tunnel_x2 = wp_right - 110
draw.rectangle([(tunnel_x1 + 4, y_z_plate_bottom + 2), (tunnel_x2 - 4, y_z_plate_bottom + par_h - 2)], fill="#F8FAFC")
draw.line([(tunnel_x1, y_z_plate_bottom), (tunnel_x1, y_z_plate_bottom + par_h)], fill="#3B82F6", width=2)
draw.line([(tunnel_x2, y_z_plate_bottom), (tunnel_x2, y_z_plate_bottom + par_h)], fill="#3B82F6", width=2)

draw.text((hole_center_x - 110, y_z_plate_bottom + 95), "FREIER LUFT-TUNNEL\n(Hier tritt die Bohrerspitze gefahrlos aus)", fill="#2563EB", font=font_body_b)

# ------------------------------------------------------------------------------
# DER SPIRALBOHRER (T02 - Ø 5.0 mm)
# ------------------------------------------------------------------------------
drill_top_y = 190
# Werkzeugaufnahme / Schaft
draw.rectangle([(hole_center_x - 45, drill_top_y), (hole_center_x + 45, y_z0 - 70)], fill="#475569", outline="#1E293B", width=2)
draw.text((hole_center_x - 38, drill_top_y + 15), "WERKZEUGHALTER", fill="#E2E8F0", font=font_badge)

# Zylindrischer Bohrerschaft (Goldfarbene TiN-Beschichtung / Carbide)
drill_cyl_pts = [
    (hole_left_x + 6, y_z0 - 70),
    (hole_right_x - 6, y_z0 - 70),
    (hole_right_x - 6, y_z_cyl_end),
    (hole_left_x + 6, y_z_cyl_end)
]
draw.polygon(drill_cyl_pts, fill="#F59E0B", outline="#B45309", width=2)

# Spannuten / Spiralnuten (Flutes)
for y_flute in range(y_z0 - 50, y_z_cyl_end, 36):
    draw.arc([(hole_left_x + 8, y_flute), (hole_right_x - 8, y_flute + 28)], 0, 180, fill="#78350F", width=3)

# Bohrerspitze (118° Kegel) von y_z_cyl_end nach y_z_tip
drill_tip_pts = [
    (hole_left_x + 6, y_z_cyl_end),
    (hole_right_x - 6, y_z_cyl_end),
    (hole_center_x, y_z_tip)
]
draw.polygon(drill_tip_pts, fill="#D97706", outline="#78350F", width=2)
# Querschneide / Schneidkante
draw.line([(hole_left_x + 6, y_z_cyl_end), (hole_center_x, y_z_tip)], fill="#FEF3C7", width=2)
draw.line([(hole_right_x - 6, y_z_cyl_end), (hole_center_x, y_z_tip)], fill="#FEF3C7", width=2)

# Rote Markierung für die äußerste Spitze
draw.ellipse([(hole_center_x - 5, y_z_tip - 5), (hole_center_x + 5, y_z_tip + 5)], fill="#EF4444", outline="#991B1B", width=2)

# ------------------------------------------------------------------------------
# REFERENZ-EBENEN (Dotted & Solid Reference Lines)
# ------------------------------------------------------------------------------
def draw_ref_line(y, label, color, dash=True):
    if dash:
        for x in range(cad_x0 + 15, cad_x0 + cad_w - 15, 12):
            draw.line([(x, y), (x + 7, y)], fill=color, width=2)
    else:
        draw.line([(cad_x0 + 15, y), (cad_x0 + cad_w - 15, y)], fill=color, width=2)

# Z = 0 Ebene (Bauteil-Oberkante)
draw_ref_line(y_z0, "", "#2563EB", dash=False)
# Nullpunkt Symbol G54
draw.ellipse([(wp_left - 12, y_z0 - 12), (wp_left + 12, y_z0 + 12)], fill="#2563EB", outline="#1D4ED8", width=2)
draw.text((wp_left + 18, y_z0 - 24), "G54 NULLPUNKT (Z = 0.000 mm)", fill="#2563EB", font=font_h3)

# Z = -12.0 mm (Platten-Unterkante)
draw_ref_line(y_z_plate_bottom, "", "#64748B", dash=True)
draw.text((cad_x0 + 20, y_z_plate_bottom - 22), "Z = -12.000 mm (Bauteil-Unterkante)", fill="#475569", font=font_body_b)

# Z = -13.0 mm (Zylinder-Ende / Durchbruch)
draw_ref_line(y_z_cyl_end, "", "#059669", dash=True)
draw.text((cad_x0 + 20, y_z_cyl_end - 20), "Z = -13.000 mm (Voller Bohrerdurchmesser D=5 durch)", fill="#059669", font=font_body_b)

# Z = -14.5 mm (Z-MIN / Tiefster Punkt)
draw_ref_line(y_z_tip, "", "#DC2626", dash=False)
draw.text((cad_x0 + 20, y_z_tip + 8), "Z-MIN = -14.500 mm (Äußerste Bohrerspitze im Freiraum)", fill="#DC2626", font=font_h3)

# ------------------------------------------------------------------------------
# BEMASSUNGS-PFEILE LINKS (Die 3 Teilabschnitte)
# ------------------------------------------------------------------------------
dim_x = 220

def draw_dim_arrow(x, y1, y2, label, color, text_offset=12):
    # Vertikale Linie
    draw.line([(x, y1), (x, y2)], fill=color, width=2)
    # Begrenzungsstriche
    draw.line([(x - 8, y1), (x + 8, y1)], fill=color, width=2)
    draw.line([(x - 8, y2), (x + 8, y2)], fill=color, width=2)
    # Pfeilspitzen
    draw.polygon([(x, y1), (x - 4, y1 + 8), (x + 4, y1 + 8)], fill=color)
    draw.polygon([(x, y2), (x - 4, y2 - 8), (x + 4, y2 - 8)], fill=color)
    # Text
    ymid = (y1 + y2) // 2
    draw.text((x + text_offset, ymid - 10), label, fill=color, font=font_dim)

# 1. Bauteildicke 12.0 mm
draw_dim_arrow(300, y_z0, y_z_plate_bottom, "12.0 mm (Plattendicke)", "#1E293B")
# 2. Durchbruch 1.0 mm
draw_dim_arrow(300, y_z_plate_bottom, y_z_cyl_end, "1.0 mm (Überlauf)", "#059669")
# 3. Spitzenlänge 1.5 mm
draw_dim_arrow(300, y_z_cyl_end, y_z_tip, "1.5 mm (Bohrerspitze)", "#D97706")

# Gesammtmaß rechts (14.5 mm)
draw_dim_arrow(710, y_z0, y_z_tip, "GESAMT = 14.500 mm\n-> Z-MIN = -14.500 mm", "#DC2626", text_offset=-220)


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
draw.text((card_x0 + 35, b1_y + 12), "❌ WARUM REICHT Z = -12.0 mm BEIM DURCHBOHREN NICHT?", fill="#991B1B", font=font_h3)
draw.text((card_x0 + 35, b1_y + 44), 
          "* Würde der Bohrer bei Z = -12.0 mm stoppen, hätte nur die Spitze das Bauteil berührt.\n"
          "* Das Bohrloch an der Unterseite wäre noch trichterförmig verschlossen!\n"
          "* Der zylindrische Schaft (D = 5.0 mm) muss VOLLSTÄNDIG aus der Unterseite austreten,\n"
          "  damit eine Schraube oder ein Bolzen hindurchpasst.", fill="#7F1D1D", font=font_body)

# Block 2: Die 3 Komponenten der Rechnung
b2_y = b1_y + 145
draw.rounded_rectangle([(card_x0 + 20, b2_y), (card_x0 + card_w - 20, b2_y + 245)], radius=8, fill="#F8FAFC", outline="#E2E8F0", width=1)
draw.text((card_x0 + 35, b2_y + 12), "📐 DIE 3 TEIL-KOMPONENTEN DER Z-TIEFE:", fill="#1E293B", font=font_h3)

# 1. Bauteildicke
draw.text((card_x0 + 35, b2_y + 48), "1. Bauteildicke (h):", fill="#0F172A", font=font_body_b)
draw.text((card_x0 + 240, b2_y + 48), "= 12.0 mm", fill="#2563EB", font=font_body_b)
draw.text((card_x0 + 35, b2_y + 70), "   Vollmaterial der Aluminium-Flanschplatte von Z = 0 bis Z = -12.0 mm.", fill="#64748B", font=font_body)

# 2. Durchbruch-Zugabe
draw.text((card_x0 + 35, b2_y + 100), "2. Durchbruch-Zugabe:", fill="#0F172A", font=font_body_b)
draw.text((card_x0 + 240, b2_y + 100), "=  1.0 mm", fill="#059669", font=font_body_b)
draw.text((card_x0 + 35, b2_y + 122), "   Zylindrischer Überlauf ins Freie, damit an der Austrittskante kein Grat bleibt.", fill="#64748B", font=font_body)

# 3. Spitzenlänge Formel
draw.text((card_x0 + 35, b2_y + 152), "3. Bohrerspitzen-Länge (l):", fill="#0F172A", font=font_body_b)
draw.text((card_x0 + 240, b2_y + 152), "=  1.5 mm  (bei D = 5.0 mm & Spitzenwinkel 118°)", fill="#D97706", font=font_body_b)
draw.text((card_x0 + 35, b2_y + 175), "   Exakte Formel:  l = d / (2 * tan(118° / 2)) = 5.0 / (2 * 1.60) = 1.56 mm", fill="#64748B", font=font_code)
draw.text((card_x0 + 35, b2_y + 200), "   Werkstatt-Faustformel:  l ≈ 0.3 * d  =  0.3 * 5.0 mm  =  1.5 mm", fill="#B45309", font=font_body_b)

# Block 3: Die Gesamtrechnung
b3_y = b2_y + 260
draw.rounded_rectangle([(card_x0 + 20, b3_y), (card_x0 + card_w - 20, b3_y + 120)], radius=8, fill="#EFF6FF", outline="#93C5FD", width=2)
draw.text((card_x0 + 35, b3_y + 12), "✅ DIE GESAMTRECHNUNG FÜR DEN G-CODE:", fill="#1D4ED8", font=font_h3)
draw.text((card_x0 + 35, b3_y + 44), 
          "Gesamttiefe = Bauteildicke (12.0) + Durchbruch (1.0) + Spitze (1.5) = 14.5 mm\n\n"
          "Da Z = 0 oben liegt und es nach unten ins Material geht:\n"
          "--> Resultierende Koordinate:  Z = -14.500 mm  (Z-MIN)", fill="#1E3A8A", font=font_body_b)

# Block 4: Wann wird dieser Wert ermittelt?
b4_y = b3_y + 135
draw.rounded_rectangle([(card_x0 + 20, b4_y), (card_x0 + card_w - 20, b4_y + 215)], radius=8, fill="#F8FAFC", outline="#E2E8F0", width=1)
draw.text((card_x0 + 35, b4_y + 12), "⏱️ WANN WIRD DIESER WERT ERMITTELT?", fill="#0F172A", font=font_h3)

steps = [
    ("Phase 1: Im CAM (Fusion 360)", "Beim Klick auf 'Generieren'. Fusion berechnet Bahnen\nund speichert Z-Min intern in section.getGlobalZRange().", "#2563EB"),
    ("Phase 2: Im Postprozessor", "Beim Klick auf 'Posten'. getToolMinimumZ() liest -14.5 mm\naus und schreibt: (T02 | BOHRER | Z-MIN=-14.500MM).", "#D97706"),
    ("Phase 3: An der Fräsmaschine", "Beim Rüsten VOR Start. Der Fräser wählt Parallelunterlagen\nmit Tunnel, damit der Bohrer ins Freie austritt.", "#059669")
]

step_y = b4_y + 42
for title, desc, color in steps:
    draw.ellipse([(card_x0 + 35, step_y + 3), (card_x0 + 47, step_y + 15)], fill=color)
    draw.text((card_x0 + 55, step_y), title, fill=color, font=font_body_b)
    draw.text((card_x0 + 55, step_y + 20), desc, fill="#475569", font=font_body)
    step_y += 58

# Speichern
out_dir = "c:/Projekte/CNC/docs/bilder"
os.makedirs(out_dir, exist_ok=True)
out_path = os.path.join(out_dir, "cnc_bohrung_z_min_14_5mm_berechnung.jpg")
img.save(out_path, quality=95)
print("Gespeichert unter:", out_path)

# Kopieren in Artifacts
artifact_dir = r"C:\Users\Administrador\.gemini\antigravity\brain\ac827183-5a60-427d-8f0a-24b569bcc77f"
if os.path.exists(artifact_dir):
    artifact_path = os.path.join(artifact_dir, "cnc_bohrung_z_min_14_5mm_berechnung.jpg")
    shutil.copyfile(out_path, artifact_path)
    print("In Artifacts kopiert:", artifact_path)
