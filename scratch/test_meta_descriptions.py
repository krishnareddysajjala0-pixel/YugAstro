import unittest
from app import app

class MetaDescriptionsTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_unique_meta_descriptions(self):
        routes = [
            '/about',
            '/contact',
            '/privacy-policy',
            '/terms',
            '/disclaimer',
            '/nakshatrams',
            '/rashulu',
            '/gocharalu',
            '/jyotishyam-basics'
        ]
        descriptions = set()
        for r in routes:
            res = self.client.get(r)
            self.assertEqual(res.status_code, 200, f"Route {r} failed with status {res.status_code}")
            html = res.get_data(as_text=True)
            self.assertIn('<meta name="description" content="', html, f"Route {r} missing description tag")
            
            # Extract content value
            import re
            match = re.search(r'<meta name="description" content="(.*?)"', html)
            self.assertIsNotNone(match, f"Could not parse meta description for {r}")
            desc = match.group(1).strip()
            self.assertTrue(len(desc) > 10, f"Description too short for {r}: {desc}")
            self.assertNotIn(desc, descriptions, f"Duplicate description found for {r}: {desc}")
            descriptions.add(desc)

if __name__ == '__main__':
    unittest.main()
