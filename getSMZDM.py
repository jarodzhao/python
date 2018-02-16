import requests
import sqlite3
import random
import time
from bs4 import BeautifulSoup as bsp

class Item:
    def __init__(self, id_, item_type, title, price, store, time, url, user, user_url, desc, zhi, comments, buy_link):
        self.id_ = id_
        self.item_type = item_type
        self.title = title
        self.price = price
        self.store = store
        self.time_ = time
        self.url = url
        self.user_ = user
        self.user_url = user_url
        self.desc = desc
        self.zhi = zhi
        self.comments = comments
        self.buy_link = buy_link

item = Item

'''
分离数据
传进来的是 li 标签
'''
def fetchData(li):
    item.id_ = random.random()

    #1 div
    feed_block_ver = li.find('div', class_='feed-block-ver')

    #2 div 类别信息（可选）
    feed_ver_pic = li.find('div', class_='feed-ver-pic')
    tag = feed_ver_pic.find('span')
    if tag != None:
        item.item_type = tag.text
    else:
        item.item_type = 'no'

    #2 h5 标题和zdm_url
    h5 = li.find('h5')
    item.title = h5.find('a').text
    item.url = h5.find('a')['href']

    #  电商
    mall = li.find('a', class_='tag-bottom-right')
    item.store = mall.text

    #2 div 价格
    z_highlight = li.find('div', class_='z-highlight')
    item.price = z_highlight.text.strip()

    #2 span 用户信息
    feed_ver_row = li.find('div', class_='feed-ver-row')

    if feed_ver_row.find('div', 'feed-ver-row-l') != None:
        feed_ver_row_l = feed_ver_row.find('div', class_='feed-ver-row-l')

        if feed_ver_row_l.find('span', class_='z-avatar-group') != None:
            z_avatar_group = feed_ver_row_l.find('span', class_='z-avatar-group')

            if z_avatar_group.find('a', class_='z-avatar-name') != None:
                item.user_ = z_avatar_group.find('a', class_='z-avatar-name').text.strip()
                item.user_url = z_avatar_group.find('a', class_='z-avatar-name')['href']
            else:
                item.user_ = z_avatar_group.text.strip()
                item.user_url = 'a#'
        else:
            item.user_ = feed_ver_row_l.text.strip()
            item.user_url = 'b#'
    else:
        item.user_ = '$$'   #根本没有用户信息
        item.user_url = 'c#'


    # 发布时间
    today = time.strftime('%m-%d ', time.localtime())

    feed_ver_row_r = li.find_all(class_='feed-ver-row-r')

    for tag in feed_ver_row_r:
        if tag.find('div', class_='feed-link-btn') == None:
            time_ = tag.text

    if time_.find('-') == -1:
        item.time_ = today + time_
    else:
        item.time_ = time_

    #2 div 描述信息
    feed_ver_descripe = li.find('div', class_="feed-ver-descripe")
    item.desc = feed_ver_descripe.text.strip()

    #5 span 值
    unvoted_wrap = li.find('span', class_='unvoted-wrap')
    item.zhi = unvoted_wrap.find('span').text

    #5 i 评论数
    comments = li.find('i', class_='z-icon-comment')
    item.comments = comments.find_parent().text

    #  购买链接
    link = li.find('div', class_='feed-link-btn').find('a')
    item.buy_link = link['href']

    return item


def saveData(p, w):
    url = 'https://faxian.smzdm.com/p' + str(p)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

    r = requests.get(url, headers=headers)

    cont = bsp(r.text, 'html.parser')

    ul_html = cont.find('ul', id='feed-main-list')
    li_html = ul_html.findAll('li')

    s = 0

    #开爬 smzdm
    for li in li_html:
        item = fetchData(li) #分离出商品条目信息
        inDB(item)

        # try:
        #     inDB(item) #入库
        # except:
        #     print('err: %s' % li, end='\n')

        print('%s | %s\n%s %s %s 评：%s\n%s %s\n%s' % (item.item_type, item.title, item.store, item.price, item.time_, item.comments, item.user_, item.user_url, item.buy_link), 
            end='\n-\n')
    print('***************************************** 第 %s 页, 等待 %s 秒... **************************************************' % (p, w))

'''插入对象到数据上'''
def inDB(item):
    conn = sqlite3.connect('smzdm.db')

    cursor = conn.execute('create table if not exists faxian (id_, item_type, title, price, store, time_, url, user_, user_url, desc, zhi, comments, buy_link)')

    sql = 'insert into faxian values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    cursor.execute(sql, (item.id_, item.item_type, item.title, item.price, item.store, item.time_, item.url, item.user_, item.user_url, item.desc, item.zhi, item.comments, item.buy_link))
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == '__main__':
    for i in range(1000):
        w = int(random.random() * 5)
        i += 1
        saveData(i, w)
        time.sleep(w)