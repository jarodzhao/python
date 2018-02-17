import requests
import sqlite3
import random
import time
import uuid
from bs4 import BeautifulSoup as bsp

class Item:
	def __init__(self, price, type, title, user, label, desc, more, zhi, unzhi, fav, comments, time, store, buy_link):
		self.title = title
		self.price = price
		self.type = type
		self.user = user
		self.label = label	#格式：分类 标签 标签
		self.desc = desc
		self.more = more
		self.zhi = zhi
		self.nuzhi = unzhi
		self.fav = fav
		self.comments = comments
		self.time = time
		self.store = store
		self.buy_link = buy_link

	def __repr__(self):
		return ' 测试 repr 函数'
	def __str__(slef):
		return ' 测试 str 函数'

item = Item


def get_last_time():
    last_time = ''

    conn = sqlite3.connect('smzdm.db')
    sql = 'select time_ from faxian order by time_ desc limit 1'
    cursor = conn.execute(sql)

    for item in cursor:
    	print(item[0])

    cursor.close()
    conn.close()
    # return cursor


if __name__ == '__main__':
	
	for i in range(10):
		if i > 5:
			i += 1
			break
		print(i)

	#<img src="https://y.zdmimg.com/201802/17/5a8708aa076625755.jpg_d200.jpg" alt="中华老字号 鹰金钱 豆豉鲮鱼罐头 227g" title="" width="200px" height="200px" style="margin-top:0px">