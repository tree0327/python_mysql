# 1. 가상환경 생성 및 활성화
# 2. python_mysql % pip install mysql-connector-python
# 3. python connector.py
import mysql.connector

# MySQL 연결 설정
connection = mysql.connector.connect(
    host = 'localhost', # MySQL 서버 주소
    user = "root", # 사용자 이름
    password = 'rlaekqls23', # 비밀번호
    database = "python_test" # 사용할 데이터 베이스
)

cursor = connection.cursor() # 데이터베이스 작업을 위한 커서 객체 생성

# 데이터 삽입 쿼리 query
sql = "INSERT INTO users (name, email) values (%s, %s)" # 사용자 데이터를 추가하는 SQL 쿼리
values = ("Encore", "encore@example.com") # 값으로 사용할 데이터

cursor.execute(sql, values) # 쿼리 실행
connection.commit() # 변경사항 커밋

print(f"{cursor.rowcount}개의 행이 추가되었습니다.") # 추가된 행(row)의 수 출력

cursor.close()
connection.close()