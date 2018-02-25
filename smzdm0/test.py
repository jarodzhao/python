import re

url = 'https://qny.smzdm.com/201802/25/5a92aef47d5b91309.jpg_d200.jpg'
url = 'https://www.smzdm.com/p/8734379/'

url_item = url.split('/')
fn = url_item.pop()
fn = url_item.pop()

print(fn)
for i in url_item:
	print(i)
