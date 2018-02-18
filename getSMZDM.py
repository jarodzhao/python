import random
import time
import sqlite3
import requests
from smzdm.faxian import FaxianItem as Item
from bs4 import BeautifulSoup as bsp

last_data = []

'''
抓取 HTML 源方法
'''
def get_html(page):
    url = 'https://faxian.smzdm.com/p' + str(page)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

    r = requests.get(url, headers=headers)
    content = bsp(r.text, 'html.parser')

    ul_html = content.find('ul', id='feed-main-list')
    li_html = ul_html.findAll('li')    

    return li_html

'''
获取库中的最新时间戳的item.url属性字符串列表、item.time_
可能存在同一时间多条记录，url 需要保存多条，所以 urls 是一个列表
因为 time_ 值都相同，所以保存一条即可
'''
def get_last_data():
    conn = sqlite3.connect('smzdm_test.db')
    cursor = conn.cursor()

    global last_data
    urls = []

    #除非是空数据库，否则一定会返回记录集
    sql = 'SELECT time_, url FROM faxian WHERE time_ = (SELECT time_ FROM faxian ORDER BY id_ LIMIT 1)'
    rs = cursor.execute(sql)

    for row in rs:
        urls.append(row[1])

    # 需要把 02-17 18:34 这样的时间转换一下 --------------------------
    last_data = [row[0], urls]

    conn.close()

    return last_data

'''
根据 item.title 判断库中是否已有该记录
'''
def has_item(item):
    conn = sqlite3.connect('smzdm_test.db')
    cursor = conn.cursor()

    sql = "select * from faxian where title = ?"
    result = cursor.execute(sql, (item.title)).fetchall()   #一个坑，不调用 fetchall() 方法，返回的数量始终为 -1

    if len(result) > 0:
        return True
    else:
        return False

#======================
# 页面开始，向下顺序执行
#======================

'''外层循环'''
def go_loop():
    goon = True #是否继续循环，默认值继续

    for page in range(1000): #1000页为能获取到的最大页码
        #库中最晚时间戳的对象列表
        last_data = get_last_data()
        #等待几秒后继续下一页
        wait = int(random.random() * 5)
        page += 1

        # goon 的返回值问题？！！
        if fetch_data(page, wait, last_data):
            '''
            如果抓取到的记录库中已有，并且有特殊标记的记录
            没有特殊标记的，视为本次抓取中的重复记录，自动忽略
            '''
            goon = False
            break
        
        #抓取完一页，等待几秒后再继续
        time.sleep(wait)

    return goon

'''
分离业务的逻辑过程
需要返回什么值？ ----------------------------
'''
def fetch_data(page, wait, last_data):
    html = get_html(page)
    item = Item   #每次循环开始，必须实例化一个新对象。-----------------------------------测试时，试一下看不能取消这一句
    
    #开始抓取 smzdm.faxiam
    for li in html:
        in_db_result = False    #每条记录写库前初始化写库结果为 False，写库成功后更新为 True
        item = fetch_item(li) #分离出商品条目信息（对于页面中确实两条一样的记录，是否作为两个对象处理？）

        '''
        如何辨别分离出来的这个 item 是抓上一页数据时存入库中的
        还是上一次抓取到的数据（如果是上次抓的，那应该是上次最早抓到的一条记录）
        方案： 每次开始抓取数据时，抓到的第一条记录特别标记一下！
              此种方案是否可以解决问题？！
              如若可行，表中增加一个字段，抓取到的首条记录保存时间（或标
              识）之后抓取的记录保存为0（或者null)

        每次写库，更新 write_time
        写库时检察上次时间，如果超过 3600 秒则认为是一次新的抓取开始
        
        使用全局变量 last_data[0] 保存最后写库时间，只要程序一直运行，该值就一直存在
        1.暂停xxxx秒后，该值依然存在并可继续使用
        2.重新启动后（停止后的重启），该值为数据库中的最新时间戳
        last_data 保存的时间戳为全局变量，所以该列表不能重新赋值，只能更新内容！！
        '''
        if time.time() - last_data[0] > item.next_time:
            #print('头条记录...\n')
            item.first = 1      #本次抓取的头条记录
        else:
            item.first = 0      #本次抓取的非头条记录

        '''
        重复记录比对：
            1.抓到的头条记录需要比对：
              a-是否在 last_data[1] 列表中
              b-库中是否存在？可能性很小，但有
            2.抓取的非头条记录
              a-库中是否存在？
            需要写一个方法，检测 item 是否存在 has_item(item)
        '''

        db_has_item = has_item(item) # True or False

        '''
        if 是头条记录：
            if 库中无：
                写入库中
            else 库中有：
                已抓取自上次操作后的所有数据
        else 不是头条记录：
            if 库中无：
                写入库中
            else 库中有
                重复了？！忽略！
        '''

        if item.first = 1:
            if not db_has_item:
                in_db(item)
            else:
                print('已获取到截止上次操作后的所有数据！\n最后获取记录： %s' % item.title)
                return False
                break   #跳出循环
        else:
            if not db_has_item:
                in_db(item)
                print('%s | %s\n%s %s %s 评：%s\n%s %s\n%s\n%s' % (item.item_type, item.title, item.store, item.price, item.time_, 
                    item.comments, item.user_, item.user_url, item.desc, item.buy_link), end='\n-\n')
            else:
                pass
                print('%s | %s\n%s %s %s 评：%s\n%s %s\n%s\n%s\n-------------本条已忽略!!!-------------' % (item.item_type, item.title,
                    item.store, item.price, item.time_, item.comments, item.user_, item.user_url, item.desc, item.buy_link), end='\n-\n')

        # 入库后需要返回两个结果：
        # 1.入库标识，记录是否写入库中 
        # 2.最后写库时间，需要保持在页面级的变量中
        # 写库操作只返回一个 boolean 为 True 的值，写库过程中更新最后写库时间到全局变量 last_data 中

    # 页面抓取完成，等候 x 秒后继续...
    print('***************************************** 第 %s 页, 等待 %s 秒继续下一页... **************************************************' % (page, wait))
    return True
    

