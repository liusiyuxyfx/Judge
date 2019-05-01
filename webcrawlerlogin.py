import json
from selenium import webdriver
import time

url = 'https://www.icourse163.org/member/login.htm#/webLoginIndex'
driver = webdriver.Chrome()
driver.get(url)

#自动登录
#遇到的问题
#由于登录界面有三个子界面，要选择爱课程登录界面，但是这三个子界面都放在一个表格中，其class属性只是用来记录最后一次点击的按钮，而其余两个按钮的class属性是一样的
#并且它们都没有自己的 id 值，因此，一开始我通过find_element_by_class_name是无法找到正确的按钮的，因此采用xpath来寻找所需元素
time.sleep(3)
driver.find_element_by_xpath('//ul[@class="ux-tabs-underline_hd"]/li[3]').click()
#driver.switch_to.frame( driver.find_element_by_xpath('//*[@id="j-ursContainer-1"]/iframe'))
driver.find_element_by_xpath('//div[@class="icourse-login-form"]/div[@class="account-field"]/label/input').clear()
driver.find_element_by_xpath('//div[@class="icourse-login-form"]/div[@class="account-field"]/label/input').send_keys("18324605567@163.com")
driver.find_element_by_xpath('//div[@class="icourse-login-form"]/div[@class="password-field"]/label/input').clear()
driver.find_element_by_xpath('//div[@class="icourse-login-form"]/div[@class="password-field"]/label/input').send_keys("yf691111")
driver.find_element_by_xpath('//div[@class="icourse-login-form"]/div[@class="button-field"]/span').click()

time.sleep(3)
cookie = driver.get_cookies()
jsonCookies = json.dumps(cookie)
with open('mooccookie.json', 'w') as f:
    f.write(jsonCookies)

driver.close()