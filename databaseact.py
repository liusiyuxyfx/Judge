# coding=gbk
import pymysql
import uuid
import chardet
def connectDB():
    db = pymysql.connect(host="localhost",
                         user="root",
                         password="richardliu",
                         database="STUDENTSCORE",
                         charset="utf8")
    db.autocommit(True)
    cursor = db.cursor()
    return db, cursor

def createTable(title):
    db, cursor = connectDB()
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
    cursor.close()
    db.close()

def insertScoresSql(cursor ,table, nickname, realname, score, answer):
    sql = 'insert into StudentScore.' + table
    sql += "(nickname, realname, score, answer) values ('"
    sql += (nickname + "','" + realname + "','" + str(score) + "','" + answer + "')")
    cursor.execute(sql)

def insertScore(table, scoredict):
    db, cursor = connectDB()
    for key, value in scoredict.items():
        #print(key, value[0], value[1], value[2])
        insertScoresSql(cursor, table, key, value[1], value[0], value[2])
    cursor.close()
    db.close()

def createQuestion(title, detail, wordcloudpath, numbercountpath):
    db, cursor = connectDB()
    id = str(uuid.uuid1().hex[16:])
    sql = ("insert into StudentScore.questioninfo ( id, title, detail, wordcloud, numbercount)"
           "values ( %s, %s, %s, %s, %s)")
    values = ( id, title, detail, wordcloudpath, numbercountpath)
    #print(chardet.detect(wordpath))
    cursor.execute(sql, values)
    cursor.close()
    db.close()
    return id

def autocreateQuestion(title, detail, wordcloudpath, numbercountpath,scoresdict):
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

if __name__ == '__main__':
    #createTableSql('asds',cursor)
    import answerprocessing
    scoresdict, wordpath, numbercountpath = answerprocessing.calculate("""������˼ά�������ڣ��ƶ����������������ݡ��Ƽ���ȿƼ����Ϸ�չ�ı����£����г������û����Բ�Ʒ������ҵ��ֵ��������������ҵ��̬�Ľ����������ӵ�˼����ʽ���������������˼ά���ǰٶȹ�˾��ʼ������ꡣ�ڰٶȵ�һ�����ͻ�ϣ�������봫ͳ��ҵ���ϰ塢��ҵ��̽�ַ�չ����ʱ��������״��ᵽ��������˼ά������ʡ���˵��������Щ��ҵ���ǽ��Ҫ�л�����˼ά���������������鲻�ǻ������������˼ά��ʽҪ���������ķ�ʽȥ�����⡣���ڼ����ȥ�ˣ����ֹ����Ѿ��𲽱�Խ��Խ�����ҵ�ҡ�������ҵ����ĸ��и�ҵ����������������Ͽ��ˡ�����������˼ά�������Ҳ�ݱ�ɶ����ͬ�Ľ��͡�������ʱ����˼����ʽ���������ڻ�������Ʒ����������ҵ������ָ�Ļ�����������ָ���滥���������ƶ����������Ƿ�����������Ϊδ����������̬һ���ǿ�Խ�����ն��豸�ģ�̨ʽ�����ʼǱ���ƽ�塢�ֻ����ֱ��۾����ȵȡ�""")
    autocreateQuestion('������ְ�','',wordpath,numbercountpath,scoresdict)