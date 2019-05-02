import re
from collections import defaultdict

def getCleandict(str):
    dict=defaultdict(list)
    str = re.sub(r'<.*?>','',str)
    str.replace(u'\xa0', u' ')
    allcontent = re.findall(re.compile(r'(s\d+).content="(.*)";'),str)
    #print(allcontent)
    for cp in allcontent:
        next = re.search(re.compile(cp[0]+'.replyer=(s\d+)'),str).group(1)
        nickname = re.search(re.compile(next+'.nickName=(.*?);'),str).group(1)
        realname = re.search(re.compile(next+'.realName=(.*?);'),str).group(1)
        nickname = re.sub(r'"*', '', nickname).encode('utf-8').decode('unicode_escape').encode('gbk', 'ignore').decode(
            'gbk', 'ignore')
        realname = re.sub(r'"*', '', realname).encode('utf-8').decode('unicode_escape').encode('gbk', 'ignore').decode(
            'gbk', 'ignore')
        #print(nickname, realname)
        if nickname not in dict.keys():
            dict[nickname].append(re.sub(r'&nbsp;',' ',cp[1].encode('utf-8').decode('unicode_escape').encode('gbk', 'ignore').decode('gbk', 'ignore')))
            dict[nickname].append(realname)
    return dict
