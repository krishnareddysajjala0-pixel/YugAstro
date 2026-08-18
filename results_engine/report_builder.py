# -*- coding: utf-8 -*-
"""
STEP 12: 40-Section Report Builder.
Constructs structured 40-section report objects for UI and PDF rendering.
"""

from typing import Dict, Any, List
from .context import NormalizedChartContext
from .safety_filter import SafetyFilter

ALL_40_SECTIONS = [
    "వ్యక్తిత్వం", "శరీర స్వభావం", "ఆరోగ్యం", "విద్య", "మేధస్సు",
    "ఉద్యోగం", "వృత్తి", "వ్యాపారం", "ధనం", "ఆదాయం",
    "కుటుంబం", "వివాహం", "దాంపత్యం", "సంతానం", "తల్లి",
    "తండ్రి", "సోదరులు", "గృహం", "వాహనం", "స్థిరాస్తి",
    "విదేశీ ప్రయాణం", "తీర్థయాత్రలు", "ఆధ్యాత్మికత", "శత్రువులు", "ఋణాలు",
    "పోటీ", "గౌరవం", "అధికార స్థానం", "లాభాలు", "ఖర్చులు",
    "మోక్ష/ఆధ్యాత్మిక అంశాలు", "ముఖ్య యోగాలు", "ప్రస్తుత దశ", "అంతర్దశ", "గోచారం"
]

class ReportBuilder:
    @staticmethod
    def build_report(context: NormalizedChartContext, evaluated_data: Dict[str, Any]) -> Dict[str, Any]:
        categories = evaluated_data.get("categories", {})
        meta = evaluated_data.get("meta", {})
        yogas = evaluated_data.get("yogas", [])

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

        pos_cnt = meta.get("positive_count", 0)
        neg_cnt = meta.get("negative_count", 0)

        if pos_cnt > neg_cnt * 1.5:
            overall_status = "ఈ జాతకంలో యోగకారక స్థానాలు మరియు అనుకూల దశా గ్రహాల ప్రభావం అధికంగా ఉన్నందున శుభ ఫలితాలు అధికంగా లభిస్తాయి."
        elif neg_cnt > pos_cnt * 1.5:
            overall_status = "ఈ జాతకంలో శోధన మరియు హెచ్చరికలను సూచించే గ్రహ స్థితులు ఉన్నందున ప్రణాళికాబద్ధమైన జాగ్రత్తలతో ముందుకు సాగడం శ్రేయస్కరం."
        else:
            overall_status = "ఈ జాతకంలో అనుకూల మరియు ప్రతికూల అంశాలు సమతుల్య నిష్పత్తిలో ఉన్నందున శ్రమతో కూడిన విజయాలు లభిస్తాయి."

        overall_status = SafetyFilter.sanitize_text(overall_status)

        # Format 40 section list
        sections = []
        for cat_name in ALL_40_SECTIONS:
            cat_data = categories.get(cat_name, {})
            sections.append({
                "title": cat_name,
                "score": cat_data.get("score", 0),
                "level": cat_data.get("level", "మిశ్రమ / సాధారణం"),
                "color": cat_data.get("color", "#eab308"),
                "icon": cat_data.get("icon", "🟡"),
                "summary": cat_data.get("user_summary", "ఈ రంగానికి సంబంధించి ఫలితాలు సమతుల్యంగా ఉన్నాయి."),
                "reasons": cat_data.get("all_reasons", []),
                "supporting_rules_count": cat_data.get("positive_reasons_count", len(cat_data.get("positive_reasons", []))),
                "contradicting_rules_count": cat_data.get("negative_reasons_count", len(cat_data.get("negative_reasons", [])))
            })

        report = {
            "report_title": "సంపూర్ణ జాతక ఫలితాలు",
            "subtitle": "త్రైత సిద్ధాంత 40-విభాగాల నివేదిక",
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
            "yogas": yogas,
            "meta": meta
        }

        return SafetyFilter.apply_safety_filter_to_report(report)
