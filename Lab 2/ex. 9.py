import turtle
import math


turtle.shape('turtle')
R = 40
n = 3
x = 1
turtle.penup()
turtle.goto(R, 0)
turtle.pendown()


def polygon(i):
    while i <= n:
        turtle.left((180 - 360 / n) / 2)
        turtle.left(360 / n)
        turtle.forward(2 * R * math.sin(math.pi / n))
        i += 1
        turtle.right((180 - 360 / n) / 2)


for n in range(3, 11):
    polygon(x)
    R += 21
    turtle.penup()
    turtle.goto(R, 0)
    turtle.pendown()
turtle.exitonclick()
