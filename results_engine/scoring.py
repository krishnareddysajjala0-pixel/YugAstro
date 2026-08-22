# -*- coding: utf-8 -*-
"""
Scoring Engine for YugAstro Results Engine.
Calculates explainable numeric scores and maps them to Telugu evaluation levels.
"""

from typing import Dict, Any

SCORE_THRESHOLDS = [
    (8, "అత్యంత అనుకూలం", "#10b981", "🟢"),
    (5, "అనుకూలం", "#22c55e", "🟢"),
    (2, "కొంత అనుకూలం", "#84cc16", "🟡"),
    (-1, "మిశ్రమ / సాధారణం", "#eab308", "🟡"),
    (-4, "జాగ్రత్త అవసరం", "#f97316", "🟠"),
    (-7, "ప్రతికూల ప్రభావం", "#ef4444", "🔴"),
    (-999, "బలమైన ప్రతికూల సూచన", "#dc2626", "🔴")
]

WEIGHTS = {
    'BHAVA_LORD_SHUBHA': 3,
    'BHAVA_LORD_PAAPA': -3,
    'BHAVA_MEANING_SHUBHA': 2,
    'BHAVA_MEANING_PAAPA': -2,
    'PARTY_FAVORABLE': 2,
    'PARTY_UNFAVORABLE': -2,
    'DASHA_FAVORABLE': 2,
    'DASHA_UNFAVORABLE': -2,
    'TRANSIT_FAVORABLE': 2,
    'TRANSIT_UNFAVORABLE': -2,
    'EXTRA_SUPPORT': 1,
    'EXTRA_CAUTION': -1
}

def get_level_for_score(score: int) -> Dict[str, str]:
    for threshold, level_name, color, icon in SCORE_THRESHOLDS:
        if score >= threshold:
            return {
                "level": level_name,
                "color": color,
                "icon": icon,
                "score": score
            }
    return {
        "level": "బలమైన ప్రతికూల సూచన",
        "color": "#dc2626",
        "icon": "🔴",
        "score": score
    }

class CategoryScorer:
    def __init__(self, category_name: str):
        self.category_name = category_name
        self.positive_score = 0
        self.negative_score = 0
        self.positive_reasons = []
        self.negative_reasons = []

    def add_reason(self, reason: Dict[str, Any], weight: int):
        if weight > 0:
            self.positive_score += weight
            self.positive_reasons.append(reason)
        elif weight < 0:
            self.negative_score += weight  # weight is negative
            self.negative_reasons.append(reason)

    def total_score(self) -> int:
        return self.positive_score + self.negative_score

    def get_summary(self) -> Dict[str, Any]:
        tot = self.total_score()
        level_info = get_level_for_score(tot)
        return {
            "category": self.category_name,
            "score": tot,
            "positive_score": self.positive_score,
            "negative_score": self.negative_score,
            "level": level_info["level"],
            "color": level_info["color"],
            "icon": level_info["icon"],
            "positive_reasons": self.positive_reasons,
            "negative_reasons": self.negative_reasons,
            "all_reasons": self.positive_reasons + self.negative_reasons
        }
