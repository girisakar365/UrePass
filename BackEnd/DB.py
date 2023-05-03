from sqlite3 import *


class DB:

    def __init__(self):
        self.__con = connect('UC-410D.db')
        self.__cur = self.__con.cursor()
        
    def initate_db(self):

        self.__cur.execute('''CREATE TABLE IF NOT EXISTS UPU(
        id TEXT NOT NULL PRIMARY KEY,
        fname TEXT NOT NULL,
        lname TEXT NOT NULL,
        userName TEXT NOT NULL,
        passWord TEXT NOT NULL)''')
        
        self.__cur.execute('''CREATE TABLE IF NOT EXISTS CU(User TEXT NOT NULL)''')
        
        self.__cur.execute('''CREATE TABLE IF NOT EXISTS CPH("#001" TEXT)''')
    
        self.__con.commit()
        
    def ins(self,data:list):
        self.__cur.execute('INSERT INTO UPU VALUES (?,?,?,?,?)',data)
        self.__con.commit()

    def ins_specific(self, id:str, data:list):
        self.__cur.execute(f'INSERT INTO "{id}" VALUES (?,?,?,?,?)',data)
        self.__con.commit()

    def fetch_user(self, id:str):
        return self.__cur.execute(f'SELECT * FROM UPU WHERE "id" = "{id}"').fetchall()

    def fetch_specific(self, id:str):
        return self.__cur.execute(f'SELECT * FROM "{id}"').fetchall()
    
    def update_cu(self,rowName, id, data):
        self.__cur.execute(f'UPDATE UPU set "{rowName}" = (?) WHERE "id" = "{id}"',[data])
        self.__con.commit()

    def cu(self,data:str):
        self.__cur.execute('UPDATE CU set "user" = (?)', [data])
        self.__con.commit()

    def fetch_cu(self) -> str:
        return next(iter( self.__cur.execute('SELECT * from CU').fetchall() ))[0] #out from tuple
    
    def fetch(self):
        data = self.__cur.execute('SELECT * FROM UPU')
        return data.fetchall()
    
    def delete(self, id):
        self.__cur.execute(f'DELETE FROM UPU WHERE id = "{id}"')
        self.__cur.execute(f'DROP TABLE {id}')
        self.__con.commit()

    def delete_specific(self, table:str, id:str):
        self.__cur.execute(f'DELETE FROM {table} WHERE id  = "{id}"')
        self.__con.commit()

    def create_table(self,id:str):
        self.__cur.execute(
        f'''CREATE TABLE IF NOT EXISTS "{id}"(
        id TEXT NOT NULL PRIMARY KEY,
        accountType TEXT NOT NULL,
        account TEXT NOT NULL,
        userName TEXT NOT NULL,
        passWord TEXT NOT NULL)''')
        self.__con.commit()