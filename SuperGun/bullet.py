import pygame
from pygame.draw import circle
from random import randint
import random
from pygame.image import load

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)


class Bullet(pygame.sprite.Sprite):
    """
    """
    def __init__(self, filename, x, y, FPS, *groups):
        super().__init__(*groups)
        self.image = load(filename)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        self.vy = random.randint(-1, 1)
        self.vx = random.randint(-1, 1)
        self.t = 0.66*FPS

    # def pos_x(self):
    #     return self.rect.x
    #
    # def pos_y(self):
    #     return self.rect.y
    #
    # def center(self):
    #     return self.rect.center
    #
    # def radius(self):
    #     return self.radius

    def draw(self):
        screen.blit(self.image, self.rect.center)

    def default_move(self):
        self.x += self.vx * self.t
        self.y += -self.vy * self.t + self.g*(self.t**2)/2
        self.vy -= self.g * self.t

    def move(self):
        """
        Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        elf.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.default_move()
        if self.y >= 500:
            self.y = 500
            self.vy = -0.6 * self.vy
            self.vx = 0.9 * self.vx
            if abs(self.vy) < 1.5:
                self.vy = 0
                self.t = 0

        if self.x >= 650:
            self.x = 650
            self.vx = -0.7 * self.vx
            self.vy = 0.9 * self.vy

    # def color(self):
    #     return self.color
