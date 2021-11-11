import pygame
from pygame.image import load
import tanks
import bullet
import targets


FPS = 30
WHITE = 0xFFFFFF
RED = (255, 0, 0)
background = load('XXXL.jpg')
wizard = load('C__fakepath_400px-Колдунов_Леонид_Модестович.png')
wizard.set_colorkey((255, 255, 255))
WIDTH = 800
HEIGHT = 600


class Game:
    """
    Сама игра.
    """
    def __init__(self):
        self.font2 = pygame.font.Font(None, 100)
        self.end_text = self.font2.render('ИДИ БОТАЙ', True, RED)
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
        self.score = 0
        self.count = str(self.score)
        self.score_text = self.font2.render(self.count, True, RED)
        self.f1 = pygame.font.Font(None, 36)
        self.tank1 = self.f1.render('Танк 1:', True, 'green3')

    def make_text(self):
        """
        Текст,который появляетсяво время игрового процесса.
        """
        screen.blit(self.text1, (10, 10))
        screen.blit(self.f1.render(self.count, True, 'black'), (84, 10))
        screen.blit(self.tank1, (300, 10))
        screen.blit(self.f1.render(str(self.tank.live), True, 'green3'), (390, 10))

    def manual(self):
        """
        Инструкция
        """
        introduction = self.f1.render('В этой игре вам предстоит сбивать цели с помощью танка', True, 'black')
        screen.blit(introduction, (20, 20))
        introduction = self.f1.render('У  танка 50 жизней, уклоняйтесь от падающих бомб', True, 'black')
        screen.blit(introduction, (20, 50))
        introduction = self.f1.render('Управление:', True, 'black')
        screen.blit(introduction, (20, 80))
        introduction = self.f1.render('Стрелки вправо и влево - движение танков, их можно зажимать', True, 'black')
        screen.blit(introduction, (20, 110))
        introduction = self.f1.render('Space - огонь, можно зажимать для увеличения', True, 'black')
        screen.blit(introduction, (20, 200))
        introduction = self.f1.render('мощности выстрела', True, 'black')
        screen.blit(introduction, (20, 230))
        introduction = self.f1.render('Для начала игры нажмите крестик', True, 'black')
        screen.blit(introduction, (20, 300))

    def manual_window(self):
        """
        Окно синструкцией
        """
        finished = False
        clock = pygame.time.Clock()
        while not finished:
            screen.fill(WHITE)
            self.manual()
            pygame.display.update()
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True

    def mainloop(self):
        """
        Запуск игры
        """
        clock = pygame.time.Clock()
        finished = False

        while not finished:
            screen.fill(WHITE)
            self.count = str(self.score)
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
            self.make_text()

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
                self.tank.gun.gun_turn('K_x', screen, self.tank.get_center_x(), self.tank.get_center_y())
            if keys[pygame.K_z]:
                self.tank.gun.gun_turn('K_z', screen, self.tank.get_center_x(), self.tank.get_center_y())
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
            if self.tank.live <= 0:
                finished = True
            self.score_text = self.font2.render("Очков: " + self.count, True, RED)

        print(self.score)
        print(self.tank.live)

    def end_window(self):
        """
        Окно конца игры
        """
        finished = False
        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
            screen.fill(WHITE)
            screen.blit(background, (0, 0))
            screen.blit(wizard, (500, 300))
            screen.blit(self.end_text, (100, 100))
            screen.blit(self.score_text, (100, 300))

            pygame.display.flip()

        pygame.quit()


def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    game = Game()
    game.manual_window()
    game.mainloop()
    game.end_window()


if __name__ == '__main__':
    screen = None
    main()
