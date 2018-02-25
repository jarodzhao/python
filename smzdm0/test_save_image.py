import re
import random
import time
from urllib import request

req = request.Request('http://mm.taobao.com/json/request_top_list.htm?page=1')

html = request.urlopen(req)

# 先假设 request.urlopen 的值每次请求后只能使用一次
# print(html.read().decode('gbk'))

pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',re.S)
items = re.findall(pattern, html.read().decode('gbk'))


def saveImg(url):
	req = request.Request(url)
	res = request.urlopen(req)

	fn = str(int(random.random() * 100000)) + '.jpg'

	f = open(fn, 'wb')
	f.write(res.read())
	f.close

	print('保存完毕！  ' + fn)


for i in items:
	img_url = 'https:' + i[1]
	saveImg(img_url)


