# -*- coding: utf-8 -*-
import unittest
from app import app, get_kundali_data, get_dasha_info
from results_engine import evaluate_kundali_results

class TestResultsRegression(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_kundali_data_and_dasha_integrity(self):
        data = get_kundali_data("Test Native", "1995-01-01", "12:00", "Hyderabad", 17.3850, 78.4867)
        self.assertIn('lagna', data)
        self.assertIn('planet_positions', data)
        self.assertIn('houses', data)

        # Verify 12 planets
        planets = data['planet_positions']
        planet_names = [p['name'] for p in planets] if isinstance(planets, list) else list(planets.keys())
        for p in ["సూర్యుడు", "చంద్రుడు", "కుజుడు", "బుధుడు", "గురు", "శుక్రుడు", "శని", "రాహు", "కేతు", "భూమి", "మిత్ర", "చిత్ర"]:
            self.assertIn(p, planet_names)

        # Verify Results Engine Evaluation
        dasha_info = get_dasha_info(data) if isinstance(data, dict) else {}
        report = evaluate_kundali_results(data, dasha_info if isinstance(dasha_info, dict) else {})

        self.assertEqual(report['report_title'], "సంపూర్ణ జాతక ఫలితాలు")
        self.assertGreater(len(report['sections']), 30)

    def test_api_jathaka_results_endpoint(self):
        # Test API endpoint
        with self.app.session_transaction() as sess:
            sess['birth_info'] = get_kundali_data("Test Native", "1995-01-01", "12:00", "Hyderabad", 17.3850, 78.4867)

        res = self.app.get('/api/jathaka-results')
        self.assertEqual(res.status_code, 200)
        json_data = res.get_json()
        self.assertTrue(json_data.get('success'))
        self.assertIn('results', json_data)

if __name__ == "__main__":
    unittest.main()
