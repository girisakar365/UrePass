from random import *

from cryptography.fernet import Fernet

from .DB import *

UNIQUE_CHAR = [chr(i) for i in range(33,47)] + [chr(i) for i in range(58,65)] + [chr(20)] 
NORMAL_CHAR = [chr(i) for i in range(97,123)]
CAPITAL_CHAR = [chr(i) for i in range(65,91)]
NUMBER = [chr(i) for i in range(48,58)]

def generate_pass():
    return ''.join( sample([chr(i) for i in range(33,47)] + [chr(i) for i in range(58,65)] + NORMAL_CHAR + CAPITAL_CHAR + NUMBER, k=randint(8, 12)) )

class CPH:
    def __init__(self):
        self.__con = connect('UC-410D.db')
        self.__cur = self.__con.cursor()

    def __insert_key(self,data:bytes):
        self.__cur.execute('INSERT INTO CPH VALUES (?)',[data])
        self.__con.commit()

    def key(self) -> str:
        data = self.__cur.execute('SELECT * FROM CPH')
        for k in data.fetchall(): return next(iter(k))

    def set_new_key(self):
        self.__insert_key(Fernet.generate_key())

class Hash(CPH):
    def __init__(self):
        super().__init__()

        if self.key() == None:
            self.set_new_key()
            self.__fer = Fernet( self.key() )
            
        else:
            self.__fer = Fernet( self.key() )
        
        self.db = DB()

    def _id(self):
        self.__chr = CAPITAL_CHAR + NUMBER
        shuffle(self.__chr)
        return ''.join( sample(self.__chr, k=5) )

    def _encrypt(self, data:str): return self.__fer.encrypt( bytes(data, 'utf8') )

    def _decrypt(self, cyp:bytes): return str(self.__fer.decrypt(cyp), 'utf8')