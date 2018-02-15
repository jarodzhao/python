import requests
from bs4 import BeautifulSoup as bsp

class Item:
    def __init__(self, title, price, store, time, url):
        self.title = title
        self.price = price
        self.store = store
        self.time = time
        self.url = url

item = Item

#分离数据
def featchData(data):
    li_1 = data.find('div', class_='feed-block-ver')
    tit_1 = li_1.find('div', class_='feed-ver-descripe')
    item.title = tit_1.text.strip()
    pri_1 = li_1.find('div', class_='z-highlight')
    item.price = pri_1.text.strip()
    sto_1 = li_1.find('div', class_='feed-ver-pic').find('a', class_='tag-bottom-right')
    item.store = sto_1.text

    tim_1 = li_1.find('div', class_='feed-ver-row').find('div', class_='feed-ver-row-r')
    item.time = tim_1.text

    #第二个标签才是url
    url_1 = li_1.findAll('div', class_='feed-ver-row')
    url_2 = url_1[1].find('div', class_='feed-ver-row-r').find('div', class_='feed-link-btn').find('div', class_='feed-link-btn-inner').find('a')
    item.url = url_2['href']

    return item

url = 'https://faxian.smzdm.com/p1/'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

r = requests.get(url, headers=headers)
# print(r.text)

cont = bsp(r.text, 'html.parser')

ul_html = cont.find('ul', id='feed-main-list')


li_html = ul_html.findAll('li')

#开爬 smzdm
for li in li_html:
    item = featchData(li)
    print(' 电商：%s 价格：%s 时间：%s \n 标题：%s \n 地址：%s' % (item.store, item.price, item.time, item.title, item.url), 
        end='\n---------------------------------------------------------------------------------------\n')

