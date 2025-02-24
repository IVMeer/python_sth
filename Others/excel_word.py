import openpyxl
from docxtpl import DocxTemplate

# 读取 Excel 文件
def read_excel(file_path):
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active  # 读取第一个工作表
    headers = [cell.value for cell in sheet[1]]  # 获取表头
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        data.append(dict(zip(headers, row)))  # 将表头与行数据组合成字典
    return data

# 将数据填充到 Word 模板中
def fill_template(data, template_path, output_path):
    doc = DocxTemplate(template_path)
    for row in data:
        doc.render(row)
        doc.save(output_path.format(row['name']))  # 按照名字保存每个 Word 文件

# 主函数
def excel_to_word_with_template(excel_path, template_path, output_path):
    data = read_excel(excel_path)
    fill_template(data, template_path, output_path)
    print(f"数据已从 {excel_path} 转换并填充到 {output_path} 中")

# 示例：从 Excel 填充 Word 模板
excel_to_word_with_template('C:/Users/win11/Desktop/123.xlsx', 'template.docx', 'C:/Users/win11/Desktop/ttt.xlsx')
