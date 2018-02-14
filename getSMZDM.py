import requests
from bs4 import BeautifulSoup as bsp
import re

site = 'https://faxian.smzdm.com/'
lineNo = 1


class Item:

    def __init__(self, name, url, img, price):
        self.name = name
        self.url = url
        self.img = img
        self.price = link

    def __str__(self):
        return '%s,\t%s,\t%s' % (self.img, self.name, self.price)

    __repr__ = __str__

def filterItem(url):
    resultList = []
    soup = bsp(requests.get(url)

def getPageResource(url):
    resultList = filterItem(url)


#主程序运行#
if __name__ == '__main__':
    for index in range(5):
        index += 1
        url = site + '/p' + str(index)
        getPageResource(url)

