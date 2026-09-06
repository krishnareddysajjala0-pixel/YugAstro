# -*- coding: utf-8 -*-
filepath = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\astrology_data.py"

with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

aliases_code = """
RASHI_ALIASES = {
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

if "def get_rashi_data(slug):" in text and "RASHI_ALIASES" not in text:
    text = text.replace("def get_rashi_data(slug):", aliases_code)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully added RASHI_ALIASES to astrology_data.py!")
else:
    print("RASHI_ALIASES already exists or get_rashi_data not found.")