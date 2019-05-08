from showpage import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QTableWidget,QTableWidgetItem,QWidget,QHBoxLayout,QHeaderView,QMessageBox
import data_databaseact
import sys
import xlwt
import re
import detailpage
class childWindow(QDialog, Ui_Dialog_showpage):
    sendStudentDetail = pyqtSignal( str, int, str, str, str, str)
    showed = False
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        #self.questionid = global_questionid
        self.childwindow3 = DetailPage()
        self.sendStudentDetail.connect(self.childwindow3.loadPage)
        self.label_title.setWordWrap(True)
        self.label_content.setWordWrap(True)
        self.pushButton_search.clicked.connect(self.searchStudentByName)
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_delete.clicked.connect(self.deleteQuestion)
        #self.pageload(self.questionid)
        self.pushButton_getexcel.clicked.connect(self.saveAsExcel)
        self.pushButton_search.clicked.connect(self.showDetailPageByName)
    #从查询数据库按钮进入时
    def loadFromFirstButton(self):
        self.reloadCombobox(False)
        try:
            questionid = data_databaseact.searchQuestionList()[0][0]
            self.pageload(questionid)
        except:
            pass
    def loadFromNextButton(self):
        self.reloadCombobox(True)
    #加载页面
    def pageload(self, questionid):
        print('查询数据库')
        questioninfo, rownum, scoretable = data_databaseact.searchQuestionsDetail(questionid)
        print('查找完成')
        self.questionid = questionid
        self.label_title.setText(questioninfo[1])
        self.label_content.setText(questioninfo[2])
        self.updateTable(rownum, scoretable)
        print('加载图片')
        self.loadPicture(questioninfo[3], self.label_wordcloud)
        self.loadPicture(questioninfo[4], self.label_numbercount)
        print('加载完成')

    #表格内查询按钮
    def queryButton(self,row,  id):
        widget = QWidget()
        queryButton = QPushButton('详情')
        queryButton.clicked.connect(lambda: self.searchStudentById(row, id))
        hLayout = QHBoxLayout()
        hLayout.addWidget(queryButton)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    #加载combobox选项
    def reloadCombobox(self, nextButton):
        try:
            self.comboBox.currentTextChanged.disconnect(self.loadByCombobox)
        except:
            pass
        self.comboBox.clear()
        questionlist = data_databaseact.searchQuestionList()
        for i in range(len(questionlist)):
            self.comboBox.addItem(questionlist[i][1],questionlist[i][0])
        if not nextButton:
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

    #加载图片
    def loadPicture(self,name,widget):
        pix = QPixmap('./images/' + name + '.png')
        widget.setPixmap(pix)

    #删除问题
    def deleteQuestion(self):
        data_databaseact.deleteQuestion(self.comboBox.currentData())
        self.loadFromFirstButton()

    #更新表格内容
    def updateTable(self, rownum, scoretable):
        titles = ['昵称', '姓名', '成绩']
        #print()
        self.tableWidget.clear()
        print('删除完成')
        self.tableWidget.setRowCount(rownum)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(titles)
        print('添加中')
        try:
            for i in range(rownum):
                for j in range(4):
                    if j == 3:
                        self.tableWidget.setCellWidget(i, j, self.queryButton(i, scoretable[i][0]))
                    else :
                        content = scoretable[i][j]
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(content)))
        except Exception as e:
            print(e)

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

    def showDetailPageByName(self):
        try:
            studentinfo = data_databaseact.searchStudentByName(self.lineEdit.text(), self.questionid)
            item = self.tableWidget.findItems(self.lineEdit.text(), Qt.MatchContains)
            if item:
                item = item[0]
                row = item.row()
                self.sendStudentDetail.emit(self.questionid, row, studentinfo[0], studentinfo[1], studentinfo[2], studentinfo[3])
                self.childwindow3.sendRowChange.connect(self.updateRowData)
                self.childwindow3.show()
            else :
                QMessageBox.warning(self,'警告','查无此人',QMessageBox.Ok)
        except Exception as e:
            QMessageBox.critical(self, '错误', str(e), QMessageBox.Ok)

    #框内查询事件
    def searchStudentById(self,row, id):
     try:
         studentinfo = data_databaseact.searchStudentById(id, self.questionid)
         self.sendStudentDetail.emit(self.questionid, row, studentinfo[0], studentinfo[1], studentinfo[2],
                                     studentinfo[3])
         self.childwindow3.sendRowChange.connect(self.updateRowData)
         self.childwindow3.show()
     except Exception as e:
         QMessageBox.critical(self, '错误', str(e)+'    '+id+ '        '+self.questionid, QMessageBox.Ok)
    def updateRowData(self,row, realname, score):
        self.tableWidget.setItem(row, 1, QTableWidgetItem(str(realname)))
        self.tableWidget.setItem(row, 2, QTableWidgetItem(str(score)))

class DetailPage(QDialog,detailpage.Ui_Dialog_DetailPage):
    sendRowChange = pyqtSignal(int, str, str)
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_update.clicked.connect(self.updateData)

    def updateData(self):
        try:
             data_databaseact.updateStudentScore(self.questionid, self.nickname, self.lineEdit_realname.text(), self.lineEdit_score.text())
             self.sendRowChange.emit(self.row, self.lineEdit_realname.text(), self.lineEdit_score.text())
        except Exception as e:
            QMessageBox.critical(self, '错误', str(e), QMessageBox.Ok)
    def loadPage(self, questionid,row, nickname, realname, score, answer):
        self.row = row
        self.questionid= questionid
        self.nickname = nickname
        self.realname = realname
        self.answer = answer
        self.lineEdit_nickname.setText(nickname)
        self.lineEdit_realname.setText(realname)
        self.lineEdit_score.setText(score)
        self.plainTextEdit_answer.setPlainText(answer)
        self.lineEdit_nickname.setReadOnly(True)
        self.plainTextEdit_answer.setReadOnly(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    childWindow = childWindow()
    childWindow.show()
    sys.exit(app.exec_())
#     app = QApplication(sys.argv)
#     loadingpage = LoadingWindow()
#     loadingpage.show()
#     sys.exit(app.exec_())
#