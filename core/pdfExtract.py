from pdfminer.high_level import extract_text

def pdfMine(pdf_path):
    return extract_text(pdf_path)


