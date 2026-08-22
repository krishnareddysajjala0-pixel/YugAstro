# -*- coding: utf-8 -*-
"""
Populate ALL remaining untranslated strings (FAQ Q&A titles, Terms headings, JS alerts, etc.) across 6 languages.
"""

import json
import os

trans_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\translations"

extra_dict = {
    "ఈ బ్రౌజర్ జియోలొకేషన్ మద్దతు ఇవ్వదు": {
        "en": "This browser does not support geolocation.",
        "hi": "यह ब्राउज़र भू-स्थान का समर्थन नहीं करता है।",
        "kn": "ಈ ಬ್ರೌಸರ್ ಜಿಯೋಲೋಕೇಶನ್ ಬೆಂಬಲಿಸುವುದಿಲ್ಲ.",
        "ta": "இந்த உலாவி இருப்பிட சேவையை ஆதரிக்கவில்லை.",
        "ml": "ഈ ബ്രൗസർ ജിയോലൊക്കേഷൻ പിന്തുണയ്ക്കുന്നില്ല.",
        "or": "ଏହି ବ୍ରାଉଜର୍ ଭୂ-ସ୍ଥାନ ସମର୍ଥନ କରେ ନାହିଁ |"
    },
    "స్థానం పొందడంలో లోపం": {
        "en": "Error getting location",
        "hi": "स्थान प्राप्त करने में त्रुटि",
        "kn": "ಸ್ಥಾನ ಪಡೆಯುವಲ್ಲಿ ದೋಷ",
        "ta": "இருப்பிடத்தைப் பெறுவதில் பிழை",
        "ml": "ലൊക്കേഷൻ ലഭിക്കുന്നതിൽ പിശക്",
        "or": "ସ୍ଥାନ ପାଇବାରେ ତ୍ରୁଟି"
    },
    "స్థానం అనుమతి నిరాకరించబడింది": {
        "en": "Location permission denied",
        "hi": "स्थान अनुमति अस्वीकृत",
        "kn": "ಸ್ಥಾನದ ಅನುಮತಿ ನಿರಾಕರಿಸಲಾಗಿದೆ",
        "ta": "இருப்பிட அனுமதி மறுக்கப்பட்டது",
        "ml": "ലൊക്കേഷൻ അനുമതി നിരസിച്ചു",
        "or": "ସ୍ଥାନ ଅନୁମତି ପ୍ରତ୍ୟାଖ୍ୟାନ କରାଯାଇଛି"
    },
    "స్థాన సమాచారం అందుబాటులో లేదు": {
        "en": "Location information unavailable",
        "hi": "स्थान की जानकारी उपलब्ध नहीं है",
        "kn": "ಸ್ಥಾನದ ಮಾಹಿತಿ ಲಭ್ಯವಿಲ್ಲ",
        "ta": "இருப்பிடத் தகவல் கிடைக்கவில்லை",
        "ml": "ലൊക്കേഷൻ വിവരങ്ങൾ ലഭ്യമല്ല",
        "or": "ସ୍ଥାନ ସୂଚନା ଉପଲବ୍ଧ ନାହିଁ"
    },
    "స్థానం అభ్యర్థన సమయం ముగిసింది": {
        "en": "Location request timed out",
        "hi": "स्थान अनुरोध का समय समाप्त हो गया",
        "kn": "ಸ್ಥಾನ ವಿನಂತಿಯ ಸಮಯ ಮುಗಿದಿದೆ",
        "ta": "இருப்பிட கோரிக்கை நேரம் முடிந்தது",
        "ml": "ലൊക്കേഷൻ അഭ്യർത്ഥന സമയം കഴിഞ്ഞു",
        "or": "ସ୍ଥାନ ଅନୁରୋଧ ସମୟ ସମାପ୍ତ ହୋଇଛି"
    },
    "1) జాతకములో ఏ సమస్యనైనా తెలియవచ్చునా?": {
        "en": "1) Can any problem be known from the birth chart?",
        "hi": "1) क्या कुंडली से किसी भी समस्या का पता चल सकता है?",
        "kn": "1) ಜಾತಕದಿಂದ ಯಾವುದೇ ಸಮಸ್ಯೆಯನ್ನು ತಿಳಿಯಬಹುದೇ?",
        "ta": "1) ஜாதகத்தின் மூலம் எந்தப் பிரச்சினையையும் அறிய முடியுமா?",
        "ml": "1) ജാതകത്തിൽ നിന്ന് എന്തെങ്കിലും പ്രശ്നം അറിയാൻ കഴിയുമോ?",
        "or": "1) କୁଣ୍ଡଳୀରୁ କୌଣସି ସମସ୍ୟା ଜାଣିହେବ କି?"
    },
    "1. జ్యోతిష్య శాస్త్రము: జ్యోతిష్యము అంటే ఏమిటి?": {
        "en": "1. Astrology Science: What is Astrology?",
        "hi": "1. ज्योतिष शास्त्र: ज्योतिष क्या है?",
        "kn": "1. ಜ್ಯೋತಿಷ್ಯ ಶಾಸ್ತ್ರ: ಜ್ಯೋತಿಷ್ಯ ಎಂದರೇನು?",
        "ta": "1. ஜோதிட சாஸ்திரம்: ஜோதிடம் என்றால் என்ன?",
        "ml": "1. ജ്യോതിഷ ശാസ്ത്രം: ജ്യോതിഷം എന്നാൽ എന്താണ്?",
        "or": "1. ଜ୍ୟୋତିଷ ଶାସ୍ତ୍ର: ଜ୍ୟୋତିଷ କ’ଣ?"
    },
    "1. వైద్య, న్యాయ లేదా ఆర్థిక సలహా కాదు (Not Professional Advice)": {
        "en": "1. Not Professional Advice (Medical, Legal, or Financial)",
        "hi": "1. चिकित्सीय, कानूनी या वित्तीय सलाह नहीं (Professional Advice)",
        "kn": "1. ವೈದ್ಯಕೀಯ, ಕಾನೂನು ಅಥವಾ ಆರ್ಥಿಕ ಸಲಹೆಯಲ್ಲ",
        "ta": "1. மருத்துவ, சட்ட அல்லது நிதி ஆலோசனையல்ல",
        "ml": "1. വൈദ്യ, നിയമ അല്ലെങ്കിൽ സാമ്പത്തിക ഉപദേശമല്ല",
        "or": "1. ଡାକ୍ତରୀ, ଆଇନଗତ କିମ୍ବା ଆର୍ଥିକ ପରାମର୍ଶ ନୁହେଁ"
    },
    "1. సేవల వినియోగం (Permitted Use)": {
        "en": "1. Permitted Use of Services",
        "hi": "1. सेवाओं का उपयोग (Permitted Use)",
        "kn": "1. ಸೇವೆಗಳ ಬಳಕೆ",
        "ta": "1. சேவைகளின் பயன்பாடு",
        "ml": "1. സേവനങ്ങളുടെ ഉപയോഗം",
        "or": "1. ସେବାସମୂହର ବ୍ୟବହାର"
    },
    "12 లగ్నాలు (12 Lagnams) - లగ్నాధిపతులు": {
        "en": "12 Lagnams - Lagnam Lords",
        "hi": "12 लग्न - लग्नाधिपति",
        "kn": "12 ಲಗ್ನಗಳು - ಲಗ್ನಾಧಿಪತಿಗಳು",
        "ta": "12 லக்னங்கள் - லக்னாதிபதிகள்",
        "ml": "12 ലഗ്നങ്ങൾ - ലഗ്നാധിപതികൾ",
        "or": "12 ଲଗ୍ନ - ଲଗ୍ନାଧିପତି"
    },
    "12 లగ్నాలు (లగ్నాలు)": {
        "en": "12 Lagnams",
        "hi": "12 लग्न",
        "kn": "12 ಲಗ್ನಗಳು",
        "ta": "12 லக்னங்கள்",
        "ml": "12 ലഗ്നങ്ങൾ",
        "or": "12 ଲଗ୍ନ"
    },
    "12 లగ్నాలు - స్వభావం & అధిపతులు | RAVAN ASTRO": {
        "en": "12 Lagnams - Nature & Lords | RAVAN ASTRO",
        "hi": "12 लग्न - स्वभाव और स्वामी | RAVAN ASTRO",
        "kn": "12 ಲಗ್ನಗಳು - ಸ್ವಭಾವ ಮತ್ತು ಅಧಿಪತಿಗಳು | RAVAN ASTRO",
        "ta": "12 லக்னங்கள் - இயல்பு & அதிபதிகள் | RAVAN ASTRO",
        "ml": "12 ലഗ്നങ്ങൾ - സ്വഭാവം & അധിപതികൾ | RAVAN ASTRO",
        "or": "12 ଲଗ୍ନ - ସ୍ୱଭାବ ଏବଂ ଅଧିପତି | RAVAN ASTRO"
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

    for te_key, val_dict in extra_dict.items():
        data[te_key] = val_dict.get(lang, val_dict.get("en", te_key))

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print(f"Populated Extra Translations in translations_{lang}.json ({len(data)} total keys)")
