import os

out_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\static\images\diagrams"
os.makedirs(out_dir, exist_ok=True)

def save_svg(filename, content):
    filepath = os.path.join(out_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"Saved: {filename}")

# 12. Patam 12: Jeeva Shape
svg_12 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <defs>
    <radialGradient id="jeevaGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#d97706" stop-opacity="0.2"/>
    </radialGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.5"/>
    </filter>
  </defs>
  <rect width="100%" height="100%" fill="#090d16" rx="16"/>
  <circle cx="250" cy="250" r="230" fill="none" stroke="#fbbf24" stroke-width="3"/>
  <circle cx="250" cy="250" r="200" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,4"/>
  
  <!-- Outer Ring: Ahamu -->
  <circle cx="250" cy="250" r="180" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="3" filter="url(#shadow)"/>
  <text x="250" y="85" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#f87171" text-anchor="middle">అహము (Ahamu - Outer Shell)</text>

  <!-- Middle Ring: Chitta -->
  <circle cx="250" cy="250" r="130" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="3" filter="url(#shadow)"/>
  <text x="250" y="140" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">చిత్తము (Chitta - Memory Layer)</text>

  <!-- Inner Ring: Buddhi -->
  <circle cx="250" cy="250" r="80" fill="rgba(16, 185, 129, 0.2)" stroke="#10b981" stroke-width="3" filter="url(#shadow)"/>
  <text x="250" y="195" font-family="'Outfit', sans-serif" font-size="18" font-weight="bold" fill="#34d399" text-anchor="middle">బుద్ధి (Buddhi)</text>

  <!-- Center: Jeeva -->
  <circle cx="250" cy="250" r="30" fill="url(#jeevaGlow)" stroke="#f59e0b" stroke-width="3"/>
  <text x="250" y="256" font-family="'Outfit', sans-serif" font-size="18" font-weight="bold" fill="#ffffff" text-anchor="middle">జీవుడు</text>
  
  <text x="250" y="465" font-family="'Outfit', sans-serif" font-size="18" font-weight="bold" fill="#fbbf24" text-anchor="middle">12వ పటము: జీవుని ఆకారము (బుద్ధి, చిత్తము, అహము పొరలు)</text>
