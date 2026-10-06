"""
Marriage Compatibility Engine (దక్షిణ భారత / తెలుగు వివాహ దశకూట & ద్వాదశకూట పొంతన)
===================================================================================
Self-contained calculation engine for South Indian Telugu Dashakoota Porutham,
Special Nakshatra Doshas, Lagna Compatibility, 8th House Mangalya Bhagyam,
Rahu-Ketu 1/7 Axis Balance, and Detailed Shadashtaka.

Does NOT modify or affect any existing Kundali, Dasacharam, or general chart pages.
"""

# Master 27 Nakshatras Data Table (Exact User Specification)
NAKSHATRA_DATA = {
    "అశ్విని": {
        "index": 1,
        "gana": "దేవ",
        "yoni": "గుర్రం",
        "nadi": "ఆది",
        "rajju": "పాద",
        "lord": "కేతు",
    },
    "భరణి": {
        "index": 2,
        "gana": "మనుష్య",
        "yoni": "ఏనుగు",
        "nadi": "మధ్య",
        "rajju": "కటి",
        "lord": "శుక్రుడు",
    },
    "కృత్తిక": {
        "index": 3,
        "gana": "రాక్షస",
        "yoni": "మేక",
        "nadi": "అంత్య",
        "rajju": "నాభి",
        "lord": "సూర్యుడు",
    },
    "రోహిణి": {
        "index": 4,
        "gana": "మనుష్య",
        "yoni": "సర్పం",
        "nadi": "అంత్య",
        "rajju": "కంఠ",
        "lord": "చంద్రుడు",
    },
    "మృగశిర": {
        "index": 5,
        "gana": "దేవ",
        "yoni": "సర్పం",
        "nadi": "మధ్య",
        "rajju": "శిరస్సు",
        "lord": "కుజుడు",
    },
    "ఆర్ద్ర": {
        "index": 6,
        "gana": "మనుష్య",
        "yoni": "కుక్క",
        "nadi": "ఆది",
        "rajju": "కంఠ",
        "lord": "రాహు",
    },
    "పునర్వసు": {
        "index": 7,
        "gana": "దేవ",
        "yoni": "పిల్లి",
        "nadi": "ఆది",
        "rajju": "నాభి",
        "lord": "గురుడు",
    },
    "పుష్యమి": {
        "index": 8,
        "gana": "దేవ",
        "yoni": "మేక",
        "nadi": "మధ్య",
        "rajju": "కటి",
        "lord": "శని",
    },
    "ఆశ్లేష": {
        "index": 9,
        "gana": "రాక్షస",
        "yoni": "పిల్లి",
        "nadi": "అంత్య",
        "rajju": "పాద",
        "lord": "బుధుడు",
    },
    "మఖ": {
        "index": 10,
        "gana": "రాక్షస",
        "yoni": "ఎలుక",
        "nadi": "ఆది",
        "rajju": "పాద",
        "lord": "కేతు",
    },
    "పూర్వఫల్గుణి": {
        "index": 11,
        "gana": "మనుష్య",
        "yoni": "ఎలుక",
        "nadi": "మధ్య",
        "rajju": "కటి",
        "lord": "శుక్రుడు",
    },
    "ఉత్తరఫల్గుణి": {
        "index": 12,
        "gana": "మనుష్య",
        "yoni": "ఆవు",
        "nadi": "అంత్య",
        "rajju": "నాభి",
        "lord": "సూర్యుడు",
    },
    "హస్త": {
        "index": 13,
        "gana": "దేవ",
        "yoni": "దున్నపోతు",
        "nadi": "ఆది",
        "rajju": "కంఠ",
        "lord": "చంద్రుడు",
    },
    "చిత్ర": {
        "index": 14,
        "gana": "రాక్షస",
        "yoni": "పులి",
        "nadi": "మధ్య",
        "rajju": "శిరస్సు",
        "lord": "కుజుడు",
    },
    "స్వాతి": {
        "index": 15,
        "gana": "దేవ",
        "yoni": "దున్నపోతు",
        "nadi": "అంత్య",
        "rajju": "కంఠ",
        "lord": "రాహు",
    },
    "విశాఖ": {
        "index": 16,
        "gana": "రాక్షస",
        "yoni": "పులి",
        "nadi": "ఆది",
        "rajju": "నాభి",
        "lord": "గురుడు",
    },
    "అనూరాధ": {
        "index": 17,
        "gana": "దేవ",
        "yoni": "జింక",
        "nadi": "మధ్య",
        "rajju": "కటి",
        "lord": "శని",
    },
    "జ్యేష్ఠ": {
        "index": 18,
        "gana": "రాక్షస",
        "yoni": "జింక",
        "nadi": "అంత్య",
        "rajju": "పాద",
        "lord": "బుధుడు",
    },
    "మూల": {
        "index": 19,
        "gana": "రాక్షస",
        "yoni": "కుక్క",
        "nadi": "ఆది",
        "rajju": "పాద",
        "lord": "కేతు",
    },
    "పూర్వాషాఢ": {
        "index": 20,
        "gana": "మనుష్య",
        "yoni": "కోతి",
        "nadi": "మధ్య",
        "rajju": "కటి",
        "lord": "శుక్రుడు",
    },
    "ఉత్తరాషాఢ": {
        "index": 21,
        "gana": "మనుష్య",
        "yoni": "ముంగిస",
        "nadi": "అంత్య",
        "rajju": "నాభి",
        "lord": "సూర్యుడు",
    },
    "శ్రవణం": {
        "index": 22,
        "gana": "దేవ",
        "yoni": "కోతి",
        "nadi": "ఆది",
        "rajju": "కంఠ",
        "lord": "చంద్రుడు",
    },
    "ధనిష్ఠ": {
        "index": 23,
        "gana": "రాక్షస",
        "yoni": "సింహం",
        "nadi": "మధ్య",
        "rajju": "శిరస్సు",
        "lord": "కుజుడు",
    },
    "శతభిషం": {
        "index": 24,
        "gana": "రాక్షస",
        "yoni": "గుర్రం",
        "nadi": "అంత్య",
        "rajju": "కంఠ",
        "lord": "రాహు",
    },
    "పూర్వాభాద్ర": {
        "index": 25,
        "gana": "మనుష్య",
        "yoni": "సింహం",
        "nadi": "ఆది",
        "rajju": "నాభి",
        "lord": "గురుడు",
    },
    "ఉత్తరాభాద్ర": {
        "index": 26,
        "gana": "మనుష్య",
        "yoni": "ఆవు",
        "nadi": "మధ్య",
        "rajju": "కటి",
        "lord": "శని",
    },
    "రేవతి": {
        "index": 27,
        "gana": "దేవ",
        "yoni": "ఏనుగు",
        "nadi": "అంత్య",
        "rajju": "పాద",
        "lord": "బుధుడు",
    },
}

# 12 Rashis List (Exact User Specification)
RASHIS = [
    "మేషం",
    "వృషభం",
    "మిథునం",
    "కర్కాటకం",
    "సింహం",
    "కన్య",
    "తుల",
    "వృశ్చికం",
    "ధనుస్సు",
    "మకరం",
    "కుంభం",
    "మీనం",
]

# Rashi Lords Mapping (Exact User Specification)
RASHI_LORDS = {
    "మేషం": "కుజుడు",
    "వృషభం": "శుక్రుడు",
    "మిథునం": "బుధుడు",
    "కర్కాటకం": "చంద్రుడు",
    "సింహం": "సూర్యుడు",
    "కన్య": "బుధుడు",
    "తుల": "శుక్రుడు",
    "వృశ్చికం": "కుజుడు",
    "ధనుస్సు": "గురుడు",
    "మకరం": "శని",
    "కుంభం": "శని",
    "మీనం": "గురుడు",
}

# Name aliases for seamless interoperability
NAKSHATRA_ALIASES = {
    "చిత్త": "చిత్ర",
    "శ్రవణ": "శ్రవణం",
    "శతభిష": "శతభిషం",
    "ఆరుద్ర": "ఆర్ద్ర",
    "పుబ్బ": "పూర్వఫల్గుణి",
    "పూర్వ ఫల్గుణి": "పూర్వఫల్గుణి",
    "ఉత్తర": "ఉత్తరఫల్గుణి",
    "ఉత్తర ఫల్గుణి": "ఉత్తరఫల్గుణి",
}

RASHI_ALIASES = {
    "తులా": "తుల",
    "ధనస్సు": "ధనుస్సు"
}

# Standard Constants & Matrices
DINA_GOOD = {2, 4, 6, 8, 9, 11, 13, 15, 18, 20, 24, 26}
MAHENDRA_GOOD = {4, 7, 10, 13, 16, 19, 22, 25}

GANA_MATRIX = {
    ("దేవ", "దేవ"): {"score": 1.0, "status": "ఉత్తమం", "icon": "✅", "desc": "ఇద్దరిదీ దేవ గణము. అత్యుత్తమ మనోవైఖరి, దాంపత్య శాంతి."},
    ("మనుష్య", "మనుష్య"): {"score": 1.0, "status": "ఉత్తమం", "icon": "✅", "desc": "ఇద్దరిదీ మనుష్య గణము. ఆదర్శవంతమైన జీవన శైలి."},
    ("దేవ", "మనుష్య"): {"score": 0.5, "status": "మధ్యమం", "icon": "✅", "desc": "వధువు దేవ గణం, వరుడు మనుష్య గణం. పరస్పర సహకారం కలదు."},
    ("మనుష్య", "దేవ"): {"score": 0.5, "status": "మధ్యమం", "icon": "✅", "desc": "వధువు మనుష్య గణం, వరుడు దేవ గణం. గౌరవప్రదమైన అనుకూలత."},
    ("రాక్షస", "రాక్షస"): {"score": 0.5, "status": "మధ్యమం", "icon": "⚠️", "desc": "ఇద్దరిదీ రాక్షస గణం. సమాన స్వభావాలు, సర్దుబాటు అవసరం."},
    ("దేవ", "రాక్షస"): {"score": 0.0, "status": "బలహీనము", "icon": "❌", "desc": "వధువు దేవ గణం, వరుడు రాక్షస గణం. స్వభావ భేదాలు రావచ్చు."},
    ("మనుష్య", "రాక్షస"): {"score": 0.0, "status": "బలహీనము", "icon": "❌", "desc": "వధువు మనుష్య గణం, వరుడు రాక్షస గణం. అభిప్రాయ భేదాలు రావచ్చు."},
    ("రాక్షస", "దేవ"): {"score": 0.0, "status": "బలహీనము", "icon": "❌", "desc": "వధువు రాక్షస గణం, వరుడు దేవ గణం. సంప్రదాయం ప్రకారం బలహీన పొంతన."},
    ("రాక్షస", "మనుష్య"): {"score": 0.0, "status": "బలహీనము", "icon": "❌", "desc": "వధువు రాక్షస గణం, వరుడు మనుష్య గణం. బలహీన పొంతన."}
}

