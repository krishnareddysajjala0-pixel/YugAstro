# -*- coding: utf-8 -*-
"""
Scan ALL template HTML files in templates/ for Jinja i18n keys
and ensure they exist in all 6 translation JSON files.
"""

import json
import os
import re

tpl_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\templates"
trans_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\translations"

j_keys = set()
for file in os.listdir(tpl_dir):
    if file.endswith('.html'):
        p = os.path.join(tpl_dir, file)
        with open(p, 'r', encoding='utf-8') as f:
            content = f.read()
        matches = re.findall(r"\{\{\s*_\(['\"](.+?)['\"]\)\s*\}\}", content)
        for m in matches:
            if m.strip():
                j_keys.add(m.strip())

print(f"Total Jinja i18n keys found across ALL templates: {len(j_keys)}")

fallback_en = {
    "మా గురించి": "About Us",
    "సంప్రదించండి": "Contact Us",
    "గోప్యతా విధానం": "Privacy Policy",
    "నిబంధనలు": "Terms & Conditions",
    "నిరాకరణ": "Disclaimer",
    "జన్మ కుండలి": "Birth Chart",
    "కుండలి పొంతన": "Kundali Matching",
    "దిన పంచాంగం": "Daily Panchangam",
    "పండుగల క్యాలెండర్": "Festivals Calendar",
    "27 నక్షత్రాలు": "27 Nakshatras",
    "12 లగ్నాలు": "12 Lagnams",
    "గోచారాలు 2026": "Transits 2026",
    "జ్యోతిష్య పాఠాలు": "Astrology Lessons",
    "ఖచ్చితమైన త్రైత జ్యోతిష్య పంచాంగం, జన్మ కుండలి గణనలు మరియు గుణ మేళన సమాచారం.": "Accurate Thraitha Astrology Panchangam, Birth Chart calculations and Matching info.",
    "త్రైత జ్యోతిష్య శోధన, జన్మ కుండలి, గుణ మేళన పొంతన, దిన పంచాంగము మరియు క్యాలెండర్ వివరాలు తెలుగులో.": "Accurate Thraitha Astrology, Birth Chart, Matching, Daily Panchangam & Calendar details.",
    "పుట్టినప్పుడే నిర్ణయించబడిన పతకము కావున దీనిని జాఫతకము అంటున్నాము.": "Since it is a plan determined at the time of birth, we call it a Birth Plan.",
    "ద్వాదశ గ్రహములతో కూడిన జ్యోతిష్య శాస్త్రము ఆధారముగా మీ జాఫతకము నిర్ణయించబడుతుంది.": "Your birth chart is determined based on astrology with 12 planets.",
    "మీ పూర్తి పేరు": "Your Full Name",
    "దయచేసి జన్మ తేది ఎంచుకోండి": "Please select date of birth",
    "దయచేసి సమయం ఎంచుకోండి": "Please select time of birth",
    "10 అంకెల నంబర్": "10 Digit Mobile Number",
    "టెలిగ్రామ్‌లో జాతకం PDF పొందండి": "Get Horoscope PDF on Telegram",
    "జన్మ స్థలం": "Place of Birth",
    "క్లియర్": "Clear",
    "కుండలి చూపించండి": "Show Kundali",
    "ఫలితాలు లేవు": "No results found",
    "గణన చేస్తోంది": "Calculating...",
    "భాష": "Language",
    "హోమ్": "Home",
    "పోలిక": "Matching",
    "పంచాంగం": "Panchangam",
    "క్యాలెండర్": "Calendar"
}

fallback_hi = {
    "మా గురించి": "हमारे बारे में",
    "సంప్రదించండి": "संपर्क करें",
    "గోప్యతా విధానం": "गोपनीयता नीति",
    "నిబంధనలు": "नियम व शर्तें",
    "నిరాకరణ": "अस्वीकरण",
    "జన్మ కుండలి": "जन्म कुंडली",
    "కుండలి పొంతన": "कुंडली मिलान",
    "దిన పంచాంగం": "दैनिक पंचांग",
    "పండుగల క్యాలెండర్": "त्योहार कैलेंडर",
    "27 నక్షత్రాలు": "27 नक्षत्र",
    "12 లగ్నాలు": "12 लग्न",
    "గోచారాలు 2026": "गोचर 2026",
    "జ్యోతిష్య పాఠాలు": "ज्योतिष पाठ",
    "క్లియర్": "साफ़ करें",
    "కుండలి చూపించండి": "कुंडली दिखाएं",
    "భాష": "भाषा",
    "హోమ్": "होम",
    "పోలిక": "मिलान",
    "పంచాంగం": "पंचांग",
    "క్యాలెండర్": "कैलेंडर"
}

