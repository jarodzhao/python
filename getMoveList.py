import requests
from bs4 import BeautifulSoup as bsp
import re

site = 'http://www.ygdy8.net'
lineNo = 1


class Movie:

    def __init__(self, name, url, score, link):
        self.name = name
        self.url = url
        self.score = score
        self.link = link

    def __str__(self):
        return '%s,\t%s分,\t%s' % (self.name, self.score, self.link)

    __repr__ = __str__


def getSoup(url):
    r = requests.get(url)
    r.encoding = 'gb18030'
    print(r.text)
    return bsp(r.text, "html.parser")


#处理传入的 url 地址
def filterMovie(url):
    resultList = []
    soup = getSoup(url)
    tables = soup.find_all('table', class_='tbspan')
    for table in tables:
        nameA = table.find('a', text=re.compile("《"))
        td = table.find('td', text=re.compile("IMD"))
        if td is not None:
            scoreStr = re.findall(r"评分 (.+?)/10", td.text)
            if(len(scoreStr) > 0):
                try:
                    score = float(scoreStr[0])
                    if(score > 8):
                        name = nameA.text
                        url = site + nameA['href']
                        # print('url:', url)
                        # print('title:', name)
                        # print('score:', score)
                        downloadLink = getDownloadLink(url)
                        movie = Movie(name, url, score, downloadLink)
                        resultList.append(movie)
                except:
                    print('error !!')
    return resultList


def getDownloadLink(url):
    soup = getSoup(url)
    downloadTd = soup.find('td', attrs={"style": "WORD-WRAP: break-word"})
    downloadA = downloadTd.find('a')
    return downloadA['href']


def saveInfo(movieList):
    fileObj = open('moveList.txt', 'a', encoding='UTF-8')
    for movie in movieList:
        movie_str = str(movie)
        print('movie info:', movie_str)
        global lineNo
        fileObj.write('(' + str(lineNo) + ') ' + movie_str)
        fileObj.write('\n')
        fileObj.write('\n')
        # fileObj.write(str(lineNo) + ', ')
        # fileObj.write('爬虫电影测试\n')
        lineNo += 1
        if lineNo == 5:
            exit()
    fileObj.close()

#传入url地址，然后分析
def getPageResource(url):
    resultList = filterMovie(url)
    if len(resultList) > 0:
        saveInfo(resultList)

#主程序运行#
if __name__ == '__main__':
    for index in range(1):
        index += 1
        url = 'http://www.ygdy8.net/html/gndy/oumei/list_7_' + \
            str(index) + '.html'
        getPageResource(url)