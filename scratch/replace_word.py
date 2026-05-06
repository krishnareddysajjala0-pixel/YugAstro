import os

def replace_in_file(filepath, old_word, new_word):
    if not os.path.exists(filepath):
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if old_word in content:
        new_content = content.replace(old_word, new_word)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Replaced in {filepath}")
    else:
        print(f"Word not found in {filepath}")

old = "భావాధిపతి"
new = "స్థానాధిపతి"

files = [
    'app.py',
    'templates/results.html',
    'bhava_lord_rules.json',
    'detailed_bhava_meanings.json',
    'astro_constants.json'
]

for file in files:
    replace_in_file(file, old, new)
