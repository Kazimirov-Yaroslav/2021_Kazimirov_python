import pygame
from pygame.image import load

WHITE = 0xFFFFFF


class Bullet(pygame.sprite.Sprite):
    """
    Класс пули. Появляется у края дула пушки при выстреле.
    """
    def __init__(self, filename, x, y, FPS, *groups):
        """
        Скорость задается пушкой, т.е. силой выстрела, поэтому начальная скорость равна нулю при создании. Радиус
        необходим для фиксации столкновения спрайтов пулии целей.
        self.live - время жизни пули, чтобы уничтожалась, а не лежала на полу при неудачном выстреле.
        :param FPS: FPS игры. Нужен, чтобы рассчитать время self.t пули для ее плавного движения по экрану.
        """
        super().__init__(*groups)
        self.image = load(filename)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        self.vy = 0
        self.vx = 0
        self.g = 2
        self.t = 15/FPS
        self.radius = 10
        self.live = 100

    def draw(self, screen):
        """
        Отрисовка пули. При движении время жизни пули self.live уменьшается.
        """
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.image.get_rect(center=(self.x, self.y)))
        if self.live > 0:
            self.live -= 1
        else:
            self.kill()

    def default_move(self):
        """
        Движение без ограничений.
        """
        self.x += self.vx * self.t
        self.y += -self.vy * self.t + self.g*(self.t**2)/2
        self.vy -= self.g * self.t

    def move(self):
        """
        Переместить пулю по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        Ограничение на стенки, уменьшение энергии при столкновении со стенкой и полом.
        """

        self.default_move()
        if self.y < -80:
            self.kill()
        if self.y >= 580:
            self.y = 580
            self.vy = -0.6 * self.vy
            self.vx = 0.9 * self.vx
            if abs(self.vy) < 1.5:
                self.vy = 0
                self.t = 0

        if self.x >= 800:
            self.x = 800
            self.vx = -0.7 * self.vx
            self.vy = 0.9 * self.vy

        if self.x <= 0:
            self.x = 0
            self.vx = -0.7 * self.vx
            self.vy = 0.9 * self.vy
