from tkinter import *

window = Tk()

# 메뉴 부분 구성, 상위 메뉴
# 메인 메뉴의 부몬 창 -> window
mainMenu = Menu(window)
# 틀린 부분, 메인 메뉴는 하나만 있고, 하위 메뉴는 부모 메뉴에 붙이면 된다
# mainMenu2 = Menu(window)
window.config(menu = mainMenu)
# window.config(menu = mainMenu2)

'''파일 메뉴의 부모 창 -> 메인 메뉴'''
fileMenu = Menu(mainMenu)
# fileMenu2 = Menu(mainMenu2) <- 틀린 부분
fileMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
mainMenu.add_cascade(label = "파일2", menu = fileMenu2)


fileMenu.add_command(label = "열기")
fileMenu.add_separator()
fileMenu.add_command(label = "종료")

fileMenu2.add_command(label = "열기2")
fileMenu2.add_separator()
fileMenu2.add_command(label = "종료2", command=quit)

window.mainloop()