YONI_ENEMIES = {
    ("గుర్రం", "దున్నపోతు"), ("దున్నపోతు", "గుర్రం"),
    ("ఏనుగు", "సింహం"), ("సింహం", "ఏనుగు"),
    ("మేక", "కోతి"), ("కోతి", "మేక"),
    ("సర్పం", "ముంగిస"), ("ముంగిస", "సర్పం"),
    ("కుక్క", "జింక"), ("జింక", "కుక్క"),
    ("పిల్లి", "ఎలుక"), ("ఎలుక", "పిల్లి"),
    ("ఆవు", "పులి"), ("పులి", "ఆవు")
}

# Vasya Matrix
VASYA_MATRIX = {
    "మేషం": ["సింహం", "వృశ్చికం"],
    "వృషభం": ["కర్కాటకం", "తుల"],
    "మిథునం": ["కన్య"],
    "కర్కాటకం": ["వృశ్చికం", "ధనుస్సు"],
    "సింహం": ["తుల"],
    "కన్య": ["మిథునం", "మీనం"],
    "తుల": ["మకరం"],
    "వృశ్చికం": ["కర్కాటకం", "కన్య"],
    "ధనుస్సు": ["మీనం"],
    "మకరం": ["కుంభం", "మేషం"],
    "కుంభం": ["మేషం"],
    "మీనం": ["మకరం"]
}

# Vedha Pairs (13 Classical Pairs)
VEDHA_PAIRS = {
    ("అశ్విని", "జ్యేష్ఠ"), ("జ్యేష్ఠ", "అశ్విని"),
    ("భరణి", "అనూరాధ"), ("అనూరాధ", "భరణి"),
    ("కృత్తిక", "విశాఖ"), ("విశాఖ", "కృత్తిక"),
    ("రోహిణి", "స్వాతి"), ("స్వాతి", "రోహిణి"),
    ("మృగశిర", "ధనిష్ఠ"), ("ధనిష్ఠ", "మృగశిర"),
    ("ఆర్ద్ర", "శ్రవణం"), ("శ్రవణం", "ఆర్ద్ర"),
    ("పునర్వసు", "ఉత్తరాషాఢ"), ("ఉత్తరాషాఢ", "పునర్వసు"),
    ("పుష్యమి", "పూర్వాషాఢ"), ("పూర్వాషాఢ", "పుష్యమి"),
    ("ఆశ్లేష", "మూల"), ("మూల", "ఆశ్లేష"),
    ("మఖ", "రేవతి"), ("రేవతి", "మఖ"),
    ("పూర్వఫల్గుణి", "ఉత్తరాభాద్ర"), ("ఉత్తరాభాద్ర", "పూర్వఫల్గుణి"),
    ("ఉత్తరఫల్గుణి", "పూర్వాభాద్ర"), ("పూర్వాభాద్ర", "ఉత్తరఫల్గుణి"),
    ("హస్త", "శతభిషం"), ("శతభిషం", "హస్త")
}

# Vriksha (Sacred Trees) & Milky Sap Mapping
VRIKSHA_DATA = {
    "అశ్విని": {"tree": "విషముష్టి", "is_milky": False},
    "భరణి": {"tree": "ఉసిరి", "is_milky": False},
    "కృత్తిక": {"tree": "అత్తి / మేడి", "is_milky": True},
    "రోహిణి": {"tree": "నేరేడు", "is_milky": False},
    "మృగశిర": {"tree": "చండ్ర", "is_milky": False},
    "ఆర్ద్ర": {"tree": "తింత్రిణి (చింత)", "is_milky": False},
    "పునర్వసు": {"tree": "వెదురు", "is_milky": False},
    "పుష్యమి": {"tree": "రావి", "is_milky": True},
    "ఆశ్లేష": {"tree": "నాగకేసరి", "is_milky": False},
    "మఖ": {"tree": "మర్రి", "is_milky": True},
    "పూర్వఫల్గుణి": {"tree": "మోదుగ", "is_milky": False},
    "ఉత్తరఫల్గుణి": {"tree": "జువ్వి", "is_milky": True},
    "హస్త": {"tree": "జమ్మి", "is_milky": False},
    "చిత్ర": {"tree": "తాటి", "is_milky": False},
    "స్వాతి": {"tree": "మద్ది", "is_milky": False},
    "విశాఖ": {"tree": "వెలగ", "is_milky": False},
    "అనూరాధ": {"tree": "పొగడ", "is_milky": False},
    "జ్యేష్ఠ": {"tree": "విరిగి / దేవదారు", "is_milky": False},
    "మూల": {"tree": "మద్ది (సాల)", "is_milky": False},
    "పూర్వాషాఢ": {"tree": "అశోక", "is_milky": False},
    "ఉత్తరాషాఢ": {"tree": "పనస", "is_milky": True},
    "శ్రవణం": {"tree": "జిల్లేడు", "is_milky": True},
    "ధనిష్ఠ": {"tree": "జమ్మి", "is_milky": False},
    "శతభిషం": {"tree": "కదంబ", "is_milky": False},
    "పూర్వాభాద్ర": {"tree": "మామిడి", "is_milky": False},
    "ఉత్తరాభాద్ర": {"tree": "వేప", "is_milky": False},
    "రేవతి": {"tree": "ఇప్ప", "is_milky": True},
}

# 5 Elements (Pancha Bhoota) Mapping
BHOOTA_MAP = {
    # Prithvi (భూమి)
    "అశ్విని": "భూమి", "భరణి": "భూమి", "కృత్తిక": "భూమి", "రోహిణి": "భూమి", "మృగశిర": "భూమి",
    # Jala (జలం)
    "ఆర్ద్ర": "జలం", "పునర్వసు": "జలం", "పుష్యమి": "జలం", "ఆశ్లేష": "జలం", "మఖ": "జలం", "పూర్వఫల్గుణి": "జలం",
    # Agni (అగ్ని)
    "ఉత్తరఫల్గుణి": "అగ్ని", "హస్త": "అగ్ని", "చిత్ర": "అగ్ని", "స్వాతి": "అగ్ని", "విశాఖ": "అగ్ని", "అనూరాధ": "అగ్ని",
    # Vayu (వాయువు)
    "జ్యేష్ఠ": "వాయువు", "మూల": "వాయువు", "పూర్వాషాఢ": "వాయువు", "ఉత్తరాషాఢ": "వాయువు", "శ్రవణం": "వాయువు",
    # Akasa (ఆకాశం)
    "ధనిష్ఠ": "ఆకాశం", "శతభిషం": "ఆకాశం", "పూర్వాభాద్ర": "ఆకాశం", "ఉత్తరాభాద్ర": "ఆకాశం", "రేవతి": "ఆకాశం"
}

# Planetary Relationships
PLANET_FRIENDS = {
    "సూర్యుడు": {
        "friends": ["చంద్రుడు", "కుజుడు", "గురుడు"],
        "neutrals": ["బుధుడు"],
        "enemies": ["శుక్రుడు", "శని"]
    },
    "చంద్రుడు": {
        "friends": ["సూర్యుడు", "బుధుడు"],
        "neutrals": ["కుజుడు", "గురుడు", "శుక్రుడు", "శని"],
        "enemies": []
    },
    "కుజుడు": {
        "friends": ["సూర్యుడు", "చంద్రుడు", "గురుడు"],
        "neutrals": ["శుక్రుడు", "శని"],
        "enemies": ["బుధుడు"]
    },
    "బుధుడు": {
        "friends": ["సూర్యుడు", "శుక్రుడు"],
        "neutrals": ["కుజుడు", "గురుడు", "శని"],
        "enemies": ["చంద్రుడు"]
    },
    "గురుడు": {
        "friends": ["సూర్యుడు", "చంద్రుడు", "కుజుడు"],
        "neutrals": ["శని"],
        "enemies": ["బుధుడు", "శుక్రుడు"]
    },
    "శుక్రుడు": {
        "friends": ["బుధుడు", "శని"],
        "neutrals": ["కుజుడు", "గురుడు"],
        "enemies": ["సూర్యుడు", "చంద్రుడు"]
    },
    "శని": {
        "friends": ["బుధుడు", "శుక్రుడు"],
        "neutrals": ["గురుడు"],
        "enemies": ["సూర్యుడు", "చంద్రుడు", "కుజుడు"]
    }
}

NAVATARA_NAMES = [
    "పరమ మిత్ర", "జన్మ", "సంపత్", "విపత్", "క్షేమ", "ప్రత్యక్", "సాధన", "నైధన", "మిత్ర"
]


def _get_nak_name(val):
    """Helper to extract normalized nakshatra name."""
    if isinstance(val, dict):
        val = val.get("nakshatra", "అశ్విని")
    name = str(val).strip()
    return NAKSHATRA_ALIASES.get(name, name)


def _get_rasi_name(val):
    """Helper to extract normalized rasi name."""
    if isinstance(val, dict):
        val = val.get("rashi", val.get("rasi", "మేషం"))
    name = str(val).strip()
    name = RASHI_ALIASES.get(name, name)
    for r in RASHIS:
        if r in name:
            return r
    return name


def calculate_dina(bride, groom):
    """
    1. Dina Porutham (దిన పొంతన).
    Count inclusive: Bride Star (1) to Groom Star.
    """
    b_name = _get_nak_name(bride)
    g_name = _get_nak_name(groom)

    b_idx = NAKSHATRA_DATA.get(b_name, {}).get("index", 1)
    g_idx = NAKSHATRA_DATA.get(g_name, {}).get("index", 1)

    count = ((g_idx - b_idx) % 27) + 1
    tara_name = NAVATARA_NAMES[count % 9]

    if count in DINA_GOOD:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        details = f"వధువు ({b_name}) నుండి వరుని ({g_name}) వరకు దూరం: {count}. '{tara_name} తార' - సంపూర్ణ ఆయురారోగ్యాలు, సంపదలకు శుభకరం."
    elif count in {12, 14, 16, 17, 21, 23, 27}:
        score = 0.5
        status = "మధ్యమం"
        icon = "⚠️"
        details = f"వధువు నుండి వరుని నక్షత్ర సంఖ్య: {count} ({tara_name} తార). మధ్యమ అనుకూలత కలదు."
    else:
        score = 0.0
        status = "బలహీనము"
        icon = "❌"
        details = f"వధువు నుండి వరుని నక్షత్ర సంఖ్య: {count} ({tara_name} తార). దిన పొంతన బలహీనంగా ఉన్నది."

    return {
        "id": "dina",
        "name_te": "దిన పొంతన",
        "name_en": "Dina Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "count": count,
        "tara": tara_name,
        "details": details,
        "bride_val": f"{b_name} (1)",
        "groom_val": f"{g_name} ({count})"
    }


