import fitz
from pdf2docx import Converter


"依赖于pymudpf，提取pdf文本并将其写入word文档中"
def pdf_convert(pdf_path,word_path):
    doc = fitz.open(pdf_path)
    text = ''
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    with open(word_path, 'w', encoding='utf-8') as f:
        f.write(text)


"""依赖于pdf2docx库，进行pdf到word的转换"""
def pdf_to_word_pdf2docx(pdf_path, word_path):
    cv = Converter(pdf_path)
    cv.convert(word_path, start=0, end=None)
    cv.close()
pdf_to_word_pdf2docx('C:/Users/win11/Desktop/xxx.pdf', 'C:/Users/win11/Desktop/123.docx')

