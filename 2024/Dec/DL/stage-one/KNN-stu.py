"""
KNN 手写数字识别
"""

# 导入必要的库
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# 加载 MNIST 数据集
from sklearn.datasets import fetch_openml
mnist = fetch_openml('mnist_784', version=1)

# 获取特征和标签
X, y = mnist["data"], mnist["target"]

# 将标签转换为整数类型
y = y.astype(int)

# 拆分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 数据标准化（标准化对于KNN特别重要）
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 使用 KNN 进行训练
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_scaled, y_train)

# 对测试集进行预测
y_pred = knn.predict(X_test_scaled)

# 计算准确率
accuracy = accuracy_score(y_test, y_pred)
print(f"KNN Accuracy: {accuracy * 100:.2f}%")

# 显示第一张预测结果
plt.imshow(X_test.iloc[0].to_numpy().reshape(28, 28), cmap="gray")
plt.title(f"Predicted Label: {y_pred[0]}")
plt.show()
