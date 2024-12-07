from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# 初始化 WebDriver
chromedriver_path = 'E:\\workspace\\python_demo\\Dec\\chromedriver.exe'
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()

try:
    # 打开目标页面
    driver.get("https://tjj.gz.gov.cn/datav/admin/home/www_nj/")  

    # 等待 iframe 加载完成
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myframe"))
    )

    # 定位 iframe 并切换到其中
    iframe = driver.find_element(By.ID, "myframe")
    driver.switch_to.frame(iframe)

    # 在 iframe 内查找目标元素
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='directory/01.html']"))
    )
    print("目标元素找到:", element.text)

    # 如果需要点击目标链接
    element.click()
    
    element2 = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//a[@href="01/html/01-14.htm"]'))
    )
    print("目标元素2找到：", element2.text)
    element2.click()
    
    time.sleep(5)

finally:
    # 退出浏览器
    driver.quit()
