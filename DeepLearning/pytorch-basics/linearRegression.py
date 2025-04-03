import torch.nn as nn
import torch.optim as optim
import torch

# 定义模型
class LinearRegression(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)  # 输入 1 维，输出 1 维

    def forward(self, x):
        return self.linear(x)

# 训练数据
X = torch.tensor([[1.0], [2.0], [3.0]])
Y = torch.tensor([[2.0], [4.0], [6.0]])

# 创建模型
model = LinearRegression()
criterion = nn.MSELoss()  # 均方误差损失
optimizer = optim.SGD(model.parameters(), lr=0.01)  # 随机梯度下降

# 训练
for epoch in range(100):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, Y)
    loss.backward()
    optimizer.step()

print(f"最终 loss: {loss.item()}")
