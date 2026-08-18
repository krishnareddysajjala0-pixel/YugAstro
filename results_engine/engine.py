# -*- coding: utf-8 -*-
"""
RAVAN ASTRO VERSION 5 — Core Interpretation & Evidence Engine.
Creates structured Evidence Objects, calculates net scores, and prints mandatory debug output:
TOPIC | SELECTED_RULE_IDS | POS_CNT | NEG_CNT | POS_SCORE | NEG_SCORE | NET_SCORE | CLASSIFICATION
"""

from typing import Dict, List, Any, Optional
from .context import NormalizedChartContext
from .rule_loader import RuleLoader
from .rule_cleaner import RuleCleaner
from .topic_evidence import TopicEvidenceFilter
from .topic_definitions import TOPIC_DEFINITIONS
from .scoring import CategoryScorer, WEIGHTS
from .categories import CATEGORIES
from .dasha_interpreter import DashaInterpreter
from .transit_interpreter import TransitInterpreter
from .yoga_engine import YogaEngine
from .safety_filter import SafetyFilter
from .synthesizer import ResultSynthesizer

class ResultsEngine:
    def __init__(self, rule_loader: Optional[RuleLoader] = None):
        self.rule_loader = rule_loader or RuleLoader.get_instance()
        raw_matrix = self.rule_loader.get_bhava_lord_rules()
        self.bhava_lord_rules = RuleCleaner.clean_bhava_lord_matrix(raw_matrix)
        self.detailed_meanings = self.rule_loader.get_detailed_bhava_meanings()
        self.astro_constants = self.rule_loader.get_astro_constants()
        self.yoga_engine = YogaEngine(self.rule_loader)

    def evaluate(self, context: NormalizedChartContext) -> Dict[str, Any]:
        scorers: Dict[str, CategoryScorer] = {cat: CategoryScorer(cat) for cat in CATEGORIES}

        # 1. Evaluate House Lord Placements with Strict Relevance Gate
        self._evaluate_house_lord_placements(context, scorers)

        # 2. Evaluate Detailed Bhava Meanings with Strict Relevance Gate
        self._evaluate_detailed_bhava_meanings(context, scorers)

        # 3. Evaluate Dasha & Antardasha
        self._evaluate_dasa_and_antardasha(context, scorers)

        # 4. Evaluate Transits
        self._evaluate_transits(context, scorers)

        # 5. Evaluate Yogas
        yogas = self.yoga_engine.evaluate_yogas(context)
        if yogas:
            for y in yogas:
                reason = {
                    "rule_id": y["id"],
                    "source": y["source"],
                    "type": "shubha",
                    "text": y["positive_result"],
                    "explanation": y["positive_result"]
                }
                scorers["ముఖ్య యోగాలు"].add_reason(reason, 3)

        # Mandatory Debug Table Print
        print("\n===================================================================================================")
        print("RAVAN ASTRO VERSION 5 RESULTS ENGINE CONSOLE DEBUG REPORT")
        print("===================================================================================================")
        print(f"{'TOPIC':<20} | {'SELECTED_RULE_IDS':<25} | {'POS_CNT':<7} | {'NEG_CNT':<7} | {'POS_SCR':<7} | {'NEG_SCR':<7} | {'NET_SCR':<7} | CLASSIFICATION")
        print("---------------------------------------------------------------------------------------------------")

        evaluated_categories = {}
        rule_count = 0
        positive_count = 0
        negative_count = 0
        neutral_count = 0

        for cat_name in CATEGORIES:
            scorer = scorers[cat_name]
            res = scorer.get_summary()

            pos_reasons = res.get("positive_reasons", [])
            neg_reasons = res.get("negative_reasons", [])

            pos_rule_ids = list(dict.fromkeys([r.get("rule_id") for r in pos_reasons if r.get("rule_id")]))
            neg_rule_ids = list(dict.fromkeys([r.get("rule_id") for r in neg_reasons if r.get("rule_id")]))
            all_selected_ids = pos_rule_ids + neg_rule_ids

            syn_info = ResultSynthesizer.synthesize_topic_result(cat_name, pos_reasons, neg_reasons)
            summary_te = syn_info["synthesized_text"]

            t_def = TOPIC_DEFINITIONS.get(cat_name, {})
            t_id = t_def.get("topic_id", cat_name)

            # Build Topic Object matching Internal Data Model
            topic_object = {
                "topic_id": t_id,
                "title_te": cat_name,
                "classification": res["level"],
                "color": res["color"],
                "icon": res["icon"],
                "positive_score": res["positive_score"],
                "negative_score": res["negative_score"],
                "net_score": res["net_score"],
                "score": res["net_score"],
                "summary_te": summary_te,
                "user_summary": summary_te,
                "positive_evidence": pos_reasons,
                "negative_evidence": neg_reasons,
                "all_reasons": pos_reasons + neg_reasons,
                "supporting_rule_ids": pos_rule_ids,
                "contradicting_rule_ids": neg_rule_ids,
                "confidence": "high" if len(all_selected_ids) >= 2 else "medium",
                "dasha_relevance": f"{context.current_dasa} దశ - {context.current_anthara} భుక్తి",
                "transit_relevance": "2026 శని & గురు గోచారం"
            }

            evaluated_categories[cat_name] = topic_object

            rule_ids_str = ",".join(all_selected_ids[:2]) if all_selected_ids else "NONE"
            if len(all_selected_ids) > 2:
                rule_ids_str += f"(+{len(all_selected_ids)-2})"

            print(f"{cat_name:<20} | {rule_ids_str:<25} | {len(pos_reasons):<7} | {len(neg_reasons):<7} | {res['positive_score']:<7} | {res['negative_score']:<7} | {res['net_score']:<7} | {res['level']}")

            cat_rules = len(all_selected_ids)
            rule_count += cat_rules
            if res["net_score"] >= 4:
                positive_count += 1
            elif res["net_score"] <= -3:
                negative_count += 1
            else:
                neutral_count += 1

        print("===================================================================================================\n")

        return {
            "categories": evaluated_categories,
            "yogas": yogas,
            "meta": {
                "rule_count": rule_count,
                "positive_count": positive_count,
                "negative_count": negative_count,
                "neutral_count": neutral_count
            }
        }

    def _evaluate_house_lord_placements(self, context: NormalizedChartContext, scorers: Dict[str, CategoryScorer]):
        for h_num in range(1, 13):
            p_house = context.lord_placements.get(h_num, 1)
            lord_planet = context.house_lords.get(h_num, "సూర్యుడు")

            rule_entry = self.bhava_lord_rules.get(str(h_num), {}).get(str(p_house), {})
            shubha_text = rule_entry.get("shubha", "")
            paapa_text = rule_entry.get("paapa", "")

            is_favorable = context.is_favorable_planet(lord_planet)

            for topic in CATEGORIES:
                rule_dict = {"text": shubha_text or paapa_text, "explanation": shubha_text or paapa_text}
                if not TopicEvidenceFilter.is_relevant(rule_dict, topic, h_num, lord_planet):
                    continue

                if shubha_text:
                    weight = WEIGHTS['BHAVA_LORD_SHUBHA'] if is_favorable else 2
                    reason = {
                        "rule_id": f"BHAVA_LORD_{h_num}_{p_house}_SHUBHA",
                        "topic_id": TOPIC_DEFINITIONS.get(topic, {}).get("topic_id", topic),
                        "source": "bhava_lord_rules.json",
                        "house": h_num,
                        "planet": lord_planet,
                        "lord": lord_planet,
                        "placement": p_house,
                        "polarity": "positive",
                        "strength": weight,
                        "type": "shubha",
                        "text": shubha_text,
                        "explanation": f"{h_num}వ భావాధిపతి ({lord_planet}) {p_house}వ భావ స్థితి: {shubha_text}"
                    }
                    scorers[topic].add_reason(reason, weight)

                if paapa_text:
                    weight = WEIGHTS['BHAVA_LORD_PAAPA'] if not is_favorable else -2
                    reason = {
                        "rule_id": f"BHAVA_LORD_{h_num}_{p_house}_PAAPA",
                        "topic_id": TOPIC_DEFINITIONS.get(topic, {}).get("topic_id", topic),
                        "source": "bhava_lord_rules.json",
                        "house": h_num,
                        "planet": lord_planet,
                        "lord": lord_planet,
                        "placement": p_house,
                        "polarity": "negative",
                        "strength": abs(weight),
                        "type": "paapa",
                        "text": paapa_text,
                        "explanation": f"{h_num}వ భావాధిపతి ({lord_planet}) {p_house}వ భావ స్థితి (హెచ్చరిక): {paapa_text}"
                    }
                    scorers[topic].add_reason(reason, weight)

    def _evaluate_detailed_bhava_meanings(self, context: NormalizedChartContext, scorers: Dict[str, CategoryScorer]):
        for h_num in range(1, 13):
            meaning_entry = self.detailed_meanings.get(str(h_num), {})
            if not meaning_entry:
                continue

            title = meaning_entry.get("title", f"{h_num}వ భావం")
            shubha_text = meaning_entry.get("shubha", "").strip()
            paapa_text = meaning_entry.get("paapa", "").strip()

            lord = context.house_lords.get(h_num, "")
            is_favorable = context.is_favorable_planet(lord) if lord else True

            for topic in CATEGORIES:
                rule_dict = {"text": shubha_text or paapa_text, "explanation": shubha_text or paapa_text}
                if not TopicEvidenceFilter.is_relevant(rule_dict, topic, h_num, lord):
                    continue

                if is_favorable and shubha_text:
                    reason = {
                        "rule_id": f"BHAVA_MEANING_{h_num}_SHUBHA",
                        "topic_id": TOPIC_DEFINITIONS.get(topic, {}).get("topic_id", topic),
                        "source": "detailed_bhava_meanings.json",
                        "house": h_num,
                        "planet": lord,
                        "polarity": "positive",
                        "strength": WEIGHTS['BHAVA_MEANING_SHUBHA'],
                        "type": "shubha",
                        "text": shubha_text,
                        "explanation": f"{title} శుభ స్థితి: {shubha_text}"
                    }
                    scorers[topic].add_reason(reason, WEIGHTS['BHAVA_MEANING_SHUBHA'])
                elif not is_favorable and paapa_text:
                    reason = {
                        "rule_id": f"BHAVA_MEANING_{h_num}_PAAPA",
                        "topic_id": TOPIC_DEFINITIONS.get(topic, {}).get("topic_id", topic),
                        "source": "detailed_bhava_meanings.json",
                        "house": h_num,
                        "planet": lord,
                        "polarity": "negative",
                        "strength": abs(WEIGHTS['BHAVA_MEANING_PAAPA']),
                        "type": "paapa",
                        "text": paapa_text,
                        "explanation": f"{title} హెచ్చరిక: {paapa_text}"
                    }
                    scorers[topic].add_reason(reason, WEIGHTS['BHAVA_MEANING_PAAPA'])

    def _evaluate_dasa_and_antardasha(self, context: NormalizedChartContext, scorers: Dict[str, CategoryScorer]):
        dasa_reason = DashaInterpreter.interpret_mahadasha(context)
        weight = WEIGHTS['DASHA_FAVORABLE'] if dasa_reason.get("is_favorable") else WEIGHTS['DASHA_UNFAVORABLE']
        scorers["ప్రస్తుత దశ"].add_reason(dasa_reason, weight)

        anthara_reason = DashaInterpreter.interpret_antardasha(context)
        weight_a = 1 if anthara_reason.get("is_favorable") else -1
        scorers["అంతర్దశ"].add_reason(anthara_reason, weight_a)

    def _evaluate_transits(self, context: NormalizedChartContext, scorers: Dict[str, CategoryScorer]):
        transit_reasons = TransitInterpreter.interpret_transits(context)
        for tr_r in transit_reasons:
            w = 2 if tr_r.get("type") == "shubha" else -1
            scorers["గోచారం"].add_reason(tr_r, w)
