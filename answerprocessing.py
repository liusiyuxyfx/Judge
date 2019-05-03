# coding=gbk
import jieba
import json
import re
import weboptions
from collections import defaultdict
correctanswer = """普适计算又称普存计算、普及计算（英文中叫做pervasive computing或者Ubiquitous computing）这一概念强调和环境融为一体的计算，而计算机本身则从人们的视线里消失。在普适计算的模式下，人们能够在任何时间、任何地点、以任何方式进行信息的获取与处理。普适计算的目的是建立一个充满计算和通信能力的环境,同时使这个环境与人们逐渐地融合在一起。在这个融合空间中人们可以随时随地、透明地获得数字化服务。在普适计算环境下, 整个世界是一个网络的世界, 数不清的为不同目的服务的计算和通信设备都连接在网络中, 在不同的服务环境中自由移动。在信息时代，普适计算可以降低设备使用的复杂程度，使人们的生活更轻松、更有效率。实际上，普适计算是网络计算的自然延伸，它使得不仅个人电脑，而且其它小巧的智能设备也可以连接到网络中，从而方便人们即时地获得信息并采取行动"""

def calculate(answerdict):
    jieba.enable_parallel(4)  # 开启并行分词模式
    for key, values in  answerdict.items():
        nickname = key
        realname = values[1]
        answer = values[0]
        segpart = jieba.cut(answer, cut_all=False) #分词
        seglist = []
        stopworddict = getStopworddict()
        #去除停用词
        for word in segpart:
            if word not in stopworddict:
                if word != '\t':
                    seglist.append(word)
        print(nickname, seglist)


    jieba.disable_parallel()
    return answerdict

# def stopwordslist():
#     stopwords = {}
#     stopwords = [line.strip() for line in open('./nlpfiles/CNENstopwords.txt',encoding='UTF-8').readlines()]
#     return stopwords
#由于字典采用hash表，所以python对于字典的查找速度要比list快，在数据较大的情况下，使用dict更加快速
def getStopworddict():
    stopwords = {}
    with open('./nlpfiles/CNENstopwords.txt', 'r',encoding='UTF-8') as file:
        for lines in file:
            stopwords[lines.strip()] = lines.strip()
    return stopwords


if __name__ == '__main__':
    answerdict = defaultdict(list)
    with open(weboptions.getCachePath('answers'), 'r') as file:
        answerdict = json.load(file)
    calculate(answerdict)