# -*- coding: utf-8 -*-
"""
Topic-Specific Telugu Synthesizer Engine.
Prevents generic paragraph reuse by synthesizing evidence specific to each topic.
"""

from typing import Dict, Any, List
from .safety_filter import SafetyFilter
from .topic_definitions import TOPIC_DEFINITIONS

class ResultSynthesizer:
    @staticmethod
    def synthesize_topic_result(topic: str, pos_reasons: List[Dict[str, Any]], neg_reasons: List[Dict[str, Any]]) -> Dict[str, Any]:
        t_def = TOPIC_DEFINITIONS.get(topic, {})
        title_te = t_def.get("title_te", topic)

        pos_texts = list(dict.fromkeys([r.get("text", "").strip() for r in pos_reasons if r.get("text")]))
        neg_texts = list(dict.fromkeys([r.get("text", "").strip() for r in neg_reasons if r.get("text")]))

        pos_count = len(pos_reasons)
        neg_count = len(neg_reasons)

        if pos_texts and neg_texts:
            pos_lead = pos_texts[0]
            neg_lead = neg_texts[0]
            synthesized_text = f"మీ {title_te} జాతక స్థానమున {pos_lead} అనుకూల ఫలితాలను అందిస్తుండగా, {neg_lead} హెచ్చరిస్తోంది."
        elif pos_texts:
            lead = pos_texts[0]
            synthesized_text = f"మీ {title_te} స్థాన బలము: {lead} ద్వార యోగకారక అవకాశాలు సిద్ధస్తాయి."
        elif neg_texts:
            lead = neg_texts[0]
            synthesized_text = f"మీ {title_te} స్థానమున {lead} కొంత పరీక్షా సమయాన్ని చూపుతోంది; ప్రణాళికతో ముందడుగు వేయాలి."
        else:
            t_id = t_def.get("topic_id", topic)
            if t_id == "education":
                synthesized_text = "మీ విద్య స్థానము (4, 5వ భావములు) నందు అభ్యాసం మరియు చదువులకు అనుకూలమైన సాధారణ ప్రభావాలు నిలకడగా ఉన్నాయి."
            elif t_id == "intelligence":
                synthesized_text = "మీ మేధస్సు స్థానము (5వ భావం) నందు బుద్ధికుశలత మరియు జ్ఞాపకశక్తికి శోభన సమతుల్యం నెలకొంది."
            elif t_id == "enemies":
                synthesized_text = "మీ శత్రు వర్గ స్థానము (6వ భావం) నందు విరోధుల ప్రభావం నివారించబడి శాంతి వాతావరణం నెలకొంది."
            elif t_id == "marriage":
                synthesized_text = "మీ వివాహ స్థానము (7వ భావం) నందు పరిణయం మరియు కల్యాణ అవకాశాలు సాధారణ సమతులాన్ని చూపుతున్నాయి."
            elif t_id == "health":
                synthesized_text = "మీ ఆరోగ్య స్థానము (1, 6వ భావములు) నందు దేహకాంతి మరియు రోగనిరోధక శక్తి సమతుల్యంగా ఉన్నాయి."
            elif t_id == "home":
                synthesized_text = "మీ గృహ స్థానము (4వ భావం) నందు నివాససౌఖ్యం మరియు కుటుంబ వాతావరణం ప్రశాంతంగా నిలిచింది."
            elif t_id == "vehicle":
                synthesized_text = "మీ వాహన స్థానము (4వ భావం) నందు వాహన యోగం మరియు ప్రయాణ సౌఖ్యం సమతుల్యంగా ఉన్నాయి."
            elif t_id == "property":
                synthesized_text = "మీ స్థిరాస్తి స్థానము (4వ భావం) నందు భూవసతి మరియు స్థలాస్తి అవకాశాలు సాధారణంగా నిలిచాయి."
            elif t_id == "foreign_travel":
                synthesized_text = "మీ విదేశీ ప్రయాణ స్థానము (9, 12వ భావములు) నందు అపరిచిత ప్రదేశాలు మరియు విదేశ వాస యోగాలు సాధారణ స్థితిలో ఉన్నాయి."
            elif t_id == "pilgrimage":
                synthesized_text = "మీ తీర్థయాత్ర స్థానము (9వ భావం) నందు పుణ్యక్షేత్ర సందర్శనం మరియు దైవ దర్శన భాగ్యం ప్రశాంతంగా సిద్ధస్తోంది."
            elif t_id == "spirituality":
                synthesized_text = "మీ ఆధ్యాత్మిక స్థానము (9, 12వ భావములు) నందు సాధన మరియు ఉపాసనా దృష్టి సమతుల్యంగా ఉంది."
            else:
                kws = ", ".join(t_def.get("keywords", [])[:2])
                synthesized_text = f"మీ {title_te} విభాగానికి ({kws}) సంబంధించి గ్రహ స్థితులు సమతుల్యమైన ఫలితాలను అందిస్తున్నాయి."

        synthesized_text = SafetyFilter.sanitize_text(synthesized_text)

        return {
            "topic": topic,
            "synthesized_text": synthesized_text,
            "supporting_rules_count": pos_count,
            "contradicting_rules_count": neg_count
        }
