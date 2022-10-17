from datetime import datetime
from turtle import up

from FrontEnd.src import *

from .Csys import Hash


class User(Hash):

    def __init__(self, mainDict:dict):
        super().__init__()

        self.parent:QtWidgets.QMainWindow = mainDict['parent']
        self.firstNameEntry: QtWidgets.QLineEdit = mainDict['firstNameEntry']
        self.lastNameEntry: QtWidgets.QLineEdit = mainDict['lastNameEntry']
        self.userNameEntry: QtWidgets.QLineEdit = mainDict['userNameEntry']
        self.passwordEntry: QtWidgets.QLineEdit = mainDict['passwordEntry']
        self.repasswordEntry: QtWidgets.QLineEdit = mainDict['repasswordEntry']
        self.updateButton: QtWidgets.QPushButton = mainDict['updateButton']
        self.deleteButton: QtWidgets.QPushButton = mainDict['deleteButton']
        self.welcomeTextLable: QtWidgets.QLabel = mainDict['welcomeTextLable']

        self.updateButton.clicked.connect(self.update)

        self.errorStyleSheet = 'QLineEdit{border-radius:15px;background-color:#F0F0F0;border:1px solid;border-color:red;}'
        self.normalStyleSheet = 'QLineEdit{border-radius: 15px;background-color: #F0F0F0;border: 1px solid;border-color:#EBEBEB}' 
    
    def sayHello(self):
        self.welcomeTextLable.setText(
            f'Good {self.greetings()}, {self.__userName()}'
        )    
        self.welcomeTextLable.adjustSize()
    
    def greetings(self):

        time = int( datetime.now().strftime('%H') )

        if time >= 0 and time < 12: return 'morning'

        elif time >= 12 and time < 18: return 'afternoon'

        elif time >= 18 and time < 20: return 'evening'

        elif time >= 20 and time <= 23: return 'night'        

    def __get_inputs(self):
        return self.firstNameEntry.text(), self.lastNameEntry.text(), self.userNameEntry.text(), self.passwordEntry.text(), self.repasswordEntry.text()

    def __userName(self):
        for table in self.db.fetch():
            for row in table:
                if row == self.db.fetch_cu():
                    return self._decrypt(table[1])

    def check_user_exist(self, userName:str):
        userList = [self._decrypt(i[3]) for i in self.db.fetch()]
        idList = [i[0] for i in self.db.fetch()]
        if userName in [self._decrypt(i[3]) for i in self.db.fetch()]\
        and idList[ userList.index(userName) ] != self.db.fetch_cu(): 
            return True
        
        else: return False
    
    def validate(self):
        for entry in [self.firstNameEntry, self.lastNameEntry, self.userNameEntry,
            self.passwordEntry, self.repasswordEntry]: entry.setStyleSheet(self.normalStyleSheet)

        if any([self.__get_inputs()[0] =='', self.__get_inputs()[1] == '',self.__get_inputs()[2] == '']):
            for entry in [self.firstNameEntry, self.lastNameEntry, self.userNameEntry, self.passwordEntry, self.repasswordEntry]: 
                entry.setStyleSheet(self.errorStyleSheet)
            message(self.parent, 'Felids empty!','w')

        if self.__get_inputs()[3] != '':

            if self.__get_inputs()[4] == '':
                self.repasswordEntry.setStyleSheet(self.errorStyleSheet)
                message(self.parent, 'Felids empty!','w')
    
            elif self.__get_inputs()[2] == self.__get_inputs()[3]:
                message(self.parent,'Invalid input: User name and password must not be same!','w')
    
            elif len(self.__get_inputs()[3]) < 8:
                message(self.parent,'Password can\'t have less than 8 characters','w')
                self.passwordEntry.setStyleSheet(self.errorStyleSheet)
            
            elif self.checkUqChar():
                message(self.parent,'Your password must contain special characters like @,#,$ etc.','w')
                self.passwordEntry.setStyleSheet(self.errorStyleSheet)

            elif self.__get_inputs()[3].isnumeric() or self.__get_inputs()[3].isalpha():
                message(self.parent,'Your password must conatin alphabets and numbers.','w')
                self.passwordEntry.setStyleSheet(self.errorStyleSheet)

            elif self.__get_inputs()[3] != self.__get_inputs()[4]:
                        message(self.parent,'Password Unmatched!','w')
                        self.repasswordEntry.setStyleSheet(self.errorStyleSheet)

        elif len(self.__get_inputs()[2]) < 5:
            message(self.parent,'User name can\'t have less than 5 characters','w')
            self.userNameEntry.setStyleSheet(self.errorStyleSheet)

        elif len(self.__get_inputs()[2]) > 30: 
            message(self.parent,'User name can\'t have more than 30 characters','w')
            self.userNameEntry.setStyleSheet(self.errorStyleSheet)

        else: 
            userName = self.__get_inputs()[2]

            if self.check_user_exist(userName):
                message(self.parent,'User already exists! Try other user name.','w')
                self.userNameEntry.setStyleSheet(self.errorStyleSheet)

            else:
                return True

    def checkUqChar(self):
        uqChar = '@_!#$%^&*()<>?-~'
        for letters in list(self.__get_inputs()[3]):
            if uqChar.find(letters) > -1: return False

        return True
            
    def filter(self):
        id = self.db.fetch_cu()

        for datas in self.db.fetch():

            for data in datas:

                if id == data:

                    return self._decrypt(datas[1]),self._decrypt(datas[2]),self._decrypt(datas[3])

    def placement(self):
        fname, sname, username = self.filter()
    
        self.firstNameEntry.setText(fname)
        self.lastNameEntry.setText(sname)
        self.userNameEntry.setText(username)

    def update(self): 

        if self.validate():

            rowList = ['fname', 'lname', 'userName', 'passWord']    

            orginal = [self._decrypt(data) for data in self.db.fetch_user( self.db.fetch_cu() )[0][1:]]

            updateList = list( self.__get_inputs()[:4] )
            updateList[0] = updateList[0].capitalize()
            updateList[1] = updateList[0].capitalize()
            
            for data in updateList:

                if data not in orginal and data != '':
                    
                    index = updateList.index(data)

                    data = self._encrypt(data)

                    self.db.update_cu(
                        rowList[ index ], self.db.fetch_cu(), data
                    )
            
            
            if orginal == [self._decrypt(data) for data in self.db.fetch_user( self.db.fetch_cu() )[0][1:]]:
                message(self.parent, 'No changes were made!','a')
            
            else:
                message(self.parent,'Your account was updated successfully!','s')
                self.sayHello()
                self.placement()

    def delete_user(self):
        self.db.delete(self.db.fetch_cu())