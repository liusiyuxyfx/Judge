# coding=gbk
import pymysql
import uuid
import string
import random
import os
#获得唯一问题号
def getUniqueQuestionId():
    i = random.randint(1, 15)
    a = random.randint(1, 15)
    uid = uuid.uuid1().hex
    imgid = uid[:i]
    imgid2 = uid[len(uid)-a:]
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    imgid  = imgid + imgid2 +  ran_str
    return imgid

#连接数据库
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
#获得表名
def tablename(questionid):
    return 'question' + str(questionid)

#获取最新记录
def getLatestId():
    sql = 'select * from studentscore.questioninfo where id=(select last_insert_id());'
    db, cursor = connectDB()
    cursor.execute(sql)
    id = cursor.fetchone()[0]
    return id



#创建成绩表
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

#插入语句SQL
def insertScoresSql(cursor ,table, nickname, realname, score, answer):
    try:
        sql = 'insert into StudentScore.' + table
        sql += "(nickname, realname, score, answer) values ( %s, %s, %s, %s)"
        value = (nickname, realname, str(score), answer)
        cursor.execute(sql, value)
    except Exception as e:
        raise Exception(e, nickname, realname, score, answer, sql)

#插入全部成绩
def insertScore(table, scoredict):
    db, cursor = connectDB()
    for key, value in scoredict.items():
        #print(key, value[0], value[1], value[2])
        try:
            insertScoresSql(cursor, table, key, value[1], value[0], value[2])
        except Exception as e:
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            print('数据库插入错误')
            print('错误类型：')
            print(e)

    cursor.close()
    db.close()

#添加问题信息
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
        print ('添加问题错误')
        print ('错误类型:')
        print (e)

#自动创建问题及成绩表
def autocreateQuestion(title, detail, wordcloudpath, numbercountpath, scoresdict):
    try:
        print('================================')
        print('开始写入数据库..........')
        print('  + 创建问题详情.....')
        questionid = createQuestion(title, detail, wordcloudpath, numbercountpath)
        print('  + 创建成绩表.....')
        createTable(tablename(questionid))
        print('  + 插入成绩.....')
        insertScore(tablename(questionid), scoresdict)
        print('  + 数据库存储完成！')
        return questionid
    except Exception as e:
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        print('自动添加问题和成绩表出错')
        print('错误类型:')
        print(e)
        print('尝试撤回所有数据库操作')
        try:
            deleteQuestion(questionid)
            os.remove('./images/' + wordcloudpath +'.png')
            os.remove('./images/' + numbercountpath + '.png')
        except:
            pass
        finally:
            print('撤回操作完成')




#查询问题详情
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

#查询全部问题
def searchQuestionList():
    db, cursor = connectDB()
    sql = 'select id, title from studentscore.questioninfo'
    cursor.execute(sql)
    questionlist = cursor.fetchall()
    cursor.close()
    db.close()
    return questionlist

#查询根据学生id查询成绩详情
def searchStudentById(id,questionid):
    db, cursor = connectDB()
    filename = tablename(questionid)
    sql = ('select * from studentscore.' + filename +' where nickname = %s')
    cursor.execute(sql, id)
    studentinfo = cursor.fetchone()
    cursor.close()
    db.close()
    return studentinfo

#查询根据学生姓名查询
def searchStudentByName(name, questionid):
    db, cursor = connectDB()
    filename = tablename(questionid)
    sql = "select * from studentscore." + filename + " where nickname like '%" + name + "%' or realname like '%" + name + "%'"
    cursor.execute(sql)
    studentinfo = cursor.fetchone()
    cursor.close()
    db.close()
    return studentinfo

#查询所有学生成绩
def searchScoreTable(questionid):
    db, cursor = connectDB()
    sql = "select nickname, realname, score from studentscore." + tablename(questionid)
    cursor.execute(sql)
    scoretable = cursor.fetchall()
    cursor.close()
    db.close()
    return scoretable

#删除问题及其关联表格
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
        raise Exception('登录失败')
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
