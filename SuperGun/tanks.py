import math
from random import choice, randint
import pygame
from pygame.draw import rect
from pygame.image import load
from pygame.color import update
import bullet

WHITE = 0xFFFFFF
FPS = 30


def coord(x, y, l, angel):
    return x+l*math.cos(math.radians(angel)), y-l*math.sin(math.radians(angel))


class Gun(pygame.sprite.Sprite):
    def __init__(self, filename):
        """
        """
        self.f2_power = 10
        self.f2_on = 0
        self.angel = 90
        self.gun_image = load(filename)
        self.image = self.gun_image
        self.rect = self.image.get_rect()
        self.angel_bul = 0

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self):
        """
        Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        x1, y1 = coord(self.rect.center[0], self.rect.center[1], 75, self.angel)
        new_bullet = bullet.Bullet('cannon ball.png', x1, y1, FPS)
        new_bullet.vx = self.f2_power * math.cos(math.radians(self.angel))
        new_bullet.vy = self.f2_power * math.sin(math.radians(self.angel))
        self.f2_on = 0
        self.f2_power = 10
        return new_bullet

    def targetting(self, key):
        """
        Прицеливание.
        """
        if 0 < self.angel < 180:
            if key == 'K_z':
                self.angel += 5
            if key == 'K_x':
                self.angel -= 5
            return True
        elif self.angel == 180:
            if key == 'K_x':
                self.angel -= 5
            return True
        elif self.angel == 0:
            if key == 'K_z':
                self.angel += 5
            return True

        # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on == 1:
            if self.f2_power < 100:
                self.f2_power += 3

    def gun_turn(self, key, screen, x, y):
        if self.targetting(key):
            self.image = load('vacuum gun.png')
            self.image.set_colorkey(WHITE)
            self.image = pygame.transform.rotate(self.image, self.angel)
            self.rect = self.image.get_rect(center=(x+85, y+5))
            screen.blit(self.image, self.rect)


class Tank(pygame.sprite.Sprite):
    def __init__(self, filename, *groups):
        super().__init__(*groups)
        self.image = load(filename)
        self.x = 100
        self.y = 500
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.live = 50

        self.gun = Gun('vacuum gun.png')
        self.gun.image = pygame.transform.rotate(self.gun.image, 90)
        self.gun.rect = self.gun.image.get_rect(center=(self.x+85, self.y+5))

    def move_r(self):
        self.x += 5
        self.gun.rect = self.gun.image.get_rect(center=(self.x + 85, self.y + 5))

    def move_l(self):
        self.x -= 5
        self.gun.rect = self.gun.image.get_rect(center=(self.x + 85, self.y + 5))

    def draw(self, screen):
        self.rect = self.image.get_rect(center=(self.x, self.y))
        screen.blit(self.gun.image, self.gun.image.get_rect(center=(self.x+85, self.y+5)))
        screen.blit(self.image, (self.x, self.y))


