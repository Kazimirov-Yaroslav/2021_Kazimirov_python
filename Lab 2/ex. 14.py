import turtle
turtle.shape('turtle')
n = int(input())
x = 1


def stars(i):
    turtle.left(180 - (180 / i))
    turtle.forward(200)


for x in range(n):
    stars(n)
turtle.exitonclick()
