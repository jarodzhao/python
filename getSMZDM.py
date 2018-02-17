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
获取数据库中最新记录的时间戳
'''
def get_last_title():
    last_title = ''

    conn = sqlite3.connect('smzdm.db')
    sql = 'select title from faxian order by id_ desc limit 1'
    cursor = conn.execute(sql)

    for item in cursor:
        last_title = item[0]

    return last_title

'''
分离数据
传进来的是 li 标签
'''
def fetch_data(li):
    item.id_ = time.time()

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


def save_data(page, wait, last_title):
    url = 'https://faxian.smzdm.com/p' + str(page)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

    r = requests.get(url, headers=headers)

    cont = bsp(r.text, 'html.parser')

    ul_html = cont.find('ul', id='feed-main-list')
    li_html = ul_html.findAll('li')

    #获取数据库最新记录的时间
    has_item = False

    #计数器
    item = []

    #开爬 smzdm
    for li in li_html:
        item = fetch_data(li) #分离出商品条目信息

        # if item.title == last_title:
        #     has_item = True
        #     break

        in_dB(item)

        print('%s | %s\n%s %s %s 评：%s\n%s %s\n%s\n%s' % (item.item_type, item.title, item.store, item.price, item.time_, item.comments, item.user_, item.user_url, item.desc, item.buy_link), end='\n-\n')

    print('***************************************** 第 %s 页, 等待 %s 秒继续下一页... **************************************************' % (page, wait))
    
    if has_item == True:
        print('已获取到截止上次操作后的所有数据！\n最后获取记录： %s' % item.title)

    return has_item

'''插入对象到数据库'''
def in_dB(item):
    conn = sqlite3.connect('smzdm.db0')
    cursor = conn.execute('create table if not exists faxian (id_, item_type, title, price, store, time_, url, user_, user_url, desc, zhi, comments, buy_link)')

    sql = 'insert into faxian values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'

    cursor.execute(sql, (item.id_, item.item_type, item.title, item.price, item.store, item.time_, item.url, item.user_, item.user_url, item.desc, item.zhi, item.comments, item.buy_link))
    conn.commit()

    cursor.close()
    conn.close()

'''外层循环1'''
def go_loop_1():
    goon = True #继续循环

    # 这里继续下次循环时应重新获取一下数据库中的时间戳
    last_title = get_last_title()

    for page in range(1000):
        wait = int(random.random() * 5)
        page += 1

        #程序编写错误，02-16 19:42 至 02-17 00:00 时间段有重复记录
        # if save_data(page, wait, last_title) == True:
        #     goon = False
        #     break
        save_data(page, wait, last_title)
        time.sleep(wait)

    return goon

'''页面执行入口'''
if __name__ == '__main__':
    while go_loop_1() == False:
        wait2 = 20 + int(random.random() * 30)
        print('\n暂停 %s 秒后继续...\n' % int(wait2))
        time.sleep(wait2)