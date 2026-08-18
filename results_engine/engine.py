# -*- coding: utf-8 -*-
"""
Core Evaluation Engine for YugAstro Results Engine.
Implements the 13-Step Pipeline: Rule database cleanup, Topic Mapping,
Duplicate Removal, Positive/Negative Synthesis, Scoring, Dasha, Antardasha,
Transit, Yoga Engine, and Safety Filter.
"""

from typing import Dict, List, Any, Optional
from .context import NormalizedChartContext
from .rule_loader import RuleLoader
from .rule_cleaner import RuleCleaner
from .topic_rules import TopicMapper
from .scoring import CategoryScorer, WEIGHTS
from .categories import CATEGORIES, HOUSE_CATEGORY_MAP
from .dasha_interpreter import DashaInterpreter
from .transit_interpreter import TransitInterpreter
from .yoga_engine import YogaEngine
from .safety_filter import SafetyFilter

class ResultsEngine:
    def __init__(self, rule_loader: Optional[RuleLoader] = None):
        self.rule_loader = rule_loader or RuleLoader.get_instance()
        raw_matrix = self.rule_loader.get_bhava_lord_rules()
        # STEP 1: Rule Database Cleanup
        self.bhava_lord_rules = RuleCleaner.clean_bhava_lord_matrix(raw_matrix)
        self.detailed_meanings = self.rule_loader.get_detailed_bhava_meanings()
        self.astro_constants = self.rule_loader.get_astro_constants()
        self.yoga_engine = YogaEngine(self.rule_loader)

    def evaluate(self, context: NormalizedChartContext) -> Dict[str, Any]:
        scorers: Dict[str, CategoryScorer] = {cat: CategoryScorer(cat) for cat in CATEGORIES}

        # STEP 2: Rule -> Topic Mapping & Evaluation
        self._evaluate_house_lord_placements(context, scorers)
        self._evaluate_detailed_bhava_meanings(context, scorers)

        # STEP 6 & STEP 7: Dasha & Antardasha Interpretation
        self._evaluate_dasa_and_antardasha(context, scorers)

        # STEP 8: Transit Interpretation
        self._evaluate_transits(context, scorers)

        # STEP 9: Yoga Engine Evaluation
        yogas = self.yoga_engine.evaluate_yogas(context)
        for y in yogas:
            reason = {
                "rule_id": y["rule_id"],
                "source": y["source"],
                "type": "shubha",
                "text": y["text"],
                "explanation": y["explanation"]
            }
            scorers["ముఖ్య యోగాలు"].add_reason(reason, 3)

        # STEP 3, 4, 5, 10: Deduplication, Synthesis, Scoring, Safety Filter
        evaluated_categories = {}
        rule_count = 0
        positive_count = 0
        negative_count = 0
        neutral_count = 0

        for cat_name, scorer in scorers.items():
            res = scorer.get_summary()

            # STEP 3 & STEP 4: Deduplicate and Synthesize Telugu summary
            res["user_summary"] = self._build_user_summary(res)

            # STEP 10: Safety Filter Application
            res["user_summary"] = SafetyFilter.sanitize_text(res["user_summary"])

            evaluated_categories[cat_name] = res

            cat_rules = len(res["all_reasons"])
            rule_count += cat_rules
            if res["score"] >= 2:
                positive_count += 1
            elif res["score"] <= -2:
                negative_count += 1
            else:
                neutral_count += 1

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
            categories = TopicMapper.get_categories_for_house(h_num)

            rule_entry = self.bhava_lord_rules.get(str(h_num), {}).get(str(p_house), {})
            shubha_text = rule_entry.get("shubha", "")
            paapa_text = rule_entry.get("paapa", "")

            is_favorable = context.is_favorable_planet(lord_planet)

            if shubha_text:
                weight = WEIGHTS['BHAVA_LORD_SHUBHA'] if is_favorable else 1
                reason = {
                    "rule_id": f"BHAVA_LORD_{h_num}_{p_house}_SHUBHA",
                    "source": "bhava_lord_rules.json",
                    "house": h_num,
                    "lord": lord_planet,
                    "placement": p_house,
                    "type": "shubha",
                    "text": shubha_text,
                    "explanation": f"{h_num}వ భావాధిపతి ({lord_planet}) {p_house}వ భావంలో ఉన్నందున (శుభ ఫలితం): {shubha_text}"
                }
                for cat in categories:
                    scorers[cat].add_reason(reason, weight)

            if paapa_text:
                weight = WEIGHTS['BHAVA_LORD_PAAPA'] if not is_favorable else -1
                reason = {
                    "rule_id": f"BHAVA_LORD_{h_num}_{p_house}_PAAPA",
                    "source": "bhava_lord_rules.json",
                    "house": h_num,
                    "lord": lord_planet,
                    "placement": p_house,
                    "type": "paapa",
                    "text": paapa_text,
                    "explanation": f"{h_num}వ భావాధిపతి ({lord_planet}) {p_house}వ భావంలో ఉన్నందున (ప్రతికూల సూచన): {paapa_text}"
                }
                for cat in categories:
                    scorers[cat].add_reason(reason, weight)

    def _evaluate_detailed_bhava_meanings(self, context: NormalizedChartContext, scorers: Dict[str, CategoryScorer]):
        for h_num in range(1, 13):
            meaning_entry = self.detailed_meanings.get(str(h_num), {})
            if not meaning_entry:
                continue

            categories = TopicMapper.get_categories_for_house(h_num)
            title = meaning_entry.get("title", f"{h_num}వ భావం")
            shubha_text = meaning_entry.get("shubha", "").strip()
            paapa_text = meaning_entry.get("paapa", "").strip()

            lord = context.house_lords.get(h_num, "")
            is_favorable = context.is_favorable_planet(lord) if lord else True

            if is_favorable and shubha_text:
                reason = {
                    "rule_id": f"BHAVA_MEANING_{h_num}_SHUBHA",
                    "source": "detailed_bhava_meanings.json",
                    "house": h_num,
                    "type": "shubha",
                    "text": shubha_text,
                    "explanation": f"{title} శుభ స్థితి: {shubha_text}"
                }
                for cat in categories:
                    scorers[cat].add_reason(reason, WEIGHTS['BHAVA_MEANING_SHUBHA'])
            elif not is_favorable and paapa_text:
                reason = {
                    "rule_id": f"BHAVA_MEANING_{h_num}_PAAPA",
                    "source": "detailed_bhava_meanings.json",
                    "house": h_num,
                    "type": "paapa",
                    "text": paapa_text,
                    "explanation": f"{title} ప్రతికూల సూచన: {paapa_text}"
                }
                for cat in categories:
                    scorers[cat].add_reason(reason, WEIGHTS['BHAVA_MEANING_PAAPA'])

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

    def _build_user_summary(self, category_summary: Dict[str, Any]) -> str:
        pos_reasons = category_summary.get("positive_reasons", [])
        neg_reasons = category_summary.get("negative_reasons", [])

        # STEP 3: Deduplicate identical statements
        pos_texts = list(dict.fromkeys([r.get("text", "") for r in pos_reasons if r.get("text")]))
        neg_texts = list(dict.fromkeys([r.get("text", "") for r in neg_reasons if r.get("text")]))

        # STEP 4: Positive/Negative Synthesis
        if pos_texts and neg_texts:
            pos_combined = " ".join(pos_texts[:2])
            neg_combined = " ".join(neg_texts[:2])
            return f"{pos_combined} అయితే, {neg_combined}"
        elif pos_texts:
            return " ".join(pos_texts[:3])
        elif neg_texts:
            return " ".join(neg_texts[:3])
        else:
            return "ఈ విభాగానికి సంబంధించి ఫలితాలు సాధారణంగా సమతుల్యంగా ఉంటాయి."
