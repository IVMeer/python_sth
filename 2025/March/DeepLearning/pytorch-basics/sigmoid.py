"Pytorch 绘制sigmoid函数"
import torch 
import matplotlib.pyplot as plt
def sigmoid(x):
    return 1 / (1 + torch.exp(-x))
