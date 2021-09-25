import turtle

turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
x = 1
for x in range(1, 5):
    turtle.circle(-50, 180, 100)
    turtle.circle(-10, 180, 100)
turtle.exitonclick()
