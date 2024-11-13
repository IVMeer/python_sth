import torch
import torch.nn as nn 
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

BATCH_SIZE = 64
DEVICE =torch.device("cuda" if torch.cuda.is_available() else "cpu")
# DEVICE = torch.device("cuda")
EPOCHS = 10

# 图像处理 transform
pipeline = transforms.Compose([transforms.ToTensor(), # 将图片转换为张量
                               transforms.Normalize(mean=0.1307, std=0.3081) # 归一化处理
                               ])

# 下载数据集
train_set = datasets.MNIST('data', train=True, download=True, transform=pipeline)
test_set = datasets.MNIST('data', train=False, download=True, transform=pipeline)

# 加载数据集
train_loader = DataLoader(train_set, batch_size=BATCH_SIZE, shuffle=True)
test_loader = DataLoader(test_set, batch_size=BATCH_SIZE, shuffle=True)

# 构建网络
class module(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 10, 5) # 10个卷积核，5*5的卷积核
        self.conv2 = nn.Conv2d(10, 20, 3) 
        self.fc1 = nn.Linear(20*10*10, 500)#
        self.fc2 = nn.Linear(500, 10)

    def forward(self, x):
        input_size = x.size(0)
        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2, 2)

        x = self.conv2(x)
        x = F.relu(x)

        x = x.view(input_size,-1)#拉伸 -1(自动计算长度):20*10*10 = 2000

        x = self.fc1(x)#输入：2000 输出：500
        x = F.relu(x)#激活函数
        x = self.fc2(x)#输入：500 输出：10

        output = F.log_softmax(x,dim=1)#计算分类后，每个数字的概率值
        return output

model = module().to(DEVICE)
optimizer = optim.Adam(model.parameters())

def train_model(model,device,train_loader,optimizer,epoch):
    model.train()#模型训练
    for batch_index,(data ,target) in enumerate(train_loader):#一批中的一个，（图片，标签）
        data,target = data.to(device),target.to(device)#部署到DEVICE上去
        optimizer.zero_grad()#梯度初始化为0
        output = model(data)#训练后的结果
        loss = F.cross_entropy(output,target)#多分类计算损失函数
        loss.backward()#反向传播 得到参数的梯度参数值
        optimizer.step()#参数优化
        if batch_index %3000 == 0:#每3000个打印一次
            print("Train Epoch: {} \t Loss:{:.6f}".format(epoch,loss.item()))

def test_model(model,device,text_loader):
    model.eval()#模型验证
    correct = 0.0#正确
    Accuracy = 0.0#正确率
    text_loss = 0.0
    with torch.no_grad():#不会计算梯度，也不会进行反向传播
        for data,target in text_loader:
            data,target = data.to(device),target.to(device)#部署到device上
            output = model(data)#处理后的结果
            text_loss += F.cross_entropy(output,target).item()#计算测试损失之和
            pred = output.argmax(dim=1)#找到概率最大的下标（索引）
            correct += pred.eq(target.view_as(pred)).sum().item()#累计正确的次数
        text_loss /= len(test_loader.dataset)#损失和/数据集的总数量 = 平均loss
        Accuracy = 100.0*correct / len(text_loader.dataset)#正确个数/数据集的总数量 = 正确率
        print("Test__Average loss: {:4f},Accuracy: {:.3f}\n".format(text_loss,Accuracy))

for epoch in range(1,EPOCHS+1):
    train_model(model,DEVICE,train_loader,optimizer,epoch)
    test_model(model,DEVICE,test_loader)

torch.save(model.state_dict(),'model.ckpt')
