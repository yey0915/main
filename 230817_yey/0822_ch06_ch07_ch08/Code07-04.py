import xlrd   # xlrd : 엑셀 파일 읽기 용도
# xlwt : 엑셀 파일 쓰기 용도
import xlwt

# 엑셀 파일 읽기
workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
# 엑셀 파일에 쓰기
outWorkbook = xlwt.Workbook()

# 엑셀의 워크시트 이름 목록
wsheetList = workbook.sheets()
# 워크시트에서 각 하나의 워크시트 선택
for worksheet in wsheetList :
    # 새 엑셀 파일에 -> 워크시트 이름을 추가
    outSheet = outWorkbook.add_sheet(worksheet.name)
    # 읽은 엑셀 파일의 전체 행의 갯수
    for row in range(worksheet.nrows) :
        for col in range(worksheet.ncols) :
            # 새 엑셀 파일의 새 워크시트 부분의 이름 : outSheet
            # 첫번째, 두번째 매개변수는 해당 셀의 위치이고,
            # 세번째 ㅐ매개변수는 입력 값(읽은 엑셀 파일의 내용)
            outSheet.write(row, col, worksheet.cell_value(row, col))

outWorkbook.save('c:/CookAnalysis/Excel/outSinger1_0822.xls')
print("Save. OK~")