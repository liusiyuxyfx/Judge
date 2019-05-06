from showpage import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QTableWidget,QTableWidgetItem,QWidget,QHBoxLayout,QHeaderView,QMessageBox
from Mainwindow import *
import data_databaseact
import page_main
import sys
import re
class childWindow(QDialog, Ui_Dialog_showpage):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.questionid = global_questionid
        self.label_title.setWordWrap(True)
        self.label_content.setWordWrap(True)
        self.pushButton_search.clicked.connect(self.searchStudentByName)
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_delete.clicked.connect(self.deleteQuestion)
        self.pageload(self.questionid)

    def pageload(self, questionid):
        questioninfo, rownum, scoretable = data_databaseact.searchQuestionsDetail(questionid)
        self.label_title.setText(questioninfo[1])
        self.label_content.setText(questioninfo[2])
        self.updateTable(rownum, scoretable)
        self.loadPicture(questioninfo[3], self.label_wordcloud)
        self.loadPicture(questioninfo[4], self.label_numbercount)
        self.reloadCombobox()

    def queryButton(self, id):
        widget = QWidget()
        queryButton = QPushButton('详情')
        queryButton.clicked.connect(lambda: self.searchStudentById(id))
        hLayout = QHBoxLayout()
        hLayout.addWidget(queryButton)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def reloadCombobox(self):
        try:
            self.comboBox.currentIndexChanged.disconnect(self.loadByCombobox)
        except:
            pass
        self.comboBox.clear()
        questionlist = data_databaseact.searchQuestionList()
        for i in range(len(questionlist)):
            self.comboBox.addItem(questionlist[i][1],questionlist[i][0])
        self.questionid = self.comboBox.currentData()
        self.comboBox.currentIndexChanged.connect(self.loadByCombobox)

    def loadByCombobox(self,i):
        questionid = self.comboBox.itemData(i)
        print(questionid)
        self.pageload(questionid)

    def searchStudentByName(self):
        name = self.lineEdit.text()
        if name == '':
            QMessageBox.critical(self, "错误", "请输入学生姓名!", QMessageBox.Ok)
        try:
            return data_databaseact.searchStudentByName(name, self.questionid)
        except:
            QMessageBox.critical(self, "错误", "查无此人", QMessageBox.Ok)

    def searchStudentById(self, id):
        return data_databaseact.searchStudentById(id, self.questionid)

    def loadPicture(self,name,widget):
        pix = QPixmap('./images/' + name + '.png')
        widget.setPixmap(pix)

    def deleteQuestion(self):
        data_databaseact.deleteQuestion(self.comboBox.currentData())
        self.reloadCombobox()

    def updateTable(self, rownum, scoretable):
        titles = ['昵称', '姓名', ]
        self.tableWidget.clear()
        self.tableWidget.setRowCount(rownum)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(titles)
        for i in range(rownum):
            for j in range(4):
                if j != 3:
                    content = scoretable[i][j]
                    if content == '' or content == 'null':
                        try:
                            content = re.search(r'hrbcu[0-9]*(.*)', scoretable[i][0]).group(1)
                        except:
                            content = '未填写'
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(content)))
                else:
                    self.tableWidget.setCellWidget(i, j, self.queryButton(scoretable[i][0]))

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch | QHeaderView.Stretch) #行宽自适应

if __name__ == '__main__':
    global global_questionid
    global_questionid = 'f3ed92700d11e9a286d8cb8a7fdab2mEdh5LzX'
    app = QApplication(sys.argv)
    childWindow = childWindow()
    childWindow.show()
    sys.exit(app.exec_())
