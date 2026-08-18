# -*- coding: utf-8 -*-
"""
STEP 6 & STEP 7: Dasha & Antardasha Interpretation Engine
Generates detailed Telugu analysis for current Mahadasha and Antardasha (Bhukti).
"""

from typing import Dict, Any, List
from .context import NormalizedChartContext

class DashaInterpreter:
    @staticmethod
    def interpret_mahadasha(context: NormalizedChartContext) -> Dict[str, Any]:
        dasa_planet = context.current_dasa
        if not dasa_planet:
            return {
                "rule_id": "DASHA_GENERAL",
                "text": "ప్రస్తుత దశా కాల విశ్లేషణ సిద్ధంగా ఉంది.",
                "explanation": "దశా గణన విశ్లేషణ."
            }

        is_fav = context.dasa_favorable
        party = context.get_party_for_planet(dasa_planet)
        lagna_party = "గురు వర్గం" if context.is_guru_party_lagna else "శని వర్గం"

        if is_fav:
            text = f"ప్రస్తుతం రన్ అవుతున్న {dasa_planet} మహాగ్రహ దశ మీ {context.lagna} లగ్నమునకు ({lagna_party}) అనుకూల యోగకారక దశగా పనిచేస్తుంది."
            explanation = f"త్రైత సిద్ధాంతం ప్రకారం {dasa_planet} ({party} వర్గం) మీ లగ్న వర్గముతో సమానంగా ఉన్నందున శుభ ఫలితాలు, ధనాభివృద్ధి, కార్యసిద్ధి లభిస్తాయి."
        else:
            text = f"ప్రస్తుతం రన్ అవుతున్న {dasa_planet} మహాగ్రహ దశ మీ {context.lagna} లగ్నమునకు ({lagna_party}) పరీక్షా సమయంగా పనిచేస్తుంది."
            explanation = f"త్రైత సిద్ధాంతం ప్రకారం {dasa_planet} ({party} వర్గం) మీ లగ్న వర్గముతో వ్యతిరేకంగా ఉన్నందున శ్రమ, ఓపిక మరియు జాగ్రత్తలు అవసరం."

        return {
            "rule_id": f"MAHADASHA_{dasa_planet}",
            "dasa_planet": dasa_planet,
            "is_favorable": is_fav,
            "text": text,
            "explanation": explanation
        }

    @staticmethod
    def interpret_antardasha(context: NormalizedChartContext) -> Dict[str, Any]:
        anthara_planet = context.current_anthara
        dasa_planet = context.current_dasa

        if not anthara_planet:
            return {
                "rule_id": "ANTHARA_GENERAL",
                "text": "అంతర్దశ ఫలితాలు విశ్లేషించబడ్డాయి.",
                "explanation": "అంతర్దశ గణన."
            }

        is_anthara_fav = context.is_favorable_planet(anthara_planet)

        if is_anthara_fav:
            text = f"ప్రస్తుత అంతర్దశ (భుక్తి): {anthara_planet} భుక్తి మీకు శుభఫలితాలను మరియు అనుకూల వాతావరణాన్ని అందిస్తుంది."
            explanation = f"{dasa_planet} మహాదశలో {anthara_planet} అంతర్దశ అనుకూల ప్రభావాన్ని చూపుతోంది."
        else:
            text = f"ప్రస్తుత అంతర్దశ (భుక్తి): {anthara_planet} భుక్తి సమయంలో మానసిక ఒత్తిడి లేదా శారీరక అలసట కలగవచ్చు."
            explanation = f"{dasa_planet} మహాదశలో {anthara_planet} అంతర్దశ పరీక్షా సమయాన్ని సూచిస్తోంది."

        return {
            "rule_id": f"ANTARDASHA_{anthara_planet}",
            "anthara_planet": anthara_planet,
            "is_favorable": is_anthara_fav,
            "text": text,
            "explanation": explanation
        }
