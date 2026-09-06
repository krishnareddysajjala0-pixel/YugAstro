# -*- coding: utf-8 -*-
filepath = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\templates\marana_dasa.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

target = "</div>\n{% endblock %}"
section_html = """  <!-- Thraithic 120-Year Dasha & Rebirth Science Section -->
  <div style="background: var(--card-bg, rgba(15, 23, 42, 0.9)); border: 1px solid var(--card-border, rgba(251, 191, 36, 0.25)); border-radius: 18px; padding: 26px; margin-top: 36px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid rgba(251, 191, 36, 0.25); padding-bottom: 12px; margin-bottom: 20px;">
      <h2 style="color: #fbbf24; font-size: 1.35rem; font-weight: 800; margin: 0;">
        <i class="fas fa-microscope" style="margin-right: 8px;"></i> {{ _('త్రైత 120 సంవత్సరముల దశా విజ్ఞానం & దైవజ్ఞాన కర్మ దహనం') }}
      </h2>
      <span style="background: rgba(251, 191, 36, 0.15); color: #fbbf24; border: 1px solid rgba(251, 191, 36, 0.4); padding: 4px 12px; border-radius: 20px; font-weight: bold; font-size: 0.82rem;">
        {{ _('గ్రంథ వివరణ') }}
      </span>
    </div>

    <!-- Diagrams Grid -->
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 20px; margin-bottom: 24px;">
      <div style="background: rgba(0,0,0,0.4); border: 1px solid rgba(56,189,248,0.3); border-radius: 14px; padding: 16px; text-align: center;">
        <img src="/static/images/diagrams/patam_50_planet_directions.svg" alt="50వ పటము: గ్రహముల సంచార దిశలు" style="max-width: 100%; height: auto; border-radius: 10px;">
        <div style="color: #38bdf8; font-weight: bold; font-size: 1rem; margin-top: 10px;">50వ పటము: రాహు-కేతువుల అపసవ్య తనిఖీ దిశ (Checkers)</div>
      </div>
      <div style="background: rgba(0,0,0,0.4); border: 1px solid rgba(16,185,129,0.3); border-radius: 14px; padding: 16px; text-align: center;">
        <img src="/static/images/diagrams/patam_48_108_padas_lagnams.svg" alt="48వ పటము: 108 నక్షత్ర పాదముల సంపూర్ణ అమరిక" style="max-width: 100%; height: auto; border-radius: 10px;">
        <div style="color: #34d399; font-weight: bold; font-size: 1rem; margin-top: 10px;">48వ పటము: 12 లగ్నములలో 108 నక్షత్ర పాదముల అమరిక</div>
      </div>
    </div>

    <!-- Case Studies & Bhagavad Gita Explanation -->
    <div style="font-size: 0.98rem; line-height: 1.8; color: #e2e8f0;">
      <div style="background: rgba(251, 191, 36, 0.08); border-left: 4px solid #fbbf24; border-radius: 0 10px 10px 0; padding: 16px; margin-bottom: 20px;">
        <h4 style="color: #fbbf24; margin-top: 0; font-size: 1.1rem;">🔥 భగవద్గీత 4.37 — జ్ఞానాగ్ని ద్వారా కర్మల దహనం:</h4>
        <p style="margin-bottom: 0; color: #fef3c7;">
          <strong>"యథైధాంసి సమిద్ధోగ్నిర్భస్మసాత్కురుతేర్జాయునా! జ్ఞానాగ్నిః సర్వకర్మాణి భస్మసాత్కురుతే తథా!!" (భగవద్గీత 4.37)</strong><br>
          అజ్ఞాని గ్రహచారంలో ప్రారబ్ద కర్మను తప్పించుకోలేక కష్టసుఖాలు అనుభవిస్తాడు. కానీ దైవజ్ఞానము పొందిన ఆత్మజ్ఞాని దశాచారంలో 'జ్ఞానాగ్ని' ద్వారా తన ప్రారబ్ద కర్మలను భస్మం చేసుకుంటాడు!
        </p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px;">
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 16px;">
          <h4 style="color: #34d399; margin-top: 0;">ప్రముఖ జాతక విశ్లేషణ - శ్రీ సత్యసాయిబాబా:</h4>
          <p style="font-size: 0.92rem; color: #cbd5e1; margin-bottom: 0;">
            జాతకరీత్యా 92 ఏళ్ళు ఆయుష్షు ఉన్నప్పటికీ, తమ జ్ఞానశక్తి ద్వారా 6 ఏళ్ళ కర్మను దహనం చేసుకోవడం వల్ల 86వ ఏటనే అవతార సమాప్తి గావించారు.
          </p>
        </div>
        <div style="background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 16px;">
          <h4 style="color: #f87171; margin-top: 0;">ప్రముఖ జాతక విశ్లేషణ - శ్రీ రాజీవ్ గాంధీ:</h4>
          <p style="font-size: 0.92rem; color: #cbd5e1; margin-bottom: 0;">
            20 ఆగస్టు 1944న తులా లగ్నంలో జన్మించారు. 21 మే 1991న కర్కాటకంలో కుజ-గురు-రవుల కలయిక వల్ల 8వ ఆయు స్థానము మరియు శనిపై కుజ తీవ్ర దాడి జరిగి బాంబు పేలుడులో అకాల మరణం సంభవించింది.
          </p>
        </div>
      </div>
    </div>
  </div>

</div>
{% endblock %}"""

if target in content and 'patam_50_planet_directions.svg' not in content:
    content = content.replace(target, section_html)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully added Dasha secrets section to marana_dasa.html!")
else:
    print("Target not found or already added.")