# coding=utf8
#https://www.cnblogs.com/gaigaige/p/7883713.html
import web_requests
import nlp_AnswerProcessing
import sys
import re
import data_databaseact
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from Mainwindow import *
from terminalshow import *
from showpage import *
import data_showtime
import time
import faulthandler
from collections import defaultdict
class printThread(QThread):
    buttonclicked = pyqtSignal(int)
    stopsignal = pyqtSignal(int)
    dbsignal = pyqtSignal(str, str, dict, str, list, list)
    def __init__(self):
        super(printThread,self).__init__()
    def run(self):
        self.buttonclicked.emit(0)
        print(global_url, global_name, global_password)
        question, content , islogin = web_requests.getData(global_url, global_name, global_password)
        if islogin:
            #print(question, content)
            scoredict, wordcloudblob, numberlist, averagescore = nlp_AnswerProcessing.calculate(global_standardAnswer)
            #sleep(3)
            print("--------------")
            print('断点')
            #time.sleep(3)
            print('================================')
            print('请点击 *下一步* 按钮')
        self.buttonclicked.emit(1)
        self.dbsignal.emit(question, content, scoredict, wordcloudblob, numberlist, averagescore)
        #self.stopsignal.emit(1)

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号
    def write(self, text):
        self.textWritten.emit(str(text))

class MyWindow(QMainWindow, Ui_MainWindow):
    printth = printThread()
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        sys.stdout = EmittingStream(textWritten=self.outputWritten)
        sys.stderr = EmittingStream(textWritten=self.outputWritten)
        #绑定线程信号
        self.printth.buttonclicked.connect(self.ifbuttoncanpush)
        self.printth.stopsignal.connect(self.stopthread)
        self.printth.dbsignal.connect(self.saveDatabase)

        #绑定窗口信号
        self.pushButton_getScore.clicked.connect(self.onclick)

        self.lineEdit_url.setText('https://www.icourse163.org/spoc/learn/COMPUTER-1002604037?tid=1002792051&_trace_c_p_k2_=8b2564ba9a21437fa6e40053c1f9ef35#/learn/forumdetail?pid=1005050559')
        self.lineEdit_name.setText('18324605567@163.com')
        self.lineEdit_password.setText('yf691111')
        self.plainTextEdit_standardanswer.setPlainText("顺序查找 假定有一个元素顺序情况不明的数组。这种情况如果我们要搜索一个元素就要遍历整个数组，才能知道这个元素是否在数组中。这种方法要检查整个数组，核对每个元素。")
        # print(self.lineEdit_password.text())
    def outputWritten(self, text):
        cursor = self.consoleText.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.consoleText.setTextCursor(cursor)
        self.consoleText.ensureCursorVisible()
    def onclick(self):
        url = re.sub(r'\s+', '',self.lineEdit_url.text())
        name = re.sub(r'\s+', '',self.lineEdit_name.text())
        password = re.sub(r'\s+', '',self.lineEdit_password.text())
        standardAnswer = re.sub(r'\s+', '',self.plainTextEdit_standardanswer.toPlainText())
        if name == '' :
            QMessageBox.critical(self, "错误", "请输入用户名!!", QMessageBox.Ok)
        elif password == '' :
            QMessageBox.critical(self, "错误", "请输入密码!!", QMessageBox.Ok)
        elif url == '':
            QMessageBox.critical(self, "错误", "请输入地址!!", QMessageBox.Ok)
        elif standardAnswer == '' :
            QMessageBox.critical(self, "错误", "请输入标准答案!!", QMessageBox.Ok)
        else :
            #print(type(self.plainTextEdit_standardanswer.toPlainText()))
            global global_url , global_name, global_standardAnswer, global_password
            global_url = self.lineEdit_url.text()
            global_name = self.lineEdit_name.text()
            global_password = self.lineEdit_password.text()
            global_standardAnswer = self.plainTextEdit_standardanswer.toPlainText()
            self.printth.start()
        # self.printth.stopsignal.connect(self.stopthread)

    def stopthread(self, i):
        if i == 1:
            print('stop thread')
            self.printth.quit()
            #self.printth.wait()
            #del(self.printh)
            #self.printth.stop()
            #print()

    def saveDatabase(self,question, content, scoredict, wordcloudblob, numberlist, averagescore):
        print('  + 绘制条形图.....')
        #print(global_numberlist, global_qveragescore)
        print(question, content)
        print(scoredict)
        print(wordcloudblob, numberlist, averagescore)
        numberlistpath = data_showtime.getNumberCount(numberlist, averagescore)
        print('  + 绘制完成!')
        data_databaseact.autocreateQuestion(question, content, wordcloudblob, numberlistpath, scoredict)
    #def showPage(self):
    def ifbuttoncanpush(self, i):
        if i == 0:
            self.pushButton.setEnabled(False)
            self.pushButton_getScore.setEnabled(False)
        elif i == 1:
            self.pushButton.setEnabled(True)
            self.pushButton_getScore.setEnabled(True)

class childWindow2(QDialog, Ui_Dialog_showpage):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)


if __name__ == '__main__':
    faulthandler.enable()
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

