import unittest
from app import app

class HomepageVisualDesignTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage_visual_elements(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        html = res.get_data(as_text=True)

        # 1. Subtle Zodiac Star Backdrop
        self.assertIn('hero-zodiac-backdrop', html)

        # 2. Three-Item Telugu Visual Strip
        self.assertIn('ద్వాదశ గ్రహాలు', html)
        self.assertIn('12 లగ్నాలు', html)
        self.assertIn('27 నక్షత్రాలు', html)

        # 3. Three-Step Guidance for Birth Form
        self.assertIn('form-steps-guidance', html)
        self.assertIn('జన్మ వివరాలు ఎంటర్ చేయండి', html)
        self.assertIn('లగ్నము & 12 గ్రహాల గణన', html)
        self.assertIn('పరిశీలన & PDF నివేదిక', html)

        # 4. 12-Lagnam Circular/Grid Navigation Section
        self.assertIn('/rashi/mesha', html)
        self.assertIn('/rashi/meena', html)

        # 5. Compact Preview Grid for 9 Nakshatras
        self.assertIn('/nakshatram/ashwini', html)
        self.assertIn('/nakshatram/ashlesha', html)
        self.assertIn('చు, చే, చో, లా', html)

        # 6. Today Panchangam Highlight
        self.assertIn('నేటి దిన పంచాంగం', html)

        # 7. Reduced Motion Guard
        self.assertIn('prefers-reduced-motion', html)

if __name__ == '__main__':
    unittest.main()
