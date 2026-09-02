import math
import os

out_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\static\images\diagrams"
FONT = "font-family=\"'Outfit', 'Segoe UI', 'Noto Sans Telugu', sans-serif\""

def save_svg(name, svg_content):
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Generated {name}")

def draw_dual_chart(patam_name, title, sq_highlight_map, circle_highlight_map, sq_label_map={}, circle_label_map={}):
    # Width 750, Height 420
    # Left: Square 4x4, Right: Circle 12 sectors
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 430" width="100%" height="100%" {FONT}>',
           '<defs><linearGradient id="bgDual" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#020617"/></linearGradient></defs>',
           '<rect width="760" height="430" fill="url(#bgDual)" rx="18" stroke="rgba(255,255,255,0.1)"/>']
    
    # Left: Square Grid (X: 40..340, Y: 40..340) -> size 300x300, cell 75x75
    sq_x, sq_y, cell_size = 40, 45, 75
    b_nums = [
        [12, 1, 2, 3],
        [11, 0, 0, 4],
        [10, 0, 0, 5],
        [9, 8, 7, 6]
    ]
    
    svg.append(f'<rect x="{sq_x}" y="{sq_y}" width="300" height="300" fill="#090d16" stroke="#475569" stroke-width="2"/>')
    for r in range(4):
        for c in range(4):
            num = b_nums[r][c]
            x = sq_x + c * cell_size
            y = sq_y + r * cell_size
            if num > 0:
                bg = sq_highlight_map.get(num, "#1e293b")
                bd = "#fbbf24" if num in sq_highlight_map else "#334155"
                svg.append(f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" fill="{bg}" stroke="{bd}" stroke-width="1.5"/>')
                # House number outside/corner
                svg.append(f'<text x="{x+6}" y="{y+14}" fill="#94a3b8" font-size="11" font-weight="700">{num}</text>')
                # Label text
                if num in sq_label_map:
                    lines = sq_label_map[num].split("\n")
                    start_y = y + 25 + (3 - len(lines)) * 4
                    for idx, line in enumerate(lines):
                        svg.append(f'<text x="{x + cell_size/2}" y="{start_y + idx*13}" fill="#ffffff" font-size="10.5" font-weight="800" text-anchor="middle">{line}</text>')
            elif r == 1 and c == 1:
                svg.append(f'<rect x="{x}" y="{y}" width="{cell_size*2}" height="{cell_size*2}" fill="#020617" stroke="#475569" stroke-width="1.5" stroke-dasharray="4 4"/>')
                svg.append(f'<text x="{x + cell_size}" y="{y + cell_size + 4}" fill="#fbbf24" font-size="15" font-weight="900" text-anchor="middle">కర్మపత్రము</text>')

    # Right: Circular Wheel (CX: 570, CY: 195, R: 150)
    cx, cy, r = 570, 195, 150
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#090d16" stroke="#475569" stroke-width="2.5"/>')
    for i in range(12):
        num = i + 1
        a1 = math.radians(i * 30 - 90)
        a2 = math.radians((i + 1) * 30 - 90)
        mid = math.radians(i * 30 + 15 - 90)
        
        x1 = cx + r * math.cos(a1)
        y1 = cy + r * math.sin(a1)
        x2 = cx + r * math.cos(a2)
        y2 = cy + r * math.sin(a2)
        
        bg = circle_highlight_map.get(num, "#1e293b")
        svg.append(f'<path d="M {cx} {cy} L {x1} {y1} A {r} {r} 0 0 1 {x2} {y2} Z" fill="{bg}" stroke="#334155" stroke-width="1.5"/>')
        
        # Number on outer rim
        num_x = cx + (r * 1.15) * math.cos(mid)
        num_y = cy + (r * 1.15) * math.sin(mid)
        svg.append(f'<text x="{num_x}" y="{num_y+4}" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">{num}</text>')
        
        # Sector label
        if num in circle_label_map:
            tx = cx + (r * 0.65) * math.cos(mid)
            ty = cy + (r * 0.65) * math.sin(mid)
            lines = circle_label_map[num].split("\n")
            start_y = ty - (len(lines)-1)*6
            for idx, line in enumerate(lines):
                svg.append(f'<text x="{tx}" y="{start_y + idx*12}" fill="#ffffff" font-size="9.5" font-weight="800" text-anchor="middle">{line}</text>')

    # Bottom Title
    svg.append(f'<text x="380" y="395" fill="#f8fafc" font-size="16" font-weight="900" text-anchor="middle">{title}</text>')
    svg.append('</svg>')
    save_svg(patam_name, "\n".join(svg))

# --- 37. Patam 37: 4th Kendra ---
draw_dual_chart(
    "patam_37_kendra_4.svg",
    "37వ పటము. నాల్గవ స్థానము కేంద్రము (అంగీ)",
    {4: "#f59e0b", 1: "#059669", 7: "#dc2626"},
    {4: "#f59e0b", 1: "#059669", 7: "#dc2626"},
    {4: "కేంద్రం\n(స్థూల ఆస్తి)", 1: "శరీరం", 7: "భార్య"},
    {4: "కేంద్రం\n(స్థూల)", 1: "శరీరం", 7: "భార్య"}
)

# --- 38. Patam 38: 10th Kendra ---
draw_dual_chart(
    "patam_38_kendra_10.svg",
    "38వ పటము. పదవ స్థానము కేంద్రము (అర్ధాంగి)",
    {10: "#f59e0b", 1: "#059669", 7: "#dc2626"},
    {10: "#f59e0b", 1: "#059669", 7: "#dc2626"},
    {10: "కేంద్రం\n(కీర్తి)", 1: "శరీరం", 7: "భార్య"},
    {10: "కేంద్రం\n(కీర్తి)", 1: "శరీరం", 7: "భార్య"}
)

# --- 39. Patam 39: Trikonas Geometry ---
def gen_patam_39():
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 430" width="100%" height="100%" {FONT}>',
           '<defs><linearGradient id="bg39" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#020617"/></linearGradient></defs>',
           '<rect width="760" height="430" fill="url(#bg39)" rx="18" stroke="rgba(255,255,255,0.1)"/>']
    
    # Left square with triangle connecting 1, 5, 9
    sq_x, sq_y, cs = 40, 45, 75
    svg.append(f'<rect x="{sq_x}" y="{sq_y}" width="300" height="300" fill="#090d16" stroke="#475569" stroke-width="2"/>')
    b_nums = [[12, 1, 2, 3], [11, 0, 0, 4], [10, 0, 0, 5], [9, 8, 7, 6]]
    centers = {}
    for r in range(4):
        for c in range(4):
            num = b_nums[r][c]
            x = sq_x + c * cs
            y = sq_y + r * cs
            if num > 0:
                svg.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>')
                svg.append(f'<text x="{x+6}" y="{y+14}" fill="#94a3b8" font-size="11" font-weight="700">{num}</text>')
                centers[num] = (x + cs/2, y + cs/2)
                
    # Triangle 1 -> 5 -> 9
    p1 = centers[1]; p5 = centers[5]; p9 = centers[9]
    svg.append(f'<polygon points="{p1[0]},{p1[1]} {p5[0]},{p5[1]} {p9[0]},{p9[1]}" fill="#10b981" fill-opacity="0.25" stroke="#10b981" stroke-width="3"/>')
    
    # Right circle with triangles
    cx, cy, r = 570, 195, 150
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#090d16" stroke="#475569" stroke-width="2"/>')
    c_pts = {}
    for i in range(12):
        num = i + 1
        mid = math.radians(i * 30 + 15 - 90)
        px = cx + r * math.cos(mid)
        py = cy + r * math.sin(mid)
        c_pts[num] = (px, py)
        # Sector line
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + r*math.cos(math.radians(i*30-90))}" y2="{cy + r*math.sin(math.radians(i*30-90))}" stroke="#334155"/>')
        # Number
        nx = cx + (r * 1.15) * math.cos(mid)
        ny = cy + (r * 1.15) * math.sin(mid)
        svg.append(f'<text x="{nx}" y="{ny+4}" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">{num}</text>')
        
    t1 = c_pts[1]; t5 = c_pts[5]; t9 = c_pts[9]
    svg.append(f'<polygon points="{t1[0]},{t1[1]} {t5[0]},{t5[1]} {t9[0]},{t9[1]}" fill="#10b981" fill-opacity="0.25" stroke="#10b981" stroke-width="3"/>')
    
    svg.append('<text x="380" y="395" fill="#f8fafc" font-size="16" font-weight="900" text-anchor="middle">39వ చిత్రపటము. కోణముల త్రికోణాకృతి (1, 5, 9)</text>')
    svg.append('</svg>')
    save_svg("patam_39_trikonas_geometry.svg", "\n".join(svg))

