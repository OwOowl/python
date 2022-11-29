from tkinter import *
from tkinter import messagebox


def myfunc():
    messagebox.showinfo('강아지 버튼', '강아지가 귀엽죠? ^^')


window = Tk()

photo = PhotoImage(file='GIF/dog2.gif')
button1 = Button(window, image=photo, command=myfunc())

button1.pack()
window.mainloop()
