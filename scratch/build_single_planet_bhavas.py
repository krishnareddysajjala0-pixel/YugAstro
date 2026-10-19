# -*- coding: utf-8 -*-
"""
Builder for 144 Single Planet Bhava Combinations (12 Planets x 12 Bhavas)
Applying Complete Karakatvas, Governed Items, and Diseases according to Thraitha Siddhantam.
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('thraitha_planet_karakatvas_complete.json', 'r', encoding='utf-8') as f:
    PLANETS = json.load(f)

BHAVA_NAMES = {
    1: {"name": "1వ భావము (తను స్థానము / లగ్నము)", "core": "స్థూల శరీరము, ఆరోగ్యం, రూపం, ప్రాథమిక ఆత్మశక్తి, శారీరక పుణ్యం"},
    2: {"name": "2వ భావము (ధన స్థానము / కుటుంబము)", "core": "కుటుంబ సుఖం, వాక్చాతుర్యం, ప్రాపంచిక ధన చలామణి, ఆహార అలవాట్లు"},
    3: {"name": "3వ భావము (భ్రాతృ స్థానము / శ్రమ / ధైర్యం)", "core": "తోబుట్టువులు, శారీరక శ్రమ, నిద్రలేమి, సంపాదన తాపత్రయం, పాపకోణం"},
    4: {"name": "4వ భావము (మాతృ / గృహ / వాహన స్థానము)", "core": "తల్లి ఆదరణ, సొంత ఇల్లు, అంతస్తుల భవనాలు, వాహనాలు, నీటి వసతి (బోర్లు/బావులు), అంగీ కేంద్రం"},
    5: {"name": "5వ భావము (సంతాన / పుణ్య / బుద్ధి స్థానము)", "core": "సత్పుత్రులు/సంతతి, మేధాశక్తి, లౌకిక విద్యా వివేకం, మంత్రాంగం, పుణ్యకోణం"},
    6: {"name": "6వ భావము (శత్రు / రోగ / ఋణ స్థానము)", "core": "వ్యాధులు, శత్రుపీడ, అప్పులు, కోర్టు కేసులు, దయ్యాలు/గ్రహపీడలు, రోగనిరోధక శక్తి"},
    7: {"name": "7వ భావము (కళత్ర / వివాహ / సంసార స్థానము)", "core": "భార్య/అర్ధాంగి, వివాహం, దాంపత్య సుఖం, భాగస్వామ్యాలు, సంసార బాధ్యత, పాపకోణం"},
    8: {"name": "8వ భావము (ఆయుః స్థానము / మరణము)", "core": "ఆయుష్షు, మరణం రకం (సహజ vs రక్తపాత/ఆయుధ మరణం), ప్రమాదాలు, ఆపదలు, రహస్య వ్యాధులు"},
    9: {"name": "9వ భావము (భాగ్య / ధర్మ / పితృ స్థానము)", "core": "తండ్రి ప్రేమ, పూర్వీకుల ఆస్తి, దైవభక్తి, తీర్థయాత్రలు, ఉన్నత విద్య, పుణ్యకోణం"},
    10: {"name": "10వ భావము (కర్మ / రాజ్య / ఉద్యోగ స్థానము)", "core": "వృత్తి, ఉద్యోగం, రాజ్యాధికారం, సమాజంలో కీర్తి ప్రతిష్ఠలు, నాయకత్వం, అర్ధాంగీ కేంద్రం"},
    11: {"name": "11వ భావము (లాభ / ఆశయ స్థానము)", "core": "సమస్త లాభాలు, కోరికల నెరవేర్పు, పెద్ద సోదరులు, ప్రాపంచిక ఆశలు, పాపకోణం"},
    12: {"name": "12వ భావము (వ్యయ / మోక్ష స్థానము)", "core": "శుభ/అశుభ ఖర్చులు, నిద్ర, కారాగార బంధనం, ఆసుపత్రి వ్యయాలు, మోక్షం/పరలోక గతి"}
}

SINGLE_PLANET_DATA = []

for b_num in range(1, 13):
    b_info = BHAVA_NAMES[b_num]
    for p_name, p in PLANETS.items():
        party = p["party"]
        items = p["governed_physical_items"][:4]
        diseases = p["governed_body_parts_and_diseases"]["diseases"][:3]
        professions = p["governed_professions_and_trades"][:3]
        
        # Build contextual prediction for single planet in this Bhava
        friendly_res = ""
        harmful_res = ""
        applied_items = ", ".join(items)
        applied_diseases = ", ".join(diseases)
        
        if b_num == 1:
            friendly_res = f"{p_name} మిత్రుడై లగ్నంలో ఉంటే శరీరానికి అద్భుతమైన ఆరోగ్యం, తేజస్సు లభిస్తాయి. {p_name} ఆధీనంలోని సద్గుణాలు వ్యక్తిత్వాన్ని ఉన్నతంగా తీర్చిదిద్దుతాయి."
            harmful_res = f"{p_name} శత్రువై లగ్నంలో ఉంటే బలహీన దేహం, అంగలోపం లేదా దీర్ఘకాలిక రోగాలు ({applied_diseases}) శరీరంపై ప్రభావం చూపుతాయి."
        elif b_num == 2:
            friendly_res = f"{p_name} మిత్రుడై 2వ ఇంట్లో ఉంటే అద్భుతమైన వాక్చాతుర్యం, నిరంతర ధన చలామణి, కుటుంబంలో శాంతి ఉంటాయి. {applied_items} ద్వారా ధనార్జన జరుగుతుంది."
            harmful_res = f"{p_name} శత్రువైతే నోటి దురుసుతనం, కుటుంబ కలహాలు, విపరీతమైన ధన నష్టం, కంటి లేదా గొంతు సంబంధిత వ్యాధులు కలుగుతాయి."
        elif b_num == 3:
            friendly_res = f"{p_name} మిత్రుడైతే స్వయంకృషితో ధైర్యంగా ముందుకు సాగుతారు, సోదరుల సహాయం లభిస్తుంది. కష్టపడి పనిచేసే శారీరక ఓర్పు ఉంటుంది."
            harmful_res = f"{p_name} శత్రువైతే సోదరులతో తీవ్ర విరోధం, నిద్రలేమి, సంపాదన కోసం విపరీతమైన శారీరక శ్రమ పడినా ఫలితం దక్కదు."
        elif b_num == 4:
            friendly_res = f"{p_name} 4వ ఇంట్లో మిత్రుడైతే సొంత ఇల్లు, భవన ప్రాప్తి, వాహన సౌఖ్యం మరియు పుష్కలమైన నీటి వసతి లభిస్తాయి. తల్లి సంపూర్ణ ఆదరణ దక్కుతుంది."
            harmful_res = f"{p_name} శత్రువైతే ఉన్న ఇల్లు అమ్ముకోవడం, అద్దె ఇళ్ళలో తిరగడం, వాహన నష్టాలు, బావులు/బోర్లు ఎండిపోవడం లేదా గృహ దారుల పంచాయితీలు వస్తాయి."
        elif b_num == 5:
            friendly_res = f"{p_name} 5వ ఇంట్లో మిత్రుడైతే తీక్షణమైన బుద్ధికుశలత, సత్పుత్రుల ప్రాప్తి, ఉన్నత విద్యా ప్రావీణ్యం లభిస్తాయి. సమాజంలో గొప్ప గౌరవం పొందుతారు."
            harmful_res = f"{p_name} శత్రువైతే సంతానలేమి లేదా పుత్ర శోకం, మందబుద్ధి, పరీక్షల్లో ఆటంకాలు మరియు సంతానాన్ని అశుభ గ్రహాలు హరించడం జరుగుతుంది."
        elif b_num == 6:
            friendly_res = f"{p_name} 6వ ఇంట్లో మిత్రుడైతే రోగనిరోధక శక్తి వజ్రకవచంలా పనిచేస్తుంది; శత్రువులను సులభంగా అణచివేస్తారు; అప్పులు త్వరగా తీరుస్తారు."
            harmful_res = f"{p_name} శత్రువైతే దీర్ఘకాలిక వ్యాధులు ({applied_diseases}), శత్రుపీడ, తీరని అప్పులు మరియు గ్రహపీడలు/దయ్యాల బాధలు శరీరంలో ప్రవేశిస్తాయి."
        elif b_num == 7:
            friendly_res = f"{p_name} 7వ ఇంట్లో మిత్రుడైతే అందమైన, అనుకూలవతియైన భార్య లభించుట, దాంపత్య పరమ సుఖం, చిన్న వయస్సులోనే వివాహ భాగ్యం దక్కుతాయి."
            harmful_res = f"{p_name} శత్రువైతే వివాహం ఆలస్యం కావడం, వయస్సు ముదరడం, భార్యతో నిరంతర కలహాలు, స్త్రీ సౌఖ్యం లేకపోవడం లేదా విడాకులకు దారితీస్తుంది."
        elif b_num == 8:
            friendly_res = f"{p_name} 8వ ఇంట్లో మిత్రుడైతే సంపూర్ణ దీర్ఘాయుష్షు, ఘోర ప్రమాదాల నుండి అద్భుతంగా తప్పించుకోవడం, ప్రశాంతమైన సహజ మరణం లభిస్తాయి."
            harmful_res = f"{p_name} శత్రువైతే అకాల మరణ భయాలు, ఆయుధ గాయాలు, ప్రమాదాలు, లేదా శని ఆయుష్షును హరించడం వల్ల అకాల మరణం సంభవిస్తుంది."
        elif b_num == 9:
            friendly_res = f"{p_name} 9వ ఇంట్లో మిత్రుడైతే అఖండ భాగ్యం, తండ్రి సంపూర్ణ ఆదరణ, ఉన్నత విద్యాభాగ్యం, విదేశీ యానాలు, దైవభక్తి లభిస్తాయి."
            harmful_res = f"{p_name} శత్రువైతే తండ్రితో బద్ధవైరం లేదా తండ్రికి అకాల కష్టాలు, దైవకార్యాల పట్ల నిర్లక్ష్యం, సమాజంలో అపకీర్తి కలుగుతాయి."
        elif b_num == 10:
            friendly_res = f"{p_name} 10వ ఇంట్లో మిత్రుడైతే ఉన్నత ప్రభుత్వ ఉద్యోగం, రాజ్యాధికారం, {', '.join(professions)} రంగాలలో తిరుగులేని ఆధిపత్యం లభిస్తాయి."
            harmful_res = f"{p_name} శత్రువైతే ఉద్యోగంలో సస్పెన్షన్, పదవీచ్యుతి, వ్యాపారంలో నష్టాలు, సమాజంలో పరువు నష్టం మరియు నీచ వృత్తులు చేయాల్సి వస్తుంది."
        elif b_num == 11:
            friendly_res = f"{p_name} 11వ ఇంట్లో మిత్రుడైతే సమస్త వ్యాపారాలలో అఖండ ధన లాభాలు, ఆశయాలు నెరవేరడం, పెద్ద సోదరుల సంపూర్ణ సహకారం దక్కుతాయి."
            harmful_res = f"{p_name} శత్రువైతే ఆశలన్నీ అడియాసలు కావడం, వ్యాపారాలలో భారీ నష్టాలు, నమ్మిన వారి చేతిలో మోసపోవడం జరుగుతుంది."
        elif b_num == 12:
            friendly_res = f"{p_name} 12వ ఇంట్లో మిత్రుడైతే ధర్మకార్యాలకు, ఆశ్రమాలకు దానధర్మాలు చేయడం, ఆధ్యాత్మిక ప్రయాణాలు, మోక్షసాధన మరియు సద్గతి లభిస్తాయి."
            harmful_res = f"{p_name} శత్రువైతే జైలు బంధనాలు, కోర్టు జరిమానాలు, ఆసుపత్రుల పాలై విపరీతమైన ధనం వృథా కావడం, వ్యసనాలతో పతనం కావడం జరుగుతుంది."

        entry = {
            "bhava_number": b_num,
            "bhava_name": b_info["name"],
            "bhava_core_significance": b_info["core"],
            "planet_name": p_name,
            "planet_party": party,
            "friendly_state_result": friendly_res,
            "enemy_state_result": harmful_res,
            "applied_governed_items": applied_items,
            "applied_diseases": applied_diseases,
            "key_thraitha_sutra": f"{p_name} తన కిరణాల ద్వారా {b_num}వ భావ కర్మను స్వీకరించి క్రిందనున్న జీవుడికి అందిస్తుంది. మిత్రుడైతే శుభాన్ని, శత్రువైతే అశుభాన్ని ప్రసాదిస్తుంది."
        }
        SINGLE_PLANET_DATA.append(entry)

def export_all():
    # 1. JSON
    json_path = 'thraitha_single_planet_bhavas_144.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(SINGLE_PLANET_DATA, f, ensure_ascii=False, indent=2)
    print(f"Single planet 144 JSON saved: {json_path}")
    
    # 2. Desktop text
    desktop_path = r'C:\Users\KRISH\Desktop\ఏక_గ్రహ_12_భావ_ఫలితాలు_త్రైత_సిద్ధాంతం.txt'
    with open(desktop_path, 'w', encoding='utf-8-sig') as f:
        f.write("=" * 110 + "\n")
        f.write("శ్రీశ్రీశ్రీ ఆచార్య ప్రబోధానంద యోగీశ్వరుల 'జ్యోతిష్యశాస్త్రము' ఆధారంగా ద్వాదశ భావములలో ఏక గ్రహ ఫలితాలు (144 Combinations)\n")
        f.write("ప్రతి గ్రహము ఒంటరిగా ఒక భావములో ఉన్నప్పుడు కలిగే శుభ/అశుభ ఫలితాలు & కారకత్వాల అనుసంధానము (త్రైత సిద్ధాంతం)\n")
        f.write("=" * 110 + "\n\n")
        
        curr_b = 0
        for item in SINGLE_PLANET_DATA:
            if item["bhava_number"] != curr_b:
                curr_b = item["bhava_number"]
                f.write(f"\n################################################################################\n")
                f.write(f"### {item['bhava_name']}\n")
                f.write(f"### భావ కారకత్వము: {item['bhava_core_significance']}\n")
                f.write(f"################################################################################\n\n")
            
            f.write(f"★ గ్రహము: {item['planet_name']} ({item['planet_party']})\n")
            f.write(f"  • మిత్రుడైనపుడు (Favorable / Friendly): {item['friendly_state_result']}\n")
            f.write(f"  • శత్రువైనపుడు (Hostile / Enemy)       : {item['enemy_state_result']}\n")
            f.write(f"  • క్రియాశీలమయ్యే వస్తువులు             : {item['applied_governed_items']}\n")
            f.write(f"  • సంభవించే రోగాలు / రుగ్మతలు          : {item['applied_diseases']}\n")
            f.write(f"  • త్రైత సిద్ధాంత సూత్రము                 : {item['key_thraitha_sutra']}\n")
            f.write("-" * 90 + "\n")
            
    print(f"Desktop Telugu single planet file saved: {desktop_path}")
    
    # 3. English named copy
    eng_path = r'C:\Users\KRISH\Desktop\Thraitha_Single_Planet_12_Bhavas_144_Rules.txt'
    import shutil
    shutil.copyfile(desktop_path, eng_path)
    print(f"English named copy saved: {eng_path}")

if __name__ == '__main__':
    export_all()
