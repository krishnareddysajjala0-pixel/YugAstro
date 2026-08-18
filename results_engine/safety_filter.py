# -*- coding: utf-8 -*-
"""
STEP 10: Safety Filter Engine
Filters and softens extreme or fatalistic statements into constructive, advisory guidance.
"""

import re
from typing import Dict, Any, List

FATALISTIC_TERMS = [
    ("అకాల మరణము", "ఆరోగ్య విషయంలో ప్రత్యేక శ్రద్ధ"),
    ("మరణశిక్ష", "న్యాయ సంబంధిత వ్యవహారాలలో జాగ్రత్త"),
    ("నరకము", "పరిహారాలు మరియు శ్రమ"),
    ("ప్రమాదాలు", "ప్రయాణాలలో జాగ్రత్తలు")
]

class SafetyFilter:
    @staticmethod
    def sanitize_text(text: str) -> str:
        if not text:
            return ""

        sanitized = text
        for term, replacement in FATALISTIC_TERMS:
            sanitized = sanitized.replace(term, replacement)

        return sanitized

    @staticmethod
    def apply_safety_filter_to_report(report: Dict[str, Any]) -> Dict[str, Any]:
        if "overall_summary" in report:
            report["overall_summary"] = SafetyFilter.sanitize_text(report["overall_summary"])

        if "sections" in report and isinstance(report["sections"], list):
            for sec in report["sections"]:
                if "summary" in sec:
                    sec["summary"] = SafetyFilter.sanitize_text(sec["summary"])
                if "reasons" in sec and isinstance(sec["reasons"], list):
                    for r in sec["reasons"]:
                        if "explanation" in r:
                            r["explanation"] = SafetyFilter.sanitize_text(r["explanation"])
                        if "text" in r:
                            r["text"] = SafetyFilter.sanitize_text(r["text"])

        return report
