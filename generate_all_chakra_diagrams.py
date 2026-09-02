import math
import os

out_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\static\images\diagrams"
os.makedirs(out_dir, exist_ok=True)

FONT = "font-family=\"'Outfit', 'Segoe UI', 'Noto Sans Telugu', sans-serif\""

def save_svg(name, svg_content):
    path = os.path.join(out_dir, name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Generated {name}")

# --- 1. Patam 1: Circular Kaala Chakram (12 Rashis) ---
def gen_patam_1():
    cx, cy, r = 250, 250, 210
    rashis = ["మేషం", "వృషభం", "మిథునం", "కర్కాటకము", "సింహం", "కన్య", "తుల", "వృశ్చికం", "ధనుస్సు", "మకరము", "కుంభము", "మీనము"]
    colors = ["#fef08a", "#dcfce7", "#e0e7ff", "#fce7f3", "#fee2e2", "#ffedd5", "#fef9c3", "#d1fae5", "#e0f2fe", "#ede9fe", "#f3e8ff", "#fae8ff"]
    
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%" {FONT}>',
           '<defs><radialGradient id="bg1" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#1e1b4b"/><stop offset="100%" stop-color="#090d16"/></radialGradient></defs>',
           '<rect width="500" height="500" fill="url(#bg1)" rx="20"/>',
           f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0f172a" stroke="#fbbf24" stroke-width="4"/>']
    
    # 12 Sectors
    for i in range(12):
        a1 = math.radians(i * 30 - 90)
        a2 = math.radians((i + 1) * 30 - 90)
        mid = math.radians(i * 30 + 15 - 90)
        
        x1 = cx + r * math.cos(a1)
        y1 = cy + r * math.sin(a1)
        x2 = cx + r * math.cos(a2)
        y2 = cy + r * math.sin(a2)
        
        tx = cx + (r * 0.65) * math.cos(mid)
        ty = cy + (r * 0.65) * math.sin(mid)
        
        c = colors[i % len(colors)]
        svg.append(f'<path d="M {cx} {cy} L {x1} {y1} A {r} {r} 0 0 1 {x2} {y2} Z" fill="{c}" fill-opacity="0.12" stroke="#38bdf8" stroke-width="1.5"/>')
        svg.append(f'<text x="{tx}" y="{ty+5}" fill="#f8fafc" font-size="14" font-weight="800" text-anchor="middle">{rashis[i]}</text>')
    
    # Center circle
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="45" fill="#020617" stroke="#fbbf24" stroke-width="3"/>')
    svg.append(f'<text x="{cx}" y="{cy-2}" fill="#fbbf24" font-size="15" font-weight="900" text-anchor="middle">కాల</text>')
    svg.append(f'<text x="{cx}" y="{cy+16}" fill="#fbbf24" font-size="15" font-weight="900" text-anchor="middle">చక్రము</text>')
    svg.append('</svg>')
    save_svg("patam_1_kalachakram_circle.svg", "\n".join(svg))

# --- 2. Patam 2: 4-Tier 3D Spindle Stack ---
def gen_patam_2():
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 600" width="100%" height="100%" {FONT}>',
           '<defs><linearGradient id="bg2" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#020617"/></linearGradient></defs>',
           '<rect width="540" height="600" fill="url(#bg2)" rx="20"/>',
           # Spindle needle
           '<polygon points="266,40 274,40 273,560 267,560" fill="url(#spindleGrad)" stroke="#cbd5e1" stroke-width="1"/>',
           '<defs><linearGradient id="spindleGrad" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#94a3b8"/><stop offset="50%" stop-color="#ffffff"/><stop offset="100%" stop-color="#64748b"/></linearGradient></defs>',
           # Top spindle point
           '<circle cx="270" cy="40" r="5" fill="#fbbf24"/>',
           '<polygon points="270,580 265,550 275,550" fill="#cbd5e1"/>']
    
    layers = [
        ("బ్రహ్మ చక్రము", 100, 150, 42, "#ec4899", "బ్రహ్మ", False),
        ("కాల చక్రము", 210, 175, 48, "#38bdf8", "కాల", True),
        ("కర్మ చక్రము", 320, 175, 48, "#fbbf24", "కర్మ", True),
        ("గుణ చక్రము", 430, 185, 52, "#10b981", "గుణ", False)
    ]
    
    for name, cy, rx, ry, col, label, has_rays in layers:
        cx = 270
        # Oval disc shadow / bottom
        svg.append(f'<ellipse cx="{cx}" cy="{cy+6}" rx="{rx}" ry="{ry}" fill="#000000" fill-opacity="0.4"/>')
        # Main Oval disc
        svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{col}" fill-opacity="0.18" stroke="{col}" stroke-width="3"/>')
        
        if has_rays:
            for deg in range(0, 360, 30):
                rad = math.radians(deg)
                x = cx + rx * math.cos(rad)
                y = cy + ry * math.sin(rad)
                svg.append(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{col}" stroke-width="1.5" stroke-opacity="0.6"/>')
        elif label == "గుణ":
            # Concentric rings
            svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx*0.7}" ry="{ry*0.7}" fill="none" stroke="{col}" stroke-width="1.5" stroke-dasharray="4 4"/>')
            svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx*0.4}" ry="{ry*0.4}" fill="none" stroke="{col}" stroke-width="1.5"/>')
            
        # Center hole around spindle
        svg.append(f'<ellipse cx="{cx}" cy="{cy}" rx="14" ry="7" fill="#020617" stroke="#ffffff" stroke-width="1.5"/>')
        
        # Label to right and left
        svg.append(f'<text x="65" y="{cy+6}" fill="{col}" font-size="18" font-weight="900">{label}</text>')
        svg.append(f'<text x="475" y="{cy+6}" fill="{col}" font-size="18" font-weight="900" text-anchor="end">చక్రము</text>')
    
    # Title
    svg.append('<text x="270" y="555" fill="#f8fafc" font-size="16" font-weight="800" text-anchor="middle">బ్రహ్మ, కాల, కర్మ, గుణచక్రము - 2వ పటము</text>')
    svg.append('</svg>')
    save_svg("patam_2_four_chakras_stack.svg", "\n".join(svg))

