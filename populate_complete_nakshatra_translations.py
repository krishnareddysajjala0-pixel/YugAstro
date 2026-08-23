# -*- coding: utf-8 -*-
"""
Populate complete 27 Nakshatras and 12 Lagnams native script translations across all 6 languages:
EN, HI, KN, TA, ML, OR.
"""

import json
import os
import sys

sys.path.insert(0, r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro")
import astrology_data

trans_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\translations"
langs = ["en", "hi", "kn", "ta", "ml", "or"]

NAKSHATRAS_SCRIPT = {
    "ashwini": {"en": "Ashwini", "hi": "अश्विनी", "kn": "ಅಶ್ವಿನಿ", "ta": "அஸ்வினி", "ml": "അശ്വതി", "or": "ଅଶ୍ୱିନୀ"},
    "bharani": {"en": "Bharani", "hi": "भरणी", "kn": "ಭರಣಿ", "ta": "பரணி", "ml": "ഭരണി", "or": "ଭରଣୀ"},
    "krittika": {"en": "Krittika", "hi": "कृत्तिका", "kn": "ಕೃತ್ತಿಕಾ", "ta": "கார்த்திகை", "ml": "കാർത്തിക", "or": "କୃତ୍ତିକା"},
    "rohini": {"en": "Rohini", "hi": "रोहिणी", "kn": "ರೋಹಿಣಿ", "ta": "ரோகிணி", "ml": "രോഹിണി", "or": "ରୋହିଣୀ"},
    "mrigashira": {"en": "Mrigashira", "hi": "मृगशिरा", "kn": "ಮೃಗಶಿರಾ", "ta": "மிருகசீரிஷம்", "ml": "മകയിരം", "or": "ମୃଗଶିରା"},
    "ardra": {"en": "Ardra", "hi": "आर्द्रा", "kn": "ಆರ್ಪ್ರಾ", "ta": "திருவாதிரை", "ml": "തിരുവാതിര", "or": "ଆର୍ଦ୍ରା"},
    "punarvasu": {"en": "Punarvasu", "hi": "पुनर्वसु", "kn": "ಪುನರ್ವಸು", "ta": "புனர்பூசம்", "ml": "പുണർതം", "or": "ପୁନର୍ବସୁ"},
    "pushya": {"en": "Pushyami", "hi": "पुष्यमी", "kn": "ಪುಷ್ಯಮಿ", "ta": "பூசம்", "ml": "പൂയം", "or": "ପୁଷ୍ୟା"},
    "ashlesha": {"en": "Ashlesha", "hi": "आश्लेषा", "kn": "ಆಶ್ಲೇಷಾ", "ta": "ஆயில்யம்", "ml": "ആയില്യം", "or": "ଆଶ୍ଲେଷା"},
    "magha": {"en": "Magha", "hi": "मघा", "kn": "ಮಘಾ", "ta": "மகம்", "ml": "മകം", "or": "ମଘା"},
    "purva-phalguni": {"en": "Purva Phalguni", "hi": "पूर्वा फाल्गुनी", "kn": "ಪೂರ್ವಾ ಫಾಲ್ಗುಣಿ", "ta": "பூரம்", "ml": "പൂരം", "or": "ପୂର୍ବ ଫାଲ୍ଗୁନୀ"},
    "uttara-phalguni": {"en": "Uttara Phalguni", "hi": "उत्तरा फाल्गुनी", "kn": "ಉತ್ತರಾ ಫಾಲ್ಗುಣಿ", "ta": "உத்திரம்", "ml": "ഉത്രം", "or": "ଉତ୍ତର ଫାଲ୍ଗୁନୀ"},
    "hasta": {"en": "Hasta", "hi": "हस्त", "kn": "ಹಸ್ತಾ", "ta": "ஹஸ்தம்", "ml": "അത്തം", "or": "ହସ୍ତା"},
    "chitra": {"en": "Chitra", "hi": "चित्रा", "kn": "ಚಿತ್ತಾ", "ta": "சித்திரை", "ml": "ചിത്തിര", "or": "ଚିତ୍ରା"},
    "swati": {"en": "Swati", "hi": "स्वाति", "kn": "ಸ್ವಾತಿ", "ta": "சுவாதி", "ml": "ചോതി", "or": "ସ୍ୱାତୀ"},
    "visakha": {"en": "Visakha", "hi": "विशाखा", "kn": "ವಿಶಾಖಾ", "ta": "விசாகம்", "ml": "വിശാഖം", "or": "ବିଶାଖା"},
    "anuradha": {"en": "Anuradha", "hi": "अनुराधा", "kn": "ಅನುರಾಧಾ", "ta": "அனுஷம்", "ml": "അനിഴം", "or": "ଅନୁରାଧା"},
    "jyeshtha": {"en": "Jyeshtha", "hi": "ज्येष्ठा", "kn": "ಜ್ಯೇಷ್ಠಾ", "ta": "கேட்டை", "ml": "തൃക്കേട്ട", "or": "ଜ୍ୟେଷ୍ଠା"},
    "mula": {"en": "Mula", "hi": "मूल", "kn": "ಮೂಲಾ", "ta": "மூலம்", "ml": "മൂലം", "or": "ମୂଳା"},
    "purvashadha": {"en": "Purvashadha", "hi": "पूर्वाषाढ़ा", "kn": "ಪೂರ್ವಾಷಾಢಾ", "ta": "பூராடம்", "ml": "പൂരാടം", "or": "ପୂର୍ବାଷାଢ଼ା"},
    "uttarashadha": {"en": "Uttarashadha", "hi": "उत्तराषाढ़ा", "kn": "ಉತ್ತರಾಷಾಢಾ", "ta": "உத்திராடம்", "ml": "ഉത്രാടം", "or": "ଉତ୍ତରାଷାଢ଼ା"},
    "shravana": {"en": "Shravanam", "hi": "श्रवण", "kn": "ಶ್ರವಣ", "ta": "திருவோணம்", "ml": "തിരുവോണം", "or": "ଶ୍ରବଣା"},
    "dhanishta": {"en": "Dhanishta", "hi": "धनिष्ठा", "kn": "ಧನಿಷ್ಠಾ", "ta": "அவிட்டம்", "ml": "അവിട്ടം", "or": "ଧନିଷ୍ଠା"},
    "shatabhisha": {"en": "Shatabhisha", "hi": "शतभिषा", "kn": "ಶತಭಿಷಾ", "ta": "சதயம்", "ml": "ചതയം", "or": "ଶତଭିଷା"},
    "purvabhadra": {"en": "Purvabhadra", "hi": "पूर्वाभाद्रपद", "kn": "ಪೂರ್ವಾಭಾದ್ರಾ", "ta": "பூரட்டாதி", "ml": "പൂരുരുട്ടാതി", "or": "ପୂର୍ବଭାଦ୍ରପଦ"},
    "uttarabhadra": {"en": "Uttarabhadra", "hi": "उत्तराभाद्रपद", "kn": "ಉತ್ತರಾಭಾದ್ರಾ", "ta": "உத்திரட்டாதி", "ml": "ഉത്രട്ടാതി", "or": "ଉତ୍ତରଭାଦ୍ରପଦ"},
    "revati": {"en": "Revati", "hi": "रेवती", "kn": "ರೇವತಿ", "ta": "ரேவதி", "ml": "രേവതി", "or": "ରେବତୀ"}
}

RASHIS_SCRIPT = {
    "మేష లగ్నం": {"en": "Aries Lagnam", "hi": "मेष लग्न", "kn": "ಮೇಷ ಲಗ್ನ", "ta": "மேஷ லக்னம்", "ml": "മേട ലഗ്നം", "or": "ମେଷ ଲଗ୍ନ"},
    "వృషభ లగ్నం": {"en": "Taurus Lagnam", "hi": "वृषभ लग्न", "kn": "ವೃಷಭ ಲಗ್ನ", "ta": "ரிஷப லக்னம்", "ml": "ഇടവ ലഗ്നം", "or": "ବୃଷ ଲଗ୍ନ"},
    "మిథున లగ్నం": {"en": "Gemini Lagnam", "hi": "मिथुन लग्न", "kn": "ಮಿಥುನ ಲಗ್ನ", "ta": "மிதுன லக்னம்", "ml": "മിഥുന ലഗ്നം", "or": "ମିଥୁନ ଲଗ୍ନ"},
    "కర్కాటక లగ్నం": {"en": "Cancer Lagnam", "hi": "कर्क लग्न", "kn": "ಕರ್ಕಾಟಕ ಲಗ್ನ", "ta": "கடக லக்னம்", "ml": "കർക്കടക ലഗ്നം", "or": "କର୍କଟ ଲଗ୍ନ"},
    "సింహ లగ్నం": {"en": "Leo Lagnam", "hi": "सिंह लग्न", "kn": "ಸಿಂಹ ಲಗ್ನ", "ta": "சிம்ம லக்னம்", "ml": "ചിങ്ങ ലഗ്നം", "or": "ସିଂହ ଲଗ୍ନ"},
    "కన్యా లగ్నం": {"en": "Virgo Lagnam", "hi": "कन्या लग्न", "kn": "ಕನ್ಯಾ ಲಗ್ನ", "ta": "கன்னி லக்னம்", "ml": "കന്നി ലഗ്നം", "or": "କନ୍ୟା ଲଗ୍ନ"},
    "తులా లగ్నం": {"en": "Libra Lagnam", "hi": "तुला लग्न", "kn": "ತುಲಾ ಲಗ್ನ", "ta": "துலா லக்னம்", "ml": "തുലാം ലഗ്നം", "or": "ତୁଳା ଲଗ୍ନ"},
    "వృశ్చిక లగ్నం": {"en": "Scorpio Lagnam", "hi": "वृश्चिक लग्न", "kn": "ವೃಶ್ಚಿಕ ಲಗ್ನ", "ta": "விருச்சிக லக்னம்", "ml": "വൃശ്ചിക ലഗ്നം", "or": "ବିଛା ଲଗ୍ନ"},
    "ధనూ లగ్నం": {"en": "Sagittarius Lagnam", "hi": "धनु लग्न", "kn": "ಧನೂ ಲಗ್ನ", "ta": "தனுசு லக்னம்", "ml": "ധനു ലഗ്നം", "or": "ଧନୁ ଲଗ୍ନ"},
    "మకర లగ్నం": {"en": "Capricorn Lagnam", "hi": "मकर लग्न", "kn": "ಮಕರ ಲಗ್ನ", "ta": "மகர லக்னம்", "ml": "മകര ലഗ്നം", "or": "ମକର ଲଗ୍ନ"},
    "కుంభ లగ్నం": {"en": "Aquarius Lagnam", "hi": "कुंभ लग्न", "kn": "ಕುಂಭ ಲಗ್ನ", "ta": "கும்ப லக்னம்", "ml": "കുംഭ ലഗ്നം", "or": "କୁମ୍ଭ ଲଗ୍ନ"},
    "మీన లగ్నం": {"en": "Pisces Lagnam", "hi": "मीन लग्न", "kn": "ಮೀನ ಲಗ್ನ", "ta": "மீன லக்னம்", "ml": "മീന ലഗ്നം", "or": "ମୀନ ଲଗ୍ନ"},

    "మేష / వృషభ లగ్నం": {"en": "Aries / Taurus Lagnam", "hi": "मेष / वृषभ लग्न", "kn": "ಮೇಷ / ವೃಷಭ ಲಗ್ನ", "ta": "மேஷம் / ரிஷபம் லக்னம்", "ml": "മേടം / ഇടവം ലഗ്നം", "or": "ମେଷ / ବୃଷ ଲଗ୍ନ"},
    "వృషభ / మిథున లగ్నం": {"en": "Taurus / Gemini Lagnam", "hi": "वृषभ / मिथुन लग्न", "kn": "ವೃಷಭ / ಮಿಥುನ ಲಗ್ನ", "ta": "ரிஷபம் / மிதுனம் லக்னம்", "ml": "ഇടവം / മിഥുനം ലഗ്നം", "or": "ବୃଷ / ମିଥୁନ ଲଗ୍ନ"},
    "మిథున / కర్కాటక లగ్నం": {"en": "Gemini / Cancer Lagnam", "hi": "मिथुन / कर्क लग्न", "kn": "ಮಿಥುನ / ಕರ್ಕಾಟಕ ಲಗ್ನ", "ta": "மிதுனம் / கடகம் லக்னம்", "ml": "മിഥുനം / കർക്കടകം ലഗ്നം", "or": "ମିଥୁନ / କର୍କଟ ଲଗ୍ନ"},
    "సింహ / కన్యా లగ్నం": {"en": "Leo / Virgo Lagnam", "hi": "सिंह / कन्या लग्न", "kn": "सिंह / कन्या लग्न", "ta": "சிம்மம் / கன்னி லக்னம்", "ml": "ചിങ്ങം / കന്നി ലഗ്നം", "or": "ସିଂହ / କନ୍ୟା ଲଗ୍ନ"},
    "కన్యా / తులా లగ్నం": {"en": "Virgo / Libra Lagnam", "hi": "कन्या / तुला लग्न", "kn": "ಕನ್ಯಾ / ತುಲಾ ಲಗ್ನ", "ta": "கன்னி / துலாம் லக்னம்", "ml": "കന്നി / തുലാം ലഗ്നം", "or": "କନ୍ୟା / ତୁଳା ଲଗ୍ନ"},
    "తులా / వృశ్చిక లగ్నం": {"en": "Libra / Scorpio Lagnam", "hi": "तुला / वृश्चिक लग्न", "kn": "ತುಲಾ / ವೃಶ್ಚಿಕ ಲಗ್ನ", "ta": "துலாம் / விருச்சிகம் லக்னம்", "ml": "തുലാം / വൃശ്ചികം ലഗ്നം", "or": "ତୁଳା / ବିଛା ଲଗ୍ନ"},
    "ధనూ / మకర లగ్నం": {"en": "Sagittarius / Capricorn Lagnam", "hi": "धनु / मकर लग्न", "kn": "ಧನೂ / ಮಕರ ಲಗ್ನ", "ta": "தனுசு / மகரம் லக்னம்", "ml": "ധനു / മകരം ലഗ്നം", "or": "ଧନୁ / ମକର ଲଗ୍ନ"},
    "మకర / కుంభ లగ్నం": {"en": "Capricorn / Aquarius Lagnam", "hi": "मकर / कुंभ लग्न", "kn": "ಮಕರ / ಕುಂಭ ಲಗ್ನ", "ta": "மகரம் / கும்பம் லக்னம்", "ml": "മകരം / കുംഭം ലഗ്നം", "or": "ମକର / କୁମ୍ଭ ଲଗ୍ନ"},
    "కుంభ / మీన లగ్నం": {"en": "Aquarius / Pisces Lagnam", "hi": "कुंभ / मीन लग्न", "kn": "ಕುಂಭ / ಮೀನ ಲಗ್ನ", "ta": "கும்பம் / மீனம் லக்னம்", "ml": "കുംഭം / മീനം ലഗ്നം", "or": "କୁମ୍ଭ / ମୀନ ଲଗ୍ନ"}
}

PLANETS_MAP = {
    "సూర్యుడు": {"en": "Sun", "hi": "सूर्य", "kn": "ಸೂರ್ಯ", "ta": "சூரியன்", "ml": "സൂര്യൻ", "or": "ସୂର୍ଯ୍ୟ"},
    "చంద్రుడు": {"en": "Moon", "hi": "चंद्र", "kn": "ಚಂದ್ರ", "ta": "சந்திரன்", "ml": "ചന്ദ്രൻ", "or": "ଚନ୍ଦ୍ର"},
    "కుజుడు": {"en": "Mars", "hi": "मंगल", "kn": "ಮಂಗಳ", "ta": "செவ்வாய்", "ml": "ചൊവ്വ", "or": "ମଙ୍ଗଳ"},
    "బుధుడు": {"en": "Mercury", "hi": "बुध", "kn": "ಬುಧ", "ta": "புதன்", "ml": "ബുധൻ", "or": "ବୁଧ"},
    "గురువు": {"en": "Jupiter", "hi": "गुरु", "kn": "ಗುರು", "ta": "குரு", "ml": "വ്യാഴം", "or": "ଗୁରୁ"},
    "గురు": {"en": "Jupiter", "hi": "गुरु", "kn": "ಗುರು", "ta": "குரு", "ml": "വ്യാഴം", "or": "ଗୁରୁ"},
    "శుక్రుడు": {"en": "Venus", "hi": "शुक्र", "kn": "ಶುಕ್ರ", "ta": "சுக்கிரன்", "ml": "ശുക്രൻ", "or": "ଶୁକ୍ର"},
    "శని": {"en": "Saturn", "hi": "शनि", "kn": "ಶನಿ", "ta": "சனி", "ml": "ശനി", "or": "ଶନି"},
    "రాహువు": {"en": "Rahu", "hi": "राहु", "kn": "ರಾಹು", "ta": "ராகு", "ml": "രാഹു", "or": "ରାହୁ"},
    "కేతువు": {"en": "Ketu", "hi": "केतु", "kn": "ಕೇತು", "ta": "கேது", "ml": "കേതു", "or": "କେତୁ"},
    "భూమి": {"en": "Earth (Bhumi)", "hi": "पृथ्वी (भूमि)", "kn": "ಭೂಮಿ", "ta": "பூமி", "ml": "ഭൂമി", "or": "ଭୂମି"},
    "చిత్ర": {"en": "Chitra", "hi": "चित्र", "kn": "ಚಿತ್ರ", "ta": "சித்ரா", "ml": "ചിത്ര", "or": "ଚିତ୍ର"},
    "మిత్ర": {"en": "Mitra", "hi": "मित्र", "kn": "ಮಿತ್ರ", "ta": "மித்ரா", "ml": "മിത്ര", "or": "ମିତ୍ର"}
}

all_trans = {lang: {} for lang in langs}

for idx, item in enumerate(astrology_data.NAKSHATRAS_LIST):
    slug, name_te, name_en, lord_te, deity_te, rashi_te, symbol_te, letters = item
    num = idx + 1
    
    k_name_te = f"{name_te} నక్షత్రం"
    k_h1 = f"{name_te} నక్షత్రం: సంక్షిప్త వివరాలు మరియు ఫలితాలు"
    k_intro = f"{name_te} నక్షత్రం త్రైత జ్యోతిష్యంలో {num}వ నక్షత్రం. దీనికి అధిపతి {lord_te} మరియు దేవత {deity_te}."
    k_overview = f"{name_te} నక్షత్రానికి అధిపతిగా {lord_te} వ్యవహరిస్తారు. ఈ నక్షత్రం {rashi_te}లో ఉంటుంది."
    k_str1 = f"{lord_te} గ్రహ ప్రాభవం వల్ల కలిగే సద్గుణాలు"
    k_car = f"{lord_te} గ్రహానికి సంబంధించిన సాంకేతిక, పరిపాలనా లేదా సేవారంగాలు."
    k_faq_q1 = f"{name_te} నక్షత్రం ఏ లగ్నంలో ఉంటుంది?"
    k_faq_a1 = f"{name_te} నక్షత్రం {rashi_te}లో ఉంటుంది."
    k_faq_q2 = f"{name_te} నక్షత్ర అధిపతి ఎవరు?"
    k_faq_a2 = f"{lord_te} అధిపతి గ్రహం."

    for lang in langs:
        n_script = NAKSHATRAS_SCRIPT.get(slug, {}).get(lang, name_en)
        lord_l = PLANETS_MAP.get(lord_te, {}).get(lang, lord_te)
        rashi_l = RASHIS_SCRIPT.get(rashi_te, {}).get(lang, rashi_te)

        if lang == "en":
            all_trans[lang][k_name_te] = f"{n_script} Nakshatra"
            all_trans[lang][k_h1] = f"{n_script} Nakshatra: Overview & Results"
            all_trans[lang][k_intro] = f"{n_script} Nakshatra is the {num}th nakshatra in Thraitha Astrology. Its ruler planet is {lord_l} and deity is {deity_te}."
            all_trans[lang][k_overview] = f"{lord_l} rules {n_script} Nakshatra. This nakshatra resides in {rashi_l}."
            all_trans[lang][k_str1] = f"Positive qualities due to the influence of {lord_l}"
            all_trans[lang][k_car] = f"Technical, administrative, or service sectors related to {lord_l}."
            all_trans[lang][k_faq_q1] = f"Which Lagnam does {n_script} Nakshatra belong to?"
            all_trans[lang][k_faq_a1] = f"{n_script} Nakshatra resides in {rashi_l}."
            all_trans[lang][k_faq_q2] = f"Who is the ruling planet of {n_script} Nakshatra?"
            all_trans[lang][k_faq_a2] = f"{lord_l} is the ruling planet."
        elif lang == "hi":
            all_trans[lang][k_name_te] = f"{n_script} नक्षत्र"
            all_trans[lang][k_h1] = f"{n_script} नक्षत्र: विवरण और परिणाम"
            all_trans[lang][k_intro] = f"{n_script} नक्षत्र त्रैत ज्योतिष में {num}वां नक्षत्र है। इसके स्वामी {lord_l} हैं।"
            all_trans[lang][k_overview] = f"{lord_l} {n_script} नक्षत्र के स्वामी हैं। यह नक्षत्र {rashi_l} में स्थित है।"
            all_trans[lang][k_str1] = f"{lord_l} ग्रह के प्रभाव से प्राप्त सकारात्मक गुण"
            all_trans[lang][k_car] = f"{lord_l} ग्रह से संबंधित तकनीकी या प्रशासनिक क्षेत्र।"
            all_trans[lang][k_faq_q1] = f"{n_script} नक्षत्र किस लग्न में स्थित है?"
            all_trans[lang][k_faq_a1] = f"{n_script} नक्षत्र {rashi_l} में स्थित है।"
            all_trans[lang][k_faq_q2] = f"{n_script} नक्षत्र के स्वामी कौन हैं?"
            all_trans[lang][k_faq_a2] = f"{lord_l} स्वामी ग्रह हैं।"
        elif lang == "kn":
            all_trans[lang][k_name_te] = f"{n_script} ನಕ್ಷತ್ರ"
            all_trans[lang][k_h1] = f"{n_script} ನಕ್ಷತ್ರ: ಸಾರಾಂಶ ಮತ್ತು ಫಲಿತಾಂಶಗಳು"
            all_trans[lang][k_intro] = f"{n_script} ನಕ್ಷತ್ರವು ತ್ರೈತ ಜ್ಯೋತಿಷ್ಯದಲ್ಲಿ {num}ನೇ ನಕ್ಷತ್ರವಾಗಿದೆ. ಇದರ ಅಧಿಪತಿ {lord_l}."
            all_trans[lang][k_overview] = f"{lord_l} {n_script} ನಕ್ಷತ್ರದ ಅಧಿಪತಿ. ಈ ನಕ್ಷತ್ರವು {rashi_l} ನಲ್ಲಿದೆ."
            all_trans[lang][k_str1] = f"{lord_l} ಗ್ರಹದ ಪ್ರಭಾವದಿಂದ ಉಂಟಾಗುವ ಸದ್ಗುಣಗಳು"
            all_trans[lang][k_car] = f"{lord_l} ಗ್ರಹಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ತಾಂತ್ರಿಕ ಅಥವಾ ಸೇವಾ ಕ್ಷೇತ್ರಗಳು."
            all_trans[lang][k_faq_q1] = f"{n_script} ನಕ್ಷತ್ರವು ಯಾವ ಲಗ್ನದಲ್ಲಿದೆ?"
            all_trans[lang][k_faq_a1] = f"{n_script} ನಕ್ಷತ್ರವು {rashi_l} ನಲ್ಲಿದೆ."
            all_trans[lang][k_faq_q2] = f"{n_script} ನಕ್ಷತ್ರದ ಅಧಿಪತಿ ಯಾರು?"
            all_trans[lang][k_faq_a2] = f"{lord_l} ಅಧಿಪತಿ ಗ್ರಹ."
        elif lang == "ta":
            all_trans[lang][k_name_te] = f"{n_script} நட்சத்திரம்"
            all_trans[lang][k_h1] = f"{n_script} நட்சத்திரம்: கண்ணோட்டம் மற்றும் பலன்கள்"
            all_trans[lang][k_intro] = f"{n_script} நட்சத்திரம் த்ரைத ஜோதிடத்தில் {num}வது நட்சத்திரமாகும். இதன் அதிபதி {lord_l}."
            all_trans[lang][k_overview] = f"{lord_l} {n_script} நட்சத்திரத்தின் அதிபதியாவார். இந்த நட்சத்திரம் {rashi_l} இல் உள்ளது."
            all_trans[lang][k_str1] = f"{lord_l} கிரகத்தின் தாக்கத்தால் ஏற்படும் நற்குணங்கள்"
            all_trans[lang][k_car] = f"{lord_l} கிரகத்திற்குட்பட்ட சேவைத் துறைகள்."
            all_trans[lang][k_faq_q1] = f"{n_script} நட்சத்திரம் எந்த லக்னத்தில் உள்ளது?"
            all_trans[lang][k_faq_a1] = f"{n_script} நட்சத்திரம் {rashi_l} இல் உள்ளது."
            all_trans[lang][k_faq_q2] = f"{n_script} நட்சத்திரத்தின் அதிபதி யார்?"
            all_trans[lang][k_faq_a2] = f"{lord_l} அதிபதி கிரகமாவார்."
        elif lang == "ml":
            all_trans[lang][k_name_te] = f"{n_script} നക്ഷത്രം"
            all_trans[lang][k_h1] = f"{n_script} നക്ഷത്രം: അവലോകനവും ഫലങ്ങളും"
            all_trans[lang][k_intro] = f"{n_script} നക്ഷത്രം ത്രൈത ജ്യോതിഷത്തിൽ {num}-ാം നക്ഷത്രമാണ്. ഇതിന്റെ അധിപതി {lord_l} ആണ്."
            all_trans[lang][k_overview] = f"{lord_l} ആണ് {n_script} നക്ഷത്രത്തിന്റെ അധിപതി. ഈ നക്ഷത്രം {rashi_l} ൽ സ്ഥിതിചെയ്യുന്നു."
            all_trans[lang][k_str1] = f"{lord_l} ഗ്രഹത്തിന്റെ സ്വാധീനം കൊണ്ടുള്ള നല്ല ഗുണങ്ങൾ"
            all_trans[lang][k_car] = f"{lord_l} ഗ്രഹവുമായി ബന്ധപ്പെട്ട മേഖലകൾ."
            all_trans[lang][k_faq_q1] = f"{n_script} നക്ഷത്രം ഏത് ലഗ്നത്തിലാണ്?"
            all_trans[lang][k_faq_a1] = f"{n_script} നക്ഷത്രം {rashi_l} ൽ കാണപ്പെടുന്നു."
            all_trans[lang][k_faq_q2] = f"{n_script} നക്ഷത്രത്തിന്റെ അധിപതി ആരാണ്?"
            all_trans[lang][k_faq_a2] = f"{lord_l} അധിപതി ഗ്രഹമാണ്."
        elif lang == "or":
            all_trans[lang][k_name_te] = f"{n_script} ନକ୍ଷତ୍ର"
            all_trans[lang][k_h1] = f"{n_script} ନକ୍ଷତ୍ର: ସଂକ୍ଷିପ୍ତ ବିବରଣୀ ଏବଂ ଫଳାଫଳ"
            all_trans[lang][k_intro] = f"{n_script} ନକ୍ଷତ୍ର ତ୍ରୈତ ଜ୍ୟୋତିଷରେ {num}ତମ ନକ୍ଷତ୍ର। ଏହାର ଅଧିପତି {lord_l}।"
            all_trans[lang][k_overview] = f"{lord_l} {n_script} ନକ୍ଷତ୍ରର ଅଧିପତି। ଏହି ନକ୍ଷତ୍ର {rashi_l} ରେ ଅବସ୍ଥିତ।"
            all_trans[lang][k_str1] = f"{lord_l} ଗ୍ରହର ପ୍ରଭାବ ହେତୁ ସଦ୍ଗୁଣ"
            all_trans[lang][k_car] = f"{lord_l} ଗ୍ରହ ସମ୍ବନ୍ଧୀୟ କ୍ଷେତ୍ର।"
            all_trans[lang][k_faq_q1] = f"{n_script} ନକ୍ଷତ୍ର କେଉଁ ଲଗ୍ନରେ ଅବସ୍ଥିତ?"
            all_trans[lang][k_faq_a1] = f"{n_script} ନକ୍ଷତ୍ର {rashi_l} ରେ ରହିଥାଏ।"
            all_trans[lang][k_faq_q2] = f"{n_script} ନକ୍ଷତ୍ରର ଅଧିପତି କିଏ?"
            all_trans[lang][k_faq_a2] = f"{lord_l} ଅଧିପତି ଗ୍ରହ।"

# Merge and save into translations JSON files
for lang in langs:
    fpath = os.path.join(trans_dir, f"translations_{lang}.json")
    dict_data = {}
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            try:
                dict_data = json.load(f)
            except Exception:
                dict_data = {}

    for k, v in all_trans[lang].items():
        dict_data[k] = v

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(dict_data, f, ensure_ascii=False, indent=4)

    print(f"Successfully populated native script Nakshatra strings for {lang} ({len(dict_data)} total keys)")
