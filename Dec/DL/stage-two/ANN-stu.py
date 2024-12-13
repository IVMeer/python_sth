import numpy as np

# 1. 数据准备：XOR 数据集
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],  # XOR 结果
              [0],
              [0],
              [1]])

# 2. 激活函数（sigmoid 和其导数）
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# 3. 初始化权重和偏置
input_layer_size = 2   # 输入层大小
hidden_layer_size = 4  # 隐藏层大小
output_layer_size = 1  # 输出层大小

np.random.seed(42)  # 设置随机种子，使得每次运行结果一致

# 初始化权重
W1 = np.random.randn(input_layer_size, hidden_layer_size)  # 输入到隐藏层的权重
b1 = np.zeros((1, hidden_layer_size))  # 隐藏层的偏置

W2 = np.random.randn(hidden_layer_size, output_layer_size)  # 隐藏层到输出层的权重
b2 = np.zeros((1, output_layer_size))  # 输出层的偏置

# 4. 前向传播
def forward_propagation(X):
    # 输入到隐藏层
    Z1 = np.dot(X, W1) + b1
    A1 = sigmoid(Z1)

    # 隐藏层到输出层
    Z2 = np.dot(A1, W2) + b2
    A2 = sigmoid(Z2)

    return A1, A2

# 5. 损失函数（均方误差）
def compute_loss(y, A2):
    m = y.shape[0]
    loss = np.sum((y - A2) ** 2) / m  # 均方误差
    return loss

# 6. 反向传播
def backward_propagation(X, y, A1, A2):
    m = X.shape[0]

    # 计算输出层的梯度
    dZ2 = A2 - y
    dW2 = np.dot(A1.T, dZ2) / m
    db2 = np.sum(dZ2, axis=0, keepdims=True) / m

    # 计算隐藏层的梯度
    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * sigmoid_derivative(A1)
    dW1 = np.dot(X.T, dZ1) / m
    db1 = np.sum(dZ1, axis=0, keepdims=True) / m

    return dW1, db1, dW2, db2

# 7. 更新权重和偏置
def update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate=0.1):
    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1
    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    return W1, b1, W2, b2

# 8. 训练模型
epochs = 10000  # 迭代次数
learning_rate = 0.1

for epoch in range(epochs):
    # 前向传播
    A1, A2 = forward_propagation(X)
    
    # 计算损失
    loss = compute_loss(y, A2)
    
    # 反向传播
    dW1, db1, dW2, db2 = backward_propagation(X, y, A1, A2)
    
    # 更新权重和偏置
    W1, b1, W2, b2 = update_parameters(W1, b1, W2, b2, dW1, db1, dW2, db2, learning_rate)
    
    # 每 1000 次迭代打印一次损失
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.10f}")

# 9. 训练完成后，进行预测
A1, A2 = forward_propagation(X)
predictions = (A2 > 0.5).astype(int)  # 将输出大于 0.5 的值判定为 1，反之为 0

print("\n训练完成后的预测结果：")
print(predictions)

