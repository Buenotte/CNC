"""
Generiert die präzise technische Schnittansicht:
'Warum knallt der Fräser bei Z = -10 mm in den Schraubstock?'
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = 1440
H = 800
img = Image.new("RGB", (W, H), "#F8FAFC")
draw = ImageDraw.Draw(img)

# Schriftarten
font_title = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 26)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 17)
font_h3 = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 18)
font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 16)
font_body_b = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 16)
font_badge = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 14)

# Hintergrund-Gitter
for x in range(0, W, 40):
    draw.line([(x, 0), (x, H)], fill="#EDF2F7", width=1)
for y in range(0, H, 40):
    draw.line([(0, y), (W, y)], fill="#EDF2F7", width=1)

# Header
draw.text((40, 22), "Schnittansicht: Warum knallt der Fräser bei Z = -10 mm in den Schraubstock?", fill="#0F172A", font=font_title)
draw.text((40, 58), "Seitenansicht (Querschnitt) durch das Werkstück im Maschinenschraubstock", fill="#64748B", font=font_subtitle)

# Geometrie
wp_x0, wp_x1 = 440, 840
y_z0 = 220
y_z_jaw = y_z0 + 150       # Z = -10.0 mm (15 px/mm)
y_z_part_bot = y_z0 + 310   # Z = -20.6 mm
y_z_pocket = y_z0 + 75     # Z = -5.0 mm
y_z_crash = y_z_jaw + 30   # Z = -12.0 mm (2 mm Crash)

jaw_w = 150
# Linke Backe (x = 290..440)
draw.rectangle([(wp_x0 - jaw_w, y_z_jaw), (wp_x0, y_z_part_bot + 40)], fill="#334155", outline="#1E293B", width=2)
# Rechte Backe (x = 840..990)
draw.rectangle([(wp_x1, y_z_jaw), (wp_x1 + jaw_w, y_z_part_bot + 40)], fill="#334155", outline="#1E293B", width=2)

# Gehärtete Stahloberfläche oben (rot)
draw.rectangle([(wp_x0 - jaw_w, y_z_jaw - 6), (wp_x0, y_z_jaw)], fill="#EF4444")
draw.rectangle([(wp_x1, y_z_jaw - 6), (wp_x1 + jaw_w, y_z_jaw)], fill="#EF4444")

# Werkstück Aluminium
draw.rectangle([(wp_x0, y_z0), (wp_x1, y_z_part_bot + 20)], fill="#E2E8F0", outline="#94A3B8", width=2)
# Freier Überstand (hellblau)
draw.rectangle([(wp_x0, y_z0), (wp_x1, y_z_jaw)], fill="#DBEAFE", outline="#93C5FD", width=1)

# Beschriftungen in Werkstück & Backen
draw.text(((wp_x0 + wp_x1) // 2, y_z0 + 38), "ALUMINIUM (10 mm frei über Backe)", fill="#1E40AF", font=font_h3, anchor="mm")
draw.text(((wp_x0 + wp_x1) // 2, (y_z_jaw + y_z_part_bot) // 2), "ALUMINIUM (eingespannt)", fill="#475569", font=font_h3, anchor="mm")

draw.text((wp_x0 - jaw_w // 2, y_z_jaw + 65), "STAHLBACKE\n(Schraubstock)", fill="#FFFFFF", font=font_h3, anchor="mm")
draw.text((wp_x0 - jaw_w // 2, y_z_jaw + 115), "Gehärteter\nWerkzeugstahl", fill="#94A3B8", font=font_body, anchor="mm")

draw.text((wp_x1 + jaw_w // 2, y_z_jaw + 65), "STAHLBACKE", fill="#FFFFFF", font=font_h3, anchor="mm")
draw.text((wp_x1 + jaw_w // 2, y_z_jaw + 95), "Feste Spannbacke", fill="#94A3B8", font=font_body, anchor="mm")

# Schaftfräser D=10 mm links (x = 394..440)
mill_w = 46
mill_x1 = wp_x0
mill_x0 = mill_x1 - mill_w
mill_y0 = 115
mill_y1 = y_z_crash

draw.rectangle([(mill_x0, mill_y0), (mill_x1, mill_y1)], fill="#F59E0B", outline="#B45309", width=2)
for fy in range(mill_y0 + 20, mill_y1, 26):
    draw.line([(mill_x0 + 4, fy), (mill_x1 - 4, fy - 14)], fill="#78350F", width=2)

draw.text(((mill_x0 + mill_x1) // 2, mill_y0 - 18), "FRÄSER (D=10 mm)", fill="#B45309", font=font_badge, anchor="mm")

# Crash-Überlappung (2 mm im Stahl!)
draw.rectangle([(mill_x0, y_z_jaw), (mill_x1, y_z_crash)], fill="#DC2626", outline="#FEF08A", width=2)

# Crash Callout Box links (x = 30..250)
draw.rounded_rectangle([(30, y_z_jaw + 40), (250, y_z_jaw + 160)], radius=8, fill="#FEF2F2", outline="#DC2626", width=2)
draw.text((45, y_z_jaw + 55), "BAMM! CRASH!", fill="#DC2626", font=font_h3)
draw.text((45, y_z_jaw + 85), "Fräser rammt 2 mm tief\nin die gehärtete\nStahlbacke!", fill="#7F1D1D", font=font_body)
draw.line([(250, y_z_jaw + 85), (mill_x0 + 5, y_z_jaw + 15)], fill="#DC2626", width=2)

# Referenz-Linien rechts
ref_line_end = wp_x1 + jaw_w + 30  # 1020
text_start = ref_line_end + 15     # 1035

# 1. Z = 0.000 mm
draw.line([(wp_x0, y_z0), (ref_line_end, y_z0)], fill="#2563EB", width=2)
draw.text((text_start, y_z0), "Z = 0.000 mm (Bauteil-Oberkante / Part Surface)", fill="#2563EB", font=font_body_b, anchor="lm")

# 2. Z = -5.0 mm
draw.line([(wp_x0, y_z_pocket), (ref_line_end, y_z_pocket)], fill="#16A34A", width=2)
draw.text((text_start, y_z_pocket), "Z = -5.0 mm (Sichere Frästiefe Tasche / Safe Pocket)", fill="#16A34A", font=font_body_b, anchor="lm")

# 3. Z = -10.0 mm
draw.line([(wp_x0 - jaw_w, y_z_jaw), (ref_line_end, y_z_jaw)], fill="#DC2626", width=2)
draw.text((text_start, y_z_jaw), "Z = -10.0 mm (OBERKANTE SCHRAUBSTOCK-BACKEN)", fill="#DC2626", font=font_body_b, anchor="lm")

# 4. Z = -12.0 mm
draw.line([(mill_x0, y_z_crash), (ref_line_end, y_z_crash)], fill="#991B1B", width=2)
draw.text((text_start, y_z_crash), "Z = -12.0 mm (Z-MIN: Werkzeug taucht 2 mm in Backe!)", fill="#991B1B", font=font_body_b, anchor="lm")

# Crash Klammer bei x = ref_line_end - 15
draw.line([(ref_line_end - 15, y_z_jaw), (ref_line_end - 15, y_z_crash)], fill="#DC2626", width=2)
draw.line([(ref_line_end - 20, y_z_jaw), (ref_line_end - 10, y_z_jaw)], fill="#DC2626", width=2)
draw.line([(ref_line_end - 20, y_z_crash), (ref_line_end - 10, y_z_crash)], fill="#DC2626", width=2)
draw.text((ref_line_end - 25, (y_z_jaw + y_z_crash) // 2), "2 mm CRASH", fill="#DC2626", font=font_badge, anchor="rm")

# Untere Erklärungskarte
draw.rounded_rectangle([(30, H - 150), (W - 30, H - 25)], radius=8, fill="#FFFFFF", outline="#CBD5E1", width=1)
draw.text((50, H - 135), "Das Geheimnis einfach erklärt:", fill="#0F172A", font=font_h3)
draw.text((50, H - 105), "1. Vom Bauteil-Deckel (Z = 0) bis zur Oberkante der Stahlbacke sind es genau 10 mm freies Aluminium.", fill="#334155", font=font_body)
draw.text((50, H - 75), "2. Fährt der Fräser auf Z = -12 mm um die Außenkontur, schneidet er 10 mm Alu - und rammt 2 mm tief in den massiven Stahl der Backe!", fill="#DC2626", font=font_body_b)

# Speichern
out_file = "c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/bilder/cnc_crash_schnitt_erklaerung.jpg"
img.save(out_file, quality=95)
print("Gespeichert:", out_file)
