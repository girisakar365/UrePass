from FrontEnd.src import *

from .Csys import Hash


class Authorize(Hash):

    def __init__(self,mainDict:dict):

        super().__init__()
        self.errorStyleSheet = 'QLineEdit{border-radius:15px;background-color:#FFFFFF;border:1px solid;border-color:red;}'
        self.normalStyleSheet = 'QLineEdit{border-radius: 15px;background-color: #FFFFFF;border: 1px solid;border-color:#EBEBEB}' 
        self.parent:QtWidgets.QMainWindow = mainDict['parent']
        self.passwordEntry:QtWidgets.QLineEdit = mainDict['passwordEntry']
        self.submitButton:QtWidgets.QPushButton = mainDict['submitButton']
        self.toBeFormattedLable:QtWidgets.QLabel = mainDict['toBeFormattedLable']

    def __getInput(self):
        return self.passwordEntry.text()
    
    def _userName(self):
        for table in self.db.fetch():
            for row in table:
                if row == self.db.fetch_cu():
                    return table[1]

    def __password(self):
        for table in self.db.fetch_user( self.db.fetch_cu() ):
            return self._decrypt(table[4])

    def formatMessageLable(self):
        userName = self._decrypt( self._userName() )
        self.toBeFormattedLable.setText(f'Hello {userName},\nPlease enter your password to verify.')
        self.toBeFormattedLable.adjustSize()

    def validate(self):
        
        self.passwordEntry.setStyleSheet(self.normalStyleSheet)
        enterdPassword = self.__getInput()

        if enterdPassword == self.__password():
            self.passwordEntry.clear() 
            return True
        
        else:
            message(self.parent,'Invalid password!', 'w')
            self.passwordEntry.clear() 
            self.passwordEntry.setStyleSheet(self.errorStyleSheet)
            return False