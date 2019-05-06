# coding=gbk
import jieba
import json
import tfidf
import weboptions
from collections import defaultdict
import showtime
import time
def getSegString(sentence):
    segpart = jieba.cut(sentence, cut_all=False)  # �ִ�
    # ȥ��ͣ�ô�
    seglist = []
    segstr = ''
    for word in segpart:
        if word not in stopworddict:
            if word != '\t' and word != ' ':
                segstr += word
                segstr += ' '
    return segstr

def getScoreDict(answerdict, standardAnswer):
    #�����д𰸽��зִʣ�seganswerdoc[0]�Ǳ�׼��
    scoresdict = defaultdict(list)
    seganswersdoc = []
    seganswersdoc.append(getSegString(standardAnswer))
    print("  + ��ʼ�ִ�.....")
    for key, values in  answerdict.items():
        seganswersdoc.append(getSegString(values[0]))

    print("  + ���ڼ���TF-IDF����.....")
    weight = tfidf.getTfidf(seganswersdoc)
    weight = tfidf.getTopK(20,weight)

    fullscore = tfidf.getCosine(weight[0], weight[0])
    cnt = 1
    numberlist = [0] * 7
    averagescore= [0] * 7
    print(" + ��ʼͳ�Ƴɼ�.....")
    for key, value in answerdict.items():
        score = tfidf.getCosine(weight[0], weight[cnt])
        score = int(round(score/fullscore, 2) * 100)
        if score < 40:
            numberlist[0] += 1
            averagescore[0] += score
        elif 40 <= score and score < 50:
            numberlist[1] += 1
            averagescore[1] += score
        elif 50 <= score and score < 60:
            numberlist[2] += 1
            averagescore[2] += score
        elif 60 <= score and score < 70:
            numberlist[3] += 1
            averagescore[3] += score
        elif 70 <= score and score < 80:
            numberlist[4] += 1
            averagescore[4] += score
        elif 80 <= score and score < 90:
            numberlist[5] += 1
            averagescore[5] += score
        else :
            numberlist[6] += 1
            averagescore[6] += score
        scoresdict[key].append(score)
        scoresdict[key].append(value[1])
        scoresdict[key].append(value[0])
        cnt += 1
    for i in range(7):
        if numberlist[i] != 0:
            averagescore[i] = int(averagescore[i] / numberlist[i])
    #print(numberlist, averagescore)
    print('  + ���������')
    return scoresdict, seganswersdoc, numberlist, averagescore
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
    print('================================')
    print('��ʼ����ɼ�........')
    global stopworddict
    stopworddict = getStopworddict()
    scoredict , seganswerdoc, numberlist, averagescore = getScoreDict(readAnswersdoc(), standardAnswer)
    print('  + ���ƴ���.....')
    wordcloudpath = showtime.getWordCloud(''.join(seganswerdoc))
    print('  + ��������ͼ.....')
    print(numberlist)
    print(averagescore)
    time.sleep(5)
    numberlistpath = showtime.getNumberCount(numberlist, averagescore)
    print('  + �������!')
    time.sleep(3)
    showtime.saveAsExcel(scoredict)
    return scoredict, wordcloudpath, numberlistpath

if __name__ == '__main__':
    scoredict, wordcloudurl, numberlisturl = calculate("""������˼ά�������ڣ��ƶ����������������ݡ��Ƽ���ȿƼ����Ϸ�չ�ı����£����г������û����Բ�Ʒ������ҵ��ֵ��������������ҵ��̬�Ľ����������ӵ�˼����ʽ���������������˼ά���ǰٶȹ�˾��ʼ������ꡣ�ڰٶȵ�һ�����ͻ�ϣ�������봫ͳ��ҵ���ϰ塢��ҵ��̽�ַ�չ����ʱ��������״��ᵽ��������˼ά������ʡ���˵��������Щ��ҵ���ǽ��Ҫ�л�����˼ά���������������鲻�ǻ������������˼ά��ʽҪ���������ķ�ʽȥ�����⡣���ڼ����ȥ�ˣ����ֹ����Ѿ��𲽱�Խ��Խ�����ҵ�ҡ�������ҵ����ĸ��и�ҵ����������������Ͽ��ˡ�����������˼ά�������Ҳ�ݱ�ɶ����ͬ�Ľ��͡�������ʱ����˼����ʽ���������ڻ�������Ʒ����������ҵ������ָ�Ļ�����������ָ���滥���������ƶ����������Ƿ�����������Ϊδ����������̬һ���ǿ�Խ�����ն��豸�ģ�̨ʽ�����ʼǱ���ƽ�塢�ֻ����ֱ��۾����ȵȡ�
""")