def calculate_gana(bride, groom):
    """2. Gana Porutham (గణ పొంతన)."""
    b_name = _get_nak_name(bride)
    g_name = _get_nak_name(groom)

    b_gana = NAKSHATRA_DATA.get(b_name, {}).get("gana", "దేవ")
    g_gana = NAKSHATRA_DATA.get(g_name, {}).get("gana", "దేవ")

    info = GANA_MATRIX.get((b_gana, g_gana), {"score": 0.0, "status": "బలహీనము", "icon": "❌", "desc": "గణ విభేదం కలదు."})

    return {
        "id": "gana",
        "name_te": "గణ పొంతన",
        "name_en": "Gana Porutham",
        "score": info["score"],
        "max_score": 1.0,
        "status": info["status"],
        "icon": info["icon"],
        "details": f"వధువు: {b_gana} గణం, వరుడు: {g_gana} గణం. {info['desc']}",
        "bride_val": f"{b_gana} గణం",
        "groom_val": f"{g_gana} గణం"
    }


def calculate_mahendra(bride, groom):
    """3. Mahendra Porutham (మహేంద్ర పొంతన)."""
    b_name = _get_nak_name(bride)
    g_name = _get_nak_name(groom)

    b_idx = NAKSHATRA_DATA.get(b_name, {}).get("index", 1)
    g_idx = NAKSHATRA_DATA.get(g_name, {}).get("index", 1)

    count = ((g_idx - b_idx) % 27) + 1

    if count in MAHENDRA_GOOD:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        details = f"నక్షత్ర దూరం: {count}. మహేంద్ర పొంతన ఉన్నది. సంతాన ప్రాప్తి, సౌభాగ్య వృద్ధి, వంశాభివృద్ధికి అత్యంత శ్రేష్ఠం."
    else:
        score = 0.0
        status = "బలహీనము"
        icon = "❌"
        details = f"నక్షత్ర దూరం: {count}. సంప్రదాయ మహేంద్ర స్థానాలలో (4, 7, 10, 13, 16, 19, 22, 25) రానందున మహేంద్ర పొంతన లేదు."

    return {
        "id": "mahendra",
        "name_te": "మహేంద్ర పొంతన",
        "name_en": "Mahendra Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "count": count,
        "details": details,
        "bride_val": b_name,
        "groom_val": f"{g_name} ({count})"
    }


def calculate_stree_deergha(bride, groom):
    """4. Stree Deergha Porutham (స్త్రీ దీర్ఘ పొంతన)."""
    b_name = _get_nak_name(bride)
    g_name = _get_nak_name(groom)

    b_idx = NAKSHATRA_DATA.get(b_name, {}).get("index", 1)
    g_idx = NAKSHATRA_DATA.get(g_name, {}).get("index", 1)

    count = ((g_idx - b_idx) % 27) + 1

    if count > 13:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        details = f"నక్షత్ర దూరం: {count} (13 కంటే ఎక్కువ). వరుని నక్షత్రం దూరంగా ఉన్నందున దాంపత్య దీర్ఘాయువు, సుఖశాంతులు చేకూరును."
    elif count >= 8:
        score = 0.5
        status = "మధ్యమం"
        icon = "⚠️"
        details = f"నక్షత్ర దూరం: {count} (8 నుండి 13). మధ్యమ శ్రేణి స్త్రీ దీర్ఘ పొంతన ఉన్నది."
    else:
        score = 0.0
        status = "బలహీనము"
        icon = "❌"
        details = f"నక్షత్ర దూరం: {count} (7 లేదా తక్కువ). వరుని నక్షత్రం సమీపంలో ఉన్నందున స్త్రీ దీర్ఘం బలహీనంగా ఉన్నది."

    return {
        "id": "stree_deergha",
        "name_te": "స్త్రీ దీర్ఘ పొంతన",
        "name_en": "Stree Deergha Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "count": count,
        "details": details,
        "bride_val": b_name,
        "groom_val": f"{g_name} ({count})"
    }


def calculate_yoni(bride, groom):
    """5. Yoni Porutham (యోని పొంతన)."""
    b_name = _get_nak_name(bride)
    g_name = _get_nak_name(groom)

    b_yoni = NAKSHATRA_DATA.get(b_name, {}).get("yoni", "")
    g_yoni = NAKSHATRA_DATA.get(g_name, {}).get("yoni", "")

    if b_yoni == g_yoni:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        details = f"ఇద్దరిదీ సమాన యోని ({b_yoni}). శారీరక అనుకూలత, పరస్పర ఆకర్షణ పరిపూర్ణమైనది."
    elif (b_yoni, g_yoni) in YONI_ENEMIES:
        score = 0.0
        status = "బలహీనము"
        icon = "❌"
        details = f"వైర యోని జంట ({b_yoni} ↔ {g_yoni}). సంప్రదాయం ప్రకారం పరస్పర శత్రుత్వం వల్ల దాంపత్యంలో విభేదాలు రావచ్చు."
    else:
        score = 0.5
        status = "మధ్యమం"
        icon = "✅"
        details = f"వధువు: {b_yoni}, వరుడు: {g_yoni}. పరస్పర శత్రుత్వం లేని అనుకూల యోనులు."

    return {
        "id": "yoni",
        "name_te": "యోని పొంతన",
        "name_en": "Yoni Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "details": details,
        "bride_val": f"{b_yoni} యోని",
        "groom_val": f"{g_yoni} యోని"
    }


def classify_shadashtaka(b_rasi, g_rasi):
    """Classify 6/8 Shadashtaka relationship into Preethi, Sama, or Mrityu."""
    b_norm = _get_rasi_name(b_rasi)
    g_norm = _get_rasi_name(g_rasi)

    pair = tuple(sorted([b_norm, g_norm]))

    # 1. Preethi / Mitra Shadashtaka (Same Lord - Mars or Venus)
    if pair in {("మేషం", "వృశ్చికం"), ("తుల", "వృషభం")}:
        lord = "కుజుడు" if "మేషం" in pair else "శుక్రుడు"
        return {
            "type": "ప్రీతి షడాష్టకం",
            "score": 0.5,
            "severity": "శుభం / దోష భంగం",
            "icon": "🟢",
            "details": f"ఇద్దరి రాశ్యాధిపతి ఒకరే ({lord}). 'ప్రీతి షడాష్టకం' వల్ల దోష భంగం కలిగి అనుకూలత చేకూరింది."
        }
    # 2. Neutral Shadashtaka
    elif pair in {("మిథునం", "మకరం"), ("ధనుస్సు", "వృషభం"), ("కన్య", "కుంభం")}:
        return {
            "type": "సమ షడాష్టకం",
            "score": 0.25,
            "severity": "మధ్యమం",
            "icon": "🟡",
            "details": "రాశ్యాధిపతుల మధ్య శత్రుత్వం లేనందున సర్దుబాటుతో ఆమోదయోగ్యమైనది."
        }
    # 3. Mrityu / Arishta Shadashtaka (Enemy Lords: Sun-Saturn, Moon-Saturn)
    elif pair in {("మకరం", "సింహం"), ("కర్కాటకం", "కుంభం"), ("మీనం", "సింహం")}:
        return {
            "type": "మృత్యు / అరిష్ట షడాష్టకం",
            "score": 0.0,
            "severity": "తీవ్ర దోషం",
            "icon": "🔴",
            "details": "రాశ్యాధిపతుల మధ్య నైసర్గిక వైరం కలదు. తీవ్ర షడాష్టక దోషం - ప్రత్యేక శాంతి లేదా ప్రత్యక్ష పరిశీలన అవసరం."
        }
    else:
        return {
            "type": "సాధారణ షడాష్టకం",
            "score": 0.0,
            "severity": "జాగ్రత్త",
            "icon": "⚠️",
            "details": "6/8 రాశి సంబంధం - అభిప్రాయ భేదాలు రాకుండా పరస్పర అవగాహన అవసరం."
        }


def calculate_rasi(bride, groom):
    """6. Rasi Porutham (రాశి పొంతన)."""
    b_rasi = _get_rasi_name(bride)
    g_rasi = _get_rasi_name(groom)

    b_idx = RASHIS.index(b_rasi) if b_rasi in RASHIS else 0
    g_idx = RASHIS.index(g_rasi) if g_rasi in RASHIS else 0

    rel_pos = ((g_idx - b_idx) % 12) + 1
    shadashtaka_info = None

    if rel_pos == 1:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        rel_str = "1/1 (ఏక రాశి)"
        details = "ఇద్దరిదీ ఒకే రాశి. మానసిక ఏకత్వం, కుటుంబ అనుకూలత మంచిది."
    elif rel_pos == 7:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        rel_str = "7/7 (సమసప్తకం)"
        details = "పరస్పర సమసప్తక రాశులు. పరస్పర అనురాగం, దీర్ఘకాలిక దాంపత్య సుఖం లభించును."
    elif rel_pos in {3, 11}:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        rel_str = f"3/11 ({rel_pos}వ రాశి)"
        details = "3/11 రాశి సంబంధం. పరస్పర సహకారం, ధనలాభం, ఉన్నతి చేకూరును."
    elif rel_pos in {4, 10}:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        rel_str = f"4/10 ({rel_pos}వ రాశి)"
        details = "4/10 కేంద్ర సంబంధం. కుటుంబ సుఖం, పరస్పర గౌరవం ఉండును."
    elif rel_pos in {5, 9}:
        score = 0.5
        status = "మధ్యమం"
        icon = "⚠️"
        rel_str = "5/9 (త్రికోణ సంబంధం)"
        details = "5/9 త్రికోణ సంబంధం. శుభదాయకమైనది, సాధారణ అనుకూలత."
    elif rel_pos in {2, 12}:
        score = 0.0
        status = "బలహీనము"
        icon = "❌"
        rel_str = "2/12 (ద్విర్ద్వాదశ)"
        details = "2/12 ద్విర్ద్వాదశ సంబంధం. ధనవ్యయం లేదా పరస్పర అవగాహన లోపాలు రావచ్చు."
    elif rel_pos in {6, 8}:
        shadashtaka_info = classify_shadashtaka(b_rasi, g_rasi)
        score = shadashtaka_info["score"]
        status = shadashtaka_info["severity"]
        icon = shadashtaka_info["icon"]
        rel_str = f"6/8 ({shadashtaka_info['type']})"
        details = shadashtaka_info["details"]
    else:
        score = 0.5
        status = "మధ్యమం"
        icon = "⚠️"
        rel_str = f"{rel_pos}వ స్థానం"
        details = f"రాశి సంబంధం: {rel_pos}వ స్థానం."

    return {
        "id": "rasi",
        "name_te": "రాశి పొంతన",
        "name_en": "Rasi Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "relationship": rel_str,
        "shadashtaka_info": shadashtaka_info,
        "details": details,
        "bride_val": b_rasi,
        "groom_val": f"{g_rasi} ({rel_str})"
    }


