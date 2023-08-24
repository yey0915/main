import csv
import time
import datetime

# csv 파일 생성 : 날짜와 시간을 추가하는 부분
csvName =  'c:/CookAnalysis/CSV/datetime.csv'
with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['연월일', '시분초'])

count = 10 # 상태변수
while count > 0 :
    count -= 1

    now = datetime.datetime.now()
    yymmdd = now.strftime('%Y-%m-%d')
    hhmmss = now.strftime('%H:%M:%S')
    time_list = [yymmdd, hhmmss]
    print(time_list)

    # 날짜, 시간을 적어주는 작업 'a' 추가
    with open(csvName, 'a', newline='') as csvFp:
        csvWriter = csv.writer(csvFp)
        csvWriter.writerow(time_list)

    time.sleep(3)
