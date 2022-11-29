# 라디오 버튼
from tkinter import *


window = Tk()


def myfunc():
    if var.get() == 1:
        label1.configure(text='파이썬')
    elif var.get() == 2:
        label1.configure(text='C++')
    elif var.get() == 3:
        label1.configure(text='Java')


var = IntVar()
rb1 = Radiobutton(window, text='파이썬', variable=var, value=1, command=myfunc)
rb2 = Radiobutton(window, text='C++', variable=var, value=2, command=myfunc)
rb3 = Radiobutton(window, text='Java', variable=var, value=3, command=myfunc)
label1 = Label(window, text='선택한 언어', fg='red')

label1.pack()
rb1.pack()
rb2.pack()
rb3.pack()

window.mainloop()
