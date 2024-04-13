import pymysql
import pymysql.cursors

class Conexao():

    cursor = pymysql.cursors

    def __init__(self):
        self.host='sql10.freesqldatabase.com' #localhost
        self.port=3306
        self.user='sql10698413' #root
        self.password='GpcJIkum5q'
        self.database='sql10698413' #mini_projeto

    def conectar(self):
        try:
            conexao = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                cursorclass=pymysql.cursors.DictCursor
            )
            return conexao
        except:
            return False

    def desconectar(self, cursor):
        try:
            cursor.close()
        except:
            return False