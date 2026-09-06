import os

out_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\static\images\diagrams"
os.makedirs(out_dir, exist_ok=True)

def save_svg(filename, content):
    filepath = os.path.join(out_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip())
    print(f"Saved: {filename}")

# Patam 16: Mesha / Meena Lagnam Friends & Enemies Chart
svg_16 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 550" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0f172a" rx="16"/>
  <text x="300" y="35" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fbbf24" text-anchor="middle">16వ పటము: మేష / మీన లగ్నముల మిత్ర-శత్రు గ్రహ విభజన (2:1 సూత్రం)</text>

  <!-- Left: Friends (Green) -->
  <rect x="30" y="60" width="250" height="440" fill="rgba(16, 185, 129, 0.1)" stroke="#10b981" stroke-width="2" rx="12"/>
  <text x="155" y="95" font-family="'Outfit', sans-serif" font-size="18" font-weight="bold" fill="#34d399" text-anchor="middle">🟢 మిత్రులు (పుణ్య పాలిత)</text>
  <line x1="45" y1="110" x2="265" y2="110" stroke="#10b981" stroke-width="1.5"/>
  <text x="55" y="145" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">12. గురువు (మీనం)</text>
  <text x="55" y="185" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">1.  కుజుడు (మేషం)</text>
  <text x="55" y="225" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">4.  చంద్రుడు (కర్కాటక)</text>
  <text x="55" y="265" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">5.  సూర్యుడు (సింహ)</text>
  <text x="55" y="305" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">8.  భూమి (వృశ్చిక)</text>
  <text x="55" y="345" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">9.  కేతువు (ధనూ)</text>

  <!-- Right: Enemies (Red) -->
  <rect x="320" y="60" width="250" height="440" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="2" rx="12"/>
  <text x="445" y="95" font-family="'Outfit', sans-serif" font-size="18" font-weight="bold" fill="#f87171" text-anchor="middle">🔴 శత్రువులు (పాప పాలిత)</text>
  <line x1="335" y1="110" x2="555" y2="110" stroke="#ef4444" stroke-width="1.5"/>
  <text x="345" y="145" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">2.  మిత్ర (వృషభం)</text>
  <text x="345" y="185" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">3.  చిత్ర (మిథునం)</text>
  <text x="345" y="225" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">6.  బుధుడు (కన్య)</text>
  <text x="345" y="265" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">7.  శుక్రుడు (తుల)</text>
  <text x="345" y="305" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">10. రాహువు (మకర)</text>
  <text x="345" y="345" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">11. శని (కుంభ)</text>
</svg>'''
save_svg("patam_16_mesha_meena_lagnam.svg", svg_16)

# Patam 17: Vrishabha / Mithuna Lagnam Friends & Enemies Chart
svg_17 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 550" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0f172a" rx="16"/>
  <text x="300" y="35" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fbbf24" text-anchor="middle">17వ పటము: వృషభ / మిథున లగ్నముల మిత్ర-శత్రు గ్రహ విభజన</text>

  <!-- Left: Friends (Green) -->
  <rect x="30" y="60" width="250" height="440" fill="rgba(16, 185, 129, 0.1)" stroke="#10b981" stroke-width="2" rx="12"/>
  <text x="155" y="95" font-family="'Outfit', sans-serif" font-size="18" font-weight="bold" fill="#34d399" text-anchor="middle">🟢 మిత్రులు (పుణ్య పాలిత)</text>
  <line x1="45" y1="110" x2="265" y2="110" stroke="#10b981" stroke-width="1.5"/>
  <text x="55" y="145" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">2.  మిత్ర (వృషభం)</text>
  <text x="55" y="185" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">3.  చిత్ర (మిథునం)</text>
  <text x="55" y="225" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">6.  బుధుడు (కన్య)</text>
  <text x="55" y="265" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">7.  శుక్రుడు (తుల)</text>
  <text x="55" y="305" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">10. రాహువు (మకర)</text>
  <text x="55" y="345" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">11. శని (కుంభ)</text>

  <!-- Right: Enemies (Red) -->
  <rect x="320" y="60" width="250" height="440" fill="rgba(239, 68, 68, 0.1)" stroke="#ef4444" stroke-width="2" rx="12"/>
  <text x="445" y="95" font-family="'Outfit', sans-serif" font-size="18" font-weight="bold" fill="#f87171" text-anchor="middle">🔴 శత్రువులు (పాప పాలిత)</text>
  <line x1="335" y1="110" x2="555" y2="110" stroke="#ef4444" stroke-width="1.5"/>
  <text x="345" y="145" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">12. గురువు (మీనం)</text>
  <text x="345" y="185" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">1.  కుజుడు (మేషం)</text>
  <text x="345" y="225" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">4.  చంద్రుడు (కర్కాటక)</text>
  <text x="345" y="265" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">5.  సూర్యుడు (సింహ)</text>
  <text x="345" y="305" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">8.  భూమి (వృశ్చిక)</text>
  <text x="345" y="345" font-family="'Outfit', sans-serif" font-size="16" fill="#ffffff">9.  కేతువు (ధనూ)</text>
</svg>'''
save_svg("patam_17_vrishabha_mithuna_lagnam.svg", svg_17)

