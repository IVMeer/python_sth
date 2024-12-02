import requests
from parsel import Selector
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0'
}


parsel_docs_url = 'https://parsel.readthedocs.org/en/latest/_static/selectors-sample1.html'

page_text = requests.get(parsel_docs_url).text

slector = Selector(text=page_text)

print(page_text)