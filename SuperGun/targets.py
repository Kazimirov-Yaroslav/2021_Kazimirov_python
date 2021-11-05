import math
import random
from random import choice, randint
import pygame
from pygame.draw import rect
from pygame.image import load
from pygame.color import update

WHITE = 0xFFFFFF


class HealTarget(pygame.sprite.Sprite):
    """
    Хилит при попадании
    """
    def move(self):
        """
        Двигается по горизонтали
        """
        pass


class Airplane(pygame.sprite.Sprite):
    """
    Кидает бомбы
    """
    def __init__(self, filename, *groups):
        super().__init__(*groups)
        self.image = load(filename)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 110
        self.rect.y = 100
        self.speed = 1
        self.rect.center = (self.rect.x, self.rect.y)
        self.t = 0

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_r(self):
        self.rect.x += 5

    def move_l(self):
        self.rect.x -= 5

    def move(self):
        if 10 <= self.rect.x <= 630 and self.speed > 0:
            self.move_r()
        if (self.rect.x > 630 or self.rect.x < 10) and self.speed > 0:
            self.image = load('airplan_l.png')
            self.image.set_colorkey(WHITE)
            self.move_l()
            self.speed = -1
        if 10 <= self.rect.x <= 630 and self.speed < 0:
            self.move_l()
        if (self.rect.x > 630 or self.rect.x < 10) and self.speed < 0:
            self.image = load('airplan_r.png')
            self.image.set_colorkey(WHITE)
            self.move_r()
            self.speed = 1
        if self.t != 20:
            self.t += 1
        else:
            self.t = 0


class Coin(pygame.sprite.Sprite):
    """
    Дает очки
    """
    def __init__(self, filename, *groups):
        super().__init__(*groups)
        self.image = load(filename)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 800)
        self.rect.y = random.randint(20, 200)
        self.rect.center = (self.rect.x, self.rect.y)
        self.radius = 25

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        pass


class Bomb(pygame.sprite.Sprite):
    """
    Наносит урон при попадании
    """
    def __init__(self, filename, x, y, FPS, *groups):
        super().__init__(*groups)
        self.g = 2
        self.image = load(filename)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vy = 0
        self.rect.center = (self.x, self.y)
        self.t = 15/FPS
        self.live = 50

    def move(self):
        """
        Падает с ускорением g
        """
        self.y += -self.vy * self.t + self.g*(self.t**2)/2
        self.vy -= self.g * self.t

    def draw(self, screen):
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.image.get_rect(center=(self.x, self.y)))
        if self.live > 0:
            self.live -= 1
        else:
            self.kill()

