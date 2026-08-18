# -*- coding: utf-8 -*-
"""
STEP 2: Rule -> Topic Mapping
Maps rules, houses, and planetary karakatwas to the 37 specification categories.
"""

from typing import Dict, List
from .categories import HOUSE_CATEGORY_MAP, CATEGORIES

# Planet Karakatwa -> Topic Category Mapping
PLANET_TOPIC_MAP: Dict[str, List[str]] = {
    "సూర్యుడు": ["వ్యక్తిత్వం", "అధికార స్థానం", "గౌరవం", "తండ్రి", "ఆరోగ్యం"],
    "చంద్రుడు": ["శరీర స్వభావం", "తల్లి", "విద్య", "మేధస్సు", "ధనం"],
    "కుజుడు": ["పోటీ", "సోదరులు", "స్థిరాస్తి", "శత్రువులు", "ఆరోగ్యం"],
    "బుధుడు": ["విద్య", "మేధస్సు", "వ్యాపారం", "ఆదాయం"],
    "గురు": ["విద్య", "ధనం", "సంతానం", "ఆధ్యాత్మికత", "గౌరవం"],
    "శుక్రుడు": ["వివాహం", "దాంపత్యం", "వాహనం", "గృహం", "లాభాలు"],
    "శని": ["ఉద్యోగం", "వృత్తి", "ఋణాలు", "శత్రువులు", "జాగ్రత్తలు"],
    "రాహు": ["విదేశీ ప్రయాణం", "పోటీ", "జాగ్రత్తలు"],
    "కేతు": ["మోక్ష/ఆధ్యాత్మిక అంశాలు", "ఆధ్యాత్మికత", "తీర్థయాత్రలు"],
    "భూమి": ["స్థిరాస్తి", "గృహం", "శరీర స్వభావం"],
    "మిత్ర": ["ఆరోగ్యం", "ఆధ్యాత్మికత", "దాంపత్యం"],
    "చిత్ర": ["ఆధ్యాత్మికత", "మోక్ష/ఆధ్యాత్మిక అంశాలు", "జాగ్రత్తలు"]
}

class TopicMapper:
    @staticmethod
    def get_categories_for_house(house_num: int) -> List[str]:
        return HOUSE_CATEGORY_MAP.get(house_num, ["వ్యక్తిత్వం"])

    @staticmethod
    def get_categories_for_planet(planet_name: str) -> List[str]:
        return PLANET_TOPIC_MAP.get(planet_name, ["వ్యక్తిత్వం"])
