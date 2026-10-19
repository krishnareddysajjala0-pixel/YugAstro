# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('bhava_conjunctions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for b in [1, 2, 4, 7, 10, 12]:
    print(f"=== Bhava {b} Sample ===")
    rules = data[str(b)]
    for r in rules[:2]:
        print(f"  {r['combination']} | {r['status']}")
        print(f"    {r['result'][:100]}...")
