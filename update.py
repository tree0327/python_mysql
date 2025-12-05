import mysql.connector

# MySQL 연결 설정
connection = mysql.connector.connect(
    host = 'localhost', # MySQL 서버 주소
    user = "root", # 사용자 이름
    password = 'rlaekqls23', # 비밀번호
    database = "python_test" # 사용할 데이터 베이스
)

cursor = connection.cursor() # 데이터베이스 작업을 위한 커서 객체 생성

sql = "update users set email = %s WHERE name = %s" # 이름을 받아 이메일을 업데이트
values = ("new_encore@example.com", "Encore") # 업데이트할 데이터 값

cursor.execute(sql, values) # 쿼리 실행
connection.commit() # 변경 사항 저장

print(f'{cursor.rowcount}개의 행이 업데이트 되었습니다.') # 업데이트한 행 수 출력

cursor.close()
connection.close()

