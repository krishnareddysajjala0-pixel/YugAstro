# -*- coding: utf-8 -*-
"""
STEP 1: Rule Database Cleanup
Cleans, normalizes, and sanitizes rule texts and data structures.
"""

import re
from typing import Dict, Any, List

class RuleCleaner:
    @staticmethod
    def clean_text(text: str) -> str:
        if not text:
            return ""
        # Strip HTML tags
        clean = re.sub(r'<[^>]+>', '', text)
        # Normalize whitespace
        clean = re.sub(r'\s+', ' ', clean).strip()
        # Remove redundant punctuation
        clean = clean.replace('..', '.').replace(',,', ',')
        return clean

    @staticmethod
    def clean_rule_entry(rule_entry: Dict[str, Any]) -> Dict[str, str]:
        if not isinstance(rule_entry, dict):
            return {"shubha": "", "paapa": ""}

        shubha = RuleCleaner.clean_text(str(rule_entry.get("shubha", "")))
        paapa = RuleCleaner.clean_text(str(rule_entry.get("paapa", "")))
        return {"shubha": shubha, "paapa": paapa}

    @staticmethod
    def clean_bhava_lord_matrix(matrix: Dict[str, Any]) -> Dict[str, Dict[str, Dict[str, str]]]:
        cleaned_matrix = {}
        for h_str, h_dict in matrix.items():
            if not isinstance(h_dict, dict):
                continue
            cleaned_h = {}
            for p_str, p_entry in h_dict.items():
                cleaned_h[p_str] = RuleCleaner.clean_rule_entry(p_entry)
            cleaned_matrix[h_str] = cleaned_h
        return cleaned_matrix
