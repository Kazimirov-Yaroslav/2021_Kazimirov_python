import pygame
from pygame.draw import *
from random import randint
import random


class Target(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        r = 20
        surface = pygame.Surface((2*r, 2*r), pygame.SRCALPHA)
        circle(surface, color, (r, r), r)
        self.image = surface
        self.rect = self.image.get_rect()
        self.radius = r
        self.color = color
        self.rect.x = random.randint(100, 1140)
        self.rect.y = random.randint(100, 650)
        self.rect.center = (self.rect.x, self.rect.y)
        self.speed_y = random.randint(8, 15)
        self.speed_x = random.randint(8, 15)

    def pos_x(self):
        return self.rect.x

    def pos_y(self):
        return self.rect.y

    def center(self):
        return self.rect.center

    def radius(self):
        return self.radius

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top < 0:
            self.speed_y = -self.speed_y
        if self.rect.bottom > 700:
            self.speed_y = -self.speed_y
        if self.rect.right > 1200:
            self.speed_x = -self.speed_x
        if self.rect.left < 0:
            self.speed_x = -self.speed_x

    def color(self):
        return self.color