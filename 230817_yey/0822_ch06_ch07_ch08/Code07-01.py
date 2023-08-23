# pip install xlrd : 터미널 창에서 설치하기
import xlrd

# 엑셀 파일 읽기, workbook 인스턴스, 메모리 임시로 저장
workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
# 엑샐의 워크시트 갯수 확인
# workbook.nsheets : 속성을 이용해서 값을 구함
sheetCount = workbook.nsheets
print('워크시트는 %d개 입니다' % (sheetCount))

# sheets() : 워크북(엑셀파일)의 워크시트(탭부분 내용) 내용을 가지고 옴
# senior / junior 두개의 워크시트가 존재
wsheetList = workbook.sheets()
print(f"워크시트의 이름 : {wsheetList}")
for worksheet in wsheetList :
    print('** 워크시트의 이름 : %s' % (worksheet.name) )
    print(" 행 수는 %d, 열 개수는 %d 입니다." % (worksheet.nrows, worksheet.ncols))
