# coding=gbk
import jieba
import json
import tfidf
import weboptions
from collections import defaultdict
#import showtime

def getSegString(sentence):
    segpart = jieba.cut(sentence, cut_all=False)  # �ִ�
    # ȥ��ͣ�ô�
    seglist = []
    str = ''
    for word in segpart:
        if word not in stopworddict:
            if word != '\t' and word != ' ':
                str += word
                str += ' '
    return str

def getScoreDict(answerdict, standardAnswer):
    #�����д𰸽��зִʣ�seganswerdoc[0]�Ǳ�׼��
    scoresdict = defaultdict(list)
    seganswersdoc = []
    seganswersdoc.append(getSegString(standardAnswer))
    jieba.enable_parallel(4)  # �������зִ�ģʽ
    for key, values in  answerdict.items():
        seganswersdoc.append(getSegString(values[0]))
    jieba.disable_parallel()

    weight = tfidf.getTfidf(seganswersdoc)
    weight = tfidf.getTopK(20,weight)
    fullscore = tfidf.getCosine(weight[0], weight[0])
    cnt = 1
    for key, value in answerdict.items():
        score = tfidf.getCosine(weight[0], weight[cnt])
        score = round(score/fullscore, 2) * 100
        scoresdict[key].append(int(score))
        scoresdict[key].append(value[1])
        scoresdict[key].append(value[0])
        cnt += 1
    return scoresdict, seganswersdoc
#scoredict�ṹ{key = nickname, value=[score, realname, answer)}
#seganswerdoc�ṹ{key = nickname, value=[realname, answer])

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
    scoredict , seganswerdoc = getScoreDict(readAnswersdoc(), standardAnswer)
    #showtime.getWordCloud(''.join(seganswerdoc))
    return scoredict, seganswerdoc

if __name__ == '__main__':
    scoredict, seganswerdoc = calculate("""������˼ά�������ڣ��ƶ����������������ݡ��Ƽ���ȿƼ����Ϸ�չ�ı����£����г������û����Բ�Ʒ������ҵ��ֵ��������������ҵ��̬�Ľ����������ӵ�˼����ʽ���������������˼ά���ǰٶȹ�˾��ʼ������ꡣ�ڰٶȵ�һ�����ͻ�ϣ�������봫ͳ��ҵ���ϰ塢��ҵ��̽�ַ�չ����ʱ��������״��ᵽ��������˼ά������ʡ���˵��������Щ��ҵ���ǽ��Ҫ�л�����˼ά���������������鲻�ǻ������������˼ά��ʽҪ���������ķ�ʽȥ�����⡣���ڼ����ȥ�ˣ����ֹ����Ѿ��𲽱�Խ��Խ�����ҵ�ҡ�������ҵ����ĸ��и�ҵ����������������Ͽ��ˡ�����������˼ά�������Ҳ�ݱ�ɶ����ͬ�Ľ��͡�������ʱ����˼����ʽ���������ڻ�������Ʒ����������ҵ������ָ�Ļ�����������ָ���滥���������ƶ����������Ƿ�����������Ϊδ����������̬һ���ǿ�Խ�����ն��豸�ģ�̨ʽ�����ʼǱ���ƽ�塢�ֻ����ֱ��۾����ȵȡ�
""")
    print(''.join(seganswerdoc))