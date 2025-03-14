"""
尝试获取当天时间作为变量传入filter中,命名也包含当天时间。
"""

import pandas as pd
from datetime import datetime
# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv(r'E:\workspace\python_demo\Dec\Excel\0123-厦门.csv')


# 获取当天的日期并转化为字符串
today_date = datetime.today().strftime('%Y/%m/%d')    # 输出格式为:'2024/12/20' '2025/01/23'
# 去掉月份前的0
today_date = today_date.replace(f"/0{datetime.today().month}/", f"/{datetime.today().month}/")
print("当天时间: ",today_date)
filter_df = df[(df.iloc[:, 0] == today_date) & (df.iloc[:, 9] == '已完成')]
# print("已筛选完数据 ")
# 处理摄像头编号（第四列）和文件夹编号（第五列），并合并
filter_df['合并结果'] = (
    # filter_df.iloc[:, 2].astype(str) + '-' +  # 数据包日期（第三列）
    filter_df.iloc[:, 2].astype(int).astype(str) + '-' +  # 数据包日期（第三列）
    filter_df.iloc[:, 3].astype(int).astype(str).str.zfill(2) + '-' +  # 摄像头编号（第四列）
    filter_df.iloc[:, 4].astype(int).astype(str)  # 文件夹编号（第五列）
)

# 删除原始的三列（数据包日期、摄像头编号、文件夹编号）
filter_df.drop(columns=[filter_df.columns[2], filter_df.columns[3], filter_df.columns[4]], inplace=True)

# 将合并结果插入到第二列
filter_df.insert(1, '时间', filter_df.pop('合并结果'))

# 删除列名为Unnamed的列
filter_df.loc[:, ~filter_df.columns.str.contains('^Unnamed')]

# 输出结果
# print("清洗完数据:")
print(filter_df)



# 将结果保存到新的 Excel 文件中
# 尝试将日期名称写入文件名中
today_date_atype = datetime.today().strftime('%Y_%m_%d')
file_name = f'{today_date_atype}_完成名单_demo2.csv'
filter_df.to_csv(file_name, index = False)
# filter_df.to_csv("filtered_data_20.csv", index = False)