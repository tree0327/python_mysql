import mysql.connector

# MySQL 연결 설정
connection = mysql.connector.connect(
    host = 'localhost', # MySQL 서버 주소
    user = "root", # 사용자 이름
    password = 'rlaekqls23', # 비밀번호
    database = "python_test" # 사용할 데이터 베이스
)

# cursor = connection.cursor() # 데이터베이스 작업을 위한 커서 객체 생성
cursor = connection.cursor(dictionary=True) # 데이터베이스 작업을 위한 커서 객체 생성

cursor.execute("SELECT * FROM USERS") # USERS 테이블 내 모든 데이터 조회

rows = cursor.fetchall() # 조회 결과를 가져온다.

for row in rows:
    print(row) # 각 행 출력

cursor.close()
connection.close()