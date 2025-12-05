import mysql.connector

# MySQL 연결 설정
connection = mysql.connector.connect(
    host = 'localhost', # MySQL 서버 주소
    user = "root", # 사용자 이름
    password = 'rlaekqls23', # 비밀번호
    database = "python_test" # 사용할 데이터 베이스
)

if connection.is_connected():
    print("MySQL에 성공적으로 연결되었습니다.")

connection.close()