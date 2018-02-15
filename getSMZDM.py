import requests
import sqlite3
import random
import time
from bs4 import BeautifulSoup as bsp

class Item:
    def __init__(self, id, title, price, store, time, url):
        self.id_ = id
        self.title = title
        self.price = price
        self.store = store
        self.time_ = time
        self.url = url

item = Item

#分离数据
def featchData(data):
    item.id_ = random.random()
    li_1 = data.find('div', class_='feed-block-ver')
    tit_1 = li_1.find('h5', class_='feed-ver-title').find('a')
    item.title = tit_1.text
    pri_1 = li_1.find('div', class_='z-highlight')
    item.price = pri_1.text.strip()
    sto_1 = li_1.find('div', class_='feed-ver-pic').find('a', class_='tag-bottom-right')
    item.store = sto_1.text

    tim_1 = li_1.find('div', class_='feed-ver-row').find('div', class_='feed-ver-row-r')
    item.time_ = tim_1.text

    #第二个标签才是url
    url_1 = li_1.findAll('div', class_='feed-ver-row')
    url_2 = url_1[1].find('div', class_='feed-ver-row-r').find('div', class_='feed-link-btn').find('div', class_='feed-link-btn-inner').find('a')
    item.url = url_2['href']

    return item

def saveData(p):
    url = 'https://faxian.smzdm.com/p' + str(p)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

    r = requests.get(url, headers=headers)

    cont = bsp(r.text, 'html.parser')

    ul_html = cont.find('ul', id='feed-main-list')
    li_html = ul_html.findAll('li')

    #开爬 smzdm
    for li in li_html:
        item = featchData(li) #分离出商品条目信息
        inDB(item) #入库
        print('%s\n%s %s %s\n%s' % (item.title, item.store, item.price, item.time_, item.url), 
            end='\n\n')
    print('*******************************************************************************************')

'''插入对象到数据上'''
def inDB(item):
    conn = sqlite3.connect('smzdm.db')

    cursor = conn.execute('create table if not exists faxian (id_ varchar, title varchar, store varchar, price varchar, time_ varchar, url varchar)')

    sql = 'insert into faxian values (?, ?, ?, ?, ?, ?)'

    cursor.execute(sql, (item.id_, item.title, item.store, item.price, item.time_, item.url))
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    for i in range(100):
        i += 1
        saveData(i)
        time.sleep(5)