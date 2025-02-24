import os
import json

# 设置输入目录路径
input_directory = 'C:/Users/win11/Desktop/1'

# 设置输出目录路径
output_directory = 'C:/Users/win11/Desktop/convert_1'




# 创建输出目录(如果不存在)
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 遍历输入目录中的所有文件
for filename in os.listdir(input_directory):
    if filename.endswith('.json'):
        # 构建输入文件路径
        input_file_path = os.path.join(input_directory, filename)
        
        # 构建输出文件路径
        output_file_path = os.path.join(output_directory, filename)
        
        try:
            # 读取JSON文件内容
            with open(input_file_path, 'r') as file:
                data = json.load(file)
            
            # 交换"shapes"列表中每个项目的"label"值
            for shape in data['shapes']:
                if 'label' in shape:
                    label = shape['label']
                    if label == '1':
                        shape['label'] = '0'
                    else:
                        shape['label'] = '1'
                else:
                    print(f"警告: {filename}中的'shapes'列表项没有找到'label'字段")
            
            # 将修改后的数据写入输出文件,保持原有缩进
            with open(output_file_path, 'w') as file:
                json.dump(data, file, indent=4)
        
        except (KeyError, ValueError) as e:
            print(f"错误: 处理 {filename} 时出现问题 - {e}")
            continue

print('所有JSON文件中的标签已成功交换,输出文件已保存在指定目录。')