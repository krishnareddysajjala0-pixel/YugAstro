# -*- coding: utf-8 -*-
"""
Generate Markdown Artifact for 12 Planets Karakatvas, Governed Items, and Diseases.
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

artifact_dir = r"C:\Users\KRISH\.gemini\antigravity\brain\e452eb38-9877-4220-ac5d-43c54ad9cf9a"
artifact_file = os.path.join(artifact_dir, "thraitha_planet_karakatvas_diseases.md")

with open(r"C:\Users\KRISH\Documents\GitHub\YugAstro\thraitha_planet_karakatvas_complete.json", "r", encoding="utf-8") as f:
    data = json.load(f)

lines = []
lines.append("# త్రైత సిద్ధాంతం: ద్వాదశ గ్రహముల కారకత్వములు, వస్తువులు, ఉపయోగాలు, నష్టాలు & రోగాలు\n")
lines.append("> **ఆధార గ్రంథము**: 'జ్యోతిష్య శాస్త్రము (శాస్త్రమా? మూఢనమ్మకమా?)' - శ్రీ శ్రీ శ్రీ ఆచార్య ప్రబోధానంద యోగీశ్వరులు  \n")
lines.append("> **అధ్యాయము 41**: *గ్రహములవద్ద ఏమీ ఉండవా?* (గ్రంథం పేజీలు 172 – 212)\n\n")
lines.append("---\n")

lines.append("## సిద్ధాంత సూత్రము (Core Principle)\n")
lines.append("భూమిపై మనిషికి ఉపయోగపడేవి, నష్టం చేసేవి, సమస్త వస్తువులు, ధాన్యాలు, రత్నాలు, లోహాలు మరియు శరీర రోగాలు అన్నీ పన్నెండు గ్రహాలలో ఏదో ఒక గ్రహ ఆధీనంలో కలవు.\n")
lines.append("- జాతక లగ్నమును బట్టి గ్రహము **మిత్రుడు (శుభుడు)** అయినప్పుడు: ఆ గ్రహ ఆధీనంలోని ఉత్తమ సంపదలు, ఉపయోగాలు, రక్షణ, ఉన్నత పదవులు లభిస్తాయి.\n")
lines.append("- గ్రహము **శత్రువు (పాపి)** అయినప్పుడు: ఆ గ్రహ ఆధీనంలోని నష్టాలు, వ్యసనాలు, మోసాలు మరియు నిర్దిష్ట రోగాలు/వ్యాధులు ఆ భావముపై దాడి చేస్తాయి.\n\n")
lines.append("---\n")

for idx, (pname, pinfo) in enumerate(data.items(), 1):
    lines.append(f"## {idx}. {pname} ({', '.join(pinfo['aliases'])})\n")
    lines.append(f"- **వర్గము**: `{pinfo['party']}` | **స్వక్షేత్రము**: `{pinfo['own_sign']}`\n")
    lines.append(f"- **రత్నము**: `{pinfo['gem']}` | **ధాన్యము**: `{pinfo['grain']}`\n")
    lines.append(f"- **దిశ**: `{pinfo['direction']}` | **దినము/వారము**: `{pinfo['day']}`\n\n")

    lines.append("### 1. ఆధీనంలో ఉన్న సమస్త విషయాలు & వస్తువులు\n")
    lines.append(", ".join(pinfo['governed_items']) + ".\n\n")

    lines.append("### 2. మనిషికి ఉపయోగపడేవి (మిత్రుడైతే లభించే శుభ ఫలితాలు)\n")
    for b in pinfo['beneficial_manifestations']:
        lines.append(f"- ✅ **{b}**\n")
    lines.append("\n")

    lines.append("### 3. మనిషికి నష్టం చేసేవి (శత్రువైతే కలిగే అశుభ ఫలితాలు)\n")
    for h in pinfo['harmful_manifestations']:
        lines.append(f"- ⚠️ **{h}**\n")
    lines.append("\n")

    lines.append("### 4. ఈ గ్రహము వలన సంభవించే నిర్దిష్ట రోగములు / వ్యాధులు\n")
    for d in pinfo['diseases']:
        lines.append(f"- 🩺 **{d}**\n")
    lines.append("\n---\n\n")

with open(artifact_file, "w", encoding="utf-8") as out:
    out.write("".join(lines))

print(f"Generated artifact at: {artifact_file}")
