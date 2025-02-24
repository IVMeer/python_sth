from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# options = Options()
# options.add_argument('--headless')


# driver = webdriver.Chrome(options = options)
# driver.get("https://baidu.com")
# driver.quit()

driver = webdriver.Chrome()
    
driver.get("https://www.baidu.com")
# Find the search box
search_box = driver.find_element(By.ID, "kw")
# Enter the word to the search box
search_box.send_keys("selenium")
# Enter the "baiduyixia" button
submit_button = driver.find_element(By.ID, "su")
search_box.click()
driver.implicitly_wait(1000)

driver.quit()