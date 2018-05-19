import urllib.request
import time
import MySelfSql

from lxml import html


def getContent(page):
    print(page)
    url = "http://cq.meituan.com/xiuxianyule/c52/pn%d" % page

    # 伪装浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Host': 'cq.meituan.com',
        'GET': '/xiuxianyule/c52/pn%d/ HTTP/1.1' % (page)
    }
    req = urllib.request.Request(url=url, headers=headers)
    ret = urllib.request.urlopen(req)
    document = html.fromstring(ret.read())
    title = document.xpath('//*[@class="list-item-desc-top"]/a/text()')
    print(title)
    point = document.xpath('//*[@class="list-item-desc-top"]/div[1]/span[1]/text()')
    comment_num = document.xpath('//*[@class="list-item-desc-top"]/div[1]/span[2]/text()')
    site = document.xpath('//*[@class="list-item-desc-top"]/div[2]/span/text()')
    list = []
    for p in range(len(title)):
        if p * 2 < len(point):
            text = title[p] + "|" + point[p * 2] + "|" + comment_num[p * 2] + "|" + site[p * 4 + 2] + "|" + site[
                p * 4 + 3]
            print(text)
            list.append(text)
    MySelfSql.insertData(list)


def getPageFirst():
    url = "http://cq.meituan.com/xiuxianyule/c52/"

    # 伪装浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Host': 'cq.meituan.com',
        'GET': '/xiuxianyule/c52/ HTTP/1.1',
        # 'Connection': 'keep - alive',
        # 'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8'
    }
    req = urllib.request.Request(url=url, headers=headers)
    ret = urllib.request.urlopen(req)
    # file = open("jy.html", "wb")
    # file.write(ret.read())
    # file.close()
    document = html.fromstring(ret.read())
    return document.xpath('//*[@id="react"]/div/div/div[2]/div[1]/nav/ul/li[6]/a/text()')


def getContentFromFile():
    text = open("jy.html", "r", encoding="UTF-8").read()
    document = html.fromstring(text)
    title = document.xpath('//*[@class="list-item-desc-top"]/a/text()')
    point = document.xpath('//*[@class="list-item-desc-top"]/div[1]/span[1]/text()')
    comment_num = document.xpath('//*[@class="list-item-desc-top"]/div[1]/span[2]/text()')
    site = document.xpath('//*[@class="list-item-desc-top"]/div[2]/span/text()')
    listTest = []
    for p in range(len(title)):
        if p * 2 < len(point):
            text = title[p] + "|" + point[p * 2] + "|" + comment_num[p * 2] + "|" + site[p * 4 + 2] + "|" + site[
                p * 4 + 3]
            listTest.append(text)
    MySelfSql.insertData(listTest)


# getContentFromFile()
listPage = getPageFirst()
if len(listPage) > 0:
    pageCount = int(listPage[0])
    print(pageCount)
    if pageCount > 1:
        curPage = 17
        while curPage <= pageCount:
            time.sleep(10 + curPage)
            getContent(curPage)
            curPage = curPage + 1
