"""
Count directory numbers
"""

import os

def count_jpg_files_recursive(directory):
    return sum(
        file.lower().endswith('.jpg') for _, _, files in os.walk(directory) for file in files)


folder_path = r'C:\Users\win11\Desktop\123'
print(f'jpg文件总数(含子目录下的):{count_jpg_files_recursive(folder_path)}')

