import turtle

turtle.forward(500)
turtle.forward(-800)
turtle.speed(0)

x, y = -300, 0
Vx = 10
Vy = 50
ay = -10
dt = 0.01
for i in range(10000):
    if y>=0:
        x += Vx * dt
        y += Vy * dt + ay * dt ** 2 / 2
        Vy += ay * dt
        turtle.goto(x, y)
    if y<0:
        Vy = -Vy+0.2*Vy
        x += Vx * dt
        y += Vy * dt + ay * dt ** 2 / 2
        Vy += ay * dt