# Patam 35: Angi & Ardhangi Division
svg_35 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 500" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0b0f19" rx="16"/>
  <text x="300" y="40" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fbbf24" text-anchor="middle">35వ పటము: కర్మపత్రములో అంగీ (1-6) మరియు అర్ధాంగి (7-12) విభజన</text>
  
  <rect x="40" y="80" width="240" height="360" fill="rgba(56, 189, 248, 0.1)" stroke="#38bdf8" stroke-width="2" rx="12"/>
  <text x="160" y="115" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#38bdf8" text-anchor="middle">అంగీ (Angi - Body/Self)</text>
  <text x="160" y="140" font-family="'Outfit', sans-serif" font-size="14" fill="#93c5fd" text-anchor="middle">1వ స్థానము నుండి 6వ స్థానము వరకు</text>
  <line x1="60" y1="155" x2="260" y2="155" stroke="#38bdf8" stroke-width="1.5"/>
  <text x="70" y="195" font-family="'Outfit', sans-serif" font-size="15" fill="#ffffff">1వ స్థానం: శరీరాది ఆరంభం</text>
  <text x="70" y="235" font-family="'Outfit', sans-serif" font-size="15" fill="#ffffff">2వ స్థానం: అజ్ఞాన జీవిత కాలం</text>
  <text x="70" y="275" font-family="'Outfit', sans-serif" font-size="15" fill="#ffffff">3వ స్థానం: ప్రపంచ ధనం</text>
  <text x="70" y="315" font-family="'Outfit', sans-serif" font-size="15" fill="#38bdf8" font-weight="bold">4వ స్థానం: అంగీ కేంద్రం (ఆస్తి)</text>
  <text x="70" y="355" font-family="'Outfit', sans-serif" font-size="15" fill="#ffffff">5వ స్థానం: ప్రపంచ విద్య/జ్ఞానం</text>
  <text x="70" y="395" font-family="'Outfit', sans-serif" font-size="15" fill="#ffffff">6వ స్థానం: శత్రు, ఋణ, రోగములు</text>

  <rect x="320" y="80" width="240" height="360" fill="rgba(236, 72, 153, 0.1)" stroke="#ec4899" stroke-width="2" rx="12"/>
  <text x="440" y="115" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#ec4899" text-anchor="middle">అర్ధాంగి (Spouse/Divine)</text>
  <text x="440" y="140" font-family="'Outfit', sans-serif" font-size="14" fill="#fbcfe8" text-anchor="middle">7వ స్థానము నుండి 12వ స్థానము వరకు</text>
  <line x1="340" y1="155" x2="540" y2="155" stroke="#ec4899" stroke-width="1.5"/>
  <text x="350" y="195" font-family="'Outfit', sans-serif" font-size="15" fill="#ffffff">7వ స్థానం: భార్య/వివాహ కర్మ</text>
  <text x="350" y="235" font-family="'Outfit', sans-serif" font-size="15" fill="#ffffff">8వ స్థానం: జ్ఞాన జీవిత కాలం</text>
  <text x="350" y="275" font-family="'Outfit', sans-serif" font-size="15" fill="#ffffff">9వ స్థానం: పరమాత్మ ధనం</text>
  <text x="350" y="315" font-family="'Outfit', sans-serif" font-size="15" fill="#ec4899" font-weight="bold">10వ స్థానం: అర్ధాంగి కేంద్రం (కీర్తి)</text>
  <text x="350" y="355" font-family="'Outfit', sans-serif" font-size="15" fill="#ffffff">11వ స్థానం: దైవజ్ఞాన గ్రహీత</text>
  <text x="350" y="395" font-family="'Outfit', sans-serif" font-size="15" fill="#ffffff">12వ స్థానం: శరీరాంత్యం (మరణం)</text>