def calculate_rasyadhipathi(bride, groom):
    """7. Rasyadhipathi Porutham / Graha Maitri (రాశ్యాధిపతి పొంతన)."""
    b_rasi = _get_rasi_name(bride)
    g_rasi = _get_rasi_name(groom)

    b_lord = RASHI_LORDS.get(b_rasi, "చంద్రుడు")
    g_lord = RASHI_LORDS.get(g_rasi, "చంద్రుడు")

    if b_lord == g_lord:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        details = f"ఇద్దరి రాశ్యాధిపతి ఒక్కరే ({b_lord}). పరిపూర్ణ గ్రహ మైత్రి, ఆలోచనలలో ఏకత్వం."
    else:
        b_rel = PLANET_FRIENDS.get(b_lord, {})
        g_rel = PLANET_FRIENDS.get(g_lord, {})

        b_to_g = "friend" if g_lord in b_rel.get("friends", []) else ("neutral" if g_lord in b_rel.get("neutrals", []) else "enemy")
        g_to_b = "friend" if b_lord in g_rel.get("friends", []) else ("neutral" if b_lord in g_rel.get("neutrals", []) else "enemy")

        if b_to_g == "friend" and g_to_b == "friend":
            score = 1.0
            status = "ఉత్తమం"
            icon = "✅"
            details = f"పరస్పర మిత్ర గ్రహాలు ({b_lord} ↔ {g_lord}). చక్కటి అవగాహన, ఆత్మీయత ఉండును."
        elif (b_to_g in {"friend", "neutral"}) and (g_to_b in {"friend", "neutral"}):
            score = 0.5
            status = "మధ్యమం"
            icon = "✅"
            details = f"మిత్ర-సమ గ్రహాలు ({b_lord} ↔ {g_lord}). సాధారణ అనుకూలత కలదు."
        else:
            score = 0.0
            status = "బలహీనము"
            icon = "❌"
            details = f"శత్రు గ్రహాలు ({b_lord} ↔ {g_lord}). ఆలోచనా విధానంలో తేడాలు రావచ్చు."

    return {
        "id": "rasyadhipathi",
        "name_te": "రాశ్యాధిపతి పొంతన",
        "name_en": "Rasyadhipathi Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "details": details,
        "bride_val": f"{b_rasi} ({b_lord})",
        "groom_val": f"{g_rasi} ({g_lord})"
    }


def calculate_vasya(bride, groom):
    """8. Vasya Porutham (వశ్య పొంతన)."""
    b_rasi = _get_rasi_name(bride)
    g_rasi = _get_rasi_name(groom)

    b_vasyas = VASYA_MATRIX.get(b_rasi, [])
    g_vasyas = VASYA_MATRIX.get(g_rasi, [])

    b_attracts_g = g_rasi in b_vasyas
    g_attracts_b = b_rasi in g_vasyas

    if b_attracts_g and g_attracts_b:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        details = "పరస్పర వశ్యం (Mutual Vasya). ఇద్దరి మధ్య అపారమైన అనురాగం, ఆకర్షణ ఉండును."
    elif b_attracts_g or g_attracts_b:
        score = 0.5
        status = "మధ్యమం"
        icon = "⚠️"
        side = "వధువు రాశికి వరుడు వశ్యం" if b_attracts_g else "వరుని రాశికి వధువు వశ్యం"
        details = f"ఏకపక్ష వశ్యం ({side}). ఆమోదయోగ్యమైన పొంతన."
    else:
        score = 0.0
        status = "సాధారణం"
        icon = "⚪"
        details = "ప్రత్యేక వశ్య సంబంధం లేదు (సాధారణ స్థితి)."

    return {
        "id": "vasya",
        "name_te": "వశ్య పొంతన",
        "name_en": "Vasya Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "details": details,
        "bride_val": b_rasi,
        "groom_val": g_rasi
    }


def calculate_rajju(bride, groom):
    """9. Rajju Porutham (రజ్జు పొంతన) — CRITICAL."""
    b_name = _get_nak_name(bride)
    g_name = _get_nak_name(groom)

    b_rajju = NAKSHATRA_DATA.get(b_name, {}).get("rajju", "పాద")
    g_rajju = NAKSHATRA_DATA.get(g_name, {}).get("rajju", "పాద")

    rajju_effects = {
        "శిరస్సు": "శిరో రజ్జు (శిరస్సు): భర్త క్షేమానికి దోషం",
        "కంఠ": "కంఠ రజ్జు (కంఠం): భార్య క్షేమానికి దోషం",
        "నాభి": "నాభి రజ్జు (నాభి): సంతాన సమస్యలు / ఆలస్యం",
        "కటి": "కటి రజ్జు (కటి/నడుము): దారిద్య్రం, ధన నష్టం",
        "పాద": "పాద రజ్జు (పాదాలు): దేశాంతర సంచారం, స్థిరత్వం లేకపోవడం"
    }

    if b_rajju == g_rajju:
        score = 0.0
        status = "తీవ్ర దోషం"
        icon = "❌"
        has_dosha = True
        eff = rajju_effects.get(b_rajju, "తీవ్ర దాంపత్య సమస్యలు")
        details = f"ఇద్దరిదీ ఒకే రజ్జు ({b_rajju} రజ్జు). సంప్రదాయ జ్యోతిష్య నియమాల ప్రకారం 'రజ్జు దోషం' ఉన్నది. ప్రభావం: {eff}."
    else:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        has_dosha = False
        details = f"భిన్న రజ్జులు (వధువు: {b_rajju}, వరుడు: {g_rajju}). రజ్జు దోషం లేదు, మాంగల్య సౌభాగ్యాలు శుభప్రదం."

    return {
        "id": "rajju",
        "name_te": "రజ్జు పొంతన",
        "name_en": "Rajju Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "has_dosha": has_dosha,
        "rajju_name": b_rajju if b_rajju == g_rajju else f"{b_rajju} / {g_rajju}",
        "details": details,
        "bride_val": f"{b_rajju} రజ్జు",
        "groom_val": f"{g_rajju} రజ్జు"
    }


def calculate_vedha(bride, groom):
    """10. Vedha Porutham (వేధ పొంతన) — CRITICAL."""
    b_name = _get_nak_name(bride)
    g_name = _get_nak_name(groom)

    is_vedha = (b_name, g_name) in VEDHA_PAIRS

    if is_vedha:
        score = 0.0
        status = "తీవ్ర దోషం"
        icon = "❌"
        has_dosha = True
        details = f"పరస్పర వేధ నక్షత్రాలు ({b_name} ↔ {g_name}). సంప్రదాయ జ్యోతిష్యం ప్రకారం 'వేధ దోషం' ఉన్నది. దాంపత్యంలో అనుకోని ఒడిదుడుకులు రావచ్చు."
    else:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        has_dosha = False
        details = f"వేధ దోషం లేదు ({b_name} & {g_name}). నక్షత్రాలు ఒకదానితో ఒకటి బాధకము కావు. శుభప్రదం."

    return {
        "id": "vedha",
        "name_te": "వేధ పొంతన",
        "name_en": "Vedha Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "has_dosha": has_dosha,
        "details": details,
        "bride_val": b_name,
        "groom_val": g_name
    }


def calculate_vriksha(bride, groom):
    """11. Vriksha Porutham (వృక్ష పొంతన - ద్వాదశ కూటం)."""
    b_name = _get_nak_name(bride)
    g_name = _get_nak_name(groom)

    b_tree_info = VRIKSHA_DATA.get(b_name, {"tree": "వృక్షం", "is_milky": False})
    g_tree_info = VRIKSHA_DATA.get(g_name, {"tree": "వృక్షం", "is_milky": False})

    b_milky = b_tree_info["is_milky"]
    g_milky = g_tree_info["is_milky"]

    if b_milky and g_milky:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        details = f"ఇద్దరి నక్షత్రాలూ క్షీర వృక్షాలు (పాల చెట్లు: {b_tree_info['tree']} & {g_tree_info['tree']}). సంతాన సమృద్ధి, కుటుంబ సుఖం కలుగును."
    elif b_milky or g_milky:
        score = 0.5
        status = "మధ్యమం"
        icon = "✅"
        details = f"ఒకరు క్షీర వృక్షం ({b_tree_info['tree'] if b_milky else g_tree_info['tree']}). ఆమోదయోగ్యమైన పొంతన."
    else:
        score = 0.5
        status = "సాధారణం"
        icon = "⚪"
        details = f"వధువు వృక్షం: {b_tree_info['tree']}, వరుని వృక్షం: {g_tree_info['tree']}. సాధారణ పొంతన."

    return {
        "id": "vriksha",
        "name_te": "వృక్ష పొంతన",
        "name_en": "Vriksha Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "details": details,
        "bride_val": f"{b_tree_info['tree']} ({'పాల చెట్టు' if b_milky else 'సాధారణ'})",
        "groom_val": f"{g_tree_info['tree']} ({'పాల చెట్టు' if g_milky else 'సాధారణ'})"
    }


