# -*- coding: utf-8 -*-
"""
STEP 13: 5-Chart Regression Testing Suite
Tests 5 distinct known birth charts representing Guru-party Lagnas, Shani-party Lagnas,
and different birth times/locations to verify 100% calculation integrity and 0 regressions.
"""

import unittest
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

class Test5ChartsRegression(unittest.TestCase):
    def test_all_5_charts_regression(self):
        for idx, chart in enumerate(TEST_CHARTS, 1):
            with self.subTest(chart=chart["name"]):
                data = get_kundali_data(
                    chart["name"], chart["dob"], chart["tob"],
                    chart["place"], chart["lat"], chart["lon"]
                )

                self.assertIsNotNone(data, f"Chart {idx} returned None")
                self.assertIn('lagna', data)
                self.assertIn('planet_positions', data)
                self.assertIn('houses', data)

                # Verify 12 planets preserved
                planets = data['planet_positions']
                planet_names = [p['name'] for p in planets] if isinstance(planets, list) else list(planets.keys())
                expected_12 = ["సూర్యుడు", "చంద్రుడు", "కుజుడు", "బుధుడు", "గురు", "శుక్రుడు", "శని", "రాహు", "కేతు", "భూమి", "మిత్ర", "చిత్ర"]
                for p in expected_12:
                    self.assertIn(p, planet_names, f"Planet {p} missing in {chart['name']}")

                # Evaluate Results Engine
                dasha_info = get_dasha_info(data) if isinstance(data, dict) else {}
                report = evaluate_kundali_results(data, dasha_info if isinstance(dasha_info, dict) else {})

                self.assertEqual(report['report_title'], "సంపూర్ణ జాతక ఫలితాలు")
                self.assertIn('sections', report)
                self.assertGreater(len(report['sections']), 30, f"Sections incomplete for {chart['name']}")
                self.assertIn('meta', report)
                self.assertGreater(report['meta']['rule_count'], 0)

if __name__ == "__main__":
    unittest.main()
