import pygame
from ball import Ball
from superball import Superball
from operator import itemgetter
from pygame.image import load
from target import Target
from random import randint
"""
Import classes and libraries.
"""
pygame.init()


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHT_BLUE = (175, 238, 238)
DODGER_BLUE = (30, 144, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
"""
Array of colors of the Balls class. 
"""


def balls_create(s):
    """
    Create a group of sprites of class Ball, create balls and add balls to the group of all sprites.
    :param s: numbers balls
    :type s: int
    """
    for c in range(s):
        random_color = randint(0, 5)
        ball = Ball(COLORS[random_color])
        all_sprites.add(ball)
        balls.add(ball)


def superballs_create(s):
    """
    Create a group of sprites of class Superball, create superballs and add superballs to the group of all sprites.
    :param s: numbers superballs
    :type s: int
    """
    for c in range(s):
        superball = Superball(BLACK)
        all_sprites.add(superball)
        balls.add(superball)


def target_create(s):
    """
    Create a group of sprites of class Target, create targets and add targets to the group of all sprites.
    :param s: numbers targets
    :type s: int
    """
    for c in range(s):
        target = Target('1602273595_7.png')
        all_sprites.add(target)
        amogus.add(target)


def tables(file1, file2, name_player):
    """
    Saving the result to file2, file1 is used as a draft.
    :param name_player: name player
    :param file1: draft
    :param file2: original
    """
    points = []
    table = open(file2, 'w')
    with open(file1, 'a') as output:
        print(name_player, '"', str(score), file=output)
    with open(file1, 'r') as f:
        for string in range(0, 1000, 1):
            line = f.readline()
            if line != '':
                pairs = line.split('" ')
                points.append(pairs)
                element = points[string][1]
                element.rstrip('\n')
                element = int(element)
                points[string][1] = element
    new_list = sorted(points, key=itemgetter(1))
    new_list.reverse()
    print('ТАБЛИЦА ЛИДЕРОВ', file=table)
    for i in range(0, len(new_list), 1):
        new_list[i][1] = str(new_list[i][1])
        print(''.join(new_list[i]), file=table)
    table.close()


FPS = 60
score = 0
text = ''

screen = pygame.display.set_mode((1200, 700))
background = load('XXXL.jpg')
wizard = load('C__fakepath_400px-Колдунов_Леонид_Модестович.png')
wizard.set_colorkey((255, 255, 255))

f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 100)

all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
amogus = pygame.sprite.Group()

balls_create(6)
superballs_create(3)
target_create(3)
clock = pygame.time.Clock()

finished = False
active = False
done = False

input_box = pygame.Rect(100, 100, 140, 32)
text3 = f1.render('Введите своё имя:', True, WHITE)
color_inactive = LIGHT_BLUE
color_active = DODGER_BLUE
color1 = color_inactive

finished = False
active = False
done = False

while not finished and not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color1 = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    done = True
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
    screen.fill(BLACK)
    txt_surface = f1.render(text, True, color1)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color1, input_box, 2)
    screen.blit(text3, (50, 70))

    pygame.display.flip()
    clock.tick(30)

done = False
while not finished and not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tables('Results', 'table', text)
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in balls:
                a, b = pygame.mouse.get_pos()
                x, y = sprite.rect.center
                r = sprite.radius
                if (a - x) ** 2 + (b - y) ** 2 <= r ** 2 and type(sprite) == Superball:
                    score += 8
                    print(score)
                    sprite.kill()
                    b = Superball(BLACK)
                    all_sprites.add(b)
                    balls.add(b)
                elif (a - x) ** 2 + (b - y) ** 2 <= r ** 2 and type(sprite) == Ball:
                    score += 2
                    print(score)
                    sprite.kill()
                    random_colors = randint(0, 5)
                    b = Ball(COLORS[random_colors])
                    all_sprites.add(b)
                    balls.add(b)
            for sprite in amogus:
                a, b = pygame.mouse.get_pos()
                x, y = sprite.rect.center
                if sprite.rect.collidepoint((a, b)) and type(sprite) == Target:
                    score += 15
                    print(score)
                    sprite.kill()
                    a = Target('1602273595_7.png')
                    all_sprites.add(a)
                    amogus.add(a)

    all_sprites.update()
    # Рендеринг
    screen.fill((255, 255, 255))
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    text2 = f1.render('Очки: ' + str(score), True, BLACK)

    screen.blit(text2, (10, 10))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    clock.tick(FPS)
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    screen.fill((255, 255, 255, 255))
    screen.blit(background, (0, 0))
    screen.blit(wizard, (500, 300))
    text2 = f2.render('ИДИ БОТАЙ', True, RED)
    screen.blit(text2, (100, 100))
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
pygame.quit()
