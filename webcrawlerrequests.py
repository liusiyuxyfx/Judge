
import json
import string
import sys
import requests
from bs4 import BeautifulSoup
import weboptions
from selenium import webdriver
from collections import defaultdict
import time
from lxml import etree
mainPage = 'https://www.icourse163.org/member/login.htm#/webLoginIndex'
url = 'https://www.icourse163.org/spoc/learn/COMPUTER-1002604037?tid=1002792051&_trace_c_p_k2_=7fbdf498494f4412bd9f3cc97483253d#/learn/forumdetail?pid=1005195052'
domainurl = 'https://www.icourse163.org/dwr/call/plaincall/PostBean.getPaginationReplys.dwr'

pid = url.split('=')[-1]
#初始化数据
listCookies = weboptions.getCookies()
answerdict = defaultdict(list)
httpsessionID = ""
s = requests.Session()
for cookie in listCookies:
    s.cookies.set(cookie['name'], cookie['value'])
    if cookie['name'] == "NTESSTUDYSI" :
        httpsessionID = cookie['value']
    #print(cookie['name'], cookie['value'])

#print(httpsessionID)
#print(weboptions.getHeaders())
html = requests.get(domainurl, data=weboptions.getPrivate(httpsessionID, pid, 10), headers=weboptions.getHeaders(url))
print(html.text)


"""
#注入cookie
driver = webdriver.Chrome()
driver.get('https://www.icourse163.org/member/login.htm#/webLoginIndex')
driver.delete_all_cookies()
for item in listCookies: driver.add_cookie(item)
"""

"""
#首次获取页面
driver.get(url)
time.sleep(2)
divs = driver.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div[2]/div/div[4]/div/div[1]/div[1]/*')
pages = driver.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div[2]/div/div[4]/div/div[1]/div[2]/div[1]/*')
print(pages[-2].get_attribute("innerText"))
#print(divs)
for div in divs:
    answer = ""
    student = ""
    #print(div.get_attribute("innerHTML"))
    answercontent = div.find_element_by_xpath('.//div[contains(@class, "f-richEditorText j-content")]')
    answer = answercontent.get_attribute("innerText")
    usercontent = div.find_element_by_xpath('.//span[@class="userInfo j-userInfo"]/a')
    student = usercontent.get_attribute("title")

    if answer != None and student != None:
        answerdict[student].append(answer)

print(answerdict)

cnt = 1;
pages[-1].click()
"""
