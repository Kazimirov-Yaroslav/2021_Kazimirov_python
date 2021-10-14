from typing import List

import pygame
from pygame.draw import circle
from random import randint
import random
from ball import Ball
from superball import Superball
from operator import itemgetter

pygame.init()

FPS = 60
screen = pygame.display.set_mode((1200, 700))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0
all_sprites = pygame.sprite.Group()
balls = pygame.sprite.Group()
for i in range(6):
    b = Ball(COLORS[i])
    all_sprites.add(b)
    balls.add(b)
for i in range(2):
    hard = Superball(BLACK)
    all_sprites.add(hard)
    balls.add(hard)

clock = pygame.time.Clock()
finished = False

f1 = pygame.font.Font(None, 36)
text1 = f1.render('Очки:', True, 'white')
text3 = f1.render('Введите своё имя:', True, 'white')
input_box = pygame.Rect(100, 100, 140, 32)

pygame.display.update()

count = 0
frames_count = [0, 40, 80]
active = False
done = False

points = []
table = open('table', 'w')

font = pygame.font.Font(None, 32)
input_box = pygame.Rect(100, 100, 140, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color1 = color_inactive
active = False
text = ''
done = False
while (not finished) and (done == False):
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
                    screen.fill(BLACK)
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode

    screen.fill((0, 0, 0))
    txt_surface = font.render(text, True, color1)
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color1, input_box, 2)
    screen.blit(text3, (50, 70))

    pygame.display.flip()
    clock.tick(30)

while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open('Results', 'a') as output:
                print(text, '"', str(score), file=output)
            with open('Results', 'r') as f:
                for string in range(0, 1000, 1):
                    stroka = f.readline()
                    if stroka != '':
                        pairs = stroka.split('" ')
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
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            for sprite in balls:
                a, b = pygame.mouse.get_pos()
                x, y = sprite.rect.center
                r = sprite.radius
                if (a - x) ** 2 + (b - y) ** 2 <= r ** 2 and type(sprite) == Superball:
                    score += 5
                    print(score)
                    sprite.kill()
                    b = Superball(BLACK)
                    all_sprites.add(b)
                    balls.add(b)
                elif (a - x) ** 2 + (b - y) ** 2 <= r ** 2 and type(sprite) == Ball:
                    score += 1
                    print(score)
                    color = sprite.color
                    sprite.kill()
                    b = Ball(color)
                    all_sprites.add(b)
                    balls.add(b)

    all_sprites.update()
    # Рендеринг
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
