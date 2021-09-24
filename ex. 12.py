import turtle

turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
x = 1
while x <= 6:
    turtle.circle(-50, 180, 100)
    turtle.circle(-10, 180, 100)
    x += 1
turtle.exitonclick()
