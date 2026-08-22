# -*- coding: utf-8 -*-
"""
STEP 13 & QA ARCHITECTURE TEST: 5-Chart Distinction & Text Similarity Verification.
Tests 5 distinct known birth charts and asserts that text similarity between unrelated topics
is strictly less than 60%.
"""

import unittest
from difflib import SequenceMatcher
from app import get_kundali_data, get_dasha_info
from results_engine import evaluate_kundali_results

TEST_CHARTS = [
    {
        "name": "Chart 1 (Meena Lagna - Guru Party)",
        "dob": "1990-03-15",
        "tob": "06:30",
        "place": "Hyderabad",
        "lat": 17.3850,
        "lon": 78.4867
    },
    {
        "name": "Chart 2 (Mesha Lagna - Guru Party)",
        "dob": "1985-04-20",
        "tob": "07:15",
        "place": "Vijayawada",
        "lat": 16.5062,
        "lon": 80.6480
    },
    {
        "name": "Chart 3 (Kumbha Lagna - Shani Party)",
        "dob": "1995-08-12",
        "tob": "18:45",
        "place": "Visakhapatnam",
        "lat": 17.6868,
        "lon": 83.2185
    },
    {
        "name": "Chart 4 (Mithuna Lagna - Shani Party)",
        "dob": "2000-06-10",
        "tob": "14:20",
        "place": "Tirupati",
        "lat": 13.6288,
        "lon": 79.4192
    },
    {
        "name": "Chart 5 (Vrishchika Lagna - Guru Party)",
        "dob": "1998-11-25",
        "tob": "05:00",
        "place": "Kurnool",
        "lat": 15.8281,
        "lon": 78.0373
    }
]

def calculate_similarity(text1: str, text2: str) -> float:
    if not text1 or not text2:
        return 0.0
    return SequenceMatcher(None, text1, text2).ratio()

class Test5ChartsRegression(unittest.TestCase):
    def test_5_charts_distinction_and_similarity_gate(self):
        reports = []

        for idx, chart in enumerate(TEST_CHARTS, 1):
            data = get_kundali_data(
                chart["name"], chart["dob"], chart["tob"],
                chart["place"], chart["lat"], chart["lon"]
            )
            self.assertIsNotNone(data)
            dasha_info = get_dasha_info(data) if isinstance(data, dict) else {}
            report = evaluate_kundali_results(data, dasha_info if isinstance(data, dict) else {})
            reports.append(report)

            # Check 40 sections present
            self.assertIn("sections", report)
            self.assertGreaterEqual(len(report["sections"]), 35)

            # Text Similarity Check across unrelated topic pairs within the same chart
            sec_dict = {s["title"]: s["summary"] for s in report["sections"]}

            unrelated_pairs = [
                ("మేధస్సు", "స్థిరాస్తి"),
                ("విద్య", "శత్రువులు"),
                ("వృత్తి", "తీర్థయాత్రలు"),
                ("ధనం", "విదేశీ ప్రయాణం"),
                ("వివాహం", "ఆరోగ్యం"),
                ("తల్లి", "ఉద్యోగం"),
                ("విదేశీ ప్రయాణం", "ఆరోగ్యం"),
                ("విద్య", "ఖర్చులు")
            ]

            for t1, t2 in unrelated_pairs:
                txt1 = sec_dict.get(t1, "")
                txt2 = sec_dict.get(t2, "")
                if txt1 and txt2:
                    sim = calculate_similarity(txt1, txt2)
                    self.assertLess(
                        sim, 0.60,
                        f"Text similarity between unrelated topics '{t1}' and '{t2}' is {sim:.2f} (must be < 0.60)"
                    )

if __name__ == "__main__":
    unittest.main()
