import json
import os

translations = {
    "en": {
        "మొబైల్ నంబర్": "Mobile Number",
        "10 అంకెల నంబర్": "10 digit number",
        "enter correct mobile number": "enter correct mobile number",
        "టెలిగ్రామ్‌లో జాతకం PDF పొందండి": "Receive Jatakam PDF on Telegram",
        "enter full name": "enter full name"
    },
    "hi": {
        "మొబైల్ నంబర్": "मोबाइल नंबर",
        "10 అంకెల నంబర్": "10 अंकों का नंबर",
        "enter correct mobile number": "कृपया सही मोबाइल नंबर दर्ज करें",
        "టెలిగ్రామ్‌లో జాతకం PDF పొందండి": "टेलीग्राम पर जातकम् PDF प्राप्त करें",
        "enter full name": "कृपया पूरा नाम दर्ज करें"
    },
    "ta": {
        "మొబైల్ నంబర్": "மொபைல் எண்",
        "10 అంకెల నంబర్": "10 இலக்க எண்",
        "enter correct mobile number": "சரியான மொபைல் எண்ணை உள்ளிடவும்",
        "టెలిగ్రామ్‌లో జాతకం PDF పొందండి": "டெலிகிராமில் ஜாதகம் PDF பெறவும்",
        "enter full name": "முழு பெயரை உள்ளிடவும்"
    },
    "kn": {
        "మొబైల్ నంబర్": "ಮೊಬೈಲ್ ಸಂಖ್ಯೆ",
        "10 అంకెల నంబర్": "10 ಅಂಕಿಯ ಸಂಖ್ಯೆ",
        "enter correct mobile number": "ಸರಿಯಾದ ಮೊಬೈಲ್ ಸಂಖ್ಯೆಯನ್ನು ನಮೂದಿಸಿ",
        "టెలిగ్రామ్‌లో జాతకం PDF పొందండి": "ಟೆಲಿಗ್ರಾಮ್‌ನಲ್ಲಿ ಜಾತಕ PDF ಪಡೆಯಿರಿ",
        "enter full name": "ಪೂರ್ಣ ಹೆಸರನ್ನು ನಮೂದಿಸಿ"
    },
    "ml": {
        "మొబైల్ నంబర్": "മൊബൈൽ നമ്പർ",
        "10 అంకెల നമ്പർ": "10 അക്ക നമ്പർ",
        "enter correct mobile number": "ശരിയായ മൊബൈൽ നമ്പർ നൽകുക",
        "టెలిగ్రామ్‌లో జాతకం PDF పొందండి": "ടെലിഗ്രാമിൽ ജാതകം PDF നേടുക",
        "enter full name": "മുഴുവൻ പേരും നൽകുക"
    },
    "or": {
        "మొబైల్ నంబర్": "ମୋବାଇଲ୍ ନମ୍ବର",
        "10 అంకెల నంబర్": "10 ଅଙ୍କ ବିଶିଷ୍ଟ ନମ୍ବର",
        "enter correct mobile number": "ସଠିକ୍ ମୋବାଇଲ୍ ନମ୍ବର ପ୍ରବେଶ କରନ୍ତୁ",
        "టెలిగ్రామ్‌లో జాతకం PDF పొందండి": "ଟେଲିଗ୍ରାମରେ ଜାତକମ PDF ପ୍ରାପ୍ତ କରନ୍ତୁ",
        "enter full name": "ପୂରା ନାମ ପ୍ରବେଶ କରନ୍ତୁ"
    }
}

base_dir = r"C:\Users\gnana\.gemini\antigravity\scratch\YugAstro\translations"

for lang, new_keys in translations.items():
    file_path = os.path.join(base_dir, f"translations_{lang}.json")
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        # Update with new keys
        for k, v in new_keys.items():
            data[k] = v
            
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Updated {lang}")
    else:
        print(f"File not found: {file_path}")
