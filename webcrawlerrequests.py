import requests
import weboptions
import dataclean
import time
from collections import defaultdict
from selenium import webdriver
from bs4 import BeautifulSoup
testurl = 'https://www.icourse163.org/spoc/learn/COMPUTER-1002235015?tid=1002353031&_trace_c_p_k2_=7b969657396a44d8941e666e083563d1#/learn/forumdetail?pid=1004204387'

def getPageNumber(url):
    # 注入cookie
    driver = webdriver.Chrome(chrome_options=weboptions.Chrome_headless())
    driver.get('https://www.icourse163.org/member/login.htm#/webLoginIndex')
    time.sleep(20)
    print("删除cookies")
    try:
        driver.delete_all_cookies()
    except:
        print("失败")
    print("删除成功")
    listCookies = weboptions.getCookies()
    print('获取列表成功')
    for item in listCookies:
        driver.add_cookie(item)
    # 首次获取页面
    print("注入cookies成功")
    driver.get(url)
    print('正在访问页面')
    time.sleep(2)
    print('正在解析')
    pages = driver.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div[2]/div/div[4]/div/div[1]/div[2]/div[1]/*')
    cnt = -2
    pagenumber = ''
    print("页面加载完成，正在读取页数")
    while cnt > -10:
        pagenumber = pages[cnt].get_attribute("innerText")
        if pagenumber == '':
            cnt-=1
        else:
            break

    print (pagenumber,type(pagenumber))
    driver.close()
    return int(pagenumber)

def getData(url):
    datadict = defaultdict(list)
    mainPage = 'https://www.icourse163.org/member/login.htm#/webLoginIndex'
    domainurl = 'https://www.icourse163.org/dwr/call/plaincall/PostBean.getPaginationReplys.dwr'

    pid = url.split('=')[-1]
    pagenumber = getPageNumber(url)
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
    for i in range (pagenumber):
        html = requests.post(domainurl, data=weboptions.getPrivate(httpsessionID, pid, i+1), headers=weboptions.getHeaders(url), cookies=cookies, timeout=None)
        print('================================')
        print('正在解析第 %d 页，共 %d 页'% (i+1, pagenumber))
        datadict = dict(dataclean.getCleandict(html.text), **datadict)
    print(datadict)
    return datadict

getData('https://www.icourse163.org/spoc/learn/HRBCU-362005?tid=419007&_trace_c_p_k2_=bcca62dee7a340d7b4cecbb9237eb475#/learn/forumdetail?pid=996042')