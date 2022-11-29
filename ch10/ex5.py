# 체크 박스
from tkinter import *
from tkinter import messagebox


window = Tk()


def myfunc():
    if chk.get() == 0:
        messagebox.showinfo('', '체크 버튼이 꺼졌습니다.')
    else:
        messagebox.showinfo('', '체크 버튼이 켜졌습니다.')


chk = IntVar()  # 정수 변수 선언
cb1 = Checkbutton(window, text='클릭하세요', variable=chk, command=myfunc)

cb1.pack()
window.mainloop()

