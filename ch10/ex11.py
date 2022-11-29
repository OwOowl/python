from tkinter import *
from tkinter import messagebox

window = Tk()



def clickLeft(event):
    messagebox.showinfo('마우스', '마우스 왼쪽 버튼이 클릭됨')


# window.bind('<Button-1>', clickLeft)  # 마우스 왼쪽
# window.bind('<Button-2>', clickLeft)  # 마우스 휠버튼
# window.bind('<Button-3>', clickLeft)    # 마우스 오른쪽
window.bind('<Button>', clickLeft)  # 1~3 모두

window.mainloop()
