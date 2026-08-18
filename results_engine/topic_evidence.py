# -*- coding: utf-8 -*-
"""
STEP 1 & STEP 2: Strict Topic Evidence Definitions & Relevance Gate.
Prevents duplicate paragraphs across topics by enforcing specific house, planet,
and karakatwa relevance checks for every topic.
"""

from typing import Dict, List, Any

# Strict Evidence Definitions for every topic
TOPIC_EVIDENCE_MAP: Dict[str, Dict[str, Any]] = {
    "విద్య": {
        "primary_houses": [4, 5],
        "supporting_houses": [2],
        "planets": ["బుధుడు", "గురు", "చంద్రుడు"],
        "keywords": ["విద్య", "చదువు", "జ్ఞాన", "పాఠశాల", "పరీక్ష"]
    },
    "మేధస్సు": {
        "primary_houses": [5],
        "supporting_houses": [1],
        "planets": ["బుధుడు", "గురు"],
        "keywords": ["మేధస్సు", "బుద్ధి", "వివేకం", "ఆలోచన", "జ్ఞాపకశక్తి"]
    },
    "సంతానం": {
        "primary_houses": [5],
        "supporting_houses": [2, 9, 11],
        "planets": ["గురు"],
        "keywords": ["సంతానం", "పుత్రు", "పుత్రిక", "పిల్లలు", "వంశాభివృద్ధి"]
    },
    "గృహం": {
        "primary_houses": [4],
        "supporting_houses": [2],
        "planets": ["శుక్రుడు", "భూమి"],
        "keywords": ["గృహం", "ఇల్లు", "నివాసం", "గృహసౌఖ్యం"]
    },
    "వాహనం": {
        "primary_houses": [4],
        "supporting_houses": [11],
        "planets": ["శుక్రుడు"],
        "keywords": ["వాహన", "కారు", "రవాణా", "సవారి"]
    },
    "స్థిరాస్తి": {
        "primary_houses": [4],
        "supporting_houses": [2, 11],
        "planets": ["కుజుడు", "భూమి"],
        "keywords": ["స్థిరాస్తి", "భూమి", "ఆస్తి", "పొలం", "స్థలం"]
    },
    "వివాహం": {
        "primary_houses": [7],
        "supporting_houses": [2, 8, 11],
        "planets": ["శుక్రుడు", "గురు", "మిత్ర"],
        "keywords": ["వివాహం", "కల్యాణం", "పెళ్లి", "భార్య", "భర్త"]
    },
    "దాంపత్యం": {
        "primary_houses": [7],
        "supporting_houses": [4, 12],
        "planets": ["శుక్రుడు", "మిత్ర"],
        "keywords": ["దాంపత్యం", "అనురాగం", "సహజీవనం", "సౌఖ్యం", "కలహాలు"]
    },
    "విదేశీ ప్రయాణం": {
        "primary_houses": [9, 12],
        "supporting_houses": [3, 7],
        "planets": ["రాహు", "కేతు", "చంద్రుడు"],
        "keywords": ["విదేశీ", "దూరప్రయాణం", "విదేశ యాత్ర", "సముద్ర ప్రయాణం"]
    },
    "ఖర్చులు": {
        "primary_houses": [12],
        "supporting_houses": [6, 8],
        "planets": ["శని", "రాహు"],
        "keywords": ["ఖర్చులు", "వ్యయం", "నష్టం", "ధనవ్యయం"]
    },
    "ఆధ్యాత్మికత": {
        "primary_houses": [9, 12],
        "supporting_houses": [5],
        "planets": ["కేతు", "గురు", "చిత్ర"],
        "keywords": ["ఆధ్యాత్మిక", "ఉపాసన", "భక్తి", "జ్ఞానం", "ధర్మం"]
    },
    "తీర్థయాత్రలు": {
        "primary_houses": [9],
        "supporting_houses": [12],
        "planets": ["కేతు", "గురు"],
        "keywords": ["తీర్థయాత్ర", "పుణ్యక్షేత్రం", "యాత్ర", "దర్శనం"]
    },
    "సోదరులు": {
        "primary_houses": [3],
        "supporting_houses": [11],
        "planets": ["కుజుడు"],
        "keywords": ["సోదర", "అన్న", "తమ్ముడు", "అక్క", "చెల్లెలు", "భ్రాతృ"]
    },
    "ఉద్యోగం": {
        "primary_houses": [10],
        "supporting_houses": [6, 11],
        "planets": ["శని", "సూర్యుడు"],
        "keywords": ["ఉద్యోగం", "సేవ", "పని", "కార్యాలయం"]
    },
    "వృత్తి": {
        "primary_houses": [10],
        "supporting_houses": [2, 6, 11],
        "planets": ["శని", "బుధుడు"],
        "keywords": ["వృత్తి", "జీవనోపాధి", "వృత్తి నైపుణ్యం"]
    },
    "వ్యాపారం": {
        "primary_houses": [7],
        "supporting_houses": [2, 10, 11],
        "planets": ["బుధుడు", "శుక్రుడు"],
        "keywords": ["వ్యాపారం", "వాణిజ్యం", "వర్తకం", "భాగస్వామి"]
    },
    "ధనం": {
        "primary_houses": [2],
        "supporting_houses": [5, 9, 11],
        "planets": ["గురు", "శుక్రుడు"],
        "keywords": ["ధనం", "సంపాదన", "నిధి", "ఆర్థిక"]
    },
    "ఆదాయం": {
        "primary_houses": [11],
        "supporting_houses": [2, 9],
        "planets": ["గురు", "బుధుడు"],
        "keywords": ["ఆదాయం", "లాభం", "వరవడి"]
    },
    "ఆరోగ్యం": {
        "primary_houses": [1, 6, 8],
        "supporting_houses": [12],
        "planets": ["సూర్యుడు", "కుజుడు", "శని", "మిత్ర"],
        "keywords": ["ఆరోగ్యం", "దేహం", "వ్యాధి", "చికిత్స"]
    }
}

class TopicEvidenceFilter:
    @staticmethod
    def is_rule_relevant(rule_dict: Dict[str, Any], topic: str, house_num: int, lord_planet: str) -> bool:
        ev = TOPIC_EVIDENCE_MAP.get(topic)
        if not ev:
            return True

        primary = ev.get("primary_houses", [])
        supporting = ev.get("supporting_houses", [])
        planets = ev.get("planets", [])
        keywords = ev.get("keywords", [])

        # 1. House Check
        if house_num in primary or house_num in supporting:
            return True

        # 2. Planet Karakatwa Check
        if lord_planet in planets:
            return True

        # 3. Keyword Check in Rule Explanation/Text
        rule_text = str(rule_dict.get("text", "")) + " " + str(rule_dict.get("explanation", ""))
        for kw in keywords:
            if kw in rule_text:
                return True

        return False
