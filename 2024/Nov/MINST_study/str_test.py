# 例子1: 输出循环迭代次数
for i in range(5):
    print("This is iteration number " + str(i))

# 例子2: 构建文件名
file_prefix = "data_"
file_suffix = ".txt"
for i in range(10):
    file_name = file_prefix + str(i) + file_suffix
    print(file_name)

# 例子3: 处理列表数据
numbers = [1, 2, 3, 4, 5]
for i in range(len(numbers)):
    print("Number at index " + str(i) + " is " + str(numbers[i]))

# 例子4: 构建URL
base_url = "https://www.example.com/api/"
for i in range(1, 11):
    url = base_url + "item" + str(i)
    print(url)
