from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
chromedriver_path = 'E:\\workspace\\python_demo\\Dec\\chromedriver.exe'

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome()

try:
    # 打开目标页面
    driver.get("https://tjj.gz.gov.cn/datav/admin/home/www_nj/")

    # 判断目标元素是否直接可见
    try:
        element = driver.find_element(By.XPATH, "//a[@href='directory/01.html']")
        print("目标元素不在 iframe 中")
    except:
        print("目标元素不在主页面中，开始检查 iframe")

    # 获取所有 iframe
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"页面中共有 {len(iframes)} 个 iframe")

    # 遍历每个 iframe
    found = False
    for index, iframe in enumerate(iframes):
        driver.switch_to.frame(iframe)
        try:
            # 尝试在 iframe 中查找目标元素
            element = driver.find_element(By.XPATH, "//a[@href='directory/01.html']")
            print(f"目标元素在第 {index + 1} 个 iframe 中")
            found = True
            break
        except:
            print(f"目标元素不在第 {index + 1} 个 iframe 中")
        finally:
            driver.switch_to.default_content()  # 切回主页面

    if not found:
        print("目标元素不在任何 iframe 中")

finally:
    driver.quit()