fallback_kn = {
    "మా గురించి": "ನಮ್ಮ ಬಗ್ಗೆ",
    "సంప్రదించండి": "ಸಂಪರ್ಕಿಸಿ",
    "గోప్యతా విధానం": "ಗೌಪ್ಯತಾ ನೀತಿ",
    "నిబంధనలు": "ನಿಯಮಗಳು",
    "నిరాకరణ": "ಹಕ್ಕುತ್ಯಾಗ",
    "జన్మ కుండలి": "ಜನ್ಮ ಕುಂಡಲಿ",
    "కుండలి పొంతన": "ಕುಂಡಲಿ ಮಿಲನ",
    "దిన పంచాంగం": "ದಿನ ಪಂಚಾಂಗ",
    "పండుగల క్యాలెండర్": "ಹಬ್ಬಗಳ ಕ್ಯಾಲೆಂಡರ್",
    "27 నక్షత్రాలు": "27 ನಕ್ಷತ್ರಗಳು",
    "12 లగ్నాలు": "12 ಲಗ್ನಗಳು",
    "గోచారాలు 2026": "ಗೋಚಾರ 2026",
    "జ్యోతిష్య పాఠాలు": "ಜ್ಯೋತಿಷ್ಯ ಪಾಠಗಳು",
    "క్లియర్": "ತೆರವುಗೊಳಿಸಿ",
    "కుండలి చూపించండి": "ಕುಂಡಲಿ ತೋರಿಸಿ",
    "భాష": "ಭಾಷೆ",
    "హోమ్": "ಹೋಮ್",
    "పోలిక": "ಹೊಂದಾಣಿಕೆ",
    "పంచాంగం": "ಪಂಚಾಂಗ",
    "క్యాలెండర్": "ಕ್ಯಾಲೆಂಡರ್"
}

fallback_ta = {
    "మా గురించి": "எங்களைப் பற்றி",
    "సంప్రదించండి": "தொடர்பு கொள்ள",
    "గోప్యతా విధానం": "தனியురిமைக் கொள்கை",
    "నిబంధనలు": "விதிமுறைகள்",
    "నిరాకరణ": "பொறுப்புத் துறப்பு",
    "జన్మ కుండలి": "ஜாதக கட்டம்",
    "కుండలి పొంతన": "திருமண பொருத்தம்",
    "దిన పంచాంగం": "தினசரி பஞ்சாங்கம்",
    "పండుగల క్యాలెండర్": "பண்டிகை நாட்காட்டி",
    "27 నక్షత్రాలు": "27 நட்சத்திரங்கள்",
    "12 లగ్నాలు": "12 லக்னங்கள்",
    "గోచారాలు 2026": "பெயர்ச்சி 2026",
    "జ్యోతిష్య పాఠాలు": "ஜோதிட பாடங்கள்",
    "భాష": "மொழி",
    "హోమ్": "முகப்பு",
    "పోలిక": "பொருத்தம்",
    "పంచాంగం": "பஞ்சாங்கம்",
    "క్యాలెండర్": "நாட்காட்டி"
}

fallback_ml = {
    "మా గురించి": "ഞങ്ങളെക്കുറിച്ച്",
    "సంప్రదించండి": "ബന്ധപ്പെടുക",
    "గోప్యతా విధానం": "സ്വകാര്യതാ നയം",
    "నిబంధనలు": "നിബന്ധനകൾ",
    "నిరాకరణ": "നിരാകരണം",
    "జన్మ కుండలి": "ജന്മ കുണ്ഡലി",
    "కుండలి పొంతన": "ജാതക പൊരുത്തം",
    "దిన పంచాంగం": "ദിന പഞ്ചാംഗം",
    "పండుగల క్యాలెండర్": "ആഘോഷ കലണ്ടർ",
    "27 నక్షత్రాలు": "27 നക്ഷത്രങ്ങൾ",
    "12 లగ్నాలు": "12 ലഗ്നങ്ങൾ",
    "గోచారాలు 2026": "ഗോചരം 2026",
    "జ్యోతిష్య పాఠాలు": "ജ്യോതിഷ പാഠങ്ങൾ",
    "భాష": "ഭാഷ",
    "హోమ్": "ഹോം",
    "పోలిక": "പൊരുത്തം",
    "పంచాంగം": "പഞ്ചാംഗം",
    "క్యాలెండർ": "കലണ്ടർ"
}

fallback_or = {
    "మా గురించి": "ଆମ ବିଷୟରେ",
    "సంప్రదించండి": "ଯୋଗାଯୋଗ କରନ୍ତୁ",
    "గోప్యతా విధానం": "ଗୋପନୀୟତା ନୀତି",
    "నిబంధనలు": "ନିୟମାବଳୀ",
    "నిరాకరణ": "ଦାବି ତ୍ୟାଗ",
    "జన్మ కుండలి": "ଜନ୍ମ କୁଣ୍ଡଳୀ",
    "కుండలి పొంతన": "କୁଣ୍ଡଳୀ ମେଳକ",
    "దిన పంచాంగం": "ଦୈନିକ ପଞ୍ଚାଙ୍ଗ",
    "పండుగల క్యాలెండర్": "ପର୍ବପର୍ବାଣି କ୍ୟାଲେଣ୍ଡର",
    "27 నక్షత్రాలు": "27 ନକ୍ଷତ୍ର",
    "12 లగ్నాలు": "12 ଲଗ୍ନ",
    "గోచారాలు 2026": "ଗୋଚର ୨୦୨୬",
    "జ్యోతిష్య పాఠాలు": "ଜ୍ୟୋତିଷ ପାଠ",
    "భాష": "ଭାଷା",
    "హోమ్": "ହୋମ୍",
    "పోలిక": "ମେଳକ",
    "పంచాంగం": "ପଞ୍ଚାଙ୍ଗ",
    "క్యాలెండర్": "କ୍ୟାଲେଣ୍ଡର"
}

maps = {
    "en": fallback_en,
    "hi": fallback_hi,
    "kn": fallback_kn,
    "ta": fallback_ta,
    "ml": fallback_ml,
    "or": fallback_or
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

    f_map = maps.get(lang, {})
    for k in j_keys:
        if k not in data:
            data[k] = f_map.get(k, fallback_en.get(k, k))

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Verified translations_{lang}.json ({len(data)} keys total)")
