import sqlite3

## 변수 선언 부분 ##
con, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row=None

## 메인 코드 부분 ##
con = sqlite3.connect("pydb0822.db")
cur = con.cursor()

cur.execute("SELECT * FROM userTable")

print("사용자ID    사용자이름    이메일            출생연도")
print("--------------------------------------------------------")

while (True) :
    # fetchone() : 한행을 불러옴
    row = cur.fetchone()
    # 한행이 없다면 반복문 종료, None(=null)
    if row == None :
        break;
    # 해당 행의 컬럼 값을 할당
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    print("%5s   %15s   %15s" % (data1, data2, data3))

con.close()
