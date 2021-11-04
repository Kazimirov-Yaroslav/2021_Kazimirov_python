import pygame
from pygame.image import load

WHITE = 0xFFFFFF


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

    def fire2_start(self):
        self.f2_on = 1

    def pos_gun(self):
        return self.image.midright

    def fire2_end(self, event):
        """
        Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        new_bullet = Bullet()
        self.angel = math.atan2((pos_gun[1]-new_bullet.y), (pos_gun[0]-new_bullet.x))
        new_bullet.vx = self.f2_power * math.cos(self.an)
        new_bullet.vy = - self.f2_power * math.sin(self.an)
        self.f2_on = 0
        self.f2_power = 10
        return new_bullet

    def targetting(self, key):
        """
        Прицеливание.
        """
        if key == 'K_z':
            self.angel += 5
        if key == 'K_x':
            self.angel -= 5
        return True

    def draw(self):
        if self.f2_on:
            fill(self.image, RED, self.f2_power)
        else:
            self.image = load('vacuum gun.png')
        image = pygame.transform.rotate(self.image, math.degrees(-self.an))
        screen.blit(image, (30, 450))

        # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 3


class Tank(pygame.sprite.Sprite):
    def __init__(self, filename, *groups):
        super().__init__(*groups)
        self.image = load(filename)
        self.x = 100
        self.y = 500
        self.rect = self.image.get_rect(center=(self.x, self.y))

        self.gun = Gun('vacuum gun.png')
        self.gun.image = pygame.transform.rotate(self.gun.image, 90)
        self.gun.rect = self.gun.image.get_rect(center=(self.x+85, self.y+5))

    def move_r(self):
        self.x += 5

    def move_l(self):
        self.x -= 5

    def gun_turn(self, key, screen):
        if self.gun.targetting(key):
            self.gun.image = load('vacuum gun.png')
            self.gun.image.set_colorkey(WHITE)
            self.gun.image = pygame.transform.rotate(self.gun.image, self.gun.angel)
            self.gun.rect = self.gun.image.get_rect(center=(self.x+85, self.y+5))
            screen.blit(self.gun.image, self.gun.rect)

    def draw(self, screen):
        screen.blit(self.gun.image, self.gun.image.get_rect(center=(self.x+85, self.y+5)))
        screen.blit(self.image, (self.x, self.y))








