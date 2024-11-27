import re
import io
a = open('familytree.txt',mode='r',encoding='utf-8')
b = open('ff.txt',mode='w',encoding='utf-8')
lines = a.readlines()
for line in lines:
    newline = re.sub(r'^\s*$\n','',line)
    newline = re.sub(r'^\—\s[0-9]*\s\—$\n','',newline)
    b.write(newline)
a.close()
b.close()


'''
import PyPDF2
def read_pdf_with_pypdf2(file_path):
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    num_pages = pdf_reader.getNumPages()

    for i in range(num_pages):
        page = pdf_reader.getPage(i)
        text = page.extractText()
        print(text)

    pdf_file.close()


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import io

def read_pdf_with_pdfminer(file_path):
    resource_manager = PDFResourceManager()
    output_stream = io.StringIO()
    laparams = LAParams()
    device = TextConverter(resource_manager, output_stream, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)

    with open(file_path, 'rb') as pdf_file:
        for page in PDFPage.get_pages(pdf_file, check_extractable=True):
            interpreter.process_page(page)

    text = output_stream.getvalue()

    device.close()
    output_stream.close()

    print(text)
'''