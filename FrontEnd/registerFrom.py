# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'this.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from .backgroundDesign import registerFormBg
from .src import *

class Register(object):
    def __init__(self, MainWindow):

        self.login_form = QtWidgets.QFrame(MainWindow)
        self.login_form.setEnabled(True)
        self.login_form.setGeometry(QtCore.QRect(160, 140, 431, 441))
        self.login_form.setStyleSheet("background-color: #ffffff;\n"
"border-radius: 25px;")
        self.login_form.setGraphicsEffect(shadow(89))
        self.login_form.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_form.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_form.setObjectName("login_form")
        
        self.label = QtWidgets.QLabel(self.login_form)
        self.label.setGeometry(QtCore.QRect(120, 40, 184, 61))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.lineEdit = QtWidgets.QLineEdit(self.login_form)
        self.lineEdit.setGeometry(QtCore.QRect(80, 120, 130, 30))
        self.lineEdit.setGraphicsEffect(shadow(110))        
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{border-radius: 15px;background-color: #FFFFFF;border: 1px solid;border-color:#EBEBEB}\n"
" QLineEdit:hover{border-color:#4169B6;}")
        self.lineEdit.setObjectName("lineEdit")        

        self.lineEdit_2 = QtWidgets.QLineEdit(self.login_form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 120, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setFamily("Segoe UI")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{border-radius: 15px;background-color: #FFFFFF;border: 1px solid;border-color:#EBEBEB}\n"
" QLineEdit:hover{border-color:#4169B6;}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setGraphicsEffect(shadow(110))
        
        self.lineEdit_3 = QtWidgets.QLineEdit(self.login_form)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 180, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setGraphicsEffect(shadow(110))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{border-radius: 15px;background-color: #FFFFFF;border: 1px solid;border-color:#EBEBEB}\n"
" QLineEdit:hover{border-color:#4169B6;}")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.login_form)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 240, 160, 30))
        self.lineEdit_4.setGraphicsEffect(shadow(110))
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{border-radius: 15px;background-color: #FFFFFF;border: 1px solid;border-color:#EBEBEB}\n"
" QLineEdit:hover{border-color:#4169B6;}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.lineEdit_5 = QtWidgets.QLineEdit(self.login_form)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 300, 160, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setGraphicsEffect(shadow(110))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit{border-radius: 15px;background-color: #FFFFFF;border: 1px solid;border-color:#EBEBEB}\n"
" QLineEdit:hover{border-color:#4169B6;}")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_5.setObjectName("lineEdit_5")
        
        self.pushButton = QtWidgets.QPushButton(self.login_form)
        self.pushButton.setGeometry(QtCore.QRect(130, 355, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"        background-color: #FFFFFF;\n"
"        border-radius: 15px;\n"
"        padding-right: 40px;\n"
"        }\n"
"        QPushButton:hover{\n"
"        background-color: #E3DFDF;\n"
"        }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Image/add-user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setGraphicsEffect(shadow(110))
        
        self.pushButton1 = QtWidgets.QPushButton(self.login_form)
        self.pushButton1.setGeometry(QtCore.QRect(130, 400, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/enter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton1.setIcon(icon)
        self.pushButton1.setIconSize(QtCore.QSize(20, 20))
        self.pushButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton1.setStyleSheet("QPushButton{\n"
        "background-color: #FFFFFF;\n"
        "border-radius: 15px;\n"
        "padding-right: 55px;\n"
        "}"
        "QPushButton:hover{\n"
        "background-color: #E3DFDF;\n"
        "}")
        self.pushButton1.setObjectName("pushButton")
        self.pushButton1.setGraphicsEffect(shadow(110))

        self.pushButton2 = QtWidgets.QPushButton(self.login_form)
        self.pushButton2.setGeometry(QtCore.QRect(320, 250, 24, 13))
        self.pushButton2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton2.setIcon(icon)
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.pressed.connect(lambda:show(self.pushButton2,self.lineEdit_4))
        self.pushButton2.released.connect(lambda:hide(self.pushButton2,self.lineEdit_4))
        
        self.pushButton3 = QtWidgets.QPushButton(self.login_form)
        self.pushButton3.setGeometry(QtCore.QRect(320, 310, 24, 13))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/show.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton3.setIcon(icon)
        self.pushButton3.setObjectName("pushButton")
        self.pushButton3.pressed.connect(lambda:show(self.pushButton3,self.lineEdit_5))
        self.pushButton3.released.connect(lambda:hide(self.pushButton3,self.lineEdit_5))

        self.pushButton4 = QtWidgets.QPushButton(self.login_form)
        self.pushButton4.setGeometry(QtCore.QRect(360, 250, 20, 16))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Image/password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton4.setIcon(icon)
        self.pushButton4.setObjectName("pushButton")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        registerFormBg(self.login_form)
        self.hide()

    def hide(self): self.login_form.hide()
    def master(self): return self.login_form
    def firstNameEntry(self): return self.lineEdit
    def lastNameEntry(self): return self.lineEdit_2
    def userNameEntry(self): return self.lineEdit_3
    def passwordEntry(self): return self.lineEdit_4
    def repasswordEntry(self): return self.lineEdit_5
    def registerButton(self): return self.pushButton
    def loginButton(self): return self.pushButton1
    def generate(self): return self.pushButton4

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">REGISTRATION</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "First name"))        
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Last Name"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Re-enter Password"))
        self.pushButton.setText(_translate("MainWindow", "         Register"))
        self.pushButton1.setText(_translate("MainWindow", "             Login"))