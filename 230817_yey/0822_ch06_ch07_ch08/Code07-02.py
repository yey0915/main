import xlrd

workbook = xlrd.open_workbook('c:/CookAnalysis/Excel/singer.xls')
sheetCount = workbook.nsheets

# 워크시트의 이름 목록
wsheetList = workbook.sheets()
# 각 워크 시트의 이름, 행, 열 조회
# 반복문으로, 읽어서, 터미널에 출력
for worksheet in wsheetList :
    print('** 워크시트의 이름 : %s' % (worksheet.name) )
    for row in range(worksheet.nrows) :
        for col in range(worksheet.ncols) :
            print("%s" % worksheet.cell_value(row, col), end = '\t')
        print()
    print()