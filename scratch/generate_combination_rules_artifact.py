# -*- coding: utf-8 -*-
import json

with open('thraitha_astrology_combination_rules.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

md = []
md.append('# శ్రీశ్రీశ్రీ ఆచార్య ప్రబోధానంద యోగీశ్వరుల "జ్యోతిష్యశాస్త్రము" - ప్రత్యేక గ్రహ కలయికలు, భావ సూత్రాలు & ఉదాహరణ జాతక విశ్లేషణలు\n\n')
md.append('> **మూల గ్రంథము**: *జ్యోతిష్యశాస్త్రము* (రచన: త్రైత సిద్ధాంత ఆదికర్త, సంచలనాత్మక రచయిత, ఇందూ ధర్మ ప్రధాత శ్రీశ్రీశ్రీ ఆచార్య ప్రబోధానంద యోగీశ్వరులు)\n')
md.append('> **పరిధి**: కుజ-శుక్ర కలయిక, సంతాన నిర్ధారణ సూత్రాలు, ఆయుష్షు-రక్తపాత మరణ సూత్రాలు, గృహ-జల యోగాలు, దయ్యాలు-రోగాలు, ఉదాహరణ జాతకాలు (గాంధీ, రాజీవ్ గాంధీ, ప్రవక్త మహమ్మద్, జగన్).\n\n')

# Diagram: Kendra-Kona & Angi-Ardhangi
md.append('```mermaid\n')
md.append('flowchart TD\n')
md.append('    subgraph KarmaChakra["ద్వాదశ భావ కర్మచక్రము (12 Houses)"]\n')
md.append('        Angi["అంగీ (1 నుండి 6 భావములు)<br>జాతకుని స్థూల శరీరము, ధనము, ఇల్లు, రోగాలు"]\n')
md.append('        Ardhangi["అర్ధాంగీ (7 నుండి 12 భావములు)<br>భార్య, సంసారము, ఆయుష్షు, కర్మ, మోక్షము"]\n')
md.append('    end\n')
md.append('    subgraph Yogas["ప్రధాన త్రైత సూత్రాలు"]\n')
md.append('        KujaSukra["కుజ-శుక్ర కలయిక<br>యౌవన vs కళత్ర శత్రుత్వం -> దాంపత్య కలహాలు"]\n')
md.append('        Santhanam["సంతాన విచారణ (5వ భావం)<br>పిల్లల కోసం: చంద్రుడు | పుత్రుల కోసం: గురువు"]\n')
md.append('        Ayush["ఆయుష్షు & మరణం (8వ భావం)<br>శని (ఆయుష్షు) + కుజుడు (ఆయుధం/రక్తం)"]\n')
md.append('    end\n')
md.append('    KarmaChakra --> Yogas\n')
md.append('```\n\n')
md.append('---\n\n')

for sec_key, sec in data.items():
    md.append(f"## {sec['title']}\n\n")
    md.append(f"> {sec['description']}\n\n")
    
    for idx, r in enumerate(sec['rules'], 1):
        md.append(f"### {idx}. {r['rule_name']}\n\n")
        md.append(f"- **గ్రంథ ఆధార పేజీ**: `{r['reference_page']}`\n\n")
        md.append("**ప్రధాన సూత్రాలు & ఫలితాలు**:\n")
        for p in r['principles']:
            md.append(f"- {p}\n")
        md.append("\n")
    md.append("---\n\n")

artifact_path = r'C:\Users\KRISH\.gemini\antigravity\brain\e452eb38-9877-4220-ac5d-43c54ad9cf9a\thraitha_astrology_combination_rules.md'
with open(artifact_path, 'w', encoding='utf-8') as f:
    f.writelines(md)

print('Combination Rules Artifact generated successfully at:', artifact_path)
