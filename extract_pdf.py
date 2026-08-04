import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += f"\n--- Page {page_num + 1} ---\n"
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_path = "12 భావ ఫలాలు.pdf"
    try:
        extracted_text = extract_text_from_pdf(pdf_path)
        with open("extracted_rules.txt", "w", encoding="utf-8") as f:
            f.write(extracted_text)
        print("Successfully extracted text to extracted_rules.txt")
    except Exception as e:
        print(f"Error: {e}")
