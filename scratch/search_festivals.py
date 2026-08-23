# -*- coding: utf-8 -*-
import os, glob

files = glob.glob('**/*.py', recursive=True) + glob.glob('**/*.html', recursive=True) + glob.glob('**/*.json', recursive=True)

festival_keywords = ['సంక్రాంతి', 'ఉగాది', 'వినాయక', 'దీపావళి', 'పండుగ', 'festivals', 'FESTIVALS']

for fpath in files:
    if '.git' in fpath or 'venv' in fpath or '__pycache__' in fpath:
        continue
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
            for kw in festival_keywords:
                if kw in content:
                    print(f"Found '{kw}' in {fpath}")
                    break
    except Exception as e:
        pass
