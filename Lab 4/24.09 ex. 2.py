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

screen = pygame.display.set_mode((600, 750))
screen.fill(BLACK)
# screen = screen.convert_alpha(screen)

# rect(screen, BLACK, (0, 300, 800, 400))
rect(screen, GREY, (0, 0, 600, 300))

scales = [(-0.2702702702702703, -0.4260869565217391), (-0.28378378378378377, -0.3391304347826087),
          (-0.3310810810810811, -0.2), (-0.3783783783783784, -0.10434782608695652),
          (-0.39864864864864863, -0.034782608695652174), (-0.4391891891891892, 0.06086956521739131),
          (-0.4797297297297297, 0.17391304347826086), (-0.5, 0.3130434782608696),
          (-0.44594594594594594, 0.34782608695652173), (-0.36486486486486486, 0.3565217391304348),
          (-0.27702702702702703, 0.3217391304347826), (-0.22972972972972974, 0.391304347826087),
          (-0.16891891891891891, 0.45217391304347826), (-0.0945945945945946, 0.4956521739130435),
          (0.006756756756756757, 0.4782608695652174), (0.033783783783783786, 0.3826086956521739),
          (0.08108108108108109, 0.3130434782608696), (0.1554054054054054, 0.3130434782608696),
          (0.27702702702702703, 0.3217391304347826), (0.40540540540540543, 0.28695652173913044),
          (0.4594594594594595, 0.2608695652173913), (0.4594594594594595, 0.22608695652173913),
          (0.49324324324324326, 0.12173913043478261), (0.4391891891891892, -0.06086956521739131),
          (0.3581081081081081, -0.1391304347826087), (0.32432432432432434, -0.1565217391304348),
          (0.25, -0.24347826086956523), (0.20270270270270271, -0.25217391304347825),
          (0.10810810810810811, -0.3130434782608696), (0.07432432432432433, -0.3739130434782609),
          (0.0472972972972973, -0.4260869565217391), (0.02702702702702703, -0.4608695652173913),
          (0.006756756756756757, -0.4956521739130435)]
eyes = [(-0.25555555555555554, -0.5222222222222223), (-0.14444444444444443, -0.5333333333333333)]


def ell(scr, c, coord, fi):
    a, b, w, h = coord
    rotated_surf = pygame.Surface((w, h))  # создаём новый холст с заданным размером, на котором будем рисовать
    rotated_surf = rotated_surf.convert_alpha(
        rotated_surf)  # convert_alpha - имба, меняет формат холста чтобы прозрачность работала корректно
    # rotated_surf.fill(pygame.Color(0, 0, 0, 0))  # ??? заливаем холст прозрачным бесцветьем (чёрный
    # бесцветный==прозрачный)
    ellipse(rotated_surf, c, (0, 0, w, h))  # рисуем нужную фигуру на нашем холсте
    rotated_surf = pygame.transform.rotate(rotated_surf, fi)  # поворачиваем весь наш холст с нарисованной на нём
    # фигуркой на заданный угол пр.ч.с.
    scr.blit(rotated_surf, (a, b))  # накладывает сверху на screen наш рисунокна холсте, левый верхний угол холста
    # попадает в указанную точку


def ghost(x1, y1, w, h, ori):
    if ori == 0:
        x_c = x1 - 20 * w / 120
        y_c = y1 - 55 * h / 120
        circle(screen, GREY, (x_c, y_c), 23 * h / 110)
        coord = []
        for a1, b1 in scales:
            coord.append((a1 * w + x1, b1 * h + y1))
        polygon(screen, GREY, coord)
        polygon(screen, GREY, coord, width=4)
        ell_s = 25
        for a1, b1 in eyes:
            circle(screen, BLUE, (a1 * w + x1, b1 * h + y1), w / 21)
            circle(screen, BLACK, (a1 * w + x1, b1 * h + y1), w / 50)
            ell(screen, WHITE, (a1 * w + x1, b1 * h + y1 - w / 30, w / ell_s, 0.35 * w / ell_s), 35)
    if ori == 1:
        x_c = x1 + 20 * w / 120
        y_c = y1 - 55 * h / 120
        circle(screen, GREY, (x_c, y_c), 23 * h / 110)
        coord = []
        for a1, b1 in scales:
            coord.append((-a1 * w + x1, b1 * h + y1))
        polygon(screen, GREY, coord)
        polygon(screen, GREY, coord, width=4)
        ell_s = 25
        for a1, b1 in eyes:
            circle(screen, BLUE, (-a1 * w + x1, b1 * h + y1), w / 21)
            circle(screen, BLACK, (-a1 * w + x1, b1 * h + y1), w / 50)
            ell(screen, WHITE, (-a1 * w + x1 - w / 50, b1 * h + y1 - w / 30, w / ell_s, 0.35 * w / ell_s), -35)


def house(x1, y1, w, h):
    rect(screen, BOL, (x1, y1, w, h))
    rect(screen, BROWN, (x1 + w / 10, y1 + h * 0.7, w / 5, h / 5))
    rect(screen, BROWN, (x1 + 4 * w / 10, y1 + h * 0.7, w / 5, h / 5))
    rect(screen, YELLOW, (x1 + 7 * w / 10, y1 + h * 0.7, w / 5, h / 5))
    for i in range(1, 5):
        rect(screen, (78, 78, 78), (x1 + 3 * i * w / 17, y1, w / 12, h / 3))
    polygon(screen, BROWN, [(x1-40, y1), (x1, y1-30), (x1+w, y1-30), (x1+w+40, y1)])
    rect(screen, BROWN, (x1-30, y1+h/2-20, 60+w, 20))
    for i in range(1, 7):
        rect(screen, BROWN, (x1 - 45+i*40, y1+h/2-40, 10, 20))
    rect(screen, BROWN, (x1 - 20, y1 + h / 2 - 40, 40 + w, 10))
    rect(screen, BLACK, (x1+40, y1-75, 15, 65))
    rect(screen, BLACK, (x1 + 20, y1 - 55, 5, 35))
    rect(screen, BLACK, (x1 + 170, y1 - 60, 10, 45))


circle(screen, WHITE, (550, 50), 50)

ell1 = pygame.Surface((350, 50))
ell1.set_colorkey(BLACK)
ell1.set_alpha(150)
ellipse(ell1, (78, 78, 78), (0, 0, 350, 50))
screen.blit(ell1, (50, 40))

ell2 = pygame.Surface((400, 50))
ell2.set_colorkey(BLACK)
ell2.set_alpha(250)
ellipse(ell2, (138, 138, 138), (0, 0, 400, 50))
screen.blit(ell2, (200, 10))

ghost(427, 654, 190, 190, 0)
house(50, 250, 200, 300)


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
