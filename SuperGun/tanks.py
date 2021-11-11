import math
import pygame
from pygame.image import load
import bullet

WHITE = 0xFFFFFF
FPS = 30


def coord(x, y, length, angel):
    """
    Функция для вычисления координаты пули при выстреле относительнодула пушки.
    """
    return x+length*math.cos(math.radians(angel)), y-length*math.sin(math.radians(angel))


class Gun(pygame.sprite.Sprite):
    """
    Класс пушки танка.
    """
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
        """
        Активация пушки.
        """
        self.f2_on = 1

    def fire2_end(self):
        """
        Выстрел пулей.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        x1, y1 = coord(self.rect.centerx, self.rect.centery, 75, self.angel)
        new_bullet = bullet.Bullet('cannon ball.png', x1, y1, FPS)
        new_bullet.vx = self.f2_power * math.cos(math.radians(self.angel))
        new_bullet.vy = self.f2_power * math.sin(math.radians(self.angel))
        self.f2_on = 0
        self.f2_power = 10
        return new_bullet

    def fix_gun(self, x, y):
        """
        Фиксация центра пушки при перемещении вместе с телом танка.
        """
        self.rect = self.image.get_rect(center=(x + 1, y - 48))

    def targetting(self, key):
        """
        В зависимости от клавиши возвращает, как поворачивать пушку или уже нельзя повернуть.
        :param key: Передает, какая клавиша нажата.
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

    def power_up(self):
        """
        Функция увеличения мощности пушки при длительном зажатии клавиши выстрела.
        """
        if self.f2_on == 1:
            if self.f2_power < 100:
                self.f2_power += 3

    def gun_turn(self, key, screen, x, y):
        """
        Функция поворота пушки при нажатии клавиши.
        :param key: Передает, какая клавиша нажата.
        :param screen: Передает поверхность, на которой происходит отрисовка пушки.
        :param x: Координаты центра пушки
        :param y: Координаты центра пушки
        """
        if self.targetting(key):
            self.image = load('vacuum gun.png')
            self.image.set_colorkey(WHITE)
            self.image = pygame.transform.rotate(self.image, self.angel)
            self.fix_gun(x, y)
            screen.blit(self.image, self.rect)


class Tank(pygame.sprite.Sprite):
    """
    Класс танка.
    """
    def __init__(self, filename, *groups):
        super().__init__(*groups)
        self.image = load(filename)
        self.rect = self.image.get_rect(center=(100, 500))
        self.live = 50
        """
        Параметры танка.
        """

        self.gun = Gun('vacuum gun.png')
        self.gun.image = pygame.transform.rotate(self.gun.image, 90)
        self.gun.fix_gun(self.rect.centerx, self.rect.centery)
        """
        Параметры пушки,котороя создается вместе с танкоми прявязана только к нему.
        """

    def get_center_x(self):
        return self.rect.centerx

    def get_center_y(self):
        return self.rect.centery

    def move_r(self):
        """
        Движение всего танка вправо.
        """
        if self.rect.right >= 800:
            return
        self.rect.x += 5
        self.gun.fix_gun(self.rect.centerx, self.rect.centery)

    def move_l(self):
        """
        Движение всего танка влево.
        """
        if self.rect.x <= 0:
            return
        self.rect.x -= 5
        self.gun.fix_gun(self.rect.centerx, self.rect.centery)

    def draw(self, screen):
        """
        Отрисовка танка.
        """
        screen.blit(self.gun.image, self.gun.rect)
        screen.blit(self.image, self.rect)
