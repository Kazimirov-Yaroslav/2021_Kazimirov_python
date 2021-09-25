import turtle
turtle.shape('turtle')

for i in range(1, 10):
    turtle.forward(30+20*(i-1))
    turtle.left(90)
    turtle.forward(30+20*(i-1))
    turtle.left(90)
    turtle.forward(30+20*(i-1))
    turtle.left(90)
    turtle.forward(30+20*(i-1))
    turtle.penup()
    turtle.goto(-10*i, -10*i)
    turtle.left(90)
    turtle.pendown()