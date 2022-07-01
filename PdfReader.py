from PyPDF2 import PdfReader

reader = PdfReader("1.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)
