import turtle

turtle.shape('turtle')
turtle.left(90)
s = int(input())
n = 30
x = 1


def butterfly(i):
    turtle.circle(i)
    turtle.circle(-i)


for x in range(1, s):
    butterfly(n)
    n += 5
turtle.exitonclick()
