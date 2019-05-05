import requests
import weboptions
import dataclean
import re
import json
import time
import webcrawlerlogin
from collections import defaultdict

def getData(url, name, password):
    if not webcrawlerlogin.LoginAndSaveCookie(name, password):
        print('用户名或密码错误，请检查')
        return '','',False
    mainPage = 'https://www.icourse163.org/member/login.htm#/webLoginIndex'

    #数据初始化
    pid = url.split('=')[-1]
    httpsessionID = ""
    datadict = defaultdict(list)
    cookies = {}

    #获取cookies和httpsessionID,httpsessionID为cookies['NTESSTUDYSI"]
    cookies, httpsessionID = weboptions.getCookiesAndSessionID()

    print('================================')
    print('开始抓取问题.....')
    #获取问题
    questionlist = requests.post(weboptions.getDomainDwrUrl('question'), data=weboptions.getQuestionPayloads(httpsessionID, pid),
                                 headers=weboptions.getHeaders(), cookies=cookies, timeout=None)
    question, content = dataclean.getQuestions(questionlist.text)
    print('问题：' + question)
    print('详情: ' + content)
    #获取页数
    pagehtml = requests.post(weboptions.getDomainDwrUrl('answers'), data=weboptions.getPayloads(httpsessionID, pid, 1),
                         headers=weboptions.getHeaders(), cookies=cookies, timeout=None)
    pagenumber=int(re.search(r'totalPageCount:(\d+)',pagehtml.text).group(1))
    print('页数: ' + str(pagenumber))
    time.sleep(1)
    print('================================')
    print('开始抓取学生答案.....')
    for i in range (pagenumber):
        try:
            print('    ********************************')
            print('    正在解析第 %d 页，共 %d 页' % (i + 1, pagenumber))
            html = requests.post(weboptions.getDomainDwrUrl('answers'), data=weboptions.getPayloads(httpsessionID, pid, i+1),
                                 headers=weboptions.getHeaders(), cookies=cookies, timeout=None)
            datadict = dict(dataclean.getCleandict(html.text), **datadict)#合并字典，以后面字典为基准，如新字典中key值已在原字典中，不更新
        except:
            print('    断开连接，正在尝试重新登录......')
            i -= 1
            webcrawlerlogin.LoginAndSaveCookie(name, password)
            listCookies = weboptions.getCookies()
            cookies.clear()
            cookies, httpsessionID = weboptions.getCookiesAndSessionID()
        finally:
            time.sleep(2)
    print('===================================')
    print('抓取完成，共抓取到 %d 位学生的答案' % len(datadict))
    print('将答案保存至 "./cachefiles/answers.json"')
    with open(weboptions.getCachePath('answers'), 'w') as file:
        json.dump(datadict, file)
    print('保存成功！')
    time.sleep(1)
    return question, content, True

if __name__ == '__main__':
    #webcrawlerlogin.LoginAndSaveCookie()
    url = 'https://www.icourse163.org/spoc/learn/COMPUTER-1002604037?tid=1002792051&_trace_c_p_k2_=155222ed06ef4bdebc23526990270e78#/learn/forumdetail?pid=1005145548'
    name  = '18324605567@163.com'
    password = 'yf691111'
    a,b,c =getData(url, name, password)
    if c:
        print('true')
    else:
        print('false')