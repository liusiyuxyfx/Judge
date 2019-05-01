#参考
#https://blog.csdn.net/weixin_40444270/article/details/80593058
#https://blog.csdn.net/KaryKwok/article/details/80943843
import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

with open('qqhomepage.json','r',encoding='utf-8') as f:
    listCookies=json.loads(f.read())
#cookie = [item["name"] + "=" + item["value"] for item in listCookies]
#cookiestr = '; '.join(item for item in cookie)
print(listCookies)
#print(cookiestr)
headers = {
    'Connection':'keep-alive',
    'Cache-Control':'max-age=0',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer':'https://www.tianyancha.com/',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9'
}


url = 'http://www.icourse163.org/learn/preview/HIT-7001?tid=1001795014#/learn/forumdetail?pid=1002527389'

driver = webdriver.Chrome()
driver.get("https://www.icourse163.org/")
driver.delete_all_cookies()
for item in listCookies: driver.add_cookie(item)
driver.refresh()
driver.get(url)
