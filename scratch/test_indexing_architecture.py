import unittest
from app import app

class IndexingArchitectureTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_private_report_order_noindex(self):
        res = self.client.get('/report/ra_ord_test123')
        self.assertEqual(res.status_code, 200)
        self.assertIn('noindex, nofollow', res.get_data(as_text=True))

    def test_public_reports_offer_page_indexed(self):
        res = self.client.get('/reports')
        self.assertEqual(res.status_code, 200)
        self.assertIn('index, follow', res.get_data(as_text=True))
        self.assertIn('RAVAN ASTRO', res.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
