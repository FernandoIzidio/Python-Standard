import mysql.connector
from json import dumps
class Manager_Db:
    def __init__(self, host, user, passwd, db) -> None:
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = db
    
    def start_connection(self):
        self.dbconnection = mysql.connector.connect(host=self.host, user=self.user, password=self.passwd, database=self.database)
        self.cursor = self.dbconnection.cursor()


    def createtable(self, tbname:str, colunms: list, types: list, **constraints):
        if len(colunms) == len(types):
            prompt = f"CREATE TABLE {tbname}" + dumps([f"{coluna} {types[pos]}" if coluna not in constraints.keys() else f"{coluna} {types[pos]} {constraints.get(coluna)}" for pos, coluna in enumerate(colunms)]).replace('[', '(').replace(']', ', created_at date default CURRENT_TIMESTAMP, update_at date default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP);').replace('"', '')
            
            self.cursor.execute(prompt)
       

            self.dbconnection.commit()
            self.dbconnection.close()
        else:
            raise Exception("Error: colunms and values doesn't match")

database = Manager_Db("localhost", "root", "", "mydb")

database.start_connection()

database.createtable('Person', ['id_person', 'name', 'age', 'gender', 'birthday', 'cpf'], ['int', 'varchar(100)', "int", "varchar(50)", "date", 'char(11)'], id_person="auto_increment primary key")

