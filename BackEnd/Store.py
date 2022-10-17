from datetime import datetime

from BackEnd.Csys import Hash
from FrontEnd.src import *


class conStoreBD(Hash):
    def __init__(self):
        super().__init__()
        self.switch = False

    def _store(self, data: tuple[str, str, str, str]):
        accountType, accountName, userName, passWord = data

        if self.user_check(userName, accountType):
            return True
        
        else:
            self.db.ins_specific(self.db.fetch_cu(), 
                [self._id(),self._encrypt(accountType),self._encrypt(accountName),
                self._encrypt(userName), self._encrypt(passWord)]
            )
            self.switch = True
            return False
    
    def user_check(self, userName:str, accountType: str):
            
            userList = [self._decrypt(userName[3])  for userName in self.db.fetch_specific( self.db.fetch_cu() ) ]
            accountTypeList = [self._decrypt(accountType[1])  for accountType in self.db.fetch_specific( self.db.fetch_cu() ) ]

            if userName in userList:
                index = -1

                for user in userList:
                    index += 1

                    if user == userName:
                        if accountType == accountTypeList[index]:
                            return True
            else:
                return False

class validateStore(conStoreBD):
    def __init__(self,mainDict):
        super().__init__()
        
        self.errorStyleSheet = 'QLineEdit{border-radius:15px;background-color:#FFFFFF;border:1px solid;border-color:red;}'
        self.normalStyleSheet = 'QLineEdit{border-radius: 15px;background-color: #FFFFFF;border: 1px solid;border-color:#EBEBEB}' 
        self.normalStyleSheetCombo = '''QComboBox{ border:1px solid;border-color:#FFFFFF;border-radius: 10px;padding-left: 10px;}
        QComboBox QAbstractItemView{selection-background-color:#DADADA;selection-color: #000000;}
        QComboBox::drop-down{border:0px;}QComboBox::down-arrow{image:url(:/Icon/down-arrow.png);height: 15px;width: 15px;padding-left:-15px;}
        QComboBox:hover{border-color:#5992EC;color:#5992EC;}
        QScrollBar{background: #e1e1e1;width: 8px;}
        QScrollBar::handle:vertical {background: #999999;border-radius: 1px;}
        QScrollBar::handle:vertical:hover{background: #686868;}'''
        self.errorStyleSheetCombo = '''QComboBox { border:1px solid;border-color:red;border-radius: 10px;padding-left: 10px;}
        QComboBox QAbstractItemView{selection-background-color:#DADADA;selection-color: #000000;}
        QComboBox::drop-down{border:0px;}QComboBox::down-arrow{image:url(:/Icon/down-arrow.png);height: 15px;width: 15px;padding-left:-15px;}
        QComboBox:hover{border-color:#5992EC;color:#5992EC;}
        QScrollBar{background: #e1e1e1;width: 8px;}
        QScrollBar::handle:vertical {background: #999999;border-radius: 1px;}
        QScrollBar::handle:vertical:hover{background: #686868;
        }'''
        
        self.parent = mainDict['parent']
        self.master = mainDict['master']
        self.welcomeTextLable = mainDict['toBeFormattedLable']
        self.accountType:QtWidgets.QComboBox = mainDict['accountTypeCombo']
        self.accountName:QtWidgets.QLineEdit = mainDict['accountNameEntry']
        self.userName:QtWidgets.QLineEdit = mainDict['userNameEntry']
        self.pwd:QtWidgets.QLineEdit = mainDict['passwordEntry']
        self.get:QtWidgets.QPushButton = mainDict['storeButton']
        self.out:QtWidgets.QPushButton = mainDict['logoutButton']

        self.out.clicked.connect(lambda: self.db.cu("NU"))

    def __userName(self):
        for table in self.db.fetch():
            for row in table:
                if row == self.db.fetch_cu():
                    return self._decrypt(table[1])

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
        return self.accountType.currentText(), self.accountName.text(),  self.userName.text(), self.pwd.text()
    
    def validate(self):
        for i in [self.accountName, self.userName, self.pwd]: i.setStyleSheet(self.normalStyleSheet)
        self.accountType.setStyleSheet(self.normalStyleSheetCombo)
        if any([self.__get_inputs()[0] == '', 
                self.__get_inputs()[1] =='',
                self.__get_inputs()[2] =='',
                self.__get_inputs()[3] =='']):
            for entry in [self.accountName, self.userName, self.pwd]: 
                entry.setStyleSheet(self.errorStyleSheet)
            self.accountType.setStyleSheet(self.errorStyleSheetCombo)
            message(self.parent, 'Felids empty!','w')
        elif len(self.__get_inputs()[2]) < 5:
            message(self.parent,'User name can\'t have less than 5 characters','w')
            self.userName.setStyleSheet(self.errorStyleSheet)
        elif len(self.__get_inputs()[3]) < 8:
            message(self.parent,'Invalid Password','w')
            self.pwd.setStyleSheet(self.errorStyleSheet)
        else:
            if self._store(self.__get_inputs()):
                message(self.parent,'This account is already saved! You can edit it instade.','a')

            else:
                for entry in [self.accountName, self.userName, self.pwd]: entry.clear()
                self.accountType.setCurrentIndex(-1)
                message(self.parent,f'Your {self.__get_inputs()[0]} account has been successfully secured!','s')