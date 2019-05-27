import requests
import web_options
import nlp_dataclean
import re
import json
import time
import web_login
from collections import defaultdict

def getData(url, name, password, timeinterval = 2):
    try:
        web_login.LoginAndSaveCookie(name, password)
    except Exception as e:
        print (e)
        print('用户名或密码错误，请检查')

    if timeinterval.isdigit():
        timeinterval = int(timeinterval)
        if timeinterval < 0 or timeinterval > 5:
            timeinterval = 2
            print('间隔时间不在范围内，采用默认2秒!')
    elif timeinterval == '' or timeinterval == None:
        timeinterval = 2
    else:
        raise Exception('间隔时间: 请输入数字!')

    mainPage = 'https://www.icourse163.org/member/login.htm#/webLoginIndex'
    #数据初始化
    pid = url = re.search(r'pid=([0-9]*)',  url).group(1)
    datadict = defaultdict(list)

    #获取cookies和httpsessionID,httpsessionID为cookies['NTESSTUDYSI"]
    cookies, httpsessionID = web_options.getCookiesAndSessionID()

    print('================================')
    print('开始抓取问题.....')
    #获取问题
    questionlist = requests.post(web_options.getDomainDwrUrl('question'), data=web_options.getQuestionPayloads(httpsessionID, pid),
                                 headers=web_options.getHeaders(), cookies=cookies, timeout=None)
    question, content = nlp_dataclean.getQuestions(questionlist.text)
    content = re.sub(r'&nbsp;',' ',content)
    print('问题：' + question)
    print('详情: ' + content)
    #获取页数
    try:
        pagehtml = requests.post(web_options.getDomainDwrUrl('answers'), data=web_options.getPayloads(httpsessionID, pid, 1),
                                 headers=web_options.getHeaders(), cookies=cookies, timeout=None)
        pagenumber=int(re.search(r'totalPageCount:(\d+)',pagehtml.text).group(1))
    except Exception as e:
        raise e
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
        except Exception as e:
            print(e)
            print('    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            print('    断开连接，正在尝试重新登录......')
            i -= 1
            web_login.LoginAndSaveCookie(name, password)
            cookies.clear()
            cookies, httpsessionID = web_options.getCookiesAndSessionID()
        finally:
            if timeinterval == 0:
                pass
            else:
                time.sleep(timeinterval)
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
#     standardAnswer = """
#      电脑要解决的问题有许多，提高cpu性能提高计算机对数据的处理能力，互联网 的覆盖面问题等。计算思维是学习计算机语言的基础，通过学习计算思维，才能真正掌握计算机语言，学会用计算机语言去解决一系列的问题，况且计算思维不单单只为编程服务，它
# 还能帮助我们解决生活中的许许多多的问题。计算思维是学习计算机语言的基础，通过学习计算思维，才能真正掌握计算机语言，学会用计算机语言去解决一系列的
# 问题，况且计算思维不单单只为编程服务，它还能帮助我们解决生活中的许许多多的问题。"""
#     # question, content, islogin = getData(url, name, password, 0)
#     scoredict, wordcloudblob, numberlist, averagescore = nlp_AnswerProcessing.calculate(standardAnswer)
#     print('  + 绘制条形图.....')
#     numberlistpath = data_showtime.getNumberCount(numberlist, averagescore)
#     print('  + 绘制完成!')
#     data_databaseact.autocreateQuestion('【讨论1-1】计算思维对你所学习、从事的学科、专业有价值吗？', """你认为计算思维对你所学习、从事的学科、专业有价值吗？有哪些价值？能否与大家讨论、分享一下你的见解和观点。提示：你所学习和从事的专业是什么？什么是计算思维和有哪些计算思维？你的专业怎样或可能怎样利用计算思维？，大家可以畅想一番！""", wordcloudblob, numberlistpath, scoredict)
#     print('================================')
#     print('分析完成，请点击下一步')