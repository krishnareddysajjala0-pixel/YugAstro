import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import app as flask_app
import astrology_data

class FullMasterPlanTestCase(unittest.TestCase):
    def setUp(self):
        flask_app.app.testing = True
        self.client = flask_app.app.test_client()

    def test_phase1_seo_legal(self):
        self.assertEqual(self.client.get('/robots.txt').status_code, 200)
        self.assertEqual(self.client.get('/sitemap.xml').status_code, 200)
        for route in ['/about', '/contact', '/privacy-policy', '/terms', '/disclaimer']:
            self.assertEqual(self.client.get(route).status_code, 200, f"Failed: {route}")

    def test_phase2_content_system(self):
        for hub in ['/nakshatrams', '/rashulu', '/gocharalu', '/jyotishyam-basics']:
            self.assertEqual(self.client.get(hub).status_code, 200, f"Failed: {hub}")
        for item in astrology_data.NAKSHATRAS_LIST:
            self.assertEqual(self.client.get(f'/nakshatram/{item[0]}').status_code, 200)
        for item in astrology_data.RASHULU_LIST:
            self.assertEqual(self.client.get(f'/rashi/{item[0]}').status_code, 200)

    def test_phase3_structured_data(self):
        res_home = self.client.get('/')
        self.assertIn('"@type": "WebSite"', res_home.get_data(as_text=True))
        res_nak = self.client.get('/nakshatram/ashwini')
        self.assertIn('"@type": "BreadcrumbList"', res_nak.get_data(as_text=True))
        self.assertIn('"@type": "Article"', res_nak.get_data(as_text=True))

    def test_phase5_ads_txt(self):
        res = self.client.get('/ads.txt')
        self.assertEqual(res.status_code, 200)

    def test_phase6_report_funnel_security(self):
        # 1. Draft creation
        res = self.client.get('/api/create_report_draft')
        self.assertEqual(res.status_code, 302)
        
        # 2. Details page
        res_page = self.client.get('/report/ra_ord_test123')
        self.assertEqual(res_page.status_code, 200)
        self.assertIn('ra_ord_test123', res_page.get_data(as_text=True))

        # 3. Security test: Webhook without signature header MUST return 400 rejection
        res_hook = self.client.post('/api/payment_webhook', json={'payload': {'order_id': 'ra_ord_test123'}})
        self.assertEqual(res_hook.status_code, 400)

    def test_chart_no_regression(self):
        data = {
            'name': 'Krishna',
            'dob': '1990-08-15',
            'tob': '10:15',
            'lat': '17.3850',
            'lon': '78.4867',
            'tz': '5.5',
            'place_search': 'Hyderabad'
        }
        res = self.client.post('/chart', data=data)
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()