# --- 3. Patam 3: Square Kaala Chakra (12 Rashis) ---
def gen_patam_3():
    grid = [
        ["మీనము", "మేషం", "వృషభం", "మిథునం"],
        ["కుంభము", "", "", "కర్కాటక"],
        ["మకరము", "", "", "సింహ"],
        ["ధనస్సు", "వృశ్చిక", "తుల", "కన్య"]
    ]
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%" {FONT}>',
           '<rect width="500" height="500" fill="#090d16" rx="20"/>',
           '<rect x="30" y="30" width="440" height="440" fill="#0f172a" stroke="#38bdf8" stroke-width="3" rx="10"/>']
    
    w, h = 110, 110
    for r in range(4):
        for c in range(4):
            x = 30 + c * w
            y = 30 + r * h
            val = grid[r][c]
            if val:
                svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#1e293b" fill-opacity="0.6" stroke="#38bdf8" stroke-width="1.5"/>')
                svg.append(f'<text x="{x + w/2}" y="{y + h/2 + 6}" fill="#e0f2fe" font-size="16" font-weight="800" text-anchor="middle">{val}</text>')
            elif r == 1 and c == 1:
                # Center box spanning 2x2
                svg.append(f'<rect x="{x}" y="{y}" width="{w*2}" height="{h*2}" fill="#020617" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6 6"/>')
                svg.append(f'<text x="{x + w}" y="{y + h - 5}" fill="#38bdf8" font-size="22" font-weight="900" text-anchor="middle">కాలచక్రము</text>')
                svg.append(f'<text x="{x + w}" y="{y + h + 22}" fill="#94a3b8" font-size="14" font-weight="600" text-anchor="middle">3వ పటము</text>')
                
    svg.append('</svg>')
    save_svg("patam_3_kalachakram_square.svg", "\n".join(svg))

