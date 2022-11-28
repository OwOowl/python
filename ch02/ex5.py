import turtle

myT = None

myT = turtle.Turtle()
#myT.shape("classic")
myT.shape("turtle")

for i in range(0 , 100):
    myT.forward(200)
    myT.right(90)

turtle.done()