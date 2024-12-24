import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# 爬取页面的函数
def scrape_poems():
    for page_num in range(10):  # 爬取前10页
        url = f'https://www.gushiwen.cn/default_{ page_num + 1 }.aspx'
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            # soup = BeautifulSoup(response.text, 'html.parser')
            soup = BeautifulSoup(response.text, 'lxml')
            
            # 定位每首古诗文的外层容器
            poems = soup.find_all('div', class_='cont')

            for poem in poems:
                try:
                    # 标题
                    title = poem.find('a', class_='').get_text(strip=True)
                    
                    # 作者和朝代
                    author_dynasty = poem.find('p', class_='source').get_text(strip=True)
                    
                    # 正文
                    content = poem.find('div', class_='contson').get_text(strip=True)
                    
                    print(f"标题: {title}")
                    print(f"作者与朝代: {author_dynasty}")
                    print(f"正文: {content}")
                    print('-' * 50)
                except AttributeError:
                    # 如果某个字段不存在，跳过该条数据
                    continue
        else:
            print(f"无法访问页面: {url}, 状态码: {response.status_code}")
        print("=" * 50)
# 调用爬取函数
scrape_poems()
