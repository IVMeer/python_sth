import pandas as pd
import os

# 设置文件夹路径
input_dir = r'E:\workspace\python_demo\Dec\Excel'  # 你要处理的文件夹路径
output_dir = r'E:\workspace\python_demo\Dec\Excel'  # 输出结果保存的文件夹

# 输入截止日期
date = '0108'

# 遍历输入文件夹中的所有 CSV 文件
for file_name in os.listdir(input_dir):
    if file_name.endswith('.csv'):  # 只处理 CSV 文件
        input_file = os.path.join(input_dir, file_name)  # 获取完整文件路径

        # 获取文件名中的 '-xx' 部分（假设文件名格式为 "数据-xx.csv" 或 "名单-xx.csv"）
        prefix = file_name.split('-')[0]

        # 检查是否已经处理过此文件
        processed_file = os.path.join(input_dir, f"{file_name}.done")
        if os.path.exists(processed_file):
            print(f"文件 {file_name} 已处理，跳过。\n")
            continue  # 跳过已处理的文件

        # 如果文件名中的前缀是“数据”，则处理
        if prefix == '数据':
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
            # head_and_tail = pd.concat([filter_blank_num.head(5), filter_blank_num.tail(5)])
            # print(f"文件: {file_name}")
            # print(head_and_tail)  # 打印前五条和尾五条数据

            # 输出全部数据
            print(filter_blank_num)

            # 保存为 CSV 格式
            filter_blank_num.to_csv(output_file, index=False)

            # 输出提示
            print(f"【{output_file}】已输出！\n")

            # 创建一个标志文件，表示该文件已处理
            with open(processed_file, 'w') as f:
                f.write("This file has been processed.")  # 文件内容可以为空或标记信息
        else:
            # 如果文件名的前缀是“名单”，跳过不处理
            print(f"文件 {file_name} 跳过处理。\n")
