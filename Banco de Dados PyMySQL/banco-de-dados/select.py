import pymysql.cursors
from connection import connectionDB

try:
    with connectionDB.cursor() as cursor:
        sql = "SELECT * FROM `users`"
        cursor.execute(sql)
        dados = cursor.fetchall()
finally:
    for dado in dados:
        print(dado['email'], dado['senha'])
    connectionDB.close()