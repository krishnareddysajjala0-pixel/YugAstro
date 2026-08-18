# -*- coding: utf-8 -*-
"""
STEP 10: Safety Filter Engine (Enhanced).
Transforms deterministic/fatalistic statements into safe, constructive, advisory guidance.
"""

import re
from typing import Dict, Any, List

SAFETY_TRANSFORMATIONS = [
    (r"ఆత్మహత్య ప్రేరణ|ఆత్మహత్య", "తీవ్రమైన మానసిక ఒత్తిడి లేదా సంక్షోభ పరిస్థితుల్లో అదనపు జాగ్రత్త మరియు ఓపిక అవసరం"),
    (r"అకాల మృత్యువు|అకాల మరణము", "ఆరోగ్యం మరియు శారీరక భద్రత విషయంలో అదనపు శ్రద్ధ అవసరం"),
    (r"మరణశిక్ష", "న్యాయపరమైన అంశాలు మరియు వివాదాల విషయంలో ప్రణాళికాబద్ధమైన జాగ్రత్త అవసరం"),
    (r"నరక బాధ|నరకము", "ఆధ్యాత్మిక పరిహారాలు మరియు క్రమశిక్షణతో కూడిన శ్రమ అవసరం"),
    (r"తీవ్రమైన ప్రమాదాలు|ప్రమాదం", "ప్రయాణాలు మరియు వాహనాలు నడిపే సమయంలో అదనపు జాగ్రత్త వహించడం శ్రేయస్కరం")
]

class SafetyFilter:
    @staticmethod
    def sanitize_text(text: str) -> str:
        if not text:
            return ""

        sanitized = text
        for pattern, replacement in SAFETY_TRANSFORMATIONS:
            sanitized = re.sub(pattern, replacement, sanitized)

        return sanitized

    @staticmethod
    def apply_safety_filter_to_report(report: Dict[str, Any]) -> Dict[str, Any]:
        if "overall_summary" in report and report["overall_summary"]:
            report["overall_summary"] = SafetyFilter.sanitize_text(report["overall_summary"])

        if "sections" in report and isinstance(report["sections"], list):
            for sec in report["sections"]:
                if "summary" in sec and sec["summary"]:
                    sec["summary"] = SafetyFilter.sanitize_text(sec["summary"])
                if "reasons" in sec and isinstance(sec["reasons"], list):
                    for r in sec["reasons"]:
                        if "explanation" in r and r["explanation"]:
                            r["explanation"] = SafetyFilter.sanitize_text(r["explanation"])
                        if "text" in r and r["text"]:
                            r["text"] = SafetyFilter.sanitize_text(r["text"])

        return report
