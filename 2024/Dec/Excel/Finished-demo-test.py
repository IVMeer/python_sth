import pandas as pd
import os
#在终端输入pwd可以查看当前路径

# 输入文件路径
input_file = r'E:\workspace\python_demo\Dec\Excel\0111-xiamen.csv'


df = pd.read_csv(input_file)

date = '0108'


df['日期'] = pd.to_datetime(df['日期'], format='%Y/%m/%d', errors='coerce')
print(df['日期'].dtype)