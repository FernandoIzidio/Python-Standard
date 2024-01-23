"""
SQLite é uma base de dados relacional que suporta as operações ACID(Atomicidade, consistência, isolamento, durabilidade),
a principal caracteristica do sqlite é que é uma base de dados aclopada na aplicação, oque evita ter uma base de dados externa se tornando ótima para aplicações moveis, e para desenvolvimento em dispositivos limitados

INSERT INTO Table(name, city) VALUES (?, ?) -
? - delimita um valor a ser inserido na consulta, ou seja habilita consulta parametrizada
em alguns outros sgbds o delimitador é %s

conn  = sqlite.connect(file.sqlite3) - Abre uma conexão com um servidor sqlite3
cursor = conn.cursor() - Retorna um cursor para manipular banco de dados

cursor.execute(query, parameters) - Executa uma query SQL no DB

conn.commit() - Confirma as alterações no db
cursor.close() - fecha o cursor
conn.close() - Fecha a conexão

INTEGER - inteiro no SQLITE
TEXT - utilizado para char e varchar

cursor.executemany(query, parameters) - Executa varias vezes a mesma query, baseado no número de parameters fornecidos

cursor.fechtone() - Recupera uma linha capturada por select
cursor.fechtall() - Recupera todas as linhas, capturadas por select

"""
import sqlite, faker




class Context_SQLite:
    """
    Context manager for managing a SQLite connection.

    Parameters
    ----------
    dbpath : str
        Path to the SQLite database file.

    Examples
    --------
    >>> with Context_SQLite("mydatabase.db") as conn:
    ...     cursor = conn.cursor()
    ...     cursor.execute("SELECT * FROM mytable")
    ...     results = cursor.fetchall()
    >>>
    """

    def __init__(self, dbpath):
        self.dbpath = dbpath

    def __enter__(self):
        self.conn = sqlite.connect(self.dbpath)
        return self.conn

    def __exit__(self, class_error, obj_error, error_tb):
        self.conn.close()


with Context_SQLite("./db_sql.sqlite3") as conn:
    cursor = conn.cursor()
    cursor.execute("select ")

    cursor.close()