def calculate_bhoota(bride, groom):
    """12. Bhoota Porutham (పంచభూత పొంతన - ద్వాదశ కూటం)."""
    b_name = _get_nak_name(bride)
    g_name = _get_nak_name(groom)

    b_bhoota = BHOOTA_MAP.get(b_name, "భూమి")
    g_bhoota = BHOOTA_MAP.get(g_name, "భూమి")

    if b_bhoota == g_bhoota:
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        details = f"ఇద్దరిదీ సమాన పంచభూత తత్వం ({b_bhoota} తత్వం). పరిపూర్ణ మానసిక సామరస్యం."
    elif (b_bhoota in {"భూమి", "జలం"} and g_bhoota in {"భూమి", "జలం"}):
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        details = f"భూమి మరియు జల తత్వాల మైత్రి ({b_bhoota} + {g_bhoota}). సస్యశ్యామల వృద్ధి, కుటుంబ సుఖం."
    elif (b_bhoota in {"అగ్ని", "వాయువు"} and g_bhoota in {"అగ్ని", "వాయువు"}):
        score = 1.0
        status = "ఉత్తమం"
        icon = "✅"
        details = f"అగ్ని మరియు వాయు తత్వాల మైత్రి ({b_bhoota} + {g_bhoota}). పరస్పర ప్రోత్సాహం, ఉన్నతి."
    elif b_bhoota == "ఆకాశం" or g_bhoota == "ఆకాశం":
        score = 0.5
        status = "మధ్యమం"
        icon = "✅"
        details = f"ఆకాశ తత్వ సమన్వయం ({b_bhoota} & {g_bhoota}). శాంతియుతమైన సంబంధం."
    elif (b_bhoota == "అగ్ని" and g_bhoota == "జలం") or (b_bhoota == "జలం" and g_bhoota == "అగ్ని"):
        score = 0.0
        status = "బలహీనము"
        icon = "❌"
        details = f"అగ్ని ↔ జల పరస్పర శత్రు తత్వాలు. సహజ భావోద్వేగ వ్యత్యాసాలు రావచ్చు."
    else:
        score = 0.5
        status = "మధ్యమం"
        icon = "⚠️"
        details = f"వధువు {b_bhoota} తత్వం, వరుడు {g_bhoota} తత్వం. మధ్యమ అనుకూలత."

    return {
        "id": "bhoota",
        "name_te": "పంచభూత పొంతన",
        "name_en": "Bhoota Porutham",
        "score": score,
        "max_score": 1.0,
        "status": status,
        "icon": icon,
        "details": details,
        "bride_val": f"{b_bhoota} తత్వం",
        "groom_val": f"{g_bhoota} తత్వం"
    }


def calculate_nadi(bride, groom, bride_padam=1, groom_padam=1, bride_rasi="", groom_rasi=""):
    """Nadi Analysis (నాడి పరిశీలన)."""
    b_name = _get_nak_name(bride)
    g_name = _get_nak_name(groom)

    if isinstance(bride, dict):
        bride_padam = bride.get("pada", bride.get("padam", bride_padam))
        bride_rasi = bride.get("rashi", bride.get("rasi", bride_rasi))
    if isinstance(groom, dict):
        groom_padam = groom.get("pada", groom.get("padam", groom_padam))
        groom_rasi = groom.get("rashi", groom.get("rasi", groom_rasi))

    b_nadi = NAKSHATRA_DATA.get(b_name, {}).get("nadi", "ఆది")
    g_nadi = NAKSHATRA_DATA.get(g_name, {}).get("nadi", "ఆది")

    if b_nadi != g_nadi:
        return {
            "has_dosha": False,
            "bhanga": False,
            "status": "దోషం లేదు (ఉత్తమం)",
            "icon": "🟢",
            "bride_nadi": b_nadi,
            "groom_nadi": g_nadi,
            "details": f"భిన్న నాడీ వర్గాలు (వధువు: {b_nadi}, వరుడు: {g_nadi}). నాడి దోషం లేదు. శరీర ధర్మం, సంతాన అనుకూలత శుభప్రదం."
        }

    # Same Nadi -> Check Cancellations (దోష భంగం)
    bhanga_reasons = []
    if b_name == g_name and bride_padam != groom_padam:
        bhanga_reasons.append("ఏక నక్షత్రమైనప్పటికీ విభిన్న పాదాలు")

    b_norm = _get_rasi_name(bride_rasi)
    g_norm = _get_rasi_name(groom_rasi)
    if b_norm == g_norm and b_name != g_name:
        bhanga_reasons.append("ఏక రాశి అయినప్పటికీ విభిన్న నక్షత్రాలు")

    b_lord = RASHI_LORDS.get(b_norm, "")
    g_lord = RASHI_LORDS.get(g_norm, "")
    if b_lord and b_lord == g_lord:
        bhanga_reasons.append(f"రాశ్యాధిపతి మైత్రి ({b_lord})")

    if bhanga_reasons:
        return {
            "has_dosha": True,
            "bhanga": True,
            "status": "దోష భంగం కలదు (మధ్యమం)",
            "icon": "🟡",
            "bride_nadi": b_nadi,
            "groom_nadi": g_nadi,
            "bhanga_reasons": bhanga_reasons,
            "details": f"ఇద్దరిదీ ఒకే నాడి ({b_nadi}). అయితే {', '.join(bhanga_reasons)} వల్ల నాడి దోష భంగం కలిగి అనుకూలత చేకూరింది."
        }
    else:
        return {
            "has_dosha": True,
            "bhanga": False,
            "status": "నాడి దోషం కలదు",
            "icon": "🔴",
            "bride_nadi": b_nadi,
            "groom_nadi": g_nadi,
            "details": f"ఇద్దరిదీ సమాన నాడి ({b_nadi} నాడి). సంప్రదాయం ప్రకారం నాడి దోష సూచన ఉన్నది. వైద్య / జాతక పరిశీలన మంచిది."
        }


def check_special_nakshatra_doshas(bride_data, groom_data):
    """Special Nakshatra Doshas (జ్యేష్ఠ, మూల, ఆశ్లేష, విశాఖ)."""
    b_nak = _get_nak_name(bride_data.get("nakshatra", ""))
    g_nak = _get_nak_name(groom_data.get("nakshatra", ""))
    b_pada = bride_data.get("padam", bride_data.get("pada", 1))
    g_pada = groom_data.get("padam", groom_data.get("pada", 1))

    doshas = []

    # 1. Jyeshtha Dosha
    if b_nak == "జ్యేష్ఠ":
        doshas.append({
            "name": "జ్యేష్ఠా కన్యక (Jyeshtha Kanya)",
            "severity": "మధ్యమం / శాంతి అవసరం",
            "icon": "⚠️",
            "details": "వధువు జ్యేష్ఠా నక్షత్రం. వరుడు కుటుంబంలో పెద్ద కుమారుడు (జ్యేష్ఠ పుత్రుడు) అయినచో వివాహానికి ముందు జ్యేష్ఠా శాంతి లేదా హోమం చేయించడం సంప్రదాయం."
        })
    if g_nak == "జ్యేష్ఠ" and b_nak == "జ్యేష్ఠ":
        doshas.append({
            "name": "ఉభయ జ్యేష్ఠా నక్షత్రం",
            "severity": "తీవ్రం",
            "icon": "🔴",
            "details": "ఇద్దరిదీ జ్యేష్ఠా నక్షత్రం. సంప్రదాయం ప్రకారం ప్రత్యేక నక్షత్ర శాంతి చేయించాలి."
        })

    # 2. Moola Dosha
    if b_nak == "మూల":
        pada_msgs = {
            1: "మూల 1వ పాదం: మామగారికి గండ సూచన (మూలా శాంతి హోమం అవసరం).",
            2: "మూల 2వ పాదం: అత్తగారికి గండ సూచన (మూలా శాంతి పూజ అవసరం).",
            3: "మూల 3వ పాదం: ధన వ్యయ సూచన (సాధారణ పరిహారం).",
            4: "మూల 4వ పాదం: దోషం లేదు, అత్యంత శుభప్రదం."
        }
        doshas.append({
            "name": f"వధువు మూలా నక్షత్రం ({b_pada}వ పాదం)",
            "severity": "తీవ్రం" if b_pada in {1, 2} else "సాధారణం",
            "icon": "🔴" if b_pada in {1, 2} else "🟢",
            "details": pada_msgs.get(b_pada, "మూలా శాంతి పరిశీలన అవసరం.")
        })

    # 3. Aslesha Dosha
    if b_nak == "ఆశ్లేష":
        aslesha_msgs = {
            1: "ఆశ్లేష 1వ పాదం: శుభప్రదం (దోషం లేదు).",
            2: "ఆశ్లేష 2వ పాదం: ధనహాని సూచన.",
            3: "ఆశ్లేష 3వ పాదం: అత్తగారికి గండ సూచన (ఆశ్లేషా బలి / నాగపూజ అవసరం).",
            4: "ఆశ్లేష 4వ పాదం: మామగారికి గండ సూచన (శాంతి పూజ అవసరం)."
        }
        doshas.append({
            "name": f"వధువు ఆశ్లేషా నక్షత్రం ({b_pada}వ పాదం)",
            "severity": "తీవ్రం" if b_pada in {3, 4} else "సాధారణం",
            "icon": "🔴" if b_pada in {3, 4} else "🟢",
            "details": aslesha_msgs.get(b_pada, "ఆశ్లేషా శాంతి పూజ అవసరం.")
        })

    # 4. Visakha Dosha
    if b_nak == "విశాఖ" and b_pada == 4:
        doshas.append({
            "name": "విశాఖా 4వ పాదం (మరిది దోషం)",
            "severity": "మధ్యమం",
            "icon": "⚠️",
            "details": "వధువు విశాఖ 4వ పాదం. వరునికి తమ్ముడు (మరిది) ఉన్నచో విశాఖా శాంతి పూజ చేయించడం శ్రేయస్కరం."
        })

    return {
        "has_special_doshas": any(d["icon"] in {"🔴", "⚠️"} for d in doshas),
        "doshas_list": doshas
    }


