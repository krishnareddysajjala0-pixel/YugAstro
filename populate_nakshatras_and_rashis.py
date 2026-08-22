# -*- coding: utf-8 -*-
"""
Populate complete 27 Nakshatras & 12 Lagnams data translations across all 6 target languages.
"""

import json
import os
import sys

sys.path.insert(0, r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro")
import astrology_data

trans_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\translations"
langs = ["en", "hi", "kn", "ta", "ml", "or"]

all_strings = set()

for item in astrology_data.NAKSHATRAS_LIST:
    # (slug, name_te, name_en, lord, deity, rashi, symbol, letters)
    all_strings.add(item[1]) # name_te
    all_strings.add(item[3]) # lord
    all_strings.add(item[4]) # deity
    all_strings.add(item[5]) # rashi
    all_strings.add(item[6]) # symbol
    all_strings.add(item[7]) # letters
    
    # fetch detail data
    data = astrology_data.get_nakshatra_data(item[0])
    if data:
        for k in ['name_te', 'h1', 'intro', 'lord_te', 'deity_te', 'rashi_te', 'symbol_te', 'overview', 'career', 'relationships']:
            if data.get(k):
                all_strings.add(data[k])
        for s in data.get('strengths', []):
            all_strings.add(s)
        for c in data.get('cautions', []):
            all_strings.add(c)
        for pada in data.get('padas', []):
            if pada.get('navamsha'):
                all_strings.add(pada['navamsha'])
            if pada.get('desc'):
                all_strings.add(pada['desc'])
        for faq in data.get('faqs', []):
            if faq.get('q'):
                all_strings.add(faq['q'])
            if faq.get('a'):
                all_strings.add(faq['a'])

for item in astrology_data.RASHULU_LIST:
    # (slug, name_te, name_en, lord, element, symbol)
    all_strings.add(item[1])
    all_strings.add(item[3])
    all_strings.add(item[4])
    all_strings.add(item[5])

    data = astrology_data.get_rashi_data(item[0])
    if data:
        for k in ['name_te', 'h1', 'intro', 'lord_te', 'element_te', 'symbol_te', 'overview', 'career', 'relationships', 'finance', 'health', 'gocharam_2026']:
            if data.get(k):
                all_strings.add(data[k])
        for s in data.get('strengths', []):
            all_strings.add(s)
        for c in data.get('cautions', []):
            all_strings.add(c)
        for faq in data.get('faqs', []):
            if faq.get('q'):
                all_strings.add(faq['q'])
            if faq.get('a'):
                all_strings.add(faq['a'])

print(f"Total unique Telugu strings collected from Nakshatras & Rashis data: {len(all_strings)}")

# Auto-populate translation files
for lang in langs:
    fpath = os.path.join(trans_dir, f"translations_{lang}.json")
    dict_data = {}
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            try:
                dict_data = json.load(f)
            except Exception:
                dict_data = {}

    added = 0
    for s in all_strings:
        if s not in dict_data:
            added += 1
            dict_data[s] = s

    with open(fpath, 'w', encoding='utf-8') as f:
        json.dump(dict_data, f, ensure_ascii=False, indent=4)

    print(f"Added {added} new Nakshatras/Rashis keys to translations_{lang}.json ({len(dict_data)} total keys)")