'''
分离对象过程
'''
def fetch_item(html):
    item.id_ = time.time()

    #1 div
    feed_block_ver = html.find('div', class_='feed-block-ver')

    #2 div 类别信息（可选）
    feed_ver_pic = html.find('div', class_='feed-ver-pic')
    tag = feed_ver_pic.find('span')
    if tag != None:
        item.item_type = tag.text
    else:
        item.item_type = 'no'

    #2 h5 标题和zdm_url
    h5 = html.find('h5')
    item.title = h5.find('a').text
    item.url = h5.find('a')['href']

    #  电商
    mall = html.find('a', class_='tag-bottom-right')
    item.store = mall.text

    #2 div 价格
    z_highlight = html.find('div', class_='z-highlight')
    item.price = z_highlight.text.strip()

    #2 span 用户信息
    feed_ver_row = html.find('div', class_='feed-ver-row')

    if feed_ver_row.find('div', 'feed-ver-row-l') != None:
        feed_ver_row_l = feed_ver_row.find('div', class_='feed-ver-row-l')

        if feed_ver_row_l.find('span', class_='z-avatar-group') != None:
            z_avatar_group = feed_ver_row_l.find('span', class_='z-avatar-group')

            if z_avatar_group.find('a', class_='z-avatar-name') != None:
                item.user_ = z_avatar_group.find('a', class_='z-avatar-name').text.strip() #正常用户信息
                item.user_url = z_avatar_group.find('a', class_='z-avatar-name')['href']
            else:
                item.user_ = z_avatar_group.text.strip()
                item.user_url = '推广信息，无用户信息'
        else:
            item.user_ = feed_ver_row_l.text.strip()
            item.user_url = 'b#'
    else:
        item.user_ = '广告时间'   #根本没有用户信息
        item.user_url = '广告信息，无用户信息'

    feed_ver_row_r = html.find_all(class_='feed-ver-row-r')

    for tag in feed_ver_row_r:  #这里会有两个 feed-ver-row-r，不包含 feed-link-btn 属性的标签即为时间
        if tag.find('div', class_='feed-link-btn') == None:
            time_ = tag.text
    item.time_ = time_

    #2 div 描述信息
    feed_ver_descripe = html.find('div', class_="feed-ver-descripe")
    item.desc = feed_ver_descripe.text.strip()

    #5 span 值
    unvoted_wrap = html.find('span', class_='unvoted-wrap')
    item.zhi = unvoted_wrap.find('span').text

    #5 i 评论数
    comments = html.find('i', class_='z-icon-comment')
    item.comments = comments.find_parent().text

    #  购买链接
    link = html.find('div', class_='feed-link-btn').find('a')
    item.buy_link = link['href']

    return item

'''
插入对象到数据库
'''
def in_db(item):
    conn = sqlite3.connect('smzdm.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists faxian (id_, first, item_type, title, price, store, time_, url, user_, user_url, desc, zhi, comments, buy_link)')

    sql = 'insert into faxian values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(sql, (item.id_, item.first, item.item_type, item.title, item.price, item.store, item.time_, item.url, item.user_, item.user_url, item.desc, 
        item.zhi, item.comments, item.buy_link))

    conn.commit()
    conn.close()

    #最后写库时间更新
    global last_data
    last_data[0] = time.time()

    return True

'''
页面执行入口
'''
if __name__ == '__main__':
    while go_loop() == False:
        wait2 = 30 + int(random.random() * 20)
        print('\n暂停 %s 秒后重新开始...\n' % int(wait2))
        time.sleep(wait2)