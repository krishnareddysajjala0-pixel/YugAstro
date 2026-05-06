import json

with open("bhava_lord_rules.json", "r", encoding="utf-8") as f:
    rules = json.load(f)

with open("bhava_lord_rules_py.txt", "w", encoding="utf-8") as f:
    f.write("BHAVA_LORD_RULES = ")
    json.dump(rules, f, ensure_ascii=False, indent=4)
