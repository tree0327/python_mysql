import mysql.connector

with mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rlaekqls23",
    database = "python_test"
) as connection:
    
    with connection.cursor() as cursor:
        cursor.execute("select * from users")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