# --- 4. Patam 4: Circular Karma Chakra (with Guru in center) ---
def gen_patam_4():
    cx, cy, r = 250, 250, 210
    bhavas = ["ప్రథమ స్థానము", "ద్వితీయ స్థానము", "తృతీయ స్థానము", "చతుర్థ స్థానము", "పంచమ స్థానము", "షష్ఠమ స్థానము", "సప్తమ స్థానము", "అష్టమ స్థానము", "నవమ స్థానము", "దశమ స్థానము", "ఏకాదశ స్థానము", "ద్వాదశ స్థానము"]
    
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%" {FONT}>',
           '<defs><radialGradient id="bg4" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#1e1b4b"/><stop offset="100%" stop-color="#020617"/></radialGradient></defs>',
           '<rect width="500" height="500" fill="url(#bg4)" rx="20"/>',
           f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0f172a" stroke="#fbbf24" stroke-width="4"/>']
    
    for i in range(12):
        a1 = math.radians(i * 30 - 90)
        a2 = math.radians((i + 1) * 30 - 90)
        mid = math.radians(i * 30 + 15 - 90)
        
        x1 = cx + r * math.cos(a1)
        y1 = cy + r * math.sin(a1)
        x2 = cx + r * math.cos(a2)
        y2 = cy + r * math.sin(a2)
        
        tx = cx + (r * 0.68) * math.cos(mid)
        ty = cy + (r * 0.68) * math.sin(mid)
        num_x = cx + (r * 0.9) * math.cos(mid)
        num_y = cy + (r * 0.9) * math.sin(mid)
        
        svg.append(f'<path d="M {cx} {cy} L {x1} {y1} A {r} {r} 0 0 1 {x2} {y2} Z" fill="#fbbf24" fill-opacity="0.08" stroke="#f59e0b" stroke-width="1.5"/>')
        svg.append(f'<text x="{num_x}" y="{num_y+5}" fill="#fbbf24" font-size="14" font-weight="900" text-anchor="middle">{i+1}</text>')
        svg.append(f'<text x="{tx}" y="{ty+4}" fill="#fde68a" font-size="11" font-weight="700" text-anchor="middle">{bhavas[i]}</text>')
        
    # Center circle with 'గురువు'
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="48" fill="#020617" stroke="#fbbf24" stroke-width="3.5"/>')
    svg.append(f'<text x="{cx}" y="{cy-8}" fill="#fbbf24" font-size="16" font-weight="900" text-anchor="middle">గు</text>')
    svg.append(f'<text x="{cx}" y="{cy+12}" fill="#fbbf24" font-size="16" font-weight="900" text-anchor="middle">రు వు</text>')
    svg.append(f'<text x="{cx}" y="{cy+470}" fill="#94a3b8" font-size="14" font-weight="700" text-anchor="middle">కర్మచక్రము - 4వ పటము</text>')
    svg.append('</svg>')
    save_svg("patam_4_karmachakram_circle_guru.svg", "\n".join(svg))

