import mysql.connector

# MySQL 연결 설정
connection = mysql.connector.connect(
    host = 'localhost', # MySQL 서버 주소
    user = "root", # 사용자 이름
    password = 'rlaekqls23', # 비밀번호
    database = "python_test" # 사용할 데이터 베이스
)

cursor = connection.cursor() # 데이터베이스 작업을 위한 커서 객체 생성

sql = "delete from users where name = %s" # 특정 이름의 사용자 삭제
values = ("Encore", )  # 값이 하나이더라도 string datatype은 들어갈 수 없다.

cursor.execute(sql, values)
connection.commit()

print(f"{cursor.rowcount}개의 행이 삭제되었습니다.")

cursor.close()
connection.close()