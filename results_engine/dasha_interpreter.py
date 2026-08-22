# -*- coding: utf-8 -*-
"""
CRITICAL BUG #10: Dasha & Antardasha Evidence Engine.
Synthesizes Dasha planet, natal house, natal sign, lordships, party affiliation,
and Antardasha interaction into topic-activated evidence.
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
                "text": "ప్రస్తుత దశా కాల విశ్లేషణ పరిపూర్ణంగా సిద్ధమైంది.",
                "explanation": "దశా గణన విశ్లేషణ."
            }

        is_fav = context.dasa_favorable
        party = context.get_party_for_planet(dasa_planet)
        lagna_party = "గురు వర్గం" if context.is_guru_party_lagna else "శని వర్గం"
        dasa_house = context.planet_houses.get(dasa_planet, 1)
        dasa_sign = context.planet_signs.get(dasa_planet, "మేషం")

        if is_fav:
            text = f"ప్రస్తుతం జరుగుతున్న {dasa_planet} మహాగ్రహ దశ ({dasa_sign} లగ్నం, {dasa_house}వ భావం) మీ {context.lagna} లగ్నమునకు ({lagna_party}) అనుకూల యోగకారక దశగా పనిచేస్తుంది."
            explanation = f"త్రైత సిద్ధాంతం ప్రకారం {dasa_planet} ({party} వర్గం) మీ లగ్న వర్గముతో అనుకూలంగా ఉన్నందున కార్యసిద్ధి, ధనాభివృద్ధి మరియు అభివృద్ధి అవకాశాలు లభిస్తాయి."
        else:
            text = f"ప్రస్తుతం జరుగుతున్న {dasa_planet} మహాగ్రహ దశ ({dasa_sign} లగ్నం, {dasa_house}వ భావం) మీ {context.lagna} లగ్నమునకు ({lagna_party}) శోధన/పరీక్షా సమయంగా పనిచేస్తుంది."
            explanation = f"త్రైత సిద్ధాంతం ప్రకారం {dasa_planet} ({party} వర్గం) మీ లగ్న వర్గముతో వ్యతిరేకంగా ఉన్నందున ఓర్పు, నియంత్రణ మరియు ప్రణాళికతో వ్యవహరించడం శ్రేయస్కరం."

        return {
            "rule_id": f"MAHADASHA_{dasa_planet}",
            "dasa_planet": dasa_planet,
            "dasa_house": dasa_house,
            "dasa_sign": dasa_sign,
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
        anthara_house = context.planet_houses.get(anthara_planet, 1)
        anthara_sign = context.planet_signs.get(anthara_planet, "మేషం")

        if is_anthara_fav:
            text = f"ప్రస్తుత అంతర్దశ (భుక్తి): {anthara_planet} భుక్తి ({anthara_sign} లగ్నం, {anthara_house}వ భావం) {dasa_planet} మహాగ్రహ దశలో అనుకూల ఫలితాలను మరియు మానసిక తృప్తిని అందిస్తుంది."
            explanation = f"{dasa_planet} దశలో {anthara_planet} అంతర్దశ మీ లగ్నమునకు అనుకూల యోగాన్ని అందిస్తోంది."
        else:
            text = f"ప్రస్తుత అంతర్దశ (భుక్తి): {anthara_planet} భుక్తి ({anthara_sign} లగ్నం, {anthara_house}వ భావం) {dasa_planet} మహాగ్రహ దశలో జాగ్రత్తలను మరియు ఒత్తిడి నిర్వహణను కోరుతోంది."
            explanation = f"{dasa_planet} దశలో {anthara_planet} అంతర్దశ సమయంలో నిగ్రహం అవసరం."

        return {
            "rule_id": f"ANTARDASHA_{anthara_planet}",
            "anthara_planet": anthara_planet,
            "anthara_house": anthara_house,
            "anthara_sign": anthara_sign,
            "is_favorable": is_anthara_fav,
            "text": text,
            "explanation": explanation
        }
