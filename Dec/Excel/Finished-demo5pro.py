"""
输出未完成质检CSV文件.
文件输入路径和输出路径都一样，容易多次处理同一个文件。
"""

import pandas as pd
import os

# 设置文件夹路径
input_dir = r'E:\workspace\python_demo\Dec\Excel'  # 你要处理的文件夹路径
output_dir = r'E:\workspace\python_demo\Dec\Excel'  # 输出结果保存的文件夹（与输入路径相同）

# 输入截止日期
date = '0108'

# 遍历输入文件夹中的所有 CSV 文件
for file_name in os.listdir(input_dir):
    if file_name.endswith('.csv'):  # 只处理 CSV 文件
        input_file = os.path.join(input_dir, file_name)  # 获取完整文件路径
        # 查看输出文件路径
        print(input_file)
        # 获取文件名中的 '-xx' 部分，判断 - 前的两个字
        prefix = file_name.split('-')[0]  # 获取 - 前的部分

        if prefix == "名单":
            print(f"跳过文件: {file_name}（文件名前两个字为“名单”）")
            continue  # 跳过该文件

        # 读取 CSV 文件并将其转化成 DataFrame
        df = pd.read_csv(input_file)

        # 获取文件名中的 '-xx' 部分
        file_name_part = file_name.split('-')[1].split('.')[0]  # 获取 '-xx' 部分

        # 生成输出文件名
        blank_name = f'截止{date}剩余未完成质检名单-{file_name_part}'
        output_file = os.path.join(output_dir, f'{blank_name}.csv')

        # 过滤条件：第一列有数据，且第五列为空
        filter_blank_num = df[df.iloc[:, 0].notna() & df.iloc[:, 4].isna()]

        # 输出为空的行（这里只打印前5行，避免数据量过大）
        print(f"处理文件: {file_name}")
        print(filter_blank_num)

        # 保存为 CSV 格式
        filter_blank_num.to_csv(output_file, index=False)

        # 输出提示
        print(f"【{output_file}】已输出！\n")
