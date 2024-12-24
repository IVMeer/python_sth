import pandas as pd
"""
从表3抽第三列数据进入表1
"""

excel_1 = pd.read_excel(r'C:\Users\win11\Desktop\excel_1.xlsx')
excel_2 = pd.read_excel(r'C:\Users\win11\Desktop\excel_2.xlsx')

third_column = excel_2.iloc[:, 2]

excel_1['3'] = third_column

excel_1.to_excel('update_excel_1.xlsx', index=False)

print("操作完成，已将数据更新到 updated_excel1.xlsx")