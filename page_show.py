from showpage import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QTableWidget,QTableWidgetItem,QWidget,QHBoxLayout,QHeaderView,QMessageBox
import data_databaseact
import sys
import xlwt
import re
class childWindow(QDialog, Ui_Dialog_showpage):

    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        #self.questionid = global_questionid
        self.label_title.setWordWrap(True)
        self.label_content.setWordWrap(True)
        self.pushButton_search.clicked.connect(self.searchStudentByName)
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_delete.clicked.connect(self.deleteQuestion)
        #self.pageload(self.questionid)
        self.pushButton_getexcel.clicked.connect(self.saveAsExcel)
        self.reloadCombobox()
        try:
            questionid = data_databaseact.searchQuestionList()[0][0]
            self.pageload(questionid)
        except:
            pass

    #加载页面
    def pageload(self, questionid):
        questioninfo, rownum, scoretable = data_databaseact.searchQuestionsDetail(questionid)
        self.questionid = questionid
        self.label_title.setText(questioninfo[1])
        self.label_content.setText(questioninfo[2])
        self.updateTable(rownum, scoretable)
        self.loadPicture(questioninfo[3], self.label_wordcloud)
        self.loadPicture(questioninfo[4], self.label_numbercount)

    #表格内查询按钮
    def queryButton(self, id):
        widget = QWidget()
        queryButton = QPushButton('详情')
        queryButton.clicked.connect(lambda: self.searchStudentById(id))
        hLayout = QHBoxLayout()
        hLayout.addWidget(queryButton)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    #加载combobox选项
    def reloadCombobox(self):
        try:
            self.comboBox.currentTextChanged.disconnect(self.loadByCombobox)
        except:
            pass
        self.comboBox.clear()
        questionlist = data_databaseact.searchQuestionList()
        for i in range(len(questionlist)):
            self.comboBox.addItem(questionlist[i][1],questionlist[i][0])
        self.questionid = self.comboBox.currentData()
        try:
            self.comboBox.currentTextChanged.connect(self.loadByCombobox)
        except:
            pass

    #combobox选择事件
    def loadByCombobox(self):
        self.questionid = self.comboBox.currentData()
        print(self.questionid)
        self.pageload(self.questionid)

    #根据学生姓名查询
    def searchStudentByName(self):
        name = self.lineEdit.text()
        if name == '':
            QMessageBox.critical(self, "错误", "请输入学生姓名!", QMessageBox.Ok)
        try:
            return data_databaseact.searchStudentByName(name, self.questionid)
        except:
            QMessageBox.critical(self, "错误", "查无此人", QMessageBox.Ok)

    #框内查询事件
    def searchStudentById(self, id):
        return data_databaseact.searchStudentById(id, self.questionid)

    #加载图片
    def loadPicture(self,name,widget):
        pix = QPixmap('./images/' + name + '.png')
        widget.setPixmap(pix)

    #删除问题
    def deleteQuestion(self):
        data_databaseact.deleteQuestion(self.comboBox.currentData())
        self.reloadCombobox()

    #更新表格内容
    def updateTable(self, rownum, scoretable):
        titles = ['昵称', '姓名', '成绩']
        print('删除中')
        self.tableWidget.clear()
        print('删除完成')
        self.tableWidget.setRowCount(rownum)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(titles)
        print('添加中')
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
        print('添加完成')
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch | QHeaderView.Stretch) #行宽自适应

    def saveAsExcel(self):
        scoretable = data_databaseact.searchScoreTable(self.questionid)
        f = xlwt.Workbook()
        sheet1 = f.add_sheet('成绩', cell_overwrite_ok=True)
        row0 = ["昵称", "姓名", "成绩"]
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i])
        cnt = 1
        for i in range (len(scoretable)):
            sheet1.write(cnt, 0, scoretable[i][0])
            sheet1.write(cnt, 1, scoretable[i][1])
            sheet1.write(cnt, 2, scoretable[i][2])
            cnt += 1
        f.save('./学生成绩单.xls')
        QMessageBox.information(self, '导出成功', '请到程序根目录查看 学生成绩单.xls')
if __name__ == '__main__':
    global global_questionid
    global_questionid = 'f3ed92700d11e9a286d8cb8a7fdab2mEdh5LzX'
    app = QApplication(sys.argv)
    childWindow = childWindow()
    childWindow.show()
    sys.exit(app.exec_())
