# 각 이미지의 RGB의 색깔을
from tkinter import *
import xlsxwriter
window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF2/picture06.gif')
h = photo.height()
w = photo.width()

# 컴프리헨션 표현, 이중 리스트 만들기.
photoR=[ [0 for _ in range(h)] for _ in range(w)]
photoG=[ [0 for _ in range(h)] for _ in range(w)]
photoB=[ [0 for _ in range(h)] for _ in range(w)]

# 이미지의 각 픽셀의 RGB 값 추출
for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k)
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

# 엑셀 파일에 해당 픽셀에, RGB 값을, 셀 속성 배경색으로 설정.
workbook = xlsxwriter.Workbook('C:/CookAnalysis/Excel/picture06_art_0822.xlsx')
# 워크시트 이름 수동. photoRGB
worksheet = workbook.add_worksheet('photoRGB')

worksheet.set_column(0, w - 1, 1.0)  # 약 0.34
for i in range(h):
    worksheet.set_row(i, 9.5)  # 약 0.35

# photoR[i][k]의 값을 HEX함수를 이용해서 16진수로 바뀜
for i in range(w) :
    for k in range(h) :
        hexR = hex(photoR[i][k])
        hexG = hex(photoG[i][k])
        hexB = hex(photoB[i][k])
        hexStr = '#'
        # 16진수 특성 상 표기
        # 0x12, 만약 예) 0x02 이런 경우 0을 추가하고,
        # 
        if len(hexR[2:]) < 2:
            hexStr += '0' + hexR[2:]
        else:
            hexStr += hexR[2:]
        if len(hexG[2:]) < 2:
            hexStr += '0' + hexG[2:]
        else:
            hexStr += hexG[2:]
        if len(hexB[2:]) < 2:
            hexStr += '0' + hexB[2:]
        else:
            hexStr += hexB[2:]

        cell_format = workbook.add_format()
        # 각셀의 배경색 지정하는 함수
        # print(f"hexStr의 값 : {hexStr}")
        cell_format.set_bg_color(hexStr)
        worksheet.write(k, i, '', cell_format)

workbook.close()
print('Save. OK~')