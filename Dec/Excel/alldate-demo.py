import pandas as pd
from datetime import datetime

file_name = r'E:\workspace\python_demo\Dec\Excel\0120-厦门.csv'

# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv(file_name)

# 筛选已完成的数据
filter_df = df[df.iloc[:, 9] == '已完成']
print("已完成的记录:", filter_df)

# 假设第一列是日期，并确保日期列为日期格式（如果它是字符串格式）
filter_df.iloc[:, 0] = pd.to_datetime(filter_df.iloc[:, 0], errors='coerce')

# 获取所有唯一日期
unique_dates = filter_df.iloc[:, 0].unique()

# 遍历每个日期进行处理
for date in unique_dates:
    # 按日期过滤
    date_filtered_df = filter_df[filter_df.iloc[:, 0] == date]
    
    # 处理摄像头编号和文件夹编号，并合并
    date_filtered_df['合并结果'] = (
        date_filtered_df.iloc[:, 2].astype(int).astype(str) + '-' +  # 数据包日期（第三列）
        date_filtered_df.iloc[:, 3].astype(int).astype(str).str.zfill(2) + '-' +  # 摄像头编号（第四列）
        date_filtered_df.iloc[:, 4].astype(str)  # 文件夹编号（第五列）
    )
    
    # 删除原始的三列（数据包日期、摄像头编号、文件夹编号）
    date_filtered_df.drop(columns=[date_filtered_df.columns[2], date_filtered_df.columns[3], date_filtered_df.columns[4]], inplace=True)
    
    # 将合并结果插入到第二列
    date_filtered_df.insert(1, '时间', date_filtered_df.pop('合并结果'))

    # 获取文件名中的 '-xx' 部分
    file_name_part = file_name.split('-')[1].split('.')[0]  # 获取 '-xx' 部分
    
    # 定义输出文件名，使用日期作为文件名的一部分
    output_file_name = f'{date.strftime("%Y-%m-%d")}-完成名单-{file_name_part}.csv'
    
    # 保存为 CSV 文件
    date_filtered_df.to_csv(output_file_name, index=False)
    print(f"已输出: {output_file_name}")
