#https://www.jianshu.com/p/68b0b3126e8c
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import math
def sumproduct(x, y): #x1x2+y1y2+..
    sum = 0
    for a, b in zip(x, y):
        sum += a*b
    return sum

def squreroot(x): #sqrt(x1^2+y1^2)
    return math.sqrt(sumproduct(x, x))

def getCosine(x, y):
    return sumproduct(x, y)/(squreroot(x)*squreroot(y) + 0.000000000001)#防止分母为0

def getTopK(k, weight):
    sortindices = np.argsort(weight[0])
    dataset = np.delete(weight, sortindices[:len(sortindices) - k].tolist(), axis=1)#获取tfidf值最高的关键词的索引，并将其他关键词删除
    return dataset

def getTfidf(seganswersdoc):
    vectorizer = CountVectorizer()
    freqmatrix = vectorizer.fit_transform(seganswersdoc) #计算词频矩阵
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(freqmatrix) #计算tf-idf
    word = vectorizer.get_feature_names()  # 获取所有关键词
    weight = tfidf.toarray()  #将tf-idf的稀疏矩阵（csr_matrix格式）转化为普通矩阵
    return weight
