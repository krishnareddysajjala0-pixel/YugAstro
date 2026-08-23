# -*- coding: utf-8 -*-
with open('templates/chart.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print("chart.html 1880-1890:")
for i in range(1880, 1890):
    if i < len(lines):
        print(f"{i+1}: {repr(lines[i])}")

with open('templates/compare_results.html', 'r', encoding='utf-8') as f:
    lines2 = f.readlines()
print("compare_results.html 1670-1680:")
for i in range(1670, 1680):
    if i < len(lines2):
        print(f"{i+1}: {repr(lines2[i])}")
