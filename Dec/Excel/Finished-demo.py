"""
输入日期, 筛选出当天的已完成的文件夹, 并将数据写入新的excel中
"""

import pandas as pd
from datetime import datetime
# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv(r'E:\workspace\python_demo\Dec\Excel\1224-new.csv')

# 输入日期
date = '2024/12/24'
# 获取当天的日期并转化为字符串
# date_str = datetime.today().strftime('%Y/%m/%d')    # 输出格式为 '2024/12/20'
# print(date_str)
# 过滤条件：第三列是 '2024/12/19' 且第十列是 '已完成'
filter_df = df[(df.iloc[:, 0] == date) & (df.iloc[:, 9] == '已完成')]
# print("已筛选完数据 ")
# 处理摄像头编号（第四列）和文件夹编号（第五列），并合并
filter_df['合并结果'] = (
    filter_df.iloc[:, 2].astype(str) + '-' +  # 数据包日期（第三列）
    filter_df.iloc[:, 3].astype(float).astype(int).astype(str).str.zfill(2) + '-' +  # 摄像头编号（第四列）
    filter_df.iloc[:, 4].astype(float).astype(int).astype(str)  # 文件夹编号（第五列）
)

# # 用合并结果替代原始的三列
# filter_df['合并结果'] = filter_df['合并结果']

# 删除原始的三列（数据包日期、摄像头编号、文件夹编号）
filter_df.drop(columns=[filter_df.columns[2], filter_df.columns[3], filter_df.columns[4]], inplace=True)

# 将合并结果插入到第二列
filter_df.insert(1, '时间', filter_df.pop('合并结果'))

# 输出结果
# print("清洗完数据:")
print(filter_df)

# 输出结果
# print(filter_df[['合并结果']])


# 尝试将日期名称写入文件名中
# file_name = f'fileted_data_{ date_str }.xlsx'
# filter_df.to_excel(file_name, index = False)
date_convert = date.replace('/', '-')
file_name = f'{date_convert}-完成名单.csv'

# 将完成名单保存为csv格式
filter_df.to_csv(file_name, index = False)

