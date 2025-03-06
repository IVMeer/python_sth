from pathlib import Path
import pandas as pd

# 获取当前工作目录
current_path = Path.cwd()
print(f"当前路径: {current_path}")

# 目标文件路径
folder_path = current_path / '2024' / 'Dec' / 'Excel'
file_name = folder_path / '0223-优惠多.csv'

# 检查文件是否存在
if not file_name.exists():
    print(f"文件 {file_name} 不存在!")
    exit()

# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv(file_name)

# 输入日期（你可以修改为动态输入）
date = '2025/2/21'

# 过滤 DataFrame
filter_df = df[(df['日期'] == date) & (df['完成情况'] == '已完成')]

# 合并结果列
filter_df['合并结果'] = (
    filter_df['数据包日期'].astype(str) + '-' +
    filter_df['机器号'].astype(str).str.zfill(2) + '-' +
    filter_df['文件夹号数'].apply(lambda x: str(x) if isinstance(x, str) and '_' in x else str(int(x)))
)

# 删除不需要的列
filter_df.drop(columns=['数据包日期', '机器号', '文件夹号数'], inplace=True)

# 将合并结果插入到第二列
filter_df.insert(1, '时间', filter_df.pop('合并结果'))

# 输出结果
print(filter_df)

# 转换日期格式
date_convert = date.replace('/', '-')

# 获取文件名中的 '-xx' 中的 xx 部分
file_name_part = file_name.stem.split('-')[1]

# 定义输出文件名
output_file_name = folder_path / f'{date_convert}-{file_name_part}-完成名单.csv'

# 保存完成名单为 csv 格式
filter_df.to_csv(output_file_name, index=False)
print('已输出!')
print(f"完成名单→ {output_file_name}")
