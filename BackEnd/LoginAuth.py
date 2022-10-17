from FrontEnd.src import *

from .Csys import Hash


class conDBLogin(Hash):
    def __init__(self):
        super().__init__()
        self.switch = False

    def check_user(self,user:str):
        userName = [self._decrypt(i[3]) for i in self.db.fetch()] 
        
        if user in userName:
            return [self._decrypt(i[4]) for i in self.db.fetch()][userName.index( user )],\
            [i[0] for i in self.db.fetch()][userName.index( user )]
            # pwd,id = [list of pwd][index of exiting user],[list of id][index of exiting user]
        else: return False

    def authenticate(self,inputTuple:tuple):
        userName, pwd = inputTuple
        
        if self.check_user(userName):
            org, id = self.check_user(userName)

            if pwd == org:
                self.switch = True
                self.db.cu(id)
                return True

            else: return False

        else: return False

class validateLogin(conDBLogin):

    def __init__(self,mainDict:dict):
        super().__init__()

        self.errorStyleSheet = 'QLineEdit{border-radius:15px;background-color:#F0F0F0;border:1px solid;border-color:red;}'
        self.normalStyleSheet = 'QLineEdit{border-radius: 15px;background-color: #F0F0F0;border: 1px solid;border-color:#EBEBEB}'
        self.parent = mainDict['parent']
        self.master = mainDict['master']
        self.userName:QtWidgets.QLineEdit = mainDict['userNameEntry']
        self.pwd:QtWidgets.QLineEdit = mainDict['passwordEntry']
        self.get:QtWidgets.QPushButton = mainDict['loginButton']

    def __get_inputs(self): return self.userName.text(), self.pwd.text()

    def validate(self):

        for i in [self.userName, self.pwd]: i.setStyleSheet(self.normalStyleSheet)

        if any([self.__get_inputs()[0] =='', self.__get_inputs()[1] =='']):
            for entry in [self.userName, self.pwd]: entry.setStyleSheet(self.errorStyleSheet)
            message(self.parent, 'Felids empty!','w')

        elif len(self.__get_inputs()[0]) < 5: 
            message(self.parent,'User name can\'t have less than 5 characters','w')
            self.userName.setStyleSheet(self.errorStyleSheet)

        elif len(self.__get_inputs()[1]) < 8:
            message(self.parent,'Invalid Password','w')
            self.pass1.setStyleSheet(self.errorStyleSheet)

        else:
            if self.authenticate(self.__get_inputs()):
                user = self._decrypt( self.db.fetch_user(self.db.fetch_cu())[0][1] )
                message(self.parent,f'Welcome {user}!','s')
                for entry in [self.userName, self.pwd]: entry.clear()
            
            else:
                message(self.parent,f'Invaild user name or password!','w')
                for entry in [self.userName, self.pwd]: 
                    entry.setStyleSheet(self.errorStyleSheet)
                    entry.clear()