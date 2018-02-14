import requests
from bs4 import BeautifulSoup as bsp

class Item:
	def __init__(self, day, title, content, url, readcount, comment):
		self.day = day
		self.title = title
		self.content = content
		self.url = url
		self.readcount = readcount
		self.comment = comment
	def __str__(self):
		return '%s, %s, %s' % (self.title, self.day, self.url)

lineNo = 1

for i in range(7):
	i += 1
	url = 'http://www.cnblogs.com/jarod99/default.html?page=' + str(i)
	r = requests.get(url)
	r.encoding = 'utf8'
	# print(r.text)
	soup = bsp(r.text, 'html.parser')

	html = soup.findAll('div', class_='day')

	for day in html:

		item = Item

		#处理标题和url
		title_div = day.find('div', class_='postTitle')
		t = title_div.find('a')
		item.title = t.text.strip()
		item.url = t['href']

		#处理日期
		day_div = day.find('div', class_='dayTitle')
		item.day = day_div.text.strip()

		lineNo += 1

		print('%s %s %s %s' % (lineNo, item.title, item.url, item.day))
		# print(day)

	print('****************************** 第 %s 页 *************************************' % (i))
