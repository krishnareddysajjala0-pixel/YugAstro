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

GURU_LAGNAS = ["మేషం", "మేషము", "కర్కాటకం", "కర్కాటకము", "సింహం", "సింహము", "వృశ్చికం", "వృశ్చికము", "ధనుస్సు", "ధనస్సు", "ధనువు", "మీనం", "మీనము"]
SANI_LAGNAS = ["వృషభం", "వృషభము", "మిథునం", "మిథునము", "కన్య", "కన్యక", "తులా", "తుల", "తులము", "మకరం", "మకరము", "కుంభం", "కుంభము"]

def normalize_rashi(r):
    """Normalize Telugu rashi names handling orthographic variants."""
    if not r:
        return ""
    r = r.strip()
    mapping = {
        "మేషము": "మేషం",
        "వృషభము": "వృషభం",
        "మిథునము": "మిథునం",
        "కర్కాటకము": "కర్కాటకం",
        "సింహము": "సింహం",
        "కన్యక": "కన్య",
        "తుల": "తులా",
        "తులము": "తులా",
        "వృశ్చికము": "వృశ్చికం",
        "ధనస్సు": "ధనుస్సు",
        "ధనువు": "ధనుస్సు",
        "ధను": "ధనుస్సు",
        "మకరము": "మకరం",
        "కుంభము": "కుంభం",
        "మీనము": "మీనం"
    }
    return mapping.get(r, r)

RASHI_ORDER = [
    "మేషం", "వృషభం", "మిథునం", "కర్కాటకం", "సింహం", "కన్య",
    "తులా", "వృశ్చికం", "ధనస్సు", "మకరం", "కుంభం", "మీనం"
]

# త్రైత సిద్ధాంతం ప్రకారం 12 రాశులకు 12 మంది ప్రత్యేక అధిపతులు (Strict 1-to-1 bijection).
# ఒక రాశికి / భావానికి ఒకే ఒక అధిపతి; ఒక గ్రహానికి ఒకే ఒక స్వక్షేత్రం / భావాధిపత్యం.
# పరాశర సిద్ధాంతంలోని ద్వి-రాశ్యాధిపత్యము (కుజుడికి 4, 11 లేదా గురువుకి 3, 12 మొదలైనవి) త్రైత సిద్ధాంతంలో వర్తించదు.
THRAITHA_RASHI_LORDS = {
    normalize_rashi("మేషం"): "కుజుడు",
    normalize_rashi("వృషభం"): "మిత్ర",
    normalize_rashi("మిథునం"): "చిత్ర",
    normalize_rashi("కర్కాటకం"): "చంద్రుడు",
    normalize_rashi("సింహం"): "సూర్యుడు",
    normalize_rashi("కన్య"): "బుధుడు",
    normalize_rashi("తులా"): "శుక్రుడు",
    normalize_rashi("వృశ్చికం"): "భూమి",
    normalize_rashi("ధనుస్సు"): "కేతువు",
    normalize_rashi("ధనస్సు"): "కేతువు",
    normalize_rashi("మకరం"): "రాహువు",
    normalize_rashi("కుంభం"): "శని",
    normalize_rashi("మీనం"): "గురువు"
}

PRIMARY_RASHI_LORDS = {r: [p] for r, p in THRAITHA_RASHI_LORDS.items()}

