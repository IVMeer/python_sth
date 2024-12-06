import requests
from lxml import html

# Headers 防止被反爬
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

# 爬取页面的函数
def scrape_poems():
    for page_num in range(10):  # 爬取前10页
        url = f'https://www.gushiwen.cn/default_{page_num + 1}.aspx'
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            tree = html.fromstring(response.content)

            # 使用 XPath 提取标题、作者和朝代、正文内容
            titles = tree.xpath('//div[@class="left"]/div[@class="cont"]/a/text()')  # 获取标题
            authors_dynasties = tree.xpath('//div[@class="left"]/div[@class="cont"]/p[@class="source"]/text()')  # 获取作者与朝代
            contents = tree.xpath('//div[@class="left"]/div[@class="contson"]/text()')  # 获取正文内容
            
            # 输出每一首古诗文的信息
            for title, author_dynasty, content in zip(titles, authors_dynasties, contents):
                print(f"标题: {title.strip()}")
                print(f"作者与朝代: {author_dynasty.strip()}")
                print(f"正文: {content.strip()}")
                print('-' * 50)
        else:
            print(f"无法访问页面: {url}, 状态码: {response.status_code}")

# 调用爬取函数
scrape_poems()
