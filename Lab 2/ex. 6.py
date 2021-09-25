import turtle
n = int(input())
turtle.shape('turtle')
turtle.speed(2)

for i in range(1, n+1):
    turtle.forward(100)
    turtle.stamp()
    turtle.back(100)
    turtle.right(360 / n)
turtle.exitonclick()