file_path = r"C:\Users\KRISH\.gemini\antigravity\scratch\YugAstro\astrology_data.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Fix missing closing brace and comma on line 194
bad_str = 'కానీ బయటి ప్రపంచ వస్తువులు/ఎన్నికల గురించి చెప్పునది జ్యోతిష్యము కాదు. అది శరీరాంతర్గత కర్మకు సంబంధించినది కాదు."""\n        "rashi-vs-lagnam-and-planet-speeds": {'
good_str = 'కానీ బయటి ప్రపంచ వస్తువులు/ఎన్నికల గురించి చెప్పునది జ్యోతిష్యము కాదు. అది శరీరాంతర్గత కర్మకు సంబంధించినది కాదు."""\n    },\n    "rashi-vs-lagnam-and-planet-speeds": {'

if bad_str in content:
    content = content.replace(bad_str, good_str)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Fixed syntax in astrology_data.py!")
else:
    print("Pattern not found, checking...")