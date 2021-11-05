import math
from random import choice, randint
import pygame
from pygame.draw import rect
from pygame.image import load
from pygame.color import update
import tanks
import bullet
import targets


FPS = 30
RED = (255, 0, 0, 0)
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


class Game:
    def __init__(self):
        self.score = 0
        self.tank = tanks.Tank('tanks_tankGreen_body3.png')
        self.airplane = targets.Airplane('airplan_r.png')
        self.bullets = pygame.sprite.Group()
        self.targets = pygame.sprite.Group()
        self.airplanes = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.airplanes.add(self.airplane)
        for _ in range(5):
            t = targets.Coin('star coin 1.png')
            self.targets.add(t)

    def mainloop(self):
        clock = pygame.time.Clock()
        finished = False

        while not finished:
            screen.fill(WHITE)
            self.tank.draw(screen)
            for b in self.bullets:
                b.draw(screen)
            for t in self.targets:
                t.draw(screen)
            for a in self.airplanes:
                a.draw(screen)
                if a.t == 10:
                    bomb = targets.Bomb('bomb.png', a.rect.x+110, a.rect.y+60, FPS)
                    self.bombs.add(bomb)
            for bomb in self.bombs:
                bomb.draw(screen)

            pygame.display.update()
            keys = pygame.key.get_pressed()

            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.tank.gun.fire2_start()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        new_bullet = self.tank.gun.fire2_end()
                        self.bullets.add(new_bullet)

            if keys[pygame.K_x]:
                self.tank.gun.gun_turn('K_x', screen, self.tank.x, self.tank.y)
            if keys[pygame.K_z]:
                self.tank.gun.gun_turn('K_z', screen, self.tank.x, self.tank.y)
            if keys[pygame.K_LEFT]:
                self.tank.move_l()
            if keys[pygame.K_RIGHT]:
                self.tank.move_r()
            for b in self.bullets:
                b.move()
            for a in self.airplanes:
                a.move()
            for bomb in self.bombs:
                bomb.move()
            self.tank.gun.power_up()

            hits = pygame.sprite.groupcollide(self.targets, self.bullets, True, True, pygame.sprite.collide_circle)
            for _ in hits:
                c = targets.Coin('star coin 1.png')
                self.targets.add(c)
                self.score += 5
            hits = pygame.sprite.groupcollide(self.airplanes, self.bullets, True, True)
            for _ in hits:
                a = targets.Airplane('airplan_r.png')
                self.airplanes.add(a)
                self.score += 10
            pygame.sprite.groupcollide(self.bombs, self.bullets, True, True)
            hits = pygame.sprite.spritecollide(self.tank, self.bombs, True)
            if hits:
                self.tank.live -= 1

        print(self.score)
        print(self.tank.live)

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
