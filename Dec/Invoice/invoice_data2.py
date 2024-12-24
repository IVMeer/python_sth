"""
处理单个PDF文件,并将其新建重命名
"""



import pdfplumber
import re
import os
import shutil

# pdf路径
path = r'E:\workspace\python_demo\Dec\Invoice\123.pdf'
# 提取PDF文件所在路径
dir_path = os.path.dirname(path)
# 获取文件名（不包括拓展名）
filename_without_extension = os.path.splitext(os.path.basename(path))[0]

# 打开 PDF 文件
with pdfplumber.open(path) as pdf:
    # 假设发票在第一页
    page = pdf.pages[0]
    
    # 提取文本内容
    text = page.extract_text()
    
    # 打印整页文本（可以检查文本布局）
    # print("Extracted Text:")
    # print(text)

    # 按行分割文本
    lines = text.split("\n")
    
    # 所要提取的数据
    invoice_number = "" # 发票号码
    amount = ""         # 金额
    seller_name = ""    # 销售方名称
    
    
    print("获取结果如下" + "↓"*50)
    
    # 获取发票号码（第二行）
    if len(lines) > 1:
        invoice_line = lines[1]
        invoice_number = re.search(r"\d+", invoice_line) # 正则表达式 \d 匹配一个数字 \d+
        if invoice_number:
            invoice_number = invoice_number.group()  # 提取匹配的数字部分
            print(f"发票号码: {invoice_number}")
        else:
            print("未能找到发票号码中的数字。") 

    # 获取价税合计小写
    if len(lines) > 15:
        total_amount = lines[15]
        match_number = re.search(r'￥(\d+\.\d{2})', total_amount)
        if match_number:
            amount = match_number.group(1)  
            print(f"价税合计小写: {amount}")
        else:
            print("未能找到价税合计小写中的数字。")
    # 获取名称
    if len(lines) > 16:
        name = lines[16] 
        match_name = re.search(r'名\s*称:(.+)',name)
        if match_name:
            seller_name = match_name.group(1)
            print(f"销售方名称:{seller_name}")
        else:
            print("未能找到名称。")
            
print(f'{seller_name}_{invoice_number} {amount}元')

if invoice_number and amount and seller_name:
    print("提取成功")
    # 创建新的文件夹名
    new_filename = f'{seller_name}_{invoice_number} {amount}元.pdf'
    new_file_path = os.path.join(dir_path, new_filename)
    
    # 复制文件并重命名
    shutil.copy2(path, new_file_path)
    print(f"文件已重命名为: {new_filename}")
else:
    print("未能提取到完整的发票消息, 文件未复制")