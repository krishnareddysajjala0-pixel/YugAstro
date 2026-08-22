# -*- coding: utf-8 -*-
"""
Script to extract ALL Astrological Rules from YugAstro / Timeastro databases
into a clean, comprehensive text document: ALL_ASTROLOGICAL_RULES.txt.
"""

import json
import os

def generate_all_rules_txt():
    base_dir = os.path.dirname(__file__)
    output_path = os.path.join(base_dir, "ALL_ASTROLOGICAL_RULES.txt")

    # Load JSON files
    bhava_lord_path = os.path.join(base_dir, "bhava_lord_rules.json")
    detailed_meanings_path = os.path.join(base_dir, "detailed_bhava_meanings.json")
    astro_constants_path = os.path.join(base_dir, "astro_constants.json")

    bhava_lord_rules = {}
    if os.path.exists(bhava_lord_path):
        with open(bhava_lord_path, 'r', encoding='utf-8') as f:
            bhava_lord_rules = json.load(f)

    detailed_meanings = {}
    if os.path.exists(detailed_meanings_path):
        with open(detailed_meanings_path, 'r', encoding='utf-8') as f:
            detailed_meanings = json.load(f)

    astro_constants = {}
    if os.path.exists(astro_constants_path):
        with open(astro_constants_path, 'r', encoding='utf-8') as f:
            astro_constants = json.load(f)

    lines = []
    lines.append("==========================================================================================")
    lines.append("                         RAVAN ASTRO / YUGASTRO - 100% COMPLETE RULE HANDBOOK             ")
    lines.append("==========================================================================================")
    lines.append("")

    # Section 1: Core System & Planet Rulerships
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("SECTION 1: 12-PLANET TRITHA SIDDHANTHA SYSTEM & RULERSHIPS (త్రైత సిద్ధాంత 12 గ్రహములు)")
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("1. సూర్యుడు    -> సింహ రాశి అధిపతి")
    lines.append("2. చంద్రుడు   -> కర్కాటక రాశి అధిపతి")
    lines.append("3. కుజుడు     -> మేష రాశి అధిపతి")
    lines.append("4. బుధుడు     -> కన్యా రాశి అధిపతి")
    lines.append("5. గురు       -> మీన రాశి అధిపతి")
    lines.append("6. శుక్రుడు    -> తులా రాశి అధిపతి")
    lines.append("7. శని        -> కుంభ రాశి అధిపతి")
    lines.append("8. రాహు      -> మకర రాశి అధిపతి")
    lines.append("9. కేతు      -> ధనూ రాశి అధిపతి")
    lines.append("10. భూమి      -> వృశ్చిక రాశి అధిపతి")
    lines.append("11. మిత్ర     -> వృషభ రాశి అధిపతి")
    lines.append("12. చిత్ర     -> మిథున రాశి అధిపతి")
    lines.append("")
    lines.append("గురు వర్గ లగ్నములు: మీనం, మేషం, కర్కాటకం, సింహం, వృశ్చికం, ధనస్సు")
    lines.append("గురు వర్గ గ్రహములు: సూర్యుడు, భూమి, కుజుడు, గురు, కేతు, చంద్రుడు")
    lines.append("శని వర్గ గ్రహములు: శని, రాహు, బుధుడు, శుక్రుడు, మిత్ర, చిత్ర")
    lines.append("")

    # Section 2: Detailed Bhava Meanings (12 Houses)
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("SECTION 2: DWADASA BHAVA DETAILED MEANINGS (12 భావముల ఫలితములు)")
    lines.append("------------------------------------------------------------------------------------------")
    for h_num in range(1, 13):
        h_str = str(h_num)
        b_info = detailed_meanings.get(h_str, {})
        title = b_info.get("title", f"{h_num}వ భావం")
        meaning = b_info.get("meaning", "")
        shubha = b_info.get("shubha", "")
        paapa = b_info.get("paapa", "")
        neutral = b_info.get("neutral", "")

        lines.append(f"★ [భావము {h_num}] {title}")
        lines.append(f"   - కారకత్వములు (Topics): {meaning}")
        if shubha:
            lines.append(f"   - శుభ ఫలితము (Shubha): {shubha}")
        if paapa:
            lines.append(f"   - పాప/హెచ్చరిక ఫలితము (Paapa): {paapa}")
        if neutral:
            lines.append(f"   - సమతుల్య ఫలితము (Neutral): {neutral}")
        lines.append("")

    # Section 3: Bhava Lord Placement Matrix (144 Rules)
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("SECTION 3: BHAVA LORD PLACEMENT MATRIX (144 భావాధిపతుల స్థాన ఫలితములు)")
    lines.append("------------------------------------------------------------------------------------------")
    rule_count = 0
    for h_lord in range(1, 13):
        lines.append(f"=== {h_lord}వ భావాధిపతి విశ్లేషణ ===")
        for p_house in range(1, 13):
            entry = bhava_lord_rules.get(str(h_lord), {}).get(str(p_house), {})
            shubha_text = entry.get("shubha", "").strip()
            paapa_text = entry.get("paapa", "").strip()

            if shubha_text or paapa_text:
                rule_count += 1
                lines.append(f"[{h_lord}వ భావాధిపతి {p_house}వ భావంలో ఉన్నప్పుడు]:")
                if shubha_text:
                    lines.append(f"   • శుభ ఫలితము (మిత్ర గ్రహమైనచో): {shubha_text}")
                if paapa_text:
                    lines.append(f"   • పాప ఫలితము (శత్రు గ్రహమైనచో): {paapa_text}")
        lines.append("")

    # Section 4: Specific Planetary Life Scenario Rules (Timeastro Specific Rules)
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("SECTION 4: PLANETARY LIFE SCENARIO RULES (ప్రత్యేక గ్రహ స్థితి జీవిత ఫలితములు)")
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("1. [4వ భావము - సూర్యుడు (శుభ)]: సూర్యుడు 4వ లగ్నములో ఉండటమువలన మీకు పై అంతస్థు భవనములు కట్టించు ప్రేరణ చేయును. ఒకవేళ పేదవారైనా ఆ ఇంటిలో నివాసము కల్గునట్లు చేయును.")
    lines.append("2. [4వ భావము - సూర్యుడు (పాప)]: సూర్యుడు శత్రుగ్రహమై 4వ లగ్నములో ఉన్నందున గృహ సుఖములు లోపించును. ఉన్న పెద్ద ఇల్లును కూడా అమ్మి చిన్న ఇల్లును కొందామనుకొనును.")
    lines.append("3. [4వ భావము - రాహువు (శుభ)]: దొంగవృత్తి లేదా దోపిడీల ద్వారా లక్షలు సంపాదించుట, సమాజములో భయంతో కూడిన గౌరవము.")
    lines.append("4. [4వ భావము - రాహువు (పాప)]: దొంగతనములలో దొరికిపోవుట, పోలీస్ కేసులు, జైలు జీవితము అనుభవించవలసి రావచ్చు.")
    lines.append("5. [8వ భావము - రాహువు (శత్రు)]: పాముకాటు లేదా విషాహారం వలన ప్రమాదం.")
    lines.append("6. [8వ భావము - చంద్రుడు (శత్రు)]: నీటి గండముతో మరణ భయం.")
    lines.append("7. [8వ భావము - శుక్రుడు (శత్రు)]: అగ్ని వలన ప్రమాదం.")
    lines.append("8. [8వ భావము - బుధుడు (శత్రు)]: దయ్యాల పీడ లేదా వైద్యులకు అంతుచిక్కని రోగము.")
    lines.append("9. [8వ భావము - కుజుడు (శత్రు)]: ఆయుధాల చేత లేదా రక్తసిక్త ప్రమాదము (బాంబులు/తుపాకులు).")
    lines.append("10. [6వ భావము - కుజుడు (పాప)]: మృగముల చేత గాయపడుట, ఆయుధములచేత దాడి, వ్రణములు, లేదా టీబీ/క్యాన్సర్ వంటి రోగముల భయము.")
    lines.append("11. [6వ భావము - బుధుడు (శుభ)]: వైద్య విద్యలో రాణించుట, భూతవైద్యము కూడా తెలిసియుండుట.")
    lines.append("12. [6వ భావము - బుధుడు (పాప)]: దయ్యాల బాధలు, దయ్యములు శరీరములో రోగరూపముగా ఉండి బాధింపవచ్చును.")
    lines.append("13. [7వ భావము - శుక్రుడు (శుభ)]: అందమైన, అనుకూలమైన భార్య/భర్త లభించును. ఆమె/అతని వలన మనశ్శాంతి, సుఖము ఉండును.")
    lines.append("14. [7వ భావము - శుక్రుడు (పాప)]: కళత్రము వలన కష్టములు, మనఃశ్శాంతి లోపించును.")
    lines.append("15. [7వ భావము - కుజుడు (పాప)]: యుక్తవయస్సులో వివాహము ఆలస్యమగును.")
    lines.append("16. [3వ భావము - గురు (శుభ)]: బంగారము లేదా ధనము ఏదో ఒక విధంగా లభ్యమగుట (వ్యాపార లాభం లేదా అదృష్టం).")
    lines.append("17. [3వ భావము - గురు (పాప)]: ఉన్న బంగారమును కూడా అమ్మవలసిన పరిస్థితులు ఏర్పడును.")
    lines.append("18. [3వ భావము - రాహు+గురు (సంయోగం)]: రాహువు గురువు కలిసి ఉండటము వలన బంగారు దొంగలు ఎత్తుకొని పోవు భయమున్నది.")
    lines.append("19. [10వ భావము - సూర్యుడు/చంద్రుడు]: ప్రభుత్వ ఉన్నత ఉద్యోగి (కలెక్టర్) లేదా మంత్రి పదవి యోగం.")
    lines.append("20. [10వ భావము - కుజుడు+సూర్యుడు/చంద్రుడు]: మిలిటరీలో పెద్ద డాక్టరుగా పేరు తెచ్చుకొందురు.")
    lines.append("21. [10వ భావము - కుజుడు (కేవలం)]: ప్రభుత్వ డాక్టరుగా లేదా గొప్ప సర్జన్ గా పేరు తెచ్చుకొందురు.")
    lines.append("22. [10వ భావము - శుక్రుడు]: అష్టైశ్వర్యములతో కూడిన సుఖమయ జీవితం.")
    lines.append("23. [11వ భావము - బుధుడు (శుభ)]: కట్నకానుకల రూపంలో లబ్ది.")
    lines.append("24. [11వ భావము - గురు (శుభ)]: డొనేషన్లు లేదా విద్యాసంస్థల ద్వారా లాభం.")
    lines.append("25. [5వ భావము - కేతువు (శుభ)]: దేవుని వైపు చింత, హేతువాదిక జ్ఞానము, సత్యాన్వేషణలో దైవభక్తి పెరగడము.")
    lines.append("26. [5వ భావము - కేతువు (పాప)]: దైవజ్ఞానము మీద ఆసక్తి ఉండదు, పూర్తిగా ప్రపంచ జ్ఞానములోనే ఉండిపోవుట.")
    lines.append("")

    # Section 5: Major Yogas (ముఖ్య యోగాలు)
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("SECTION 5: MAJOR YOGAS (ముఖ్య యోగాలు)")
    lines.append("------------------------------------------------------------------------------------------")
    lines.append("1. గజకేసరి యోగం: గురు మరియు చంద్రుల కేంద్ర/త్రికోణ సంయోగం వల్ల ఉన్నత పదవి, సమాజంలో గౌరవం.")
    lines.append("2. బుధాదిత్య యోగం: సూర్యుడు మరియు బుధుల కలయిక వల్ల మేధస్సు, విద్యా ప్రాప్తి, తార్కిక ఆలోచన.")
    lines.append("3. ధన యోగం: 2, 5, 9, 11 భావాధిపతుల అనుకూల స్థితి వల్ల ఐశ్వర్యం మరియు ఆర్థిక స్థిరత్వం.")
    lines.append("4. రాజ యోగం: 1, 4, 7, 10 (కేంద్ర) మరియు 5, 9 (త్రికోణ) అధిపతుల సంబంధం వల్ల అధికారం మరియు కీర్తి.")
    lines.append("")
    lines.append("==========================================================================================")
    lines.append("                                    END OF HANDBOOK                                       ")
    lines.append("==========================================================================================")

    content = "\n".join(lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Successfully generated ALL_ASTROLOGICAL_RULES.txt ({len(lines)} lines)")

if __name__ == "__main__":
    generate_all_rules_txt()
