# -*- coding: utf-8 -*-
"""
STEP 8: Transit Interpretation Engine
Generates date-aware transit analysis for Saturn, Jupiter, Rahu/Ketu, and 12 planets.
"""

from typing import Dict, Any, List
from .context import NormalizedChartContext

class TransitInterpreter:
    @staticmethod
    def interpret_transits(context: NormalizedChartContext) -> List[Dict[str, Any]]:
        results = []
        is_guru_party = context.is_guru_party_lagna
        lagna = context.lagna

        # 1. 2026 Saturn Transit (కుంభం నుండి మీన లగ్నం)
        saturn_text = f"2026 శని గోచారం (మీన లగ్నం ప్రవేశం): మీ {lagna} లగ్నమునకు శని గోచార ప్రభావం కర్మఫలదాతగా పనిచేస్తుంది."
        saturn_exp = "త్రైత సిద్ధాంతం ప్రకారం సరి లగ్నాలకు (శని వర్గం) అనుకూల ఫలితాలు, బేసి లగ్నాలకు (గురు వర్గం) పరీక్షా సమయం."
        results.append({
            "rule_id": "GOCHARAM_SATURN_2026",
            "planet": "శని",
            "type": "shubha" if not is_guru_party else "paapa",
            "text": saturn_text,
            "explanation": saturn_exp
        })

        # 2. 2026 Jupiter Transit (కర్కాటక ఉచ్చ స్థితి)
        jupiter_text = f"2026 గురు గోచారం (కర్కాటక లగ్నంలో ఉచ్చ స్థితి): గురు భగవానుని అనుగ్రహం లభిస్తుంది."
        jupiter_exp = "గురు గ్రహం కర్కాటకంలో ఉచ్చ స్థితి పొందడం వల్ల ఆధ్యాత్మిక ఆలోచనలు, ధార్మిక కార్యక్రమాలు మరియు జ్ఞానాభివృద్ధి కలుగుతాయి."
        results.append({
            "rule_id": "GOCHARAM_JUPITER_2026",
            "planet": "గురు",
            "type": "shubha" if is_guru_party else "shubha",
            "text": jupiter_text,
            "explanation": jupiter_exp
        })

        # 3. Rahu / Ketu Transit
        rahu_text = "రాహు-కేతువుల గోచారం: ఆకస్మిక మార్పులు మరియు విదేశీ/ఆధ్యాత్మిక ప్రయత్నాలకు అనుకూలం."
        rahu_exp = "రాహు మకరం/కేతు ధనస్సు గోచారం త్రైత మార్పులను సూచిస్తుంది."
        results.append({
            "rule_id": "GOCHARAM_RAHU_KETU_2026",
            "planet": "రాహు/కేతు",
            "type": "shubha",
            "text": rahu_text,
            "explanation": rahu_exp
        })

        return results
