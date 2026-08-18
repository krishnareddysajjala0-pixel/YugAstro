# -*- coding: utf-8 -*-
"""
RAVAN ASTRO VERSION 5 — Topic Rule Registry.
Defines allowed houses, planets, lordships, required keywords, and excluded keywords
for strict topic separation across all 40 topics.
"""

from typing import Dict, List, Any

TOPIC_DEFINITIONS: Dict[str, Dict[str, Any]] = {
    "వ్యక్తిత్వం": {
        "topic_id": "personality",
        "title_te": "వ్యక్తిత్వం",
        "allowed_houses": [1],
        "allowed_planets": ["సూర్యుడు", "చంద్రుడు"],
        "allowed_lords": [1],
        "keywords": ["వ్యక్తిత్వం", "స్వభావం", "మనస్తత్వం", "నడవడిక", "లగ్న"],
        "excluded_keywords": ["దేహకాంతి", "రోగం", "అప్పులు"]
    },
    "శరీర స్వభావం": {
        "topic_id": "body_nature",
        "title_te": "శరీర స్వభావం",
        "allowed_houses": [1],
        "allowed_planets": ["భూమి", "సూర్యుడు"],
        "allowed_lords": [1],
        "keywords": ["దేహం", "శరీరం", "రూపం", "కాంతి", "నిర్మాణం", "శారీరక"],
        "excluded_keywords": ["చదువు", "జ్ఞాపకశక్తి", "పెళ్లి"]
    },
    "ఆరోగ్యం": {
        "topic_id": "health",
        "title_te": "ఆరోగ్యం",
        "allowed_houses": [1, 6, 8, 12],
        "allowed_planets": ["సూర్యుడు", "కుజుడు", "శని", "మిత్ర"],
        "allowed_lords": [1, 6, 8, 12],
        "keywords": ["ఆరోగ్యం", "వ్యాధి", "రోగం", "చికిత్స", "బలం", "దేహము"],
        "excluded_keywords": ["పోటీ", "శత్రువులు", "వ్యాపారం"]
    },
    "విద్య": {
        "topic_id": "education",
        "title_te": "విద్య",
        "allowed_houses": [4, 5],
        "allowed_planets": ["బుధుడు", "గురు"],
        "allowed_lords": [4, 5],
        "keywords": ["విద్య", "చదువు", "పాఠశాల", "అభ్యాసం", "డిగ్రీ", "పరీక్షలు"],
        "excluded_keywords": ["సంతానం", "పిల్లలు", "పుత్రు", "జ్ఞాపకశక్తి"]
    },
    "మేధస్సు": {
        "topic_id": "intelligence",
        "title_te": "మేధస్సు",
        "allowed_houses": [5],
        "allowed_planets": ["బుధుడు", "గురు", "చంద్రుడు"],
        "allowed_lords": [5],
        "keywords": ["మేధస్సు", "బుద్ధి", "వివేకం", "జ్ఞాపకశక్తి", "తర్కం", "ఆలోచన"],
        "excluded_keywords": ["సంతానం", "పిల్లలు", "వంశాభివృద్ధి", "పాఠశాల"]
    },
    "ఉద్యోగం": {
        "topic_id": "job",
        "title_te": "ఉద్యోగం",
        "allowed_houses": [10, 6],
        "allowed_planets": ["శని", "సూర్యుడు"],
        "allowed_lords": [10, 6],
        "keywords": ["ఉద్యోగం", "సేవ", "కొలువు", "కార్యాలయం", "పని", "ఉద్యోగస్థితి"],
        "excluded_keywords": ["స్వతంత్ర వృత్తి", "వ్యాపార భాగస్వామి"]
    },
    "వృత్తి": {
        "topic_id": "career",
        "title_te": "వృత్తి",
        "allowed_houses": [10],
        "allowed_planets": ["శని", "బుధుడు"],
        "allowed_lords": [10],
        "keywords": ["వృత్తి", "జీవనోపాధి", "కెరీర్", "రంగం", "వృత్తి నైపుణ్యం"],
        "excluded_keywords": ["ఉద్యోగ సేవ", "ప్రభుత్వ నాయకత్వం"]
    },
    "వ్యాపారం": {
        "topic_id": "business",
        "title_te": "వ్యాపారం",
        "allowed_houses": [7, 10, 11],
        "allowed_planets": ["బుధుడు", "శుక్రుడు"],
        "allowed_lords": [7, 10, 11],
        "keywords": ["వ్యాపారం", "వాణిజ్యం", "వర్తకం", "భాగస్వామ్యం", "సరుకు"],
        "excluded_keywords": ["ఉద్యోగం", "కల్యాణం", "పెళ్లి"]
    },
    "ధనం": {
        "topic_id": "money",
        "title_te": "ధనం",
        "allowed_houses": [2, 11],
        "allowed_planets": ["గురు", "శుక్రుడు"],
        "allowed_lords": [2, 11],
        "keywords": ["ధనం", "సంపాదన", "నిధి", "ఆర్థిక సంపద", "నిల్వధనం"],
        "excluded_keywords": ["నెలవారీ రాబడి", "వ్యాపార లాభాలు"]
    },
    "ఆదాయం": {
        "topic_id": "income",
        "title_te": "ఆదాయం",
        "allowed_houses": [11, 2],
        "allowed_planets": ["గురు", "బుధుడు"],
        "allowed_lords": [11, 2],
        "keywords": ["ఆదాయం", "వరవడి", "నెలవారీ రాబడి", "ధనాగమనం", "రాబడి"],
        "excluded_keywords": ["నిల్వధనం", "ఆస్తి అమ్మకం"]
    },
    "కుటుంబం": {
        "topic_id": "family",
        "title_te": "కుటుంబం",
        "allowed_houses": [2, 4],
        "allowed_planets": ["గురు", "శుక్రుడు"],
        "allowed_lords": [2, 4],
        "keywords": ["కుటుంబం", "సభ్యులు", "బంధువులు", "వంశం", "గృహసభ్యులు"],
        "excluded_keywords": ["భార్య", "భర్త", "దాంపత్యం"]
    },
    "వివాహం": {
        "topic_id": "marriage",
        "title_te": "వివాహం",
        "allowed_houses": [7],
        "allowed_planets": ["శుక్రుడు", "గురు", "మిత్ర"],
        "allowed_lords": [7],
        "keywords": ["వివాహం", "కల్యాణం", "పెళ్లి", "పరిణయం", "శ్రీమతి/భర్త"],
        "excluded_keywords": ["కలహాలు", "విడాకులు", "సహజీవనం", "కాపురం"]
    },
    "దాంపత్యం": {
        "topic_id": "marital_life",
        "title_te": "దాంపత్యం",
        "allowed_houses": [7, 4, 12],
        "allowed_planets": ["శుక్రుడు", "మిత్ర"],
        "allowed_lords": [7, 4, 12],
        "keywords": ["దాంపత్యం", "సహజీవనం", "అనురాగం", "అనుబంధం", "కాపురం", "అన్యోన్యత"],
        "excluded_keywords": ["పెళ్లి సమయం", "వివాహ నిశ్చయం"]
    },
    "సంతానం": {
        "topic_id": "children",
        "title_te": "సంతానం",
        "allowed_houses": [5],
        "allowed_planets": ["గురు"],
        "allowed_lords": [5],
        "keywords": ["సంతానం", "పిల్లలు", "పుత్రు", "పుత్రిక", "వంశాభివృద్ధి"],
        "excluded_keywords": ["వివేకం", "జ్ఞాపకశక్తి", "చదువు"]
    },
    "తల్లి": {
        "topic_id": "mother",
        "title_te": "తల్లి",
        "allowed_houses": [4],
        "allowed_planets": ["చంద్రుడు"],
        "allowed_lords": [4],
        "keywords": ["తల్లి", "మాతృ", "అమ్మ", "మాతృసౌఖ్యం"],
        "excluded_keywords": ["నాన్న", "పితృ", "తండ్రి"]
    },
    "తండ్రి": {
        "topic_id": "father",
        "title_te": "తండ్రి",
        "allowed_houses": [9],
        "allowed_planets": ["సూర్యుడు"],
        "allowed_lords": [9],
        "keywords": ["తండ్రి", "పితృ", "నాన్న", "పిత్రార్జితం"],
        "excluded_keywords": ["అమ్మ", "మాతృ", "తల్లి"]
    },
    "సోదరులు": {
        "topic_id": "siblings",
        "title_te": "సోదరులు",
        "allowed_houses": [3],
        "allowed_planets": ["కుజుడు"],
        "allowed_lords": [3],
        "keywords": ["సోదర", "అన్న", "తమ్ముడు", "అక్క", "చెల్లెలు", "భ్రాతృ"],
        "excluded_keywords": ["భూమి", "వాహనం", "ఇల్లు"]
    },
    "గృహం": {
        "topic_id": "home",
        "title_te": "గృహం",
        "allowed_houses": [4],
        "allowed_planets": ["శుక్రుడు", "భూమి"],
        "allowed_lords": [4],
        "keywords": ["గృహం", "నివాసం", "ఇల్లు", "గృహసౌఖ్యం"],
        "excluded_keywords": ["కారు", "వాహనం", "పొలం"]
    },
    "వాహనం": {
        "topic_id": "vehicle",
        "title_te": "వాహనం",
        "allowed_houses": [4],
        "allowed_planets": ["శుక్రుడు"],
        "allowed_lords": [4],
        "keywords": ["వాహనం", "కారు", "రవాణా", "సవారి"],
        "excluded_keywords": ["ఇల్లు", "నివాసం", "స్థలం"]
    },
    "స్థిరాస్తి": {
        "topic_id": "property",
        "title_te": "స్థిరాస్తి",
        "allowed_houses": [4],
        "allowed_planets": ["కుజుడు", "భూమి"],
        "allowed_lords": [4],
        "keywords": ["స్థిరాస్తి", "భూమి", "స్థలం", "పొలం", "ఆస్తి"],
        "excluded_keywords": ["కారు", "వాహనం", "ఇల్లు నివాసం"]
    },
    "విదేశీ ప్రయాణం": {
        "topic_id": "foreign_travel",
        "title_te": "విదేశీ ప్రయాణం",
        "allowed_houses": [9, 12],
        "allowed_planets": ["రాహు", "కేతు", "చంద్రుడు"],
        "allowed_lords": [9, 12],
        "keywords": ["విదేశీ", "దూరప్రయాణం", "విదేశయాత్ర", "సముద్ర ప్రయాణం"],
        "excluded_keywords": ["పుణ్యక్షేత్రం", "తీర్థయాత్ర", "ఉపాసన"]
    },
    "తీర్థయాత్రలు": {
        "topic_id": "pilgrimage",
        "title_te": "తీర్థయాత్రలు",
        "allowed_houses": [9, 12],
        "allowed_planets": ["కేతు", "గురు"],
        "allowed_lords": [9, 12],
        "keywords": ["తీర్థయాత్ర", "పుణ్యక్షేత్రం", "యాత్ర", "దేవాలయ దర్శనం"],
        "excluded_keywords": ["విదేశీ ఉద్యోగం", "వ్యాపార పర్యటన"]
    },
    "ఆధ్యాత్మికత": {
        "topic_id": "spirituality",
        "title_te": "ఆధ్యాత్మికత",
        "allowed_houses": [9, 12],
        "allowed_planets": ["కేతు", "గురు", "చిత్ర"],
        "allowed_lords": [9, 12],
        "keywords": ["ఆధ్యాత్మిక", "ఉపాసన", "జపం", "సాధన", "ధర్మం"],
        "excluded_keywords": ["ధనం", "ఆస్తి", "లాభాలు", "రుణాలు"]
    },
    "శత్రువులు": {
        "topic_id": "enemies",
        "title_te": "శత్రువులు",
        "allowed_houses": [6, 8],
        "allowed_planets": ["కుజుడు", "శని", "రాహు"],
        "allowed_lords": [6, 8],
        "keywords": ["శత్రువులు", "విరోధులు", "మత్సరం", "వివాదాలు"],
        "excluded_keywords": ["అప్పులు", "రుణాలు", "రోగం"]
    },
    "ఋణాలు": {
        "topic_id": "debts",
        "title_te": "ఋణాలు",
        "allowed_houses": [6, 2, 12],
        "allowed_planets": ["శని", "కుజుడు"],
        "allowed_lords": [6, 2, 12],
        "keywords": ["ఋణాలు", "అప్పులు", "రుణభారం", "కిస్తీలు"],
        "excluded_keywords": ["శత్రువులు", "విరోధులు", "పోటీ"]
    },
    "పోటీ": {
        "topic_id": "competition",
        "title_te": "పోటీ",
        "allowed_houses": [6, 3, 11],
        "allowed_planets": ["కుజుడు", "సూర్యుడు", "రాహు"],
        "allowed_lords": [6, 3, 11],
        "keywords": ["పోటీ", "పరీక్షలు", "పోరాటం", "విజయం"],
        "excluded_keywords": ["వ్యాధి", "అప్పులు", "వైద్యం"]
    },
    "గౌరవం": {
        "topic_id": "honour",
        "title_te": "గౌరవం",
        "allowed_houses": [10, 1, 5, 9],
        "allowed_planets": ["సూర్యుడు", "గురు"],
        "allowed_lords": [10, 1, 5, 9],
        "keywords": ["గౌరవం", "కీర్తి", "మర్యాద", "ప్రతిష్ఠ"],
        "excluded_keywords": ["ఉపాసన", "మోక్షం", "జపం"]
    },
    "అధికార స్థానం": {
        "topic_id": "authority",
        "title_te": "అధికార స్థానం",
        "allowed_houses": [10, 1, 5, 9, 11],
        "allowed_planets": ["సూర్యుడు", "కుజుడు"],
        "allowed_lords": [10, 1, 5, 9, 11],
        "keywords": ["అధికారం", "పదవి", "ప్రభుత్వబలం", "నాయకత్వం"],
        "excluded_keywords": ["సాధారణ ఉద్యోగం", "వ్యాపారం"]
    },
    "లాభాలు": {
        "topic_id": "gains",
        "title_te": "లాభాలు",
        "allowed_houses": [11, 2, 9],
        "allowed_planets": ["గురు", "శుక్రుడు"],
        "allowed_lords": [11, 2, 9],
        "keywords": ["లాభాలు", "ఫలితప్రాప్తి", "ప్రయోజనం", "విజయం"],
        "excluded_keywords": ["నెలవారీ జీతం", "అప్పులు"]
    },
    "ఖర్చులు": {
        "topic_id": "expenses",
        "title_te": "ఖర్చులు",
        "allowed_houses": [12, 6, 8],
        "allowed_planets": ["శని", "రాహు"],
        "allowed_lords": [12, 6, 8],
        "keywords": ["ఖర్చులు", "వ్యయం", "నష్టం", "ధనవ్యయం"],
        "excluded_keywords": ["ఆధ్యాత్మికత", "మోక్షం", "జపం"]
    },
    "మోక్ష/ఆధ్యాత్మిక అంశాలు": {
        "topic_id": "moksha",
        "title_te": "మోక్ష/ఆధ్యాత్మిక అంశాలు",
        "allowed_houses": [12, 9, 8],
        "allowed_planets": ["కేతు", "చిత్ర"],
        "allowed_lords": [12, 9, 8],
        "keywords": ["మోక్షం", "ముక్తి", "వైరాగ్యం", "పరమార్థం"],
        "excluded_keywords": ["ఇల్లు", "వాహనం", "స్థిరాస్తి", "ధనం"]
    }
}
