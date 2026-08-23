# -*- coding: utf-8 -*-
with open('templates/chart.html', 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if 'split(' in line:
            print(f"chart.html:{idx+1}: {line.strip()}")

with open('templates/compare_results.html', 'r', encoding='utf-8') as f:
    for idx, line in enumerate(f):
        if 'split(' in line:
            print(f"compare_results.html:{idx+1}: {line.strip()}")
