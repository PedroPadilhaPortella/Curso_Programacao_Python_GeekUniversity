from pymysql import cursors
import pymysql.cursors
from connection import connectionDB

try:
    with connectionDB.cursor() as cursor:
        # Create table
        sql = "CREATE TABLE IF NOT EXISTS `users` (`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY, `email` VARCHAR(100) NOT NULL, `password` VARCHAR(50) NOT NULL);"

        cursor.execute(sql)

    connectionDB.commit()
finally:
    connectionDB.close()
    print("Tabela Criada!")