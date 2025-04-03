import torch

model = torch.load('mnist_cnn.pth')
model.eval()