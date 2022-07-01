from PyPDF2 import PdfReader

def GetText(path):
    reader = PdfReader(path)
    text = []
    for page in reader.pages:
        text.append(page.extract_text())
    return text

