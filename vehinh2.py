from turtle import *
color("red")
for j in range(4):
    if j % 2 == 0:
        pencolor("blue")
    else:
        pencolor("red")
    stt = j + 3
    for i in range(stt):
        forward(100)
        left(360/stt)
hideturtle()
mainloop()