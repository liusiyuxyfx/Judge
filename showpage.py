# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showpage.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_showpage(object):
    def setupUi(self, Dialog_showpage):
        Dialog_showpage.setObjectName("Dialog_showpage")
        Dialog_showpage.resize(1241, 854)
        self.layoutWidget = QtWidgets.QWidget(Dialog_showpage)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 551, 691))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_left = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_left.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_left.setObjectName("verticalLayout_left")
        self.label_title = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_left.addWidget(self.label_title)
        self.label_content = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_content.setFont(font)
        self.label_content.setObjectName("label_content")
        self.verticalLayout_left.addWidget(self.label_content)
        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_left.addWidget(self.tableWidget)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog_showpage)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 770, 521, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton_search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_search.setObjectName("pushButton_search")
        self.horizontalLayout.addWidget(self.pushButton_search)
        self.pushButton_close = QtWidgets.QPushButton(Dialog_showpage)
        self.pushButton_close.setGeometry(QtCore.QRect(1020, 770, 151, 41))
        self.pushButton_close.setObjectName("pushButton_close")
        self.label_2 = QtWidgets.QLabel(Dialog_showpage)
        self.label_2.setGeometry(QtCore.QRect(631, 51, 46, 28))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog_showpage)
        self.label_3.setGeometry(QtCore.QRect(631, 391, 46, 28))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Dialog_showpage)
        self.comboBox.setGeometry(QtCore.QRect(630, 10, 511, 51))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_delete = QtWidgets.QPushButton(Dialog_showpage)
        self.pushButton_delete.setGeometry(QtCore.QRect(1140, 20, 61, 31))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label_wordcloud = QtWidgets.QLabel(Dialog_showpage)
        self.label_wordcloud.setGeometry(QtCore.QRect(640, 90, 560, 300))
        self.label_wordcloud.setText("")
        self.label_wordcloud.setObjectName("label_wordcloud")
        self.label_numbercount = QtWidgets.QLabel(Dialog_showpage)
        self.label_numbercount.setGeometry(QtCore.QRect(640, 430, 560, 300))
        self.label_numbercount.setText("")
        self.label_numbercount.setObjectName("label_numbercount")

        self.retranslateUi(Dialog_showpage)
        QtCore.QMetaObject.connectSlotsByName(Dialog_showpage)

    def retranslateUi(self, Dialog_showpage):
        _translate = QtCore.QCoreApplication.translate
        Dialog_showpage.setWindowTitle(_translate("Dialog_showpage", "Dialog"))
        self.label_title.setText(_translate("Dialog_showpage", "TextLabel"))
        self.label_content.setText(_translate("Dialog_showpage", "TextLabel"))
        self.label.setText(_translate("Dialog_showpage", "根据姓名查询："))
        self.pushButton_search.setText(_translate("Dialog_showpage", "查询"))
        self.pushButton_close.setText(_translate("Dialog_showpage", "关闭"))
        self.label_2.setText(_translate("Dialog_showpage", "热词:"))
        self.label_3.setText(_translate("Dialog_showpage", "统计:"))
        self.pushButton_delete.setText(_translate("Dialog_showpage", "删除"))


