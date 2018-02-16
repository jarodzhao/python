import requests
from bs4 import BeautifulSoup as bsp

url = 'https://www.zhihu.com/people/jarodzhao'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

req = requests.get(url, headers=headers)
json_data = bsp(req.text, 'html.parser')

jarod_data = json_data.find('div', id='data')

print(jarod_data['data-state'])


