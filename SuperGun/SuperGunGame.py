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
        self.tank1 = tanks.Tank('tanks_tankGreen_body3.png')
        self.tank2 = tanks.Tank('tanks_tankGreen_body3.png', center=(700, 500))
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
        self.text1 = self.f1.render('Очки:', True, 'black')
        self.text_tank1 = self.f1.render('Танк 1:', True, 'green3')
        self.text_tank2 = self.f1.render('Танк 2:', True, 'green3')

    def make_text(self):
        """
        Текст, который появляетсяво время игрового процесса.
        """
        screen.blit(self.text1, (10, 10))
        screen.blit(self.f1.render(self.count, True, 'black'), (84, 10))
        screen.blit(self.text_tank1, (270, 10))
        screen.blit(self.text_tank2, (410, 10))
        screen.blit(self.f1.render(str(self.tank1.live), True, 'green3'), (360, 10))
        screen.blit(self.f1.render(str(self.tank2.live), True, 'green3'), (500, 10))

    def manual(self):
        """
        Инструкция
        """
        introduction = self.f1.render('В этой игре вам предстоит сбивать цели с помощью 2 танков.', True, 'black')
        screen.blit(introduction, (20, 20))
        introduction = self.f1.render('У каждого танка 50 жизней, уклоняйтесь от падающих бомб.', True, 'black')
        screen.blit(introduction, (20, 50))
        introduction = self.f1.render('Управление:', True, 'black')
        screen.blit(introduction, (20, 80))
        introduction = self.f1.render('Стрелки вправо и влево - движение первого танка,', True, 'black')
        screen.blit(introduction, (20, 110))
        introduction = self.f1.render('клавиши X и C - второго, их можно зажимать', True, 'black')
        screen.blit(introduction, (20, 140))
        introduction = self.f1.render('Клавиши < и > - управление башней первого танка', True, 'black')
        screen.blit(introduction, (20, 170))
        introduction = self.f1.render('клавиши W и S - второго, их можно зажимать.', True, 'black')
        screen.blit(introduction, (20, 200))
        introduction = self.f1.render('Огонь: Space - первый танк, Q - второй танк,', True, 'black')
        screen.blit(introduction, (20, 230))
        introduction = self.f1.render('можно зажимать для увеличения мощности выстрела.', True, 'black')
        screen.blit(introduction, (20, 260))
        introduction = self.f1.render('Для начала игры нажмите крестик.', True, 'black')
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

    def hit_bullets(self, group, class_group):
        """
        Проверка столкновений пули.
        """
        hits = pygame.sprite.groupcollide(group, self.bullets, True, True, pygame.sprite.collide_circle)
        if class_group == "Coin":
            for _ in hits:
                c = targets.Coin('star coin 1.png')
                self.targets.add(c)
                self.score += 5
        if class_group == "Airplane":
            for _ in hits:
                a = targets.Airplane('airplan_r.png')
                self.airplanes.add(a)
                self.score += 10

    def draw(self):
        """
        Отрисовка всего.
        """
        screen.fill(WHITE)
        self.count = str(self.score)
        self.tank1.draw(screen)
        self.tank2.draw(screen)
        for b in self.bullets:
            b.draw(screen)
        for t in self.targets:
            t.draw(screen)
        for a in self.airplanes:
            a.draw(screen)
            if a.t == 10:
                bomb = targets.Bomb('bomb.png', a.rect.x + 110, a.rect.y + 60, FPS)
                self.bombs.add(bomb)
        for bomb in self.bombs:
            bomb.draw(screen)

        self.score_text = self.font2.render("Очков: " + self.count, True, RED)
        self.make_text()

    def process_events(self):
        """
        Обработка событий.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.tank1.gun.fire2_start()
                if event.key == pygame.K_q:
                    self.tank2.gun.fire2_start()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    new_bullet = self.tank1.gun.fire2_end()
                    self.bullets.add(new_bullet)
                if event.key == pygame.K_q:
                    new_bullet = self.tank2.gun.fire2_end()
                    self.bullets.add(new_bullet)
        keys = pygame.key.get_pressed()
        self.tank1_process(keys)
        self.tank2_process(keys)

    def tank1_process(self, keys):
        """
        Обработка событий первого танка.
        """
        if keys[pygame.K_COMMA]:
            self.tank1.gun.gun_turn('left', screen, self.tank1.get_center_x(), self.tank1.get_center_y())
        if keys[pygame.K_PERIOD]:
            self.tank1.gun.gun_turn('right', screen, self.tank1.get_center_x(), self.tank1.get_center_y())
        if keys[pygame.K_LEFT]:
            self.tank1.move_l()
        if keys[pygame.K_RIGHT]:
            self.tank1.move_r()

    def tank2_process(self, keys):
        """
        Обработка событий второго танка.
        """
        if keys[pygame.K_x]:
            self.tank2.gun.gun_turn('left', screen, self.tank2.get_center_x(), self.tank2.get_center_y())
        if keys[pygame.K_c]:
            self.tank2.gun.gun_turn('right', screen, self.tank2.get_center_x(), self.tank2.get_center_y())
        if keys[pygame.K_w]:
            self.tank2.move_l()
        if keys[pygame.K_s]:
            self.tank2.move_r()

    def move(self):
        """
        Движение автообЪектов.
        """
        for b in self.bullets:
            b.move()
        for a in self.airplanes:
            a.move()
        for bomb in self.bombs:
            bomb.move()

    def hit_tanks(self):
        """
        Столкновение танков с обЪектами.
        """
        for tank in self.tank1, self.tank2:
            hits = pygame.sprite.spritecollide(tank, self.bombs, True)
            if hits:
                tank.live -= 1
            if tank.live <= 0:
                return True

    def hit(self):
        """
        Проверка всех столкновений.
        """
        self.hit_bullets(self.airplanes, "Airplane")
        self.hit_bullets(self.targets, "Coin")
        pygame.sprite.groupcollide(self.bombs, self.bullets, True, True)
        if self.hit_tanks():
            return True

    def mainloop(self):
        """
        Запуск игры
        """
        clock = pygame.time.Clock()
        finished = False
        while not finished:
            self.draw()
            pygame.display.update()
            clock.tick(FPS)
            if self.process_events():
                finished = True
            self.move()
            self.tank1.gun.power_up()
            self.tank2.gun.power_up()
            if self.hit():
                finished = True

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
