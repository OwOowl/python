import turtle
from myTurtle import *

# 전역 변수
inStr = ''
swidth, sheight = 300, 300
tx, ty, tAngle, txtSize = [0] * 4

turtle.title('거북이 글자 쓰기(모듈 버전)')
turtle.shape('turtle')
turtle.setup(width=swidth + 50, height=sheight + 50)
turtle.screensize(swidth, sheight)
turtle.pensize()
turtle.penup()
turtle.speed(5)

inStr = getString()

for ch in inStr:
    tx, ty, tAngle, txtSize = getXYAS(swidth, sheight)
    r, g, b = getRGB()

    turtle.goto(tx, ty)
    turtle.left(tAngle)
    turtle.pencolor((r, g, b))
    turtle.write(ch, font=('맑은고딕', txtSize, 'bold'))

turtle.done()

