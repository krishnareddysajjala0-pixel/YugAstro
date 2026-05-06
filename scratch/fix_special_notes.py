import re
import os

path = r'c:\Users\gnana\.gemini\antigravity\scratch\astroexp\app.py'
if not os.path.exists(path):
    print(f"File not found: {path}")
    exit(1)

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    stripped = line.strip()
    if stripped.startswith('special_note += '):
        match = re.match(r'^(\s*)special_note \+= (.*)$', line)
        if match:
            indent = match.group(1)
            val = match.group(2).strip()
            # Remove trailing space in string if it exists
            if val.endswith('" '): val = val[:-2] + '"'
            elif val.endswith("' "): val = val[:-2] + "'"
            new_lines.append(f'{indent}special_notes.append({val})\n')
        else:
            new_lines.append(line)
    elif stripped == 'special_note = ""':
        new_lines.append(line.replace('special_note = ""', 'special_notes = []'))
    elif '"special_note": special_note' in line:
        new_lines.append(line.replace('"special_note": special_note', '"special_notes": special_notes'))
    else:
        new_lines.append(line)

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print("Done")
