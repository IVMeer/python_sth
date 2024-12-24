"""
尝试提取发票中我所需要的数据
需要提取的数据是:1.名称(第二个) 2.发票号码 3.

"""
import pdfplumber
import re

def extract_invoice_data(pdf_path):
    # 打开PDF文件
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()

    # 使用正则表达式提取发票号、金额、日期等信息
    # 从上往下 提取 发票号码→价税合计（小写）→名称（销售方）
    # 最后总合成一个字符串。
    # 例:xxx有限公司_发票号码_xxx元
    invoice_number = re.search(r"发票号[:：]?\s*(\S+)", full_text)
    total_amount = re.search(r"价税合计[:：]?\s*(\d+(\.\d{1,2})?)", full_text)
    seller_name = re.search(r"销售方名称[:：]?\s*(\S+[\S\s]*?)\n", full_text)


    invoice_info = {
        "invoice_number": invoice_number.group(1) if invoice_number else None,
        "total_amount": total_amount.group(1) if total_amount else None,
        "seller_name": seller_name.group(1).strip() if seller_name else None,
    }
    
    return invoice_info

# 示例调用
# pdf_path = "invoice.pdf"
pdf_path = r'E:\workspace\python_demo\Dec\Invoice\123.pdf'
invoice_data = extract_invoice_data(pdf_path)
print(invoice_data)

