import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service




chromedriver_path = 'E:\\workspace\\python_demo\\Dec\\Crawler\\chromedriver.exe'
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

try:
    # driver.get('http://192.168.30.245:8080/tasks/create?projectId=63')
    driver.get('http://192.168.30.245:8080/')
    # 验证登录
    """
    一共有三种定位方式:
    1.find_elements匹配元素,通过索引选择;
    have = driver.find_elements(By.CSS_SELECTOR, '.ant-typography.css-n0gjrg')
    need = have[2]
    
    2.通过xpath文本定位;
    
    3.通过父元素定位。
    # 如果目标 <span> 位于一个特定的父元素中
    parent_element = driver.find_element(By.ID, 'parent-id')  # 假设父元素有一个 ID
    # 然后通过父元素来定位目标 <span>
    target_element = parent_element.find_element(By.CSS_SELECTOR, '.ant-typography.css-n0gjrg')

    
    By.CLASS_NAME 不支持多个class类名,只能写成(By.CLASS_NAME, 'ant-typography')
    这里用CSS_SELECTOR的话,因为有三个相同类名。所以得用find_elements,再用索引去定位。
    
    """
    # target_element = driver.find_element(By.XPATH, "//span[@class='ant-typography css-n0gjrg' and text()='Email or username']")
    # target_element.send_keys('')
    # 使用 XPath 根据文本内容定位
    # wait = WebDriverWait(driver, 10)
    # target_element = wait.until(
    #     EC.presence_of_all_elements_located(
    #         (By.CSS_SELECTOR, '.ant-typography.css-n0gjrg')
    #     )
    # )
    # 延迟五秒等待页面加载完成。
    time.sleep(5)
    # 设置页面加载超时为30s
    # driver.set_page_load_timeout(10)
    span_element = driver.find_element(By.CSS_SELECTOR, '.ant-input-affix-wrapper.ant-input-affix-wrapper-focussed.css-n0gjrg.ant-input-outlined.cvat-input-floating-label')
    # 输出目标元素的文本
    print(span_element.text)
    span_element.click()
    span_element.send_keys('test')
    # WebDriverWait(driver, 3).until(
    #     EC.presence_of_element_located(
    #         (By.CSS_SELECTOR, '.ant-typography.css-n0gjrg')
    #     )
    # )
    # have = driver.find_elements(By.CSS_SELECTOR, '.ant-typography.css-n0gjrg')
    # print(have)
    # need = have[2]
    # need.send_keys('test')
    # time.sleep(10)
    
    
    
    
    
    
    
    # # 打开任务创建页面之前，遇到登录问题先解决登录问题先。
    # driver.get('http://192.168.30.245:8080/tasks/create?projectId=63')
    
    # time.sleep(10)
    # # enter the task name 
    # element_task_name = driver.find_element(By.ID, 'name')
    # # entet the text
    # element_task_name.send_keys('20241117')
    
    # element_select_file = driver.fine_element(By.CSS_SELECTOR, 'span.ant-upload.ant-upload-drag')
    # element_select_file.click()
    # time.sleep(10)
    
finally:
    driver.quit()