gen_patam_39()

# --- 40. Patam 40: Mitra Konas & Shatru Konas ---
def gen_patam_40():
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 760 430" width="100%" height="100%" {FONT}>',
           '<defs><linearGradient id="bg40" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#020617"/></linearGradient></defs>',
           '<rect width="760" height="430" fill="url(#bg40)" rx="18" stroke="rgba(255,255,255,0.1)"/>']
    
    # Left Circle: Mitra Konas (1, 5, 9)
    cx1, cy1, r = 210, 190, 140
    svg.append(f'<circle cx="{cx1}" cy="{cy1}" r="{r}" fill="#090d16" stroke="#10b981" stroke-width="2.5"/>')
    pts1 = {}
    for i in range(12):
        num = i + 1
        mid = math.radians(i * 30 + 15 - 90)
        px = cx1 + r * math.cos(mid)
        py = cy1 + r * math.sin(mid)
        pts1[num] = (px, py)
        nx = cx1 + (r * 1.15) * math.cos(mid)
        ny = cy1 + (r * 1.15) * math.sin(mid)
        svg.append(f'<text x="{nx}" y="{ny+4}" fill="#34d399" font-size="12" font-weight="800" text-anchor="middle">{num}</text>')
        svg.append(f'<line x1="{cx1}" y1="{cy1}" x2="{cx1 + r*math.cos(math.radians(i*30-90))}" y2="{cy1 + r*math.sin(math.radians(i*30-90))}" stroke="#334155"/>')
    p1 = pts1[1]; p5 = pts1[5]; p9 = pts1[9]
    svg.append(f'<polygon points="{p1[0]},{p1[1]} {p5[0]},{p5[1]} {p9[0]},{p9[1]}" fill="#10b981" fill-opacity="0.3" stroke="#10b981" stroke-width="3"/>')
    svg.append(f'<text x="{cx1}" y="365" fill="#34d399" font-size="15" font-weight="900" text-anchor="middle">మిత్రస్థాన కోణములు (1, 5, 9)</text>')
    
    # Right Circle: Shatru Konas (3, 7, 11)
    cx2, cy2 = 550, 190
    svg.append(f'<circle cx="{cx2}" cy="{cy2}" r="{r}" fill="#090d16" stroke="#ef4444" stroke-width="2.5"/>')
    pts2 = {}
    for i in range(12):
        num = i + 1
        mid = math.radians(i * 30 + 15 - 90)
        px = cx2 + r * math.cos(mid)
        py = cy2 + r * math.sin(mid)
        pts2[num] = (px, py)
        nx = cx2 + (r * 1.15) * math.cos(mid)
        ny = cy2 + (r * 1.15) * math.sin(mid)
        svg.append(f'<text x="{nx}" y="{ny+4}" fill="#f87171" font-size="12" font-weight="800" text-anchor="middle">{num}</text>')
        svg.append(f'<line x1="{cx2}" y1="{cy2}" x2="{cx2 + r*math.cos(math.radians(i*30-90))}" y2="{cy2 + r*math.sin(math.radians(i*30-90))}" stroke="#334155"/>')
    s3 = pts2[3]; s7 = pts2[7]; s11 = pts2[11]
    svg.append(f'<polygon points="{s3[0]},{s3[1]} {s7[0]},{s7[1]} {s11[0]},{s11[1]}" fill="#ef4444" fill-opacity="0.3" stroke="#ef4444" stroke-width="3"/>')
    svg.append(f'<text x="{cx2}" y="365" fill="#f87171" font-size="15" font-weight="900" text-anchor="middle">శత్రుస్థాన కోణములు (3, 7, 11)</text>')

    svg.append('<text x="380" y="405" fill="#f8fafc" font-size="16" font-weight="900" text-anchor="middle">40వ చిత్రపటము (మిత్ర & శత్రు కోణములు)</text>')
    svg.append('</svg>')
    save_svg("patam_40_mitra_shatru_konas.svg", "\n".join(svg))

