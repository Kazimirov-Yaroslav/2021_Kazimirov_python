import pygame
from pygame.draw import rect, polygon, circle

pygame.init()
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (225, 225, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))

circle(screen, YELLOW, (200, 200), 150)
rect(screen, BLACK, (120, 280, 160, 20))

circle(screen, RED, (130, 160), 30)
circle(screen, BLACK, (130, 160), 15)

circle(screen, RED, (260, 160), 25)
circle(screen, BLACK, (260, 160), 15)

polygon(screen, BLACK, [[50, 60], [50, 70], [168, 153], [175, 140]])
polygon(screen, BLACK, [[350, 60], [350, 70], [232, 153], [225, 140]])

pygame.display.update()

clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
