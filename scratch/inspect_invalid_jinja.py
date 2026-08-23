# -*- coding: utf-8 -*-
import glob, os, re

templates = glob.glob(r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\templates\*.html")

for t in templates:
    with open(t, 'r', encoding='utf-8') as f:
        content = f.read()
    # Find any {{ _('...') }} that contains '{%' or '{{'
    bad_matches = re.findall(r'\{\{\s*_\([\'"][^\'"]*?(?:\{\%|\{\{).*?\)\s*\}\}', content, flags=re.DOTALL)
    if bad_matches:
        print(f"=== INVALID JINJA WRAPPERS IN {os.path.basename(t)} ({len(bad_matches)} found) ===")
        for m in bad_matches[:5]:
            print(repr(m[:120]))
