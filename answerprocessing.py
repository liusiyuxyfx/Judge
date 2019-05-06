# coding=gbk
import jieba
import json
import tfidf
import weboptions
from collections import defaultdict
import showtime
import time
def getSegString(sentence):
    segpart = jieba.cut(sentence, cut_all=False)  # 分词
    # 去除停用词
    seglist = []
    segstr = ''
    for word in segpart:
        if word not in stopworddict:
            if word != '\t' and word != ' ':
                segstr += word
                segstr += ' '
    return segstr

def getScoreDict(answerdict, standardAnswer):
    #对所有答案进行分词，seganswerdoc[0]是标准答案
    scoresdict = defaultdict(list)
    seganswersdoc = []
    seganswersdoc.append(getSegString(standardAnswer))
    print("  + 开始分词.....")
    for key, values in  answerdict.items():
        seganswersdoc.append(getSegString(values[0]))

    print("  + 正在计算TF-IDF矩阵.....")
    weight = tfidf.getTfidf(seganswersdoc)
    weight = tfidf.getTopK(20,weight)

    fullscore = tfidf.getCosine(weight[0], weight[0])
    cnt = 1
    numberlist = [0] * 7
    averagescore= [0] * 7
    print(" + 开始统计成绩.....")
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
    print('  + 计算结束！')
    return scoresdict, seganswersdoc, numberlist, averagescore
#scoredict结构{key = nickname, value=[score, realname, answer)}
#seganswerdoc结构{key = nickname, value=[realname, answer])

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
    print('开始计算成绩........')
    global stopworddict
    stopworddict = getStopworddict()
    scoredict , seganswerdoc, numberlist, averagescore = getScoreDict(readAnswersdoc(), standardAnswer)
    print('  + 绘制词云.....')
    wordcloudpath = showtime.getWordCloud(''.join(seganswerdoc))
    print('  + 绘制条形图.....')
    print(numberlist)
    print(averagescore)
    time.sleep(5)
    numberlistpath = showtime.getNumberCount(numberlist, averagescore)
    print('  + 绘制完成!')
    time.sleep(3)
    showtime.saveAsExcel(scoredict)
    return scoredict, wordcloudpath, numberlistpath

if __name__ == '__main__':
    scoredict, wordcloudurl, numberlisturl = calculate("""互联网思维，就是在（移动）互联网、大数据、云计算等科技不断发展的背景下，对市场、对用户、对产品、对企业价值链乃至对整个商业生态的进行重新审视的思考方式。最早提出互联网思维的是百度公司创始人李彦宏。在百度的一个大型活动上，李彦宏与传统产业的老板、企业家探讨发展问题时，李彦宏首次提到“互联网思维”这个词。他说，我们这些企业家们今后要有互联网思维，可能你做的事情不是互联网，但你的思维方式要逐渐像互联网的方式去想问题。现在几年过去了，这种观念已经逐步被越来越多的企业家、甚至企业以外的各行各业、各个领域的人所认可了。但“互联网思维”这个词也演变成多个不同的解释。互联网时代的思考方式，不局限在互联网产品、互联网企业；这里指的互联网，不单指桌面互联网或者移动互联网，是泛互联网，因为未来的网络形态一定是跨越各种终端设备的，台式机、笔记本、平板、手机、手表、眼镜，等等。
""")
