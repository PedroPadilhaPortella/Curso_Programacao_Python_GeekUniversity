import pymysql.cursors
from connection import connectionDB

try:
    with connectionDB.cursor() as cursor:
        # Create a new record
        nome = input('Digite seu Nome: ')
        senha = input('Digite sua senha: ')
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, (nome, senha))

    connectionDB.commit()
finally:
    connectionDB.close()