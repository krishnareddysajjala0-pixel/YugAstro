# -*- coding: utf-8 -*-
"""
CRITICAL BUG #12: Structured Yoga Engine.
Strict condition matching for repository-supported planetary Yogas.
Reports Yogas only when ALL required conditions are satisfied.
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

        # 1. Sun + Mercury in same house (Budhaditya Yoga)
        sun_h = context.planet_houses.get("సూర్యుడు")
        budha_h = context.planet_houses.get("బుధుడు")
        if sun_h and budha_h and sun_h == budha_h:
            active_yogas.append({
                "id": "YOGA_RAVI_BUDHA",
                "name_te": "రవి-బుధ యోగం (బుధాదిత్య యోగం)",
                "conditions": ["సూర్యుడు మరియు బుధుడు ఒకే భావంలో స్థితి"],
                "matched_conditions": [f"సూర్యుడు మరియు బుధుడు {sun_h}వ భావంలో కలిసి ఉన్నారు"],
                "strength": "ఉత్తమ",
                "affected_topics": ["విద్య", "మేధస్సు", "వ్యాపారం", "గౌరవం"],
                "positive_result": "విశేష విద్యా ప్రావీణ్యం, గణిత నైపుణ్యం, సమాజంలో గుర్తింపు మరియు వ్యాపార చాతుర్యం లభిస్తాయి.",
                "caution": "మానసిక తొందరపాటును అదుపులో ఉంచుకోవాలి.",
                "source": "yugastro_repository_yogas"
            })

        # 2. Jupiter + Ketu in same house (Spiritual Yoga)
        guru_h = context.planet_houses.get("గురు")
        ketu_h = context.planet_houses.get("కేతు")
        if guru_h and ketu_h and guru_h == ketu_h:
            active_yogas.append({
                "id": "YOGA_GURU_KETU",
                "name_te": "గురు-కేతు ఆధ్యాత్మిక వివేక యోగం",
                "conditions": ["గురు మరియు కేతువు ఒకే భావంలో స్థితి"],
                "matched_conditions": [f"గురు మరియు కేతువు {guru_h}వ భావంలో కలిసి ఉన్నారు"],
                "strength": "ఉత్తమ",
                "affected_topics": ["ఆధ్యాత్మికత", "మోక్ష/ఆధ్యాత్మిక అంశాలు", "తీర్థయాత్రలు"],
                "positive_result": "తీవ్రమైన ఆత్మజ్ఞానం, ఆధ్యాత్మిక వివేకం మరియు ధార్మిక గ్రంథ పరిజ్ఞానం లభిస్తుంది.",
                "caution": "లౌకిక విషయాలలో ఉదాసీనత వహించకూడదు.",
                "source": "yugastro_repository_yogas"
            })

        # 3. Swakshetra Yoga (Planet in own ruled sign)
        for p_name, p_sign in context.planet_signs.items():
            lord_of_sign = context.house_lords.get(context.houses.get(p_sign, 0), "")
            if lord_of_sign == p_name:
                h_num = context.planet_houses.get(p_name, 1)
                active_yogas.append({
                    "id": f"YOGA_SWAKSHETRA_{p_name}",
                    "name_te": f"{p_name} స్వక్షేత్ర యోగం",
                    "conditions": [f"{p_name} తన స్వంత లగ్నం నందు స్థితి పొందడం"],
                    "matched_conditions": [f"{p_name} తన స్వంత లగ్నం అయిన {p_sign} ({h_num}వ భావం) నందు స్థితి పొందింది"],
                    "strength": "మంచి",
                    "affected_topics": [context.house_signs.get(h_num, "వ్యక్తిత్వం")],
                    "positive_result": f"{p_name} స్వక్షేత్ర స్థితి వల్ల ఆ భావ కారకత్వాలు పరిపూర్ణ బలంతో సిద్ధస్తాయి.",
                    "caution": "గ్రహ ఆధిక్యతను గ్రహించి ప్రణాళికతో ముందడుగు వేయాలి.",
                    "source": "yugastro_repository_yogas"
                })

        return active_yogas
