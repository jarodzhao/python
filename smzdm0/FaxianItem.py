import time, random

class Item:

    # 抓取间隔时间
    next_time = 600 + int(random.random() * 100)

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

class Comment:
    def __init__(self, id_, floor, user_, user_level, user_url, time_, quote, comment_, platform, item_url, ding, cai):
        self.id_ = id_
        self.floor = floor
        self.user_ = user_
        self.user_level = user_level
        self.user_url = user_url
        self.time_ = time_
        self.quote = quote
        self.comment_ = comment_
        self.platform = platform
        self.item_url = item_url
        self.ding = ding
        self.cai = cai


class FaxianExt:
    def __init__(self):
        pass