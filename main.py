# coding=gbk
#https://www.cnblogs.com/gaigaige/p/7883713.html
import webcrawlerrequests
import answerprocessing
import xlwt
import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from Mainwindow import *
from terminalshow import *

class printThread(QThread):
    buttonclicked = pyqtSignal(int)
    def __init__(self):
        super(printThread,self).__init__()
    def run(self):
        self.buttonclicked.emit(0)
        print(global_url)
        print(global_standardAnswer)
        webcrawlerrequests.getData(global_url,global_name, global_password)
        scoredict = answerprocessing.calculate(global_standardAnswer)
        f = xlwt.Workbook()
        sheet1 = f.add_sheet('成绩', cell_overwrite_ok=True)
        row0 = ["昵称", "姓名", "成绩"]
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i])
        cnt = 1
        for key, value in scoredict.items():
            sheet1.write(cnt, 0, key)
            sheet1.write(cnt, 1, value[1])
            sheet1.write(cnt, 2, value[0])
            cnt += 1
        f.save('test.xls')
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
    def onclick(self):
        global global_url , global_name, global_standardAnswer, global_password
        global_url = self.lineEdit_url.text()
        global_name = self.lineEdit_name.text()
        global_password = self.lineEdit_password.text()
        global_standardAnswer = self.plainTextEdit_standardanswer.toPlainText()
        dialog1 = childWindow1()
        dialog1.show()
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

