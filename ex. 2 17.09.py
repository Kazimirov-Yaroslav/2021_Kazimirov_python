import turtle

a = [int(i) for i in input()]

turtle.speed(4)
turtle.left(90)
turtle.penup()
turtle.forward(200)
turtle.pendown()


def draw_1():
    turtle.right(180)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.left(135)
    turtle.forward(100*(2**(1/2)))
    turtle.right(135)
    turtle.forward(200)

    turtle.penup()
    turtle.right(180)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

    turtle.pendown()



def draw_0():
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(200)

    turtle.penup()
    turtle.right(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.pendown()




def draw_2():
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100*2**(1/2))
    turtle.left(135)
    turtle.forward(100)

    turtle.left(90)
    turtle.penup()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()

def draw_3():
    turtle.right(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(100 * 2 ** (1 / 2))
    turtle.left(135)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(100 * 2 ** (1 / 2))

    turtle.penup()
    turtle.left(135)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

    turtle.pendown()

def draw_4():
    turtle.right(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(200)
def draw_5():
    turtle.right(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
def draw_6():
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.right(135)
    turtle.forward(100 * 2 ** (1 / 2))
    turtle.left(135)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
def draw_7():
    turtle.right(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(100 * 2 ** (1 / 2))
    turtle.left(45)
    turtle.forward(100)
def draw_8():
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
def draw_9():
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(100 * 2 ** (1 / 2))
for i in range(len(a)):
    if a[i]==0:
        draw_0()
    if a[i]==1:
        draw_1()
    if a[i]==2:
        draw_2()
    if a[i]==3:
        draw_3()
    if a[i]==4:
        draw_4()
    if a[i]==5:
        draw_5()
    if a[i]==6:
        draw_6()
    if a[i]==7:
        draw_7()
    if a[i]==8:
        draw_8()
    if a[i]==9:
        draw_9()








turtle.exitonclick()