def calculate_lagna_compatibility(bride_data, groom_data):
    """Lagna-to-Lagna Compatibility (లగ్న మైత్రి)."""
    b_lagna = _get_rasi_name(bride_data.get("lagna", ""))
    g_lagna = _get_rasi_name(groom_data.get("lagna", ""))

    b_idx = RASHIS.index(b_lagna) if b_lagna in RASHIS else 0
    g_idx = RASHIS.index(g_lagna) if g_lagna in RASHIS else 0

    rel_pos = ((g_idx - b_idx) % 12) + 1

    if rel_pos == 7:
        score = 1.0
        status = "సమసప్తక లగ్నాలు (అత్యుత్తమం)"
        icon = "🟢"
        details = f"వధువు లగ్నం {b_lagna}, వరుని లగ్నం {g_lagna} (7/7 సమసప్తకం). జీవిత భాగస్వామ్యంలో పరస్పర ఆకర్షణ, పరిపూర్ణ సమన్వయం కలదు."
    elif rel_pos in {5, 9}:
        score = 1.0
        status = "త్రికోణ లగ్నాలు (చాలా మంచిది)"
        icon = "🟢"
        details = f"త్రికోణ లగ్న సంబంధం ({rel_pos}వ స్థానం). ధర్మం, సంస్కారాలు మరియు జీవన లక్ష్యాలలో సహజ ఐక్యత ఉండును."
    elif rel_pos == 1:
        score = 1.0
        status = "ఏక లగ్నం (మంచిది)"
        icon = "🟢"
        details = f"ఇద్దరిదీ ఒకే లగ్నం ({b_lagna}). ప్రాపంచిక దృక్పథం, వ్యక్తిత్వ శైలి సమానంగా ఉండును."
    elif rel_pos in {3, 11, 4, 10}:
        score = 0.8
        status = "కేంద్ర-లాభ లగ్నాలు (అనుకూలం)"
        icon = "🟢"
        details = f"కేంద్ర-లాభ లగ్న సంబంధం ({rel_pos}వ స్థానం). సాంఘిక గౌరవం, పరస్పర పురోగతి లభించును."
    elif rel_pos in {2, 12}:
        score = 0.5
        status = "ద్విర్ద్వాదశ లగ్నాలు (సాధారణం)"
        icon = "🟡"
        details = "ద్విర్ద్వాదశ లగ్నాలు (2/12). వ్యక్తిగత అభిప్రాయాలు, ఖర్చుల విషయంలో భిన్న దృక్పథాలు ఉండవచ్చు."
    elif rel_pos in {6, 8}:
        score = 0.2
        status = "షడాష్టక లగ్నాలు (జాగ్రత్త)"
        icon = "🔴"
        details = "లగ్నాలు 6/8 షడాష్టక స్థితిలో ఉన్నవి. నిత్య జీవితంలో అలవాట్లు, పనితీరులో సర్దుబాటు అవసరం."
    else:
        score = 0.5
        status = "సాధారణ లగ్న సంబంధం"
        icon = "🟡"
        details = f"లగ్న సంబంధం: {rel_pos}వ స్థానం."

    return {
        "score": score,
        "status": status,
        "icon": icon,
        "relationship": f"{rel_pos}వ స్థానం",
        "bride_lagna": b_lagna,
        "groom_lagna": g_lagna,
        "details": details
    }


def analyze_8th_and_2nd_houses(bride_data, groom_data):
    """8th House Mangalya & 2nd House Kutumba Analysis."""
    b_lagna = _get_rasi_name(bride_data.get("lagna", ""))
    b_lagna_idx = RASHIS.index(b_lagna) if b_lagna in RASHIS else 0
    b_h8_rasi = RASHIS[(b_lagna_idx + 7) % 12]
    b_h8_lord = RASHI_LORDS.get(b_h8_rasi, "")

    b_planets = [p for p in bride_data.get("planet_positions", []) if not p.get("is_hand")]
    b_h8_occupants = [p.get("name") for p in b_planets if _get_rasi_name(p.get("lagna")) == b_h8_rasi]

    has_benefic_8th = any(p in {"గురుడు", "శుక్రుడు", "బుధుడు", "చంద్రుడు"} for p in b_h8_occupants)
    has_malefic_8th = any(p in {"శని", "కుజుడు", "రాహు", "కేతు"} for p in b_h8_occupants)

    if has_benefic_8th:
        b_mangalya_status = "దీర్ఘ సుమంగళీ యోగం (శుభం)"
        b_mangalya_icon = "🟢"
        b_mangalya_details = f"అష్టమ స్థానంలో ({b_h8_rasi}) శుభగ్రహాల ప్రభావం ఉన్నది. మాంగల్య బలం మరియు దాంపత్య సౌభాగ్యం శుభప్రదం."
    elif has_malefic_8th:
        b_mangalya_status = "మాంగల్య స్థానంలో గ్రహ ప్రభావం (శాంతి సూచన)"
        b_mangalya_icon = "🟡"
        b_mangalya_details = f"అష్టమ స్థానంలో ({b_h8_rasi}) పాపగ్రహాల స్థితి కలదు. మంగళ గౌరీ పూజ లేదా శాంతి సూచించడమైనది."
    else:
        b_mangalya_status = "సాధారణ మాంగల్య బలం (శుభం)"
        b_mangalya_icon = "🟢"
        b_mangalya_details = f"అష్టమ భావం ({b_h8_rasi}) నిర్మలంగా ఉన్నది (అధిపతి: {b_h8_lord})."

    # 2nd House = Kutumba Sthanam
    b_h2_rasi = RASHIS[(b_lagna_idx + 1) % 12]
    g_lagna = _get_rasi_name(groom_data.get("lagna", ""))
    g_lagna_idx = RASHIS.index(g_lagna) if g_lagna in RASHIS else 0
    g_h2_rasi = RASHIS[(g_lagna_idx + 1) % 12]

    return {
        "bride_mangalya": {
            "h8_rasi": b_h8_rasi,
            "h8_lord": b_h8_lord,
            "occupants": b_h8_occupants if b_h8_occupants else ["గ్రహాలు లేవు (నిర్మలం)"],
            "status": b_mangalya_status,
            "icon": b_mangalya_icon,
            "details": b_mangalya_details
        },
        "kutumba_bhavas": {
            "bride_h2": b_h2_rasi,
            "groom_h2": g_h2_rasi,
            "status": "కుటుంబ స్థానాల సమతుల్యత",
            "details": f"వధువు 2వ భావం: {b_h2_rasi}, వరుని 2వ భావం: {g_h2_rasi}. కుటుంబ జీవన సామరస్యం."
        }
    }


def analyze_rahu_ketu_axis(bride_data, groom_data):
    """1/7 Axis Rahu-Ketu and Sarpa Dosha Balance."""
    def get_rk_houses(data):
        lagna = _get_rasi_name(data.get("lagna", ""))
        l_idx = RASHIS.index(lagna) if lagna in RASHIS else 0
        planets = [p for p in data.get("planet_positions", []) if not p.get("is_hand")]

        rahu_h = None
        ketu_h = None
        for p in planets:
            pname = p.get("name")
            p_rasi = _get_rasi_name(p.get("lagna"))
            p_idx = RASHIS.index(p_rasi) if p_rasi in RASHIS else 0
            h_num = ((p_idx - l_idx) % 12) + 1
            if pname == "రాహు":
                rahu_h = h_num
            elif pname == "కేతు":
                ketu_h = h_num
        return rahu_h, ketu_h

    b_rahu, b_ketu = get_rk_houses(bride_data)
    g_rahu, g_ketu = get_rk_houses(groom_data)

    b_has_1_7 = (b_rahu in {1, 7} or b_ketu in {1, 7})
    g_has_1_7 = (g_rahu in {1, 7} or g_ketu in {1, 7})

    if b_has_1_7 and g_has_1_7:
        status = "సర్పదోష సామ్యం (శుభం)"
        icon = "🟢"
        details = "ఇద్దరి జాతకాలలోనూ 1/7 స్థానాలలో రాహు-కేతువులు ఉన్నందున 'సర్పదోష సామ్యం' కలిగి దోష పరిహారమైంది."
        is_balanced = True
    elif b_has_1_7 or g_has_1_7:
        side = "వధువు" if b_has_1_7 else "వరుని"
        status = "సప్తమ రాహు/కేతు ప్రభావం (పరిశీలన)"
        icon = "🟡"
        details = f"{side} జాతకంలో 1/7 అక్షంలో రాహు-కేతు ప్రభావం ఉన్నది. శ్రీ కాళహస్తి క్షేత్రంలో పూజ లేదా శాంతి సూచించడమైనది."
        is_balanced = False
    else:
        status = "దోషం లేదు (శుభం)"
        icon = "🟢"
        details = "ఇద్దరి జాతకాలలోనూ 1/7 అక్షంలో రాహు-కేతు దోషం లేదు. వైవాహిక బంధం సుస్థిరం."
        is_balanced = True

    return {
        "status": status,
        "icon": icon,
        "is_balanced": is_balanced,
        "bride_rahu_h": b_rahu,
        "groom_rahu_h": g_rahu,
        "details": details
    }