</svg>'''
save_svg("patam_12_jeeva_shape.svg", svg_12)

# Patam 14: Own Homes of 12 Planets
svg_14 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0f172a" rx="16"/>
  <rect x="20" y="20" width="560" height="560" fill="none" stroke="#fbbf24" stroke-width="3" rx="12"/>
  
  <!-- Outer 12 Grid Box -->
  <rect x="50" y="50" width="500" height="500" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- Grid Lines -->
  <line x1="175" y1="50" x2="175" y2="550" stroke="#334155" stroke-width="2"/>
  <line x1="300" y1="50" x2="300" y2="550" stroke="#334155" stroke-width="2"/>
  <line x1="425" y1="50" x2="425" y2="550" stroke="#334155" stroke-width="2"/>
  <line x1="50" y1="175" x2="550" y2="175" stroke="#334155" stroke-width="2"/>
  <line x1="50" y1="300" x2="550" y2="300" stroke="#334155" stroke-width="2"/>
  <line x1="50" y1="425" x2="550" y2="425" stroke="#334155" stroke-width="2"/>
  
  <!-- Center Box Fill -->
  <rect x="175" y="175" width="250" height="250" fill="rgba(30, 41, 59, 0.95)" stroke="#fbbf24" stroke-width="2"/>
  <text x="300" y="290" font-family="'Outfit', sans-serif" font-size="22" font-weight="bold" fill="#fbbf24" text-anchor="middle">కాలచక్రము</text>
  <text x="300" y="320" font-family="'Outfit', sans-serif" font-size="16" fill="#38bdf8" text-anchor="middle">12 గ్రహముల స్వంత ఇళ్ళు</text>

  <!-- 12 Rashis & Planets -->
  <!-- Top row: Meena(Guru), Mesha(Kuja), Vrishabha(Mitra), Mithuna(Chitra) -->
  <!-- Meena -->
  <text x="112" y="90" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#34d399" text-anchor="middle">గురు</text>
  <text x="112" y="120" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">మీనము</text>
  
  <!-- Mesha -->
  <text x="237" y="90" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#ef4444" text-anchor="middle">కుజ</text>
  <text x="237" y="120" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">మేషం</text>
  
  <!-- Vrishabha -->
  <text x="362" y="90" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">మిత్ర</text>
  <text x="362" y="120" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">వృషభం</text>

  <!-- Mithuna -->
  <text x="487" y="90" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#fbbf24" text-anchor="middle">చిత్ర</text>
  <text x="487" y="120" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">మిథునం</text>

  <!-- Karkataka (Right 1) -->
  <text x="487" y="215" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#e2e8f0" text-anchor="middle">చంద్ర</text>
  <text x="487" y="245" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">కర్కాట</text>

  <!-- Simha (Right 2) -->
  <text x="487" y="340" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#f59e0b" text-anchor="middle">రవి</text>
  <text x="487" y="370" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">సింహ</text>

  <!-- Kanya (Bottom right) -->
  <text x="487" y="465" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#34d399" text-anchor="middle">బుధ</text>
  <text x="487" y="495" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">కన్య</text>

  <!-- Thula (Bottom 3) -->
  <text x="362" y="465" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#ec4899" text-anchor="middle">శుక్ర</text>
  <text x="362" y="495" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">తుల</text>

  <!-- Vrischika (Bottom 2) -->
  <text x="237" y="465" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">భూమి</text>
  <text x="237" y="495" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">వృశ్చిక</text>

  <!-- Dhanus (Bottom left) -->
  <text x="112" y="465" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#a855f7" text-anchor="middle">కేతు</text>
  <text x="112" y="495" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">ధనస్సు</text>

  <!-- Makara (Left 2) -->
  <text x="112" y="340" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#6366f1" text-anchor="middle">రాహు</text>
  <text x="112" y="370" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">మకరము</text>

  <!-- Kumbha (Left 1) -->
  <text x="112" y="215" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#94a3b8" text-anchor="middle">శని</text>
  <text x="112" y="245" font-family="'Outfit', sans-serif" font-size="15" fill="#e2e8f0" text-anchor="middle">కుంభము</text>
  
  <text x="300" y="582" font-family="'Outfit', sans-serif" font-size="18" font-weight="bold" fill="#fbbf24" text-anchor="middle">14వ పటము: కాలచక్రములో 12 గ్రహముల స్వంత స్థానములు</text>
</svg>'''
save_svg("patam_14_own_houses.svg", svg_14)

