"""
爬取广州地区2017-2023生产总值的数据
统计年鉴数据→地区生产总值：1.综合→1-14（地区生产总值）→表格
待解决问题
1.strip()问题 
2.只爬取了2023，如何遍历切换爬取2017-2022的数据(多线程，多进程，异步，协程，分布式？以及生产者消费者模式)
3.XPATH\CSS_SELECTOR  选择元素不熟悉
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

# 初始化 WebDriver
chromedriver_path = 'E:\\workspace\\python_demo\\Dec\\chromedriver.exe'
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()

try:
    # 打开目标页面
    driver.get("https://tjj.gz.gov.cn/datav/admin/home/www_nj/")  

    # 等待 iframe 加载完成
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.ID, "myframe"))
    )
    print("iframe 加载完成" )
    
    # 定位 iframe 并切换到其中
    iframe = driver.find_element(By.ID, "myframe")
    driver.switch_to.frame(iframe)
    print("已切换到 iframe")
    
    # 在 iframe 内查找目标元素
    element = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='directory/01.html']"))
    )
    print("目标元素1已找到:", element.text)

    # 点击目标链接
    element.click()
    
    element2 = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//a[@href="01/html/01-14.htm"]'))
    )
    print("目标元素2已找到:", element2.text)
    # 点击链接，进入地区生产总值页面
    element2.click()
    time.sleep(5)
    print('已timesleep 10s')
    # 创建一个空的列表来存储数据
    table_data = []
    # 尝试使用 css-selector 定位 tbody
    element3 = driver.find_element(By.CSS_SELECTOR, 'tbody')

    # 遍历tbody 中的所有tr
    for tr in element3.find_elements(By.TAG_NAME, 'tr'):
        row = []
        # 遍历 tr 中的所有td
        for td in tr.find_elements(By.TAG_NAME, 'td'):
            # row.append(td.text.strip())
            text = td.text.strip()
            row.append(text if text else 'NA')
        if row:
            table_data.append(row)
    # print("表格数据:", table_data)
        
    df = pd.DataFrame(table_data, columns=["项目", "Item", "2021", "2022", "2022年比增长(%)"])
    
    print(df)
    
    # 将数据保存为csv
    df.to_csv("Guanghoutongji_Final.csv", index=False, encoding='utf-8')
    # 将数据保存为excel
    df.to_excel('Guanghoutongji_Final.xlsx', index=False)    
    


finally:
    # 退出浏览器
    driver.quit()
