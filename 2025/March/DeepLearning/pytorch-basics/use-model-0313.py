"""
使用训练好的模型进行预测
"""
import torch
import torch.nn as nn 
# 加载图片测试
from torchvision import transforms
from PIL import Image


# 定义模型结构
class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=32, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size = 3, padding = 1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 7 * 7,128)
        self.fc2 = nn.Linear(128, 10)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.25)
        
    def forward(self, x):
        print("Before flatten:", x.shape)
        x = self.relu(self.conv1(x))
        x = self.pool(self.relu(self.conv2(x)))
        x = self.pool(x)
        print("After pool:",x.shape)
        x = x.view(x.size(0), -1)   # 展平
        print("After flatten:", x.shape)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x
    
model = CNN()
model.load_state_dict(torch.load('mnist_cnn.pth'))
model.eval()

# 预处理
transform = transforms.Compose([
    transforms.Grayscale(), 
    transforms.Resize((28,28)),
    transforms.ToTensor()])

# 加载图片并进行预测
img = Image.open(r'.\2024\Nov\MNIST_study\digits_processed\new0.jpg')

img = transform(img).unsqueeze(0)

# 预测
with torch.no_grad():
    output = model(img)
    prediction = output.argmax(dim=1).item()
    print("Predicted digit:", prediction)