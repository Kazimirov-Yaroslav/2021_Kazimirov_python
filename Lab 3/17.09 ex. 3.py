import turtle

s = 60
a = [int(i) for i in input()]
turtle.shape('turtle')


inp = open('17.09 ex. 3.txt', 'r')
s = inp.read()
nums = eval(s)
for i in range(len(nums)):
    for j in range(len(nums[i])):
        for k in range(len(nums[i][j])):
            for g in range(len(nums[i][j][k])):
                nums[i][j][k][g] = float(nums[i][j][k][g])






turtle.speed(1)


def draw_alg(alg):
    for v in alg:
        turtle.right(v[1])
        turtle.forward(v[0] * 60)


def dram_num(code):
    turtle.penup()
    draw_alg(code[0])
    turtle.pendown()
    draw_alg(code[1])
    turtle.penup()
    draw_alg(code[2])


turtle.penup()
turtle.forward(-300)

for i in a:
    dram_num(nums[i])
    turtle.forward(60)

# dram_num(nums[a])

turtle.exitonclick()
