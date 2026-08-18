# -*- coding: utf-8 -*-
"""
RAVAN ASTRO VERSION 5 — Topic Evidence Filter & Relevance Gate.
Enforces rule.topic_tags, allowed_houses, allowed_planets, allowed_lords, required keywords,
and excluded_keywords to eliminate cross-topic contamination.
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
        allowed_lords = t_def.get("allowed_lords", [])
        keywords = t_def.get("keywords", [])
        excluded_keywords = t_def.get("excluded_keywords", [])

        text_content = (str(rule_dict.get("text", "")) + " " + str(rule_dict.get("explanation", ""))).strip()

        # 1. Excluded Keyword Check (Strict Rejection)
        if text_content and any(ex_kw in text_content for ex_kw in excluded_keywords):
            return False

        # 2. House Check
        house_matched = house_num in allowed_houses or house_num in allowed_lords

        # 3. Planet Check
        planet_matched = lord_planet in allowed_planets

        # 4. Required Keyword Check in Rule Content
        keyword_matched = any(kw in text_content for kw in keywords) if text_content else False

        # Relevance Pass Condition: Must match allowed house AND (planet OR explicit keyword match)
        if house_matched:
            if not allowed_planets and not keywords:
                return True
            if planet_matched or keyword_matched:
                return True

        return False
