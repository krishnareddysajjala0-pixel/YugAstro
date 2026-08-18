# -*- coding: utf-8 -*-
"""
STEP 3 & STEP 8: Topic Synthesizer Engine.
Synthesizes positive & negative evidence for each topic into a distinct,
professional Telugu paragraph without raw paragraph concatenation or duplicates.
"""

from typing import Dict, Any, List
from .safety_filter import SafetyFilter

class ResultSynthesizer:
    @staticmethod
    def synthesize_topic_result(topic: str, pos_reasons: List[Dict[str, Any]], neg_reasons: List[Dict[str, Any]]) -> Dict[str, Any]:
        pos_texts = list(dict.fromkeys([r.get("text", "").strip() for r in pos_reasons if r.get("text")]))
        neg_texts = list(dict.fromkeys([r.get("text", "").strip() for r in neg_reasons if r.get("text")]))

        pos_count = len(pos_reasons)
        neg_count = len(neg_reasons)

        if pos_texts and neg_texts:
            pos_lead = pos_texts[0]
            neg_lead = neg_texts[0]
            synthesized_text = f"{topic} అంశంలో {pos_lead} అనుకూల పరిణామాలు సూచిస్తున్నాయి. అయితే, {neg_lead} తగిన అవగాహన మరియు జాగ్రత్త అవసరం."
        elif pos_texts:
            lead = pos_texts[0]
            extra = " అలాగే అనుకూల సమయం వ్యక్తమవుతోంది." if pos_count > 1 else ""
            synthesized_text = f"{topic} విభాగానికి సంబంధించి {lead} శ్రేయోదాయకమైన సూచనలు వ్యక్తమవుతున్నాయి.{extra}"
        elif neg_texts:
            lead = neg_texts[0]
            synthesized_text = f"{topic} విషయంలో {lead} కొన్ని సవాళ్లు లేదా శోధన కాలాన్ని సూచిస్తోంది. ప్రణాళికతో వ్యవహరించడం మంచిది."
        else:
            synthesized_text = f"{topic} విభాగానికి సంబంధించిన ఫలితాలు ఈ జాతకంలో సమతుల్యంగా వ్యక్తమవుతున్నాయి."

        # Safety filter transformation
        synthesized_text = SafetyFilter.sanitize_text(synthesized_text)

        return {
            "topic": topic,
            "synthesized_text": synthesized_text,
            "supporting_rules_count": pos_count,
            "contradicting_rules_count": neg_count
        }
