import time

class FaxianItem():

    '''
    抓取间隔时间
    '''
    next_time = 30

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
        if time.find('-') == -1:
            today = time.strftime('%m-%d ', time.localtime())
            self.time_ = today + time
        else:
            self.time_ = time


if __name__ == '__main__':
    item = FaxianItem('a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b')
    item.is_today()

