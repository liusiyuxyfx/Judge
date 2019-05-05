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
        font.setPointSize(25)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.verticalLayout_left.addWidget(self.label_title)
        self.label_content = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_content.setFont(font)
        self.label_content.setObjectName("label_content")
        self.verticalLayout_left.addWidget(self.label_content)
        self.tableView = QtWidgets.QTableView(self.layoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_left.addWidget(self.tableView)
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
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.graphicsView_wordcloud = QtWidgets.QGraphicsView(Dialog_showpage)
        self.graphicsView_wordcloud.setGeometry(QtCore.QRect(630, 80, 561, 301))
        self.graphicsView_wordcloud.setObjectName("graphicsView_wordcloud")
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
        self.graphicsView_vu = QtWidgets.QGraphicsView(Dialog_showpage)
        self.graphicsView_vu.setGeometry(QtCore.QRect(631, 427, 561, 321))
        self.graphicsView_vu.setObjectName("graphicsView_vu")

        self.retranslateUi(Dialog_showpage)
        QtCore.QMetaObject.connectSlotsByName(Dialog_showpage)

    def retranslateUi(self, Dialog_showpage):
        _translate = QtCore.QCoreApplication.translate
        Dialog_showpage.setWindowTitle(_translate("Dialog_showpage", "Dialog"))
        self.label_title.setText(_translate("Dialog_showpage", "TextLabel"))
        self.label_content.setText(_translate("Dialog_showpage", "TextLabel"))
        self.label.setText(_translate("Dialog_showpage", "根据姓名查询："))
        self.pushButton.setText(_translate("Dialog_showpage", "查询"))
        self.pushButton_close.setText(_translate("Dialog_showpage", "关闭"))
        self.label_2.setText(_translate("Dialog_showpage", "热词:"))
        self.label_3.setText(_translate("Dialog_showpage", "统计:"))


