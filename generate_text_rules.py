# -*- coding: utf-8 -*-
"""
Generate Master Telugu Rules Text Document.
Aggregates all 144 Bhava Lord Placement Rules, 12 House Meanings, 12 Planet Karakatwas,
Yoga Rules, 40 Topic Mappings, Extracted Rules, and QA Rules into a single UTF-8 text file.
"""

import os
from results_engine.rules_exporter import RulesExporter

def generate_text_rules_doc(output_path="static/YugAstro_All_Telugu_Rules_Master_Document.txt"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    dataset = RulesExporter.get_all_rules_dataset()

    lines = []
    lines.append("==========================================================================================")
    lines.append("త్రైత సిద్ధాంత జ్యోతిష్య శాస్త్ర — సంపూర్ణ తెలుగు ఫలిత నియమావళి (MASTER RULES TEXT DOCUMENT)")
    lines.append("YugAstro & RAVAN ASTRO — 12 Planet System Complete Rules Database")
    lines.append("==========================================================================================")
    lines.append("")
    lines.append(f"మొత్తం భావాధిపతి స్థాన నియమాలు : {dataset['total_lord_rules']} నియమాలు (12×12 మాతృక)")
    lines.append(f"మొత్తం భావార్థాలు               : {dataset['total_houses']} భావాలు")
    lines.append(f"మొత్తం త్రైత గ్రహాలు            : {dataset['total_planets']} గ్రహాలు")
    lines.append(f"మొత్తం విశ్లేషణ రంగాలు        : {dataset['total_topics']} రంగాలు")
    lines.append("")

    # CHAPTER 1: 12 PLANETS
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("అధ్యాయము 1: 12 గ్రహముల త్రైత విధానము & కారకత్వములు")
    lines.append("------------------------------------------------------------------------------------------")
    for idx, p in enumerate(dataset["planets"], 1):
        r_sign = p['ruler_sign'] if p['ruler_sign'] else "విశేష పాలన"
        lines.append(f"{idx}. {p['name']} ({p['party']}) | స్వక్షేత్రం: {r_sign}")
        lines.append(f"   కారకత్వము: {p['karakatwa']}")
        lines.append("")

    # CHAPTER 2: 12 HOUSES
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("అధ్యాయము 2: 12 భావముల ఫలితములు & విశేష అర్థాలు")
    lines.append("------------------------------------------------------------------------------------------")
    for h in dataset["house_meanings"]:
        lines.append(f"★ {h['title']}")
        lines.append(f"   ప్రధాన కారకత్వం : {h['meaning']}")
        if h['shubha']:
            lines.append(f"   🟢 శుభ ఫలిత నియమం : {h['shubha']}")
        if h['paapa']:
            lines.append(f"   🔴 హెచ్చరిక నియమం  : {h['paapa']}")
        lines.append("")

    # CHAPTER 3: 144 LORD PLACEMENT RULES
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("అధ్యాయము 3: 12×12 భావాధిపతుల స్థాన ఫలముల మాతృక (144 సంపూర్ణ నియమాలు)")
    lines.append("------------------------------------------------------------------------------------------")
    for hm in dataset["lord_matrix"]:
        lines.append(f"=== {hm['house_title']} ===")
        for p in hm["placements"]:
            lines.append(f"• [{p['rule_id']}] {p['title']}")
            if p['shubha']:
                lines.append(f"    - శుభం     : {p['shubha']}")
            if p['paapa']:
                lines.append(f"    - హెచ్చరిక : {p['paapa']}")
            if not p['shubha'] and not p['paapa']:
                lines.append("    - సమతుల్య స్థాన ప్రభావం")
        lines.append("")

    # CHAPTER 4: YOGAS
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("అధ్యాయము 4: రాశి చక్ర యోగముల నియమావళి")
    lines.append("------------------------------------------------------------------------------------------")
    for idx, y in enumerate(dataset["yogas"], 1):
        lines.append(f"{idx}. {y.get('name_te')} | మూలం: {y.get('source')} | బలం: {y.get('strength')}")
        lines.append(f"   ఫలితము: {y.get('result_te')}")
        lines.append("")

    # CHAPTER 5: 40 TOPIC MAPPINGS
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("అధ్యాయము 5: 40 రంగాలు & నియమ అనుసంధాన ప్రక్రియ (Topic Evidence Matrix)")
    lines.append("------------------------------------------------------------------------------------------")
    for idx, t in enumerate(dataset["topics"], 1):
        planets = t['allowed_planets'] if t['allowed_planets'] else "విశేష భావాధిపతులు"
        lines.append(f"{idx}. {t['name']} (ID: {t['topic_id']})")
        lines.append(f"   - అనుమతించబడిన భావాలు : {t['allowed_houses']}")
        lines.append(f"   - కారకత్వ గ్రహాలు        : {planets}")
        lines.append(f"   - కీలక పదాలు             : {t['keywords']}")
        lines.append("")

    # CHAPTER 6: EXTRACTED & QA RULES
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("అధ్యాయము 6: విస్తరించబడిన అనుబంధ నియమావళి (Extracted & QA Rules)")
    lines.append("------------------------------------------------------------------------------------------")
    if dataset.get("extracted_rules"):
        lines.append("--- Extracted Rules ---")
        for line in dataset["extracted_rules"][:50]:
            lines.append(f"• {line}")
        lines.append("")

    if dataset.get("qa_rules"):
        lines.append("--- QA Rules ---")
        for line in dataset["qa_rules"][:50]:
            lines.append(f"• {line}")
        lines.append("")

    lines.append("==========================================================================================")
    lines.append("END OF MASTER TELUGU RULES DOCUMENT")
    lines.append("==========================================================================================")

    content = "\n".join(lines)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Also save to root directory for easy access
    root_path = "YugAstro_All_Telugu_Rules_Master_Document.txt"
    with open(root_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Master Telugu Rules text document generated successfully at: {output_path} and {root_path}")
    return output_path

if __name__ == "__main__":
    generate_text_rules_doc()
