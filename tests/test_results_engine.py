# -*- coding: utf-8 -*-
import unittest
from results_engine import NormalizedChartContext, ResultsEngine, ReportBuilder, evaluate_kundali_results

class TestResultsEngine(unittest.TestCase):
    def setUp(self):
        self.sample_data = {
            'name': 'కృష్ణ రెడ్డి',
            'dob': '1995-05-15',
            'tob': '10:30',
            'place': 'Hyderabad',
            'lagna': 'కుంభం',
            'houses': {
                'కుంభం': 1, 'మీనం': 2, 'మేషం': 3, 'వృషభం': 4,
                'మిథునం': 5, 'కర్కాటకం': 6, 'సింహం': 7, 'వృశ్చికం': 8,
                'ధనస్సు': 9, 'మకరం': 10, 'తులా': 11, 'కన్య': 12
            },
            'planet_positions': {
                'సూర్యుడు': {'rasi': 'వృషభం', 'house': 4, 'longitude': 45.0},
                'చంద్రుడు': {'rasi': 'వృశ్చికం', 'house': 8, 'longitude': 225.0},
                'కుజుడు': {'rasi': 'సింహం', 'house': 7, 'longitude': 135.0},
                'బుధుడు': {'rasi': 'మేషం', 'house': 3, 'longitude': 15.0},
                'గురు': {'rasi': 'వృశ్చికం', 'house': 8, 'longitude': 230.0},
                'శుక్రుడు': {'rasi': 'మీనం', 'house': 2, 'longitude': 340.0},
                'శని': {'rasi': 'కుంభం', 'house': 1, 'longitude': 10.0},
                'రాహు': {'rasi': 'మకరం', 'house': 10, 'longitude': 280.0},
                'కేతు': {'rasi': 'ధనస్సు', 'house': 9, 'longitude': 250.0},
                'భూమి': {'rasi': 'వృశ్చికం', 'house': 8, 'longitude': 225.0},
                'మిత్ర': {'rasi': 'మిథునం', 'house': 5, 'longitude': 70.0},
                'చిత్ర': {'rasi': 'కర్కాటకం', 'house': 6, 'longitude': 100.0}
            },
            'nakshatra': 'అనురాధ',
            'padam': 2,
            'birth_dasa': 'శని'
        }
        self.sample_dasha = {
            'current_dasa': 'శని',
            'current_anthara': 'గురు',
            'all_dasas': [
                {'maha': 'శని', 'is_current': True, 'is_favorable': True}
            ]
        }

    def test_context_creation(self):
        ctx = NormalizedChartContext(self.sample_data, self.sample_dasha)
        self.assertEqual(ctx.lagna, 'కుంభం')
        self.assertFalse(ctx.is_guru_party_lagna) # Kumbham is Shani party
        self.assertEqual(ctx.house_lords[1], 'శని')
        self.assertEqual(ctx.lord_placements[1], 1)

    def test_engine_evaluation(self):
        report = evaluate_kundali_results(self.sample_data, self.sample_dasha)
        self.assertIn("report_title", report)
        self.assertIn("sections", report)
        self.assertGreater(len(report["sections"]), 0)
        self.assertGreater(report["meta"]["rule_count"], 0)

if __name__ == "__main__":
    unittest.main()
