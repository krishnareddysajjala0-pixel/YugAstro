# -*- coding: utf-8 -*-
import json

with open('thraitha_planet_karakatvas_complete.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

md = []
md.append('# శ్రీశ్రీశ్రీ ఆచార్య ప్రబోధానంద యోగీశ్వరుల ద్వాదశ గ్రహ సమగ్ర ఆధీనములు, కారకత్వములు & రోగముల సర్వస్వము\n\n')
md.append('> **మూల గ్రంథము**: *జ్యోతిష్యశాస్త్రము* (రచన: త్రైత సిద్ధాంత ఆదికర్త, సంచలనాత్మక రచయిత, ఇందూ ధర్మ ప్రధాత శ్రీశ్రీశ్రీ ఆచార్య ప్రబోధానంద యోగీశ్వరులు)\n')
md.append('> **పరిధి**: కాలచక్రంలోని 12 గ్రహముల (గురు వర్గము & శని వర్గము) సంపూర్ణ ఆధీన వస్తువులు, సాధనాలు, ప్రదేశాలు, జీవులు, వృత్తులు, సంబంధాలు, రోగాలు, ఫలితాలు.\n\n')

md.append('## విషయ సూచిక (Planetary Index)\n\n')
md.append('| క్ర.సం | గ్రహము | వర్గము / కూటమి | స్వక్షేత్రం | రత్నము | ధాన్యము | దినము / వారం | దిశ |\n')
md.append('|---|---|---|---|---|---|---|---|\n')

for idx, (p_name, p) in enumerate(data.items(), 1):
    name = p['planet_name']
    party = p['party']
    sign = p['own_sign']
    gem = p['gem']
    grain = p['grain']
    day = p['day']
    direction = p['direction']
    md.append(f'| {idx} | **{name}** | {party} | {sign} | {gem} | {grain} | {day} | {direction} |\n')

md.append('\n---\n\n')

for idx, (p_name, p) in enumerate(data.items(), 1):
    name = p['planet_name']
    aliases = ', '.join(p['aliases'])
    party = p['party']
    sign = p['own_sign']
    gem = p['gem']
    grain = p['grain']
    direction = p['direction']
    day = p['day']
    color = p['color']
    hands = p['aspect_hands']
    notes = p['thraitha_siddhanta_notes']

    md.append(f'## {idx}. {name} ({party})\n\n')
    md.append(f'- **ఇతర నామాలు**: {aliases}\n')
    md.append(f'- **స్వక్షేత్ర రాశి**: {sign} | **అధిష్టాన రత్నం**: {gem} | **ధాన్యం**: {grain}\n')
    md.append(f'- **అధీన దిశ**: {direction} | **వారం/దినం**: {day} | **రంగు**: {color}\n')
    md.append(f'- **దృష్టి / చేతులు**: {hands}\n\n')
    
    md.append('### 1. ఆధీనంలో ఉన్న సమస్త స్థూల వస్తువులు & పదార్థాలు (Governed Physical Items)\n')
    for item in p['governed_physical_items']:
        md.append(f'- {item}\n')
    md.append('\n')

    md.append('### 2. ఆధీనంలో ఉన్న ప్రదేశాలు, భవనాలు & భూములు (Governed Places & Lands)\n')
    for pl in p['governed_places_and_lands']:
        md.append(f'- {pl}\n')
    md.append('\n')

    md.append('### 3. ఆధీనంలో ఉన్న జీవులు, జంతువులు, చెట్లు & పంటలు (Living Beings, Flora & Fauna)\n')
    for bio in p['governed_living_beings_flora_fauna']:
        md.append(f'- {bio}\n')
    md.append('\n')

    md.append('### 4. ఆధీనంలో ఉన్న వృత్తులు, వ్యాపారాలు, ఉద్యోగాలు & విద్యలు (Professions & Trades)\n')
    for prof in p['governed_professions_and_trades']:
        md.append(f'- {prof}\n')
    md.append('\n')

    md.append('### 5. ఆధీనంలో ఉన్న సంబంధాలు & వ్యక్తులు (Relationships & People)\n')
    for rel in p['governed_relationships_and_people']:
        md.append(f'- {rel}\n')
    md.append('\n')

    md.append('### 6. ఆధీనంలో ఉన్న గుణాలు, స్వభావాలు & లౌకిక విషయాలు (Subtle & Behavioral Traits)\n')
    for trait in p['governed_subtle_and_behavioral_traits']:
        md.append(f'- {trait}\n')
    md.append('\n')

    md.append('### 7. శారీరక భాగాలు & సమస్త రోగాలు/రుగ్మతలు (Body Parts & Complete Diseases)\n')
    body_parts = ', '.join(p['governed_body_parts_and_diseases']['body_parts'])
    md.append(f'**శారీరక భాగాలు**: {body_parts}\n\n')
    md.append('**రోగములు / రుగ్మతలు**:\n')
    for dis in p['governed_body_parts_and_diseases']['diseases']:
        md.append(f'- ⚠️ {dis}\n')
    md.append('\n')

    md.append('### 8. మిత్రుడై అనుకూలించినపుడు కలిగే సమస్త శుభ ఫలితాలు / ఉపయోగపడేవి (Beneficial Results)\n')
    for ben in p['beneficial_manifestations']:
        md.append(f'- ✅ {ben}\n')
    md.append('\n')

    md.append('### 9. శత్రువై వ్యతిరేకించినపుడు కలిగే సమస్త అశుభ ఫలితాలు / నష్టం చేసేవి (Harmful Results)\n')
    for harm in p['harmful_manifestations']:
        md.append(f'- ❌ {harm}\n')
    md.append('\n')

    md.append(f'> [!NOTE]\n> **త్రైత సిద్ధాంత విశేష పరిశీలన**: {notes}\n\n')
    md.append('---\n\n')

artifact_path = r'C:\Users\KRISH\.gemini\antigravity\brain\e452eb38-9877-4220-ac5d-43c54ad9cf9a\thraitha_planet_karakatvas_diseases.md'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.writelines(md)

print('Artifact updated successfully at:', artifact_path)
