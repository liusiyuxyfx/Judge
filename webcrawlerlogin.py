import json
import time
import weboptions
import pickle
from selenium import webdriver


def LoginAndSaveCookie(names = "18324605567@163.com", passwords = "yf691111"):
    print('================================')
    print("开始登陆MOOC平台...........")
    url = 'https://www.icourse163.org/member/login.htm#/webLoginIndex'
    print('  + 尝试创建无界面浏览器')
    driver=webdriver.Chrome(chrome_options=weboptions.Chrome_headless())
    print('  + 创建成功，打开登录页面')
    driver.get(url)
    #自动登录
    #遇到的问题
    #由于登录界面有三个子界面，要选择爱课程登录界面，但是这三个子界面都放在一个表格中，其class属性只是用来记录最后一次点击的按钮，而其余两个按钮的class属性是一样的
    #并且它们都没有自己的 id 值，因此，一开始我通过find_element_by_class_name是无法找到正确的按钮的，因此采用xpath来寻找所需元素
    print('  + 正在切换至爱课程登录')
    time.sleep(3)

    driver.find_element_by_xpath('//ul[@class="ux-tabs-underline_hd"]/li[3]').click()
    #driver.switch_to.frame( driver.find_element_by_xpath('//*[@id="j-ursContainer-1"]/iframe'))
    print('  + 正在输入用户名')
    driver.find_element_by_xpath('//div[@class="icourse-login-form"]/div[@class="account-field"]/label/input').clear()
    driver.find_element_by_xpath('//div[@class="icourse-login-form"]/div[@class="account-field"]/label/input').send_keys(names)
    print('  + 正在输入密码')
    driver.find_element_by_xpath('//div[@class="icourse-login-form"]/div[@class="password-field"]/label/input').clear()
    driver.find_element_by_xpath('//div[@class="icourse-login-form"]/div[@class="password-field"]/label/input').send_keys(passwords)
    driver.find_element_by_xpath('//div[@class="icourse-login-form"]/div[@class="button-field"]/span').click()
    print('  + 正在登录，请稍后........')
    time.sleep(3)

    try:
        length = driver.find_element_by_class_name("exit")
        if length != 0:
            print('  + 登陆成功！')
            pickle.dump(driver.get_cookies(), open(weboptions.getCachePath('cookies'), "wb"))
            driver.close()
            return True
    except:
        driver.close()
        print("  + 登录失败！")
        return False

if __name__ == '__main__':
    LoginAndSaveCookie()