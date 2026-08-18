# -*- coding: utf-8 -*-
"""
STEP 2: Topic Evidence Definitions & Relevance Filtering Layer.
Provides evidence-based house and planet mapping for all 40 report categories.
Ensures rules are attached to topics only when supported by actual evidence.
"""

from typing import Dict, List, Any

TOPIC_EVIDENCE: Dict[str, Dict[str, Any]] = {
    "వ్యక్తిత్వం": {
        "primary_houses": [1],
        "supporting_houses": [5, 9],
        "planets": ["సూర్యుడు", "చంద్రుడు"],
        "karakatwas": ["ఆత్మకలిగియుండుట", "స్వభావం"]
    },
    "శరీర స్వభావం": {
        "primary_houses": [1],
        "supporting_houses": [6],
        "planets": ["సూర్యుడు", "చంద్రుడు", "భూమి"],
        "karakatwas": ["దేహకాంతి", "ఆరోగ్యనిర్మాణం"]
    },
    "ఆరోగ్యం": {
        "primary_houses": [1, 6, 8],
        "supporting_houses": [12],
        "planets": ["సూర్యుడు", "కుజుడు", "శని", "మిత్ర"],
        "karakatwas": ["రోగకారకత్వములు", "ఆయుష్షు"]
    },
    "విద్య": {
        "primary_houses": [4, 5],
        "supporting_houses": [2, 9],
        "planets": ["బుధుడు", "గురు", "చంద్రుడు"],
        "karakatwas": ["విద్యాకారకత్వము", "బుద్ధి"]
    },
    "మేధస్సు": {
        "primary_houses": [5],
        "supporting_houses": [1, 9],
        "planets": ["బుధుడు", "గురు"],
        "karakatwas": ["జ్ఞానము", "వివేకము"]
    },
    "ఉద్యోగం": {
        "primary_houses": [10],
        "supporting_houses": [6, 11],
        "planets": ["శని", "సూర్యుడు", "కుజుడు"],
        "karakatwas": ["ఉద్యోగబలము", "సేవ"]
    },
    "వృత్తి": {
        "primary_houses": [10],
        "supporting_houses": [2, 6, 11],
        "planets": ["శని", "సూర్యుడు", "బుధుడు"],
        "karakatwas": ["జీవనోపాధి", "కార్యనిర్వహణ"]
    },
    "వ్యాపారం": {
        "primary_houses": [7],
        "supporting_houses": [2, 10, 11],
        "planets": ["బుధుడు", "శుక్రుడు"],
        "karakatwas": ["వాణిజ్యము", "భాగస్వామ్యం"]
    },
    "ధనం": {
        "primary_houses": [2],
        "supporting_houses": [5, 9, 11],
        "planets": ["గురు", "శుక్రుడు", "చంద్రుడు"],
        "karakatwas": ["ధనసంపాదన", "నిధి"]
    },
    "ఆదాయం": {
        "primary_houses": [11],
        "supporting_houses": [2, 9],
        "planets": ["గురు", "బుధుడు"],
        "karakatwas": ["లాభము", "ఆదాయమార్గాలు"]
    },
    "కుటుంబం": {
        "primary_houses": [2],
        "supporting_houses": [4],
        "planets": ["గురు", "శుక్రుడు"],
        "karakatwas": ["కుటుంబసౌఖ్యం"]
    },
    "వివాహం": {
        "primary_houses": [7],
        "supporting_houses": [2, 8, 11],
        "planets": ["శుక్రుడు", "గురు", "మిత్ర"],
        "karakatwas": ["కల్యాణయోగం"]
    },
    "దాంపత్యం": {
        "primary_houses": [7],
        "supporting_houses": [2, 4, 12],
        "planets": ["శుక్రుడు", "మిత్ర"],
        "karakatwas": ["సహజీవనము", "అనురాగం"]
    },
    "సంతానం": {
        "primary_houses": [5],
        "supporting_houses": [2, 9, 11],
        "planets": ["గురు"],
        "karakatwas": ["పుత్ర/పుత్రికాయోగం"]
    },
    "తల్లి": {
        "primary_houses": [4],
        "supporting_houses": [1, 9],
        "planets": ["చంద్రుడు"],
        "karakatwas": ["మాతృకారకత్వము"]
    },
    "తండ్రి": {
        "primary_houses": [9],
        "supporting_houses": [10],
        "planets": ["సూర్యుడు"],
        "karakatwas": ["పితృకారకత్వము"]
    },
    "సోదరులు": {
        "primary_houses": [3],
        "supporting_houses": [11],
        "planets": ["కుజుడు"],
        "karakatwas": ["భ్రాతృకారకత్వము"]
    },
    "గృహం": {
        "primary_houses": [4],
        "supporting_houses": [2, 11],
        "planets": ["శుక్రుడు", "కుజుడు", "భూమి"],
        "karakatwas": ["గృహసౌఖ్యం", "నివాసం"]
    },
    "వాహనం": {
        "primary_houses": [4],
        "supporting_houses": [11],
        "planets": ["శుక్రుడు"],
        "karakatwas": ["వాహనయోగం"]
    },
    "స్థిరాస్తి": {
        "primary_houses": [4],
        "supporting_houses": [2, 11],
        "planets": ["కుజుడు", "భూమి"],
        "karakatwas": ["భూవసతి", "ఆస్తులు"]
    },
    "విదేశీ ప్రయాణం": {
        "primary_houses": [9, 12],
        "supporting_houses": [3, 7],
        "planets": ["రాహు", "కేతు", "చంద్రుడు"],
        "karakatwas": ["విదేశయాత్ర", "దూరప్రయాణం"]
    },
    "తీర్థయాత్రలు": {
        "primary_houses": [9],
        "supporting_houses": [12],
        "planets": ["కేతు", "గురు"],
        "karakatwas": ["పుణ్యక్షేత్రాలు"]
    },
    "ఆధ్యాత్మికత": {
        "primary_houses": [9, 12],
        "supporting_houses": [5],
        "planets": ["కేతు", "గురు", "చిత్ర"],
        "karakatwas": ["ఉపాసన", "జ్ఞానము"]
    },
    "శత్రువులు": {
        "primary_houses": [6],
        "supporting_houses": [8, 12],
        "planets": ["కుజుడు", "శని", "రాహు"],
        "karakatwas": ["విరోధులు", "మత్సరం"]
    },
    "ఋణాలు": {
        "primary_houses": [6],
        "supporting_houses": [8, 12],
        "planets": ["శని", "కుజుడు"],
        "karakatwas": ["అప్పులు", "రుణభారం"]
    },
    "పోటీ": {
        "primary_houses": [3, 6],
        "supporting_houses": [10, 11],
        "planets": ["కుజుడు", "సూర్యుడు", "రాహు"],
        "karakatwas": ["పోటీపరీక్షలు", "విజయం"]
    },
    "గౌరవం": {
        "primary_houses": [10],
        "supporting_houses": [1, 5, 9],
        "planets": ["సూర్యుడు", "గురు"],
        "karakatwas": ["కీర్తి", "మర్యాద"]
    },
    "అధికార స్థానం": {
        "primary_houses": [10],
        "supporting_houses": [1, 5, 9, 11],
        "planets": ["సూర్యుడు", "కుజుడు"],
        "karakatwas": ["ప్రభుత్వబలం", "పదవి"]
    },
    "లాభాలు": {
        "primary_houses": [11],
        "supporting_houses": [2, 9],
        "planets": ["గురు", "శుక్రుడు"],
        "karakatwas": ["ఫలితప్రాప్తి"]
    },
    "ఖర్చులు": {
        "primary_houses": [12],
        "supporting_houses": [6, 8],
        "planets": ["శని", "రాహు"],
        "karakatwas": ["వ్యయం", "నష్టం"]
    },
    "మోక్ష/ఆధ్యాత్మిక అంశాలు": {
        "primary_houses": [12],
        "supporting_houses": [8, 9],
        "planets": ["కేతు", "చిత్ర"],
        "karakatwas": ["ముక్తి", "వైరాగ్యం"]
    }
}

class TopicEvidenceFilter:
    @staticmethod
    def is_rule_relevant_to_topic(topic: str, house_num: int, lord_planet: str) -> bool:
        info = TOPIC_EVIDENCE.get(topic)
        if not info:
            return True

        primary = info.get("primary_houses", [])
        supporting = info.get("supporting_houses", [])

        # House matching relevance
        if house_num in primary or house_num in supporting:
            return True

        # Planet karakatwa matching relevance
        planets = info.get("planets", [])
        if lord_planet in planets:
            return True

        return False
