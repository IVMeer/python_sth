import os

def count_jpg_files_by_directory(directory):
    jpg_counts = {}
    total_count = 0

    for root, _, files in os.walk(directory):
        count = sum(file.lower().endswith('.jpg') for file in files)
        if count > 0:  # 只显示包含 JPG 文件的目录
            jpg_counts[root] = count
            total_count += count

    # 打印每个目录的 JPG 文件数量
    for dir_path, count in jpg_counts.items():
        print(f"{dir_path}: {count} 张 JPG 图片")

    # 打印总计
    print(f"\nJPG 文件总数（含子目录）: {total_count}")

# 指定文件夹路径
folder_path = r'Z:\anti-thief-oss-anno\20250310'
subfiles = ['Q1400028_scanning','Q1400029_scanning','Q1400030_scanning']
count_jpg_files_by_directory(folder_path,subfiles)
