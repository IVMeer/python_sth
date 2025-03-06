import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import matplotlib.pyplot as plt
from PIL import Image
from torchvision import transforms
import numpy as np
import cv2 as cv

class module(nn.Module):
    def __init__(self):
        super().__init__()#继承父类的函数
        self.conv1 = nn.Conv2d(1,10,5)# 输入通道1，输出通道10，卷积5*5
        self.conv2 = nn.Conv2d(10,20,3)# 10 20 3*3
        self.fc1 = nn.Linear(20*10*10,500)
        self.fc2 = nn.Linear(500,10)#0到9十个数字 输出10

    def forward(self,x):#定义了forward函数，backward函数就会被自动实现(利用Autograd)
        input_size = x.size(0) # batch_size *1 *28 *28
        x = self.conv1(x) # 输入 batch_size *1 *28 *28，输出 batch_size *10 *24 *24
        x = F.relu(x) #激活函数 使其变为非线性函数
        x = F.max_pool2d(x,2,2)#保持shape不变 输出 batch_size *10 *12 *12

        x = self.conv2(x)#输出： batch_size *20 *10 *10
        x = F.relu(x)

        x = x.view(input_size,-1)#拉伸  20*10*10 = 2000

        x = self.fc1(x)#输入：2000 输出：500
        x = F.relu(x)
        x = self.fc2(x)#输入：500 输出：10

        output = F.log_softmax(x,dim=1)#计算分类后，每个数字的概率值

        return output

    def imag():
        #白底黑字转换为黑底白字
        src = cv.imread('.\\0.jpg')#读取图片
        gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
        ret, binary = cv.threshold(gray, 0, 255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)#白底黑字转换为黑底白字
        cv.imwrite('.\\new0.jpg', binary)#将图像数据写入到图像文件中
        im = plt.imread('.\\new0.jpg')  # 读入图片
        images = Image.open('.\\new0.jpg')    # 将图片存储到images里面
        images = images.resize((28,28))   # 调整图片的大小为28*28
        images = images.convert('L')   # 灰度化

        transform = transforms.ToTensor()
        images = transform(images)
        images = images.resize(1,1,28,28)#处理完毕

        # 加载网络和参数
        model = module()#加载模型
        model.load_state_dict(torch.load('..\\model.ckpt'))#加载参数
        model.eval()#测试模型
        outputs = model(images)#输出结果

        label = outputs.argmax(dim =1) # 返回最大概率值的下标
        plt.title('{}'.format(int(label)))
        plt.imshow(im)
        plt.show()

    imag()
