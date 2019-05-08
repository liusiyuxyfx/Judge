import re
from collections import defaultdict

def getQuestions(str):
    pat = re.compile('<[^>]*>')
    segstr = re.sub(pat, '', str)
    segstr = re.search(r'{activeFlag.*}', segstr).group()
    question = ''.join(re.search(r'title:"(.*?)"', segstr).group(1))
    content = ''.join(re.search(r'content:"(.*?)"', segstr).group(1))
    return question.encode('utf-8').decode('unicode_escape').encode('gbk', 'ignore').decode(
            'gbk', 'ignore'), content.encode('utf-8').decode('unicode_escape').encode('gbk', 'ignore').decode(
            'gbk', 'ignore')

def getCleandict(str):
    dict=defaultdict(list)
    str = re.sub(r'<.*?>','',str)
    str.replace(u'\xa0', u' ')
    allcontent = re.findall(re.compile(r'(s\d+).content="(.*)";'),str)
    #print(allcontent)
    for cp in allcontent:
        next = re.search(re.compile(cp[0]+'.replyer=(s\d+)'),str).group(1)
        nickname = re.search(re.compile(next+'.nickName=(.*?);'),str).group(1)
        try:
            temp = re.sub(r'edu_dup_accId_his_','', nickname)
            nickname = temp
        except:
            pass
        realname = re.search(re.compile(next+'.realName=(.*?);'),str).group(1)
        nickname = re.sub(r'"*', '', nickname).encode('utf-8').decode('unicode_escape').encode('gbk', 'ignore').decode(
            'gbk', 'ignore')
        realname = re.sub(r'"*', '', realname).encode('utf-8').decode('unicode_escape').encode('gbk', 'ignore').decode(
            'gbk', 'ignore')
        if realname == '' or realname == 'null':
            if re.search(r'hrbcu[0-9]*(.*)', realname) != None:
                realname = re.search(r'hrbcu[0-9]*(.*)', realname).group(1)
            elif re.search(r'{HIT|hit}[0-9]*(.*)', realname) != None:
                realname = re.search(r'{HIT|hit}[0-9]*(.*)', realname).group(1)
            else:
                realname = '未填写'
        #print(nickname, realname)
        if nickname not in dict.keys():
            dict[nickname].append(re.sub(r'&nbsp;',' ',cp[1].encode('utf-8').decode('unicode_escape').encode('gbk', 'ignore').decode('gbk', 'ignore')))
            dict[nickname].append(realname)
    return dict
