import pygame
from pygame.draw import rect, polygon, circle, ellipse

pygame.init()
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)
GREY = (168, 168, 168, 150)
BLUE = (117, 187, 253)
BROWN = (100, 25, 0)
BOL = (95, 71, 27),

screen = pygame.display.set_mode((900, 750))
screen.fill(BLACK)
# screen = screen.convert_alpha(screen)

# rect(screen, BLACK, (0, 300, 800, 400))
rect(screen, GREY, (0, 0, 900, 300))

scales = [(-0.2668918918918919, -0.4260869565217391), (-0.2804054054054054, -0.3391304347826087), (-0.32770270270270274, -0.2), (-0.375, -0.10434782608695652), (-0.3952702702702703, -0.034782608695652174), (-0.43581081081081086, 0.06086956521739131), (-0.4763513513513513, 0.17391304347826086), (-0.4966216216216216, 0.3130434782608696), (-0.44256756756756754, 0.34782608695652173), (-0.3614864864864865, 0.3565217391304348), (-0.2736486486486487, 0.3217391304347826), (-0.22635135135135137, 0.391304347826087), (-0.16554054054054054, 0.45217391304347826), (-0.09121621621621623, 0.4956521739130435), (0.010135135135135129, 0.4782608695652174), (0.03716216216216216, 0.3826086956521739), (0.08445945945945946, 0.3130434782608696), (0.15878378378378377, 0.3130434782608696), (0.2804054054054054, 0.3217391304347826), (0.40878378378378377, 0.28695652173913044), (0.46283783783783783, 0.2608695652173913), (0.46283783783783783, 0.22608695652173913), (0.4966216216216216, 0.12173913043478261), (0.44256756756756754, -0.06086956521739131), (0.3614864864864865, -0.1391304347826087), (0.32770270270270274, -0.1565217391304348), (0.2533783783783784, -0.24347826086956523), (0.20608108108108109, -0.25217391304347825), (0.11148648648648649, -0.3130434782608696), (0.0777027027027027, -0.3739130434782609), (0.05067567567567567, -0.4260869565217391), (0.0304054054054054, -0.4608695652173913), (0.010135135135135129, -0.4956521739130435)]

eyes = [(-0.25555555555555554, -0.5222222222222223), (-0.14444444444444443, -0.5333333333333333)]


def ell(st, c, coord, fi):
    a, b, w, h = coord
    rotated_surf = pygame.Surface((w, h))  # создаём новый холст с заданным размером, на котором будем рисовать
    rotated_surf = rotated_surf.convert_alpha(
        rotated_surf)  # convert_alpha - имба, меняет формат холста чтобы прозрачность работала корректно
    # rotated_surf.fill(pygame.Color(0, 0, 0, 0))  # ??? заливаем холст прозрачным бесцветьем (чёрный
    # бесцветный==прозрачный)
    ellipse(rotated_surf, c, (0, 0, w, h))  # рисуем нужную фигуру на нашем холсте
    rotated_surf = pygame.transform.rotate(rotated_surf, fi)  # поворачиваем весь наш холст с нарисованной на нём
    # фигуркой на заданный угол пр.ч.с.
    st.blit(rotated_surf, (a, b))  # накладывает сверху на screen наш рисунокна холсте, левый верхний угол холста
    # попадает в указанную точку


