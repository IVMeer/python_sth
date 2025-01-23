import pandas as pd

# 文件路径
file_name = r'E:\workspace\python_demo\Dec\Excel\0123-唐山.csv'

# 读取 CSV 文件
df = pd.read_csv(file_name)

# 输入日期
date = '2025/1/23'

# 过滤条件：第一列是目标日期
filter_df = df[df.iloc[:, 0] == date] 

# 输出过滤后的结果
# print("过滤后的数据：")
# print(filter_df)

# 计算每个人的标注框数（假设第八列是标注框的列）
# 按照第七列（人的ID）进行分组，计算第八列标注框数量的总和
# frame_count = filter_df.groupby('名字')[df.iloc[:,7]].sum()

# # 输出计算结果
print("每个人的标注框总和：")
print(filter_df)

# # 转换日期格式
# date_convert = date.replace('/', '-')  # 2025-1-20

# # 获取文件名中的 '-xx'部分
# file_name_part = file_name.split('-')[1].split('.')[0]  # 获取'xx'部分

# # 定义输出文件名
# output_file_name = f'{date_convert}-{file_name_part}-完成名单.csv'

# # 将筛选后的数据保存为 CSV 文件
# filter_df.to_csv(output_file_name, index=False)
# print('已输出完成名单！')
# print(f"输出文件名：{output_file_name}")
