from tkinter import *

window = Tk()
window.geometry('200x200')

button1 = Button(window, text='버튼1')
button2 = Button(window, text='버튼2')
button3 = Button(window, text='버튼3')

# 왼쪽부터 정렬
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)

window.mainloop()
