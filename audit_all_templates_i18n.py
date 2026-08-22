# -*- coding: utf-8 -*-
"""
Comprehensive audit and auto-wrapping of all templates in YugAstro for 100% translation coverage.
"""

import json
import os
import re

base_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro"
tpl_dir = os.path.join(base_dir, "templates")
trans_dir = os.path.join(base_dir, "translations")

def process_template(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    def repl(match):
        prefix, text, suffix = match.group(1), match.group(2), match.group(3)
        stripped = text.strip()
        if re.search(r'[\u0C00-\u0C7F]', stripped) and not stripped.startswith('{{') and not stripped.startswith('{%'):
            clean_str = stripped.replace("'", "\\'")
            leading_ws = text[:len(text)-len(text.lstrip())]
            trailing_ws = text[len(text.rstrip()):]
            return f"{prefix}{leading_ws}{{{{ _('{clean_str}') }}}}{trailing_ws}{suffix}"
        return match.group(0)

    new_content = re.sub(r'(>)([^<]+)(<)', repl, content)

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

modified_files = []
for file in os.listdir(tpl_dir):
    if file.endswith('.html'):
        fpath = os.path.join(tpl_dir, file)
        if process_template(fpath):
            modified_files.append(file)

print(f"Wrapped Jinja i18n tags in {len(modified_files)} template files: {modified_files}")
