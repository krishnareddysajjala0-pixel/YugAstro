# -*- coding: utf-8 -*-
with open('templates/chart.html', 'r', encoding='utf-8') as f:
    c = f.read()

print("Chart.html at 54370:")
print(repr(c[54320:54420]))
