import pygame
from pygame.draw import *
from random import randint

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
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


score = 0



def new_ball():
    global x, y, r
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    surface_new = pygame.Surface((2*r, 2*r), pygame.SRCALPHA)
    circle(surface_new, color, (r, r), r)
    screen.blit(surface_new, (x, y))
    balls.append()


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            a, b = pygame.mouse.get_pos()
            if (a-x)**2+(b-y)**2 <= r**2:
                score += 1
                print(score)



        else:
            new_ball()
            pygame.display.update()
            screen.fill(BLACK)


pygame.quit()
