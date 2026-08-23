# -*- coding: utf-8 -*-
import re

with open('templates/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all script blocks
scripts = re.findall(r'<script[\s\S]*?</script>', content)

print(f"Found {len(scripts)} script blocks.")
for idx, s in enumerate(scripts):
    matches = re.findall(r'\{\{\s*_\([^\)]*\)\s*\}\}', s)
    if matches:
        print(f"=== Script Block {idx+1} has Jinja tags ===")
        for m in matches:
            print(" ", repr(m))
