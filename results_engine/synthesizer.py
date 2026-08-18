# -*- coding: utf-8 -*-
"""
STEP 3, 4, 11: Telugu Synthesis Engine.
Synthesizes positive & negative evidence, resolves contradictions, deduplicates rules,
and formats smooth, professional Telugu prose.
"""

from typing import Dict, Any, List
from .safety_filter import SafetyFilter

class ResultSynthesizer:
    @staticmethod
    def synthesize_topic_result(topic: str, pos_reasons: List[Dict[str, Any]], neg_reasons: List[Dict[str, Any]]) -> Dict[str, Any]:
        # Deduplicate positive and negative evidence
        pos_texts = list(dict.fromkeys([r.get("text", "").strip() for r in pos_reasons if r.get("text")]))
        neg_texts = list(dict.fromkeys([r.get("text", "").strip() for r in neg_reasons if r.get("text")]))

        pos_count = len(pos_reasons)
        neg_count = len(neg_reasons)

        # Contradiction Analysis & Synthesis
        if pos_texts and neg_texts:
            pos_lead = pos_texts[0]
            neg_lead = neg_texts[0]
            synthesized_text = f"{topic} విషయంలో {pos_lead} అనుకూల పరిస్థితులు సూచిస్తున్నాయి. అయితే, {neg_lead} జాగ్రత్త వహించడం అవసరం."
        elif pos_texts:
            lead = pos_texts[0]
            extra = f" అలాగే తగిన అభివృద్ధి అవకాశాలు ఉన్నాయి." if pos_count > 1 else ""
            synthesized_text = f"{topic} రంగానికి సంబంధించి {lead} శ్రేయస్కరమైన అవకాశాలు సూచిస్తోంది.{extra}"
        elif neg_texts:
            lead = neg_texts[0]
            synthesized_text = f"{topic} అంశంలో {lead} కొన్ని పరిమితులు లేదా పరీక్షా సమయాన్ని సూచిస్తోంది. ప్రణాళికాబద్ధంగా వ్యవహరించడం మంచిది."
        else:
            synthesized_text = f"{topic} రంగానికి సంబంధించి ఫలితాలు సాధారణంగా సమతుల్యంగా ఉంటాయి."

        # Apply Safety Filter
        synthesized_text = SafetyFilter.sanitize_text(synthesized_text)

        return {
            "topic": topic,
            "synthesized_text": synthesized_text,
            "supporting_rules_count": pos_count,
            "contradicting_rules_count": neg_count
        }
