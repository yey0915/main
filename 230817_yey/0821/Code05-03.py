from tkinter import *
#윈도우 창을 그려주는 인스턴스
window = Tk()

# 라벨이라는 클래스에서, 속성으로, text 속성을 사용하려면, 
label1 = Label(window, text = "COOKBOOK. 데이터 분석을")
label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg = "blue")
# anchor : SE(South, East) - 남동쪽
label3 = Label(window, text = "공부 중입니다.", bg = "magenta", width = 80, height = 40, anchor = SE)

# 윈도우 창에 붙이는 작업
label1.pack();
label2.pack();
label3.pack();

window.mainloop()
