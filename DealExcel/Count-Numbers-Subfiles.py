import os

def count_jpg_in_specific_subdirectories(parent_directory, target_subdirs):
    jpg_counts = {}
    total_count = 0

    for subdir in target_subdirs:
        subdir_path = os.path.join(parent_directory, subdir)  # 构造完整路径
        if os.path.exists(subdir_path) and os.path.isdir(subdir_path):  # 确保是目录
            count = sum(file.lower().endswith('.jpg') for file in os.listdir(subdir_path) if os.path.isfile(os.path.join(subdir_path, file)))
            jpg_counts[subdir_path] = count
            total_count += count

    # 输出统计结果
    for dir_path, count in jpg_counts.items():
        print(f"{dir_path}: {count} 张 JPG 图片")

    print(f"\n指定子目录的 JPG 文件总数: {total_count}")

# 指定父目录和目标子目录
folder_path = r'Z:\anti-thief-oss-anno\20250310'
target_subdirs = {'Q1400028_scanning', 'Q1400029_scanning','Q1400030_scanning'}  # 只统计 B 和 D 目录中的 JPG 文件

count_jpg_in_specific_subdirectories(folder_path, target_subdirs)
