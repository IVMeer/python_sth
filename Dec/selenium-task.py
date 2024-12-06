import time
from selenium import webdriver
# from [selenium.webdriver.common.by](http://selenium.webdriver.common.by/) import By
from bs4 import BeautifulSoup
import pandas as pd

# 定义要抓取的城市列表

cities = ["广州市"]

# 定义年份范围

years = list(range(2017, 2024))

# 存储所有数据的字典

data_dict = {
    '城市': [],
    '年份': [],
    '地区生产总值(亿元)': []
}

# 网站链接

urls = ["https://tjj.gz.gov.cn/datav/admin/home/www_nj/"]

def fetch_data(url):
# 设置 ChromeOptions
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")  # 无头模式
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

# 初始化 WebDriver
    driver = webdriver.Chrome(options = chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # 等待页面加载完成

        # 获取页面源码
        html_content = driver.page_source
        return html_content
    except Exception as e:
        print(f"Failed to retrieve data from {url}: {e}")
        return None
    finally:
        driver.quit()

def parse_html(html_content, city):
    soup = BeautifulSoup(html_content, 'lxml')


    parsed_data = {'城市': city}
    found_any_data = False

    table = soup.find('table')  # 找到第一个表格
    if table:
        rows = table.find_all('tr')
        header_row = rows[0]
        headers = [header.get_text(strip=True) for header in header_row.find_all(['th', 'td'])]

        for row in rows[1:]:
            cols = row.find_all(['th', 'td'])
            col_texts = [col.get_text(strip=True) for col in cols]

            if len(col_texts) >= len(headers) and city in col_texts[0]:
                year_str = col_texts[1]

                try:
                    year = int(year_str)
                    if year in years:
                        parsed_data['年份'] = year

                        for i, header in enumerate(headers):
                            if header == '地区生产总值(亿元)':
                                parsed_data[header] = col_texts[i]

                        data_dict['城市'].append(city)
                        data_dict['年份'].append(year)
                        data_dict['地区生产总值(亿元)'].append(parsed_data.get('地区生产总值(亿元)', 'N/A'))

                        found_any_data = True
                except ValueError:
                    continue

    if not found_any_data:
        print(f"No data found for {city} in the specified years")

    for url in urls:
        html_content = fetch_data(url)
        if html_content:
            for city in cities:
                parse_html(html_content, city)

    # 将数据保存到DataFrame并导出为CSV文件

    df = pd.DataFrame(data_dict)
    df.to_csv('guangzhou_economic_indicators.csv', index=False, encoding='utf-8-sig')

    print("Data extraction complete.")

    # 读取并显示生成的CSV文件内容

    try:
        df_output = pd.read_csv('guangzhou_economic_indicators.csv')
        print("\nGenerated CSV Content:")
        print(df_output)
    except Exception as e:
        print(f"Error reading CSV file: {e}")