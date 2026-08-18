# -*- coding: utf-8 -*-
"""
YugAstro Results Engine Package.
Automatic Telugu Jaataka Results Engine built on top of 12-Planet Tritha Siddhantha calculations.
"""

from typing import Dict, Any, Optional
from .context import NormalizedChartContext
from .engine import ResultsEngine
from .report_builder import ReportBuilder

_engine_instance: Optional[ResultsEngine] = None

def get_results_engine() -> ResultsEngine:
    global _engine_instance
    if _engine_instance is None:
        _engine_instance = ResultsEngine()
    return _engine_instance

def evaluate_kundali_results(data: Dict[str, Any], dasha_info: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """
    Main entry point for generating Jathaka Results report.
    Consumes output of get_kundali_data() and get_dasha_info().
    Returns structured report dictionary.
    """
    context = NormalizedChartContext(data, dasha_info)
    engine = get_results_engine()
    evaluated = engine.evaluate(context)
    report = ReportBuilder.build_report(context, evaluated)
    return report

__all__ = [
    "NormalizedChartContext",
    "ResultsEngine",
    "ReportBuilder",
    "evaluate_kundali_results",
    "get_results_engine"
]
