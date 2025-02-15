


"""
输入单个日期, 筛选出输入日期中已完成的文件夹, 并将筛选出的数据保存在csv中。
1.[]用于访问数据结构的元素,例如:DataFrame的单列或者多列。 
    df['列名']
    df[['列名1','列名2']]  
    df.loc[0]
    df.iloc[0]


"""

import pandas as pd
from datetime import datetime
file_name = r'E:\workspace\python_demo\Dec\Excel\0210-xiamen.csv'

# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv(file_name)

# 输入日期
date = '2025/2/10'
# 过滤条件第一列为date所需要的日期且第十列为已完成。

# 第一种过滤方式
# filter_df = df[(df.iloc[:, 0] == date) & (df.iloc[:, 9] == '已完成')]   # iloc[row, column]→iloc[:,0]代表所有行，以及第一列
# filter_df = df[(df.iloc[:,0] == date) & (df.iloc[:,9] == '已完成')]

# 第二种过滤方式：使用columns
# date_col = df.columns[0]
# status_col = df.columns[9]
# filter_df = df[(df[date_col] == date) & (df[status_col] == '已完成')]

# 第三种过滤方式
# filter_df = df[(df[df.columns[0]] == date) & (df[df.columns[9]] == '已完成')]

# 第四种过滤方式
filter_df = df[(df['日期'] == date) & (df['完成情况'] == '已完成')]


# print("first_fileter:",filter_df)

# 处理摄像头编号（第四列）和文件夹编号（第五列），并合并。
# filter_df['合并结果'] = (
#     filter_df.iloc[:, 2].astype(int).astype(str) + '-' +  # 数据包日期（第三列）
#     filter_df.iloc[:, 3].astype(int).astype(str).str.zfill(2) + '-' +  # 摄像头编号（第四列）
#     # filter_df.iloc[:, 4].astype(int).astype(str)  # 文件夹编号（第五列）
#     filter_df.iloc[:, 4].apply(lambda x: str(x) if isinstance(x, str) and '_' in x else str(int(x)))  # 文件夹编号（第五列），处理 1 和 1_1 等情况
# )
# 
filter_df['合并结果'] = (
    filter_df['数据包日期'].astype(int).astype(str) + '-' +
    filter_df['机器号'].astype(int).astype(str).str.zfill(2) + '-' +
    filter_df['文件夹号数'].apply(lambda x: str(x) if isinstance(x, str) and '_' in x else str(int(x)))
)


# 删除原始的三列（数据包日期、摄像头编号、文件夹编号）
filter_df.drop(columns=[filter_df.columns[2], filter_df.columns[3], filter_df.columns[4]], inplace=True)

# 将合并结果插入到第二列
filter_df.insert(1, '时间', filter_df.pop('合并结果'))

# 输出结果
print(filter_df)
# 转换日期格式  
date_convert = date.replace('/', '-')   # date = '2025/1/13'
# 获取文件名中的 '-xx'中的xx部分
file_name_part = file_name.split('-')[1].split('.')[0]  # 获取 'xx' 部分
# 定义输出文件名
output_file_name = f'{date_convert}-{file_name_part}-完成名单.csv'
# 将完成名单保存为csv格式
filter_df.to_csv(output_file_name, index = False)
print('已输出!')
print(f"完成名单→{output_file_name}")

