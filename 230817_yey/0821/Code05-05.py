from tkinter import *
window = Tk()

# 버튼, 버튼 텍스트 : 텍스트, fg : foreground, command : 이벤트 핸들러
button1 = Button(window, text = "파이썬 종료", fg = "red", command = quit, width=20, height=5)

button1.pack()

window.mainloop()
