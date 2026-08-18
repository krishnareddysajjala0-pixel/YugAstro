# -*- coding: utf-8 -*-
"""
Core Evaluation Engine for YugAstro Results Engine.
Matches normalized chart context against rule sources, reconciles contradictions,
deduplicates statements, and computes category scores and explainable reasons.
"""

from typing import Dict, List, Any, Optional
from .context import NormalizedChartContext
from .rule_loader import RuleLoader
from .scoring import CategoryScorer, WEIGHTS
from .categories import CATEGORIES, HOUSE_CATEGORY_MAP

class ResultsEngine:
    def __init__(self, rule_loader: Optional[RuleLoader] = None):
        self.rule_loader = rule_loader or RuleLoader.get_instance()
        self.bhava_lord_rules = self.rule_loader.get_bhava_lord_rules()
        self.detailed_meanings = self.rule_loader.get_detailed_bhava_meanings()
        self.astro_constants = self.rule_loader.get_astro_constants()

    def evaluate(self, context: NormalizedChartContext) -> Dict[str, Any]:
        scorers: Dict[str, CategoryScorer] = {cat: CategoryScorer(cat) for cat in CATEGORIES}

        # 1. Evaluate 12 House Lord Placements (12x12 Matrix)
        self._evaluate_house_lord_placements(context, scorers)

        # 2. Evaluate Detailed Bhava Meanings
        self._evaluate_detailed_bhava_meanings(context, scorers)

        # 3. Evaluate Current Dasa & Antardasha
        self._evaluate_dasa_support(context, scorers)

        # 4. Evaluate Transits
        self._evaluate_transits(context, scorers)

        # 5. Evaluate Special Extracted Rules
        self._evaluate_extracted_rules(context, scorers)

        # Aggregate Results
        evaluated_categories = {}
        rule_count = 0
        positive_count = 0
        negative_count = 0
        neutral_count = 0

        for cat_name, scorer in scorers.items():
            res = scorer.get_summary()
            
            # Reconcile contradictions and deduplicate statements for user output
            res["user_summary"] = self._build_user_summary(res)
            
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
            categories = HOUSE_CATEGORY_MAP.get(h_num, ["వ్యక్తిత్వం"])

            rule_entry = self.bhava_lord_rules.get(str(h_num), {}).get(str(p_house), {})
            shubha_text = rule_entry.get("shubha", "").strip() if isinstance(rule_entry, dict) else ""
            paapa_text = rule_entry.get("paapa", "").strip() if isinstance(rule_entry, dict) else ""

            is_favorable = context.is_favorable_planet(lord_planet)

            # Rule match: Shubha
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

            # Rule match: Paapa
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

            categories = HOUSE_CATEGORY_MAP.get(h_num, ["వ్యక్తిత్వం"])
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

    def _evaluate_dasa_support(self, context: NormalizedChartContext, scorers: Dict[str, CategoryScorer]):
        current_dasa = context.current_dasa
        if not current_dasa:
            return

        is_fav = context.dasa_favorable
        weight = WEIGHTS['DASHA_FAVORABLE'] if is_fav else WEIGHTS['DASHA_UNFAVORABLE']

        dasa_reason = {
            "rule_id": f"CURRENT_DASHA_{current_dasa}",
            "source": "yugastro_dasa_engine",
            "dasa": current_dasa,
            "type": "shubha" if is_fav else "paapa",
            "text": f"ప్రస్తుతం జరుగుతున్న {current_dasa} మహాగ్రహ దశ లగ్నమునకు {'అనుకూలమైనది' if is_fav else 'పరీక్షా సమయం/ప్రతికూలమైనది'}.",
            "explanation": f"త్రైత వర్గ సిద్ధాంతం ప్రకారం {current_dasa} దశ లగ్నమునకు {'యోగకారకముగా ఉంది' if is_fav else 'పరిమితులతో పనిచేస్తుంది'}."
        }

        scorers["ప్రస్తుత దశ"].add_reason(dasa_reason, weight)

        if context.current_anthara:
            anthara_reason = {
                "rule_id": f"CURRENT_ANTHARA_{context.current_anthara}",
                "source": "yugastro_dasa_engine",
                "anthara": context.current_anthara,
                "type": "shubha" if is_fav else "paapa",
                "text": f"ప్రస్తుత అంతర్దశ (భుక్తి): {context.current_anthara}",
                "explanation": f"ప్రస్తుతం నడుస్తున్న అంతర్దశ {context.current_anthara}."
            }
            scorers["అంతర్దశ"].add_reason(anthara_reason, 1 if is_fav else -1)

    def _evaluate_transits(self, context: NormalizedChartContext, scorers: Dict[str, CategoryScorer]):
        transit_reason = {
            "rule_id": "GOCHARAM_2026_SATURN_JUPITER",
            "source": "yugastro_transit_engine",
            "type": "shubha" if context.is_guru_party_lagna else "paapa",
            "text": f"2026 శని మరియు గురు గోచార ఫలితాలు లగ్నాధిపతి వర్గము ({'గురు వర్గం' if context.is_guru_party_lagna else 'శని వర్గం'}) ఆధారంగా విశ్లేషించబడ్డాయి.",
            "explanation": f"త్రైత సిద్ధాంత గోచార నియమాల ప్రకారం సరి లగ్నాలకు అనుకూల ఫలితాలు, బేసి లగ్నాలకు పరీక్షా సమయం."
        }
        scorers["గోచారం"].add_reason(transit_reason, 2 if context.is_guru_party_lagna else -1)

    def _evaluate_extracted_rules(self, context: NormalizedChartContext, scorers: Dict[str, CategoryScorer]):
        # Lagna lord impact rule from extracted_rules.txt
        lagna_lord = context.house_lords.get(1, "సూర్యుడు")
        lagna_lord_house = context.lord_placements.get(1, 1)

        rule_reason = {
            "rule_id": "EXTRACTED_LAGNA_LORD_PLACEMENT",
            "source": "extracted_rules.txt",
            "text": f"లగ్నాధిపతి ({lagna_lord}) {lagna_lord_house}వ భావంలో స్థితి పొందడం ద్వారా ఆ భావ కారకత్వాలు వ్యక్తిత్వంతో అనుసంధానించబడతాయి.",
            "explanation": "లగ్నంలో ఏ భావాధిపతి ఉంటే లేదా లగ్నాధిపతి ఏ భావంలో ఉంటే, ఆ భావకారకత్వంతో లగ్న భావం ప్రభావితమవుతుంది."
        }
        scorers["వ్యక్తిత్వం"].add_reason(rule_reason, 1)

    def _build_user_summary(self, category_summary: Dict[str, Any]) -> str:
        pos_reasons = category_summary.get("positive_reasons", [])
        neg_reasons = category_summary.get("negative_reasons", [])

        pos_texts = list(dict.fromkeys([r.get("text", "") for r in pos_reasons if r.get("text")]))
        neg_texts = list(dict.fromkeys([r.get("text", "") for r in neg_reasons if r.get("text")]))

        if pos_texts and neg_texts:
            pos_combined = " ".join(pos_texts[:2])
            neg_combined = " ".join(neg_texts[:2])
            return f"{pos_combined} అయితే, {neg_combined}"
        elif pos_texts:
            return " ".join(pos_texts[:3])
        elif neg_texts:
            return " ".join(neg_texts[:3])
        else:
            return "ఈ విభాగానికి సంబంధించి ఫలితాలు సాధారణంగా సమానంగా ఉంటాయి."
