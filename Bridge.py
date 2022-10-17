from BackEnd.Authorize import Authorize
from BackEnd.Csys import generate_pass
from BackEnd.DB import DB
from BackEnd.LoginAuth import validateLogin
from BackEnd.Registration import validateRegister
from BackEnd.Store import validateStore
from BackEnd.User import User
from BackEnd.viewAccounts import viewAccounts
from FrontEnd.src import *


class Connect(QtWidgets.QWidget):

    def __init__(self, idDict:object):
        super().__init__()

        self.idDict = idDict
        self._sidebarids:dict = self.idDict.sideBar()
        self._registerids:dict = self.idDict.registerForm()
        self._loginids:dict = self.idDict.loginForm()
        self._accountids:dict = self.idDict.accountForm()
        self._viewAccountids:dict = self.idDict.viewAccount()
        self._authorizeids:dict = self.idDict.authorizeForm()
        self._userids: dict = self.idDict.UserForm()

        self._register = validateRegister(self._registerids)
        self._login = validateLogin(self._loginids)
        self._store = validateStore(self._accountids)
        self._view = viewAccounts(self._viewAccountids)
        self._authorize = Authorize(self._authorizeids)
        self._user = User(self._userids)

        self.sidebar_switch = None

        self.db = DB()
        self.login()
        self.register()
        self.sidebar()
        self.account()
        self.user()
        self.view()
        self.view_first()
        self.authorize()

    def viewButtonClicked(self):
        self.sidebar_switch = 0

    def userButtonClicked(self):
        self.sidebar_switch = 1

    def view_first(self):

        if len(self.db.fetch()) == 0: self._registerids['master'].show()
        
        else: self._loginids['master'].show()

    def sidebar(self):
        self._sidebarids['accountButton'].clicked.connect(lambda:[self._accountids['master'].show(),
            self._userids['master'].hide(),self._authorizeids['master'].hide(), self._viewAccountids['hide']()])
        
        self._sidebarids['viewAccountButton'].clicked.connect(lambda:[self._viewAccountids['hide'](),
            self._userids['master'].hide(),self._authorizeids['master'].show(), self._accountids['hide'](),
            self.viewButtonClicked()])
        
        self._sidebarids['userButton'].clicked.connect(lambda:[
            self._userids['master'].hide(), self._accountids['hide'](),
            self._authorizeids['master'].show(), self._viewAccountids['master'].hide(),
            self.userButtonClicked()
        ])
    
    def register(self):
        self._registerids['loginButton'].clicked.connect(lambda:[ self._loginids['master'].show(), self._registerids['hide']() ])
        self._registerids['registerButton'].clicked.connect(lambda:[self._register.validate(),self.after_register()])
        self._registerids['generateButton'].clicked.connect(lambda:self._registerids['passwordEntry'].setText(generate_pass()))

    def after_register(self):
        if self._register.switch:
            self._registerids['hide']()
            self._loginids['master'].show()
            self._register.switch = False

    def login(self):
        self._loginids['registerButton'].clicked.connect(lambda:[self._registerids['master'].show(), self._loginids['master'].hide()])
        self._loginids['loginButton'].clicked.connect(lambda:[self._login.validate(),self.after_login()])

    def after_login(self):
        if self._login.switch:
            self._loginids['hide']()
            self._accountids['master'].show()
            self._sidebarids['master'].show()
            self._authorizeids['toBeFormattedLable'].setText(f'Hello {self._authorize._decrypt( self._authorize._userName() )},\nPlease enter your password to verify.')
            self._authorizeids['toBeFormattedLable'].adjustSize()
            self._store.sayHello()
            self._user.sayHello()
            self._user.placement()
            self.loadIntoTable()
            self._login.switch = False

    def loadIntoTable(self):
        self._view.load_data(
                self.db.fetch_specific( self.db.fetch_cu() )
            )

    def account(self):
        self._accountids['generateButton'].clicked.connect(lambda:self._accountids['passwordEntry'].setText(generate_pass()))
        self._accountids['logoutButton'].clicked.connect(lambda: [self._accountids['hide'](), self._sidebarids['hide'](),
        self._accountids['accountNameEntry'].clear(),self._loginids['master'].show()])
        self._accountids['storeButton'].clicked.connect(self.after_store_validation)

    def after_store_validation(self):
        self._store.validate()
        if self._store.switch:
            self.loadIntoTable()
            self._store.switch = False

    def view(self):
        self._viewAccountids['updateButton'].clicked.connect(self.after_update)

    def authorize(self):
        self._authorize.submitButton.clicked.connect(self.authorizeAccountRecords)

    def authorizeAccountRecords(self):

        if self._authorize.validate():
            self._authorizeids['master'].hide()
            
            if self.sidebar_switch:
                self._userids['master'].show()
            
            else:
                self._viewAccountids['master'].show()

    def after_update(self):
        if self._view.updateData() is not None:
            id, accountType, accountName, userName, passWord = self._view.updateData()
            self._viewAccountids['hide']()
            self._accountids['master'].show()   
            self._accountids['accountTypeCombo'].setCurrentText(accountType)
            self._accountids['accountNameEntry'].setText(accountName)
            self._accountids['userNameEntry'].setText(userName)
            self._accountids['passwordEntry'].setText(passWord)

            
    def user(self):
        self._userids['generateButton'].clicked.connect(lambda:self._userids['passwordEntry'].setText(generate_pass()))
        self._userids['deleteButton'].clicked.connect(lambda:[
            self._user.delete_user(), self._sidebarids['master'].hide(),
            self._user['master'].hide(), self.view_first()
        ])