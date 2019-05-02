import re
from collections import defaultdict

def getCleandict(str):
    dict=defaultdict(list)
    str = re.sub(r'<.*?>','',str)
    allcontent = re.findall(re.compile(r'(s\d+).content="(.*)";'),str)
    #print(allcontent)
    for cp in allcontent:
        next = re.search(re.compile(cp[0]+'.replyer=(s\d+)'),str).group(1)
        nickname = re.search(re.compile(next+'.nickName=(.*?);'),str).group(1)
        realname = re.search(re.compile(next+'.realName=(.*?);'),str).group(1)
        nickname = re.sub(r'"*', '', nickname)
        realname = re.sub(r'"*', '', realname)
        print(nickname, realname)
        if nickname not in dict.keys():
            dict[nickname].append(cp[1].encode('utf-8').decode('unicode-escape'))
            dict[nickname].append(realname.encode('utf-8').decode('unicode-escape'))
    return dict
