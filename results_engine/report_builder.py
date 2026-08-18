# -*- coding: utf-8 -*-
"""
ReportBuilder for YugAstro Results Engine.
Assembles evaluated results into structured report JSON objects for UI and API.
"""

from typing import Dict, Any, List
from .context import NormalizedChartContext
from .categories import PRIMARY_LIFE_AREAS

class ReportBuilder:
    @staticmethod
    def build_report(context: NormalizedChartContext, evaluated_data: Dict[str, Any]) -> Dict[str, Any]:
        categories = evaluated_data.get("categories", {})
        meta = evaluated_data.get("meta", {})

        # Collect positive highlights & cautions
        highlights = []
        cautions = []

        for cat_name, cat_data in categories.items():
            score = cat_data.get("score", 0)
            if score >= 5:
                highlights.append({
                    "category": cat_name,
                    "level": cat_data.get("level"),
                    "summary": cat_data.get("user_summary")
                })
            elif score <= -4:
                cautions.append({
                    "category": cat_name,
                    "level": cat_data.get("level"),
                    "summary": cat_data.get("user_summary")
                })

        # Generate overall synthesis
        pos_cnt = meta.get("positive_count", 0)
        neg_cnt = meta.get("negative_count", 0)
        
        if pos_cnt > neg_cnt * 1.5:
            overall_status = "ఈ జాతకంలో యోగకారక స్థానాలు మరియు అనుకూల దశా గ్రహాల ప్రభావం అధికంగా ఉన్నందున శుభ ఫలితాలు అధికంగా లభిస్తాయి."
        elif neg_cnt > pos_cnt * 1.5:
            overall_status = "ఈ జాతకంలో శోధన మరియు హెచ్చరికలను సూచించే గ్రహ స్థితులు ఉన్నందున జాగ్రత్తలతో ముందుకు సాగడం శ్రేయస్కరం."
        else:
            overall_status = "ఈ జాతకంలో అనుకూల మరియు ప్రతికూల అంశాలు సమాన నిష్పత్తిలో ఉన్నందున జీవితంలో శ్రమతో కూడిన విజయాలు లభిస్తాయి."

        # Format category sections for UI
        sections = []
        for cat_name, cat_data in categories.items():
            sections.append({
                "title": cat_name,
                "score": cat_data.get("score"),
                "level": cat_data.get("level"),
                "color": cat_data.get("color"),
                "icon": cat_data.get("icon"),
                "summary": cat_data.get("user_summary"),
                "reasons": cat_data.get("all_reasons", [])
            })

        return {
            "report_title": "సంపూర్ణ జాతక ఫలితాలు",
            "subtitle": "త్రైత సిద్ధాంత జ్యోతిష్య శాస్త్ర విశ్లేషణ",
            "birth_summary": {
                "name": context.name,
                "dob": context.dob,
                "tob": context.tob,
                "place": context.place,
                "lagna": context.lagna,
                "party": "గురు పార్టీ" if context.is_guru_party_lagna else "శని పార్టీ",
                "nakshatra": f"{context.nakshatra} ({context.padam}వ పాదం)",
                "current_dasa": context.current_dasa,
                "current_anthara": context.current_anthara
            },
            "overall_summary": overall_status,
            "highlights": highlights,
            "cautions": cautions,
            "sections": sections,
            "meta": meta
        }