def ghost(st, x1, y1, w, h, ori):
    if ori == 0:
        print(ori)
        x_c = x1 - 20 * w / 120
        y_c = y1 - 55 * h / 120
        circle(st, GREY, (x_c, y_c), 23 * h / 110)
        coord = []
        for a1, b1 in scales:
            coord.append((a1 * w + x1, b1 * h + y1))
        polygon(st, GREY, coord)
        polygon(st, GREY, coord, width=4)
        ell_s = 25
        for a1, b1 in eyes:
            circle(st, BLUE, (a1 * w + x1, b1 * h + y1), w / 21)
            circle(st, BLACK, (a1 * w + x1, b1 * h + y1), w / 50)
            ell(st, WHITE, (a1 * w + x1, b1 * h + y1 - w / 30, w / ell_s, 0.35 * w / ell_s), 35)
    if ori == 1:
        x_c = x1 + 20 * w / 120
        y_c = y1 - 55 * h / 120
        circle(st, GREY, (x_c, y_c), 23 * h / 110)
        coord = []
        for a1, b1 in scales:
            coord.append((-a1 * w + x1, b1 * h + y1))
        polygon(st, GREY, coord)
        polygon(st, GREY, coord, width=4)
        ell_s = 25
        for a1, b1 in eyes:
            circle(st, BLUE, (-a1 * w + x1, b1 * h + y1), w / 21)
            circle(st, BLACK, (-a1 * w + x1, b1 * h + y1), w / 50)
            ell(st, WHITE, (-a1 * w + x1 - w / 50, b1 * h + y1 - w / 30, w / ell_s, 0.35 * w / ell_s), -35)


def house(st, x1, y1, w, h):
    rect(st, BOL, (x1, y1, w, h))
    rect(st, BROWN, (x1 + w / 10, y1 + h * 0.7, w / 5, h / 5))
    rect(st, BROWN, (x1 + 4 * w / 10, y1 + h * 0.7, w / 5, h / 5))
    rect(st, YELLOW, (x1 + 7 * w / 10, y1 + h * 0.7, w / 5, h / 5))
    for i in range(1, 5):
        rect(st, (78, 78, 78), (x1 + 3 * i * w / 17, y1, w / 12, h / 3))
    polygon(st, BROWN, [(x1-40, y1), (x1, y1-30), (x1+w, y1-30), (x1+w+40, y1)])
    rect(st, BROWN, (x1-30, y1+h/2-20, 60+w, 20))
    for i in range(1, 7):
        rect(st, BROWN, (x1 - 45+i*40, y1+h/2-40, 10, 20))
    rect(st, BROWN, (x1 - 20, y1 + h / 2 - 40, 40 + w, 10))
    rect(st, BLACK, (x1+40, y1-75, 15, 65))
    rect(st, BLACK, (x1 + 20, y1 - 55, 5, 35))
    rect(st, BLACK, (x1 + 170, y1 - 60, 10, 45))


def al(func, x1, y1, w, h, ori=None):
    # print(ori)
    st = pygame.Surface((1.5*w, 1.5*h))
    st.set_colorkey(BLACK)
    st.set_alpha(150)
    if ori is not None:
        func(st, w, h, w, h, ori=ori)
    else:
        func(st, w, h, w, h)
    screen.blit(st, (x1, y1))


circle(screen, WHITE, (850, 50), 50)

ell1 = pygame.Surface((350, 50))
ell1.set_colorkey(BLACK)
ell1.set_alpha(150)
ellipse(ell1, (78, 78, 78), (0, 0, 350, 50))
screen.blit(ell1, (250, 40))

ell2 = pygame.Surface((400, 50))
ell2.set_colorkey(BLACK)
ell2.set_alpha(250)
ellipse(ell2, (138, 138, 138), (0, 0, 400, 50))
screen.blit(ell2, (500, 10))

ell3 = pygame.Surface((400, 50))
ell3.set_colorkey(BLACK)
ell3.set_alpha(150)
ellipse(ell3, (138, 138, 138), (0, 0, 400, 50))
screen.blit(ell3, (250, 100))


ghost(screen, 727, 654, 190, 190, 0)
ghost(screen, 827, 524, 90, 90, 0)
ghost(screen, 150, 650, 90, 90, 1)
house(screen, 50, 250, 200, 300)

house(screen, 350, 200, 200, 300)
house(screen, 650, 150, 200, 300)

ell2 = pygame.Surface((400, 50))
ell2.set_colorkey(BLACK)
ell2.set_alpha(200)
ellipse(ell2, (138, 138, 138), (0, 0, 400, 50))
screen.blit(ell2, (150, 200))

al(ghost, 227, 524, 90, 90, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

