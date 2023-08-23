# csv 2갤르 하나의 csv 합치는 예제
# 이 장부터는 내장 함수를 이용해서 읽기, 쓰기 작업
import csv

with open("C:/CookAnalysis/CSV/singerA.csv", "r") as inFpA :
    with open("C:/CookAnalysis/CSV/singerB.csv", "r") as inFpB:
        with open("C:/CookAnalysis/CSV/singerSum_0822.csv", "w", newline='') as outFp:
            csvReaderA = csv.reader(inFpA)
            csvReaderB = csv.reader(inFpB)
            csvWriter = csv.writer(outFp)

            # 2개의 csv 파일의 구조가 동일해서,
            # 헤더가 동일해서, 덮어쓰기 함
            header_list = next(csvReaderA)
            header_list = next(csvReaderB)
            # csv 파일을 쓰는 작업 컬럼
            csvWriter.writerow(header_list)

            # 2행부터는 실제 데이터 값
            for row_list in csvReaderA:
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                csvWriter.writerow(row_list)

print('Save. OK~')