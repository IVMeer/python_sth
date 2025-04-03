import torch
# tensor向量
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = x ** 2
y.sum().backward()
print(x.grad)

# 计算图和自动求导
x =torch.tensor(2.0, requires_grad=True)
y = x ** 2
y.backward()
print(x.grad)

