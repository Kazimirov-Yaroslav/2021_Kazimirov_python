import turtle

turtle.shape('turtle')
turtle.hideturtle()
turtle.color('black')
turtle.penup()
turtle.goto(100, 0)
turtle.left(90)
turtle.pendown()
turtle.fillcolor('yellow')
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.penup()
turtle.goto(-30, 50)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.penup()
turtle.goto(60, 50)
turtle.pendown()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.penup()
turtle.goto(0, 30)
turtle.pendown()
turtle.color('black')
turtle.pensize(8)
turtle.left(180)
turtle.forward(50)
turtle.penup()
turtle.goto(70, -10)
turtle.color('red')
turtle.pendown()
turtle.circle(-70, 180, 30)
turtle.exitonclick()
