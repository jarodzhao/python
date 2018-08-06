import requests
from bs4 import BeautifulSoup as soup

url = 'http://www.sohu.com'
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}

r = requests.get(url, headers)
html = soup(r.text)

print(html.find("title").text)