def calculate_kuja_dosha(chart_data):
    """
    Kuja Dosha (మాంగలిక / కుజ దోషం) from Lagna, Moon, and Venus.
    """
    if not isinstance(chart_data, dict):
        return {"has_dosha": False, "intensity": "లేదు", "from_lagna": False, "from_moon": False, "from_venus": False, "bhanga": False}

    planet_positions = chart_data.get("planet_positions", [])

    mars_rasi = None
    moon_rasi = None
    venus_rasi = None
    jupiter_rasi = None

    for p in planet_positions:
        if p.get("is_hand"):
            continue
        pname = p.get("name", "")
        if pname == "కుజుడు":
            mars_rasi = p.get("lagna", "")
        elif pname == "చంద్రుడు":
            moon_rasi = p.get("lagna", "")
        elif pname == "శుక్రుడు":
            venus_rasi = p.get("lagna", "")
        elif pname == "గురుడు":
            jupiter_rasi = p.get("lagna", "")

    lagna_rasi = chart_data.get("lagna", "")

    if not mars_rasi:
        return {"has_dosha": False, "intensity": "లేదు", "from_lagna": False, "from_moon": False, "from_venus": False, "bhanga": False}

    mars_norm = _get_rasi_name(mars_rasi)
    lagna_norm = _get_rasi_name(lagna_rasi)
    moon_norm = _get_rasi_name(moon_rasi) if moon_rasi else lagna_norm
    venus_norm = _get_rasi_name(venus_rasi) if venus_rasi else lagna_norm

    mars_idx = RASHIS.index(mars_norm) if mars_norm in RASHIS else 0
    lagna_idx = RASHIS.index(lagna_norm) if lagna_norm in RASHIS else 0
    moon_idx = RASHIS.index(moon_norm) if moon_norm in RASHIS else lagna_idx
    venus_idx = RASHIS.index(venus_norm) if venus_norm in RASHIS else lagna_idx
    jupiter_idx = RASHIS.index(_get_rasi_name(jupiter_rasi)) if jupiter_rasi and _get_rasi_name(jupiter_rasi) in RASHIS else None

    h_from_lagna = ((mars_idx - lagna_idx) % 12) + 1
    h_from_moon = ((mars_idx - moon_idx) % 12) + 1
    h_from_venus = ((mars_idx - venus_idx) % 12) + 1

    dosha_houses = {1, 2, 4, 7, 8, 12}
    from_lagna = h_from_lagna in dosha_houses
    from_moon = h_from_moon in dosha_houses
    from_venus = h_from_venus in dosha_houses

    has_dosha = from_lagna or from_moon or from_venus

    bhanga = False
    bhanga_reasons = []

    # Own/Exaltation
    if mars_norm in {"మేషం", "వృశ్చికం"}:
        bhanga = True
        bhanga_reasons.append(f"కుజుడు స్వక్షేత్రంలో ఉన్నాడు ({mars_norm})")
    elif mars_norm == "మకరం":
        bhanga = True
        bhanga_reasons.append("కుజుడు ఉచ్ఛ స్థితిలో ఉన్నాడు (మకరం)")

    # Jupiter conjunction or drishti
    if jupiter_idx is not None:
        if jupiter_idx == mars_idx:
            bhanga = True
            bhanga_reasons.append("గురు-కుజ సంయోగం")
        else:
            jup_dist = ((mars_idx - jupiter_idx) % 12) + 1
            if jup_dist in {5, 7, 9}:
                bhanga = True
                bhanga_reasons.append(f"గురు దృష్టి కుజునిపై ఉన్నది ({jup_dist}వ దృష్టి)")

    # Traditional house cancellations
    if h_from_lagna == 2 and mars_norm in {"మిథునం", "కన్య"}:
        bhanga = True
        bhanga_reasons.append("ద్వితీయ కుజుడు బుధ క్షేత్రంలో ఉన్నాడు")
    elif h_from_lagna == 4 and mars_norm in {"మేషం", "వృశ్చికం"}:
        bhanga = True
        bhanga_reasons.append("చతుర్థ కుజుడు స్వక్షేత్రంలో ఉన్నాడు")
    elif h_from_lagna == 7 and mars_norm in {"కర్కాటకం", "మకరం"}:
        bhanga = True
        bhanga_reasons.append("సప్తమ కుజుడు నీచ/ఉచ్ఛ స్థానంలో ఉన్నాడు")
    elif h_from_lagna == 8 and mars_norm in {"ధనుస్సు", "మీనం"}:
        bhanga = True
        bhanga_reasons.append("అష్టమ కుజుడు గురు క్షేత్రంలో ఉన్నాడు")
    elif h_from_lagna == 12 and mars_norm in {"వృషభం", "తుల"}:
        bhanga = True
        bhanga_reasons.append("ద్వాదశ కుజుడు శుక్ర క్షేత్రంలో ఉన్నాడు")

    intensity = "లేదు"
    if has_dosha:
        count_sources = sum([from_lagna, from_moon, from_venus])
        if bhanga:
            intensity = "దోష భంగం (నామమాత్రం)"
        elif count_sources >= 2 and (h_from_lagna in {7, 8} or h_from_moon in {7, 8}):
            intensity = "తీవ్ర స్థాయి"
        elif count_sources >= 2:
            intensity = "మధ్యమ స్థాయి"
        else:
            intensity = "సాధారణ స్థాయి"

    return {
        "has_dosha": has_dosha,
        "intensity": intensity,
        "from_lagna": from_lagna,
        "house_from_lagna": h_from_lagna,
        "from_moon": from_moon,
        "house_from_moon": h_from_moon,
        "from_venus": from_venus,
        "house_from_venus": h_from_venus,
        "bhanga": bhanga,
        "bhanga_reasons": bhanga_reasons,
        "mars_rasi": mars_norm
    }


def compare_kuja_samyam(b_kuja, g_kuja):
    """Compare Kuja Dosha between Bride and Groom for Kuja Samyam (కుజదోష సామ్యం)."""
    b_has = b_kuja["has_dosha"] and not b_kuja["bhanga"]
    g_has = g_kuja["has_dosha"] and not g_kuja["bhanga"]

    if not b_has and not g_has:
        return {
            "status": "దోషం లేదు (ఉత్తమం)",
            "icon": "🟢",
            "is_balanced": True,
            "details": "ఇద్దరి జాతకాలలోనూ కుజ దోషం లేదు. అత్యంత శుభప్రదం."
        }
    elif b_has and g_has:
        return {
            "status": "కుజదోష సామ్యం (శుభం)",
            "icon": "🟢",
            "is_balanced": True,
            "details": "ఇద్దరి జాతకాలలోనూ సమాన స్థాయిలో కుజ ప్రభావం కలదు. 'కుజదోష సామ్యం' వల్ల దోషం పరిహారమై వివాహానికి శుభప్రదమైనది."
        }
    elif b_kuja["bhanga"] or g_kuja["bhanga"]:
        side = "వధువుకు" if b_kuja["bhanga"] else "వరునికి"
        return {
            "status": "కుజదోష భంగం (మధ్యమం)",
            "icon": "🟡",
            "is_balanced": True,
            "details": f"{side} కుజదోష భంగం ఉన్నందున ఆమోదయోగ్యమైనది."
        }
    else:
        side_with_dosha = "వధువుకు" if b_has else "వరునికి"
        side_without = "వరునికి" if b_has else "వధువుకు"
        return {
            "status": "కుజదోష అసమతుల్యత (జాగ్రత్త)",
            "icon": "🔴",
            "is_balanced": False,
            "details": f"{side_with_dosha} కుజ ప్రభావం ఉన్నది, {side_without} లేదు. పెద్దల / జ్యోతిష్యుల పరిశీలన అవసరం."
        }


def analyze_7th_and_d9(p1_data, p2_data, groom_is_p1=True):
    """Analyze 7th house, 7th lord, Venus, Jupiter, and Navamsa (D9)."""
    groom_data = p1_data if groom_is_p1 else p2_data
    bride_data = p2_data if groom_is_p1 else p1_data

    def get_details(data, role_name):
        lagna = data.get("lagna", "")
        lagna_norm = _get_rasi_name(lagna)
        lagna_idx = RASHIS.index(lagna_norm) if lagna_norm in RASHIS else 0
        h7_idx = (lagna_idx + 6) % 12
        h7_rasi = RASHIS[h7_idx]
        h7_lord = RASHI_LORDS.get(h7_rasi, "")

        planets = data.get("planet_positions", [])
        direct_planets = [p for p in planets if not p.get("is_hand")]

        h7_occupants = [p.get("name") for p in direct_planets if _get_rasi_name(p.get("lagna")) == h7_rasi]

        lord_pos = None
        venus_pos = None
        jupiter_pos = None

        for p in direct_planets:
            pname = p.get("name")
            if pname == h7_lord:
                lord_pos = _get_rasi_name(p.get("lagna"))
            if pname == "శుక్రుడు":
                venus_pos = _get_rasi_name(p.get("lagna"))
            elif pname == "గురుడు":
                jupiter_pos = _get_rasi_name(p.get("lagna"))

        moon_lon = data.get("moon_lon", 0.0)
        d9_moon_idx = int(moon_lon / (360.0 / 108.0)) % 12
        d9_moon_rasi = RASHIS[d9_moon_idx]

        return {
            "role": role_name,
            "lagna": lagna_norm,
            "h7_rasi": h7_rasi,
            "h7_lord": h7_lord,
            "h7_occupants": h7_occupants if h7_occupants else ["గ్రహాలు లేవు (శుభం)"],
            "lord_pos": lord_pos or "విశ్లేషించబడింది",
            "venus_pos": venus_pos or "—",
            "jupiter_pos": jupiter_pos or "—",
            "d9_moon_rasi": d9_moon_rasi
        }

    groom_7th = get_details(groom_data, "వరుడు (Groom)")
    bride_7th = get_details(bride_data, "వధువు (Bride)")

    d9_g_idx = RASHIS.index(groom_7th["d9_moon_rasi"]) if groom_7th["d9_moon_rasi"] in RASHIS else 0
    d9_b_idx = RASHIS.index(bride_7th["d9_moon_rasi"]) if bride_7th["d9_moon_rasi"] in RASHIS else 0
    d9_rel = ((d9_g_idx - d9_b_idx) % 12) + 1

    if d9_rel in {1, 3, 5, 7, 9, 11}:
        d9_status = "ఉత్తమ నవాంశ మైత్రి"
        d9_icon = "🟢"
        d9_details = f"D9 చంద్ర స్థానాలు ({bride_7th['d9_moon_rasi']} ↔ {groom_7th['d9_moon_rasi']}) శుభ స్థానాలలో (సమసప్తక/త్రికోణ) ఉన్నవి."
    else:
        d9_status = "సాధారణ నవాంశ మైత్రి"
        d9_icon = "🟡"
        d9_details = f"D9 చంద్ర స్థానాలు: వధువు {bride_7th['d9_moon_rasi']}, వరుడు {groom_7th['d9_moon_rasi']}."

    return {
        "groom_7th": groom_7th,
        "bride_7th": bride_7th,
        "d9_status": d9_status,
        "d9_icon": d9_icon,
        "d9_details": d9_details
    }


def analyze_dasha_compatibility(p1_data, p2_data, groom_is_p1=True):
    """Evaluate running Mahadasha & Antardasha compatibility."""
    groom_data = p1_data if groom_is_p1 else p2_data
    bride_data = p2_data if groom_is_p1 else p1_data

    g_maha = groom_data.get("maha", "—")
    g_anthara = groom_data.get("current_anthara", "—")
    b_maha = bride_data.get("maha", "—")
    b_anthara = bride_data.get("current_anthara", "—")

    if g_maha in PLANET_FRIENDS and b_maha in PLANET_FRIENDS:
        g_friends = PLANET_FRIENDS[g_maha].get("friends", [])
        g_enemies = PLANET_FRIENDS[g_maha].get("enemies", [])
        if b_maha == g_maha or b_maha in g_friends:
            status = "శుభ దశా సమయం"
            icon = "🟢"
            details = f"వరుని దశ ({g_maha}) మరియు వధువు దశ ({b_maha}) పరస్పర మిత్రత్వంలో ఉన్నవి. వివాహ సమయానికి అత్యంత అనుకూలం."
        elif b_maha in g_enemies:
            status = "సాధారణం / జాగ్రత్త"
            icon = "🟡"
            details = f"ప్రస్తుతం వరునికి {g_maha} దశ, వధువుకు {b_maha} దశ నడుస్తున్నాయి. శత్రు గ్రహ దశలు అయినందున సమయపాలన ముఖ్యం."
        else:
            status = "మధ్యమ దశా సమయం"
            icon = "🟡"
            details = f"ప్రస్తుతం వరునికి {g_maha} దశ, వధువుకు {b_maha} దశ నడుస్తున్నాయి. ఆమోదయోగ్యమైన కాలం."
    else:
        status = "దశా వివరాలు లభ్యమయ్యాయి"
        icon = "🟢"
        details = f"వరుని ప్రస్తుత దశ: {g_maha} - {g_anthara}, వధువు ప్రస్తుత దశ: {b_maha} - {b_anthara}."

    return {
        "groom_maha": g_maha,
        "groom_anthara": g_anthara,
        "bride_maha": b_maha,
        "bride_anthara": b_anthara,
        "status": status,
        "icon": icon,
        "details": details
    }


