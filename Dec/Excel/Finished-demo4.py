"""
在已完成的文件夹中,查询第五列(质检量)为空的条数。
"""

"""
1.增加一个根据读取文件后缀，将输出文件名加上这个后缀的
"""

import pandas as pd
from datetime import datetime

# 需要写文件名。
# 读取文件路径
file_name = r'E:\workspace\python_demo\Dec\Excel\0208-唐山.csv'

# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv(file_name)
# 输入截止日期
date = '0124'
# 获取文件名中的 '-xx' 部分
file_name_part = file_name.split('-')[1].split('.')[0]  # 获取 '-xx' 部分
# 输入输出文件夹名称
blank_name = f'截止{date}剩余未完成质检名单-{file_name_part}'

filter_blank_num = df[df.iloc[:,0].notna() & df.iloc[:, 4].isna()]

# 输出为空的行
print(filter_blank_num)

file_name = f'{blank_name}.csv'

# 将完成名单保存为csv格式
filter_blank_num.to_csv(file_name, index = False)
print(f"【{file_name}】已输出！")