# --- 5. Patam 5: Square Karma Chakra (12 Bhavas) ---
def gen_patam_5():
    bhavas_grid = [
        ("(12) ద్వాదశ", "(1) ప్రథమ", "(2) ద్వితీయ", "(3) తృతీయ"),
        ("(11) ఏకాదశ", "", "", "(4) చతుర్థ"),
        ("(10) దశమ", "", "", "(5) పంచమ"),
        ("(9) నవమ", "(8) అష్టమ", "(7) సప్తమ", "(6) షష్ఠమ")
    ]
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%" {FONT}>',
           '<rect width="500" height="500" fill="#090d16" rx="20"/>',
           '<rect x="30" y="30" width="440" height="440" fill="#0f172a" stroke="#fbbf24" stroke-width="3" rx="10"/>']
    
    w, h = 110, 110
    for r in range(4):
        for c in range(4):
            x = 30 + c * w
            y = 30 + r * h
            val = bhavas_grid[r][c]
            if val:
                svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#1e1b4b" fill-opacity="0.6" stroke="#fbbf24" stroke-width="1.5"/>')
                parts = val.split(" ")
                svg.append(f'<text x="{x + w/2}" y="{y + h/2 - 6}" fill="#fbbf24" font-size="15" font-weight="900" text-anchor="middle">{parts[0]}</text>')
                svg.append(f'<text x="{x + w/2}" y="{y + h/2 + 14}" fill="#fde68a" font-size="13" font-weight="700" text-anchor="middle">{parts[1]} స్థానము</text>')
            elif r == 1 and c == 1:
                svg.append(f'<rect x="{x}" y="{y}" width="{w*2}" height="{h*2}" fill="#020617" stroke="#fbbf24" stroke-width="2" stroke-dasharray="6 6"/>')
                svg.append(f'<text x="{x + w}" y="{y + h - 5}" fill="#fbbf24" font-size="22" font-weight="900" text-anchor="middle">కర్మచక్రము</text>')
                svg.append(f'<text x="{x + w}" y="{y + h + 22}" fill="#94a3b8" font-size="14" font-weight="600" text-anchor="middle">5వ పటము</text>')
                
    svg.append('</svg>')
    save_svg("patam_5_karmachakram_square.svg", "\n".join(svg))

