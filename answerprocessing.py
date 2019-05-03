# coding=gbk
import jieba
import json
import re
import weboptions
from collections import defaultdict
correctanswer = """���ʼ����ֳ��մ���㡢�ռ����㣨Ӣ���н���pervasive computing����Ubiquitous computing����һ����ǿ���ͻ�����Ϊһ��ļ��㣬�����������������ǵ���������ʧ�������ʼ����ģʽ�£������ܹ����κ�ʱ�䡢�κεص㡢���κη�ʽ������Ϣ�Ļ�ȡ�봦�����ʼ����Ŀ���ǽ���һ�����������ͨ�������Ļ���,ͬʱʹ��������������𽥵��ں���һ��������ںϿռ������ǿ�����ʱ��ء�͸���ػ�����ֻ����������ʼ��㻷����, ����������һ�����������, �������Ϊ��ͬĿ�ķ���ļ����ͨ���豸��������������, �ڲ�ͬ�ķ��񻷾��������ƶ�������Ϣʱ�������ʼ�����Խ����豸ʹ�õĸ��ӳ̶ȣ�ʹ���ǵ���������ɡ�����Ч�ʡ�ʵ���ϣ����ʼ���������������Ȼ���죬��ʹ�ò������˵��ԣ���������С�ɵ������豸Ҳ�������ӵ������У��Ӷ��������Ǽ�ʱ�ػ����Ϣ����ȡ�ж�"""

def calculate(answerdict):
    jieba.enable_parallel(4)  # �������зִ�ģʽ
    for key, values in  answerdict.items():
        nickname = key
        realname = values[1]
        answer = values[0]
        segpart = jieba.cut(answer, cut_all=False) #�ִ�
        seglist = []
        stopworddict = getStopworddict()
        #ȥ��ͣ�ô�
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
#�����ֵ����hash������python�����ֵ�Ĳ����ٶ�Ҫ��list�죬�����ݽϴ������£�ʹ��dict���ӿ���
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