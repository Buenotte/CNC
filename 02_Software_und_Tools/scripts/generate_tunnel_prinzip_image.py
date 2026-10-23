"""
Generiert die präzise technische CAD-Grafik:
'Das Tunnel-Prinzip in der CNC-Praxis (Durchbohren ohne Maschinencrash)'
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = 1440
H = 820
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
draw.text((40, 22), "Das Tunnel-Prinzip in der CNC-Praxis (Durchbohren ohne Maschinencrash)", fill="#0F172A", font=font_title)
draw.text((40, 58), "Querschnitt: Wie 2 schmale Parallelunterlagen einen Lufttunnel unter dem Bauteil schaffen", fill="#64748B", font=font_subtitle)

# Geometrie
# Maßstab: 12 px pro mm
scale = 12.0

wp_x0, wp_x1 = 400, 880
wp_w = wp_x1 - wp_x0  # 480 px

y_z0 = 200
y_z_wp_bot = y_z0 + int(12.0 * scale)    # Z = -12.0 mm -> 200 + 144 = 344
y_z_tip = y_z_wp_bot + int(2.5 * scale)  # Z = -14.5 mm -> 344 + 30 = 374
y_z_bed = y_z_wp_bot + int(12.5 * scale) # Z = -24.5 mm -> 344 + 150 = 494

jaw_w = 140
# Spannbacken links & rechts (grau)
draw.rectangle([(wp_x0 - jaw_w, y_z0 + 40), (wp_x0, y_z_bed + 30)], fill="#334155", outline="#1E293B", width=2)
draw.rectangle([(wp_x1, y_z0 + 40), (wp_x1 + jaw_w, y_z_bed + 30)], fill="#334155", outline="#1E293B", width=2)

draw.text((wp_x0 - jaw_w // 2, y_z0 + 95), "STAHLBACKE", fill="#FFFFFF", font=font_h3, anchor="mm")
draw.text((wp_x0 - jaw_w // 2, y_z0 + 120), "Spannbacke links", fill="#94A3B8", font=font_body, anchor="mm")

draw.text((wp_x1 + jaw_w // 2, y_z0 + 95), "STAHLBACKE", fill="#FFFFFF", font=font_h3, anchor="mm")
draw.text((wp_x1 + jaw_w // 2, y_z0 + 120), "Spannbacke rechts", fill="#94A3B8", font=font_body, anchor="mm")

# Aluminium Werkstück (Z = 0 bis Z = -12 mm)
draw.rectangle([(wp_x0, y_z0), (wp_x1, y_z_wp_bot)], fill="#DBEAFE", outline="#93C5FD", width=2)

# Parallelunterlagen unter dem Werkstück (links und rechts)
par_w = 80
draw.rectangle([(wp_x0, y_z_wp_bot), (wp_x0 + par_w, y_z_bed)], fill="#64748B", outline="#334155", width=2)
draw.text((wp_x0 + par_w // 2, (y_z_wp_bot + y_z_bed) // 2), "Parallel-\nunterlage\n(Links)", fill="#FFFFFF", font=font_badge, anchor="mm")

draw.rectangle([(wp_x1 - par_w, y_z_wp_bot), (wp_x1, y_z_bed)], fill="#64748B", outline="#334155", width=2)
draw.text((wp_x1 - par_w // 2, (y_z_wp_bot + y_z_bed) // 2), "Parallel-\nunterlage\n(Rechts)", fill="#FFFFFF", font=font_badge, anchor="mm")

# Schraubstock-Bett ganz unten
draw.rectangle([(wp_x0 - jaw_w, y_z_bed), (wp_x1 + jaw_w, y_z_bed + 50)], fill="#1E293B", outline="#0F172A", width=2)
draw.text(((wp_x0 + wp_x1) // 2, y_z_bed + 18), "SCHRAUBSTOCK-BODEN (Bett aus Gusseisen / Stahl)", fill="#FFFFFF", font=font_h3, anchor="mm")
draw.text(((wp_x0 + wp_x1) // 2, y_z_bed + 38), "Darf niemals vom Bohrer getroffen werden!", fill="#FCA5A5", font=font_badge, anchor="mm")

# Freier Luft-Tunnel im Zentrum
tunnel_x0 = wp_x0 + par_w
tunnel_x1 = wp_x1 - par_w
draw.rectangle([(tunnel_x0 + 2, y_z_wp_bot + 2), (tunnel_x1 - 2, y_z_bed - 2)], fill="#F0FDF4", outline="#22C55E", width=2)

draw.text(((tunnel_x0 + tunnel_x1) // 2, (y_z_wp_bot + y_z_bed) // 2 - 12), "OFFENER LUFT-TUNNEL", fill="#15803D", font=font_h3, anchor="mm")
draw.text(((tunnel_x0 + tunnel_x1) // 2, (y_z_wp_bot + y_z_bed) // 2 + 12), "(Vollkommen freier Freiraum - kein Metall!)", fill="#166534", font=font_body, anchor="mm")
draw.text(((tunnel_x0 + tunnel_x1) // 2, (y_z_wp_bot + y_z_bed) // 2 + 34), "Hier kann kein Werkzeug crashen!", fill="#15803D", font=font_badge, anchor="mm")

# Spiralbohrer T02 im Zentrum
drill_center_x = (wp_x0 + wp_x1) // 2
drill_w = 42
drill_x0 = drill_center_x - drill_w // 2
drill_x1 = drill_center_x + drill_w // 2
drill_y0 = 105
drill_cyl_end = y_z_wp_bot + int(1.0 * scale) # 1 mm Überlauf

draw.rectangle([(drill_x0, drill_y0), (drill_x1, drill_cyl_end)], fill="#F59E0B", outline="#B45309", width=2)
for fy in range(drill_y0 + 15, drill_cyl_end, 20):
    draw.line([(drill_x0 + 4, fy), (drill_x1 - 4, fy - 10)], fill="#78350F", width=2)

# Bohrerspitze
draw.polygon([(drill_x0, drill_cyl_end), (drill_x1, drill_cyl_end), (drill_center_x, y_z_tip)], fill="#D97706", outline="#78350F", width=2)
draw.line([(drill_x0, drill_cyl_end), (drill_center_x, y_z_tip)], fill="#FEF3C7", width=2)
draw.line([(drill_x1, drill_cyl_end), (drill_center_x, y_z_tip)], fill="#FEF3C7", width=2)

draw.text((drill_center_x, drill_y0 - 16), "SPIRALBOHRER T02 (D=5.0 mm)", fill="#B45309", font=font_badge, anchor="mm")

# Text im Aluminium Werkstück (links und rechts vom Bohrer, damit kein Text überlappt!)
draw.text(((wp_x0 + drill_x0) // 2, (y_z0 + y_z_wp_bot) // 2), "ALUMINIUM-BAUTEIL", fill="#1E40AF", font=font_h3, anchor="mm")
draw.text(((drill_x1 + wp_x1) // 2, (y_z0 + y_z_wp_bot) // 2), "(Dicke h = 12.0 mm)", fill="#1E40AF", font=font_h3, anchor="mm")

# Callout Box links: KEIN CRASH! (x = 30..235)
draw.rounded_rectangle([(30, y_z_wp_bot - 10), (235, y_z_wp_bot + 105)], radius=8, fill="#F0FDF4", outline="#22C55E", width=2)
draw.text((45, y_z_wp_bot + 8), "KEIN CRASH!", fill="#15803D", font=font_h3)
draw.text((45, y_z_wp_bot + 36), "Bohrerspitze sticht 2.5 mm\nsicher in die leere Luft\ndes Tunnels!", fill="#166534", font=font_body)
draw.line([(235, y_z_wp_bot + 50), (tunnel_x0 + 30, y_z_tip)], fill="#22C55E", width=2)

# Referenz-Linien rechts
ref_line_end = wp_x1 + jaw_w + 25
text_start = ref_line_end + 15

draw.line([(wp_x0, y_z0), (ref_line_end, y_z0)], fill="#2563EB", width=2)
draw.text((text_start, y_z0), "Z = 0.000 mm (Oberkante Bauteil / Part Top)", fill="#2563EB", font=font_body_b, anchor="lm")

draw.line([(wp_x0, y_z_wp_bot), (ref_line_end, y_z_wp_bot)], fill="#475569", width=2)
draw.text((text_start, y_z_wp_bot), "Z = -12.0 mm (Unterseite Werkstück / Part Bottom)", fill="#475569", font=font_body_b, anchor="lm")

draw.line([(drill_center_x, y_z_tip), (ref_line_end, y_z_tip)], fill="#16A34A", width=2)
draw.text((text_start, y_z_tip), "Z-MIN = -14.5 mm (Bohrerspitze im Luft-Tunnel)", fill="#16A34A", font=font_body_b, anchor="lm")

# Sicherheitsabstand Klammer
draw.line([(ref_line_end - 15, y_z_tip), (ref_line_end - 15, y_z_bed)], fill="#0284C7", width=2)
draw.line([(ref_line_end - 20, y_z_tip), (ref_line_end - 10, y_z_tip)], fill="#0284C7", width=2)
draw.line([(ref_line_end - 20, y_z_bed), (ref_line_end - 10, y_z_bed)], fill="#0284C7", width=2)
draw.text((text_start, (y_z_tip + y_z_bed) // 2), "10.0 mm Sicherheitsabstand zum Schraubstock-Bett", fill="#0284C7", font=font_body_b, anchor="lm")

draw.line([(wp_x0 - jaw_w, y_z_bed), (ref_line_end, y_z_bed)], fill="#DC2626", width=2)
draw.text((text_start, y_z_bed), "Z = -24.5 mm (Schraubstock-Bett aus massivem Stahl)", fill="#DC2626", font=font_body_b, anchor="lm")

# Untere Erklärungskarte
draw.rounded_rectangle([(30, H - 150), (W - 30, H - 25)], radius=8, fill="#FFFFFF", outline="#CBD5E1", width=1)
draw.text((50, H - 135), "Warum das Tunnel-Prinzip in der CNC-Industrie Standard ist:", fill="#0F172A", font=font_h3)
draw.text((50, H - 105), "1. Durch zwei schmale Parallelunterlagen ganz links und rechts bleibt die gesamte Mitte frei von Metall.", fill="#334155", font=font_body)
draw.text((50, H - 80), "2. Der Bohrer bricht unten komplett aus dem Aluminium durch, damit das Loch vollkommen frei und sauber wird.", fill="#334155", font=font_body)
draw.text((50, H - 55), "3. Dein Z-MIN im Postprozessor (-14.5 mm) garantiert, dass noch 10 mm Sicherheitsluft bis zum massiven Boden bleiben!", fill="#15803D", font=font_body_b)

# Speichern
out_file = "c:/Projekte/CNC/03_Fachdokumentation_und_Wissen/docs/bilder/cnc_tunnel_prinzip_parallelunterlagen.jpg"
img.save(out_file, quality=95)
print("Gespeichert:", out_file)
