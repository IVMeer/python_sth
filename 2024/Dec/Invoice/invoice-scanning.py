



"""
扫描PDF文件所有内容,将其每一行内容提取出来。
"""

# 载入pdfplumber库 
import pdfplumber
# 设置PDF文件路径
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
