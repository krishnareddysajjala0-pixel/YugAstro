# -*- coding: utf-8 -*-
with open('templates/chart.html', 'r', encoding='utf-8') as f:
    c = f.read()

idx = 52580
print("Context around 52580:")
print(repr(c[idx-50:idx+50]))
