# -*- coding: utf-8 -*-
"""
Script to replace all user-facing occurrences of 'లగ్నం' / 'లగ్నాలు' with 'లగ్నం' / 'లగ్నాలు'.
Thraitha Astrology Rule: Rashi IS Lagnam.
"""

import os

base_dir = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro"

replacements = [
    # Complex / specific multi-word replacements first
    ("", ""),
    ("త్రైత జ్యోతిష్య సిద్ధాంతము ప్రకారం ", ""),
    ("", ""),
    ("12 లగ్నాలు", "12 లగ్నాలు"),
    ("లగ్నాల", "లగ్నాల"),
    ("లగ్నాలు", "లగ్నాలు"),
    ("లగ్న ఫలితాలు", "లగ్న ఫలితాలు"),
    ("లగ్న ఫలాలు", "లగ్న ఫలాలు"),
    ("లగ్న ఫలితములు", "లగ్న ఫలితములు"),
    ("లగ్న చక్రం", "లగ్న చక్రం"),
    ("లగ్న చక్రము", "లగ్న చక్రము"),
    ("లగ్నాధిపతి", "లగ్నాధిపతి"),
    ("లగ్నాధిపతి", "లగ్నాధిపతి"),
    ("లగ్నాధిపతులు", "లగ్నాధిపతులు"),
    ("చంద్ర లగ్నం", "చంద్ర లగ్నం"),
    ("సూర్య లగ్నం", "సూర్య లగ్నం"),
    ("లగ్న మార్పులు", "లగ్న మార్పులు"),
    ("మీ లగ్నంపై", "మీ లగ్నంపై"),
    ("ఈ లగ్నానికి", "ఈ లగ్నానికి"),
    ("ఈ లగ్నం", "ఈ లగ్నం"),
    ("ఏ లగ్నం", "ఏ లగ్నం"),
    ("లగ్నం", "లగ్నం"),

    # Rashi Specific Name replacements
    ("మేష లగ్నం", "మేష లగ్నం"),
    ("వృషభ లగ్నం", "వృషభ లగ్నం"),
    ("మిథున లగ్నం", "మిథున లగ్నం"),
    ("కర్కాటక లగ్నం", "కర్కాటక లగ్నం"),
    ("సింహ లగ్నం", "సింహ లగ్నం"),
    ("కన్యా లగ్నం", "కన్యా లగ్నం"),
    ("తులా లగ్నం", "తులా లగ్నం"),
    ("వృశ్చిక లగ్నం", "వృశ్చిక లగ్నం"),
    ("ధనూ లగ్నం", "ధనూ లగ్నం"),
    ("మకర లగ్నం", "మకర లగ్నం"),
    ("కుంభ లగ్నం", "కుంభ లగ్నం"),
    ("మీన లగ్నం", "మీన లగ్నం"),

    # Standalone 'లగ్నం' where applicable
    ("లగ్నం", "లగ్నం")
]

target_extensions = ('.html', '.py', '.json')

modified_files = []

for root, dirs, files in os.walk(base_dir):
    if any(ignore in root for ignore in ['.git', '__pycache__', 'venv', 'node_modules', 'brain']):
        continue
    for file in files:
        if file.endswith(target_extensions):
            # Skip python internal scripts or test files if needed, but check template/data files
            if file in ['test_5_charts_regression.py', 'extract_all_rules_to_txt.py']:
                continue
            fpath = os.path.join(root, file)
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = content
            # Apply replacements carefully
            for old_text, new_text in replacements:
                if old_text in new_content:
                    new_content = new_content.replace(old_text, new_text)

            if new_content != content:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                rel_path = os.path.relpath(fpath, base_dir)
                modified_files.append(rel_path)

print(f"Replacement complete! Modified {len(modified_files)} files:")
for mf in modified_files:
    print(f" - {mf}")
