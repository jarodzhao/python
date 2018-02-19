import requests
from smzdm.faxian import FaxianItem as Item
from bs4 import BeautifulSoup as bsp

'''
抓取 HTML 源方法
'''
def get_html(url, tag=None):
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
    r = requests.get(url, headers=headers)
    page_html = bsp(r.text, 'html.parser')

    html = content.findAll(tag[0], tag[1])

    return html