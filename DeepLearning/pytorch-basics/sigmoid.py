
import torch 
import matplotlib.pyplot as plt

# Pytorch 绘制sigmoid函数
x = torch.arange(-5, 5., 0.1)   # -5到5，步长为0.1
y = torch.sigmoid(x)
plt.plot(x.numpy() , y.numpy())
plt.title("Sigmoid Activation Function")
plt.xlabel("Input")
plt.ylabel("Output")
plt.show()

