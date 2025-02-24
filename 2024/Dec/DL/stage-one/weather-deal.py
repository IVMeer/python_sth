import pandas as pd # 数据处理
import numpy as np  # 矩阵运算
import matplotlib.pyplot as plt # 数据可视化
import re


data = pd.read_csv(r'E:\workspace\python_demo\Dec\DL\stage-one\weather.csv')
data['Date'] = data['Date'].apply(lambda x: re.findall(r'\d{4}-\d{2}-\d{2}', x))
# 数据清洗：处理缺失值（示例）
data.fillna(data.mean(), inplace=True)

# 转换日期格式
data['Date'] = pd.to_datetime(data['Date'])

# 添加一列新数据：计算温湿指数 (Heat Index)
data['Heat Index'] = (0.5 * (data['Temperature'] + data['Humidity']))

# 数据处理：获取平均温度和湿度
avg_temp = data['Temperature'].mean()
avg_humidity = data['Humidity'].mean()

print(f"平均温度: {avg_temp:.2f}°C, 平均湿度: {avg_humidity:.2f}%")

# 可视化 1：折线图显示温度和湿度随时间的变化
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Temperature'], label='Temperature (°C)', marker='o')
plt.plot(data['Date'], data['Humidity'], label='Humidity (%)', marker='x')
plt.title('Weather Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid()
plt.show()

# 可视化 2：柱状图显示每日的温湿指数
plt.figure(figsize=(10, 5))
plt.bar(data['Date'], data['Heat Index'], color='orange', label='Heat Index')
plt.title('Daily Heat Index')
plt.xlabel('Date')
plt.ylabel('Heat Index')
plt.legend()
plt.grid(axis='y')
plt.show()