# Patam 15: 2:1 Rule Division Chart (Guru party vs Shani party)
svg_15 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 500" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0b0f19" rx="16"/>
  <text x="300" y="40" font-family="'Outfit', sans-serif" font-size="22" font-weight="bold" fill="#fbbf24" text-anchor="middle">15వ పటము: 2:1 సూత్రము ప్రకారం గ్రహముల విభజన</text>
  
  <!-- Left Side: Guru Party (Green Box) -->
  <rect x="30" y="70" width="250" height="380" fill="rgba(16, 185, 129, 0.1)" stroke="#10b981" stroke-width="2" rx="12"/>
  <text x="155" y="105" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#34d399" text-anchor="middle">🟢 గురు వర్గము (Guru Party)</text>
  <text x="155" y="130" font-family="'Outfit', sans-serif" font-size="14" fill="#a7f3d0" text-anchor="middle">(పుణ్య పాలిత - 6 గ్రహాలు)</text>
  <line x1="45" y1="145" x2="265" y2="145" stroke="#10b981" stroke-width="1.5"/>
  
  <text x="55" y="180" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">12, 1 : గురు, కుజ (మీన, మేష)</text>
  <text x="55" y="225" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">4, 5  : చంద్ర, రవి (కర్కాట, సింహ)</text>
  <text x="55" y="270" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">8, 9  : భూమి, కేతు (వృశ్చిక, ధనూ)</text>
  
  <rect x="45" y="300" width="220" height="130" fill="rgba(0,0,0,0.3)" rx="8" stroke="rgba(16,185,129,0.3)"/>
  <text x="155" y="325" font-family="'Outfit', sans-serif" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">గురు వర్గం నాయకుడు: గురువు</text>
  <text x="55" y="355" font-family="'Outfit', sans-serif" font-size="14" fill="#cbd5e1">• రవి, చంద్ర, కుజ, గురు</text>
  <text x="55" y="380" font-family="'Outfit', sans-serif" font-size="14" fill="#cbd5e1">• కేతు, భూమి</text>

  <!-- Right Side: Shani Party (Red/Purple Box) -->
  <rect x="320" y="70" width="250" height="380" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="2" rx="12"/>
  <text x="445" y="105" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#f87171" text-anchor="middle">🔴 శని వర్గము (Shani Party)</text>
  <text x="445" y="130" font-family="'Outfit', sans-serif" font-size="14" fill="#fecaca" text-anchor="middle">(పాప పాలిత - 6 గ్రహాలు)</text>
  <line x1="335" y1="145" x2="555" y2="145" stroke="#ef4444" stroke-width="1.5"/>
  
  <text x="345" y="180" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">2, 3   : మిత్ర, చిత్ర (వృషభ, మిథున)</text>
  <text x="345" y="225" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">6, 7   : బుధ, శుక్ర (కన్య, తుల)</text>
  <text x="345" y="270" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">10, 11 : రాహు, శని (మకర, కుంభ)</text>

  <rect x="335" y="300" width="220" height="130" fill="rgba(0,0,0,0.3)" rx="8" stroke="rgba(239,68,68,0.3)"/>
  <text x="445" y="325" font-family="'Outfit', sans-serif" font-size="15" font-weight="bold" fill="#f87171" text-anchor="middle">శని వర్గం నాయకుడు: శని</text>
  <text x="345" y="355" font-family="'Outfit', sans-serif" font-size="14" fill="#cbd5e1">• శని, రాహు, శుక్ర, బుధ</text>
  <text x="345" y="380" font-family="'Outfit', sans-serif" font-size="14" fill="#cbd5e1">• మిత్ర, చిత్ర</text>
</svg>'''
save_svg("patam_15_rule21_division.svg", svg_15)

# Patams 22 to 27: 1x7 Badda Shatru Rule Diagrams
svg_22 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 500" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0f172a" rx="16"/>
  <rect x="40" y="40" width="420" height="420" fill="none" stroke="#fbbf24" stroke-width="2.5"/>
  
  <text x="250" y="30" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fbbf24" text-anchor="middle">22వ పటము: 1 × 7 బద్దశత్రుత్వ సూత్రము (కుజ ✕ శుక్ర)</text>
  
  <rect x="150" y="150" width="200" height="200" fill="rgba(30, 41, 59, 0.9)" stroke="#38bdf8" stroke-width="2"/>
  <text x="250" y="230" font-family="'Outfit', sans-serif" font-size="22" font-weight="bold" fill="#ef4444" text-anchor="middle">సూత్రము 1 × 7</text>
  <text x="250" y="270" font-family="'Outfit', sans-serif" font-size="18" fill="#38bdf8" text-anchor="middle">మేష లగ్నము</text>
  
  <!-- 1st House (Kuja) -->
  <rect x="190" y="50" width="120" height="60" fill="rgba(239, 68, 68, 0.25)" stroke="#ef4444" stroke-width="2" rx="8"/>
  <text x="250" y="78" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">1. కుజుడు (మేషం)</text>

  <!-- 7th House (Shukra) -->
  <rect x="190" y="390" width="120" height="60" fill="rgba(236, 72, 153, 0.25)" stroke="#ec4899" stroke-width="2" rx="8"/>
  <text x="250" y="418" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">7. శుక్రుడు (తుల)</text>

  <!-- Red Clash Arrow -->
  <line x1="250" y1="110" x2="250" y2="390" stroke="#ef4444" stroke-width="4" stroke-dasharray="8,6"/>
  <polygon points="250,385 242,370 258,370" fill="#ef4444"/>
  <polygon points="250,115 242,130 258,130" fill="#ef4444"/>
  <text x="280" y="250" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#ef4444">బద్దశత్రువు</text>
</svg>'''
save_svg("patam_22_badda_shatru_mesha.svg", svg_22)