gen_patam_40()

# --- 41. Patam 41: Karmapatram (Punya, Papa, Mixed) ---
draw_dual_chart(
    "patam_41_karmapatram_punya_papa.svg",
    "41వ చిత్రపటము. కర్మపత్రము (పుణ్యము, పాపము, పాపపుణ్యముల స్థానములు)",
    {1: "#065f46", 5: "#065f46", 9: "#065f46", 3: "#991b1b", 7: "#991b1b", 11: "#991b1b", 2: "#78350f", 4: "#78350f", 6: "#78350f", 8: "#78350f", 10: "#78350f", 12: "#78350f"},
    {1: "#065f46", 5: "#065f46", 9: "#065f46", 3: "#991b1b", 7: "#991b1b", 11: "#991b1b", 2: "#78350f", 4: "#78350f", 6: "#78350f", 8: "#78350f", 10: "#78350f", 12: "#78350f"},
    {1: "పుణ్యము", 5: "పుణ్యము", 9: "పుణ్యము", 3: "పాపము", 7: "పాపము", 11: "పాపము", 2: "పుణ్యము\nపాపము", 4: "పుణ్యము\nపాపము", 6: "పుణ్యము\nపాపము", 8: "పుణ్యము\nపాపము", 10: "పుణ్యము\nపాపము", 12: "పుణ్యము\nపాపము"},
    {1: "పుణ్యము", 5: "పుణ్యము", 9: "పుణ్యము", 3: "పాపము", 7: "పాపము", 11: "పాపము", 2: "పుణ్యము\nపాపము", 4: "పుణ్యము\nపాపము", 6: "పుణ్యము\nపాపము", 8: "పుణ్యము\nపాపము", 10: "పుణ్యము\nపాపము", 12: "పుణ్యము\nపాపము"}
)