def find_bhava_conjunction_rule(h1, h2, cur_bhava, is_odd):
    """
    Finds the exact matching Thraitha Bhava Lord Conjunction rule from bhava_conjunctions.json.
    Matches (h1 + h2) or (h2 + h1) in cur_bhava key first, then by individual bhava keys,
    filtering by lagna parity (బేసి vs సరి లగ్నాలు).
    """
    if h1 == h2 or not CONJUNCTION_RULES:
        return None
    target_key = str(cur_bhava)
    combo_names = [f"{h1} + {h2} అధిపతులు", f"{h2} + {h1} అధిపతులు"]
    
    candidates = []
    # 1. Look in current bhava key first
    for r in CONJUNCTION_RULES.get(target_key, []):
        if r.get("combination") in combo_names:
            candidates.append(r)
            
    # 2. Look in h1 or h2 keys
    if not candidates:
        for k in [str(min(h1, h2)), str(max(h1, h2))]:
            for r in CONJUNCTION_RULES.get(k, []):
                if r.get("combination") in combo_names:
                    candidates.append(r)
                    
    # 3. Filter by parity
    for c in candidates:
        st = c.get("status", "")
        if "అన్ని లగ్నాలకు" in st:
            return c
        if is_odd and "బేసి లగ్నాలకు" in st:
            return c
        if not is_odd and "సరి లగ్నాలకు" in st:
            return c
            
    return candidates[0] if candidates else None

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
    raw_lagna = data.get('lagna', 'మేషం')
    lagna = normalize_rashi(raw_lagna)
    is_guru_lagna = (lagna in GURU_LAGNAS) or (raw_lagna in GURU_LAGNAS)
    lagna_camp_str = "గురు వర్గము (గురు పార్టీ)" if is_guru_lagna else "శని వర్గము (శని పార్టీ)"
    
    raw_houses = data.get('houses', {})
    houses = {}
    for rashi, h_num in raw_houses.items():
        try:
            h_int = int(h_num)
            houses[rashi] = h_int
            houses[normalize_rashi(rashi)] = h_int
        except Exception:
            pass

    # Invert houses mapping: house_number (1..12) -> rashi_name
    house_to_rashi = {}
    for rashi, h_num in raw_houses.items():
        try:
            house_to_rashi[int(h_num)] = normalize_rashi(rashi)
        except Exception:
            pass
            
    # Calculate Lagna index and Parity (Odd / Even Lagna)
    norm_rashi_order = [normalize_rashi(r) for r in RASHI_ORDER]
    lagna_idx = norm_rashi_order.index(lagna) if lagna in norm_rashi_order else 0
    is_odd_lagna = (lagna_idx % 2 == 0)  # 0 is Mesha (1st, odd), 8 is Dhanu (9th, odd)
    
    # Map each planet to the Bhava it rules for this native's Lagna (Strict 1-to-1 bijection)
    planet_to_bhavas = {}
    bhava_to_lords = {}
    for i in range(12):
        bhava_num = i + 1
        r_name = norm_rashi_order[(lagna_idx + i) % 12]
        lord = THRAITHA_RASHI_LORDS.get(r_name)
        if lord:
            bhava_to_lords[bhava_num] = [lord]
            p_clean = clean_planet_name(lord)
            planet_to_bhavas[p_clean] = [bhava_num]
            
    # Collect resident and aspecting planets per house
    planet_positions = data.get('planet_positions', [])
    house_residents = {i: [] for i in range(1, 13)}
    house_aspects = {i: [] for i in range(1, 13)}
    
    for pp in planet_positions:
        p_name = clean_planet_name(pp.get('name'))
        p_rashi = normalize_rashi(pp.get('lagna'))
        is_hand = pp.get('is_hand', False)
        
        h_num = houses.get(p_rashi)
        if h_num:
            h_num = int(h_num)
            p_bhavas = sorted(list(set(planet_to_bhavas.get(p_name, []))))
            lordships_str = f"{p_bhavas[0]}వ అధిపతి" if p_bhavas else ""
            entry = {
                "name": p_name,
                "degree": pp.get('degree', ''),
                "nakshatra": pp.get('nakshatra', ''),
                "padam": pp.get('padam', ''),
                "is_hand": is_hand,
                "camp": "గురు వర్గము" if p_name in GURU_CAMP else "శని వర్గము",
                "is_friend": (p_name in GURU_CAMP) if is_guru_lagna else (p_name in SANI_CAMP),
                "lordships": p_bhavas,
                "lordships_text": lordships_str
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
        
        # Thraitha Fundamental Principle:
        # A planet's aspect (చూపు / చేయి) exerts the EXACT SAME power and result as if the planet is residing in that house.
        # "గ్రహం అక్కడ ఉంటే ఎలాంటి ఫలితం ఉంటుందో, చూపు ఉన్నా అదే ఫలితం ఉంటుంది. చూపుకి, గ్రహానికి ఎటువంటి తేడా లేదు – రెండూ సమానమే!"
        active_planets = residents + aspects
        active_names = [p["name"] for p in active_planets]
        
        f_active = [p for p in active_planets if p["is_friend"]]
        e_active = [p for p in active_planets if not p["is_friend"]]
        
        active_count = len(active_planets)
        f_count = len(f_active)
        e_count = len(e_active)
        
        # State determination based on all active planets (residents + aspects)
        if active_count == 0:
            state = "neutral"
            state_text = "సంపూర్ణ ఖాళీ స్థానము (గ్రహ, దృష్టి రహితం)"
        elif f_count > e_count:
            state = "shubha"
            if len(residents) == 0:
                state_text = f"శుభ స్థితి ({f_count} మిత్రుల దృష్టి చేతుల ప్రభావం)"
            elif len(aspects) == 0:
                state_text = f"శుభ స్థితి ({f_count} మిత్రులు : {e_count} శత్రువులు)"
            else:
                state_text = f"శుభ స్థితి ({f_count} మిత్రులు : {e_count} శత్రువులు - నివాస & దృష్టి)"
        elif e_count > f_count:
            state = "paapa"
            if len(residents) == 0:
                state_text = f"పాప / ప్రతికూల స్థితి ({e_count} శత్రువుల దృష్టి చేతుల ప్రభావం)"
            elif len(aspects) == 0:
                state_text = f"పాప / ప్రతికూల స్థితి ({f_count} మిత్రులు : {e_count} శత్రువులు)"
            else:
                state_text = f"పాప / ప్రతికూల స్థితి ({f_count} మిత్రులు : {e_count} శత్రువులు - నివాస & దృష్టి)"
        else:
            state = "mishra"
            state_text = f"సమతుల్య / అంతర్యుద్ధ స్థితి ({f_count} మిత్రులు : {e_count} శత్రువులు)"
            
        # Synthesize Detailed Interpretation
        interpretation_parts = []
        special_notes = []
        applied_items = []
        applied_diseases = []
        
        # Collect Governed Items & Diseases from ALL active planets (residents AND aspects)
        for p_obj in active_planets:
            pn = p_obj["name"]
            p_full = PLANET_DATA.get(pn, {})
            if p_full:
                applied_items.extend(p_full.get("governed_physical_items", [])[:3])
                applied_diseases.extend(p_full.get("governed_body_parts_and_diseases", {}).get("diseases", [])[:2])

        # 1. Single Planet Evaluation (Either resident OR aspecting hand - both are same!)
        if active_count == 1:
            p_obj = active_planets[0]
            pn = p_obj["name"]
            is_fr = p_obj["is_friend"]
            is_aspect = p_obj.get("is_hand", False)
            
            p_full = PLANET_DATA.get(pn, {})
            lookup = SINGLE_LOOKUP.get((b_num, pn))
            
            if is_aspect:
                drishti_intro = f"👉 <b>త్రైత సిద్ధాంత దృష్టి సూత్రము:</b> త్రైత సిద్ధాంతం ప్రకారం ఒక భావంలో గ్రహం స్వయంగా ఉన్నా లేదా తన దృష్టి చేతితో ఆ భావాన్ని తాకినా రెండింటి ఫలితం అక్షరాలా ఒక్కటే! ఇక్కడ <b>{pn}</b> తన దృష్టి చేతితో ఈ {b_num}వ భావాన్ని తాకుచున్నందున, {pn} ఈ స్థానంలో స్వయంగా ఉన్నప్పటి ఫలితమే సంపూర్ణంగా వర్తిస్తుంది.<br>"
                interpretation_parts.append(drishti_intro)
                if lookup:
                    if is_fr:
                        interpretation_parts.append(f"✨ <b>{pn} (స్వపక్ష మిత్రుడి దృష్టి చేయి):</b> {lookup.get('friendly_state_result', '')}")
                    else:
                        interpretation_parts.append(f"⚠️ <b>{pn} (ప్రతిపక్ష శత్రువు దృష్టి చేయి):</b> {lookup.get('enemy_state_result', '')}")
                else:
                    if is_fr:
                        interpretation_parts.append(f"ఈ భావముపై స్వపక్ష మిత్రుడైన <b>{pn}</b> దృష్టి ప్రసరించడం వల్ల ఈ భావ కారకత్వాలు శుభప్రదంగా వికసిస్తాయి.")
                    else:
                        interpretation_parts.append(f"ఈ భావముపై శత్రువర్గానికి చెందిన <b>{pn}</b> దృష్టి ప్రసరించడం వల్ల ఆటంకాలు, నష్టాలు లేదా ఆందోళనలు దాపురిస్తాయి.")
            else:
                if lookup:
                    if is_fr:
                        interpretation_parts.append(f"✨ <b>{pn} (స్వపక్ష మిత్రుడు):</b> {lookup.get('friendly_state_result', '')}")
                    else:
                        interpretation_parts.append(f"⚠️ <b>{pn} (ప్రతిపక్ష శత్రువు):</b> {lookup.get('enemy_state_result', '')}")
                else:
                    if is_fr:
                        interpretation_parts.append(f"ఈ భావంలో స్వపక్ష మిత్రుడైన <b>{pn}</b> ఒక్కడే ఉండటం వల్ల ఈ భావ కారకత్వాలు శుభప్రదంగా వికసిస్తాయి. {pn} యొక్క సహజ దయాగుణం, సత్ప్రవర్తన మరియు దైవానుగ్రహం లభిస్తాయి.")
                    else:
                        interpretation_parts.append(f"ఈ భావంలో శత్రువర్గానికి చెందిన <b>{pn}</b> ఉండటం వల్ల ఈ భావ కారకత్వాలలో ఆటంకాలు, నష్టాలు లేదా ఆందోళనలు దాపురిస్తాయి.")

            if lookup and lookup.get('key_thraitha_sutra'):
                special_notes.append(f"📌 <b>త్రైత సూత్రము:</b> {lookup.get('key_thraitha_sutra')}")

            if b_num == 4 and pn == "సూర్యుడు" and is_fr:
                interpretation_parts.append("సూర్యుడి శుభ దృష్టి/ప్రభావం వల్ల పై అంతస్తుల భవనాలు, రాజగౌరవం లభించును.")
            elif b_num == 4 and pn == "చంద్రుడు" and not is_fr:
                interpretation_parts.append("చంద్రుడి ప్రతికూల దృష్టి/స్థితి వల్ల నీటి కొరత, బోర్లు పూడిపోవడం లేదా ఇంటి పైకప్పు కారే సమస్యలు ఏర్పడవచ్చును.")
            elif b_num == 6 and pn == "బుధుడు" and not is_fr:
                interpretation_parts.append("బుధుడు శత్రువై తాకుచున్నందున దయ్యాలు, క్షుద్ర పీడలు రోగరూపంలో శరీరంలో ప్రవేశించే భయముండును.")
            elif b_num == 7 and pn == "కుజుడు" and not is_fr:
                interpretation_parts.append("యౌవన కారక కుజుడు 7వ ఇంట్లో శత్రువై ఉన్నా లేదా ఎదురు చూపుతో తాకినా కుజదోషం ఏర్పడి వివాహం ఆలస్యం కావడం, వయస్సు ముదరడం జరుగుతుంది.")

        # 2. Two Planets Evaluation (Direct residence + Aspect hands combined)
        elif active_count == 2:
            p1, p2 = active_names[0], active_names[1]
            p1_fr = active_planets[0]["is_friend"]
            p2_fr = active_planets[1]["is_friend"]
            has_aspects = any(p["is_hand"] for p in active_planets)

            if has_aspects:
                interpretation_parts.append("👉 <b>త్రైత సిద్ధాంత దృష్టి-సంయోగ సూత్రము:</b> ఈ భావంపై గ్రహాలు ప్రత్యక్ష నివాసం మరియు దృష్టి చేతుల ద్వారా సమాన బలంతో సంయుక్తంగా ప్రభావం చూపుచున్నవి (చూపు మరియు గ్రహం రెండూ సమానమే).<br>")

            if p1_fr and p2_fr:
                interpretation_parts.append(f"ఈ భావంలో ఇద్దరు మిత్రులు (<b>{p1} + {p2}</b>) కలిసి/దృష్టి చేతుల ద్వారా ప్రభావం చూపడం గొప్ప యోగం. వీరిద్దరి సంయుక్త పుణ్యబలం వల్ల ఈ భావ ఫలితాలు రెట్టింపు స్థాయిలో శుభాలను ఇస్తాయి.")
            elif not p1_fr and not p2_fr:
                interpretation_parts.append(f"ఈ భావంలో ఇద్దరు శత్రువులు (<b>{p1} + {p2}</b>) కలిసి/దృష్టి చేతుల ద్వారా తీవ్ర వ్యతిరేకతను కలిగిస్తున్నారు. నష్టాలు, వ్యతిరేక ఫలితాలు హెచ్చుగా ఉంటాయి.")
            else:
                interpretation_parts.append(f"ఈ భావంలో ఒక మిత్రుడు మరియు ఒక శత్రువు (<b>{p1} + {p2}</b>) సమక్షం/దృష్టి చేతుల వల్ల అంతర్గత ఘర్షణ ఏర్పడుతుంది. పుణ్యఫలాలు చేతికందినా ఆటంకాలు ఎదురవుతాయి.")

            # Check Kuja-Sukra
            if ("కుజుడు" in active_names or "కుజ" in active_names) and ("శుక్రుడు" in active_names or "శుక్ర" in active_names):
                special_notes.append("⚠️ <b>కుజ-శుక్ర కలయిక / పరస్పర దృష్టి సూత్రము:</b> యౌవన కారక కుజుడు, కళత్ర కారక శుక్రుడు బద్ధశత్రువులు. వీరు ఒకే ఇంట్లో కలిసినా లేదా పరస్పర దృష్టి చేతులతో తాకినా దాంపత్యంలో పొందిక లోపించడం, మాటకు మాట పోట్లాడుకోవడం లేదా వివాహేతర ఆకర్షణల వల్ల కలహాలు ఏర్పడే అవకాశముంది. జాగ్రత్త వహించవలెను.")
                all_marriage_notes.append(f"{b_num}వ భావంలో కుజ-శుక్రుల కలయిక/దృష్టి వల్ల దాంపత్య పొందికలో జాగ్రత్తలు అవసరం.")

        # 3. Multi-planet Evaluation (3 to 12 planets)
        elif active_count >= 3:
            if any(p["is_hand"] for p in active_planets):
                interpretation_parts.append("👉 <b>త్రైత సిద్ధాంత దృష్టి-కూటమి సూత్రము:</b> ఈ భావంపై నివాస గ్రహాలతో పాటు ఎదురు చూపుల చేతులు కూడా పూర్తి బలంతో కలిసి బహుగ్రహ కూటమిని ఏర్పరచినవి.<br>")

            if active_count == 12:
                interpretation_parts.append("✨ <b>ద్వాదశ గ్రహ మహా కూటమి:</b> సమస్త 12 గ్రహాలు ఈ ఒక్క భావంపైనే (నివాసం & దృష్టి ద్వారా) కేంద్రీకృతమయ్యాయి! ఇది 'సర్వ కారకత్వ విస్ఫోటనం' మరియు 'సంపూర్ణ సన్న్యాస / బ్రహ్మజ్ఞాన యోగం'. ప్రాపంచిక లాభనష్టాలు రెండూ నిరర్ధకమై తీవ్ర వైరాగ్యం జనించి పరమాత్మ వైపు చూపు మళ్ళుతుంది.")
            elif active_count == 3:
                triad_rules = MULTI_PLANET_SYSTEM.get("multi_planet_rules_by_count", {}).get("3_planets_mix", {}).get("compositions", [])
                matched_rule = None
                for tr in triad_rules:
                    if f"{f_count} Friends" in tr.get("case", "") or f"{f_count} మిత్రు" in tr.get("case", ""):
                        matched_rule = tr
                        break
                if matched_rule:
                    interpretation_parts.append(f"<b>3 గ్రహాల కలయిక/దృష్టి కూటమి ({', '.join(active_names)}) - {matched_rule.get('nature')}:</b><br>{matched_rule.get('result')}")
                else:
                    interpretation_parts.append(f"ఈ భావంలో 3 గ్రహాల కూటమి ({', '.join(active_names)}) ఏర్పడింది ({f_count} మిత్రులు : {e_count} శత్రువులు).")
            elif active_count == 4:
                quad_rules = MULTI_PLANET_SYSTEM.get("multi_planet_rules_by_count", {}).get("4_planets_mix", {}).get("compositions", [])
                matched_rule = None
                for qr in quad_rules:
                    if f"{f_count} Friends" in qr.get("case", "") or f"{f_count} మిత్రు" in qr.get("case", ""):
                        matched_rule = qr
                        break
                if matched_rule:
                    interpretation_parts.append(f"<b>4 గ్రహాల చతుర్గ్రహ కూటమి ({', '.join(active_names)}) - {matched_rule.get('nature')}:</b><br>{matched_rule.get('result')}")
                else:
                    interpretation_parts.append(f"ఈ భావంలో 4 గ్రహాల కూటమి ({', '.join(active_names)}) ఏర్పడింది ({f_count} మిత్రులు : {e_count} శత్రువులు).")
            elif active_count == 5:
                pent_rule = MULTI_PLANET_SYSTEM.get("multi_planet_rules_by_count", {}).get("5_planets_mix", {})
                interpretation_parts.append(f"<b>5 గ్రహాల పంచగ్రహ కూటమి ({', '.join(active_names)}) - {pent_rule.get('title')}:</b><br>జాతకుడి జీవిత ధ్యేయమంతా, ఆలోచనలన్నీ ఈ ఒక్క భావ కార్యకలాపాల చుట్టూనే పరిభ్రమిస్తాయి ({f_count} మిత్రులు : {e_count} శత్రువులు).")
            else:
                interpretation_parts.append(f"ఈ భావంలో <b>{active_count} గ్రహాల అసాధారణ బహుగ్రహ కూటమి ({', '.join(active_names)})</b> ఏర్పడింది ({f_count} మిత్రులు : {e_count} శత్రువులు). ఈ భావ కారకత్వాలలో జీవితంలో అనూహ్యమైన విప్లవాత్మక మలుపులు, తీవ్ర అనిశ్చితి లేదా మహా పరివర్తన చోటుచేసుకుంటాయి.")

        # 4. Completely Empty House (Zero residents AND Zero aspects)
        else:
            interpretation_parts.append("ఈ భావంలో ప్రత్యక్షంగా ఏ గ్రహాలూ నివాసం లేవు, మరియు ఏ గ్రహం యొక్క దృష్టి చేతులు కూడా ఈ స్థానాన్ని తాకడం లేదు. ఈ భావ ఫలితం కేవలం భావాధిపతి స్థానబలాన్ని బట్టి లభిస్తుంది.")

        # 5. Bhava Lord Conjunctions Evaluation (భవాధిపతుల కలయిక & దృష్టి ఫలితాలు - 234 Conjunction Rules)
        bhava_lord_conjunctions = []
        if active_count >= 2:
            seen_combos = set()
            for i_p, p1_o in enumerate(active_planets):
                for j_p, p2_o in enumerate(active_planets):
                    if i_p >= j_p:
                        continue
                    p1_n = p1_o["name"]
                    p2_n = p2_o["name"]
                    h1_list = p1_o.get("lordships", [])
                    h2_list = p2_o.get("lordships", [])

                    for h1 in h1_list:
                        for h2 in h2_list:
                            pair_key = tuple(sorted([h1, h2]))
                            if pair_key in seen_combos:
                                continue
                            seen_combos.add(pair_key)

                            rule = find_bhava_conjunction_rule(h1, h2, b_num, is_odd_lagna)
                            if rule:
                                is_curr = (h1 == b_num or h2 == b_num)
                                bhava_lord_conjunctions.append({
                                    "p1": p1_n,
                                    "p2": p2_n,
                                    "h1": h1,
                                    "h2": h2,
                                    "is_current": is_curr,
                                    "combo": rule.get("combination"),
                                    "status": rule.get("status"),
                                    "result": rule.get("result")
                                })

            # Prioritize: combinations involving this current bhava lord first, then Kendra/Kona (1,4,5,9,10)
            def conj_priority(item):
                if item["is_current"]:
                    return 0
                is_kendra_kona = (item["h1"] in [1, 4, 5, 9, 10] and item["h2"] in [1, 4, 5, 9, 10])
                return 1 if is_kendra_kona else 2

            bhava_lord_conjunctions.sort(key=lambda x: (conj_priority(x), x["h1"]))

            if bhava_lord_conjunctions:
                interpretation_parts.append("<br><b>🏛️ భవాధిపతుల కలయిక & దృష్టి ఫలితాలు (త్రైత సిద్ధాంతం):</b>")
                for c in bhava_lord_conjunctions[:5]:
                    interpretation_parts.append(
                        f"• 👑 <b>{c['combo']} ({c['p1']} + {c['p2']})</b> — <span style='color:#fbbf24;'>[{c['status']}]</span>:<br>{c['result']}"
                    )

        # Check House 8 Longevity / Accidents (considering both residence AND aspects)
        if b_num == 8 or ("కుజుడు" in active_names and "శని" in active_names):
            if not is_guru_lagna and ("కుజుడు" in active_names or "కుజ" in active_names):
                special_notes.append("⚠️ <b>ఆయుర్దాయ & ప్రమాద సూచన (గాంధీ, రాజీవ్ గాంధీ సూత్రం):</b> ఆయుః స్థానమైన 8వ భావముపై కుజుడి ప్రభావం (నివాసం లేదా దృష్టి చేతి తాకిడి) ఉన్నందున రక్తపాత, ఆయుధ, లేదా వాహన ప్రమాదాల పట్ల అప్రమత్తంగా ఉండాలి. నిత్యం దైవస్మరణ, ఆత్మజ్ఞాన విచారణ రక్షణ కల్పిస్తుంది.")
                all_accident_notes.append("8వ భావంలో కుజస్పర్శ వల్ల వాహనాలు నడిపేటప్పుడు, రక్తపాత ప్రమాదాల పట్ల జాగ్రత్త అవసరం.")

        # Check House 5 Santhanam (considering both residence AND aspects)
        if b_num == 5:
            has_guru = any(p["name"] in ["గురువు", "గురు"] for p in active_planets)
            has_chandra = any(p["name"] in ["చంద్రుడు", "చంద్ర"] for p in active_planets)
            if has_guru or has_chandra:
                if state == "shubha":
                    special_notes.append("✨ <b>సంతాన భాగ్య సూత్రము:</b> 5వ స్థానంలో సంతాన కారక గ్రహములు (నివాసం లేదా దృష్టి ద్వారా) అనుకూలంగా ఉన్నందున వంశోద్ధారకులైన ఉత్తమ సంతాన ప్రాప్తి, మేధాసంపత్తి కలుగును.")
                    all_progeny_notes.append("5వ భావంలో సంతాన కారక గ్రహాల అనుకూలత వల్ల సుపుత్ర ప్రాప్తి కలుగుతుంది.")
                else:
                    special_notes.append("⚠️ <b>సంతాన దోష సూచన:</b> 5వ స్థానంలో శత్రుగ్రహాల కలయిక/దృష్టి వల్ల సంతాన విషయంలో ఆలస్యం లేదా ఆందోళనలు రావచ్చును.")
                    all_progeny_notes.append("5వ భావంలో శత్రుగ్రహాల ప్రభావం వల్ల సంతాన విషయంలో జాగ్రత్తలు, దైవారాధన అవసరం.")


        # Category Aggregation
        if applied_diseases:
            all_health_warnings.extend(applied_diseases)
        if applied_items:
            all_wealth_yogas.extend(applied_items)

        if resident_names and aspect_names:
            planets_text = f"{', '.join(resident_names)} (ఎదురు చూపు: {', '.join(aspect_names)})"
        elif resident_names:
            planets_text = ", ".join(resident_names)
        elif aspect_names:
            planets_text = f"ఖాళీ (ఎదురు చూపుల చేతులు: {', '.join(aspect_names)})"
        else:
            planets_text = "సంపూర్ణ ఖాళీ (దృష్టి రహితం)"

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
            "planets_text": planets_text,
            "bhava_lord_conjunctions": bhava_lord_conjunctions,
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
