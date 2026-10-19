# -*- coding: utf-8 -*-
"""
Multi-Planet Conjunction Engine & Comprehensive Dataset (3 Planets to 12 Planets)
according to Sri Sri Sri Acharya Prabodhananda Yogeeshwarulu's 'Jyothishya-Shaasthramu.pdf'.
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

with open('thraitha_planet_karakatvas_complete.json', 'r', encoding='utf-8') as f:
    PLANETS = json.load(f)

# The 2 camps in Thraitha Siddhantam
GURU_CAMP = ["సూర్యుడు", "చంద్రుడు", "కుజుడు", "గురువు", "కేతువు", "భూమి"]
SANI_CAMP = ["బుధుడు", "శుక్రుడు", "శని", "రాహువు", "మిత్ర", "చిత్ర"]

MULTI_PLANET_SYSTEM = {
    "engine_architecture": {
        "title": "త్రైత సిద్ధాంత బహుగ్రహ సంయోగ విశ్లేషణ వ్యవస్థ (1 నుండి 12 గ్రహాల కలయికల సార్వత్రిక సూత్రం)",
        "foundational_principles": [
            "1. ఏక గ్రహ స్థితి (1 Planet): గ్రహం తన స్వంత కారకత్వాలను భావ కర్మతో నేరుగా అనుసంధానిస్తుంది (మిత్రుడైతే శుభం, శత్రువైతే అశుభం).",
            "2. ద్విగ్రహ కలయిక (2 Planets - 234 Conjunctions): స్వపక్ష మిత్రులైతే బలం రెట్టింపవుతుంది; పరస్పర శత్రువులైతే తీవ్ర ఘర్షణ ఏర్పడుతుంది (ఉదా: కుజ-శుక్ర కలయిక).",
            "3. త్రిగ్రహ కూటమి (3 Planets): స్వపక్ష బలం vs పరపక్ష బలం నిష్పత్తి (3:0, 2:1, 1:2, 0:3). 3 శత్రువులు కలిస్తే మహా ధ్వంసకారి (రాజీవ్ గాంధీ మరణ సమయంలో కటకంలో 3 శత్రు గ్రహాలు).",
            "4. చతుర్గ్రహ కూటమి (4 Planets): 2 మిత్రులు + 2 శత్రువులు కలిస్తే ఆ భావంలో తీవ్ర అంతర్యుద్ధం (Polarized conflict); 4 మిత్రులైతే తిరుగులేని రాజయోగం; 4 శత్రువులైతే కర్మ శూన్యం.",
            "5. పంచగ్రహ కూటమి (5 Planets): జాతకుడి జీవిత ధ్యేయమంతా ఆ ఒక్క భావ కార్యకలాపాలలోనే కేంద్రీకృతమవుతుంది.",
            "6. షడ్గ్రహ నుండి ఏకాదశ గ్రహ కూటములు (6 to 11 Planets): అసాధారణ ఖగోళ కేంద్రీకరణ; వ్యక్తిగత జీవితంలో తీవ్ర అనిశ్చితి, అస్థిరత లేదా ఒకే రంగంలో విప్లవాత్మక మార్పులు.",
            "7. ద్వాదశ గ్రహ మహా కూటమి (All 12 Planets in a House): గురువర్గం 6 + శనివర్గం 6 సంపూర్ణంగా ఒకే భావంలో కలవడం -> 'సర్వ కారకత్వ విస్ఫోటనం' & 'సంపూర్ణ సన్న్యాస / బ్రహ్మజ్ఞాన యోగం'."
        ]
    },

    "multi_planet_rules_by_count": {
        "3_planets_mix": {
            "title": "3 గ్రహాల కలయిక (త్రిగ్రహ కూటమి - 3 Planets Conjunction)",
            "compositions": [
                {
                    "case": "3 మిత్రులు (3 Friends : 0 Enemies)",
                    "nature": "పరమ శుభ యోగం (Triad of Friends)",
                    "result": "ఆ భావము యొక్క పుణ్యఫలము మూడు రెట్లు వృద్ధి చెందుతుంది. ముగ్గురు మిత్రుల ఆధీనంలోని సమస్త వస్తువులు, సంపదలు, గౌరవాలు అప్రయత్నంగా లభిస్తాయి. ఎటువంటి అశుభ రోగాలు సోకవు."
                },
                {
                    "case": "2 మిత్రులు + 1 శత్రువు (2 Friends : 1 Enemy)",
                    "nature": "మిత్రుల ఆధిక్యతతో కూడిన ఆటంకాలు (Dominant Friends with Obstacles)",
                    "result": "మిత్రుల సంఖ్యాబలం ఎక్కువ ఉన్నందున ఆ భావ కార్యం నెరవేరుతుంది; కానీ ఆ ఒక్క శత్రు గ్రహం నిరంతరం అడ్డంకులు, మానసిక ఒత్తిడి, లేదా శారీరక రుగ్మతలను కలిగిస్తూనే ఉంటుంది."
                },
                {
                    "case": "1 మిత్రుడు + 2 శత్రువులు (1 Friend : 2 Enemies)",
                    "nature": "శత్రువుల ఆధిపత్యం (Enemy Domination)",
                    "result": "ఇద్దరు శత్రువులు కలిసి ఆ ఒక్క మిత్రుడిని బంధిస్తారు. మిత్రుడి ఆధీనంలోని శుభాలు నాశనమై శత్రువుల ఆధీనంలోని రోగాలు, నష్టాలు, అప్పులు ఆ భావంలో తీవ్రమవుతాయి."
                },
                {
                    "case": "3 శత్రువులు (0 Friends : 3 Enemies)",
                    "nature": "మహా పాప కూటమి (Triad of Enemies - Devastation)",
                    "result": "ఆ భావానికి సంబంధించిన సమస్త విషయాలు భస్మమవుతాయి. రాజీవ్ గాంధీ మరణ సమయంలో కర్కాటక లగ్నంలో శత్రువర్గానికి చెందిన ముగ్గురు (గురు, కుజ, చంద్రులు) కలిసి ఎదురుగా ఉన్న శనిపై దాడి చేసి ఆయువును లాక్కున్నట్లు, తీవ్ర నష్టం లేదా అకాల విపత్తు సంభవిస్తుంది."
                }
            ]
        },

        "4_planets_mix": {
            "title": "4 గ్రహాల కలయిక (చతుర్గ్రహ కూటమి - 4 Planets Conjunction)",
            "compositions": [
                {
                    "case": "4 మిత్రులు (4 Friends : 0 Enemies)",
                    "nature": "మహా సామ్రాజ్య యోగం (Quad of Friends)",
                    "result": "ఆ భావ కార్యరంగంలో అజేయమైన విజయం. నాలుగు శుభ గ్రహాల కిరణాలు ఏకమై అపార సంపద, ఉన్నత అధికారం, తిరుగులేని కీర్తిని ప్రసాదిస్తాయి."
                },
                {
                    "case": "3 మిత్రులు + 1 శత్రువు (3 Friends : 1 Enemy)",
                    "nature": "ఘన విజయం - చిన్న లోపం (Major Success with Minor Flaw)",
                    "result": "విజయం పెద్ద స్థాయిలో ఉంటుంది, కానీ ఆ ఒక్క శత్రు గ్రహం ఏదో ఒక రంగంలో (ఉదా: ఆరోగ్యం లేదా కుటుంబంలో) అసంతృప్తిని మిగులుస్తుంది."
                },
                {
                    "case": "2 మిత్రులు + 2 శత్రువులు (2 Friends : 2 Enemies)",
                    "nature": "తీవ్ర అంతర్యుద్ధం / సమసప్తక స్తంభన (Polarized Civil War)",
                    "result": "ఆ భావంలో తీవ్ర ఘర్షణ ఉంటుంది. జీవితంలో ఆ భావానికి సంబంధించిన విషయాలు ఒకసారి అత్యున్నత స్థాయికి వెళ్ళడం, మరుసటి క్షణమే పాతాళానికి పడిపోవడం వంటి పెను తుఫానులు ఎదురవుతాయి."
                },
                {
                    "case": "1 మిత్రుడు + 3 శత్రువులు (1 Friend : 3 Enemies)",
                    "nature": "భారీ పతనం (Severe Defeat)",
                    "result": "శత్రువులు ఆ మిత్రుడి కారకత్వాలను పూర్తిగా హరిస్తారు. కోర్టు కేసులు, జైలు బంధనాలు, లేదా తీవ్రమైన ఆస్తి నష్టాలు సంభవిస్తాయి."
                },
                {
                    "case": "4 శత్రువులు (0 Friends : 4 Enemies)",
                    "nature": "సంపూర్ణ వినాశన కూటమి (Total Destruction)",
                    "result": "ఆ భావ ఫలితం పూర్తిగా శూన్యమవుతుంది. ఆయుర్దాయం, ఆరోగ్యం లేదా వైవాహిక జీవితం అంధకారమవుతాయి."
                }
            ]
        },

        "5_to_11_planets_mix": {
            "title": "5 నుండి 11 గ్రహాల కలయికలు (బహుగ్రహ కూటములు - 5 to 11 Planets)",
            "principles": [
                "పంచగ్రహ కూటమి (5 Planets): జాతకుని జన్మ కారణమంతా ఆ ఒక్క భావంపైనే కేంద్రీకృతమవుతుంది. ఉదాహరణకు 10వ భావంలో 5 గ్రహాలుంటే రాజకీయం లేదా అధికారమే సర్వస్వమవుతుంది.",
                "షడ్గ్రహ కూటమి (6 Planets - సగం గ్రహాలు ఒకే ఇంట్లో): ఇది సమాజంలో అసాధారణమైన ప్రభావం చూపే నాయకులలో లేదా సన్న్యాసులలో కనిపిస్తుంది. ప్రాపంచిక సమతుల్యత దెబ్బతింటుంది.",
                "సప్తగ్రహ నుండి ఏకాదశ గ్రహ కూటములు (7 to 11 Planets): అరుదైన యుగ సంధ్యా కూటములు. ప్రపంచ గమనాన్ని మార్చే సంఘటనలు ఆ సమయంలో పుట్టిన వ్యక్తుల ద్వారా జరుగుతాయి. వీరికి సాధారణ కుటుంబ జీవితం ఉండదు."
            ]
        },

        "12_planets_universal_mix": {
            "title": "ద్వాదశ గ్రహ మహా కూటమి (All 12 Planets in a Single House)",
            "principles": [
                "గురు వర్గములోని 6 గ్రహాలు (సూర్య, చంద్ర, కుజ, గురు, కేతు, భూమి) మరియు శని వర్గములోని 6 గ్రహాలు (బుధ, శుక్ర, శని, రాహు, మిత్ర, చిత్ర) సరిసమానంగా (6 : 6 నిష్పత్తిలో) ఒకే భావంలో కలిసినప్పుడు:",
                "1. సర్వ కారకత్వ విస్ఫోటనం: భూమిమీదున్న సమస్త వస్తువులు (బంగారం, ఇనుము, ఆయుధాలు, వాహనాలు, నీరు, విషాలు), సమస్త రోగాలు, సమస్త వృత్తులు ఆ ఒక్క భావంలో కేంద్రీకృతమవుతాయి.",
                "2. పరిపూర్ణ సన్న్యాస / బ్రహ్మజ్ఞాన యోగం: ప్రాపంచిక సుఖాలు మరియు దుఃఖాలు రెండూ సమానంగా ఢీకొని పరస్పరం రద్దయిపోతాయి (6 మిత్రులు = 6 శత్రువులు). దీనివల్ల ప్రాపంచిక విషయాలపై తీవ్ర వైరాగ్యం ఏర్పడుతుంది. మనిషి సంసారాన్ని, ఆస్తులను త్యజించి ఏకైక పరమాత్మ వైపు మళ్లుతాడు.",
                "3. అసాధారణ జీవన గమనం: ఈ జాతకుడికి సాధారణ లౌకిక జీవితం సాధ్యం కాదు. అయితే జగద్గురువు, అవధూత లేదా సంపూర్ణ విరక్తుడైన జ్ఞానిగా మారుతాడు."
            ]
        }
    }
}

def analyze_combination(bhava_num, lagna_type, planet_list):
    """
    Universal evaluation engine for any subset of planets (1 to 12)
    in any Bhava (1 to 12) for either 'even' (సరి) or 'odd' (బేసి) Lagna.
    """
    # Lagna camp definition in Thraitha Siddhantam:
    # బేసి లగ్నములు (1, 3, 5, 7, 9, 11 - మేష, మిథున, సింహ, తులా, ధనుస్సు, కుంభ) -> కుజ, బుధ, రవి, శుక్ర, గురు, శని లగ్నాలు.
    # Camp: గురు వర్గ లగ్నాలు (మేష, సింహ, ధనుస్సు, కర్కాటక, వృశ్చిక, మీన) vs శని వర్గ లగ్నాలు (వృషభ, మిథున, కన్య, తులా, మకర, కుంభ)
    
    friends = []
    enemies = []
    
    # Let's determine camp alignment for the given lagna type
    # If lagna belongs to Guru camp:
    #   Friends = GURU_CAMP, Enemies = SANI_CAMP
    # If lagna belongs to Sani camp:
    #   Friends = SANI_CAMP, Enemies = GURU_CAMP
    
    is_guru_lagna = (lagna_type.lower() in ["guru", "గురు", "గురు వర్గము", "odd"])
    
    for p in planet_list:
        if is_guru_lagna:
            if p in GURU_CAMP:
                friends.append(p)
            else:
                enemies.append(p)
        else:
            if p in SANI_CAMP:
                friends.append(p)
            else:
                enemies.append(p)
                
    f_count = len(friends)
    e_count = len(enemies)
    total = len(planet_list)
    
    # Check for specific famous yogas
    special_yogas = []
    if "కుజుడు" in planet_list and "శుక్రుడు" in planet_list:
        special_yogas.append("కుజ-శుక్ర శత్రుత్వ యోగం: దాంపత్యంలో పొందికలేకపోవడం, ప్రతి చిన్న విషయానికీ పోట్లాటలు, లేదా రోడ్డు/వాహన ప్రమాదాల సూచన.")
    if bhava_num == 5:
        if "గురువు" in planet_list or "చంద్రుడు" in planet_list:
            if f_count > e_count:
                special_yogas.append("సంతాన ప్రాప్తి యోగం: 5వ భావంలో సంతాన కారక బలం వల్ల సత్పుత్రులు/సంతతి పుణ్యం దక్కుతుంది.")
            else:
                special_yogas.append("సంతాన దోషం: శత్రు గ్రహాల ఆధిపత్యం వల్ల సంతానాన్ని అశుభ గ్రహాలు లాగేసుకునే ప్రమాదం.")
    if bhava_num == 8 or ("కుజుడు" in planet_list and "శని" in planet_list):
        special_yogas.append("ఆయుర్దాయ ప్రమాద సూచన: కుజ-శని కలయిక లేదా 8వ భావ స్పర్శ వల్ల ఆయుధ/రక్తపాత లేదా వాహన ప్రమాదాల హెచ్చరిక.")
    if "బుధుడు" in planet_list and bhava_num == 6:
        special_yogas.append("దయ్యాలు/గ్రహపీడల సూచన: 6వ ఇంట్లో బుధుడి ప్రభావం వల్ల క్షుద్రపీడలు లేదా విచిత్ర వ్యాధుల ప్రభావం.")
    if "కేతువు" in planet_list and (bhava_num in [5, 9, 12]):
        special_yogas.append("మోక్ష & నిరాకార భక్తి యోగం: హేతువాదంతో దైవసత్యాన్ని శోధించడం, బ్రహ్మజ్ఞాన ప్రాప్తి.")
    if total == 12:
        special_yogas.append("ద్వాదశ గ్రహ మహా కూటమి: సర్వ కారకత్వ విస్ఫోటనం & పరిపూర్ణ సన్న్యాస బ్రహ్మజ్ఞాన యోగం.")
        
    return {
        "bhava": bhava_num,
        "planet_count": total,
        "planets": planet_list,
        "friends_count": f_count,
        "enemies_count": e_count,
        "friends_list": friends,
        "enemies_list": enemies,
        "ratio": f"{f_count} మిత్రులు : {e_count} శత్రువులు",
        "special_yogas": special_yogas
    }

def export_all():
    # 1. Save multi-planet system JSON
    json_path = 'thraitha_multi_planet_rules_system.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(MULTI_PLANET_SYSTEM, f, ensure_ascii=False, indent=2)
    print(f"Master Multi-planet JSON saved: {json_path}")
    
    # 2. Save Desktop Text File
    desktop_path = r'C:\Users\KRISH\Desktop\బహుగ్రహ_కూటమి_3_నుండి_12_గ్రహాల_కలయికల_నియమాలు.txt'
    with open(desktop_path, 'w', encoding='utf-8-sig') as f:
        f.write("=" * 110 + "\n")
        f.write("శ్రీశ్రీశ్రీ ఆచార్య ప్రబోధానంద యోగీశ్వరుల 'జ్యోతిష్యశాస్త్రము' ఆధారంగా బహుగ్రహ కూటమి సూత్రములు (3 నుండి 12 గ్రహాలు)\n")
        f.write("ఒకే ఇంట్లో 3, 4, 5 ... 12 గ్రహాల వరకు కలిసినప్పుడు సంభవించే సంశ్లేషిత ఫలితాలు & కారకత్వాల అనుసంధానము (త్రైత సిద్ధాంతం)\n")
        f.write("=" * 110 + "\n\n")
        
        f.write("■ వ్యవస్థాపక ప్రాథమిక సూత్రములు (Foundational Principles):\n")
        for p in MULTI_PLANET_SYSTEM["engine_architecture"]["foundational_principles"]:
            f.write(f"  • {p}\n")
        f.write("\n" + "=" * 110 + "\n\n")
        
        # 3 Planets
        sec3 = MULTI_PLANET_SYSTEM["multi_planet_rules_by_count"]["3_planets_mix"]
        f.write(f"★ {sec3['title']}\n")
        f.write("-" * 90 + "\n")
        for c in sec3["compositions"]:
            f.write(f"  [{c['case']}] -> {c['nature']}\n")
            f.write(f"    ఫలితము: {c['result']}\n\n")
        f.write("=" * 110 + "\n\n")
        
        # 4 Planets
        sec4 = MULTI_PLANET_SYSTEM["multi_planet_rules_by_count"]["4_planets_mix"]
        f.write(f"★ {sec4['title']}\n")
        f.write("-" * 90 + "\n")
        for c in sec4["compositions"]:
            f.write(f"  [{c['case']}] -> {c['nature']}\n")
            f.write(f"    ఫలితము: {c['result']}\n\n")
        f.write("=" * 110 + "\n\n")
        
        # 5 to 11 Planets
        sec5 = MULTI_PLANET_SYSTEM["multi_planet_rules_by_count"]["5_to_11_planets_mix"]
        f.write(f"★ {sec5['title']}\n")
        f.write("-" * 90 + "\n")
        for p in sec5["principles"]:
            f.write(f"  • {p}\n\n")
        f.write("=" * 110 + "\n\n")
        
        # 12 Planets
        sec12 = MULTI_PLANET_SYSTEM["multi_planet_rules_by_count"]["12_planets_universal_mix"]
        f.write(f"★ {sec12['title']}\n")
        f.write("-" * 90 + "\n")
        for p in sec12["principles"]:
            f.write(f"  • {p}\n\n")
        f.write("=" * 110 + "\n")
        
    print(f"Desktop Telugu multi-planet file saved: {desktop_path}")
    
    # 3. Create English named copy
    eng_path = r'C:\Users\KRISH\Desktop\Thraitha_Multi_Planet_Conjunction_Rules_3_to_12_Planets.txt'
    import shutil
    shutil.copyfile(desktop_path, eng_path)
    print(f"English named copy saved: {eng_path}")

if __name__ == '__main__':
    export_all()
