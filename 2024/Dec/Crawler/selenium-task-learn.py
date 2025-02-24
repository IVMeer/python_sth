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
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    # 等待页面加载完成（根据具体情况调整时间或改为显式等待）
    # driver.implicitly_wait(1)
    page_text = driver.find_element(By.ID, 'my-text-id').text
    print(page_text)

finally:
    # 关闭浏览器
    driver.quit()