# Patam 34: Karma Pathram Structure (Head, Neck, Back)
svg_34 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500 650" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0b0f19" rx="16"/>
  <text x="250" y="35" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fbbf24" text-anchor="middle">34వ పటము: కర్మపత్రము (శిరస్సు, మెడ, వీపు విస్తరణ)</text>
  
  <!-- Head Diagram with 4 Chakras Stack -->
  <ellipse cx="250" cy="180" rx="140" ry="110" fill="rgba(30, 41, 59, 0.6)" stroke="#38bdf8" stroke-width="3"/>
  <text x="250" y="90" font-family="'Outfit', sans-serif" font-size="18" font-weight="bold" fill="#38bdf8" text-anchor="middle">శిరస్సు (నుదురు / ఫాలభాగము)</text>

  <!-- 4 Discs -->
  <ellipse cx="250" cy="120" rx="90" ry="16" fill="rgba(251, 191, 36, 0.3)" stroke="#fbbf24" stroke-width="2"/>
  <text x="250" y="125" font-family="'Outfit', sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">బ్రహ్మచక్రము</text>

  <ellipse cx="250" cy="155" rx="90" ry="16" fill="rgba(56, 189, 248, 0.3)" stroke="#38bdf8" stroke-width="2"/>
  <text x="250" y="160" font-family="'Outfit', sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">కాలచక్రము</text>

  <ellipse cx="250" cy="190" rx="90" ry="16" fill="rgba(239, 68, 68, 0.3)" stroke="#ef4444" stroke-width="2"/>
  <text x="250" y="195" font-family="'Outfit', sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">కర్మచక్రము</text>

  <ellipse cx="250" cy="225" rx="90" ry="16" fill="rgba(16, 185, 129, 0.3)" stroke="#10b981" stroke-width="2"/>
  <text x="250" y="230" font-family="'Outfit', sans-serif" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">గుణచక్రము</text>

  <!-- Spine / Brahma Nadi extension -->
  <rect x="240" y="240" width="20" height="280" fill="url(#spineGrad)" stroke="#fbbf24" stroke-width="2"/>
  <line x1="250" y1="90" x2="250" y2="580" stroke="#fbbf24" stroke-width="3"/>

  <!-- Neck Label -->
  <rect x="130" y="300" width="80" height="30" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="1.5" rx="6"/>
  <text x="170" y="321" font-family="'Outfit', sans-serif" font-size="15" fill="#38bdf8" text-anchor="middle">మెడ</text>
  <line x1="210" y1="315" x2="240" y2="315" stroke="#38bdf8" stroke-width="2"/>

  <!-- Back Label -->
  <rect x="130" y="420" width="80" height="30" fill="rgba(15, 23, 42, 0.9)" stroke="#ef4444" stroke-width="1.5" rx="6"/>
  <text x="170" y="441" font-family="'Outfit', sans-serif" font-size="15" fill="#f87171" text-anchor="middle">వీపు</text>
  <line x1="210" y1="435" x2="240" y2="435" stroke="#ef4444" stroke-width="2"/>

  <!-- Karma Pathram Bracket Label -->
  <path d="M 360 120 L 380 120 L 380 340 L 400 340 L 380 340 L 380 560 L 360 560" fill="none" stroke="#fbbf24" stroke-width="3"/>
  <text x="415" y="345" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fbbf24" text-anchor="start">కర్మపత్రము</text>
