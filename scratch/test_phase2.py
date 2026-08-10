import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import app as flask_app
import astrology_data

class Phase2TestCase(unittest.TestCase):
    def setUp(self):
        flask_app.app.testing = True
        self.client = flask_app.app.test_client()

    def test_hubs(self):
        hubs = ['/nakshatrams', '/rashulu', '/gocharalu', '/jyotishyam-basics']
        for hub in hubs:
            res = self.client.get(hub)
            self.assertEqual(res.status_code, 200, f"Hub failed: {hub}")

    def test_all_27_nakshatras(self):
        for item in astrology_data.NAKSHATRAS_LIST:
            slug = item[0]
            res = self.client.get(f'/nakshatram/{slug}')
            self.assertEqual(res.status_code, 200, f"Nakshatra failed: {slug}")
            self.assertIn(item[1], res.get_data(as_text=True))

    def test_all_12_rashis(self):
        for item in astrology_data.RASHULU_LIST:
            slug = item[0]
            res = self.client.get(f'/rashi/{slug}')
            self.assertEqual(res.status_code, 200, f"Rashi failed: {slug}")
            self.assertIn(item[1], res.get_data(as_text=True))

    def test_sitemap_contains_all(self):
        res = self.client.get('/sitemap.xml')
        self.assertEqual(res.status_code, 200)
        content = res.get_data(as_text=True)
        self.assertIn('https://ravanastro.vercel.app/nakshatram/ashwini', content)
        self.assertIn('https://ravanastro.vercel.app/rashi/mesha', content)

if __name__ == '__main__':
    unittest.main()
