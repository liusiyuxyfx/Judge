import requests
import web_options
import nlp_dataclean
import re
import json
import time
import web_login
from collections import defaultdict

def getData(url, name, password):
    if not web_login.LoginAndSaveCookie(name, password):
        print('用户名或密码错误，请检查')
        return '','',False
    mainPage = 'https://www.icourse163.org/member/login.htm#/webLoginIndex'

    #数据初始化
    pid = url.split('=')[-1]
    httpsessionID = ""
    datadict = defaultdict(list)
    cookies = {}

    #获取cookies和httpsessionID,httpsessionID为cookies['NTESSTUDYSI"]
    cookies, httpsessionID = web_options.getCookiesAndSessionID()

    print('================================')
    print('开始抓取问题.....')
    #获取问题
    questionlist = requests.post(web_options.getDomainDwrUrl('question'), data=web_options.getQuestionPayloads(httpsessionID, pid),
                                 headers=web_options.getHeaders(), cookies=cookies, timeout=None)
    question, content = nlp_dataclean.getQuestions(questionlist.text)
    print('问题：' + question)
    print('详情: ' + content)
    #获取页数
    pagehtml = requests.post(web_options.getDomainDwrUrl('answers'), data=web_options.getPayloads(httpsessionID, pid, 1),
                             headers=web_options.getHeaders(), cookies=cookies, timeout=None)
    pagenumber=int(re.search(r'totalPageCount:(\d+)',pagehtml.text).group(1))
    print('页数: ' + str(pagenumber))
    time.sleep(1)
    print('================================')
    print('开始抓取学生答案.....')
    for i in range (pagenumber):
        try:
            print('    ********************************')
            print('    正在解析第 %d 页，共 %d 页' % (i + 1, pagenumber))
            html = requests.post(web_options.getDomainDwrUrl('answers'), data=web_options.getPayloads(httpsessionID, pid, i + 1),
                                 headers=web_options.getHeaders(), cookies=cookies, timeout=None)
            datadict = dict(nlp_dataclean.getCleandict(html.text), **datadict)#合并字典，以后面字典为基准，如新字典中key值已在原字典中，不更新
        except:
            print('    断开连接，正在尝试重新登录......')
            i -= 1
            web_login.LoginAndSaveCookie(name, password)
            listCookies = web_options.getCookies()
            cookies.clear()
            cookies, httpsessionID = web_options.getCookiesAndSessionID()
        finally:
            time.sleep(2)
    print('===================================')
    print('抓取完成，共抓取到 %d 位学生的答案' % len(datadict))
    print('将答案保存至 "./cachefiles/answers.json"')
    with open(web_options.getCachePath('answers'), 'w') as file:
        json.dump(datadict, file)
    print('保存成功！')
    time.sleep(1)
    return question, content, True

if __name__ == '__main__':
    import nlp_AnswerProcessing
    import nlp_dataclean
    import data_databaseact
    import data_showtime

    name = '18324605567@163.com'
    password = 'yf691111'
    url = 'https://www.icourse163.org/spoc/learn/COMPUTER-1002604037?tid=1002792051&_trace_c_p_k2_=8b2564ba9a21437fa6e40053c1f9ef35#/learn/forumdetail?pid=1005050559'
    standardAnswer = "顺序查找 假定有一个元素顺序情况不明的数组。这种情况如果我们要搜索一个元素就要遍历整个数组，才能知道这个元素是否在数组中。这种方法要检查整个数组，核对每个元素。"
    question, content, islogin = getData(url, name, password)
    if islogin:
        print(question, content)
        scoredict, wordcloudblob, numberlist,averagescore = nlp_AnswerProcessing.calculate(standardAnswer)
        global global_questionid
        # sleep(3)
        print("--------------")
        print('断点')
        print(numberlist, averagescore)
        numberlistblob = data_showtime.getNumberCount(numberlist, averagescore)
        print (question, content)
        print (scoredict, wordcloudblob, numberlistblob)
        global_questionid = data_databaseact.autocreateQuestion(question, content, wordcloudblob, numberlistblob,
                                                                scoredict)
        print('================================')
        print('请点击 *下一步* 按钮')