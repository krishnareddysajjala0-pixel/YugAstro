# -*- coding: utf-8 -*-
"""
Populate complete 27 Nakshatras and 12 Lagnams dynamic translations across all 6 languages:
EN, HI, KN, TA, ML, OR.
"""

import json
import os
import sys

sys.path.insert(0, r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro")
import astrology_data

trans_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\translations"
langs = ["en", "hi", "kn", "ta", "ml", "or"]

# Planet mappings
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

# Common phrases mapping
PHRASES_MAP = {
    "కార్యదీక్ష మరియు స్వతంత్ర ఆలోచనలు": {
        "en": "Dedication to work and independent thinking",
        "hi": "कार्य के प्रति समर्पण और स्वतंत्र सोच",
        "kn": "ಕೆಲಸದ ಬಗ್ಗೆ ನಿಷ್ಠೆ ಮತ್ತು ಸ್ವತಂತ್ರ ಆಲೋಚನೆಗಳು",
        "ta": "வேலை ஈடுபாடு மற்றும் சுயசிந்தனை",
        "ml": "ജോലിയോടുള്ള ആത്മാർത്ഥതയും സ്വതന്ത്ര ചിന്തയും",
        "or": "କାର୍ଯ୍ୟ ପ୍ରତି ନିଷ୍ଠା ଏବଂ ସ୍ୱାଧୀନ ଚିନ୍ତା"
    },
    "తొందరపాటు నిర్ణయాలు తగ్గించుకోవడం మంచిది": {
        "en": "It is advisable to avoid hasty decisions",
        "hi": "जल्दबाजी में निर्णय लेने से बचना बेहतर है",
        "kn": "ಅತುರದ ನಿರ್ಧಾರಗಳನ್ನು ತಪ್ಪಿಸುವುದು ಒಳ್ಳೆಯದು",
        "ta": "அவசர முடிவுகளைத் தவிர்ப்பது நல்லது",
        "ml": "തിടുക്കപ്പെട്ട തീരുമാനങ്ങൾ ഒഴിവാക്കുന്നത് നല്ലതാണ്",
        "or": "ଅତି ଶୀଘ୍ର ନିଷ୍ପତ୍ତି ନେବାରୁ ନିବୃତ୍ତ ରହିବା ଭଲ"
    },
    "కుటుంబ బంధాలకు మరియు అనుబంధాలకు ప్రాధాన్యత ఇస్తారు.": {
        "en": "Priority is given to family bonds and relationships.",
        "hi": "पारिवारिक संबंधों और रिश्तों को प्राथमिकता दी जाती है।",
        "kn": "ಕುಟುಂಬದ ಸಂಬಂಧಗಳಿಗೆ ಆಧ್ಯತೆ ನೀಡಲಾಗುತ್ತದೆ.",
        "ta": "குடும்ப உறவுகளுக்கு முன்னுரிமை அளிக்கப்படுகிறது.",
        "ml": "കുടുംബ ബന്ധങ്ങൾക്ക് മുൻഗണന നൽകുന്നു.",
        "or": "ପାରିବାରିକ ସମ୍ପର୍କକୁ ପ୍ରାଥମିକତା ଦିଆଯାଏ।"
    },
    "మొదటి పాదంలో జన్మించిన వారికి శారీరక దృఢత్వం ఉంటుంది.": {
        "en": "Natives born in the 1st Pada possess physical strength.",
        "hi": "प्रथम पद में जन्मे जातकों में शारीरिक सुदृढ़ता होती है।",
        "kn": "ಮೊದಲ ಪಾದದಲ್ಲಿ ಜನಿಸಿದವರು ಶಾರೀರಿಕ ಬಲವನ್ನು ಹೊಂದಿರುತ್ತಾರೆ.",
        "ta": "முதல் பாதத்தில் பிறந்தவர்கள் உடல் வலிமை பெற்றிருப்பார்கள்.",
        "ml": "ഒന്നാം പാദത്തിൽ ജനിച്ചവർക്ക് ശാരീരിക ദൃഢതയുണ്ടാകും.",
        "or": "ପ୍ରଥମ ପାଦରେ ଜନ୍ମିତ ବ୍ୟକ୍ତିଙ୍କର ଶାରୀରିକ ଶକ୍ତି ଥାଏ।"
    },
    "రెండవ పాదంలో జన్మించిన వారికి బుద్ధి బలం పెరుగుతుంది.": {
        "en": "Natives born in the 2nd Pada experience enhanced intellect.",
        "hi": "द्वितीय पद में जन्मे जातकों का बुद्धि बल बढ़ता है।",
        "kn": "ಎರಡನೇ ಪಾದದಲ್ಲಿ ಜನಿಸಿದವರ ಬುದ್ಧಿಶಕ್ತಿ ಹೆಚ್ಚಾಗುತ್ತದೆ.",
        "ta": "இரண்டாம் பாதத்தில் பிறந்தவர்களுக்கு அறிவுத்திறன் அதிகரிக்கும்.",
        "ml": "രണ്ടാം പാദത്തിൽ ജനിച്ചവർക്ക് ബുദ്ധിശക്തി വർദ്ധിക്കുന്നു.",
        "or": "ଦ୍ୱିତୀୟ ପାଦରେ ଜନ୍ମିତ ବ୍ୟକ୍ତିଙ୍କର ବୁଦ୍ଧିଶକ୍ତି ବୃଦ୍ଧି ପାଏ।"
    },
    "మూడవ పాదంలో జన్మించిన వారికి సృజనాత్మకత ఉంటుంది.": {
        "en": "Natives born in the 3rd Pada possess creativity.",
        "hi": "तृतीय पद में जन्मे जातक रचनात्मक होते हैं।",
        "kn": "ಮೂರನೇ ಪಾದದಲ್ಲಿ ಜನಿಸಿದವರು ಸೃಜನಶೀಲತೆಯನ್ನು ಹೊಂದಿರುತ್ತಾರೆ.",
        "ta": "மூன்றாம் பாதத்தில் பிறந்தவர்கள் படைப்பாற்றல் மிக்கவர்கள்.",
        "ml": "മൂന്നാം പാദത്തിൽ ജനിച്ചവർക്ക് സർഗ്ഗാത്മകതയുണ്ടാകും.",
        "or": "ତୃତୀୟ ପାଦରେ ଜନ୍ମିତ ବ୍ୟକ୍ତିଙ୍କର ସୃଜନଶୀଳତା ଥାଏ।"
    },
    "నాల్గవ పాదంలో జన్మించిన వారికి సుఖసంతోషాలు లభిస్తాయి.": {
        "en": "Natives born in the 4th Pada enjoy happiness and prosperity.",
        "hi": "चतुर्थ पद में जन्मे जातकों को सुख-समृद्धि प्राप्त होती है।",
        "kn": "ನಾಲ್ಕನೇ ಪಾದದಲ್ಲಿ ಜನಿಸಿದವರಿಗೆ ಸುಖ-ಸಂತೋಷ ದೊರೆಯುತ್ತದೆ.",
        "ta": "நான்காம் பாதத்தில் பிறந்தவர்கள் மகிழ்ச்சியும் வளமும் பெறுவார்கள்.",
        "ml": "നാലാം പാദത്തിൽ ജനിച്ചവർക്ക് സന്തോഷവും സുഖവും ലഭിക്കും.",
        "or": "ଚତୁର୍ଥ ପାଦରେ ଜନ୍ମିତ ବ୍ୟକ୍ତିଙ୍କୁ ସୁଖଶାନ୍ତି ମିଳିଥାଏ।"
    },
    "కార్య స్థిరత్వం": {
        "en": "Stability in work",
        "hi": "कार्य की स्थिरता",
        "kn": "ಕೆಲಸದ ಸ್ಥಿರತೆ",
        "ta": "வேலையில் സ്ഥിരത",
        "ml": "ജോലിയിലെ സ്ഥിരത",
        "or": "କାର୍ଯ୍ୟର ସ୍ଥିରତା"
    },
    "ఒత్తిడికి లోనుకాకుండా ఉండడం మంచిది": {
        "en": "It is good to avoid stress",
        "hi": "तनाव से बचना उचित है",
        "kn": "ಒತ್ತಡಕ್ಕೆ ಒಳಗಾಗದಿರುವುದು ಒಳ್ಳೆಯದು",
        "ta": "மன அழுத்தத்தைத் தவிர்ப்பது நல்லது",
        "ml": "സമ്മർദ്ദം ഒഴിവാക്കുന്നത് നല്ലതാണ്",
        "or": "ମାନସିକ ଚାପରୁ ନିବୃତ୍ତ ରହିବା ଭଲ"
    },
    "బంధాలలో నమ్మకం మరియు ప్రేమను చూపుతారు.": {
        "en": "They demonstrate trust and love in relationships.",
        "hi": "वे रिश्तों में विश्वास और प्रेम दिखाते हैं।",
        "kn": "ಅವರು ಸಂಬಂಧಗಳಲ್ಲಿ ನಂಬಿಕೆ ಮತ್ತು ಪ್ರೀತಿಯನ್ನು ತೋರಿಸುತ್ತಾರೆ.",
        "ta": "அவர்கள் உறவுகளில் நம்பிக்கையும் அன்பும் செலுத்துவார்கள்.",
        "ml": "അവർ ബന്ധങ്ങളിൽ വിശ്വാസവും സ്നേഹവും പ്രകടിപ്പിക്കുന്നു.",
        "or": "ସେମାନେ ସମ୍ପର୍କରେ ବିଶ୍ୱାସ ଏବଂ ସ୍ନେହ ପ୍ରଦର୍ଶନ କରନ୍ତି।"
    },
    "ఆర్థిక స్థిరత్వానికి ప్రాధాన్యత ఇస్తారు.": {
        "en": "They give priority to financial stability.",
        "hi": "वे वित्तीय स्थिरता को प्राथमिकता देते हैं।",
        "kn": "ಅವರು ಆರ್ಥಿಕ ಸ್ಥಿರತೆಗೆ ಆದ್ಯತೆ ನೀಡುತ್ತಾರೆ.",
        "ta": "அவர்கள் நிதி സ്ഥിരතාවയ്ക്ക് முன்னுரிமை அளிக்கிறார்கள்.",
        "ml": "അവർ സാമ്പത്തിക ഭദ്രതയ്ക്ക് മുൻഗണന നൽകുന്നു.",
        "or": "ସେମାନେ ଆର୍ଥିକ ସ୍ଥିରତାକୁ ପ୍ରାଥମିକତା ଦିଅନ୍ତି।"
    },
    "సాధారణ ఆరోగ్య జాగ్రత్తలు అవసరం.": {
        "en": "General health precautions are required.",
        "hi": "सामान्य स्वास्थ्य सावधानियों की आवश्यकता है।",
        "kn": "ಸಾಮಾನ್ಯ ಆರೋಗ್ಯ ಮುನ್ನೆಚ್ಚರಿಕೆಗಳು ಅಗತ್ಯವಿದೆ.",
        "ta": "பொதுவான சுகாதார முன்னெச்சரிக்கைகள் தேவை.",
        "ml": "സാധാരണ ആരോഗ്യ ജാഗ്രത ആവശ്യമാണ്.",
        "or": "ସାଧାରଣ ସ୍ୱାସ୍ଥ୍ୟ ସତର୍କତା ଆବଶ୍ୟକ।"
    },
    "2026 గోచారాలు అనుకూల మార్పులను అందిస్తాయి.": {
        "en": "2026 transits bring favorable changes.",
        "hi": "2026 का गोचर अनुकूल परिवर्तन लाएगा।",
        "kn": "2026 ರ ಗೋಚಾರಗಳು ಅನುಕೂಲಕರ ಬದಲಾವಣೆಗಳನ್ನು ನೀಡುತ್ತವೆ.",
        "ta": "2026 பெயர்ச்சிகள் சாதகமான மாற்றங்களைத் தரும்.",
        "ml": "2026 ഗോചാരം അനുകൂല മാറ്റങ്ങൾ കൊണ്ടുവരും.",
        "or": "୨୦୨୬ ଗୋଚର ଅନୁକୂଳ ପରିବର୍ତ୍ତନ ଆଣିବ।"
    }
}

# Construct translations for all 27 Nakshatras and 12 Lagnams
all_trans = {lang: {} for lang in langs}

# Add static PHRASES_MAP to all_trans
for te_k, v_map in PHRASES_MAP.items():
    for lang in langs:
        all_trans[lang][te_k] = v_map[lang]

for idx, item in enumerate(astrology_data.NAKSHATRAS_LIST):
    slug, name_te, name_en, lord_te, deity_te, rashi_te, symbol_te, letters = item
    num = idx + 1
    
    # te keys generated by get_nakshatra_data
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
        lord_l = PLANETS_MAP.get(lord_te, {}).get(lang, lord_te)
        
        if lang == "en":
            all_trans[lang][k_name_te] = f"{name_en} Nakshatra"
            all_trans[lang][k_h1] = f"{name_en} Nakshatra: Overview & Results"
            all_trans[lang][k_intro] = f"{name_en} Nakshatra is the {num}th nakshatra in Thraitha Astrology. Its ruler planet is {lord_l} and deity is {deity_te}."
            all_trans[lang][k_overview] = f"{lord_l} rules {name_en} Nakshatra. This nakshatra resides in {rashi_te}."
            all_trans[lang][k_str1] = f"Positive qualities due to the influence of {lord_l}"
            all_trans[lang][k_car] = f"Technical, administrative, or service sectors related to {lord_l}."
            all_trans[lang][k_faq_q1] = f"Which Lagnam does {name_en} Nakshatra belong to?"
            all_trans[lang][k_faq_a1] = f"{name_en} Nakshatra resides in {rashi_te}."
            all_trans[lang][k_faq_q2] = f"Who is the ruling planet of {name_en} Nakshatra?"
            all_trans[lang][k_faq_a2] = f"{lord_l} is the ruling planet."
        elif lang == "hi":
            all_trans[lang][k_name_te] = f"{name_en} नक्षत्र"
            all_trans[lang][k_h1] = f"{name_en} नक्षत्र: विवरण और परिणाम"
            all_trans[lang][k_intro] = f"{name_en} नक्षत्र त्रैत ज्योतिष में {num}वां नक्षत्र है। इसके स्वामी {lord_l} हैं।"
            all_trans[lang][k_overview] = f"{lord_l} {name_en} नक्षत्र के स्वामी हैं। यह नक्षत्र {rashi_te} में स्थित है।"
            all_trans[lang][k_str1] = f"{lord_l} ग्रह के प्रभाव से प्राप्त सकारात्मक गुण"
            all_trans[lang][k_car] = f"{lord_l} ग्रह से संबंधित तकनीकी या प्रशासनिक क्षेत्र।"
            all_trans[lang][k_faq_q1] = f"{name_en} नक्षत्र किस लग्न में स्थित है?"
            all_trans[lang][k_faq_a1] = f"{name_en} नक्षत्र {rashi_te} में स्थित है।"
            all_trans[lang][k_faq_q2] = f"{name_en} नक्षत्र के स्वामी कौन हैं?"
            all_trans[lang][k_faq_a2] = f"{lord_l} स्वामी ग्रह हैं।"
        elif lang == "kn":
            all_trans[lang][k_name_te] = f"{name_en} ನಕ್ಷತ್ರ"
            all_trans[lang][k_h1] = f"{name_en} ನಕ್ಷತ್ರ: ಸಾರಾಂಶ ಮತ್ತು ಫಲಿತಾಂಶಗಳು"
            all_trans[lang][k_intro] = f"{name_en} ನಕ್ಷತ್ರವು ತ್ರೈತ ಜ್ಯೋತಿಷ್ಯದಲ್ಲಿ {num}ನೇ ನಕ್ಷತ್ರವಾಗಿದೆ. ಇದರ ಅಧಿಪತಿ {lord_l}."
            all_trans[lang][k_overview] = f"{lord_l} {name_en} ನಕ್ಷತ್ರದ ಅಧಿಪತಿ. ಈ ನಕ್ಷತ್ರವು {rashi_te} ನಲ್ಲಿದೆ."
            all_trans[lang][k_str1] = f"{lord_l} ಗ್ರಹದ ಪ್ರಭಾವದಿಂದ ಉಂಟಾಗುವ ಸದ್ಗುಣಗಳು"
            all_trans[lang][k_car] = f"{lord_l} ಗ್ರಹಕ್ಕೆ ಸಂಬಂಧಿಸಿದ ತಾಂತ್ರಿಕ ಅಥವಾ ಸೇವಾ ಕ್ಷೇತ್ರಗಳು."
            all_trans[lang][k_faq_q1] = f"{name_en} ನಕ್ಷತ್ರವು ಯಾವ ಲಗ್ನದಲ್ಲಿದೆ?"
            all_trans[lang][k_faq_a1] = f"{name_en} ನಕ್ಷತ್ರವು {rashi_te} ನಲ್ಲಿದೆ."
            all_trans[lang][k_faq_q2] = f"{name_en} ನಕ್ಷತ್ರದ ಅಧಿಪತಿ ಯಾರು?"
            all_trans[lang][k_faq_a2] = f"{lord_l} ಅಧಿಪತಿ ಗ್ರಹ."
        elif lang == "ta":
            all_trans[lang][k_name_te] = f"{name_en} நட்சத்திரம்"
            all_trans[lang][k_h1] = f"{name_en} நட்சத்திரம்: கண்ணோட்டம் மற்றும் பலன்கள்"
            all_trans[lang][k_intro] = f"{name_en} நட்சத்திரம் த்ரைத ஜோதிடத்தில் {num}வது நட்சத்திரமாகும். இதன் அதிபதி {lord_l}."
            all_trans[lang][k_overview] = f"{lord_l} {name_en} நட்சத்திரத்தின் அதிபதியாவார். இந்த நட்சத்திரம் {rashi_te} இல் உள்ளது."
            all_trans[lang][k_str1] = f"{lord_l} கிரகத்தின் தாக்கத்தால் ஏற்படும் நற்குணங்கள்"
            all_trans[lang][k_car] = f"{lord_l} கிரகத்திற்குட்பட்ட சேவைத் துறைகள்."
            all_trans[lang][k_faq_q1] = f"{name_en} நட்சத்திரம் எந்த லக்னத்தில் உள்ளது?"
            all_trans[lang][k_faq_a1] = f"{name_en} நட்சத்திரம் {rashi_te} இல் உள்ளது."
            all_trans[lang][k_faq_q2] = f"{name_en} நட்சத்திரத்தின் அதிபதி யார்?"
            all_trans[lang][k_faq_a2] = f"{lord_l} அதிபதி கிரகமாவார்."
        elif lang == "ml":
            all_trans[lang][k_name_te] = f"{name_en} നക്ഷത്രം"
            all_trans[lang][k_h1] = f"{name_en} നക്ഷത്രം: അവലോകനവും ഫലങ്ങളും"
            all_trans[lang][k_intro] = f"{name_en} നക്ഷത്രം ത്രൈത ജ്യോതിഷത്തിൽ {num}-ാം നക്ഷത്രമാണ്. ഇതിന്റെ അധിപതി {lord_l} ആണ്."
            all_trans[lang][k_overview] = f"{lord_l} ആണ് {name_en} നക്ഷത്രത്തിന്റെ അധിപതി. ഈ നക്ഷത്രം {rashi_te} ൽ സ്ഥിതിചെയ്യുന്നു."
            all_trans[lang][k_str1] = f"{lord_l} ഗ്രഹത്തിന്റെ സ്വാധീനം കൊണ്ടുള്ള നല്ല ഗുണങ്ങൾ"
            all_trans[lang][k_car] = f"{lord_l} ഗ്രഹവുമായി ബന്ധപ്പെട്ട മേഖലകൾ."
            all_trans[lang][k_faq_q1] = f"{name_en} നക്ഷത്രം ഏത് ലഗ്നത്തിലാണ്?"
            all_trans[lang][k_faq_a1] = f"{name_en} നക്ഷത്രം {rashi_te} ൽ കാണപ്പെടുന്നു."
            all_trans[lang][k_faq_q2] = f"{name_en} നക്ഷത്രത്തിന്റെ അധിപതി ആരാണ്?"
            all_trans[lang][k_faq_a2] = f"{lord_l} അധിപതി ഗ്രഹമാണ്."
        elif lang == "or":
            all_trans[lang][k_name_te] = f"{name_en} ନକ୍ଷତ୍ର"
            all_trans[lang][k_h1] = f"{name_en} ନକ୍ଷତ୍ର: ସଂକ୍ଷିପ୍ତ ବିବରଣୀ ଏବଂ ଫଳାଫଳ"
            all_trans[lang][k_intro] = f"{name_en} ନକ୍ଷତ୍ର ତ୍ରୈତ ଜ୍ୟୋତିଷରେ {num}ତମ ନକ୍ଷତ୍ର। ଏହାର ଅଧିପତି {lord_l}।"
            all_trans[lang][k_overview] = f"{lord_l} {name_en} ନକ୍ଷତ୍ରର ଅଧିପତି। ଏହି ନକ୍ଷତ୍ର {rashi_te} ରେ ଅବସ୍ଥିତ।"
            all_trans[lang][k_str1] = f"{lord_l} ଗ୍ରହର ପ୍ରଭାବ ହେତୁ ସଦ୍ଗୁଣ"
            all_trans[lang][k_car] = f"{lord_l} ଗ୍ରହ ସମ୍ବନ୍ଧୀୟ କ୍ଷେତ୍ର।"
            all_trans[lang][k_faq_q1] = f"{name_en} ନକ୍ଷତ୍ର କେଉଁ ଲଗ୍ନରେ ଅବସ୍ଥିତ?"
            all_trans[lang][k_faq_a1] = f"{name_en} ନକ୍ଷତ୍ର {rashi_te} ରେ ରହିଥାଏ।"
            all_trans[lang][k_faq_q2] = f"{name_en} ନକ୍ଷତ୍ରର ଅଧିପତି କିଏ?"
            all_trans[lang][k_faq_a2] = f"{lord_l} ଅଧିପତି ଗ୍ରହ।"

for idx, item in enumerate(astrology_data.RASHULU_LIST):
    slug, name_te, name_en, lord_te, element_te, symbol_te = item
    
    k_h1 = f"{name_te}: స్వభావం, లగ్నాధిపతి {lord_te}"
    k_intro = f"{name_te} కి లగ్నాధిపతి {lord_te} మరియు తత్వం {element_te}."
    k_overview = f"{name_te} జాతకులు {element_te} లక్షణాలను కలిగి ఉంటారు. {lord_te} ఈ లగ్నానికి అధిపతిగా వ్యవహరిస్తారు."
    k_str1 = f"{lord_te} లగ్నాధిపతి ఆధిపత్యం వల్ల కలిగే బలాలు"
    k_car = f"{lord_te} గ్రహ ప్రభావానికి అనుకూలమైన రంగాలు."
    k_faq_q = f"{name_te} లగ్నానికి లగ్నాధిపతి ఎవరు?"
    k_faq_a = f"{lord_te} ఈ లగ్నానికి లగ్నాధిపతి."

    for lang in langs:
        lord_l = PLANETS_MAP.get(lord_te, {}).get(lang, lord_te)
        
        if lang == "en":
            all_trans[lang][k_h1] = f"{name_en} Lagnam: Nature & Lagnam Lord {lord_l}"
            all_trans[lang][k_intro] = f"The Lagnam lord of {name_en} is {lord_l} and its element is {element_te}."
            all_trans[lang][k_overview] = f"Natives of {name_en} possess {element_te} traits. {lord_l} rules as the Lagnam lord."
            all_trans[lang][k_str1] = f"Strengths due to the rulership of Lagnam lord {lord_l}"
            all_trans[lang][k_car] = f"Fields favorable to the influence of {lord_l}."
            all_trans[lang][k_faq_q] = f"Who is the Lagnam lord for {name_en} Lagnam?"
            all_trans[lang][k_faq_a] = f"{lord_l} is the Lagnam lord for this Lagnam."
        elif lang == "hi":
            all_trans[lang][k_h1] = f"{name_en} लग्न: स्वभाव, लग्नाधिपति {lord_l}"
            all_trans[lang][k_intro] = f"{name_en} लग्न के स्वामी {lord_l} हैं और तत्व {element_te} है।"
            all_trans[lang][k_overview] = f"{name_en} लग्न के जातक {element_te} गुण रखते हैं। {lord_l} इस लग्न के स्वामी हैं।"
            all_trans[lang][k_str1] = f"लग्नाधिपति {lord_l} के आधिपत्य से प्राप्त शक्तियां"
            all_trans[lang][k_car] = f"{lord_l} ग्रह के प्रभाव के अनुकूल क्षेत्र।"
            all_trans[lang][k_faq_q] = f"{name_en} लग्न का स्वामी कौन है?"
            all_trans[lang][k_faq_a] = f"{lord_l} इस लग्न के स्वामी हैं।"
        elif lang == "kn":
            all_trans[lang][k_h1] = f"{name_en} ಲಗ್ನ: ಸ್ವಭಾವ, ಲಗ್ನಾಧಿಪತಿ {lord_l}"
            all_trans[lang][k_intro] = f"{name_en} ಲಗ್ನದ ಅಧಿಪತಿ {lord_l} ಮತ್ತು ತತ್ವ {element_te}."
            all_trans[lang][k_overview] = f"{name_en} ಲಗ್ನದ ಜಾತಕರು {element_te} ಗುಣಗಳನ್ನು ಹೊಂದಿರುತ್ತಾರೆ. {lord_l} ಈ ಲಗ್ನದ ಅಧಿಪತಿಯಾಗಿದ್ದಾರೆ."
            all_trans[lang][k_str1] = f"ಲಗ್ನಾಧಿಪತಿ {lord_l} ಅವರ ಆಧಿಪತ್ಯದಿಂದ ಉಂಟಾಗುವ ಬಲಗಳು"
            all_trans[lang][k_car] = f"{lord_l} ಗ್ರಹದ ಪ್ರಭಾವಕ್ಕೆ ಅನುಕೂಲಕರವಾದ ಕ್ಷೇತ್ರಗಳು."
            all_trans[lang][k_faq_q] = f"{name_en} ಲಗ್ನಕ್ಕೆ ಅಧಿಪತಿ ಯಾರು?"
            all_trans[lang][k_faq_a] = f"{lord_l} ಈ ಲಗ್ನಕ್ಕೆ ಅಧಿಪತಿ."
        elif lang == "ta":
            all_trans[lang][k_h1] = f"{name_en} லக்னம்: இயல்பு, லக்னாதிபதி {lord_l}"
            all_trans[lang][k_intro] = f"{name_en} லக்னத்தின் அதிபதி {lord_l} மற்றும் தத்துவம் {element_te}."
            all_trans[lang][k_overview] = f"{name_en} லக்ன அன்பர்கள் {element_te} குணங்களைக் கொண்டுள்ளனர். {lord_l} இந்த லக்னத்தின் அதிபதியாவார்."
            all_trans[lang][k_str1] = f"லக்னாதிபதி {lord_l} அவர்களின் ஆதிக்கத்தால் ஏற்படும் பலன்கள்"
            all_trans[lang][k_car] = f"{lord_l} கிரகத்தின் தாக்கத்திற்கு உகந்த துறைகள்."
            all_trans[lang][k_faq_q] = f"{name_en} லக்னத்திற்கு அதிபதி யார்?"
            all_trans[lang][k_faq_a] = f"{lord_l} இந்த லக்னத்தின் அதிபதியாவார்."
        elif lang == "ml":
            all_trans[lang][k_h1] = f"{name_en} ലഗ്നം: സ്വഭാവം, ലഗ്നാധിപതി {lord_l}"
            all_trans[lang][k_intro] = f"{name_en} ലഗ്നത്തിന്റെ അധിപതി {lord_l} ഉം തത്വം {element_te} ഉം ആണ്."
            all_trans[lang][k_overview] = f"{name_en} ലഗ്നക്കാർ {element_te} സവിശേഷതകൾ പുലർത്തുന്നു. {lord_l} ഈ ലഗ്നത്തിന്റെ അധിപതിയാണ്."
            all_trans[lang][k_str1] = f"ലഗ്നാധിപതി {lord_l} അധിപത്യം നൽകുന്ന ശക്തികൾ"
            all_trans[lang][k_car] = f"{lord_l} ഗ്രഹത്തിന്റെ സ്വാധീനത്തിന് അനുകൂലമായ മേഖലകൾ."
            all_trans[lang][k_faq_q] = f"{name_en} ലഗ്നത്തിന്റെ അധിപതി ആരാണ്?"
            all_trans[lang][k_faq_a] = f"{lord_l} ഈ ലഗ്നത്തിന്റെ അധിപതിയാണ്."
        elif lang == "or":
            all_trans[lang][k_h1] = f"{name_en} ଲଗ୍ନ: ସ୍ୱଭାବ, ଲଗ୍ନାଧିପତି {lord_l}"
            all_trans[lang][k_intro] = f"{name_en} ଲଗ୍ନର ଅଧିପତି {lord_l} ଏବଂ ତତ୍ତ୍ୱ {element_te}।"
            all_trans[lang][k_overview] = f"{name_en} ଲଗ୍ନର ବ୍ୟକ୍ତିମାନେ {element_te} ଗୁଣ ବହନ କରନ୍ତି। {lord_l} ଏହି ଲଗ୍ନର ଅଧିପତି।"
            all_trans[lang][k_str1] = f"ଲଗ୍ନାଧିପତି {lord_l}ଙ୍କ ପ୍ରଭାବ ହେତୁ ବଳ"
            all_trans[lang][k_car] = f"{lord_l} ଗ୍ରହର ପ୍ରଭାବ ପାଇଁ ଅନୁକୂଳ କ୍ଷେତ୍ର।"
            all_trans[lang][k_faq_q] = f"{name_en} ଲଗ୍ନର ଅଧିପତି କିଏ?"
            all_trans[lang][k_faq_a] = f"{lord_l} ଏହି ଲଗ୍ନର ଅଧିପତି।"

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

    print(f"Successfully populated {len(all_trans[lang])} Nakshatra/Rashi translated strings for {lang} (Total keys: {len(dict_data)})")
