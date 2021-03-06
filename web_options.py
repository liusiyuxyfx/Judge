import json
import pickle
import random

from selenium.webdriver.chrome.options import Options

def getDomainDwrUrl(str):
    if str == 'question':
        return 'https://www.icourse163.org/dwr/call/plaincall/PostBean.getPostDetailById.dwr'
    elif str == 'answers':
        return 'https://www.icourse163.org/dwr/call/plaincall/PostBean.getPaginationReplys.dwr'

def Chrome_headless():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    return chrome_options

def getCachePath(str):
    if str == 'answers':
        return './cachefiles/answers.json'
    elif str == 'cookies':
        return './cachefiles/moocCookies.pkl'


def getCookiesAndSessionID():
    cookies = {}
    httpsessionID = ''
    listCookies = pickle.load(open(getCachePath('cookies'), "rb"))
    for cookie in listCookies:
        cookies[cookie['name']] = cookie['value']
        if cookie['name'] == "NTESSTUDYSI":
            httpsessionID = cookie['value']
    return cookies, httpsessionID

def getHeaders():
    header= {
        #'cookie': getCookies(),
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type':'text/plain',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        #'referer':url
    }
    return header

def getPayloads(httpsessionid, pid, page):
    payloads = {
        'callCount': 1,
        'scriptSessionId':'${scriptSessionId}' + str(random.randint(0, 200)),
        'httpSessionId':httpsessionid,
        'c0-scriptName':'PostBean',
        'c0-methodName':'getPaginationReplys',
        'c0-id': 0,
        'c0-param0': pid,
        'c0-param1': 2,
        'c0-param2': page,
        'batchId': random.randint(1000000000000, 20000000000000)
    }
    return payloads
def getQuestionPayloads(httpsessionid, pid):
    payloads ={
        'callCount': 1,
        'scriptSessionId': '${scriptSessionId}' + str(random.randint(0, 200)),
        'httpSessionId': httpsessionid,
        'c0-scriptName': 'PostBean',
        'c0-methodName': 'getPostDetailById',
        'c0-id': 0,
        'c0-param0': pid,
        'batchId': random.randint(1000000000000, 20000000000000)
    }
    return payloads