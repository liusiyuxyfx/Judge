import requests
import weboptions
import dataclean
import re
import json
import time
import webcrawlerlogin
from collections import defaultdict
from selenium import webdriver
from bs4 import BeautifulSoup
testurl = 'https://www.icourse163.org/spoc/learn/COMPUTER-1002604037?tid=1002792051&_trace_c_p_k2_=257bbfbe544a419287bcd565be2f8ad2#/learn/forumdetail?pid=1005085805'


def getData(url):
    #webcrawlerlogin.LoginAndSaveCookie()

    datadict = defaultdict(list)
    mainPage = 'https://www.icourse163.org/member/login.htm#/webLoginIndex'
    domainurl = 'https://www.icourse163.org/dwr/call/plaincall/PostBean.getPaginationReplys.dwr'

    pid = url.split('=')[-1]
    #初始化数据
    listCookies = weboptions.getCookies()
    answerdict = defaultdict(list)
    httpsessionID = ""

    #获取cookies和httpsessionID,httpsessionID为cookies['NTESSTUDYSI"]
    cookies={}
    for cookie in listCookies:
        cookies[cookie['name']]=cookie['value']
        if cookie['name'] == "NTESSTUDYSI":
            httpsessionID = cookie['value']

    #获取页数
    pagehtml = requests.post(domainurl, data=weboptions.getPrivate(httpsessionID, pid, 1),
                         headers=weboptions.getHeaders(url), cookies=cookies, timeout=None)
    pagenumber=int(re.search(r'totalPageCount:(\d+)',pagehtml.text).group(1))

    for i in range (pagenumber):
        html = requests.post(domainurl, data=weboptions.getPrivate(httpsessionID, pid, i+1), headers=weboptions.getHeaders(url), cookies=cookies, timeout=None)
        print('================================')
        print('正在解析第 %d 页，共 %d 页'% (i+1, pagenumber))
        datadict = dict(dataclean.getCleandict(html.text), **datadict)
        time.sleep(2)
    with open('test.json', 'w') as file:
        json.dump(datadict, file)
    with open('test.json', 'r') as file:
        print(json.load( file))
    file.close()  # 关闭文件
    #print(json.dumps(datadict, ensure_ascii=True))
    print('===================================')
    print('共统计出 %d 位学生答案' % len(datadict))
    return datadict

getData('https://www.icourse163.org/spoc/learn/COMPUTER-1002604037?tid=1002792051&_trace_c_p_k2_=257bbfbe544a419287bcd565be2f8ad2#/learn/forumdetail?pid=1005085805')