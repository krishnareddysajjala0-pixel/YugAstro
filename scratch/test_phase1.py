import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
import app as flask_app

class Phase1TestCase(unittest.TestCase):
    def setUp(self):
        flask_app.app.testing = True
        self.client = flask_app.app.test_client()

    def test_robots_txt(self):
        response = self.client.get('/robots.txt')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Disallow: /chart', response.get_data(as_text=True))
        self.assertIn('Sitemap: https://ravanastro.vercel.app/sitemap.xml', response.get_data(as_text=True))

    def test_sitemap_xml(self):
        response = self.client.get('/sitemap.xml')
        self.assertEqual(response.status_code, 200)
        self.assertIn('https://ravanastro.vercel.app/about', response.get_data(as_text=True))
        self.assertIn('<?xml version="1.0" encoding="UTF-8"?>', response.get_data(as_text=True))

    def test_legal_routes(self):
        routes = ['/about', '/contact', '/privacy-policy', '/terms', '/disclaimer']
        for route in routes:
            response = self.client.get(route)
            self.assertEqual(response.status_code, 200, f"Failed for route {route}")

    def test_chart_no_regression(self):
        data = {
            'name': 'Test User',
            'dob': '1995-05-15',
            'tob': '08:30',
            'lat': '17.3850',
            'lon': '78.4867',
            'tz': '5.5',
            'place_search': 'Hyderabad'
        }
        response = self.client.post('/chart', data=data)
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
