import torch
model = torch.load('lenet5_mnist.pth')
model.eval()