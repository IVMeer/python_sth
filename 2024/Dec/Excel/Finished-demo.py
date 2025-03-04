"""

输入单个日期, 筛选出输入日期中已完成的文件夹, 并将筛选出的数据保存在csv格式的文件当中。

"""

import pandas as pd
file_name = r'E:\workspace\python_demo\2024\Dec\Excel\0303-金小象.csv'

# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv(file_name)

# 输入日期
date = '2025/3/3'

filter_df = df[(df['日期'] == date) & (df['完成情况'] == '已完成')]

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

