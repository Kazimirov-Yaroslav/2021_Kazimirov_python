import math
from random import choice, randint
import pygame
from pygame.draw import rect
from pygame.image import load
from pygame.color import update
import tanks


FPS = 30
RED = (255, 0, 0, 0)
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


def bullet_create(s):
    """
    Create a group of sprites of class Ball, create balls and add balls to the group of all sprites.
    :param s: numbers balls
    :type s: int
    """
    random_color = randint(0, 5)
    Ball(COLORS[random_color], all_sprites, balls)


class Game:
    def __init__(self):
        self.tank = tanks.Tank('tanks_tankGreen_body3.png')

    def mainloop(self):
        clock = pygame.time.Clock()
        finished = False

        while not finished:
            screen.fill(WHITE)
            self.tank.draw(screen)
            pygame.display.update()
            keys = pygame.key.get_pressed()

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
            # if keys[pygame.K_SPACE]:
            #     self.shoot()
            if keys[pygame.K_x]:
                self.tank.gun_turn('K_x', screen)
            if keys[pygame.K_z]:
                self.tank.gun_turn('K_z', screen)
            if keys[pygame.K_LEFT]:
                self.tank.move_l()
            if keys[pygame.K_RIGHT]:
                self.tank.move_r()

        pygame.quit()


def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game()
    game.mainloop()


if __name__ == '__main__':
    screen = None
    main()
