import zipfile
from pathlib import Path

def unzip_files(zip_path, extract_to):
    zip_path = Path(zip_path)
    extract_to = Path(extract_to)
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print(f"解压完成: {zip_path} 到 {extract_to}")
        
zip_file = r'C:\Users\win11\Desktop\123\task_0122-28-1_annotations_2025_03_25_02_47_45_coco 1.0.zip'
output_folder = r"C:\Users\win11\Desktop\123"

unzip_files(zip_file, output_folder)