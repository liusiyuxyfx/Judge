#参考
#https://blog.csdn.net/weixin_40444270/article/details/80593058
#https://blog.csdn.net/KaryKwok/article/details/80943843
import json
import string
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from lxml import etree


with open('mooccookie.json','r',encoding='utf-8') as f:
    listCookies=json.loads(f.read())

url = 'https://www.icourse163.org/spoc/learn/COMPUTER-1002604037?tid=1002792051&_trace_c_p_k2_=7fbdf498494f4412bd9f3cc97483253d#/learn/forumdetail?pid=1005195052'

#初始化数据
answerdict={}

#注入cookie
driver = webdriver.Chrome()
driver.get('https://www.icourse163.org/member/login.htm#/webLoginIndex')
driver.delete_all_cookies()
for item in listCookies: driver.add_cookie(item)

#首次获取页面
driver.get(url)
time.sleep(1)
divs = driver.find_elements_by_xpath('//*[@id="courseLearn-inner-box"]/div/div[2]/div/div[4]/div/div[1]/div[1]/*')

#print(divs)
for div in divs:
    answer = ""
    student = ""
    #print(div.get_attribute("innerHTML"))
    answercontent = div.find_element_by_xpath('.//div[contains(@class, "f-richEditorText j-content")]')
    answer = print(answercontent.get_attribute("innerText"))
    usercontent = div.find_element_by_xpath('.//span[@class="userInfo j-userInfo"]/a')
    student = usercontent.get_attribute("title")
    if answer != None:
        print ("%s : %s \n" % (student, answer))