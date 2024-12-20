import pandas as pd

df = pd.read_csv(r'E:\workspace\python_demo\Dec\Excel\防盗损文件夹领取情况.csv')

# print(df.head())
filter_df = df[(df.iloc[:, 0] == '2024/12/19') & (df.iloc[:, 9] == '已完成')]


"""
填写数据是数据包日期(第三列),_(第四列) , 文件夹号数(第五列)，需修改为→数据包日期-摄像头编号(若单个数字则补充零)-文件夹编号【例:20241117-08-1】
"""
#提取数据
# 将数据包日期（第三列）转为字符串
df['数据包日期'] = df.iloc[:, 2].astype(str)

# 尝试删除数据包日期中的NaN值
# df['数据包日期'] = df['数据包日期'].dropna(inplace = True)
# print(df['数据包日期'])


# 处理摄像头编号（第四列），确保去除 NaN 和 inf 值
df['摄像头编号'] = df.iloc[:, 3].replace([float('inf'), -float('inf')], 0)  # 将无穷大替换为0
df['摄像头编号'] = df['摄像头编号'].fillna(0)  # 将NaN值替换为0
df['摄像头编号'] = df['摄像头编号'].astype(float).astype(int).astype(str).str.zfill(2)

# 处理文件夹编号（第五列），确保去除 NaN 和 inf 值
df['文件夹编号'] = df.iloc[:, 4].replace([float('inf'), -float('inf')], 0)  # 将无穷大替换为0
df['文件夹编号'] = df['文件夹编号'].fillna(0)  # 将NaN值替换为0
df['文件夹编号'] = df['文件夹编号'].astype(float).astype(int).astype(str)

# 合并数据包日期、摄像头编号和文件夹编号为最终格式
df['合并结果'] = df['数据包日期'] + '-' + df['摄像头编号'] + '-' + df['文件夹编号']

# 输出结果
# print(df[['合并结果']])


print(filter_df)