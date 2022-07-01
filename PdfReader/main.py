from PyPDF2 import PdfReader
import PdfReader

path = "1.pdf"
text = PdfReader.GetText(path)
for i in text:
    print(i)

