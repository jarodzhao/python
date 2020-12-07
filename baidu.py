import time
import random
import requests
from bs4 import BeautifulSoup as Bsp
from ua_tools import ua_list as ua

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"


def news():
    url="http://news.baidu.com/"
    url="http://news.baidu.com/tech"
    html=get_html(url)
    # print(html)
    print("-"*50)
    items=[]
    resp=html.find_all("a")
    for t in resp:
        href=t.get("href")
        if href and href.count("baijiahao") > 0:
            items.append(t.text)
            print(t.text)
    return items
    
    
def get_html(url):
    headers = {'User-Agent': random.choice(ua)}
    try:
        r = requests.get(url, headers=headers)
        page_html = Bsp(r.text.replace('\xa0', ' '), 'html.parser')
        return page_html
    except Exception as e:
        print(e)
        return '遇到错误，中止 ...'
        

def write_txt(news):
    now=time.strftime("%Y%m%d%H%M%S", time.localtime())
    fp=r"/storage/emulated/0/1/" +now+".txt"
    i=1
    with open(fp,"a+") as f:
        for title in news:
            f.write(str(i)+". "+title+"\n")
            i += 1
    f.close()
    print()
    print("已写入文件:", fp)
    
    

if __name__=="__main__":
    items=news()
    write_txt(items)