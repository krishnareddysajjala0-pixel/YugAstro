import sys
import os
import json
import re
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import app as flask_app

class Phase3TestCase(unittest.TestCase):
    def setUp(self):
        flask_app.app.testing = True
        self.client = flask_app.app.test_client()

    def test_home_schema(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        html = res.get_data(as_text=True)
        self.assertIn('"@type": "WebSite"', html)
        self.assertIn('"@type": "Organization"', html)

    def test_nakshatra_schema(self):
        res = self.client.get('/nakshatram/ashwini')
        self.assertEqual(res.status_code, 200)
        html = res.get_data(as_text=True)
        self.assertIn('"@type": "BreadcrumbList"', html)
        self.assertIn('"@type": "Article"', html)
        self.assertIn('"@type": "FAQPage"', html)

    def test_rashi_schema(self):
        res = self.client.get('/rashi/mesha')
        self.assertEqual(res.status_code, 200)
        html = res.get_data(as_text=True)
        self.assertIn('"@type": "BreadcrumbList"', html)
        self.assertIn('"@type": "Article"', html)
        self.assertIn('"@type": "FAQPage"', html)

if __name__ == '__main__':
    unittest.main()
