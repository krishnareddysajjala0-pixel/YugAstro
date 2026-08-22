# -*- coding: utf-8 -*-
"""
Populate card right-side badge/pill tag translations in all 6 target languages.
"""

import json
import os

trans_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\translations"

pill_dict = {
    "కుండలి": {
        "en": "Kundali",
        "hi": "कुंडली",
        "kn": "ಕುಂಡಲಿ",
        "ta": "ஜாதகம்",
        "ml": "കുണ്ഡലി",
        "or": "କୁଣ୍ଡଳୀ"
    },
    "వివాహ పొంతన": {
        "en": "Marriage Match",
        "hi": "विवाह मिलान",
        "kn": "ವಿವಾಹ ಮಿಲನ",
        "ta": "திருமண பொருத்தம்",
        "ml": "വിവാഹ പൊരുത്തം",
        "or": "ବିବାହ ମେଳକ"
    },
    "త్రైత సిద్ధాంతం": {
        "en": "Thraitha Siddhantha",
        "hi": "त्रैत सिद्धांत",
        "kn": "ತ್ರైత ಸಿದ್ಧಾಂತ",
        "ta": "த்ரைதா சித்தாந்தம்",
        "ml": "ത്രൈത സിദ്ധാന്തം",
        "or": "ତ୍ରୈତ ସିଦ୍ଧାନ୍ତ"
    },
    "రోజువారీ": {
        "en": "Daily",
        "hi": "दैनिक",
        "kn": "ದೈನಂದಿನ",
        "ta": "தினசரி",
        "ml": "ദിനചര്യ",
        "or": "ଦୈନିକ"
    },
    "పండుగలు": {
        "en": "Festivals",
        "hi": "त्योहार",
        "kn": "ಹಬ್ಬಗಳು",
        "ta": "பண்டிகைகள்",
        "ml": "ആഘോഷങ്ങൾ",
        "or": "ପର୍ବପର୍ବାଣି"
    },
    "34 ప్రశ్నలు-జవాబులు": {
        "en": "34 Q&A",
        "hi": "34 प्रश्नोत्तर",
        "kn": "34 ಪ್ರಶ್ನೋತ್ತರ",
        "ta": "34 வினா-விடை",
        "ml": "34 ചോദ്യോത്തരങ്ങൾ",
        "or": "୩୪ ପ୍ରଶ୍ନୋତ୍ତର"
    },
    "2026 గోచారం": {
        "en": "2026 Transit",
        "hi": "2026 गोचर",
        "kn": "2026 ಗೋಚಾರ",
        "ta": "2026 பெயர்ச்சி",
        "ml": "2026 ഗോചരം",
        "or": "୨୦୨୬ ଗୋଚର"
    }
}

langs = ["en", "hi", "kn", "ta", "ml", "or"]

for lang in langs:
    fpath = os.path.join(trans_dir, f"translations_{lang}.json")
    data = {}
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
            except Exception:
                data = {}

    for te_key, val_dict in pill_dict.items():
        data[te_key] = val_dict.get(lang, val_dict.get("en", te_key))

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Populated Card Pill Tags in translations_{lang}.json ({len(data)} total keys)")
