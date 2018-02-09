from urllib import request
import time

#公网地址
url1 = 'http://125.46.33.20:8011/sysadmin'

#APN地址
url2 = 'http://172.31.0.17/sysadmin'

try:
	response = request.urlopen(url1, timeout=5)
except urllib.URLError:
	print(u'网址错误！')
	exit()

html = response.read()
print(html)

fp = open('chinavvv.txt', 'w')
fp.wirte('hello')