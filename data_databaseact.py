# coding=gbk
import pymysql
import uuid
import string
import random
import os
#���Ψһ�����
def getUniqueQuestionId():
    i = random.randint(1, 15)
    a = random.randint(1, 15)
    uid = uuid.uuid1().hex
    imgid = uid[:i]
    imgid2 = uid[len(uid)-a:]
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    imgid  = imgid + imgid2 +  ran_str
    return imgid

#�������ݿ�
#return next, error, db, cursor
def connectDB():
    try:
        db = pymysql.connect(host="localhost",
                             user="root",
                             password="richardliu",
                             database="STUDENTSCORE",
                             charset="utf8")
        db.autocommit(True)
        cursor = db.cursor()
        return db, cursor
    except Exception as e:
        raise e
#��ñ���
def tablename(questionid):
    return 'question' + str(questionid)

#��ȡ���¼�¼
def getLatestId():
    sql = 'select * from studentscore.questioninfo where id=(select last_insert_id());'
    db, cursor = connectDB()
    cursor.execute(sql)
    id = cursor.fetchone()[0]
    return id



#�����ɼ���
def createTable(title):
    try:
        db, cursor = connectDB()
        tabletitle = 'create table '+ title
        tablecontent="""
        (
            nickname varchar(100) not null primary key,
            realname varchar(100) null,
            score varchar(6) null,
            answer TEXT null
        );
        """
        sql = tabletitle + tablecontent
        cursor.execute(sql)
        cursor.close()
        db.close()
    except Exception as e:
        raise e

#�������SQL
def insertScoresSql(cursor ,table, nickname, realname, score, answer):
    try:
        sql = 'insert into StudentScore.' + table
        sql += "(nickname, realname, score, answer) values ( %s, %s, %s, %s)"
        value = (nickname, realname, str(score), answer)
        cursor.execute(sql, value)
    except Exception as e:
        raise Exception(e, nickname, realname, score, answer, sql)

#����ȫ���ɼ�
def insertScore(table, scoredict):
    db, cursor = connectDB()
    for key, value in scoredict.items():
        #print(key, value[0], value[1], value[2])
        try:
            insertScoresSql(cursor, table, key, value[1], value[0], value[2])
        except Exception as e:
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            print('���ݿ�������')
            print('�������ͣ�')
            print(e)

    cursor.close()
    db.close()

#���������Ϣ
def createQuestion(title, detail, wordcloudpath, numbercountpath):
    try:
        db, cursor = connectDB()
        id = getUniqueQuestionId()
        sql = ("insert into StudentScore.questioninfo ( id, title, detail, wordcloud, numbercount)"
               "values ( %s, %s, %s, %s, %s)")
        values = ( id, title, detail, wordcloudpath, numbercountpath)
        cursor.execute(sql, values)
        cursor.close()
        db.close()
        return id
    except Exception as e:
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print ('����������')
        print ('��������:')
        print (e)

#�Զ��������⼰�ɼ���
def autocreateQuestion(title, detail, wordcloudpath, numbercountpath, scoresdict):
    try:
        print('================================')
        print('��ʼд�����ݿ�..........')
        print('  + ������������.....')
        questionid = createQuestion(title, detail, wordcloudpath, numbercountpath)
        print('  + �����ɼ���.....')
        createTable(tablename(questionid))
        print('  + ����ɼ�.....')
        insertScore(tablename(questionid), scoresdict)
        print('  + ���ݿ�洢��ɣ�')
        return questionid
    except Exception as e:
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('�Զ��������ͳɼ������')
        print('��������:')
        print(e)
        print('���Գ����������ݿ����')
        try:
            deleteQuestion(questionid)
            os.remove('./images/' + wordcloudpath +'.png')
            os.remove('./images/' + numbercountpath + '.png')
        except:
            pass
        finally:
            print('���ز������')




#��ѯ��������
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

#��ѯȫ������
def searchQuestionList():
    db, cursor = connectDB()
    sql = 'select id, title from studentscore.questioninfo'
    cursor.execute(sql)
    questionlist = cursor.fetchall()
    cursor.close()
    db.close()
    return questionlist

#��ѯ����ѧ��id��ѯ�ɼ�����
def searchStudentById(id,questionid):
    db, cursor = connectDB()
    filename = tablename(questionid)
    sql = ('select * from studentscore.' + filename +' where nickname = %s')
    cursor.execute(sql, id)
    studentinfo = cursor.fetchone()
    cursor.close()
    db.close()
    return studentinfo

#��ѯ����ѧ��������ѯ
def searchStudentByName(name, questionid):
    db, cursor = connectDB()
    filename = tablename(questionid)
    sql = "select * from studentscore." + filename + " where nickname like '%" + name + "%' or realname like '%" + name + "%'"
    cursor.execute(sql)
    studentinfo = cursor.fetchone()
    cursor.close()
    db.close()
    return studentinfo

#��ѯ����ѧ���ɼ�
def searchScoreTable(questionid):
    db, cursor = connectDB()
    sql = "select nickname, realname, score from studentscore." + tablename(questionid)
    cursor.execute(sql)
    scoretable = cursor.fetchall()
    cursor.close()
    db.close()
    return scoretable

#ɾ�����⼰��������
def deleteQuestion(questionid):
    db, cursor = connectDB()
    filename = tablename(questionid)
    try:
        sql = "drop table " + filename
        cursor.execute(sql)
    except Exception as e:
        print(e)
        pass
    try:
        sql = ('select * from studentscore.questioninfo where id = %s')
        cursor.execute(sql, (questionid))
        questioninfo = cursor.fetchone()
        wordcloudname = questioninfo[3]
        numbercountname = questioninfo[4]
        os.remove('./images/'+wordcloudname+'.png')
        os.remove('./images/'+numbercountname+'.png')
    except Exception as e:
        print(e)
        pass
    try:
        sql = "delete from studentscore.questioninfo where id = %s"
        cursor.execute(sql,questionid)
    except Exception as e:
        print(e)
        pass
    cursor.close()
    db.close()

def updateStudentScore(questionid, nickname, realname, score):
    db , cursor = connectDB()
    sql = 'update studentscore.' + tablename(questionid) + ' set realname = %s , score = %s where nickname = %s'
    cursor.execute(sql,(realname, score, nickname))
    cursor.close()
    db.close()


def connectDB2():
    try:
        db = pymysql.connect(host="localhosts",
                             user="root",
                             password="richardliu",
                             database="STUDENTSCORE",
                             charset="utf8")
        db.autocommit(True)
        cursor = db.cursor()
    except Exception as e:
        print(e)

        #pass
def b(i):
    try:
        connectDB2()
    except Exception as e:
        raise Exception('��¼ʧ��')
    if i == 4:
        raise Exception('buasd')
    b = 1 / i

def a():
    b(4)
if __name__ == '__main__':
    print(getLatestId())
    #print(getUniqueQuestionId())
    # try:
    #     a()
    # except Exception as e:
    #     print(e)
    # print(list(range(1, 6)))
    #print('2'.isdigit())
    #a(2)
   #print(getUniqueQuestionId())
