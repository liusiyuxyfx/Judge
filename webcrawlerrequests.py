import requests
import weboptions
import dataclean
import re
import json
import time
import webcrawlerlogin
from collections import defaultdict

def getData(url):
    webcrawlerlogin.LoginAndSaveCookie()
    mainPage = 'https://www.icourse163.org/member/login.htm#/webLoginIndex'
    domainurl = 'https://www.icourse163.org/dwr/call/plaincall/PostBean.getPaginationReplys.dwr'

    #数据初始化
    pid = url.split('=')[-1]
    httpsessionID = ""
    datadict = defaultdict(list)
    cookies = {}

    #获取cookies和httpsessionID,httpsessionID为cookies['NTESSTUDYSI"]
    cookies, httpsessionID = weboptions.getCookiesAndSessionID()

    #获取页数
    pagehtml = requests.post(domainurl, data=weboptions.getPayloads(httpsessionID, pid, 1),
                         headers=weboptions.getHeaders(url), cookies=cookies, timeout=None)
    pagenumber=int(re.search(r'totalPageCount:(\d+)',pagehtml.text).group(1))

    for i in range (pagenumber):
        try:
            html = requests.post(domainurl, data=weboptions.getPayloads(httpsessionID, pid, i+1),
                                 headers=weboptions.getHeaders(url), cookies=cookies, timeout=None)
            print('================================')
            print('正在解析第 %d 页，共 %d 页'% (i+1, pagenumber))
            datadict = dict(dataclean.getCleandict(html.text), **datadict)#合并字典，以后面字典为基准，如新字典中key值已在原字典中，不更新
        except:
            i -= 1
            webcrawlerlogin.LoginAndSaveCookie()
            listCookies = weboptions.getCookies()
            cookies.clear()
            cookies, httpsessionID = weboptions.getCookiesAndSessionID()
        finally:
            time.sleep(2)
    print('================================')
    with open(weboptions.getCachePath('answers'), 'w') as file:
        json.dump(datadict, file)
    print('文件保存成功 answers.json')
    #print(json.dumps(datadict, ensure_ascii=True))
    print('===================================')
    print('共统计出 %d 位学生答案' % len(datadict))

if __name__ == '__main__':
    #webcrawlerlogin.LoginAndSaveCookie()
    getData('https://www.icourse163.org/spoc/learn/COMPUTER-1002604037?tid=1002792051&_trace_c_p_k2_=257bbfbe544a419287bcd565be2f8ad2#/learn/forumdetail?pid=1005085805')
