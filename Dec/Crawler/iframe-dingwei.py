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
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myframe"))
    )
    print("iframe 加载完成")
    
    # 定位 iframe 并切换到其中
    iframe = driver.find_element(By.ID, "myframe")
    driver.switch_to.frame(iframe)
    print("已切换到 iframe")
    # 在 iframe 内查找目标元素
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@href='directory/01.html']"))
    )
    print("目标元素1已找到:", element.text)

    # 点击目标链接
    element.click()
    
    element2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//a[@href="01/html/01-14.htm"]'))
    )
    print("目标元素2已找到:", element2.text)
    element2.click()
   
    # 先定位到iframe
    # WebDriverWait(driver, 3).until(
    #     EC.presence_of_element_located((By.ID, "myframe"))
    # )
    # print('等待iframe加载完成')
    
    # # 在定位到 tbody
    # WebDriverWait(driver, 30).until(
    #     EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
    # )
    # print('tbody 元素已加载完成')
    
    
    # # 创建一个空的列表来存储数据
    # table_data = []
    # 通过更长的等待时间确保新 iframe 完全加载
    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "myframe"))  # 根据新 iframe 的 ID 或其他定位方式
    # )
    # print("新的 iframe 已加载")

    # # 定位到新的 iframe 并切换
    # iframe2 = driver.find_element(By.ID, "myframe")  # 如果加载了新的 iframe, 需要重新获取
    # driver.switch_to.frame(iframe2)
    
    # # 等待 iframe 内的表格元素加载（你可以选择要等待的具体元素）
    # WebDriverWait(driver, 3).until(
    #     EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
    # )
    # print("表格数据已加载")
    table_data = []
    #首先找到tbody元素
    # element3 = driver.find_element(By.TAG_NAME, 'tbody') 
    # element3 = WebDriverWait(driver, 3).until(
    #     EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
    # )
    
    
    element3 = driver.find_element(By.TAG_NAME, 'tbody')
    driver.implicitly_wait(10)
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
    # df.to_csv('output.csv', index=False, encoding='utf-8')
    # df.to_csv('no-strip.csv', index=False, encoding='utf-8')
    df.to_csv("load-too-fast.csv", index=False, encoding='utf-8')
    # 将数据保存为excel
    # df.to_excel('output.xlsx', index=False)    
    


finally:
    # 退出浏览器
    driver.quit()
