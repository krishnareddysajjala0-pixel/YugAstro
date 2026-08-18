# -*- coding: utf-8 -*-
"""
RuleLoader for YugAstro Results Engine.
Cached loading and accessor methods for JSON and text rule files.
"""

import os
import json
from typing import Dict, List, Any, Optional

class RuleLoader:
    _instance: Optional['RuleLoader'] = None
    _cache: Dict[str, Any] = {}

    def __init__(self, base_dir: Optional[str] = None):
        if base_dir is None:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.base_dir = base_dir

    @classmethod
    def get_instance(cls, base_dir: Optional[str] = None) -> 'RuleLoader':
        if cls._instance is None:
            cls._instance = RuleLoader(base_dir)
        return cls._instance

    def _get_path(self, filename: str) -> str:
        return os.path.join(self.base_dir, filename)

    def load_json(self, filename: str) -> Dict[str, Any]:
        if filename in self._cache:
            return self._cache[filename]

        path = self._get_path(filename)
        if not os.path.exists(path):
            print(f"[RuleLoader WARNING] File not found: {path}")
            return {}

        try:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self._cache[filename] = data
                return data
        except Exception as e:
            print(f"[RuleLoader ERROR] Failed to load {filename}: {e}")
            return {}

    def load_text_lines(self, filename: str) -> List[str]:
        if filename in self._cache:
            return self._cache[filename]

        path = self._get_path(filename)
        if not os.path.exists(path):
            print(f"[RuleLoader WARNING] File not found: {path}")
            return []

        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                self._cache[filename] = lines
                return lines
        except Exception as e:
            print(f"[RuleLoader ERROR] Failed to load {filename}: {e}")
            return []

    def get_bhava_lord_rules(self) -> Dict[str, Any]:
        """Returns 12x12 matrix from bhava_lord_rules.json."""
        return self.load_json("bhava_lord_rules.json")

    def get_detailed_bhava_meanings(self) -> Dict[str, Any]:
        """Returns detailed house meanings from detailed_bhava_meanings.json."""
        return self.load_json("detailed_bhava_meanings.json")

    def get_astro_constants(self) -> Dict[str, Any]:
        """Returns constants from astro_constants.json."""
        return self.load_json("astro_constants.json")

    def get_extracted_rules(self) -> List[str]:
        """Returns lines from extracted_rules.txt."""
        return self.load_text_lines("extracted_rules.txt")

    def get_qa_rules(self) -> List[str]:
        """Returns lines from astro_qa_rules.txt."""
        return self.load_text_lines("astro_qa_rules.txt")
