# coding=gbk
import pymysql
import answerprocessing
def connectDB():
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="richardliu",
                         database="STUDENTSCORE",
                         charset="utf8")
    db.autocommit(True)
    cursor = db.cursor()
    return db, cursor

def createTableSql(title, cursor):
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

def insertScoresSql(cursor ,table, nickname, realname, score, answer):
    sql = 'insert into StudentScore.' + table
    sql += "(nickname, realname, score, answer) values ('"
    sql += (nickname + "','" + realname + "','" + str(score) + "','" + answer + "')")
    cursor.execute(sql)

def insertScore(table, scoredict):
    db, cursor = connectDB()
    for key, value in scoredict.items():
        print(key, value[0], value[1], value[2])
        insertScoresSql(cursor, table, key, value[1], value[0], value[2])
    cursor.close()
    db.close()

def createQuestion(title, detail, wordcloudblob, numbercountblob):
    db, cursor = connectDB()
    sql = ("insert into StudentScore.questioninfo (title, detail, numbercount)" 
           "values (%s, %s, %s, %s)")
    values = (title, detail, wordcloudblob, numbercountblob)
    cursor.execute(sql, values)
    cursor.close()
    db.close()

#createTable('asds', cursor)

if __name__ == '__main__':
    db, cursor = connectDB()
    createTableSql('asds',cursor)
    scoresdict, seglist = answerprocessing.calculate("""互联网思维，就是在（移动）互联网、大数据、云计算等科技不断发展的背景下，对市场、对用户、对产品、对企业价值链乃至对整个商业生态的进行重新审视的思考方式。最早提出互联网思维的是百度公司创始人李彦宏。在百度的一个大型活动上，李彦宏与传统产业的老板、企业家探讨发展问题时，李彦宏首次提到“互联网思维”这个词。他说，我们这些企业家们今后要有互联网思维，可能你做的事情不是互联网，但你的思维方式要逐渐像互联网的方式去想问题。现在几年过去了，这种观念已经逐步被越来越多的企业家、甚至企业以外的各行各业、各个领域的人所认可了。但“互联网思维”这个词也演变成多个不同的解释。互联网时代的思考方式，不局限在互联网产品、互联网企业；这里指的互联网，不单指桌面互联网或者移动互联网，是泛互联网，因为未来的网络形态一定是跨越各种终端设备的，台式机、笔记本、平板、手机、手表、眼镜，等等。""")
    insertScore(cursor,'asds', scoresdict)
    cursor.close()
    db.close()