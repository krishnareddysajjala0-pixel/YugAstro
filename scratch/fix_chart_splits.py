# -*- coding: utf-8 -*-
import glob, re

templates = glob.glob(r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\templates\*.html")

for t in templates:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()

    orig = content
    
    # Fix corrupt split('<br>...') lines
    content = re.sub(r"split\('<br>\{\{ _\(\\'\)\s*%\}\s*\{% if _\(\"లగ్నం\"\)\s*in\s*line %\}\'\)\s*\}\}", "split('<br>') %}\n        {% if 'లగ్నం' in line", content)
    content = re.sub(r"split\('<br>[\s\S]*?in line\s*[\s\S]*?\}\}", "split('<br>') %}\n        {% if 'లగ్నం' in line", content)

    if content != orig:
        with open(t, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed split in {t}")
