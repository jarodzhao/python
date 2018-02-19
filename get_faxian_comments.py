import requests
from smzdm.faxian import FaxianItem as Item
from bs4 import BeautifulSoup as bsp

class Comment:
	def __init__(self, floor, user_, user_level, user_url, time_, quote, comment_, platform, item_url):
		self.floor = floor
		self.user_ = user_
		self.user_level = user_level
		self.user_url = user_url
		self.time_ = time_
		self.quote = quote
		self.comment_ = comment_
		self.platform = platform
		self.item_url = item_url

'''
抓取 HTML 源方法
'''
def get_html():
	tag = ("section", "comments")

	url = 'https://www.smzdm.com/p/8736559/'
	headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
	r = requests.get(url, headers=headers)
	page_html = bsp(r.text, 'html.parser')

	html = page_html.find(tag[0], id=tag[1])

	return (url, html)

def fetch_data(html):
	ul_html = html[1].find('ul', class_='comment_listBox')

	li_html = ul_html.findAll("li", class_='comment_list')

	# 开始循环抓取所有评论
	comments = []

	for li in li_html:
		# 评论楼层
		floor_html = li.find('div', class_='comment_avatar')
		floor = floor_html.find('span').text

		# 评论人
		user_html = li.find('div', class_='comment_conBox')
		time_ = user_html.find('div', class_='time').text	#发表时间，需要用当前时间去计算出来
		user_ = user_html.find('a', class_='a_underline').find('span').text
		user_url = user_html.find('a', class_='a_underline')['href']
		user_level = user_html.find('div', class_='rank')['title']

		# 引用评论，保存楼层编号
		quote_html = li.find('div', class_='blockquote_wrap')
		quote = []
		if quote_html != None:
			quote_s_html = quote_html.findAll('blockquote', class_='comment_blockquote') 
			for i in quote_s_html:
				quote.append(i.find('div', class_='comment_floor').text)	# floor 引用的楼层

		# 评论内容
		content_html = li.find('div', class_='comment_conBox')

		# 引用评论标签
		blockquote_html = content_html.find('div', class_='blockquote_wrap')

		if blockquote_html == None:
			content = content_html.find('div', class_='comment_conWrap').find('span').text
		else:
			# 有引用评论
			content = blockquote_html.next_sibling.next_sibling.find('span').text

		# 终端类型
		platform_html = li.find('div', class_='comment_conWrap').find('div', class_='comment_action')
		if platform_html.find('span', class_='come_from') != None:
			platform = platform_html.find('span', class_='come_from').find('a').text
		else:
			platform = 'PC 端浏览器'

		item_url = html[0]

		# 生成评论列表
		comment = Comment(floor, user_, user_level, user_url, time_, quote, content, platform, item_url)
		comments.append(comment)

	return comments

if __name__ == '__main__':
	comments = fetch_data(get_html())
	for comment in comments:
		print(comment.floor)
		print(comment.user_)
		print(comment.user_level)
		print(comment.user_url)
		print(comment.time_)
		print(comment.quote)
		print(comment.comment_)
		print(comment.platform)
		print(comment.item_url)
		print('--------------------------------------------')

