import turtle

##ve 1 hinh binh hanh
def letdance(nm, cl, sz, quay):
    nm = turtle.Turtle()
    nm.right(90 * quay)
    nm.color(cl)
    nm.pencolor(cl)
    for i in range(2):
        nm.right(30)
        nm.forward(sz)
        nm.left(60)
        nm.forward(sz)
        nm.left(150)
    nm.hideturtle()
## ve 4 hinh binh hanh
for j in range(1,5):
    ten = 'arr' + str(j)
    letdance(ten,"red",100,j)

turtle.mainloop()


##C2 cach thong thuong
from turtle import *
pencolor ("red")
for i in range(4):
    left(30)
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
    left(120)
hideturtle
mainloop ()