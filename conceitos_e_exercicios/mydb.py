from .manager import Manager_Db

database = Manager_Db("localhost", "root", "", "MyDb")

database.start_connection()

