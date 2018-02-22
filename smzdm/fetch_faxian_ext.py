from getSMZDM import *
from smzdm.faxian import FaxianItem as Item
import re

class faxianExt:
	def __init__(self):
		pass

def fetch_ext(onclick_str):
	res = re.match('gtmAddToCart\(\{(.*)\}\)', onclick_str)
	
	if res != None:
		info = {}
		s = res.group(1).split(',')

		for a in s:
			ass = a.split(':')
			info[ass[0].replace('\'', '').strip()] = ass[1].replace('\'', '').strip()

'''
<a class="z-btn z-btn-red" href="https://go.smzdm.com/67d245dc5a10ff6b/ca_aa_fx_163_8746168_10054_47271_171" target="_blank" 
onclick="gtmAddToCart({'name':'雅语苹果ipad air2保护套休眠ipadair1平板56保护壳皮套超薄韩国','id':'8746168' , 'price':'19','brand':'YAGHVEO/雅语' ,'mall':'天猫精选', 'category':'电脑数码/数码配件/保护壳/无','metric1':'19','dimension10':'tmall.com','dimension9':'faxian','dimension11':'1阶价格','dimension12':'天猫精选','dimension20':'无','dimension32':'先发后审','dimension25':'10054'})" rel="nofollow" _hover-ignore="1">去购买<i class="z-icon-arrow-right"></i></a>
'''


		fe = faxianExt
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
	else:
		return res

def save_ext(fe):
    conn = sqlite3.connect('smzdm.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists faxian_ext (id_, fid, name, price, brand, mall, category, metric1, dimension10, dimension9, dimension11, dimension12, dimension20, dimension32, dimension25)')

    sql = 'insert into faxian_ext values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(sql, (fe.id_, fe.fid, fe.name, fe.price, fe.brand, fe.mall, fe.category, fe.metric1, fe.dimension10, fe.dimension9, fe.dimension11, 
        fe.dimension12, fe.dimension20, fe.dimension32, fe.dimension25))

    conn.commit()
    conn.close()

if __name__ == '__main__':
	onc = "gtmAddToCart({'name':'SID 超人 RS339 电动剃须刀','id':'8745901' , 'price':'85','brand':'SID/超人' ,'mall':'京东', 'category':'家用电器/个护健康/剃须除毛/电动剃须刀','metric1':'85','dimension10':'jd.com','dimension9':'faxian','dimension11':'3阶价格','dimension12':'京东','dimension20':'无','dimension32':'先发后审','dimension25':'无'})"
	t = fetch_ext(onc)

	print(t.category)