# -*- coding: utf-8 -*-
import json
import sys

sys.path.insert(0, r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro")
import astrology_data

langs = ['en', 'hi', 'kn', 'ta', 'ml', 'or']

for lang in langs:
    fpath = f"translations/translations_{lang}.json"
    with open(fpath, 'r', encoding='utf-8') as f:
        mapping = json.load(f)
    
    print(f"=== {lang.upper()} RASHULU HUB TRANSLATION CHECK ===")
    untr = 0
    total = 0
    for slug, name_te, name_en, lord, element, symbol in astrology_data.RASHULU_LIST:
        for val in [name_te, lord, element, symbol]:
            total += 1
            tr_val = mapping.get(val)
            if not tr_val or tr_val == val:
                untr += 1
                print(f"  [UNTRANSLATED] '{val}' -> '{tr_val}'")
    print(f"Total untranslated in {lang}: {untr} / {total}")
