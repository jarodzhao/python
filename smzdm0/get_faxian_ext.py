import re
import sqlite3
from FaxianItem import *


def fetch_ext(onclick_str):
	res = re.findall(r"('.*?':'.*?\\')", onclick_str, re.S)
	
	info = {}
	for item in res:
		ss = item.split(':')
		info[ss[0].replace('\'', '')] = ss[1].replace('\'', '')
	
	# print(info)
	
	fe = FaxianExt
	fe.id_ = time.time()
	fe.fid = info['id']
	fe.name = info['name']
	fe.price = info['price']
	fe.brand = info['brand']
	fe.mall = info['mall']
	fe.category = info['category']
	fe.metric1 = info['metric1']
	fe.dimension10 = info['dimension10']
	fe.dimension9 = info['dimension9']
	fe.dimension11 = info['dimension11']
	fe.dimension12 = info['dimension12']
	fe.dimension20 = info['dimension20']
	fe.dimension32 = info['dimension32']
	fe.dimension25 = info['dimension25']

	save_ext(fe)
	print('优惠商品扩展信息保存完毕！')
	print(' -----*----- ')

def save_ext(fe):
	conn = sqlite3.connect('smzdm.db')
	cursor = conn.cursor()
	cursor.execute('create table if not exists faxian_ext (id_, fid, name, price, brand, mall, category, metric1, '
	               'dimension10, dimension9, dimension11, dimension12, dimension20, dimension32, dimension25)')
	sql = 'insert into faxian_ext values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
	cursor.execute(sql, (fe.id_, fe.fid, fe.name, fe.price, fe.brand, fe.mall, fe.category, fe.metric1, fe.dimension10,
	                     fe.dimension9, fe.dimension11,	fe.dimension12, fe.dimension20, fe.dimension32, fe.dimension25))
	conn.commit()
	conn.close()


if __name__ == '__main__':
	#ss = ("gtmAddToCart({'name':'Jack N\'Jil l杰克吉尔 牙刷兔子图案1支+儿童牙膏香蕉味 50g','id':'8753131' , 'price':'11','brand':'' ,'mall':'Amcal中文官网', 'category':'母婴用品/洗护用品/婴儿护理用品/婴儿口腔护理','metric1':'11','dimension10':'amcal.com.au','dimension9':'faxian','dimension11':'1阶价格','dimension12':'Amcal中文官网','dimension20':'无','dimension32':'无','dimension25':'769'})")
	ss = ("gtmAddToCart({'name':'路狮 LS-2004儿童溜冰鞋','id':'8754398' , 'price':'49','brand':'路狮' ,'mall':'天猫精选', 'category':'运动户外/体育项目/轮滑运动/无','metric1':'49','dimension10':'tmall.com','dimension9':'faxian','dimension11':'2阶价格','dimension12':'天猫精选','dimension20':'无','dimension32':'先发后审','dimension25':'无'})")
	res = re.findall(r"('.*?':'.*?'[$|\s*,])", ss, re.S)
	
	info = {}
	for item in res:
		ss = item.split(':')
		info[ss[0].replace('\'', '')] = ss[1].replace('\'', '')
	
	print(res)
	print(info)
	
	
'''
"gtmAddToCart({'name':'路狮 LS-2004儿童溜冰鞋','id':'8754398' , 'price':'49','brand':'路狮' ,'mall':'天猫精选', 'category':'运动户外/体育项目/轮滑运动/无','metric1':'49','dimension10':'tmall.com','dimension9':'faxian','dimension11':'2阶价格','dimension12':'天猫精选','dimension20':'无','dimension32':'先发后审','dimension25':'无'})"
'''