</svg>'''
save_svg("patam_35_angi_ardhangi.svg", svg_35)

# Patam 48: 108 Nakshatra Padas across 12 Lagnams Master Diagram
svg_48 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 550" width="100%" height="100%">
  <rect width="100%" height="100%" fill="#0a0e1a" rx="16"/>
  <text x="350" y="35" font-family="'Outfit', sans-serif" font-size="20" font-weight="bold" fill="#fbbf24" text-anchor="middle">48వ పటము: 12 లగ్నములలో 108 నక్షత్ర పాదముల సంపూర్ణ అమరిక</text>
  
  <rect x="30" y="60" width="640" height="450" fill="rgba(15, 23, 42, 0.9)" stroke="#38bdf8" stroke-width="2" rx="12"/>
  
  <!-- 4 Columns, 3 Rows grid of Lagnams -->
  <g font-family="'Outfit', sans-serif" font-size="13" fill="#e2e8f0">
    <!-- Row 1 -->
    <rect x="45" y="75" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="115" y="95" font-size="15" font-weight="bold" fill="#ef4444" text-anchor="middle">మేషం (9 పాదాలు)</text>
    <text x="55" y="120" fill="#a7f3d0">• అశ్విని: 4</text>
    <text x="55" y="140" fill="#a7f3d0">• భరణి: 4</text>
    <text x="55" y="160" fill="#a7f3d0">• కృత్తిక: 1</text>

    <rect x="195" y="75" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="265" y="95" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">వృషభం (9 పాదాలు)</text>
    <text x="205" y="120" fill="#a7f3d0">• కృత్తిక: 3</text>
    <text x="205" y="140" fill="#a7f3d0">• రోహిణి: 4</text>
    <text x="205" y="160" fill="#a7f3d0">• మృగశిర: 2</text>

    <rect x="345" y="75" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="415" y="95" font-size="15" font-weight="bold" fill="#fbbf24" text-anchor="middle">మిథునం (9 పాదాలు)</text>
    <text x="355" y="120" fill="#a7f3d0">• మృగశిర: 2</text>
    <text x="355" y="140" fill="#a7f3d0">• ఆరుద్ర: 4</text>
    <text x="355" y="160" fill="#a7f3d0">• పునర్వసు: 3</text>

    <rect x="495" y="75" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="565" y="95" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">కర్కాటకం (9 పాదాలు)</text>
    <text x="505" y="120" fill="#a7f3d0">• పునర్వసు: 1</text>
    <text x="505" y="140" fill="#a7f3d0">• పుష్యమి: 4</text>
    <text x="505" y="160" fill="#a7f3d0">• ఆశ్లేష: 4</text>

    <!-- Row 2 -->
    <rect x="45" y="210" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="115" y="230" font-size="15" font-weight="bold" fill="#f59e0b" text-anchor="middle">సింహం (9 పాదాలు)</text>
    <text x="55" y="255" fill="#a7f3d0">• మఖ: 4</text>
    <text x="55" y="275" fill="#a7f3d0">• పుబ్బ: 4</text>
    <text x="55" y="295" fill="#a7f3d0">• ఉత్తర: 1</text>

    <rect x="195" y="210" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="265" y="230" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">కన్య (9 పాదాలు)</text>
    <text x="205" y="255" fill="#a7f3d0">• ఉత్తర: 3</text>
    <text x="205" y="275" fill="#a7f3d0">• హస్త: 4</text>
    <text x="205" y="295" fill="#a7f3d0">• చిత్త: 2</text>

    <rect x="345" y="210" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="415" y="230" font-size="15" font-weight="bold" fill="#ec4899" text-anchor="middle">తుల (9 పాదాలు)</text>
    <text x="355" y="255" fill="#a7f3d0">• చిత్త: 2</text>
    <text x="355" y="275" fill="#a7f3d0">• స్వాతి: 4</text>
    <text x="355" y="295" fill="#a7f3d0">• విశాఖ: 3</text>

    <rect x="495" y="210" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="565" y="230" font-size="15" font-weight="bold" fill="#38bdf8" text-anchor="middle">వృశ్చికం (9 పాదాలు)</text>
    <text x="505" y="255" fill="#a7f3d0">• విశాఖ: 1</text>
    <text x="505" y="275" fill="#a7f3d0">• అనురాధ: 4</text>
    <text x="505" y="295" fill="#a7f3d0">• జ్యేష్ఠ: 4</text>

    <!-- Row 3 -->
    <rect x="45" y="345" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="115" y="365" font-size="15" font-weight="bold" fill="#a855f7" text-anchor="middle">ధనస్సు (9 పాదాలు)</text>
    <text x="55" y="390" fill="#a7f3d0">• మూల: 4</text>
    <text x="55" y="410" fill="#a7f3d0">• పూర్వాషాఢ: 4</text>
    <text x="55" y="430" fill="#a7f3d0">• ఉత్తరాషాఢ: 1</text>

    <rect x="195" y="345" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="265" y="365" font-size="15" font-weight="bold" fill="#6366f1" text-anchor="middle">మకరం (9 పాదాలు)</text>
    <text x="205" y="390" fill="#a7f3d0">• ఉత్తరాషాఢ: 3</text>
    <text x="205" y="410" fill="#a7f3d0">• శ్రవణం: 4</text>
    <text x="205" y="430" fill="#a7f3d0">• ధనిష్ఠ: 2</text>

    <rect x="345" y="345" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="415" y="365" font-size="15" font-weight="bold" fill="#94a3b8" text-anchor="middle">కుంభం (9 పాదాలు)</text>
    <text x="355" y="390" fill="#a7f3d0">• ధనిష్ఠ: 2</text>
    <text x="355" y="410" fill="#a7f3d0">• శతభిషం: 4</text>
    <text x="355" y="430" fill="#a7f3d0">• పూర్వాభాద్ర: 3</text>

    <rect x="495" y="345" width="140" height="120" fill="rgba(30,41,59,0.8)" stroke="#334155" rx="6"/>
    <text x="565" y="365" font-size="15" font-weight="bold" fill="#34d399" text-anchor="middle">మీనం (9 పాదాలు)</text>
    <text x="505" y="390" fill="#a7f3d0">• పూర్వాభాద్ర: 1</text>
    <text x="505" y="410" fill="#a7f3d0">• ఉత్తరాభాద్ర: 4</text>
    <text x="505" y="430" fill="#a7f3d0">• రేవతి: 4</text>
  </g>
</svg>'''
save_svg("patam_48_108_padas_lagnams.svg", svg_48)

print("Batch 2 SVG generation finished successfully!")