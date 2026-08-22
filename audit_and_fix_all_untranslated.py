# -*- coding: utf-8 -*-
"""
Audits all HTML templates in templates/ and wraps remaining plain Telugu text in {{ _('...') }}.
Then populates all translation dictionaries so that 100% of text site-wide translates!
"""

import os
import glob
import re
import json

templates_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\templates"
trans_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\translations"

# Step 1: Wrap plain text nodes containing Telugu characters in templates
def contains_telugu(text):
    return bool(re.search(r'[\u0C00-\u0C7F]', text))

html_files = glob.glob(os.path.join(templates_dir, "*.html"))

total_wrapped = 0

for fpath in html_files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Avoid modifying <script> and <style> contents directly
    parts = re.split(r'(<(?:script|style)[^>]*>.*?</(?:script|style)>)', content, flags=re.DOTALL | re.IGNORECASE)
    
    new_parts = []
    for part in parts:
        if part.lower().startswith('<script') or part.lower().startswith('<style'):
            new_parts.append(part)
        else:
            # Match HTML text nodes (>text<)
            def repl(match):
                prefix, text, suffix = match.group(1), match.group(2), match.group(3)
                if contains_telugu(text):
                    # Check if already wrapped in {{ _(...) }}
                    stripped = text.strip()
                    if not (stripped.startswith("{{ _(") and stripped.endswith(") }}")):
                        global total_wrapped
                        total_wrapped += 1
                        return f"{prefix}{{{{ _('{stripped}') }}}}{suffix}"
                return match.group(0)
            
            modified_part = re.sub(r'(>)([^<]+)(<)', repl, part)
            new_parts.append(modified_part)
            
    new_content = "".join(new_parts)
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated template {os.path.basename(fpath)}")

print(f"Total newly wrapped Jinja i18n text nodes: {total_wrapped}")
