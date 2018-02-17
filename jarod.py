from bs4 import BeautifulSoup as bsp
import requests

def get_html(url, page):

    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
    r = requests.get(url + str(page), headers=headers)

    content = bsp(r.text, 'html.parser')

    ul_html = content.find('ul', id='feed-main-list')
    li_html = ul_html.findAll('li')