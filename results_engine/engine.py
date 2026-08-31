# -*- coding: utf-8 -*-
"""
Core Evaluation Engine for RAVAN ASTRO Results Engine (Strict Timeastro Rules Integration).
Enforces exact Timeastro rule database (bhava_lord_rules.json, detailed_bhava_meanings.json,
astro_constants.json, and Timeastro planetary rules) with strict topic relevance.
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

        # 1. Evaluate House Lord Placements (Timeastro bhava_lord_rules.json)
        self._evaluate_house_lord_placements(context, scorers)

        # 2. Evaluate Detailed Bhava Meanings (Timeastro detailed_bhava_meanings.json)
        self._evaluate_detailed_bhava_meanings(context, scorers)

        # 3. Evaluate Specific Timeastro Planetary Rules
        self._evaluate_timeastro_planetary_rules(context, scorers)

        # 4. Evaluate Dasha & Antardasha
        self._evaluate_dasa_and_antardasha(context, scorers)

        # 5. Evaluate Transits
        self._evaluate_transits(context, scorers)

        # 6. Evaluate Yogas
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

        # Build Topic Objects and Console Debug Report
        evaluated_categories = {}
        rule_count = 0
        positive_count = 0
        negative_count = 0
        neutral_count = 0

        try:
            print("\n==========================================================================================")
            print("RAVAN ASTRO VERSION 3 RESULTS ENGINE CONSOLE DEBUG REPORT (TIMEASTRO STRICT RULES)")
            print("==========================================================================================")
            print(f"{'TOPIC':<24} | {'POSITIVE RULES':<14} | {'NEGATIVE RULES':<14} | {'SCORE':<6} | STATUS")
            print("------------------------------------------------------------------------------------------")
        except Exception:
            pass

        for cat_name in CATEGORIES:
            scorer = scorers[cat_name]
            res = scorer.get_summary()
            pos_reasons = res.get("positive_reasons", [])
            neg_reasons = res.get("negative_reasons", [])

            pos_rule_ids = list(dict.fromkeys([r.get("rule_id") for r in pos_reasons if r.get("rule_id")]))
            neg_rule_ids = list(dict.fromkeys([r.get("rule_id") for r in neg_reasons if r.get("rule_id")]))

            syn_info = ResultSynthesizer.synthesize_topic_result(cat_name, pos_reasons, neg_reasons)
            summary_te = syn_info["synthesized_text"]

            t_def = TOPIC_DEFINITIONS.get(cat_name, {})
            t_id = t_def.get("topic_id", cat_name)

            topic_object = {
                "topic_id": t_id,
                "title_te": cat_name,
                "classification": res["level"],
                "color": res["color"],
                "icon": res["icon"],
                "score": res["score"],
                "summary_te": summary_te,
                "user_summary": summary_te,
                "positive_evidence": pos_reasons,
                "negative_evidence": neg_reasons,
                "all_reasons": pos_reasons + neg_reasons,
                "supporting_rule_ids": pos_rule_ids,
                "contradicting_rule_ids": neg_rule_ids,
                "confidence": "high" if (len(pos_rule_ids) + len(neg_rule_ids)) >= 2 else "medium",
                "dasha_relevance": f"{context.current_dasa} దశ - {context.current_anthara} భుక్తి",
                "transit_relevance": "2026 శని & గురు గోచారం"
            }

            evaluated_categories[cat_name] = topic_object

            try:
                print(f"{cat_name:<24} | {len(pos_rule_ids):<14} | {len(neg_rule_ids):<14} | {res['score']:<6} | {res['level']}")
            except Exception:
                pass

            cat_rules = len(pos_rule_ids) + len(neg_rule_ids)
            rule_count += cat_rules
            if res["score"] >= 2:
                positive_count += 1
            elif res["score"] <= -2:
                negative_count += 1
            else:
                neutral_count += 1

        try:
            print("==========================================================================================\n")
        except Exception:
            pass

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
                    weight = WEIGHTS['BHAVA_LORD_SHUBHA'] if is_favorable else 1
                    reason = {
                        "rule_id": f"BHAVA_LORD_{h_num}_{p_house}_SHUBHA",
                        "source": "bhava_lord_rules.json",
                        "house": h_num,
                        "lord": lord_planet,
                        "placement": p_house,
                        "type": "shubha",
                        "text": shubha_text,
                        "explanation": f"{h_num}వ భావాధిపతి ({lord_planet}) {p_house}వ భావ స్థితి: {shubha_text}"
                    }
                    scorers[topic].add_reason(reason, weight)

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
                        "source": "detailed_bhava_meanings.json",
                        "house": h_num,
                        "type": "shubha",
                        "text": shubha_text,
                        "explanation": f"{title} శుభ స్థితి: {shubha_text}"
                    }
                    scorers[topic].add_reason(reason, WEIGHTS['BHAVA_MEANING_SHUBHA'])
                elif not is_favorable and paapa_text:
                    reason = {
                        "rule_id": f"BHAVA_MEANING_{h_num}_PAAPA",
                        "source": "detailed_bhava_meanings.json",
                        "house": h_num,
                        "type": "paapa",
                        "text": paapa_text,
                        "explanation": f"{title} హెచ్చరిక: {paapa_text}"
                    }
                    scorers[topic].add_reason(reason, WEIGHTS['BHAVA_MEANING_PAAPA'])

    def _evaluate_timeastro_planetary_rules(self, context: NormalizedChartContext, scorers: Dict[str, CategoryScorer]):
        """Evaluates exact Timeastro planetary scenario rules across the 12 houses."""
        for p_name, p_house in context.planet_houses.items():
            is_fav = context.is_favorable_planet(p_name)

            # 4th House Rules
            if p_house == 4:
                if "సూర్యుడు" in p_name:
                    txt = "సూర్యుడు 4వ లగ్నములో ఉండటమువలన మీకు పై అంతస్థు భవనములు కట్టించు ప్రేరణ చేయును." if is_fav else "సూర్యుడు శత్రుగ్రహమై 4వ లగ్నములో ఉన్నందున గృహ సుఖములు లోపించును."
                    reason = {"rule_id": f"TIMEASTRO_P_4_SUN_{'FAV' if is_fav else 'UNFAV'}", "source": "Timeastro Rules", "house": 4, "type": "shubha" if is_fav else "paapa", "text": txt, "explanation": txt}
                    if is_fav: scorers["గృహం"].add_reason(reason, 2)
                    else: scorers["గృహం"].add_reason(reason, -2)

                if "రాహు" in p_name:
                    txt = "దొంగవృత్తి లేదా దోపిడీల ద్వారా లక్షలు సంపాదించుట, సమాజములో భయంతో కూడిన గౌరవము." if is_fav else "దొంగతనములలో దొరికిపోవుట, పోలీస్ కేసులు, జైలు జీవితము అనుభవించవలసి రావచ్చు."
                    reason = {"rule_id": f"TIMEASTRO_P_4_RAHU_{'FAV' if is_fav else 'UNFAV'}", "source": "Timeastro Rules", "house": 4, "type": "shubha" if is_fav else "paapa", "text": txt, "explanation": txt}
                    if is_fav: scorers["స్థిరాస్తి"].add_reason(reason, 2)
                    else: scorers["గృహం"].add_reason(reason, -2)

            # 7th House Rules
            if p_house == 7:
                if "శుక్రుడు" in p_name:
                    txt = "అందమైన, అనుకూలమైన భార్య/భర్త లభించును. ఆమె/అతని వలన మనశ్శాంతి, సుఖము ఉండును." if is_fav else "కళత్రము వలన కష్టములు, మనఃశ్శాంతి లోపించును."
                    reason = {"rule_id": f"TIMEASTRO_P_7_VENUS_{'FAV' if is_fav else 'UNFAV'}", "source": "Timeastro Rules", "house": 7, "type": "shubha" if is_fav else "paapa", "text": txt, "explanation": txt}
                    scorers["వివాహం"].add_reason(reason, 2 if is_fav else -2)
                if "కుజుడు" in p_name and not is_fav:
                    txt = "యుక్తవయస్సులో వివాహము ఆలస్యమగును."
                    reason = {"rule_id": "TIMEASTRO_P_7_MARS_UNFAV", "source": "Timeastro Rules", "house": 7, "type": "paapa", "text": txt, "explanation": txt}
                    scorers["వివాహం"].add_reason(reason, -2)

            # 3rd House Rules
            if p_house == 3:
                if "గురు" in p_name:
                    txt = "బంగారము లేదా ధనము ఏదో ఒక విధంగా లభ్యమగుట (వ్యాపార లాభం లేదా అదృష్టం)." if is_fav else "ఉన్న బంగారమును కూడా అమ్మవలసిన పరిస్థితులు ఏర్పడును."
                    reason = {"rule_id": f"TIMEASTRO_P_3_JUPITER_{'FAV' if is_fav else 'UNFAV'}", "source": "Timeastro Rules", "house": 3, "type": "shubha" if is_fav else "paapa", "text": txt, "explanation": txt}
                    scorers["ధనం"].add_reason(reason, 2 if is_fav else -2)

            # 10th House Rules
            if p_house == 10:
                if "సూర్యుడు" in p_name or "చంద్రుడు" in p_name:
                    txt = "ప్రభుత్వ ఉన్నత ఉద్యోగి (కలెక్టర్) లేదా మంత్రి పదవి యోగం."
                    reason = {"rule_id": "TIMEASTRO_P_10_SUN_MOON", "source": "Timeastro Rules", "house": 10, "type": "shubha", "text": txt, "explanation": txt}
                    scorers["అధికార స్థానం"].add_reason(reason, 3)
                    scorers["ఉద్యోగం"].add_reason(reason, 2)

            # 5th House Rules
            if p_house == 5:
                if "కేతు" in p_name:
                    txt = "దేవుని వైపు చింత, హేతువాదిక జ్ఞానము, సత్యాన్వేషణలో దైవభక్తి పెరగడము." if is_fav else "దైవజ్ఞానము మీద ఆసక్తి ఉండదు, పూర్తిగా ప్రపంచ జ్ఞానములోనే ఉండిపోవుట."
                    reason = {"rule_id": f"TIMEASTRO_P_5_KETU_{'FAV' if is_fav else 'UNFAV'}", "source": "Timeastro Rules", "house": 5, "type": "shubha" if is_fav else "paapa", "text": txt, "explanation": txt}
                    scorers["ఆధ్యాత్మికత"].add_reason(reason, 2 if is_fav else -2)

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
