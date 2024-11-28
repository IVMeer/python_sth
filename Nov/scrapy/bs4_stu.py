import requests
from bs4 import BeautifulSoup
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0'
}
url = "https://www.zggdwx.com/"
response = requests.get(url, headers=headers)
page_text = response.text

# 解析数据
soup = BeautifulSoup(page_text, 'lxml')

# title_tags = soup.select('a.title')
# # 遍历列表
# for tag in title_tags:
#     print(tag.text)

# # 接下来获取description 标签
# description_tags = soup.select('.description')
# for des_tag in description_tags:
#     print(des_tag.text)

# 首先确定父类
cards = soup.select(".mdui-card")
for card in cards:
    # 获取标题
    title_tags = card.select_one('a.title') 
    title_text = title_tags.text if title_tags else None
    # 获取描述
    des_tags = card.select_one('.description')
    des_text = des_tags.text if des_tags else None
    print(f'标题：{title_text}，描述：{des_text}')
    print('\n')