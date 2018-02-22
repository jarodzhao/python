from bs4 import BeautifulSoup as bsp

fo = open('li.html', 'r', encoding='UTF-8')
all = fo.read()

html = bsp(all, 'html.parser')
li = html.find_all('li', class_='comment_list')

for comm in li:
	st = comm.find_all('span', itemprop="description")
	print(st[len(st)-1].text)
	print()


