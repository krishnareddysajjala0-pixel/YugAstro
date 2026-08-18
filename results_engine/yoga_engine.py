# -*- coding: utf-8 -*-
"""
STEP 9: Yoga Engine
Detects planetary Yogas from yoga_rules.json and native chart context.
"""

from typing import Dict, Any, List, Optional
from .context import NormalizedChartContext
from .rule_loader import RuleLoader

class YogaEngine:
    def __init__(self, rule_loader: Optional[Any] = None):
        self.rule_loader = rule_loader or RuleLoader.get_instance()
        self.yoga_rules = self.rule_loader.load_json("yoga_rules.json")
        if not isinstance(self.yoga_rules, list):
            self.yoga_rules = []

    def evaluate_yogas(self, context: NormalizedChartContext) -> List[Dict[str, Any]]:
        active_yogas = []

        # 1. Check Sun + Mercury in same house (Ravi-Budha Yoga)
        sun_h = context.planet_houses.get("సూర్యుడు")
        budha_h = context.planet_houses.get("బుధుడు")
        if sun_h and budha_h and sun_h == budha_h:
            active_yogas.append({
                "rule_id": "YOGA_RAVI_BUDHA",
                "name": "రవి-బుధ యోగం (బుధాదిత్య యోగం)",
                "strength": "ఉత్తమ",
                "text": f"సూర్యుడు మరియు బుధుడు {sun_h}వ భావంలో కలిసి ఉండటం వలన బుధాదిత్య యోగం ఏర్పడుతోంది.",
                "explanation": "తీవ్రమైన విద్యా ప్రావీణ్యం, గణిత/జ్ఞాన నైపుణ్యం, సమాజంలో విశేష గుర్తింపు మరియు వ్యాపార చాతుర్యం కలుగుతుంది.",
                "source": "yugastro_repository_yogas"
            })

        # 2. Check Guru + Ketu in same house
        guru_h = context.planet_houses.get("గురు")
        ketu_h = context.planet_houses.get("కేతు")
        if guru_h and ketu_h and guru_h == ketu_h:
            active_yogas.append({
                "rule_id": "YOGA_GURU_KETU",
                "name": "గురు-కేతు ఆధ్యాత్మిక యోగం",
                "strength": "ఉత్తమ",
                "text": f"గురు మరియు కేతువు {guru_h}వ భావంలో కలిసి ఉండటం వలన ఆధ్యాత్మిక యోగం ఏర్పడుతోంది.",
                "explanation": "తీవ్రమైన ఆత్మజ్ఞానం, ఆధ్యాత్మిక చింతన, ధార్మిక గ్రంథ పఠనం మరియు గురువుల అనుగ్రహం లభిస్తుంది.",
                "source": "yugastro_repository_yogas"
            })

        # 3. Check Swakshetra (Planets in own house)
        for p_name, p_sign in context.planet_signs.items():
            lord_of_sign = context.house_lords.get(context.houses.get(p_sign, 0), "")
            if lord_of_sign == p_name:
                h_num = context.planet_houses.get(p_name, 1)
                active_yogas.append({
                    "rule_id": f"YOGA_SWAKSHETRA_{p_name}",
                    "name": f"{p_name} స్వక్షేత్ర యోగం",
                    "strength": "మంచి",
                    "text": f"{p_name} తన స్వంత రాశి ({p_sign}) {h_num}వ భావంలో స్థితి పొందడం శుభ యోగం.",
                    "explanation": "సొంత రాశిలో ఉన్న గ్రహము తన భావ కారకత్వాలను మరియు స్థాన ఫలాలను పరిపూర్ణంగా అందిస్తుంది.",
                    "source": "yugastro_repository_yogas"
                })

        # 4. Check Party Strength Yoga
        fav_count = sum(1 for p in context.planet_positions if context.is_favorable_planet(p.get("name","") if isinstance(p, dict) else str(p)))
        if fav_count >= 4:
            active_yogas.append({
                "rule_id": "YOGA_PARTY_STRENGTH",
                "name": "లగ్న గ్రహ వర్గ బల యోగం",
                "strength": "ఉత్తమ",
                "text": f"మీ {context.lagna} లగ్న వర్గానికి చెందిన గ్రహాలు అధిక బలాన్ని కలిగి ఉన్నాయి.",
                "explanation": "లగ్న వర్గానికి చెందిన అనుకూల గ్రహాలు బలమైన స్థానాలలో ఉండటం వలన జీవితంలో యోగకారక విజయాలు సాధిస్తారు.",
                "source": "yugastro_repository_yogas"
            })

        return active_yogas
