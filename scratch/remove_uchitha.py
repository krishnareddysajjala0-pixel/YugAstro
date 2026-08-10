import os

target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

replacements = [
    ('జాతక చక్రం & పంచాంగ వివరాలు', 'జాతక చక్రం & పంచాంగ వివరాలు'),
    ('ముఖ్య ఫీచర్లు (Key Features)', 'ముఖ్య ఫీచర్లు (Key Features)'),
    ('ఆస్ట్రో సాధనాలు', 'ఆస్ట్రో సాధనాలు'),
    ('త్రైత జ్యోతిష్య సేవలు', 'త్రైత జ్యోతిష్య సేవలు'),
    ('త్రైత జ్యోతిష్య శోధన', 'త్రైత జ్యోతిష్య శోధన'),
    ('జ్యోతిష్య సాధనాలు', 'జ్యోతిష్య సాధనాలు'),
    ('జన్మ కుండలి వివరాలు ఎంటర్ చేయండి', 'జన్మ కుండలి వివరాలు ఎంటర్ చేయండి'),
    ('జన్మ కుండలి', 'జన్మ కుండలి'),
    ('జ్యోతిష్య సాధనాలు', 'జ్యోతిష్య సాధనాలు'),
    ('లెక్కించండి', 'లెక్కించండి'),
    ('లెక్కించుకోండి', 'లెక్కించుకోండి'),
    ('చూడవచ్చు', 'చూడవచ్చు'),
    ('', ''),
    ('గోప్యత & భద్రత', 'గోప్యత & భద్రత'),
    ('100% గోప్యత', '100% గోప్యత'),
    ('విశ్లేషణ', 'విశ్లేషణ'),
    ('', ''),
    ('Key Features', 'Key Features'),
    ('Astrology Tools', 'Astrology Tools'),
    ('Thraitha', 'Thraitha'),
    ('', ''),
    ('', ''),
]

modified_files = []

for root, dirs, files in os.walk(target_dir):
    if any(x in root for x in ['.git', 'venv', 'node_modules', '.system_generated']):
        continue
    for file in files:
        if file.endswith(('.html', '.py', '.js', '.json', '.md', '.css', '.txt')):
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content
                for old_str, new_str in replacements:
                    new_content = new_content.replace(old_str, new_str)
                
                if new_content != content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    modified_files.append(file_path)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

print(f"Successfully updated {len(modified_files)} files.")
for f in modified_files:
    print(f" - {f}")
