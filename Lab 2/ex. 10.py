import turtle

turtle.shape('turtle')

n = int(input())
x = 1


def flower(i):
    while i <= n:
        turtle.circle(50)
        turtle.left(360 / n)
        i += 1


flower(x)
turtle.exitonclick()