# --- 42. Patam 42: Kendras Karma (1, 4, 7, 10, 12) ---
draw_dual_chart(
    "patam_42_kendras_karma.svg",
    "42వ చిత్రపటము. కేంద్రములలోని కర్మ (1, 4, 7, 10, 12)",
    {1: "#065f46", 4: "#78350f", 7: "#991b1b", 10: "#78350f", 12: "#78350f"},
    {1: "#065f46", 4: "#78350f", 7: "#991b1b", 10: "#78350f", 12: "#78350f"},
    {1: "శరీర\nప్రారంభ", 4: "స్థూల\nస్థిరాస్తులు", 7: "భార్య\nకర్మ", 10: "సూక్ష్మ\nఆస్తి(కీర్తి)", 12: "శరీర\nఅంత్య"},
    {1: "శరీర ప్రారంభ\nఅవయవాల\nకర్మ", 4: "స్థూల\nస్థిరాస్తులు", 7: "భార్య సంబంధిత\nకర్మలు", 10: "సూక్ష్మ ఆస్తి\nకీర్తి, ఉద్యోగం", 12: "శరీర అంత్యం\nచివరి దశ"}
)

# --- 43. Patam 43: Bhava 6 Karma ---
draw_dual_chart(
    "patam_43_bhava_6_karma.svg",
    "43వ చిత్రపటము. 6వ స్థానములోని కర్మ (శత్రు ఋణ రోగములు)",
    {1: "#065f46", 4: "#78350f", 7: "#991b1b", 10: "#78350f", 12: "#78350f", 6: "#991b1b"},
    {1: "#065f46", 4: "#78350f", 7: "#991b1b", 10: "#78350f", 12: "#78350f", 6: "#991b1b"},
    {1: "శరీర ప్రారంభ", 4: "స్థూల స్థిరాస్తులు", 7: "భార్య కర్మ", 10: "సూక్ష్మ స్థిరాస్తులు", 12: "శరీర అంత్య", 6: "శత్రు ఋణ\nరోగ కర్మలు"},
    {1: "శరీర ప్రారంభ", 4: "స్థూల స్థిరాస్తులు", 7: "భార్య కర్మ", 10: "సూక్ష్మ ఆస్తి", 12: "శరీర అంత్యం", 6: "శత్రు ఋణ\nరోగ కర్మలు"}
)

# --- 44. Patam 44: Bhavas 3, 4, 5 Karma ---
draw_dual_chart(
    "patam_44_bhavas_3_4_5_karma.svg",
    "44వ చిత్రపటము. 3, 4, 5 స్థానముల కర్మలు (ప్రపంచ ధనం, ఆస్తి, విద్య)",
    {1: "#065f46", 3: "#991b1b", 4: "#78350f", 5: "#065f46", 6: "#991b1b", 7: "#991b1b", 10: "#78350f", 12: "#78350f"},
    {1: "#065f46", 3: "#991b1b", 4: "#78350f", 5: "#065f46", 6: "#991b1b", 7: "#991b1b", 10: "#78350f", 12: "#78350f"},
    {1: "శరీర ప్రారంభ", 3: "ప్రపంచ\nధనము", 4: "స్థూల\nస్థిరాస్తులు", 5: "ప్రపంచ\nజ్ఞానము/చదువు", 6: "శత్రు ఋణ రోగ", 7: "భార్య కర్మ", 10: "సూక్ష్మ స్థిరాస్తులు", 12: "శరీర అంత్య"},
    {1: "శరీర ప్రారంభ", 3: "ప్రపంచ ధనము", 4: "స్థూల స్థిరాస్తులు", 5: "ప్రపంచ జ్ఞానము", 6: "శత్రు ఋణ రోగ", 7: "భార్య కర్మ", 10: "సూక్ష్మ ఆస్తి", 12: "శరీర అంత్య"}
)

