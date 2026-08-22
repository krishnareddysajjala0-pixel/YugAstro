# -*- coding: utf-8 -*-
"""
Rules Exporter Module for RAVAN ASTRO / YugAstro.
Aggregates all 144 Bhava Lord Placement Rules, 12 House Meanings, 12 Planet Constants,
Yoga Rules, Extracted Rules, and Topic Mappings into a unified master handbook dataset.
"""

import os
import json
from typing import Dict, List, Any
from .rule_loader import RuleLoader
from .topic_definitions import TOPIC_DEFINITIONS

PLANET_NAMES_TELUGU = [
    "సూర్యుడు", "చంద్రుడు", "కుజుడు", "బుధుడు", "గురు", "శుక్రుడు",
    "శని", "రాహు", "కేతు", "భూమి", "మిత్ర", "చిత్ర"
]

HOUSE_NAMES_TELUGU = [
    "1వ భావం (లగ్న భావం - వ్యక్తిత్వం & ఆరోగ్యం)",
    "2వ భావం (ధన భావం - ధనం & కుటుంబం)",
    "3వ భావం (భ్రాతృ భావం - సోదరులు & ధైర్యం)",
    "4వ భావం (మాతృ/గృహ భావం - తల్లి, గృహం, వాహనం)",
    "5వ భావం (పుత్ర/బుద్ధి భావం - సంతానం, విద్య, మేధస్సు)",
    "6వ భావం (శత్రు/రోగ భావం - శత్రువులు, ఋణాలు, ఆరోగ్యం)",
    "7వ భావం (కల్యాణ/దాంపత్య భావం - వివాహం & వ్యాపారం)",
    "8వ భావం (ఆయుర్ భావం - ఆయుష్షు & హెచ్చరికలు)",
    "9వ భావం (పితృ/భాగ్య భావం - తండ్రి, తీర్థయాత్రలు, ఆధ్యాత్మికత)",
    "10వ భావం (కర్మ భావం - ఉద్యోగం, వృత్తి, అధికార స్థానం)",
    "11వ భావం (లాభ భావం - ఆదాయం, లాభాలు, ఆశలు)",
    "12వ భావం (వ్యయ/మోక్ష భావం - ఖర్చులు, విదేశీ ప్రయాణం, మోక్షం)"
]

class RulesExporter:
    @staticmethod
    def get_all_rules_dataset() -> Dict[str, Any]:
        loader = RuleLoader.get_instance()
        bhava_lord_matrix = loader.get_bhava_lord_rules()
        detailed_meanings = loader.get_detailed_bhava_meanings()
        constants = loader.get_astro_constants()
        extracted_lines = loader.get_extracted_rules()
        qa_lines = loader.get_qa_rules()
        yogas = loader.load_json("yoga_rules.json")

        # 1. Format 12x12 Lord Placement Matrix (144 Rules)
        formatted_lord_matrix = []
        for h in range(1, 13):
            h_str = str(h)
            placements = []
            h_rules = bhava_lord_matrix.get(h_str, {})
            for p in range(1, 13):
                p_str = str(p)
                p_entry = h_rules.get(p_str, {})
                shubha = p_entry.get("shubha", "").strip() if isinstance(p_entry, dict) else ""
                paapa = p_entry.get("paapa", "").strip() if isinstance(p_entry, dict) else ""

                placements.append({
                    "house": h,
                    "placement": p,
                    "rule_id": f"BHAVA_LORD_{h}_{p}",
                    "title": f"{h}వ భావాధిపతి → {p}వ భావము నందు స్థితి",
                    "shubha": shubha,
                    "paapa": paapa
                })
            formatted_lord_matrix.append({
                "house_num": h,
                "house_title": HOUSE_NAMES_TELUGU[h-1],
                "placements": placements
            })

        # 2. Format 12 House Meanings
        formatted_house_meanings = []
        for h in range(1, 13):
            entry = detailed_meanings.get(str(h), {})
            formatted_house_meanings.append({
                "house_num": h,
                "title": entry.get("title", f"{h}వ భావం"),
                "meaning": entry.get("meaning", ""),
                "shubha": entry.get("shubha", ""),
                "paapa": entry.get("paapa", ""),
                "neutral": entry.get("neutral", "")
            })

        # 3. Format Planet System & Karakatwas
        formatted_planets = []
        for p in PLANET_NAMES_TELUGU:
            karakatwa = constants.get("karakatwas", {}).get(p, "త్రైత సిద్ధాంత ప్రధాన గ్రహము")
            ruler_sign = constants.get("rulerships", {}).get(p, "")
            party = "గురు వర్గం" if p in constants.get("guru_party_planets", []) else "శని వర్గం"
            formatted_planets.append({
                "name": p,
                "ruler_sign": ruler_sign,
                "party": party,
                "karakatwa": karakatwa
            })

        # 4. Format 40 Topic Mappings
        formatted_topics = []
        for topic_name, t_def in TOPIC_DEFINITIONS.items():
            formatted_topics.append({
                "name": topic_name,
                "topic_id": t_def.get("topic_id"),
                "allowed_houses": ", ".join(str(x) for x in t_def.get("allowed_houses", [])),
                "allowed_planets": ", ".join(t_def.get("allowed_planets", [])),
                "keywords": ", ".join(t_def.get("keywords", []))
            })

        return {
            "title": "త్రైత సిద్ధాంత జ్యోతిష్య శాస్త్ర — సంపూర్ణ ఫలిత నియమావళి (Master Rules Handbook)",
            "subtitle": "YugAstro & RAVAN ASTRO - 12 Planet System Complete Rules Database",
            "total_lord_rules": 144,
            "total_houses": 12,
            "total_planets": 12,
            "total_topics": len(TOPIC_DEFINITIONS),
            "lord_matrix": formatted_lord_matrix,
            "house_meanings": formatted_house_meanings,
            "planets": formatted_planets,
            "topics": formatted_topics,
            "yogas": yogas if isinstance(yogas, list) else [],
            "extracted_rules": extracted_lines,
            "qa_rules": qa_lines
        }