def generate_marriage_report(p1_data, p2_data, groom_is_p1=True):
    """
    Generate complete South Indian Telugu Marriage Ponthana report with:
    - 10 Dashakootam Poruthams
    - 2 Bonus Dvadasakootam Poruthams (Vriksha & Bhoota)
    - Special Nakshatra Doshas (Jyeshtha, Moola, Aslesha, Visakha)
    - Lagna-to-Lagna Compatibility
    - 8th House Mangalya & 2nd House Kutumba Analysis
    - Rahu-Ketu 1/7 Axis Balance
    - Kuja Dosha & Kuja Samyam
    - 7th House & D9 Navamsa
    - Current Dasha-Bhukti Compatibility
    """
    groom_data = p1_data if groom_is_p1 else p2_data
    bride_data = p2_data if groom_is_p1 else p1_data

    b_nak_name = _get_nak_name(bride_data.get("nakshatra", "అశ్విని"))
    g_nak_name = _get_nak_name(groom_data.get("nakshatra", "అశ్విని"))

    bride_padam = bride_data.get("padam", bride_data.get("pada", 1))
    groom_padam = groom_data.get("padam", groom_data.get("pada", 1))

    # Derive Moon Rasi
    if "moon_lon" in bride_data:
        b_rasi_name = RASHIS[int(bride_data["moon_lon"] / 30) % 12]
    else:
        b_rasi_name = _get_rasi_name(bride_data.get("rashi", bride_data.get("rasi", bride_data.get("lagna", "మేషం"))))

    if "moon_lon" in groom_data:
        g_rasi_name = RASHIS[int(groom_data["moon_lon"] / 30) % 12]
    else:
        g_rasi_name = _get_rasi_name(groom_data.get("rashi", groom_data.get("rasi", groom_data.get("lagna", "మేషం"))))

    # 1. Calculate 10 Poruthams (Dashakootam)
    dina = calculate_dina(b_nak_name, g_nak_name)
    gana = calculate_gana(b_nak_name, g_nak_name)
    mahendra = calculate_mahendra(b_nak_name, g_nak_name)
    stree = calculate_stree_deergha(b_nak_name, g_nak_name)
    yoni = calculate_yoni(b_nak_name, g_nak_name)
    rasi = calculate_rasi(b_rasi_name, g_rasi_name)
    rasyadhipathi = calculate_rasyadhipathi(b_rasi_name, g_rasi_name)
    vasya = calculate_vasya(b_rasi_name, g_rasi_name)
    rajju = calculate_rajju(b_nak_name, g_nak_name)
    vedha = calculate_vedha(b_nak_name, g_nak_name)

    poruthams = [dina, gana, mahendra, stree, yoni, rasi, rasyadhipathi, vasya, rajju, vedha]
    total_score = sum(p["score"] for p in poruthams)
    score_percentage = round((total_score / 10.0) * 100, 1)

    # 2. Bonus Dvadasakootam Poruthams (Vriksha & Bhoota)
    vriksha = calculate_vriksha(b_nak_name, g_nak_name)
    bhoota = calculate_bhoota(b_nak_name, g_nak_name)
    extra_poruthams = [vriksha, bhoota]

    # 3. Special Nakshatra Doshas (Jyeshtha, Moola, Aslesha, Visakha)
    special_doshas = check_special_nakshatra_doshas(bride_data, groom_data)

    # 4. Lagna Compatibility
    lagna_comp = calculate_lagna_compatibility(bride_data, groom_data)

    # 5. 8th House Mangalya & 2nd House Kutumba
    mangalya_kutumba = analyze_8th_and_2nd_houses(bride_data, groom_data)

    # 6. Rahu-Ketu 1/7 Axis
    rahu_ketu_axis = analyze_rahu_ketu_axis(bride_data, groom_data)

    # 7. Nadi Analysis
    nadi = calculate_nadi(b_nak_name, g_nak_name, bride_padam, groom_padam, b_rasi_name, g_rasi_name)

    # 8. Kuja Dosha Analysis
    b_kuja = calculate_kuja_dosha(bride_data)
    g_kuja = calculate_kuja_dosha(groom_data)
    kuja_comparison = compare_kuja_samyam(b_kuja, g_kuja)

    # 9. 7th House & D9 Analysis
    jathaka_7th = analyze_7th_and_d9(p1_data, p2_data, groom_is_p1)

    # 10. Dasha Compatibility
    dasha_comp = analyze_dasha_compatibility(p1_data, p2_data, groom_is_p1)

    # Critical Checks & Overrides
    has_rajju_dosha = rajju["has_dosha"]
    has_vedha_dosha = vedha["has_dosha"]
    has_critical_override = has_rajju_dosha or has_vedha_dosha

    # Overall Verdict
    if has_critical_override:
        grade = "జాగ్రత్త అవసరం (ప్రత్యక్ష పరిశీలన)"
        color = "#ef4444"
        badge_class = "verdict-critical"
        summary_te = "పొంతన గుణములు ఉన్నప్పటికీ, అత్యంత కీలకమైన 'రజ్జు' లేదా 'వేధ' దోష సూచన ఉన్నది. సంప్రదాయ ధర్మశాస్త్రం ప్రకారం కుటుంబ పెద్దలు మరియు అనుభవజ్ఞులైన సిద్ధాంతుల ప్రత్యక్ష జాతక పరిశీలన తప్పనిసరి."
    elif total_score >= 8.5 and kuja_comparison["is_balanced"]:
        grade = "అత్యుత్తమ పొంతన (Excellent Match)"
        color = "#10b981"
        badge_class = "verdict-excellent"
        summary_te = f"దశకూట పొంతనలో {total_score}/10 మార్కులు సాధించారు. రజ్జు, వేధ దోషాలు లేవు. కుజ దోష సామ్యత చక్కగా ఉన్నది. ఈ దాంపత్యం సుఖసంతోషాలు, ఆయురారోగ్యాలు, వంశాభివృద్ధితో వర్ధిల్లును."
    elif total_score >= 6.5 and kuja_comparison["is_balanced"]:
        grade = "మంచి పొంతన (Good Match)"
        color = "#059669"
        badge_class = "verdict-good"
        summary_te = f"దశకూట పొంతనలో {total_score}/10 మార్కులతో ఆమోదయోగ్యమైన ఫలితం వచ్చినది. ప్రధానమైన రజ్జు, వేధ దోషాలు లేవు. వివాహానికి అనుకూలమైన పొంతన."
    elif total_score >= 4.5:
        grade = "మధ్యమ పొంతన (Average Match)"
        color = "#d97706"
        badge_class = "verdict-average"
        summary_te = f"దశకూట పొంతనలో {total_score}/10 మార్కులు వచ్చినవి. కొన్ని కూటములు అనుకూలంగా, మరికొన్ని సాధారణంగా ఉన్నాయి. పూర్తి జాతక బలాలు, దశా పరిస్థితులను పరిశీలించి నిర్ణయం తీసుకోవచ్చు."
    else:
        grade = "బలహీన పొంతన (Low Compatibility)"
        color = "#dc2626"
        badge_class = "verdict-weak"
        summary_te = f"దశకూట పొంతనలో {total_score}/10 మార్కులు మాత్రమే వచ్చినవి. పలు ముఖ్యమైన కూటములలో పొంతన తక్కువగా ఉన్నది."

    guidance_te = "గమనిక: కేవలం నక్షత్ర పొంతన మాత్రమే వివాహానికి ప్రాతిపదిక కాదు. సప్తమ భావ బలం, ఆయుష్షు, లగ్న మైత్రి, గురు-శుక్రుల స్థితి మరియు ప్రస్తుత దశా-భుక్తులను సమగ్రంగా పరిశీలించి పెద్దల ఆశీస్సులతో శుభ నిర్ణయం తీసుకోవాలి."

    g_info = NAKSHATRA_DATA.get(g_nak_name, {})
    b_info = NAKSHATRA_DATA.get(b_nak_name, {})

    return {
        "groom": {
            "name": groom_data.get("name", "వరుడు"),
            "dob": groom_data.get("dob", ""),
            "tob": groom_data.get("tob", ""),
            "place": groom_data.get("place", ""),
            "nakshatra": g_nak_name,
            "padam": groom_padam,
            "rasi": g_rasi_name,
            "rasi_lord": RASHI_LORDS.get(g_rasi_name, ""),
            "lagna": groom_data.get("lagna", ""),
            "gana": g_info.get("gana", ""),
            "yoni": g_info.get("yoni", ""),
            "rajju": g_info.get("rajju", ""),
            "nadi": g_info.get("nadi", ""),
            "lord": g_info.get("lord", "")
        },
        "bride": {
            "name": bride_data.get("name", "వధువు"),
            "dob": bride_data.get("dob", ""),
            "tob": bride_data.get("tob", ""),
            "place": bride_data.get("place", ""),
            "nakshatra": b_nak_name,
            "padam": bride_padam,
            "rasi": b_rasi_name,
            "rasi_lord": RASHI_LORDS.get(b_rasi_name, ""),
            "lagna": bride_data.get("lagna", ""),
            "gana": b_info.get("gana", ""),
            "yoni": b_info.get("yoni", ""),
            "rajju": b_info.get("rajju", ""),
            "nadi": b_info.get("nadi", ""),
            "lord": b_info.get("lord", "")
        },
        "groom_is_p1": groom_is_p1,
        "poruthams": poruthams,
        "total_score": total_score,
        "max_total_score": 10.0,
        "score_percentage": score_percentage,
        "extra_poruthams": extra_poruthams,
        "special_doshas": special_doshas,
        "lagna_comp": lagna_comp,
        "mangalya_kutumba": mangalya_kutumba,
        "rahu_ketu_axis": rahu_ketu_axis,
        "nadi": nadi,
        "groom_kuja": g_kuja,
        "bride_kuja": b_kuja,
        "kuja_comparison": kuja_comparison,
        "jathaka_7th": jathaka_7th,
        "dasha_comp": dasha_comp,
        "has_critical_override": has_critical_override,
        "verdict": {
            "grade": grade,
            "color": color,
            "badge_class": badge_class,
            "summary_te": summary_te,
            "guidance_te": guidance_te
        }
    }
