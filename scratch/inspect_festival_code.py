# -*- coding: utf-8 -*-
with open('app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    if any(k in line for k in ['festival', 'festivals', 'పండుగ', 'సంక్రాంతి', ' calendar_view']):
        print(f"app.py:{idx+1}: {line.strip()[:100]}")
