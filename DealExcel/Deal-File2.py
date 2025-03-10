from pathlib import Path
import pandas as pd


def process_files(folder_path: Path, file_names: list, date: str):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    # 确保输入的文件夹存在
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"文件夹 {folder_path} 不存在!")
        return
    
    # 转换日期格式
    date_convert = date.replace('/', '-')
    
    for file_name in file_names:
        file_path = folder_path / file_name
        
        if not file_path.exists():
            print(f"文件 {file_path} 不存在，跳过。")
            continue
        
        file_name_part = file_path.stem.split('-')[1] if '-' in file_path.stem else '未知'
        
        try:
            # 读取 CSV 文件
            df = pd.read_csv(file_path)
            
            # 过滤 DataFrame
            filter_df = df[(df['日期'] == date) & (df['完成情况'] == '已完成')]
            
            if filter_df.empty:
                print(f"文件 {file_path.name} 无符合条件的数据，跳过。")
                continue
            
            # 生成合并结果列
            filter_df['合并结果'] = (
                filter_df['数据包日期'].astype(int).astype(str) + '-' +
                filter_df['机器号'].astype(int).astype(str).str.zfill(2) + '-' +
                filter_df['文件夹号数'].apply(lambda x: str(x) if isinstance(x, str) and '_' in x else str(int(x)))
            )
            
            # 删除不需要的列
            filter_df.drop(columns=['数据包日期', '机器号', '文件夹号数'], inplace=True)
            
            # 将合并结果插入到第二列
            filter_df.insert(1, '时间', filter_df.pop('合并结果'))
            # 输出结果
            # print(filter_df)
            # 显示筛选后的数据行数和列数
            print(f"筛选后的数据共有 {filter_df.shape[0]} 行")
            
            # 定义输出文件名
            output_file_name = folder_path / f'{date_convert}-{file_name_part}-完成名单.csv'
            
            # 保存为 CSV 格式
            filter_df.to_csv(output_file_name, index=False)
            print(f'已输出完成名单→ {output_file_name}')
        
        except Exception as e:
            print(f"处理文件 {file_path.name} 时出错: {e}")

# 示例：输入文件夹路径和文件名列表
folder_path = Path.cwd() / 'DealExcel'
file_names = ['0310-唐山.csv', '0310-优惠多.csv','0310-金小象']  # 需要处理的文件名

date = '2025/3/10'  # 可以修改为动态输入
process_files(folder_path, file_names, date)
