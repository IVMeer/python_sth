import torch
import torchvision
from PIL import Image
import torchvision.transforms as transforms

# 1. 加载模型
model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# 2. 读取图像并预处理
image = Image.open("test.jpg")
transform = transforms.Compose([transforms.ToTensor()])
image_tensor = transform(image).unsqueeze(0)

# 3. 进行目标检测
with torch.no_grad():
    predictions = model(image_tensor)

# 4. 输出检测结果
for box, label, score in zip(predictions[0]['boxes'], predictions[0]['labels'], predictions[0]['scores']):
    if score > 0.5:  # 只显示高置信度目标
        print(f"检测到目标: {label}, 置信度: {score:.2f}, 边界框: {box.numpy()}")
