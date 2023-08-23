import xlrd

# 엑셀 파일 읽기
workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
sheetCount = workbook.nsheets

# 전역 변수로 선언 및 할당
personNum = 0
personIdx = 2 # 인원 컬럼
rowCount = 0  # 집계를 위한 카운트

# 엑셀 파일의 워크시트 이름 목록
wsheetList = workbook.sheets()
# 각 워크시트의 전체 행의 갯수에서 하나 빼서,
# rowcount 집계(상태 확인.)
for worksheet in wsheetList :
    # 첫행이 컬럼 부분이라서, 빼고
    # 평균 집계 부분
    rowCount += worksheet.nrows-1
    print(f"rowCount 의 값 : {rowCount}")
    print(f"worksheet.nrows 의 값 : {worksheet.nrows}")
    # 엑셀 파일이라서 인덱스 개념이 적용이 되지 않음
    # worksheet.nrows : 각 워크시트의 전체 행의 갯수
    for row in range(1, worksheet.nrows) :
        # personNum 전역변수, cell_value 각 행X열의 원소 : 셀 위치의 값
        # 누적하는 값
        personNum +=  int(worksheet.cell_value(row, personIdx))

print("전체 가수그룹 인원 합계 : ", personNum)
print("가수그룹 인원 평균 : ", personNum/rowCount)