# -*- coding: utf-8 -*-
import os
import csv
import json

os.makedirs('conjunction_rules', exist_ok=True)

with open('user_prompt_14412.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

rows = []
reader = csv.reader(lines)
for row in reader:
    if len(row) == 3 and row[0].startswith('1 + '):
        rows.append({
            "combination": row[0],
            "status": row[1],
            "result": row[2]
        })

with open('conjunction_rules/bhava1.py', 'w', encoding='utf-8') as out:
    out.write('# -*- coding: utf-8 -*-\n')
    out.write('"""Bhava 1 Conjunctions (Reference from UPENDRAA Thraitha)"""\n\n')
    out.write('BHAVA_1_RULES = ' + json.dumps(rows, ensure_ascii=False, indent=4) + '\n')

print(f"Successfully created conjunction_rules/bhava1.py with {len(rows)} rows.")
