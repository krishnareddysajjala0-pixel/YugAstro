import json
import re

def parse_extracted_rules(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by pages
    pages = re.split(r"--- Page \d+ ---", content)
    pages = [p.strip() for p in pages if p.strip()]

    # Result structure: placement_house -> rulership_house -> { "shubha": "...", "paapa": "..." }
    rules = {}

    for i, page in enumerate(pages):
        placement_house = i + 1
        rules[placement_house] = {}

        # Look for the table content after "భావ ఫలాలు"
        table_start = page.find("భావ ఫలాలు")
        if table_start == -1:
            continue
        
        table_text = page[table_start:]
        
        # Split text into lines to process systematically
        lines = table_text.split("\n")
        
        current_house = None
        current_status = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check for House Number (1-12)
            house_match = re.match(r"^(\d{1,2})$", line)
            if house_match:
                current_house = int(house_match.group(1))
                if current_house not in rules[placement_house]:
                    rules[placement_house][current_house] = {"shubha": "", "paapa": ""}
                current_status = None
                continue
            
            # Check for Status (Shubhudu/Paapi)
            # Sometimes it's just the status, sometimes it's "status + text"
            status_match = re.match(r"^(శుభుడు|పాపి)\s*(.*)", line)
            if status_match:
                status_val = status_match.group(1)
                text_val = status_match.group(2)
                
                current_status = "shubha" if "శుభుడు" in status_val else "paapa"
                
                if current_house:
                    rules[placement_house][current_house][current_status] = text_val
                continue
            
            # If it's just more text, append to the current status of the current house
            if current_house and current_status:
                rules[placement_house][current_house][current_status] += " " + line

    # Cleanup: Strip extra spaces
    for p_h in rules:
        for r_h in rules[p_h]:
            rules[p_h][r_h]["shubha"] = rules[p_h][r_h]["shubha"].strip()
            rules[p_h][r_h]["paapa"] = rules[p_h][r_h]["paapa"].strip()

    return rules

if __name__ == "__main__":
    rules = parse_extracted_rules("extracted_rules.txt")
    # Verify we got all 12 houses for each page
    for p_h in sorted(rules.keys()):
        missing = [h for h in range(1, 13) if h not in rules[p_h]]
        if missing:
            print(f"Page {p_h} missing houses: {missing}")
        else:
            print(f"Page {p_h} is complete.")

    with open("bhava_lord_rules.json", "w", encoding="utf-8") as f:
        json.dump(rules, f, ensure_ascii=False, indent=2)
    print("Successfully created bhava_lord_rules.json")
