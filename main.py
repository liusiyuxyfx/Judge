# coding=utf8
#https://www.cnblogs.com/gaigaige/p/7883713.html
import webcrawlerrequests
import answerprocessing
import sys
import re
import databaseact
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from Mainwindow import *
from terminalshow import *
from showpage import *
import showtime
import time
import faulthandler
class printThread(QThread):
    buttonclicked = pyqtSignal(int)
    stopsignal = pyqtSignal()
    def __init__(self):
        super(printThread,self).__init__()
    def run(self):
        self.buttonclicked.emit(0)
        print(global_url, global_name, global_password)
        question, content , islogin = webcrawlerrequests.getData(global_url, global_name, global_password)
        if islogin:
            print(question, content)
            scoredict, wordcloudblob, numberlistblob = answerprocessing.calculate(global_standardAnswer)
            global questionid
            time.sleep(3)
            questionid = databaseact.autocreateQuestion(question, content, wordcloudblob, numberlistblob, scoredict)
            print('================================')
            print('请点击 *下一步* 按钮')
        self.buttonclicked.emit(1)
        self.stopsignal.emit()

class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_getScore.clicked.connect(self.onclick)

    def closeEvent(self, event):
        sys.exit(app.exec_())

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

    #def showPage(self):


class childWindow1(QDialog, Ui_Dialog):
    printth = printThread()
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        #将控制台输出重定向到textEdit控件
        # sys.stdout = EmittingStream(textWritten=self.outputWritten)
        # sys.stderr = EmittingStream(textWritten=self.outputWritten)
        # self.printth.buttonclicked.connect(self.ifbuttoncanpush)
        # self.printth.start()

    def outputWritten(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()
    def missionStart(self):
        sys.stdout = EmittingStream(textWritten=self.outputWritten)
        sys.stderr = EmittingStream(textWritten=self.outputWritten)
        self.printth.buttonclicked.connect(self.ifbuttoncanpush)
        self.printth.stopsignal.connect(self.stopthread)
        self.printth.start()
    def stopthread(self):
        self.printth.stop()
    def ifbuttoncanpush(self, i):
        if i == 0:
            self.pushButton.setEnabled(False)
        elif i == 1:
            self.pushButton.setEnabled(True)

class childWindow2(QDialog, Ui_Dialog_showpage):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

def test():
    app = QApplication(sys.argv)
    myWin = MyWindow()
    child1 = childWindow1()
    myWin.pushButton_getScore.clicked.connect(child1.show)
    myWin.pushButton_getScore.clicked.connect(child1.missionStart)
    myWin.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    faulthandler.enable()
    app = QApplication(sys.argv)
    myWin = MyWindow()
    child1 = childWindow1()
    myWin.pushButton_getScore.clicked.connect(child1.show)
    myWin.pushButton_getScore.clicked.connect(child1.missionStart)
    myWin.show()
    sys.exit(app.exec_())

