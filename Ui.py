import sys
from time import strftime

from Bridge import Connect
from FrontEnd.accountStore import Account
from FrontEnd.authorizeForm import Authorize
from FrontEnd.backgroundDesign import mainWindowBg
from FrontEnd.loginFrom import Login
from FrontEnd.registerFrom import Register
from FrontEnd.side_bar import sideBar
from FrontEnd.src import *
from FrontEnd.userForm import User
from FrontEnd.view import myAccounts


class Id:
    def __init__(self, MainWindow:QtWidgets.QMainWindow):
        self.parent = MainWindow
        self._side_bar = sideBar(MainWindow)
        self._registerForm = Register(MainWindow)
        self._userForm = User(MainWindow)
        self._loginFrom = Login(MainWindow)
        self._accountForm = Account(MainWindow)
        self._viewAccounts = myAccounts(MainWindow)
        self._authorizeForm = Authorize(MainWindow)

    def sideBar(self):
        return {    
        'parent': self.parent,    
        'master': self._side_bar.master(),
        'accountButton': self._side_bar.accountButton(),
        'viewAccountButton':self._side_bar.viewAccountButton(),
        'userButton': self._side_bar.userButton(),
        'hide': self._side_bar.hide,
        }

    def registerForm(self):
        return {
        'parent': self.parent,    
        'master': self._registerForm.master(),
        'firstNameEntry': self._registerForm.firstNameEntry(),
        'lastNameEntry': self._registerForm.lastNameEntry(),
        'userNameEntry': self._registerForm.userNameEntry(),
        'passwordEntry': self._registerForm.passwordEntry(),
        'repasswordEntry': self._registerForm.repasswordEntry(),
        'registerButton': self._registerForm.registerButton(),
        'loginButton': self._registerForm.loginButton(),
        'generateButton': self._registerForm.generate(),
        'hide': self._registerForm.hide,
        }
    
    def UserForm(self):
        return {
        'parent': self.parent,    
        'master': self._userForm.master(),
        'welcomeTextLable': self._userForm.welcomeText(),
        'firstNameEntry': self._userForm.firstNameEntry(),
        'lastNameEntry': self._userForm.lastNameEntry(),
        'userNameEntry': self._userForm.userNameEntry(),
        'passwordEntry': self._userForm.passwordEntry(),
        'repasswordEntry': self._userForm.repasswordEntry(),
        'updateButton': self._userForm.updateButton(),
        'deleteButton': self._userForm.deleteButton(),
        'generateButton': self._userForm.generate(),
        'hide': self._userForm.hide,
        }
    
    def loginForm(self):
        return {
        'parent': self.parent,
        'master': self._loginFrom.master(),
        'userNameEntry': self._loginFrom.userNameEntry(),
        'passwordEntry': self._loginFrom.passwordEntry(),
        'loginButton': self._loginFrom.loginButton(),
        'registerButton': self._loginFrom.registerButton(),
        'showHideButton': self._loginFrom.showhideButton(),
        'hide': self._loginFrom.hide,
        }

    def accountForm(self):
        return {
        'parent': self.parent,   
        'master': self._accountForm.master(),
        'toBeFormattedLable': self._accountForm.toBeFormatted(),
        'accountNameEntry': self._accountForm.accountNameEntry(),
        'passwordEntry': self._accountForm.passwordEntry(),
        'userNameEntry': self._accountForm.userNameEntry(),
        'storeButton': self._accountForm.storeButton(),
        'showHideButton': self._accountForm.showHideButton(),
        'generateButton': self._accountForm.generateButton(),
        'logoutButton': self._accountForm.logoutButton(),
        'accountTypeCombo': self._accountForm.accountType(),
        'hide': self._accountForm.hide,
        }

    def authorizeForm(self):
        return {
            'parent': self.parent,
            'master': self._authorizeForm.master(),
            'toBeFormattedLable': self._authorizeForm.toBeFormattedLable(),
            'showHideButton': self._authorizeForm.showHideButton(),
            'passwordEntry': self._authorizeForm.passwordEntry(),
            'submitButton': self._authorizeForm.submitButton()
        }

    def viewAccount(self):
        return {
        'parent': self.parent,    
        'master': self._viewAccounts.master(),
        'hide': self._viewAccounts.hide,
        'table': self._viewAccounts.table(),
        'deleteButton': self._viewAccounts.deleteButton(),
        'updateButton': self._viewAccounts.updateButton(),
        }


class Ui(Id):
    def __init__(self,MainWindow):
        super().__init__(MainWindow)
        self.MainWindow = MainWindow
        self.label = QtWidgets.QLabel(self.MainWindow)
        self.label.setGeometry(QtCore.QRect(200, 24, 64, 64))
        self.label.setStyleSheet('background-color: #FEFEFE')
        self.label.setPixmap(QtGui.QPixmap("logo_header.png"))
        self.label_2 = QtWidgets.QLabel('UrePass',self.MainWindow)
        self.label_2.setGeometry(QtCore.QRect(310, 20, 206, 72))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(45)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: #FEFEFE")
        conn = Connect(self)

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
mainWindowBg(MainWindow)
ui = Ui(MainWindow)
MainWindow.setWindowTitle('UrePass')
MainWindow.setFixedSize(677, 613)
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("google.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
production = QtWidgets.QLabel(f'a Sakar Giri production\n   UrePass © {strftime("%Y")}',MainWindow)
font = QtGui.QFont()
font.setFamily("Script MT Bold")
font.setPointSize(10)
production.setFont(font)
production.adjustSize()
production.move(308,95)
production.setStyleSheet('background-color:#F4F4F4')
MainWindow.setWindowIcon(icon)
MainWindow.setStyleSheet("background-color: #FEFEFE")
MainWindow.show()
sys.exit( app.exec_() )