# -*- coding: utf-8 -*-
filepath = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\templates\chart3_content.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = "<!-- Party Info Message -->"
diagram_html = """        <!-- Thraithic 12 Planets Diagrams Frame -->
        <div style="background: rgba(15, 23, 42, 0.9); border: 2px solid var(--accent-gold, #fbbf24); border-radius: 16px; padding: 20px; margin-bottom: 25px; box-shadow: 0 8px 25px rgba(0,0,0,0.4); text-align: center;">
            <h3 style="color: #fbbf24; font-size: 1.3rem; margin-top: 0; margin-bottom: 16px;">{{ _('ద్వాదశ గ్రహ సిద్ధాంత పటములు (Thraitha Planetary System Diagrams)') }}</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px;">
                <div style="background: rgba(0,0,0,0.4); border: 1px solid rgba(251,191,36,0.3); border-radius: 12px; padding: 12px;">
                    <img src="/static/images/diagrams/patam_14_own_houses.svg" alt="14వ పటము: 12 గ్రహముల స్వంత ఇళ్ళు" style="max-width: 100%; height: auto; border-radius: 8px;">
                    <div style="color: #fbbf24; font-weight: bold; font-size: 0.95rem; margin-top: 8px;">{{ _('14వ పటము: 12 గ్రహముల స్వంత ఇళ్ళు') }}</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); border: 1px solid rgba(16,185,129,0.3); border-radius: 12px; padding: 12px;">
                    <img src="/static/images/diagrams/patam_15_rule21_division.svg" alt="15వ పటము: 2:1 సూత్రము ప్రకారం గ్రహముల విభజన" style="max-width: 100%; height: auto; border-radius: 8px;">
                    <div style="color: #34d399; font-weight: bold; font-size: 0.95rem; margin-top: 8px;">{{ _('15వ పటము: 2:1 గురు-శని వర్గాల విభజన') }}</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); border: 1px solid rgba(239,68,68,0.3); border-radius: 12px; padding: 12px;">
                    <img src="/static/images/diagrams/patam_22_badda_shatru_mesha.svg" alt="22వ పటము: 1x7 బద్దశత్రుత్వ సూత్రము" style="max-width: 100%; height: auto; border-radius: 8px;">
                    <div style="color: #f87171; font-weight: bold; font-size: 0.95rem; margin-top: 8px;">{{ _('22వ పటము: 1 × 7 బద్దశత్రుత్వ సూత్రము') }}</div>
                </div>
                <div style="background: rgba(0,0,0,0.4); border: 1px solid rgba(56,189,248,0.3); border-radius: 12px; padding: 12px;">
                    <img src="/static/images/diagrams/patam_50_planet_directions.svg" alt="50వ పటము: గ్రహముల సంచార దిశలు" style="max-width: 100%; height: auto; border-radius: 8px;">
                    <div style="color: #38bdf8; font-weight: bold; font-size: 0.95rem; margin-top: 8px;">{{ _('50వ పటము: రాహు-కేతువుల అపసవ్య తనిఖీ దిశ') }}</div>
                </div>
            </div>
        </div>

"""

if target in content and 'patam_14_own_houses.svg' not in content:
    content = content.replace(target, diagram_html + target)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added diagram cards to chart3_content.html!")
else:
    print("Target not found or already added.")