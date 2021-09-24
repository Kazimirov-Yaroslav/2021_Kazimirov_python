import turtle
import math
turtle.shape('turtle')
turtle.goto(0.1, 0.1)
turtle.speed(0)
k=2/3600
for i in range (1, 10000):
    turtle.forward(k*math.sqrt(1+i**2))
    turtle.left(1)