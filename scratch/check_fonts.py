# -*- coding: utf-8 -*-
import glob
import re

files = glob.glob('templates/*.html')
font_matches = []

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    matches = re.findall(r'font-family\s*:\s*([^;}"\']+)', content)
    for m in matches:
        m_str = m.strip()
        if 'var(--font' not in m_str and 'Font Awesome' not in m_str and 'FontAwesome' not in m_str:
            font_matches.append((fpath, m_str))

print('Total hardcoded font-family instances found:', len(font_matches))
for path, font in font_matches[:50]:
    print(f'  {path} -> {font}')
