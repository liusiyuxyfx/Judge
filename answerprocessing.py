# coding=gbk
import jieba
import json
import tfidf
import weboptions
import numpy as np
from collections import defaultdict

def getSegString(sentence):
    segpart = jieba.cut(sentence, cut_all=False)  # 分词
    # 去除停用词
    seglist = []
    str = ''
    for word in segpart:
        if word not in stopworddict:
            if word != '\t' and word != ' ':
                str += word
                str += ' '
    return str

def getScoreDict(answerdict, standardAnswer):
    #对所有答案进行分词，seganswerdoc[0]是标准答案
    scoresdict = defaultdict(list)
    seganswersdoc = []
    seganswersdoc.append(getSegString(standardAnswer))
    jieba.enable_parallel(4)  # 开启并行分词模式
    for key, values in  answerdict.items():
        seganswersdoc.append(getSegString(values[0]))
    jieba.disable_parallel()

    weight = tfidf.getTfidf(seganswersdoc)
    weight = tfidf.getTopK(20,weight)
    fullscore = tfidf.getCosine(weight[0], weight[0])
    cnt = 1
    for key, value in answerdict.items():
        score = tfidf.getCosine(weight[0], weight[cnt])
        score = round(score/fullscore, 4) * 100
        if score > 100: print("---------------warning-----------------")
        scoresdict[key].append(score)
        scoresdict[key].append(value[1])
        cnt += 1
    return(scoresdict)

def getStopworddict():
    stopwords = {}
    with open('./nlpfiles/CNENstopwords.txt', 'r',encoding='UTF-8') as file:
        for lines in file:
            stopwords[lines.strip()] = lines.strip()
    return stopwords

def readAnswersdoc():
    answerdict = defaultdict(list)
    with open(weboptions.getCachePath('answers'), 'r') as file:
        answerdict = json.load(file)
    return answerdict

def calculate(standardAnswer):
    global stopworddict
    stopworddict = getStopworddict()
    return getScoreDict(readAnswersdoc(), standardAnswer)




if __name__ == '__main__':
    print (calculate())