</svg>'''
save_svg("patam_34_karmapathram_body.svg", svg_34)

# Patam 47: Focus Light Beam 3-Tiers
svg_47 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 550 550" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0a0e1a" rx="16"/>
  <text x="275" y="35" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fbbf24" text-anchor="middle">47వ పటము: గ్రహ కిరణ ప్రసార విధానము (Focus Light Beam)</text>
  
  <!-- Tier 1: Kaala Chakra Disc & Planet Light -->
  <ellipse cx="275" cy="110" rx="180" ry="35" fill="rgba(56, 189, 248, 0.15)" stroke="#38bdf8" stroke-width="3"/>
  <text x="275" y="90" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">కాలచక్రము (లగ్నము - గ్రహము)</text>
  <circle cx="360" cy="115" r="14" fill="#fbbf24" stroke="#ffffff" stroke-width="2"/>
  <text x="400" y="120" font-family="'Outfit', sans-serif" font-size="14" font-weight="bold" fill="#fbbf24">గ్రహము (Light Source)</text>

  <!-- Light Beam Cone -->
  <polygon points="360,115 180,260 380,260" fill="rgba(251, 191, 36, 0.2)" stroke="rgba(251, 191, 36, 0.5)" stroke-width="1.5"/>

  <!-- Tier 2: Karma Chakra Disc & Karma Rashi -->
  <ellipse cx="275" cy="260" rx="180" ry="35" fill="rgba(239, 68, 68, 0.15)" stroke="#ef4444" stroke-width="3"/>
  <text x="275" y="240" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#f87171" text-anchor="middle">కర్మచక్రము (రాశి - కర్మ లిఖితం)</text>

  <!-- Karma Ray Projection Cone to Tier 3 -->
  <polygon points="280,260 200,410 320,410" fill="rgba(236, 72, 153, 0.25)" stroke="rgba(236, 72, 153, 0.5)" stroke-width="1.5"/>

  <!-- Tier 3: Guna Chakra Disc & Jeeva -->
  <ellipse cx="275" cy="410" rx="180" ry="35" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="3"/>
  <text x="275" y="390" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#34d399" text-anchor="middle">గుణచక్రము (గుణభాగము - జీవుడు)</text>
  <circle cx="260" cy="415" r="14" fill="#34d399" stroke="#ffffff" stroke-width="2"/>
  <text x="260" y="445" font-family="'Outfit', sans-serif" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle">జీవుడు (Karma Experience)</text>
</svg>'''
save_svg("patam_47_focus_light_3tiers.svg", svg_47)

# Patam 50: Planetary Motion Directions (10 Clockwise, Rahu & Kethu Counter-clockwise)
svg_50 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 550" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0f172a" rx="16"/>
  <text x="300" y="35" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fbbf24" text-anchor="middle">50వ పటము: గ్రహముల సంచార దిశలు (10 సవ్య, రాహు-కేతు అపసవ్య)</text>
  
  <rect x="50" y="60" width="500" height="440" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="2"/>
  
  <!-- Clockwise Arrow Ring (Blue) -->
  <path d="M 120 120 L 480 120 L 480 440 L 120 440 Z" fill="none" stroke="#38bdf8" stroke-width="4" stroke-dasharray="10,6"/>
  <polygon points="480,120 465,110 465,130" fill="#38bdf8"/>
  <polygon points="480,440 490,425 470,425" fill="#38bdf8"/>
  <polygon points="120,440 135,450 135,430" fill="#38bdf8"/>
  <polygon points="120,120 110,135 130,135" fill="#38bdf8"/>
  
  <text x="300" y="105" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle">10 గ్రహాలు: సవ్య సంచారము (Clockwise ➔)</text>

  <!-- Counter-Clockwise Arrow Ring (Red) for Rahu & Kethu -->
  <path d="M 180 180 L 420 180 L 420 380 L 180 380 Z" fill="none" stroke="#ef4444" stroke-width="4"/>
  <polygon points="180,180 195,170 195,190" fill="#ef4444"/>
  <polygon points="180,380 170,365 190,365" fill="#ef4444"/>
  <polygon points="420,380 405,390 405,370" fill="#ef4444"/>
  <polygon points="420,180 430,195 410,195" fill="#ef4444"/>

  <text x="300" y="210" font-family="'Outfit', sans-serif" font-size="16" font-weight="bold" fill="#f87171" text-anchor="middle">రాహు-కేతువులు: అపసవ్య సంచారము (Inspector Checkers ⬅)</text>
  
  <rect x="210" y="250" width="180" height="90" fill="rgba(30, 41, 59, 0.95)" stroke="#fbbf24" stroke-width="2" rx="10"/>
  <text x="300" y="285" font-family="'Outfit', sans-serif" font-size="18" font-weight="bold" fill="#fbbf24" text-anchor="middle">కాలచక్ర గమనం</text>
  <text x="300" y="315" font-family="'Outfit', sans-serif" font-size="13" fill="#a7f3d0" text-anchor="middle">ఏకీకృత కర్మ తనిఖీ</text>
</svg>'''
save_svg("patam_50_planet_directions.svg", svg_50)

print("Generated all additional vector SVG diagrams successfully!")