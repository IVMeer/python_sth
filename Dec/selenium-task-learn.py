from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.service import Service
# 初始化 WebDriver
# driver = webdriver.Chrome(executable_path='./chromedriver.exe')
chromedriver_path = 'E:\\workspace\\python_demo\\Dec\\chromedriver.exe'

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    # 打开目标页面
    driver.get("https://tjj.gz.gov.cn/datav/admin/home/www_nj/")

    # 等待页面加载完成（根据具体情况调整时间或改为显式等待）
    driver.implicitly_wait(1)

    # 找到并点击 "2023年 条目1综合"
    year_section = driver.find_element(by = By.XPATH, value = "//a[@href='directory/01.html']")
    # 使用css selector 定位
    # element = driver.find_element(By.CSS_SELECTOR, "a[href='directory/01.html']")
    # year_section.click()
    
    # # 地区生产总值→点击
    # option_section = driver.find_element(By.XPATH, "//a[@href= '01/html/01-14.htm']")
    # option_section.click()

    # # 找到表格 1-14 的地区生产总值（替换为具体定位方式）
    # table = driver.find_element(By.XPATH, "//table[@class='your-table-class']")  # 修改为实际表格的定位方式

    # # 提取表格数据
    # rows = table.find_elements(By.TAG_NAME, "tr")
    # data = []
    # for row in rows:
    #     cols = row.find_elements(By.TAG_NAME, "td")
    #     data.append([col.text for col in cols])

    # # 转换为 DataFrame
    # df = pd.DataFrame(data[1:], columns=data[0])  # 假设第一行为表头
    # print(df)

    # # 保存到 CSV 文件
    # df.to_csv("地区生产总值.csv", index=False, encoding="utf-8")

finally:
    # 关闭浏览器
    driver.quit()
