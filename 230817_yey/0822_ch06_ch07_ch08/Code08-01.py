# SQLite 데이터베이스에 스키마 생성, 테이블 생성해서.
# 파이썬 버전으로 접근해서, 데이터 게터/세터
# 크롤링 한 데이터를, 임시 메모리 저장 -> 해다아 디비 쓰기 작업
# 특정 시간 마다, 입력이 되게끔 설정.
# 1) cmd -> 스키마 생성 및 테이블 생성, crud
# 2) DB Browser for SQLite(워크밴치) : GUI로 간단히
# sqlite 설치한 폴더 : c 드라이브 밑으로 이동 
import sqlite3

con = sqlite3.connect("C:/CookAnalysis/naverDB")
cur = con.cursor() # 해당 데이터베이스에서 cursor (특정 테이블에 접근하기 위한 도구.)

# 터미널에서 입력 받은 데이터를, 테이블에서 저장하는 부분
while (True) :
    data1 = input("사용자ID ==> ")
    if data1 == "" :
        break;
    data2 = input("사용자이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "','" + data2 + "','" + data3 + "', " + data4 + ")"
    # sql 문장을 cur (커서로)  C(insert)
    cur.execute(sql)
    
con.commit()
con.close()
