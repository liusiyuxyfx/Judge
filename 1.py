import re
import random
import requests
import matplotlib
# httpsessionid = ''
# pid = ''
# header= {
#         'content-type':'text/plain',
#         'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
#  }
# payloads ={
#     'callCount': 1,
#     'scriptSessionId': '${scriptSessionId}190',
#     'httpSessionId': httpsessionid,
#     'c0-scriptName': 'PostBean',
#     'c0-methodName': 'getPostDetailById',
#     'c0-id': 0,
#     'c0-param0': pid,
#     'batchId': 1557025646888
# }
# questionlist = requests.post('https://www.icourse163.org/dwr/call/plaincall/PostBean.getPostDetailById.dwr',
#                              data=payloads, headers=header, cookies=cookies, timeout=None)
#
# nohtml = re.compile('<[^>]*>')
# str = re.sub(nohtml, '', str)
# str = re.search(r'{activeFlag.*}', str).group()
# content= ''.join(re.search(r'content:"(.*?)"', str).group(1))
# question = ''.join(re.search(r'title:"(.*?)"', str).group(1))
# print("问题：".join(question))
# print("内容: ".join(content))
# #print(demjson.decode(segstr))
# #print(re.findall(r'content:".*",.??', segstr))
# #print(str.replace(r'/<[^>]+>/g',""))
#
# dict = {'a':[1,20],'b':[2,30]}
# print(list(dict.values()))
# print(list(value[0] for value in dict.values()))
colors = []
# for name, hex in plt.colors.cnames.items():
#
#     colors.append(name)
#
# print(colors)
# xlist = ['0~40', '40~50', '50~60', '60~70', '70~80', '80_90', '90~100']
# colors=['orangered','darksalmon','pink','blanchedalmond','paleturquoise','aquamarine','springgreen']
import re

str = 'hrbcu1233我是你爸爸'
str = re.search(r'hrbcu[0-9]*(.*)', str).group(1)
print(str)