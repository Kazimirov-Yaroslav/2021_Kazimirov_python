import pygame
from pygame.image import load


class Target(pygame.sprite.Sprite):
    """
    Если попасть пулей, уничтожится
    """

    def destroy(self):
        """
        При попадании разрушается
        """

        pass

    def move(self):
        """
        Движение целей
        """
        pass


class HealTarget(Target):
    """
    Хилит при попадании
    """
    def move(self):
        """
        Двигается по горизонтали
        """
        pass


class Airplane(Target):
    """
    Кидает бомбы
    """
    pass


class Coin(Target):
    """
    Дает очки
    """
    def __init__(self, filename, *groups):
        super().__init__(*groups)
        self.image = load(filename)
        self.rect = self.image.get_rect()
        self.radius = 15
        self.rect.x = random.randint(100, 1140)
        self.rect.y = random.randint(100, 650)
        self.rect.center = (self.rect.x, self.rect.y)
        pass


class Bomb(pygame.sprite.Sprite):
    """
    Наносит урон при попадании
    """
    def move(self):
        """
        Падает с ускорением g
        """
        pass
