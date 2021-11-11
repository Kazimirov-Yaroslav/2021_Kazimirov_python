import pygame
from pygame.image import load
from random import randint

WHITE = 0xFFFFFF


class Airplane(pygame.sprite.Sprite):
    """
    Класс самолета, который скидывает бомбы.
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
        """
        Отрисовка самолета.
        :param screen: Передает поверхность, на которой происходит отрисовка самолета.
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move_r(self):
        """
        Автоматическое движение самолета вправо.
        """
        self.rect.x += 5

    def move_l(self):
        """
        Автоматическое движение самолета влево.
        """
        self.rect.x -= 5

    def move(self):
        """
        Движение самолета с ограничениями на размер окна.
        """
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
    Дает очки при уничтожении.
    """
    def __init__(self, filename, *groups):
        super().__init__(*groups)
        self.image = load(filename)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = randint(50, 800)
        self.rect.y = randint(20, 200)
        self.rect.center = (self.rect.x, self.rect.y)
        self.radius = 25

    def draw(self, screen):
        """
        Отрисовка монеты.
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))


class Bomb(pygame.sprite.Sprite):
    """
    Наносит урон при попадании. Вылетает из  самолета через определенные промежутки времени.
    """
    def __init__(self, filename, x, y, FPS, *groups):
        """
        :param FPS: FPS игры. Нужен, чтобы рассчитать время self.t бомбы для ее плавного движения по экрану.
        """
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
        Падает с ускорением g и начальной скоростью 0.
        """
        self.y += -self.vy * self.t + self.g*(self.t**2)/2
        self.vy -= self.g * self.t

    def draw(self, screen):
        """
        Отрисовка бомбы. При движении время жизни пули self.live уменьшается.
        """
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.image.get_rect(center=(self.x, self.y)))
        if self.live > 0:
            self.live -= 1
        else:
            self.kill()
