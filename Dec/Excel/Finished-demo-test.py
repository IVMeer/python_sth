import pandas as pd
import os
#在终端输入pwd可以查看当前路径

# 输入文件路径
input_file = r'E:\workspace\python_demo\Dec\Excel\防盗损校验数据-厦门.csv'

# 输入截止日期
date = '0108'

# 读取CSV文件并将其转化成Dataframe
df = pd.read_csv(input_file)

file_name = os.path.basename(input_file)  # 获取文件名

file_name_part = file_name.split('-')[1].split('.')[0]  # 获取 '-xx' 部分

# 生成输出文件名
blank_name = f'截止{date}{file_name_part}剩余未完成质检'
output_file = f'{blank_name}名单.csv'

# 过滤条件：第一列有数据，且第五列为空
filter_blank_num = df[df.iloc[:, 0].notna() & df.iloc[:, 4].isna()]

# 输出为空的行（这里只打印前5行，避免数据量过大）
# head_and_tail = pd.concat([filter_blank_num.head(5), filter_blank_num.tail(5)])
# print(head_and_tail)

# 输出全部
print(filter_blank_num)

# 保存为 CSV 格式
filter_blank_num.to_csv(output_file, index=False)

# 输出提示
print(f"【{output_file}】已输出！")
