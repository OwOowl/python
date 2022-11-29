from tkinter import *
from tkinter.simpledialog import *

window = Tk()
window.geometry('400x400')

label = Label(window, text='입력된 값 : ')
value = askinteger('숫자 놀이', '주사위 숫자(1~6)를 입력하세요', minvalue=1, maxvalue=6)
label.configure(text=value)


label.pack()

window.mainloop()
