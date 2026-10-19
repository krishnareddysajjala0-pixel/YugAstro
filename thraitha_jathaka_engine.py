# -*- coding: utf-8 -*-
"""
Thraitha Siddhantam Complete Jathaka Report Generator (సంపూర్ణ జాతక నివేదిక ఇంజిన్)
Based strictly on Sri Sri Sri Acharya Prabodhananda Yogeeshwarulu's 'Jyothishya-Shaasthramu.pdf'.
"""

import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

# Load the master datasets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def _load_json(filename):
    path = os.path.join(BASE_DIR, filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

PLANET_DATA = _load_json('thraitha_planet_karakatvas_complete.json')
SINGLE_PLANET_RULES = _load_json('thraitha_single_planet_bhavas_144.json')
CONJUNCTION_RULES = _load_json('bhava_conjunctions.json')
MULTI_PLANET_SYSTEM = _load_json('thraitha_multi_planet_rules_system.json')
SPECIAL_RULES = _load_json('thraitha_astrology_combination_rules.json')

SINGLE_LOOKUP = {}
if isinstance(SINGLE_PLANET_RULES, list):
    for r in SINGLE_PLANET_RULES:
        SINGLE_LOOKUP[(r.get('bhava_number'), r.get('planet_name'))] = r

GURU_CAMP = ["సూర్యుడు", "చంద్రుడు", "కుజుడు", "గురువు", "కేతువు", "భూమి", "సూర్య", "చంద్ర", "కుజ", "గురు", "కేతు"]
SANI_CAMP = ["బుధుడు", "శుక్రుడు", "శని", "రాహువు", "మిత్ర", "చిత్ర", "బుధ", "శుక్ర", "రాహు"]

GURU_LAGNAS = ["మేషం", "కర్కాటకం", "సింహం", "వృశ్చికం", "ధనస్సు", "మీనం"]
SANI_LAGNAS = ["వృషభం", "మిథునం", "కన్య", "తులా", "మకరం", "కుంభం"]

BHAVA_META = {
    1: {"name": "1వ భావము (తను స్థానము / లగ్నము)", "type": "పుణ్యస్థానము (అంగీ ప్రారంభం)", "class": "punya", "significance": "స్థూల శరీరము, ఆరోగ్యం, రూపం, ప్రాథమిక ఆత్మశక్తి, జీవన గమనం"},
    2: {"name": "2వ భావము (ధన స్థానము / కుటుంబము)", "type": "సంధి స్థానము (పుణ్యము + పాపము)", "class": "sandhi", "significance": "కుటుంబ సౌఖ్యం, వాక్చాతుర్యం, ప్రాపంచిక ధన చలామణి, ఆహార అలవాట్లు"},
    3: {"name": "3వ భావము (భ్రాతృ / శ్రమ / ధైర్యము)", "type": "పాపస్థానము (పాపకోణం)", "class": "paapa", "significance": "తోబుట్టువులు, శారీరక శ్రమ, సంపాదన కోసం నిద్రలేని తాపత్రయం, స్వయంకృషి"},
    4: {"name": "4వ భావము (మాతృ / గృహ / వాహనము)", "type": "కేంద్ర స్థానము (అంగీ కేంద్రం)", "class": "kendra", "significance": "తల్లి ఆదరణ, సొంత ఇల్లు, అంతస్తుల భవనాలు, వాహనాలు, నీటి వసతి (బోర్లు/బావులు)"},
    5: {"name": "5వ భావము (సంతాన / పుణ్య / బుద్ధి)", "type": "పుణ్యస్థానము (పుణ్యకోణం)", "class": "punya", "significance": "సత్పుత్రులు/సంతతి, మేధాశక్తి, లౌకిక విద్యా వివేకం, మంత్రాంగం, దైవచింతన"},
    6: {"name": "6వ భావము (శత్రు / రోగ / ఋణ స్థానము)", "type": "సంధి స్థానము (రోగాలు / అప్పులు)", "class": "sandhi", "significance": "శారీరక వ్యాధులు, శత్రుపీడ, అప్పులు, కోర్టు కేసులు, దయ్యాలు/గ్రహపీడలు"},
    7: {"name": "7వ భావము (కళత్ర / వివాహ / సంసారము)", "type": "పాపస్థానము (అర్ధాంగి ప్రారంభం / పాపకోణం)", "class": "paapa", "significance": "భార్య/అర్ధాంగి, వివాహం, దాంపత్య సుఖం, భాగస్వామ్యాలు, సంసార బాధ్యత (1x7 శత్రుత్వం)"},
    8: {"name": "8వ భావము (ఆయుః స్థానము / మరణము)", "type": "సంధి స్థానము (ఆయుష్షు / ప్రమాదాలు)", "class": "sandhi", "significance": "ఆయుష్షు, మరణం స్వభావం (సహజ vs రక్తపాత/ఆయుధ మరణం), ఘోర ప్రమాదాలు, ఆపదలు"},
    9: {"name": "9వ భావము (భాగ్య / ధర్మ / పితృ స్థానము)", "type": "పుణ్యస్థానము (పుణ్యకోణం)", "class": "punya", "significance": "తండ్రి ప్రేమ, పూర్వీకుల ఆస్తి, దైవభక్తి, తీర్థయాత్రలు, ఉన్నత విద్యాభాగ్యం"},
    10: {"name": "10వ భావము (కర్మ / రాజ్య / ఉద్యోగము)", "type": "కేంద్ర స్థానము (అర్ధాంగీ కేంద్రం)", "class": "kendra", "significance": "వృత్తి, ఉద్యోగం, రాజ్యాధికారం, సమాజంలో కీర్తి ప్రతిష్ఠలు, నాయకత్వం"},
    11: {"name": "11వ భావము (లాభ / ఆశయ స్థానము)", "type": "పాపస్థానము (పాపకోణం)", "class": "paapa", "significance": "సమస్త లాభాలు, కోరికల నెరవేర్పు, పెద్ద సోదరులు, ప్రాపంచిక ఆశలు"},
    12: {"name": "12వ భావము (వ్యయ / మోక్ష స్థానము)", "type": "సంధి స్థానము (మోక్షం / ఖర్చులు)", "class": "sandhi", "significance": "శుభ/అశుభ ఖర్చులు, నిద్ర, కారాగార బంధనం, ఆసుపత్రి వ్యయాలు, మోక్షం/పరలోక గతి"}
}

def clean_planet_name(pname):
    """Normalize planet names to Telugu standard keys."""
    if not pname:
        return ""
    p = pname.strip()
    mapping = {
        "సూర్య": "సూర్యుడు", "రవి": "సూర్యుడు", "Sun": "సూర్యుడు",
        "చంద్ర": "చంద్రుడు", "ఇందు": "చంద్రుడు", "Moon": "చంద్రుడు",
        "కుజ": "కుజుడు", "అంగారక": "కుజుడు", "Mars": "కుజుడు",
        "బుధ": "బుధుడు", "Mercury": "బుధుడు",
        "గురు": "గురువు", "బృహస్పతి": "గురువు", "Jupiter": "గురువు",
        "శుక్ర": "శుక్రుడు", "Venus": "శుక్రుడు",
        "శని": "శని", "Saturn": "శని",
        "రాహు": "రాహువు", "Rahu": "రాహువు",
        "కేతు": "కేతువు", "Ketu": "కేతువు",
        "భూమి": "భూమి", "Earth": "భూమి",
        "మిత్ర": "మిత్ర", "Mitra": "మిత్ర",
        "చిత్ర": "చిత్ర", "Chitra": "చిత్ర"
    }
    return mapping.get(p, p)

def generate_thraitha_jathaka_report(data, dasha_info=None):
    """
    Main entry point: Generates exhaustive, structured Thraitha Jathaka Report.
    Consumes kundali data dictionary from app.get_kundali_data().
    """
    lagna = data.get('lagna', 'మేషం')
    is_guru_lagna = lagna in GURU_LAGNAS
    lagna_camp_str = "గురు వర్గము (గురు పార్టీ)" if is_guru_lagna else "శని వర్గము (శని పార్టీ)"
    
    houses = data.get('houses', {})
    planet_positions = data.get('planet_positions', [])
    
    # Invert houses mapping: house_number (1..12) -> rashi_name
    house_to_rashi = {}
    for rashi, h_num in houses.items():
        try:
            house_to_rashi[int(h_num)] = rashi
        except Exception:
            pass
            
    # Collect resident and aspecting planets per house
    house_residents = {i: [] for i in range(1, 13)}
    house_aspects = {i: [] for i in range(1, 13)}
    
    for pp in planet_positions:
        p_name = clean_planet_name(pp.get('name'))
        p_rashi = pp.get('lagna')
        is_hand = pp.get('is_hand', False)
        
        h_num = houses.get(p_rashi)
        if h_num:
            h_num = int(h_num)
            entry = {
                "name": p_name,
                "degree": pp.get('degree', ''),
                "nakshatra": pp.get('nakshatra', ''),
                "padam": pp.get('padam', ''),
                "is_hand": is_hand,
                "camp": "గురు వర్గము" if p_name in GURU_CAMP else "శని వర్గము",
                "is_friend": (p_name in GURU_CAMP) if is_guru_lagna else (p_name in SANI_CAMP)
            }
            if is_hand:
                house_aspects[h_num].append(entry)
            else:
                house_residents[h_num].append(entry)

    # Evaluate all 12 Bhavas
    bhava_report = []
    
    all_health_warnings = []
    all_wealth_yogas = []
    all_property_yogas = []
    all_marriage_notes = []
    all_progeny_notes = []
    all_accident_notes = []
    
    for b_num in range(1, 13):
        meta = BHAVA_META[b_num]
        rashi = house_to_rashi.get(b_num, '')
        residents = house_residents[b_num]
        aspects = house_aspects[b_num]
        
        resident_names = [p["name"] for p in residents]
        aspect_names = [p["name"] for p in aspects]
        
        f_res = [p["name"] for p in residents if p["is_friend"]]
        e_res = [p["name"] for p in residents if not p["is_friend"]]
        
        res_count = len(residents)
        
        # State determination
        if res_count == 0:
            state = "neutral"
            state_text = "ఖాళీ స్థానము (పరివర్తన / దృష్టి ప్రభావం)"
        elif len(f_res) > len(e_res):
            state = "shubha"
            state_text = f"శుభ స్థితి ({len(f_res)} మిత్రులు : {len(e_res)} శత్రువులు)"
        elif len(e_res) > len(f_res):
            state = "paapa"
            state_text = f"పాప / ప్రతికూల స్థితి ({len(f_res)} మిత్రులు : {len(e_res)} శత్రువులు)"
        else:
            state = "mishra"
            state_text = f"సమతుల్య / అంతర్యుద్ధ స్థితి ({len(f_res)} మిత్రులు : {len(e_res)} శత్రువులు)"
            
        # Synthesize Detailed Interpretation
        interpretation_parts = []
        special_notes = []
        applied_items = []
        applied_diseases = []
        
        # Collect Governed Items & Diseases
        for p_obj in residents:
            pn = p_obj["name"]
            p_full = PLANET_DATA.get(pn, {})
            if p_full:
                applied_items.extend(p_full.get("governed_physical_items", [])[:3])
                applied_diseases.extend(p_full.get("governed_body_parts_and_diseases", {}).get("diseases", [])[:2])
                

        # 1. Single Planet Evaluation
        if res_count == 1:
            p_obj = residents[0]
            pn = p_obj["name"]
            is_fr = p_obj["is_friend"]
            
            p_full = PLANET_DATA.get(pn, {})
            lookup = SINGLE_LOOKUP.get((b_num, pn))
            
            if lookup:
                if is_fr:
                    interpretation_parts.append(f"✨ <b>{pn} (స్వపక్ష మిత్రుడు):</b> {lookup.get('friendly_state_result', '')}")
                else:
                    interpretation_parts.append(f"⚠️ <b>{pn} (ప్రతిపక్ష శత్రువు):</b> {lookup.get('enemy_state_result', '')}")
                
                if lookup.get('key_thraitha_sutra'):
                    special_notes.append(f"📌 <b>త్రైత సూత్రము:</b> {lookup.get('key_thraitha_sutra')}")
            else:
                if is_fr:
                    interpretation_parts.append(f"ఈ భావంలో స్వపక్ష మిత్రుడైన <b>{pn}</b> ఒక్కడే ఉండటం వల్ల ఈ భావ కారకత్వాలు శుభప్రదంగా వికసిస్తాయి. {pn} యొక్క సహజ దయాగుణం, సత్ప్రవర్తన మరియు దైవానుగ్రహం లభిస్తాయి.")
                else:
                    interpretation_parts.append(f"ఈ భావంలో శత్రువర్గానికి చెందిన <b>{pn}</b> ఉండటం వల్ల ఈ భావ కారకత్వాలలో ఆటంకాలు, నష్టాలు లేదా ఆందోళనలు దాపురిస్తాయి.")

            if b_num == 4 and pn == "సూర్యుడు" and is_fr:
                interpretation_parts.append("సూర్యుడి శుభ దృష్టి వల్ల పై అంతస్తుల భవనాలు, రాజగౌరవం లభించును.")
            elif b_num == 4 and pn == "చంద్రుడు" and not is_fr:
                interpretation_parts.append("చంద్రుడు వ్యతిరేకమైనందున నీటి కొరత, బోర్లు పూడిపోవడం లేదా ఇంటి పైకప్పు కారే సమస్యలు ఏర్పడవచ్చును.")
            elif b_num == 6 and pn == "బుధుడు" and not is_fr:
                interpretation_parts.append("బుధుడు శత్రువైనందున దయ్యాలు, క్షుద్ర పీడలు రోగరూపంలో శరీరంలో ప్రవేశించే భయముండును.")
            elif b_num == 7 and pn == "కుజుడు" and not is_fr:
                interpretation_parts.append("యౌవన కారక కుజుడు 7వ ఇంట్లో శత్రువైనందున కుజదోషం ఏర్పడి వివాహం ఆలస్యం కావడం, వయస్సు ముదరడం జరుగుతుంది.")

        # 2. Two Planets Evaluation
        elif res_count == 2:
            p1, p2 = resident_names[0], resident_names[1]
            p1_fr = residents[0]["is_friend"]
            p2_fr = residents[1]["is_friend"]
            
            if p1_fr and p2_fr:
                interpretation_parts.append(f"ఈ భావంలో ఇద్దరు మిత్రులు (<b>{p1} + {p2}</b>) కలిసి ఉండటం గొప్ప యోగం. వీరిద్దరి సంయుక్త పుణ్యబలం వల్ల ఈ భావ ఫలితాలు రెట్టింపు స్థాయిలో శుభాలను ఇస్తాయి.")
            elif not p1_fr and not p2_fr:
                interpretation_parts.append(f"ఈ భావంలో ఇద్దరు శత్రువులు (<b>{p1} + {p2}</b>) కలిసి ఉండటం వల్ల ఈ భావ కారకత్వాలు తీవ్రంగా దెబ్బతింటాయి. నష్టాలు, వ్యతిరేక ఫలితాలు హెచ్చుగా ఉంటాయి.")
            else:
                interpretation_parts.append(f"ఈ భావంలో ఒక మిత్రుడు మరియు ఒక శత్రువు (<b>{p1} + {p2}</b>) కలిసి ఉండటం వల్ల అంతర్గత ఘర్షణ ఏర్పడుతుంది. పుణ్యఫలాలు చేతికందినా ఆటంకాలు ఎదురవుతాయి.")

            # Check Kuja-Sukra
            if ("కుజుడు" in resident_names or "కుజ" in resident_names) and ("శుక్రుడు" in resident_names or "శుక్ర" in resident_names):
                special_notes.append("⚠️ <b>కుజ-శుక్ర కలయిక సూత్రము:</b> యౌవన కారక కుజుడు, కళత్ర కారక శుక్రుడు బద్ధశత్రువులు. వీరు కలిసి ఉండటం వల్ల దాంపత్యంలో పొందిక లోపించడం, మాటకు మాట పోట్లాడుకోవడం లేదా వివాహేతర ఆకర్షణల వల్ల కలహాలు ఏర్పడే అవకాశముంది. జాగ్రత్త వహించవలెను.")
                all_marriage_notes.append(f"{b_num}వ భావంలో కుజ-శుక్రుల కలయిక వల్ల దాంపత్య పొందికలో జాగ్రత్తలు అవసరం.")

        # 3. Multi-planet Evaluation (3 to 12 planets)
        elif res_count >= 3:
            f_count = len(f_res)
            e_count = len(e_res)
            
            if res_count == 12:
                interpretation_parts.append("✨ <b>ద్వాదశ గ్రహ మహా కూటమి:</b> సమస్త 12 గ్రహాలు ఈ ఒక్క భావంలోనే కేంద్రీకృతమయ్యాయి! ఇది 'సర్వ కారకత్వ విస్ఫోటనం' మరియు 'సంపూర్ణ సన్న్యాస / బ్రహ్మజ్ఞాన యోగం'. ప్రాపంచిక లాభనష్టాలు రెండూ నిరర్ధకమై తీవ్ర వైరాగ్యం జనించి పరమాత్మ వైపు చూపు మళ్ళుతుంది.")
            elif res_count == 3:
                triad_rules = MULTI_PLANET_SYSTEM.get("multi_planet_rules_by_count", {}).get("3_planets_mix", {}).get("compositions", [])
                matched_rule = None
                for tr in triad_rules:
                    if f"{f_count} Friends" in tr.get("case", "") or f"{f_count} మిత్రు" in tr.get("case", ""):
                        matched_rule = tr
                        break
                if matched_rule:
                    interpretation_parts.append(f"<b>3 గ్రహాల కలయిక ({', '.join(resident_names)}) - {matched_rule.get('nature')}:</b><br>{matched_rule.get('result')}")
                else:
                    interpretation_parts.append(f"ఈ భావంలో 3 గ్రహాల బహుగ్రహ కూటమి ({', '.join(resident_names)}) ఏర్పడింది ({f_count} మిత్రులు : {e_count} శత్రువులు).")
            elif res_count == 4:
                quad_rules = MULTI_PLANET_SYSTEM.get("multi_planet_rules_by_count", {}).get("4_planets_mix", {}).get("compositions", [])
                matched_rule = None
                for qr in quad_rules:
                    if f"{f_count} Friends" in qr.get("case", "") or f"{f_count} మిత్రు" in qr.get("case", ""):
                        matched_rule = qr
                        break
                if matched_rule:
                    interpretation_parts.append(f"<b>4 గ్రహాల చతుర్గ్రహ కూటమి ({', '.join(resident_names)}) - {matched_rule.get('nature')}:</b><br>{matched_rule.get('result')}")
                else:
                    interpretation_parts.append(f"ఈ భావంలో 4 గ్రహాల కూటమి ({', '.join(resident_names)}) ఏర్పడింది ({f_count} మిత్రులు : {e_count} శత్రువులు).")
            elif res_count == 5:
                pent_rule = MULTI_PLANET_SYSTEM.get("multi_planet_rules_by_count", {}).get("5_planets_mix", {})
                interpretation_parts.append(f"<b>5 గ్రహాల పంచగ్రహ కూటమి ({', '.join(resident_names)}) - {pent_rule.get('title')}:</b><br>జాతకుడి జీవిత ధ్యేయమంతా, ఆలోచనలన్నీ ఈ ఒక్క భావ కార్యకలాపాల చుట్టూనే పరిభ్రమిస్తాయి ({f_count} మిత్రులు : {e_count} శత్రువులు).")
            else:
                interpretation_parts.append(f"ఈ భావంలో <b>{res_count} గ్రహాల అసాధారణ బహుగ్రహ కూటమి ({', '.join(resident_names)})</b> ఏర్పడింది ({f_count} మిత్రులు : {e_count} శత్రువులు). ఈ భావ కారకత్వాలలో జీవితంలో అనూహ్యమైన విప్లవాత్మక మలుపులు, తీవ్ర అనిశ్చితి లేదా మహా పరివర్తన చోటుచేసుకుంటాయి.")

        # Empty house evaluation
        else:
            interpretation_parts.append(f"ఈ భావంలో ప్రత్యక్షంగా ఏ గ్రహాలూ నివాసం లేవు. ఈ భావ ఫలితం ఎదురుగా ఉన్న రాశినుండి ప్రసరించే చూపులు (చేతులు) మరియు భావాధిపతి స్థానబలాన్ని బట్టి లభిస్తుంది.")
            if aspect_names:
                interpretation_parts.append(f"ఈ స్థానమును <b>{', '.join(aspect_names)}</b> గ్రహములు తమ దృష్టి చేతులతో తాకుచున్నవి.")

        # Check House 8 Longevity / Accidents
        if b_num == 8 or ("కుజుడు" in resident_names and "శని" in resident_names):
            if not is_guru_lagna and ("కుజుడు" in resident_names or "కుజుడు" in aspect_names):
                special_notes.append("⚠️ <b>ఆయుర్దాయ & ప్రమాద సూచన (గాంధీ, రాజీవ్ గాంధీ సూత్రం):</b> ఆయుః స్థానమైన 8వ భావముపై కుజుడి ప్రభావం ఉన్నందున రక్తపాత, ఆయుధ, లేదా వాహన ప్రమాదాల పట్ల అప్రమత్తంగా ఉండాలి. నిత్యం దైవస్మరణ, ఆత్మజ్ఞాన విచారణ రక్షణ కల్పిస్తుంది.")
                all_accident_notes.append("8వ భావంలో కుజస్పర్శ వల్ల వాహనాలు నడిపేటప్పుడు, రక్తపాత ప్రమాదాల పట్ల జాగ్రత్త అవసరం.")

        # Check House 5 Santhanam
        if b_num == 5:
            has_guru = any(p["name"] in ["గురువు", "గురు"] for p in residents)
            has_chandra = any(p["name"] in ["చంద్రుడు", "చంద్ర"] for p in residents)
            if has_guru or has_chandra:
                if state == "shubha":
                    special_notes.append("✨ <b>సంతాన భాగ్య సూత్రము:</b> 5వ స్థానంలో సంతాన కారక గ్రహములు అనుకూలంగా ఉన్నందున వంశోద్ధారకులైన ఉత్తమ సంతాన ప్రాప్తి, మేధాసంపత్తి కలుగును.")
                    all_progeny_notes.append("5వ భావంలో సంతాన కారక గ్రహాల అనుకూలత వల్ల సుపుత్ర ప్రాప్తి కలుగుతుంది.")
                else:
                    special_notes.append("⚠️ <b>సంతాన దోష సూచన:</b> 5వ స్థానంలో శత్రుగ్రహాల కలయిక వల్ల సంతాన విషయంలో ఆలస్యం లేదా ఆందోళనలు రావచ్చును.")
                    all_progeny_notes.append("5వ భావంలో శత్రుగ్రహాల ప్రభావం వల్ల సంతాన విషయంలో జాగ్రత్తలు, దైవారాధన అవసరం.")

        # Category Aggregation
        if applied_diseases:
            all_health_warnings.extend(applied_diseases)
        if applied_items:
            all_wealth_yogas.extend(applied_items)

        bhava_entry = {
            "number": b_num,
            "title": meta["name"],
            "lagna": rashi,
            "type_label": meta["type"],
            "state": state,
            "state_text": state_text,
            "meaning": meta["significance"],
            "residents": residents,
            "aspects": aspects,
            "planets_text": ", ".join(resident_names) if resident_names else "ఖాళీ (దృష్టి ప్రభావం)",
            "interpretation": "<br>".join(interpretation_parts),
            "applied_items": list(set(applied_items))[:4],
            "applied_diseases": list(set(applied_diseases))[:3],
            "special_notes": special_notes
        }
        bhava_report.append(bhava_entry)

    # Compile Overall Summary Report
    report_title = f"{data.get('name', 'జాతకుడు')} గారి సంపూర్ణ జాతక నివేదిక (త్రైత సిద్ధాంతం)"
    
    overall_summary = {
        "name": data.get('name', 'జాతకుడు'),
        "dob": data.get('dob', ''),
        "tob": data.get('tob', ''),
        "place": data.get('place', ''),
        "lagna": lagna,
        "lagna_camp": lagna_camp_str,
        "nakshatra": f"{data.get('nakshatra', '')} ({data.get('padam', '')}వ పాదం)",
        "tithi": f"{data.get('tithi_paksha', '')} {data.get('tithi_name', '')}",
        "total_bhavas": 12,
        "health_summary": list(set(all_health_warnings))[:6],
        "wealth_summary": list(set(all_wealth_yogas))[:6],
        "marriage_summary": all_marriage_notes[:3],
        "progeny_summary": all_progeny_notes[:2],
        "accident_summary": all_accident_notes[:2],
        "spiritual_remedy": "త్రైత సిద్ధాంత ప్రకారం గ్రహాలు కర్మను స్వీకరించి అందించే పనిముట్లు మాత్రమే. జన్మజన్మల పాపకర్మను తొలగించుకోవడానికి భగవద్గీత జ్ఞానయోగం 37వ శ్లోకం ప్రకారం ఒక్క ఆత్మజ్ఞానము (దైవజ్ఞానము) మాత్రమే సమర్థవంతమైన మార్గం. సత్యశోధన, నిరాకార దైవభక్తితో కర్మ ప్రభావాలను జయించవచ్చును."
    }

    return {
        "report_title": report_title,
        "overall_summary": overall_summary,
        "bhava_report": bhava_report
    }

if __name__ == '__main__':
    # Test execution
    sample_data = {
        "name": "శ్రీనివాస్",
        "dob": "1988-08-20",
        "tob": "14:30",
        "place": "Hyderabad",
        "lagna": "ధనస్సు",
        "houses": {
            "ధనస్సు": 1, "మకరం": 2, "కుంభం": 3, "మీనం": 4, "మేషం": 5, "వృషభం": 6,
            "మిథునం": 7, "కర్కాటకం": 8, "సింహం": 9, "కన్య": 10, "తులా": 11, "వృశ్చికం": 12
        },
        "planet_positions": [
            {"name": "సూర్యుడు", "lagna": "సింహం", "degree": "3°45′", "is_hand": False},
            {"name": "చంద్రుడు", "lagna": "ధనస్సు", "degree": "12°10′", "is_hand": False},
            {"name": "కుజుడు", "lagna": "మేషం", "degree": "21°30′", "is_hand": False},
            {"name": "శుక్రుడు", "lagna": "మేషం", "degree": "18°20′", "is_hand": False},
            {"name": "శని", "lagna": "కర్కాటకం", "degree": "5°15′", "is_hand": False}
        ]
    }
    rep = generate_thraitha_jathaka_report(sample_data)
    print("Report generated successfully!")
    print("Title:", rep["report_title"])
    print("Bhavas count:", len(rep["bhava_report"]))
    print("House 5 (Aries - Kuja+Sukra):", rep["bhava_report"][4]["special_notes"])
