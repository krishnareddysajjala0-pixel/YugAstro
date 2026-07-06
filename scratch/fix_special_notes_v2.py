import os

path = r'c:\Users\gnana\.gemini\antigravity\scratch\YugAstro\app.py'
if not os.path.exists(path):
    print(f"File not found: {path}")
    exit(1)

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all occurrences of special_note += with special_notes.append(
# and ensure the line ends with )
lines = content.split('\n')
new_lines = []
for line in lines:
    if 'special_note +=' in line:
        # Find the assignment part
        parts = line.split('special_note +=')
        prefix = parts[0]
        val = 'special_note +='.join(parts[1:]).strip()
        # Remove trailing space in string if it exists
        if val.endswith('" '): val = val[:-2] + '"'
        elif val.endswith("' "): val = val[:-2] + "'"
        new_lines.append(f'{prefix}special_notes.append({val})')
    else:
        new_lines.append(line)

with open(path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
print("Done")
