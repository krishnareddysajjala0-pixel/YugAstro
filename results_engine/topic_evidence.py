# -*- coding: utf-8 -*-
"""
Strict Relevance Gate implementation for RAVAN ASTRO Results Engine.
Enforces rule.topic_tags, allowed_houses, allowed_planets, allowed_lordships, and keywords.
"""

from typing import Dict, Any
from .topic_definitions import TOPIC_DEFINITIONS

class TopicEvidenceFilter:
    @staticmethod
    def is_relevant(rule_dict: Dict[str, Any], topic: str, house_num: int, lord_planet: str) -> bool:
        t_def = TOPIC_DEFINITIONS.get(topic)
        if not t_def:
            return False

        allowed_houses = t_def.get("allowed_houses", [])
        allowed_planets = t_def.get("allowed_planets", [])
        allowed_lordships = t_def.get("allowed_lordships", [])
        keywords = t_def.get("keywords", [])

        # 1. House Check
        house_matched = house_num in allowed_houses or house_num in allowed_lordships

        # 2. Planet Check
        planet_matched = lord_planet in allowed_planets

        # 3. Keyword Check in Rule Content
        text_content = (str(rule_dict.get("text", "")) + " " + str(rule_dict.get("explanation", ""))).strip()
        keyword_matched = any(kw in text_content for kw in keywords) if text_content else False

        # Relevance Pass Condition: Must match allowed house AND (planet OR explicit keyword match)
        if house_matched:
            if not allowed_planets and not keywords:
                return True
            if planet_matched or keyword_matched:
                return True
        return False
