'''
title : 거북이 글자 쓰기
filename : ex4.py
author : minho
date : 2022.11.28
'''
import math
import turtle
import random
from tkinter.simpledialog import *

# 전역 변수
inStr = ''
swidth, sheight = 300, 300
tx, ty, txtSize = [0] * 3

turtle.title('거북이 글자 쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.pensize()

inStr = askstring('문자열 입력', '거북이 쓸 문자열 입력')

for ch in inStr:
    tx = random.randrange(-swidth/2, swidth/2)
    ty = random.randrange(-sheight/2, sheight/2)
    r = random.random()
    g = random.random()
    b = random.random()
    txtSize = random.randrange(10, 50)

    turtle.goto(tx, ty)
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))


turtle.done()
