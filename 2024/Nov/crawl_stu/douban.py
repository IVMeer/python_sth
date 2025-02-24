import requests
from parsel import Selector
from bs4 import BeautifulSoup

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0'
}
# 静态翻页
def crwal_pages_format_method():
    for start in range(0,250,25):
        url = "https://movie.douban.com/top250?start={}&filter=".format(start)
        print(f'Scraping: {url}')
        response = requests.get(url, headers= head)

def crwal_pages_f_string_method():
    for start in range(0,250,25):
        url = f'https://movie.douban.com/top250?start={start}&filter='
        print(f'Scraping: {url}')
        response = requests.get(url, headers= head)

crwal_pages_format_method()
crwal_pages_f_string_method()