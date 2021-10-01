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
BOL = (95, 71, 27)

GHOST_LINE = [(-0.267, -0.426), (-0.280, -0.339), (-0.328, -0.2), (-0.375, -0.104), (-0.395, -0.0348), (-0.436, 0.061),
              (-0.476, 0.174), (-0.497, 0.313), (-0.443, 0.348), (-0.361, 0.357), (-0.274, 0.322), (-0.226, 0.391),
              (-0.166, 0.452), (-0.091, 0.496), (0.01, 0.478), (0.037, 0.383), (0.084, 0.313), (0.159, 0.313),
              (0.280, 0.322), (0.409, 0.287), (0.463, 0.261), (0.463, 0.226), (0.497, 0.122), (0.443, -0.061),
              (0.361, -0.139), (0.328, -0.157), (0.253, -0.243), (0.206, -0.252), (0.111, -0.313), (0.078, -0.374),
              (0.051, -0.426), (0.03, -0.461), (0.01, -0.496)]

EYES = [(-0.256, -0.522), (-0.144, -0.533)]

screen = pygame.display.set_mode((900, 750))
screen.fill(BLACK)
rect(screen, GREY, (0, 0, 900, 300))


def cloud(coord, color, transparency):
    """
    Создаёт облако
    :param coord: массив, содержащий геометрические параметры объекта: координаты левого верхнего угла и размеры
    :param color: 2вет, заданный в формате, подходящем для pygame.Color
    :param transparency: прозрачность от 0 до 255(0 - полностью прозрачное, 255 - полностью непрозрачное)
    """
    x, y, width, high = coord
    surf = pygame.Surface((width, high))
    surf.set_colorkey(BLACK)
    surf.set_alpha(transparency)
    ellipse(surf, color, (0, 0, width, high))
    screen.blit(surf, (x, y))


def flare(surface, coord, angle):
    """
    Функция, создающая блик в галзу
    :param coord: координата блика
    :param angle: угол поворота блика против часовой стрелки
    :param surface: полотно, на которое помещается блик глаза
    """
    x, y, width, high = coord
    rotated_surf = pygame.Surface((width, high))
    rotated_surf = rotated_surf.convert_alpha(rotated_surf)
    ellipse(rotated_surf, WHITE, (0, 0, width, high))
    rotated_surf = pygame.transform.rotate(rotated_surf, angle)
    surface.blit(rotated_surf, (x, y))


def ghost(coord, orientation, transparency=150):
    """
    Рисует приведение
    :param coord: массив, содержащий геометрические параметры объекта: координаты левого верхнего угла и размеры
    :param orientation: ориентация. 1, если налево, -1, если направо
    :param transparency: transparency: прозрачность от 0 до 255(0 - полностью прозрачное, 255 - полностью непрозрачное)
    :return:
    """
    x, y, width, high = coord
    surf = pygame.Surface((width, high * 1.17))
    surf.set_colorkey(BLACK)
    surf.set_alpha(transparency)
    x_c = width / 3
    y_c = 23 / 110 * high
    # Прорисовка головы
    circle(surf, GREY, (x_c, y_c), 23 * high / 110)
    # Прорисовка тела
    coord = [(i[0] * width + 0.5 * width, i[1] * high + 0.67 * high) for i in GHOST_LINE]
    polygon(surf, GREY, coord)
    polygon(surf, GREY, coord, width=4)
    # Прорисовка глаз
    for a1, b1 in EYES:
        circle(surf, BLUE, (a1 * width + 0.5 * width, b1 * high + 0.67 * high), width / 21)
        circle(surf, BLACK, (a1 * width + 0.5 * width, b1 * high + 0.67 * high), width / 50)
        flare(surf, (a1 * width + 0.5 * width, b1 * high + 0.67 * high - width / 30, width / 25, 0.35 * width / 25), 35)
    screen.blit(surf if orientation == 1
                else pygame.transform.flip(surf, True, False), (x - 0.5 * width, y - 0.67 * high))


def house(x, y, width, high):
    """
    Функция рисует дом
    :param x:
    :param y:
    :param width:
    :param high:
    :return:
    """
    rect(screen, BOL, (x, y, width, high))
    rect(screen, BROWN, (x + width / 10, y + high * 0.7, width / 5, high / 5))
    rect(screen, BROWN, (x + 4 * width / 10, y + high * 0.7, width / 5, high / 5))
    rect(screen, YELLOW, (x + 7 * width / 10, y + high * 0.7, width / 5, high / 5))
    for i in range(1, 5):
        rect(screen, (78, 78, 78), (x + 3 * i * width / 17, y, width / 12, high / 3))
    polygon(screen, BROWN, [(x - 40, y), (x, y - 30), (x + width, y - 30), (x + width + 40, y)])
    rect(screen, BROWN, (x - 30, y + high / 2 - 20, 60 + width, 20))
    for i in range(1, 7):
        rect(screen, BROWN, (x - 45 + i * 40, y + high / 2 - 40, 10, 20))
    rect(screen, BROWN, (x - 20, y + high / 2 - 40, 40 + width, 10))
    rect(screen, BLACK, (x + 40, y - 75, 15, 65))
    rect(screen, BLACK, (x + 20, y - 55, 5, 35))
    rect(screen, BLACK, (x + 170, y - 60, 10, 45))


def sky():
    """
    Функция сооздаёт небо
    """
    circle(screen, WHITE, (850, 50), 50)

    cloud((240, 40, 350, 50), (78, 78, 78), 150)
    cloud((500, 10, 400, 50), (138, 138, 138), 250)
    cloud((250, 100, 400, 50), (138, 138, 138), 150)
    cloud((150, 200, 350, 50), (78, 78, 78), 200)


def draw():
    house(50, 250, 200, 300)
    house(350, 200, 200, 300)
    house(650, 150, 200, 300)

    ghost((727, 604, 190, 190), 1)
    ghost((827, 574, 90, 90), 1)
    ghost((150, 650, 90, 90), -1)
    ghost((227, 524, 90, 90), -1)

    sky()


draw()

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
