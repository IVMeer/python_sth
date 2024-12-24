"""
先扫描pdf所有内容,再根据内容进行筛选
发票号码【第二行】
价税合计小写【17行】
名称【18行】

"""


import pdfplumber
pdf_path = r'E:\workspace\python_demo\Dec\Invoice\123.pdf'

# 打开 PDF 文件
with pdfplumber.open(pdf_path) as pdf:
    # 提取每一页的文本
    all_text = ""
    for page in pdf.pages:
        all_text += page.extract_text()
        all_text += "\n--- End of Page ---\n"

    print("Extracted Text:")
    print(all_text)

    # 提取每一页的表格
    # for page_num, page in enumerate(pdf.pages):
    #     tables = page.extract_tables()
    #     if tables:
    #         print(f"Tables on Page {page_num + 1}:")
    #         for table in tables:
    #             for row in table:
    #                 print(row)
    #         print("\n--- End of Table ---")
