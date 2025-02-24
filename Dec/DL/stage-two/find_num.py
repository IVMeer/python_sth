import os

folder_path = r'E:\\workspace\\python_demo'  # 替换为你的文件夹路径

# 获取文件夹下所有的文件和文件夹
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# 输出文件数量
print(f"文件夹中有 {len(files)} 个文件")
