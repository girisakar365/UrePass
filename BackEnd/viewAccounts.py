from BackEnd.Csys import Hash
from FrontEnd.src import *


class viewAccounts(Hash):

    def __init__(self,mainDict):

        super().__init__()
        self.parent = mainDict['parent']
        self.master = mainDict['master']
        self.deleteButton:QtWidgets.QPushButton = mainDict['deleteButton']
        self.updateButton:QtWidgets.QPushButton = mainDict['updateButton']
        self.table:QtWidgets.QTableWidget = mainDict['table']

        self.deleteButton.clicked.connect(self.deleteData)

    def load_data(self, data:list):
        self.table.setRowCount(len(data))
        data.reverse()
        
        row = col = 0
        for outOfList in data:
            for outOfTupel in outOfList:
                
                if type(outOfTupel) == bytes:
                    self.table.setItem(row, col, QtWidgets.QTableWidgetItem(self._decrypt(outOfTupel)))
                    col += 1
            
            col = 0
            row += 1

    def deleteData(self):
        data = self.db.fetch_specific( self.db.fetch_cu() )

        if len(data) != 0:
            
            data.reverse()
            self.db.delete_specific(self.db.fetch_cu(),
                data[self.table.currentRow()][0]
            )
            self.load_data(self.db.fetch_specific( self.db.fetch_cu() ))

    def updateData(self):
        data = self.db.fetch_specific( self.db.fetch_cu() )
        data.reverse()
        
        if len(data) != 0:
            dyc_list = []
            for raw in data[self.table.currentRow()]:
                if type(raw) == bytes:
                    dyc_list.append( self._decrypt(raw))
                else:
                    dyc_list.append(raw)
            return dyc_list