import math
from random import choice, randint
import pygame
from pygame.draw import rect
from pygame.image import load

FPS = 30

RED = 0xFF0000
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


class Ball:
    def __init__(self, x=40, y=450, g=2):
        """
        Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 15
        self.vx = 0
        self.vy = 0
        self.g = g
        self.color = choice(GAME_COLORS)
        self.live = 30
        self.t = 15/FPS

    def norm(self):
        self.x += self.vx * self.t
        self.y += -self.vy * self.t + self.g*(self.t**2)/2
        self.vy -= self.g * self.t

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        self.norm()
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

    def draw(self):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        # FIXME
        if type(obj) == Target:
            a = obj.x
            b = obj.y
            if (a-self.x)**2+(b-self.y)**2 <= (self.r+obj.r)**2:
                return True
            else:
                return False


class Gun:
    def __init__(self):
        """
        :param self.color: Цвет пушки
        """
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        gun_image = load('vacuum gun.png')
        self.image = gun_image
        self.rect = self.image.get_


    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_ball = Ball()
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10
        return new_ball

    def targetting(self, event):
        """
        Прицеливание. Зависит от положения мыши.
        Изменяет только расположение пушки в зависимости от положения мыши
        """
        if event:
            try:
                self.an = math.atan((event.pos[1]-450) / (event.pos[0]-40))
            except ZeroDivisionError:
                pass
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        self.image.fill(WHITE)
        rect(self.image, self.color, (1, 0, 10 + self.f2_power, 10))
        image = pygame.transform.rotate(self.image, math.degrees(-self.an))
        screen.blit(image, (30, 450))

        # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 3
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self):
        """ Инициализация новой цели. """
        self.points = 0
        self.live = 1
        self.x = randint(550, 700)
        self.y = randint(300, 500)
        self.r = randint(5, 50)
        self.color = RED
        # FIXME: don't work!!! How to call this functions when object is created?

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)


class Game:
    def __init__(self):
        self.bullet = 0
        self.balls = []
        self.gun = Gun()
        self.target = Target()

    def mainloop(self):
        clock = pygame.time.Clock()
        finished = False

        while not finished:
            screen.fill(WHITE)
            self.gun.draw()
            self.target.draw()
            for b in self.balls:
                b.draw()
            pygame.display.update()

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.gun.fire2_start()
                elif event.type == pygame.MOUSEBUTTONUP:
                    new_ball = self.gun.fire2_end(event)
                    self.bullet += 1
                    self.balls.append(new_ball)
                elif event.type == pygame.MOUSEMOTION:
                    self.gun.targetting(event)

            for b in self.balls:
                b.move()
                if b.hittest(self.target) and self.target.live:
                    self.target.live = 0
                    self.target.hit()
                    self.target = Target()

            self.gun.power_up()

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
