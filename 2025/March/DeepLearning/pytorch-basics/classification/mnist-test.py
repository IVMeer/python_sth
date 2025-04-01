import torch
import torch.nn as nn

class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)  # 输入 1, 输出 32
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1) # 输入 32, 输出 64
        self.pool = nn.MaxPool2d(2, 2)  # 2x2 池化，尺寸减半
        self.fc1 = nn.Linear(64 * 7 * 7, 128)  # 这里要正确计算

    def forward(self, x):
        print("Input shape:", x.shape)  # (batch_size, 1, 28, 28)
        x = self.conv1(x)
        x = torch.relu(x)
        print("After conv1:", x.shape)  # (batch_size, 32, 28, 28)
        
        x = self.conv2(x)
        x = torch.relu(x)
        x = self.pool(x)
        print("After conv2 + pool:", x.shape)  # (batch_size, 64, 14, 14)
        
        x = self.pool(x)
        print("After second pool:", x.shape)  # (batch_size, 64, 7, 7)

        x = x.view(x.size(0), -1)  # 展平
        print("After flatten:", x.shape)  # (batch_size, 64*7*7)
        
        x = self.fc1(x)
        return x

# 测试网络
model = CNN()
dummy_input = torch.randn(64, 1, 28, 28)  # MNIST 数据 (batch_size, 1, 28, 28)
model(dummy_input)
