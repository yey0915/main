# 엑셀 파일 읽어서 -> csv 출력
import xlrd
import csv

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')

wsheetList = workbook.sheets()
for worksheet in wsheetList :
    # 지정된 경로의 파일에 csv 로 쓰기 작업
    with open("C:/CookAnalysis/Excel/singer_" + worksheet.name + "0822.csv", "w", newline='') as outFp:
        # outFp : csv 파일에 쓰기위한 인스턴스
        # csv 모듈의 write함수 이용해서 쉽게 쓰기 작업
        csvWriter = csv.writer(outFp)
        # 해당 엑셀의 전체 갯수(worksheet.nrows)
        for row in range(worksheet.nrows) :
                print(f"row의 값 : {row}")
                row_list = worksheet.row_values(row)
                csvWriter.writerow(row_list)

print("Save. OK~")