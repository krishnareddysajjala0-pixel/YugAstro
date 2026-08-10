import os
import re

target_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

replacements = [
    ('త్రైత జ్యోతిష్య శోధన', 'త్రైత జ్యోతిష్య శోధన'),
    ('త్రైత జ్యోతిష్య సేవలు', 'త్రైత జ్యోతిష్య సేవలు'),
    ('త్రైత జ్యోతిష్య పద్ధతులను', 'త్రైత జ్యోతిష్య పద్ధతులను'),
    ('త్రైత జ్యోతిష్య సిద్ధాంతాల', 'త్రైత జ్యోతిష్య సిద్ధాంతాల'),
    ('త్రైత జ్యోతిష్య', 'త్రైత జ్యోతిష్య'),
    ('త్రైత జ్యోతిష్యం', 'త్రైత జ్యోతిష్యం'),
    ('త్రైత జ్యోతిష్యంలో', 'త్రైత జ్యోతిష్యంలో'),
    ('త్రైత జ్యోతిష్యము', 'త్రైత జ్యోతిష్యము'),
    ('త్రైత సమాచార', 'త్రైత సమాచార'),
    ('త్రైత', 'త్రైత'),
    ('Thraitha Astrology', 'Thraitha Astrology'),
    ('Thraitha Panchangam', 'Thraitha Panchangam'),
    ('Thraitha', 'Thraitha'),
    ('thraitha', 'thraitha'),
]

modified_files = []

for root, dirs, files in os.walk(target_dir):
    # skip .git, venv, node_modules, .system_generated
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
