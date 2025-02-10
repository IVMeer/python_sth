import pandas as pd

# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv(r'E:\workspace\python_demo\Dec\Excel\0210-厦门.csv')

# 定义需要筛选的日期范围
start_date = '2025/2/5'
end_date = '2025/2/10'

# # 将第一列（日期列）转换为 datetime 类型
# df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], format='%Y/%m/%d')

# 过滤条件：日期在 2025/02/05 到 2025/02/10 之间，且第十列是 '已完成'
filter_df = df[(df.iloc[:, 0] >= start_date) & (df.iloc[:, 0] <= end_date) & (df.iloc[:, 9] == '已完成')]

# 处理摄像头编号（第四列）和文件夹编号（第五列），并合并
filter_df['合并结果'] = (
    filter_df.iloc[:, 2].astype(float).astype(int).astype(str) + '-' +  # 数据包日期（第三列）
    filter_df.iloc[:, 3].astype(float).astype(int).astype(str).str.zfill(2) + '-' +  # 摄像头编号（第四列）
    filter_df.iloc[:, 4].astype(float).astype(int).astype(str)  # 文件夹编号（第五列）
)

# 删除原始的三列（数据包日期、摄像头编号、文件夹编号）
filter_df.drop(columns=[filter_df.columns[2], filter_df.columns[3], filter_df.columns[4]], inplace=True)

# 将合并结果插入到第二列
filter_df.insert(1, '时间', filter_df.pop('合并结果'))

# 输出筛选后的数据
print(filter_df)

# 生成文件名
file_name = f'2025-02-05_to_2025-02-10-完成名单（厦门）.csv'

# 将完成名单保存为 CSV 格式
filter_df.to_csv(file_name, index=False)
print("完成名单已输出！")
