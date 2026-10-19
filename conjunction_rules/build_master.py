# -*- coding: utf-8 -*-
"""
Master Builder for Planetary / Bhava Conjunctions in Thraitha Siddhantam.
Compiles all 12 Bhavas into bhava_conjunctions.csv and bhava_conjunctions.json.
"""

import os
import csv
import json

from bhava1 import BHAVA_1_RULES
from bhava2 import BHAVA_2_RULES
from bhava3 import BHAVA_3_RULES
from bhava4 import BHAVA_4_RULES
from bhava5 import BHAVA_5_RULES
from bhava6 import BHAVA_6_RULES
from bhava7 import BHAVA_7_RULES
from bhava8 import BHAVA_8_RULES
from bhava9 import BHAVA_9_RULES
from bhava10 import BHAVA_10_RULES
from bhava11 import BHAVA_11_RULES
from bhava12 import BHAVA_12_RULES

ALL_BHAVAS = [
    (1, BHAVA_1_RULES),
    (2, BHAVA_2_RULES),
    (3, BHAVA_3_RULES),
    (4, BHAVA_4_RULES),
    (5, BHAVA_5_RULES),
    (6, BHAVA_6_RULES),
    (7, BHAVA_7_RULES),
    (8, BHAVA_8_RULES),
    (9, BHAVA_9_RULES),
    (10, BHAVA_10_RULES),
    (11, BHAVA_11_RULES),
    (12, BHAVA_12_RULES),
]

def build():
    total_records = 0
    csv_rows = []
    json_data = {}

    for bhava_num, rules in ALL_BHAVAS:
        b_key = str(bhava_num)
        json_data[b_key] = rules
        total_records += len(rules)

        for r in rules:
            bhava_col = f"కలయిక ({bhava_num}వ భావములో)"
            csv_rows.append([
                r["combination"],
                r["status"],
                r["result"]
            ])

    print(f"Total Conjunction Records compiled: {total_records}")
    assert total_records == 234, f"Expected 234 records, found {total_records}"

    # 1. Write bhava_conjunctions.csv (UTF-8 with BOM for Excel compatibility)
    csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "bhava_conjunctions.csv")
    with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(["కలయిక (భావములో)", "మిత్ర / శత్రు స్థితి", "ప్రాక్టికల్ జీవితంలో ఎలాంటి ఫలితాలు"])
        for bhava_num, rules in ALL_BHAVAS:
            for r in rules:
                writer.writerow([
                    f"{r['combination']} ({bhava_num}వ భావములో)",
                    r["status"],
                    r["result"]
                ])

    # Also write with exact column header format matching user prompt for each bhava
    exact_csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "bhava_conjunctions_exact.csv")
    with open(exact_csv_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for bhava_num, rules in ALL_BHAVAS:
            writer.writerow([f"కలయిక ({bhava_num}వ భావములో)", "మిత్ర / శత్రు స్థితి", "ప్రాక్టికల్ జీవితంలో ఎలాంటి ఫలితాలు"])
            for r in rules:
                writer.writerow([
                    r["combination"],
                    r["status"],
                    r["result"]
                ])
            writer.writerow([]) # blank line between bhavas

    # 2. Write bhava_conjunctions.json
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "bhava_conjunctions.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print(f"Generated {csv_path} successfully.")
    print(f"Generated {exact_csv_path} successfully.")
    print(f"Generated {json_path} successfully.")

if __name__ == "__main__":
    build()
