# coding=gbk
import pymysql
import uuid
import chardet
import time
import string
import random
from PyQt5.QtWidgets import QMessageBox
def getUniqueQuestionId():
    i = random.randint(1, 3)
    a = random.randint(1, 3)
    imgid = uuid.uuid1().hex[:i]
    imgid2 = uuid.uuid1().hex[a:]
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    imgid  = imgid + imgid2 +  ran_str
    return imgid
def connectDB():
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="richardliu",
                         database="STUDENTSCORE",
                         charset="utf8")
    db.autocommit(True)
    cursor = db.cursor()
    return db, cursor
def tablename(questionid):
    return 'question' + str(questionid)
def createTable(title):
    db, cursor = connectDB()
    try:
        tabletitle = 'create table '+ title
        tablecontent="""
        (
            nickname varchar(40) not null primary key,
            realname varchar(20) null,
            score int null,
            answer TEXT null
        );
        """
        sql = tabletitle + tablecontent
        cursor.execute(sql)
    except Exception as e:
        print(e)
    cursor.close()
    db.close()

def insertScoresSql(cursor ,table, nickname, realname, score, answer):
    try:
        sql = 'insert into StudentScore.' + table
        sql += "(nickname, realname, score, answer) values ('"
        sql += (nickname + "','" + realname + "','" + str(score) + "','" + answer + "')")
        cursor.execute(sql)
    except Exception as e:
        print(e)
        

def insertScore(table, scoredict):
    db, cursor = connectDB()
    try:
        for key, value in scoredict.items():
            #print(key, value[0], value[1], value[2])
            insertScoresSql(cursor, table, key, value[1], value[0], value[2])
    except Exception as e:
        print(e)
    cursor.close()
    db.close()


def createQuestion(title, detail, wordcloudpath, numbercountpath):
    db, cursor = connectDB()
    id = getUniqueQuestionId()
    try:
        db, cursor = connectDB()
        sql = ("insert into StudentScore.questioninfo ( id, title, detail, wordcloud, numbercount)"
               "values ( %s, %s, %s, %s, %s)")
        values = ( id, title, detail, wordcloudpath, numbercountpath)
        #print(chardet.detect(wordpath))
        cursor.execute(sql, values)
    except Exception as e:
        print(e)

    cursor.close()
    db.close()
    return id

def autocreateQuestion(title, detail, wordcloudpath, numbercountpath, scoresdict):
    print('================================')
    print('��ʼд�����ݿ�..........')
    print('  + ������������.....')
    questionid = createQuestion(title, detail, wordcloudpath, numbercountpath)
    tablename = 'question' + str(questionid)
    print('  + �����ɼ���.....')
    createTable(tablename)
    print('  + ����ɼ�.....')
    insertScore(tablename, scoresdict)
    print('  + ���ݿ�洢��ɣ�')
    return questionid

#createTable('asds', cursor)print(createQuestion('asdasdasd','asdasdasdas',wordpath, numbercountpath))


def searchQuestionsDetail(questionid):
    db, cursor = connectDB()
    sql = ('select * from studentscore.questioninfo where id = %s')
    cursor.execute(sql, questionid)
    questioninfo = cursor.fetchone()
    sql = ('select nickname, realname, score from studentscore.' + tablename(questionid))
    cursor.execute(sql)
    rownum = cursor.rowcount
    scoretable = cursor.fetchall()
    #print(scoretable)
    cursor.close()
    db.close()
    return questioninfo, rownum, scoretable

def searchQuestionList():
    db, cursor = connectDB()
    sql = 'select id, title from studentscore.questioninfo'
    cursor.execute(sql)
    questionlist = cursor.fetchall()
    cursor.close()
    db.close()
    return questionlist

def searchStudentById(id,questionid):
    db, cursor = connectDB()
    filename = tablename(questionid)
    sql = ('select * from studentscore.' + filename +' where nickname = %s')
    cursor.execute(sql, id)
    studentinfo = cursor.fetchone()
    cursor.close()
    db.close()
    return studentinfo

def searchStudentByName(name, questionid):
    db, cursor = connectDB()
    filename = tablename(questionid)
    sql = "select * from studentscore." + filename + " where nickname like '%" + name + "%' or realname like '%" + name + "%'"
    cursor.execute(sql)
    studentinfo = cursor.fetchone()
    cursor.close()
    db.close()
    return studentinfo

def deleteQuestion(questionid):
    db, cursor = connectDB()
    filename = tablename(questionid)
    sql = "drop table " + filename
    cursor.execute(sql)
    sql = "delete from studentscore.questioninfo where id = "+ questionid
    cursor.execute(sql)
    cursor.close()
    db.close()

if __name__ == '__main__':
    #createTableSql('asds',cursor)
    # import answerprocessing
    # scoresdict, wordpath, numbercountpath = answerprocessing.calculate("""������˼ά�������ڣ��ƶ����������������ݡ��Ƽ���ȿƼ����Ϸ�չ�ı����£����г������û����Բ�Ʒ������ҵ��ֵ��������������ҵ��̬�Ľ����������ӵ�˼����ʽ���������������˼ά���ǰٶȹ�˾��ʼ������ꡣ�ڰٶȵ�һ�����ͻ�ϣ�������봫ͳ��ҵ���ϰ塢��ҵ��̽�ַ�չ����ʱ��������״��ᵽ��������˼ά������ʡ���˵��������Щ��ҵ���ǽ��Ҫ�л�����˼ά���������������鲻�ǻ������������˼ά��ʽҪ���������ķ�ʽȥ�����⡣���ڼ����ȥ�ˣ����ֹ����Ѿ��𲽱�Խ��Խ�����ҵ�ҡ�������ҵ����ĸ��и�ҵ����������������Ͽ��ˡ�����������˼ά�������Ҳ�ݱ�ɶ����ͬ�Ľ��͡�������ʱ����˼����ʽ���������ڻ�������Ʒ����������ҵ������ָ�Ļ�����������ָ���滥���������ƶ����������Ƿ�����������Ϊδ����������̬һ���ǿ�Խ�����ն��豸�ģ�̨ʽ�����ʼǱ���ƽ�塢�ֻ����ֱ��۾����ȵȡ�""")
    # autocreateQuestion('������ְ�','',wordpath,numbercountpath,scoresdict)
   # searchQuestionsDetail('8d3ed8cb8a7fdab2')
   print(getUniqueQuestionId())