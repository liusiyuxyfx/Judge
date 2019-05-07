# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'detailpage.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_DetailPage(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(585, 673)
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 90, 411, 501))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.lineEdit_realname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_realname.setFont(font)
        self.lineEdit_realname.setObjectName("lineEdit_realname")
        self.gridLayout.addWidget(self.lineEdit_realname, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_score = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_score.setFont(font)
        self.lineEdit_score.setObjectName("lineEdit_score")
        self.gridLayout.addWidget(self.lineEdit_score, 2, 1, 1, 1)
        self.lineEdit_nickname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit_nickname.setFont(font)
        self.lineEdit_nickname.setObjectName("lineEdit_nickname")
        self.gridLayout.addWidget(self.lineEdit_nickname, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.plainTextEdit_answer = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.plainTextEdit_answer.setObjectName("plainTextEdit_answer")
        self.gridLayout.addWidget(self.plainTextEdit_answer, 3, 1, 1, 1)
        self.pushButton_close = QtWidgets.QPushButton(Dialog)
        self.pushButton_close.setGeometry(QtCore.QRect(440, 610, 113, 32))
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_update = QtWidgets.QPushButton(Dialog)
        self.pushButton_update.setGeometry(QtCore.QRect(300, 610, 113, 32))
        self.pushButton_update.setObjectName("pushButton_update")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(260, 30, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "网名:"))
        self.label_4.setText(_translate("Dialog", "答案:"))
        self.label_2.setText(_translate("Dialog", "昵称:"))
        self.label_3.setText(_translate("Dialog", "成绩:"))
        self.pushButton_close.setText(_translate("Dialog", "关闭"))
        self.pushButton_update.setText(_translate("Dialog", "更新"))
        self.label_5.setText(_translate("Dialog", "详情"))


