from lec08_database import oracle_config as cfg
import cx_Oracle
"""
ex02_select.py
Oracle 데이터베이스 서버에서 select 구문 실행, 결과 확인
"""

# 데이터베이스 서버와 연결 설정 - 접속(로그인)
connection = cx_Oracle.connect(cfg.user, cfg.pwd, cfg.dsn)

# 접속한 데이터베이스 버전 정보
print('DB version:', connection.version)


# SQL 문장을 실행시키기 위해서 cursor 객체를 생성
cursor = connection.cursor()

# SQL 문장 실행
cursor.execute('select * from emp')  # 끝에 세미콜론(;) 을 붙이면 안됨
# while True:
#     row = cursor.fetchone()
#     if row is None: # select의 결과가 더 이상 없다면
#         break
#     else:
#         print(row)

row = cursor.fetchone()
while row: # 읽은 행(row)의 데이터가 있는 동안에
    print(row) # 각 행의 데이터 tuple을 출력한다
    row = cursor.fetchone() # select의 결과에서 한 행(row)의 데이터를 읽는다

# cursor 객체 사용 후 리소스 반환
cursor.close()





# 데이터베이스 서버 연결 종료
connection.close()