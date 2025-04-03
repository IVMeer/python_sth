import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# 加载预训练的 ResNet-18
model = models.resnet18(pretrained=True)
model.eval()  # 切换为推理模式

# 预处理输入图像
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# 加载图像并转换格式
image = Image.open("cat.jpg")
image = transform(image).unsqueeze(0)  # 增加 batch 维度

# 进行推理
with torch.no_grad():
    output = model(image)
    prediction = torch.argmax(output, dim=1)
print(f"预测类别索引: {prediction.item()}")
