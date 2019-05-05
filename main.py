# coding=gbk
#https://www.cnblogs.com/gaigaige/p/7883713.html
import webcrawlerrequests
import answerprocessing
import xlwt
import sys
import re
import databaseact
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from Mainwindow import *
from terminalshow import *

class printThread(QThread):
    buttonclicked = pyqtSignal(int)
    def __init__(self):
        super(printThread,self).__init__()
    def run(self):
        self.buttonclicked.emit(0)
        question, content , islogin = webcrawlerrequests.getData(global_url,global_name, global_password)
        if islogin:
            scoredict, wordcloudblob, numberlistblob = answerprocessing.calculate(global_standardAnswer)
            databaseact.insertScore(question, content, scoredict, wordcloudblob, numberlistblob)
        self.buttonclicked.emit(1)
        pass

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
            dialog1 = childWindow1()
            dialog1.exec()

class childWindow1(QDialog, Ui_Dialog):
    printth = printThread()
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        #将控制台输出重定向到textEdit控件
        sys.stdout = EmittingStream(textWritten=self.outputWritten)
        sys.stderr = EmittingStream(textWritten=self.outputWritten)
        self.printth.buttonclicked.connect(self.ifbuttoncanpush)
        self.printth.start()

    def closeEvent(self, event):
        self.printth.quit()

    def outputWritten(self, text):
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self.textEdit.setTextCursor(cursor)
        self.textEdit.ensureCursorVisible()

    def ifbuttoncanpush(self, i):
        if i == 0:
            self.pushButton.setEnabled(False)
        elif i == 1:
            self.pushButton.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

