from tkinter import *
from tkinter import messagebox
window = Tk()

## 함수 선언 부분 ##
def  myFunc() :
    if chk.get() == 0 :
        print(f"chk의 값 조회 : {chk.get()}")
        messagebox.showinfo("", "체크버튼이 꺼졌어요.")
    else :
        print(f"chk의 값 조회 : {chk.get()}")
        messagebox.showinfo("", "체크버튼이 켜졌어요.")
    
## 메인 코드 부분 ##
chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()
