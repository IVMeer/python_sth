import os
import xml.etree.ElementTree as ET

# 定义输入和输出目录
input_dir = "C:\\Users\win11\Desktop\default"
output_dir = "C:\\Users\win11\Desktop\yolo"

# 定义标签映射
label_map = {
    "person": "0",
    "car": "1",
    # 在这里添加更多标签及其对应的 YOLO 格式标签
}

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 遍历XML文件
for filename in os.listdir(input_dir):
    if filename.endswith(".xml"):
        # 解析XML文件
        tree = ET.parse(os.path.join(input_dir, filename))
        root = tree.getroot()

        # 提取图片名称
        image_name = root.find("filename").text

        # 提取图片尺寸
        image_width = int(root.find("imagesize/ncols").text)
        image_height = int(root.find("imagesize/nrows").text)

        # 输出YOLO格式的标注文件
        yolo_filename = os.path.splitext(filename)[0] + ".txt"
        yolo_filepath = os.path.join(output_dir, yolo_filename)
        with open(yolo_filepath, "w") as f:
            for obj in root.findall("object"):
                # 提取标签名称
                label = obj.find("name").text
                if label in label_map:
                    label = label_map[label]
                else:
                    continue

                # 提取边界框坐标
                x1 = float(obj.find("polygon/pt/x").text)
                y1 = float(obj.find("polygon/pt/y").text)
                x2 = float(obj.find("polygon/pt[2]/x").text)
                y2 = float(obj.find("polygon/pt[2]/y").text)
                x3 = float(obj.find("polygon/pt[3]/x").text)
                y3 = float(obj.find("polygon/pt[3]/y").text)
                x4 = float(obj.find("polygon/pt[4]/x").text)
                y4 = float(obj.find("polygon/pt[4]/y").text)

                # 计算YOLO格式的边界框参数
                x_center = (x1 + x2 + x3 + x4) / 4 / image_width
                y_center = (y1 + y2 + y3 + y4) / 4 / image_height
                width = (abs(x2 - x1) + abs(x3 - x4)) / 2 / image_width
                height = (abs(y4 - y1) + abs(y2 - y3)) / 2 / image_height

                # 写入YOLO格式的标注文件
                f.write(f"{label} {x_center:.6f} {y_center:.6f} {width:.6f} {height:.6f}\n")