# --- 45. Patam 45: Bhavas 9, 10, 11 Karma ---
draw_dual_chart(
    "patam_45_bhavas_9_10_11_karma.svg",
    "45వ చిత్రపటము. 9, 10, 11 స్థానముల కర్మలు (దైవ ధనం, కీర్తి, పరమాత్మ జ్ఞానం)",
    {1: "#065f46", 3: "#991b1b", 4: "#78350f", 5: "#065f46", 6: "#991b1b", 7: "#991b1b", 9: "#065f46", 10: "#78350f", 11: "#991b1b", 12: "#78350f"},
    {1: "#065f46", 3: "#991b1b", 4: "#78350f", 5: "#065f46", 6: "#991b1b", 7: "#991b1b", 9: "#065f46", 10: "#78350f", 11: "#991b1b", 12: "#78350f"},
    {1: "శరీర ప్రారంభ", 3: "ప్రపంచ ధనం", 4: "స్థూల స్థిరాస్తులు", 5: "ప్రపంచ జ్ఞానం", 6: "శత్రు ఋణ రోగ", 7: "భార్య సుఖం", 9: "పరమాత్మ\nప్రపంచ ధనం", 10: "దైవ సూక్ష్మ\nఆస్తి కీర్తి", 11: "పరమాత్మ\nప్రపంచ జ్ఞానం", 12: "శరీర అంత్య"},
    {1: "శరీర ప్రారంభ", 3: "ప్రపంచ ధనం", 4: "స్థూల స్థిరాస్తులు", 5: "ప్రపంచ జ్ఞానం", 6: "శత్రు ఋణ రోగ", 7: "భార్య కర్మ", 9: "పరమాత్మ ధనం", 10: "దైవ సూక్ష్మ ఆస్తి", 11: "పరమాత్మ జ్ఞానం", 12: "శరీర అంత్య"}
)

# --- 46. Patam 46: Complete Master Karma Chakra ---
draw_dual_chart(
    "patam_46_complete_karmachakram.svg",
    "46వ చిత్రపటము. పూర్తి కర్మచక్రము (Master Complete 12 Bhavas)",
    {1: "#065f46", 2: "#78350f", 3: "#991b1b", 4: "#78350f", 5: "#065f46", 6: "#78350f", 7: "#991b1b", 8: "#78350f", 9: "#065f46", 10: "#78350f", 11: "#991b1b", 12: "#78350f"},
    {1: "#065f46", 2: "#78350f", 3: "#991b1b", 4: "#78350f", 5: "#065f46", 6: "#78350f", 7: "#991b1b", 8: "#78350f", 9: "#065f46", 10: "#78350f", 11: "#991b1b", 12: "#78350f"},
    {1: "శరీర\nప్రారంభ", 2: "అజ్ఞాన\nజీవితం ఎంత", 3: "ప్రపంచ\nధనము", 4: "స్థూల\nస్థిరాస్తులు", 5: "ప్రపంచ\nజ్ఞానము", 6: "శత్రు ఋణ\nరోగ కర్మలు", 7: "భార్య\nసంబంధ", 8: "జ్ఞాన ప్రపంచ\nజీవితం ఎంత", 9: "పరమాత్మ\nప్రపంచ ధనం", 10: "కనిపించని\nఆస్తి కీర్తి", 11: "పరమాత్మ\nప్రపంచ జ్ఞానం", 12: "శరీర\nఅంత్య కర్మ"},
    {1: "శరీర ప్రారంభ", 2: "అజ్ఞాన జీవితం", 3: "ప్రపంచ ధనం", 4: "స్థూల స్థిరాస్తులు", 5: "ప్రపంచ జ్ఞానం", 6: "శత్రు ఋణ రోగ", 7: "భార్య సంబంధం", 8: "జ్ఞాన జీవితం", 9: "పరమాత్మ ధనం", 10: "కనిపించని కీర్తి", 11: "పరమాత్మ జ్ఞానం", 12: "శరీర అంత్యం"}
)