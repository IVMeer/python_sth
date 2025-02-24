import pandas as pd # 数据处理
import numpy as np  # 矩阵运算
import matplotlib.pyplot as plt # 数据可视化

import csv
# numpy 基本操作
## 数组创建
# 一维数组
a = np.array([1,2,3,4])
b = np.array([[5,6],[7,8]])
# 创建特定数组
zeros = np.zeros((2,3)) # 创建全零数组
ones = np.ones((2,3))   # 创建全一数组  
identity = np.eye(3)     # 创建单位矩阵
random = np.random.rand(2,3) # 创建随机数组
# 数组属性
# print(a.shape)  # 输出数组形状
# print(a.ndim)   # 输出数组维度
# print(a.size)   # 输出数组大小
# print(a.dtype)  # 输出数组元素类型

# 数学运算
c = a + 10             # [11, 12, 13, 14]
d = a * 2              # [2, 4, 6, 8]
# 开平方
e = np.sqrt(a)         # [1., 1.41, 1.73, 2.]

# 矩阵运算
dot = np.dot(b, b)     # 矩阵乘法 [[67,78],[91,106]]

# 数组切片
sub_array = a[1:3]     # 提取子数组 [2, 3]
# a = np.array([1,2,3,4])
# print(a.sum())
# print(a.mean())  # 输出数组元素的平均值
# print(a.max(), a.min())     
# print(a.std())  #标准差
# 数组变形
reshaped = b.reshape(4, 1)   

flattened = b.flatten()     # 展平数组 [5, 6, 7, 8]二维数组变为一维数组


# Pandas（数据处理）基本操作
# Series
s = pd.Series([1,2,3], index=['a','b','c'])
# DataFrame
data = {'Name':['Alice','Bob','Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)
# 查看数据
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.describe())
# # 选择列
# print(df['Name'])

# # 选择行
# print(df.loc[0])       # 按索引标签
# print(df.iloc[1])      # 按位置

# # 条件筛选
# print(df[df['Age'] > 25])
x = np.linspace(0, 10, 100)
y = np.sin(x)
#画图
# plt.plot(x, y)
# 显示图
# plt.show()
# 设定标题和标签
# plt.title('Sine Wave')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.show()

# plt.plot(x, y, color='green', linestyle='--', marker= 's')
# plt.title("Sine Wave withe Cutom Style")
# plt.show()
# plt.plot(x,y )
# plt.grid(True)
# plt.show()

# 创建一个 1x2 的子图
# fig, (ax1, ax2) = plt.subplots(1, 2)

# # 第一个子图
# ax1.plot(x, y)
# ax1.set_title('Sine Wave')

# # 第二个子图
# ax2.plot(x, np.cos(x))
# ax2.set_title('Cosine Wave')

# plt.tight_layout()  # 自动调整子图布局
# plt.show()
# 创建categories
# categories = ['A', 'B', 'C', 'D']
# values = [3, 7, 2, 5]
# 条形图
# plt.bar(categories, values)
# plt.title('Bar Chart Example')
# plt.xlabel('Category')
# plt.ylabel('Values')
# plt.show()
# 水平条形图
# plt.barh(categories, values)
# plt.title('Horizontal Bar Chart')
# plt.xlabel('Values')
# plt.ylabel('Category')
# plt.show()

# 散点图
# x = np.random.rand(50)
# y = np.random.rand(50)

# plt.scatter(x, y)
# plt.title('Scatter Plot Example')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()
# sizes = np.random.rand(50) * 100  # 点的大小
# colors = np.random.rand(50)       # 点的颜色

# plt.scatter(x, y, s=sizes, c=colors, cmap='viridis')
# plt.title('Custom Scatter Plot')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.show()

# 饼状图
# labels = ['A', 'B', 'C', 'D']
# sizes = [30, 20, 25, 25]

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
# plt.title('Pie Chart Example')
# plt.show()

# plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)

# # 创建一个白色圆形使饼图看起来像一个环
# centre_circle = plt.Circle((0, 0), 0.70, color='white')
# fig = plt.gcf()
# fig.gca().add_artist(centre_circle)

# plt.title('Donut Chart Example')
# plt.show()

# 直方图 Histogram
data = np.random.randn(1000)  # 正态分布数据

plt.hist(data, bins=30, edgecolor='black')  # bins表示条形数目
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

data1 = np.random.randn(1000)
data2 = np.random.randn(1000)

plt.hist([data1, data2], bins=30, edgecolor='black', label=['Data1', 'Data2'])
plt.legend()
plt.title('Multiple Histograms')
plt.show()




 


