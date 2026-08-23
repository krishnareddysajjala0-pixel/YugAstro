# -*- coding: utf-8 -*-
with open('app.py', 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if 'set_lang' in line:
            print(f"app.py:{idx+1}: {line.strip()}")
