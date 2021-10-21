import pygame
from pygame.draw import circle
from random import randint
import random
import pygame.image


class Target(pygame.sprite.Sprite):
    def __init__(self, filename,  r=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename)
        self.image.set_colorkey((248, 248, 248, 255))
        self.rect = self.image.get_rect()
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
