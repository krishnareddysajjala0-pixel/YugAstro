# -*- coding: utf-8 -*-
import unittest
from results_engine.context import NormalizedChartContext, SIGN_LORDS, GURU_PARTY_LAGNAS, GURU_PARTY_PLANETS
from results_engine.rule_loader import RuleLoader

class TestBhavaRules(unittest.TestCase):
    def test_12_planet_rulerships(self):
        self.assertEqual(len(SIGN_LORDS), 12)
        self.assertEqual(SIGN_LORDS["సింహం"], "సూర్యుడు")
        self.assertEqual(SIGN_LORDS["కర్కాటకం"], "చంద్రుడు")
        self.assertEqual(SIGN_LORDS["మకరం"], "రాహు")
        self.assertEqual(SIGN_LORDS["ధనస్సు"], "కేతు")
        self.assertEqual(SIGN_LORDS["వృశ్చికం"], "భూమి")
        self.assertEqual(SIGN_LORDS["వృషభం"], "మిత్ర")
        self.assertEqual(SIGN_LORDS["మిథునం"], "చిత్ర")

    def test_guru_shani_parties(self):
        self.assertIn("మీనం", GURU_PARTY_LAGNAS)
        self.assertIn("మేషం", GURU_PARTY_LAGNAS)
        self.assertNotIn("కుంభం", GURU_PARTY_LAGNAS)
        self.assertIn("సూర్యుడు", GURU_PARTY_PLANETS)

    def test_bhava_lord_rules_matrix_completeness(self):
        loader = RuleLoader.get_instance()
        matrix = loader.get_bhava_lord_rules()
        self.assertGreater(len(matrix), 0)
        for h in range(1, 13):
            self.assertIn(str(h), matrix)

if __name__ == "__main__":
    unittest.main()
