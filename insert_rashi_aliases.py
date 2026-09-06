# -*- coding: utf-8 -*-
filepath = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\astrology_data.py"

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

aliases_def = """RASHI_ALIASES = {
    "mesha": "mesha", "aries": "mesha",
    "vrishabha": "vrishabha", "taurus": "vrishabha",
    "mithuna": "mithuna", "gemini": "mithuna",
    "karkataka": "karkataka", "cancer": "karkataka",
    "simha": "simha", "leo": "simha",
    "kanya": "kanya", "virgo": "kanya",
    "thula": "tula", "tula": "tula", "libra": "tula",
    "vrischika": "vrischika", "scorpio": "vrischika",
    "dhanus": "dhanu", "dhanu": "dhanu", "sagittarius": "dhanu",
    "makara": "makara", "capricorn": "makara",
    "kumbha": "kumbha", "aquarius": "kumbha",
    "meena": "meena", "pisces": "meena"
}

def get_rashi_data(slug):"""

if "def get_rashi_data(slug):" in text:
    text = text.replace("def get_rashi_data(slug):", aliases_def)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully inserted RASHI_ALIASES!")
else:
    print("def get_rashi_data(slug): not found.")