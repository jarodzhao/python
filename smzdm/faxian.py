import time, random

class FaxianItem:

    # 抓取间隔时间
    next_time = 1800 + int(random.random() * 1000)

    def __init__(self, id_, first, item_type, title, price, store, time, url, user, user_url, desc, zhi, comments, buy_link):
        self.id_ = id_
        self.first = first
        self.item_type = item_type
        self.title = title
        self.price = price
        self.store = store
        self.url = url
        self.user_ = user
        self.user_url = user_url
        self.desc = desc
        self.zhi = zhi
        self.comments = comments
        self.buy_link = buy_link
        # 如果才能使单独赋值属性时，也自动加上日期？？
        if time.find('-') == -1:
            today = time.strftime('%m-%d ', time.localtime())
            self.time_ = today + time
        else:
            self.time_ = time