# --- 6, 7, 8: Guna Chakra Concentric Diagrams ---
def gen_gunachakra_base(patam_num, title, jeeva_pos=None):
    cx, cy = 250, 240
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 520" width="100%" height="100%" {FONT}>',
           '<defs><radialGradient id="bgG" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="#1e293b"/><stop offset="100%" stop-color="#020617"/></radialGradient></defs>',
           '<rect width="500" height="520" fill="url(#bgG)" rx="20"/>']
    
    # Outer ring: Tamasa
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="190" fill="#ef4444" fill-opacity="0.12" stroke="#ef4444" stroke-width="2.5"/>')
    # Middle ring: Rajasa
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="135" fill="#f59e0b" fill-opacity="0.12" stroke="#f59e0b" stroke-width="2.5"/>')
    # Inner ring: Sattva
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="80" fill="#10b981" fill-opacity="0.12" stroke="#10b981" stroke-width="2.5"/>')
    # Center Atma
    svg.append(f'<circle cx="{cx}" cy="{cy}" r="34" fill="#020617" stroke="#fbbf24" stroke-width="3"/>')
    svg.append(f'<text x="{cx}" y="{cy+6}" fill="#fbbf24" font-size="16" font-weight="900" text-anchor="middle">ఆత్మ</text>')
    
    # Texture symbols (x, 6, ~)
    # Tamas 'x'
    for deg in range(0, 360, 20):
        rad = math.radians(deg)
        x = cx + 162 * math.cos(rad)
        y = cy + 162 * math.sin(rad)
        svg.append(f'<text x="{x}" y="{y+4}" fill="#f87171" font-size="12" font-weight="800" text-anchor="middle">✕</text>')
    # Rajas '6'
    for deg in range(10, 360, 24):
        rad = math.radians(deg)
        x = cx + 108 * math.cos(rad)
        y = cy + 108 * math.sin(rad)
        svg.append(f'<text x="{x}" y="{y+4}" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">6</text>')
    # Sattva '~'
    for deg in range(5, 360, 30):
        rad = math.radians(deg)
        x = cx + 58 * math.cos(rad)
        y = cy + 58 * math.sin(rad)
        svg.append(f'<text x="{x}" y="{y+4}" fill="#34d399" font-size="14" font-weight="900" text-anchor="middle">~</text>')
        
    # Jeeva position if specified
    if jeeva_pos == "tamas":
        jx, jy = cx + 162, cy - 20
        svg.append(f'<circle cx="{jx}" cy="{jy}" r="12" fill="#ef4444" stroke="#ffffff" stroke-width="2.5"/>')
        svg.append(f'<text x="{jx}" y="{jy+4}" fill="#ffffff" font-size="9" font-weight="900" text-anchor="middle">జీవుడు</text>')
        svg.append(f'<line x1="{jx+14}" y1="{jy}" x2="430" y2="{jy}" stroke="#ef4444" stroke-width="2"/>')
        svg.append(f'<text x="435" y="{jy+4}" fill="#f87171" font-size="13" font-weight="800">తామసంలో జీవుడు</text>')
    elif jeeva_pos == "rajas":
        jx, jy = cx + 108, cy - 20
        svg.append(f'<circle cx="{jx}" cy="{jy}" r="12" fill="#f59e0b" stroke="#ffffff" stroke-width="2.5"/>')
        svg.append(f'<text x="{jx}" y="{jy+4}" fill="#020617" font-size="9" font-weight="900" text-anchor="middle">జీవుడు</text>')
        svg.append(f'<line x1="{jx+14}" y1="{jy}" x2="430" y2="{jy}" stroke="#f59e0b" stroke-width="2"/>')
        svg.append(f'<text x="435" y="{jy+4}" fill="#fbbf24" font-size="13" font-weight="800">రాజసంలో జీవుడు</text>')
    elif jeeva_pos == "sattva":
        jx, jy = cx + 58, cy - 20
        svg.append(f'<circle cx="{jx}" cy="{jy}" r="12" fill="#10b981" stroke="#ffffff" stroke-width="2.5"/>')
        svg.append(f'<text x="{jx}" y="{jy+4}" fill="#ffffff" font-size="9" font-weight="900" text-anchor="middle">జీవుడు</text>')
        svg.append(f'<line x1="{jx+14}" y1="{jy}" x2="430" y2="{jy}" stroke="#10b981" stroke-width="2"/>')
        svg.append(f'<text x="435" y="{jy+4}" fill="#34d399" font-size="13" font-weight="800">సాత్వికంలో జీవుడు</text>')
    else:
        # Default division pointers
        svg.append('<line x1="390" y1="120" x2="440" y2="100" stroke="#ef4444" stroke-width="1.5"/>')
        svg.append('<text x="445" y="104" fill="#f87171" font-size="12" font-weight="800">తామస భాగము</text>')
        svg.append('<line x1="360" y1="180" x2="440" y2="180" stroke="#f59e0b" stroke-width="1.5"/>')
        svg.append('<text x="445" y="184" fill="#fbbf24" font-size="12" font-weight="800">రాజస భాగము</text>')
        svg.append('<line x1="315" y1="240" x2="440" y2="260" stroke="#10b981" stroke-width="1.5"/>')
        svg.append('<text x="445" y="264" fill="#34d399" font-size="12" font-weight="800">సాత్విక భాగము</text>')

    svg.append(f'<text x="250" y="490" fill="#f8fafc" font-size="15" font-weight="800" text-anchor="middle">{title} - {patam_num}వ పటము</text>')
    svg.append('</svg>')
    return "\n".join(svg)

save_svg("patam_6_gunachakram_rings.svg", gen_gunachakra_base(6, "గుణచక్రము"))
save_svg("patam_7_gunachakram_3divisions.svg", gen_gunachakra_base(7, "గుణచక్రము (3 గుణాలు)"))
save_svg("patam_8_gunachakram_324gunas.svg", gen_gunachakra_base(8, "గుణచక్రము (324 గుణాలు)"))
save_svg("patam_9_jeeva_in_tamas.svg", gen_gunachakra_base(9, "తామస భాగములో జీవుడు", "tamas"))
save_svg("patam_10_jeeva_in_rajas.svg", gen_gunachakra_base(10, "రాజస భాగములో జీవుడు", "rajas"))
save_svg("patam_11_jeeva_in_sattva.svg", gen_gunachakra_base(11, "సాత్విక భాగములో జీవుడు", "sattva"))

gen_patam_1()
gen_patam_2()
gen_patam_3()
gen_patam_4()
gen_patam_5()