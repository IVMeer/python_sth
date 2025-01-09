
import pandas as pd
from datetime import datetime

# 读取文件路径
file_name = r'E:\workspace\python_demo\Dec\Excel\防盗损校验数据-厦门.csv'

# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv(file_name)
# 输入截止日期
date = '0108'
# 获取文件名中的 '-xx' 部分
file_name_part = file_name.split('-')[1].split('.')[0]  # 获取 '-xx' 部分
print(file_name)
print(file_name.split('-')[1])
print(file_name_part.split('.')[0])
print(file_name.split('-')[1].split('.')[0])
print(file_name_part)