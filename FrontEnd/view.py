# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'this.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from .backgroundDesign import viewBg
from .src import *

class myAccounts(object):
    def __init__(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 613)
        MainWindow.setStyleSheet("background-color: #FEFEFE")
        self.login = QtWidgets.QFrame(MainWindow)
        self.login.setGeometry(QtCore.QRect(160, 140, 431, 441))
        self.login.setStyleSheet("border-radius: 25px;\n"
"")
        self.login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login.setObjectName("login")
        
        self.label = QtWidgets.QLabel(self.login)
        self.label.setGeometry(QtCore.QRect(140, 60, 144, 29))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.tableWidget = QtWidgets.QTableWidget(self.login)
        self.tableWidget.setGeometry(QtCore.QRect(5, 140, 425, 201))
        self.tableWidget.setStyleSheet("QHeaderView::section{\n"
"        background-color: #ffffff;\n"
"        border-radius:25px;\n"
"        width:25;    \n"
"        color:#1F2428;\n"
"        }\n"
"        \n"
"        QTableView::item{\n"
"        color:#1F2428;\n"
"        selection-background-color:#EDEDED;\n"
"        selection-color:#000000;\n"
"        }\n"
"        \n"
"        QTableView::item:hover{\n"
"        background-color:#EDEDED;\n"
"        color:#000000;\n"
"        border-radius:14px;\n"
"        }\n"
"        \n"
"        QHeaderView::section:hover{\n"
"        background-color:#EDEDED;\n"
"        border-radius:11px;\n"
"        color:#000000;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.login.setGraphicsEffect(shadow(89))
        viewBg(self.login)

        self.edit = QtWidgets.QFrame(self.login)
        self.edit.setGraphicsEffect(shadow(190))
        self.edit.setGeometry(QtCore.QRect(135, 360, 140, 50))
        self.edit.setStyleSheet("background-color: #FEFEFE;\n"
"border-radius: 25px;")
        self.edit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.edit.setFrameShadow(QtWidgets.QFrame.Raised)

        self.pushButton = QtWidgets.QPushButton(self.edit)
        self.pushButton.setGeometry(QtCore.QRect(80, 10, 36, 32))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icon/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(32, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.edit)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 36, 32))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icon/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "My accounts"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Account Type"))
        
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Accounts Name"))
        
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "User Name"))
        
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Password"))
        
        self.tableWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        

    def hide(self): return self.login.hide()

    def master(self): return self.login

    def table(self): return self.tableWidget

    def updateButton(self): return self.pushButton_2

    def deleteButton(self): return self.pushButton