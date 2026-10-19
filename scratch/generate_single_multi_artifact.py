# -*- coding: utf-8 -*-
import json

with open('thraitha_single_planet_bhavas_144.json', 'r', encoding='utf-8') as f:
    single_data = json.load(f)

with open('thraitha_multi_planet_rules_system.json', 'r', encoding='utf-8') as f:
    multi_data = json.load(f)

md = []
md.append('# ద్వాదశ భావములలో ఏక గ్రహ మరియు బహుగ్రహ (1 నుండి 12 గ్రహముల) కలయికల సర్వస్వము\n\n')
md.append('> **మూల గ్రంథము**: *జ్యోతిష్యశాస్త్రము* (రచన: త్రైత సిద్ధాంత ఆదికర్త, ఇందూ ధర్మ ప్రధాత శ్రీశ్రీశ్రీ ఆచార్య ప్రబోధానంద యోగీశ్వరులు)\n')
md.append('> **పరిధి**: ఒక భావములో 1 గ్రహమున్నపుడు (144 ఏక గ్రహ ఫలితాలు), 3 గ్రహాలు, 4 గ్రహాలు... 12 గ్రహాల వరకు ఒకే భావంలో కలిసినపుడు సంభవించే సంశ్లేషిత ఫలితాలు & కారకత్వాల అనుసంధానము.\n\n')

# Mermaid Diagram
md.append('```mermaid\n')
md.append('flowchart TD\n')
md.append('    A["ద్వాదశ భావ కర్మక్షేత్రం (12 Houses)"] --> B["ఏక గ్రహ స్థితి (1 Planet)<br>12 గ్రహాలు x 12 భావాలు = 144 ఫలితాలు"]\n')
md.append('    A --> C["ద్విగ్రహ కలయిక (2 Planets)<br>234 భావ సంయోగాలు (మిత్ర-శత్రు వైరుధ్యాలు)"]\n')
md.append('    A --> D["బహుగ్రహ కూటములు (3 to 12 Planets)"]\n')
md.append('    D --> D1["త్రిగ్రహ కూటమి (3 Planets)<br>3:0, 2:1, 1:2, 0:3 వర్గ నిష్పత్తులు"]\n')
md.append('    D --> D2["చతుర్గ్రహ కూటమి (4 Planets)<br>మహా సామ్రాజ్య యోగం vs అంతర్యుద్ధం"]\n')
md.append('    D --> D3["పంచ - ఏకాదశ కూటములు (5-11 Planets)<br>జీవిత ధ్యేయ కేంద్రీకరణ & యుగ సంధ్య"]\n')
md.append('    D --> D4["ద్వాదశ గ్రహ మహా కూటమి (12 Planets)<br>సర్వ కారకత్వ విస్ఫోటనం & సన్న్యాస బ్రహ్మజ్ఞాన యోగం"]\n')
md.append('```\n\n')
md.append('---\n\n')

# Section 1: Multi-planet principles
md.append('## 1. బహుగ్రహ కూటమి (3 నుండి 12 గ్రహాల కలయిక) సార్వత్రిక సూత్రములు\n\n')
for p in multi_data["engine_architecture"]["foundational_principles"]:
    md.append(f'- {p}\n')
md.append('\n')

# 3 Planets
sec3 = multi_data["multi_planet_rules_by_count"]["3_planets_mix"]
md.append(f"### {sec3['title']}\n\n")
for c in sec3["compositions"]:
    md.append(f"#### ❖ {c['case']} -> *{c['nature']}*\n")
    md.append(f"- **ఫలితము**: {c['result']}\n\n")

# 4 Planets
sec4 = multi_data["multi_planet_rules_by_count"]["4_planets_mix"]
md.append(f"### {sec4['title']}\n\n")
for c in sec4["compositions"]:
    md.append(f"#### ❖ {c['case']} -> *{c['nature']}*\n")
    md.append(f"- **ఫలితము**: {c['result']}\n\n")

# 5 to 11 Planets
sec5 = multi_data["multi_planet_rules_by_count"]["5_to_11_planets_mix"]
md.append(f"### {sec5['title']}\n\n")
for p in sec5["principles"]:
    md.append(f"- {p}\n")
md.append('\n')

# 12 Planets Universal
sec12 = multi_data["multi_planet_rules_by_count"]["12_planets_universal_mix"]
md.append(f"### {sec12['title']}\n\n")
for p in sec12["principles"]:
    md.append(f"- {p}\n")
md.append('\n---\n\n')

# Section 2: 144 Single Planet Bhava Summary
md.append('## 2. ద్వాదశ భావములలో ఏక గ్రహ ఫలితాలు (144 Single Planet Bhava Rules)\n\n')
curr_b = 0
for item in single_data:
    if item["bhava_number"] != curr_b:
        curr_b = item["bhava_number"]
        md.append(f"### {item['bhava_name']}\n")
        md.append(f"> **కారకత్వము**: {item['bhava_core_significance']}\n\n")
        md.append('| గ్రహము | వర్గము | మిత్రుడైనపుడు ఫలితం | శత్రువైనపుడు ఫలితం | క్రియాశీల వస్తువులు | వ్యాధులు |\n')
        md.append('|---|---|---|---|---|---|\n')
    
    p = item["planet_name"]
    pty = item["planet_party"]
    fr = item["friendly_state_result"].replace('\n', ' ')
    en = item["enemy_state_result"].replace('\n', ' ')
    it = item["applied_governed_items"]
    dis = item["applied_diseases"]
    md.append(f"| **{p}** | {pty} | {fr} | {en} | {it} | {dis} |\n")
    md.append('\n')

artifact_path = r'C:\Users\KRISH\.gemini\antigravity\brain\e452eb38-9877-4220-ac5d-43c54ad9cf9a\thraitha_single_and_multi_planet_conjunctions.md'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.writelines(md)

print('Unified single and multi-planet artifact written:', artifact_path)
