from random import randint
import turtle as turtle

number_of_turtles = 20
steps_of_time_number = 2000

turtle.hideturtle()
turtle.penup()
turtle.goto(-200, -200)
turtle.pendown()
for i in range(4):
    turtle.forward(400)
    turtle.left(90)

pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.shape('circle')
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.left(randint(0, 360))
    unit.shapesize(0.5)

for i in range(steps_of_time_number):
    for unit in pool:
        if unit.xcor() >= 200:
            unit.left(2 * (90 - unit.heading()))
            unit.forward(2)
        if unit.ycor() >= 200:
            unit.right(2 * unit.heading())
            unit.forward(2)
        if unit.xcor() <= -200:
            unit.right(2 * (unit.heading() - 90))
            unit.forward(2)
        if unit.ycor() <= -200:
            unit.right(2 * (unit.heading() - 180))
            unit.forward(2)
        else:
            unit.forward(2)
