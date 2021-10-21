
import pygame
from random import randint
from ball import Ball
from superball import Superball
from operator import itemgetter
from pygame.image import load
from target import Target

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 700))
background = load('XXXL.jpg')

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

score = 0
wizard = pygame.image.load('C__fakepath_400px-Колдунов_Леонид_Модестович.png')
wizard.set_colorkey((255, 255, 255))


def tables(file1, file2, text):
    points = []
    table = open(file2, 'w')
    with open(file1, 'a') as output:
        print(text, '"', str(score), file=output)
    with open(file1, 'r') as f:
        for string in range(0, 1000, 1):
            line = f.readline()
            if line != '':
                pairs = line.split('" ')
                points.append(pairs)
                a = points[string][1]
                a.rstrip('\n')
                a = int(a)
                points[string][1] = a
    new_list = sorted(points, key=itemgetter(1))
    new_list.reverse()
    print('ТАБЛИЦА ЛИДЕРОВ', file=table)
    for i in range(0, len(new_list), 1):
        new_list[i][1] = str(new_list[i][1])
        print(''.join(new_list[i]), file=table)
    table.close()


all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
amogus = pygame.sprite.Group()
for i in range(6):
    b = Ball(COLORS[i])
    all_sprites.add(b)
    balls.add(b)
for i in range(2):
    hard = Superball(BLACK)
    all_sprites.add(hard)
    balls.add(hard)
for i in range(3):
    a = Target('1602273595_7.png')
    all_sprites.add(a)
    amogus.add(a)

clock = pygame.time.Clock()
finished = False

f1 = pygame.font.Font(None, 36)
f2 = pygame.font.Font(None, 100)
text3 = f1.render('Введите своё имя:', True, WHITE)
text_final = f1.render('GAME OVER', True, RED)
input_box = pygame.Rect(100, 100, 140, 32)

count = 0
frames_count = [0, 40, 80]


font = pygame.font.Font(None, 32)

color_inactive = LIGHT_BLUE
color_active = DODGER_BLUE
color1 = color_inactive
active = False
text = ''
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
    txt_surface = font.render(text, True, color1)
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
                    color = sprite.color
                    sprite.kill()
                    b = Ball(color)
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
