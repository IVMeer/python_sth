from datetime import datetime, timedelta
from pathlib import Path
from cvat_sdk import Client

# 初始化客户端
client = Client(url="http://192.168.30.245:8080/")
client.login('evo', '123456')

# 基础路径配置
base_path = Path(r"\\192.168.30.17\video\anti-thief-oss")
start_date_str = "20241115"  # 起始日期
days_to_process = 2  # 需要处理的天数

# 转换为日期对象
start_date = datetime.strptime(start_date_str, "%Y%m%d")

# 处理日期范围
for day_offset in range(days_to_process):
    current_date = start_date + timedelta(days=day_offset)
    date_str = current_date.strftime("%Y%m%d")
    date_path = base_path / date_str

    # 确认目标路径存在
    if not date_path.exists():
        print(f"路径不存在: {date_path}")
        continue

    # 遍历子文件夹并上传
    for folder in date_path.iterdir():
        if folder.is_dir() and folder.name.endswith("_scanning"):
            print(f"开始处理文件夹: {folder}")

            # 创建任务名
            task_name = f"{date_str}-{folder.name}"
            task = client.tasks.create(name=task_name)

            # 收集所有子文件夹中的文件
            files_to_upload = []
            for sub_folder in folder.iterdir():
                if sub_folder.is_dir():
                    files_to_upload.extend(str(file) for file in sub_folder.iterdir() if file.is_file())

            if not files_to_upload:
                print(f"文件夹 {folder} 中没有可上传的文件。")
                continue

            # 上传文件
            print(f"上传文件到任务 {task_name}: {files_to_upload}")
            task.upload_data(files_to_upload)
        else:
            print(f"跳过非目标文件夹: {folder}")
