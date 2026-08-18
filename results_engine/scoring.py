# -*- coding: utf-8 -*-
"""
RAVAN ASTRO VERSION 5 — Scoring & Classification Scale.
Calculates positive_score, negative_score, net_score, and maps to Telugu level names.
"""

from typing import Dict, Any, List

SCORE_THRESHOLDS = [
    (8, "అత్యంత అనుకూలం", "#10b981", "🟢"),
    (4, "అనుకూలం", "#22c55e", "🟢"),
    (1, "కొంత అనుకూలం", "#84cc16", "🟡"),
    (0, "మిశ్రమ / సాధారణం", "#eab308", "🟡"),
    (-3, "జాగ్రత్త అవసరం", "#f97316", "🟠"),
    (-7, "ప్రతికూల ప్రభావం", "#ef4444", "🔴"),
    (-999, "బలమైన ప్రతికూల సూచన", "#dc2626", "🔴")
]

WEIGHTS = {
    'BHAVA_LORD_SHUBHA': 4,
    'BHAVA_LORD_PAAPA': -4,
    'BHAVA_MEANING_SHUBHA': 3,
    'BHAVA_MEANING_PAAPA': -3,
    'PARTY_FAVORABLE': 2,
    'PARTY_UNFAVORABLE': -2,
    'DASHA_FAVORABLE': 2,
    'DASHA_UNFAVORABLE': -2,
    'TRANSIT_FAVORABLE': 2,
    'TRANSIT_UNFAVORABLE': -2,
    'EXTRA_SUPPORT': 1,
    'EXTRA_CAUTION': -1
}

def get_level_for_score(net_score: int) -> Dict[str, Any]:
    if net_score >= 8:
        return {"level": "అత్యంత అనుకూలం", "color": "#10b981", "icon": "🟢", "score": net_score}
    elif net_score >= 4:
        return {"level": "అనుకూలం", "color": "#22c55e", "icon": "🟢", "score": net_score}
    elif net_score >= 1:
        return {"level": "కొంత అనుకూలం", "color": "#84cc16", "icon": "🟡", "score": net_score}
    elif net_score == 0:
        return {"level": "మిశ్రమ / సాధారణం", "color": "#eab308", "icon": "🟡", "score": net_score}
    elif net_score >= -3:
        return {"level": "జాగ్రత్త అవసరం", "color": "#f97316", "icon": "🟠", "score": net_score}
    elif net_score >= -7:
        return {"level": "ప్రతికూల ప్రభావం", "color": "#ef4444", "icon": "🔴", "score": net_score}
    else:
        return {"level": "బలమైన ప్రతికూల సూచన", "color": "#dc2626", "icon": "🔴", "score": net_score}

class CategoryScorer:
    def __init__(self, category_name: str):
        self.category_name = category_name
        self.positive_score = 0
        self.negative_score = 0
        self.positive_reasons: List[Dict[str, Any]] = []
        self.negative_reasons: List[Dict[str, Any]] = []

    def add_reason(self, reason: Dict[str, Any], weight: int):
        if weight > 0:
            self.positive_score += weight
            self.positive_reasons.append(reason)
        elif weight < 0:
            self.negative_score += abs(weight)  # positive number for negative score sum
            self.negative_reasons.append(reason)

    def net_score(self) -> int:
        return self.positive_score - self.negative_score

    def get_summary(self) -> Dict[str, Any]:
        net = self.net_score()
        level_info = get_level_for_score(net)
        return {
            "category": self.category_name,
            "positive_score": self.positive_score,
            "negative_score": self.negative_score,
            "net_score": net,
            "score": net,
            "level": level_info["level"],
            "color": level_info["color"],
            "icon": level_info["icon"],
            "positive_reasons": self.positive_reasons,
            "negative_reasons": self.negative_reasons,
            "all_reasons": self.positive_reasons + self.negative_reasons
        }
