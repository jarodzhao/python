import random
import time
from smzdm.faxian import FaxianItem as Item

item = Item

'''
抓取 HTML 源码的方法
'''
def get_html(page):
    url = 'https://faxian.smzdm.com/p' + str(page)
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

    r = requests.get(url, headers=headers)
    content = bsp(r.text, 'html.parser')

    ul_html = content.find('ul', id='feed-main-list')
    li_html = ul_html.findAll('li')    

    return li_html

def get_last_items():
    '''
    获取库中的最新时间戳的item列表
    '''
    conn = sqlite3.connect('smzdm0.db')
    cursor = conn.cursor()

    sql = 'SELECT * FROM faxian WHERE time_ = (SELECT time_ FROM faxian ORDER BY id_ LIMIT 1)'
    rs = cursor.execute(sql)

    items = []
    for row in cursor:
        item = Item(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12]) # 如何构建对象
        items.append(item)

    conn.close()
    return items

'''插入对象到数据库'''
def in_dB(item):
    conn = sqlite3.connect('smzdm0.db')
    cursor = conn.execute('create table if not exists faxian (id_, item_type, title, price, store, time_, url, user_, user_url, desc, zhi, comments, buy_link)')

    sql = 'insert into faxian values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(sql, (item.id_, item.item_type, item.title, item.price, item.store, item.time_, item.url, item.user_, item.user_url, item.desc, item.zhi, item.comments, item.buy_link))

    conn.commit()
    conn.close()

#======================
# 页面开始，向下顺序执行
#======================

'''外层循环'''
def go_loop():
    goon = True #是否继续循环，默认值继续

    for page in range(1000): #1000页为能获取到的最大页码
        #库中最晚时间戳的对象列表
        last_items = get_last_items()
        #等待几秒后继续下一页
        wait = int(random.random() * 5)
        page += 1

        if fetch_data(page, wait, last_items):
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
分离数据过程
'''
def fetch_data(page, wait, last_title):
    html = get_html(page)

    has_item = False
    item = ''

    #开爬 smzdm
    for li in html:
        item = fetch_item(li) #分离出商品条目信息

        '''
        如何辨别分离出来的这个 item 是抓上一页数据时存入库中的
        还是上一次抓取到的数据（如果是上次抓的，那应该是上次最早抓到的一条记录）
        方案：每次开始抓取数据时，抓到的第一条记录特别标记一下！
              此种方案是否可以解决问题？！
              如若可行，表中增加一个字段，抓取到的首条记录保存时间（或标
              识）之后抓取的记录保存为0（或者null)
        '''


        # if item.title == last_title:
        #     has_item = True
        #     break

        #数据入库
        #in_dB(item)

        print('%s | %s\n%s %s %s 评：%s\n%s %s\n%s\n%s' % (item.item_type, item.title, item.store, item.price, item.time_, item.comments, item.user_, item.user_url, item.desc, item.buy_link), end='\n-\n')

    print('***************************************** 第 %s 页, 等待 %s 秒继续下一页... **************************************************' % (page, wait))
    
    if has_item == True:
        print('已获取到截止上次操作后的所有数据！\n最后获取记录： %s' % item.title)

    return has_item

'''
分离对象过程
'''
def fetch_item(li):
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

    feed_ver_row_r = li.find_all(class_='feed-ver-row-r')

    for tag in feed_ver_row_r:  #这里会有两个 feed-ver-row-r，不包含 feed-link-btn 属性的标签即为时间
        if tag.find('div', class_='feed-link-btn') == None:
            time_ = tag.text
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

'''
页面执行入口
'''
if __name__ == '__main__':
    while go_loop() == False:
        wait2 = 20 + int(random.random() * 30)
        print('\n暂停 %s 秒后继续...\n' % int(wait2))
        time.sleep(wait2)